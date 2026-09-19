#!/usr/bin/env python3
# Author: Victor.I
"""Convert research monographs from Markdown to print-ready HTML, then PDF via Chrome."""

from __future__ import annotations

import html
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PDF_DIR = ROOT / "pdfs"
HTML_DIR = ROOT / "html"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

PAPERS = [
    ("product-design/human-factors-c2-monograph.md", "01-product-design-human-factors.pdf"),
    ("software-engineering/event-driven-c2-software-monograph.md", "02-software-engineering.pdf"),
    ("ai-engineering/hitl-ai-decision-support-monograph.md", "03-ai-engineering.pdf"),
    ("ml-engineering/detection-tracking-fusion-monograph.md", "04-ml-engineering.pdf"),
    ("data-engineering/heterogeneous-sensor-data-platform-monograph.md", "05-data-engineering.pdf"),
    ("data-science/swarm-behaviour-risk-analytics-monograph.md", "06-data-science.pdf"),
    ("security-governance/secure-governed-cuas-software-monograph.md", "07-security-governance.pdf"),
    ("systems-engineering/counter-swarm-systems-integration-monograph.md", "08-systems-engineering.pdf"),
]

CSS = """
@page { size: A4; margin: 18mm 16mm; }
body {
  font-family: "IBM Plex Serif", "Source Serif 4", "Georgia", serif;
  font-size: 11pt;
  line-height: 1.45;
  color: #111;
  max-width: 780px;
  margin: 0 auto;
  padding: 24px;
}
h1 { font-size: 20pt; page-break-before: avoid; margin-top: 0; }
h2 { font-size: 14pt; margin-top: 1.6em; border-bottom: 1px solid #ccc; padding-bottom: 0.2em; page-break-after: avoid; }
h3 { font-size: 12pt; margin-top: 1.2em; page-break-after: avoid; }
h4 { font-size: 11pt; margin-top: 1em; }
p, li { orphans: 3; widows: 3; }
code, pre {
  font-family: "IBM Plex Mono", "SF Mono", Menlo, monospace;
  font-size: 9pt;
}
pre {
  background: #f4f4f4;
  border: 1px solid #ddd;
  padding: 10px;
  overflow-x: auto;
  white-space: pre-wrap;
  page-break-inside: avoid;
}
table {
  border-collapse: collapse;
  width: 100%;
  font-size: 9.5pt;
  margin: 1em 0;
  page-break-inside: avoid;
}
th, td { border: 1px solid #bbb; padding: 4px 6px; vertical-align: top; text-align: left; }
th { background: #eee; }
blockquote {
  margin: 1em 0;
  padding-left: 1em;
  border-left: 3px solid #888;
  color: #333;
}
.meta { color: #555; font-size: 10pt; margin-bottom: 2em; }
hr { border: none; border-top: 1px solid #ccc; margin: 2em 0; }
a { color: #0645ad; text-decoration: none; }
"""


def inline_format(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def md_to_html(md: str, title: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    in_code = False
    code_buf: list[str] = []
    in_ul = False
    in_ol = False
    in_table = False
    table_rows: list[str] = []

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def flush_table() -> None:
        nonlocal in_table, table_rows
        if not table_rows:
            return
        out.append("<table>")
        for ri, row in enumerate(table_rows):
            if re.match(r"^\s*\|?\s*:?-{3,}", row):
                continue
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            tag = "th" if ri == 0 else "td"
            out.append("<tr>" + "".join(f"<{tag}>{inline_format(c)}</{tag}>" for c in cells) + "</tr>")
        out.append("</table>")
        table_rows = []
        in_table = False

    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            close_lists()
            flush_table()
            if not in_code:
                in_code = True
                code_buf = []
            else:
                out.append("<pre><code>" + html.escape("\n".join(code_buf)) + "</code></pre>")
                in_code = False
            i += 1
            continue
        if in_code:
            code_buf.append(line)
            i += 1
            continue

        if line.strip().startswith("|"):
            close_lists()
            in_table = True
            table_rows.append(line)
            i += 1
            continue
        elif in_table:
            flush_table()

        if not line.strip():
            close_lists()
            i += 1
            continue

        if line.startswith("# "):
            close_lists()
            out.append(f"<h1>{inline_format(line[2:].strip())}</h1>")
        elif line.startswith("## "):
            close_lists()
            out.append(f"<h2>{inline_format(line[3:].strip())}</h2>")
        elif line.startswith("### "):
            close_lists()
            out.append(f"<h3>{inline_format(line[4:].strip())}</h3>")
        elif line.startswith("#### "):
            close_lists()
            out.append(f"<h4>{inline_format(line[5:].strip())}</h4>")
        elif line.startswith("---") and set(line.strip()) <= {"-"}:
            close_lists()
            out.append("<hr/>")
        elif line.startswith("> "):
            close_lists()
            out.append(f"<blockquote><p>{inline_format(line[2:].strip())}</p></blockquote>")
        elif re.match(r"^[-*] ", line):
            if in_ol:
                out.append("</ol>")
                in_ol = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline_format(re.sub(r'^[-*] ', '', line))}</li>")
        elif re.match(r"^\d+\. ", line):
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{inline_format(re.sub(r'^\d+\. ', '', line))}</li>")
        elif line.startswith("<!--"):
            pass
        else:
            close_lists()
            out.append(f"<p>{inline_format(line)}</p>")
        i += 1

    close_lists()
    flush_table()

    body = "\n".join(out)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<!-- Author: Victor.I -->
<title>{html.escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
<p class="meta">Counter-Swarm Defence Platform · Research monograph · Author: Victor.I · Defensive decision-support scope only</p>
{body}
</body>
</html>
"""


def chrome_pdf(html_path: Path, pdf_path: Path) -> None:
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--allow-file-access-from-files",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=120000",
        f"--print-to-pdf={pdf_path}",
        html_path.as_uri(),
    ]
    subprocess.run(cmd, check=True, capture_output=True, text=True)


def main() -> None:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    HTML_DIR.mkdir(parents=True, exist_ok=True)
    for rel, pdf_name in PAPERS:
        md_path = ROOT / rel
        text = md_path.read_text(encoding="utf-8")
        # title from first H1
        title = pdf_name
        for line in text.splitlines():
            if line.startswith("# "):
                title = line[2:].strip()
                break
        html_doc = md_to_html(text, title)
        html_path = HTML_DIR / (Path(pdf_name).stem + ".html")
        html_path.write_text(html_doc, encoding="utf-8")
        pdf_path = PDF_DIR / pdf_name
        print(f"Rendering {pdf_name} ...")
        chrome_pdf(html_path, pdf_path)
        print(f"  wrote {pdf_path} ({pdf_path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
