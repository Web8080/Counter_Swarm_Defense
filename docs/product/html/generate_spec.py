#!/usr/bin/env python3
# Author: Victor.I
"""Generate the Counter-Swarm Defence UI/UX & Workflow Specification HTML (~100 pages)."""

from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "html" / "ui-ux-workflow-specification.html"

CSS = r"""
@page { size: A4 landscape; margin: 10mm; }
:root {
  --bg:#0B1014; --elev:#121A21; --grid:#1A2430; --text:#E6EEF4; --muted:#9AA8B5;
  --dim:#6B7A88; --accent:#2BB3A3; --t3:#E85D4C; --t2:#E2A93B; --t1:#3C8FBF;
  --ok:#3FAE7F; --down:#D35D5D; --infer:#D0B15A; --pred:#6FA8C9; --border:#243140;
  --sans:"IBM Plex Sans","Source Sans 3","Segoe UI",sans-serif;
  --mono:"IBM Plex Mono","SF Mono",Menlo,monospace;
}
*{box-sizing:border-box}
body{margin:0;font-family:var(--sans);background:#111;color:var(--text);font-size:13px}
.page{width:1100px;min-height:700px;margin:18px auto;background:var(--bg);border:1px solid #2a2a2a;
  page-break-after:always;break-after:page;position:relative;overflow:hidden}
.page:last-child{page-break-after:auto}
.hdr{display:flex;justify-content:space-between;align-items:center;padding:8px 14px;
  border-bottom:1px solid var(--border);background:#0E1419;font-size:11px;color:var(--muted)}
.hdr strong{color:var(--text);letter-spacing:.03em}
.pg{font-family:var(--mono);color:var(--dim)}
.badge{display:inline-block;padding:2px 7px;border-radius:2px;font-size:9px;font-weight:650;
  letter-spacing:.07em;text-transform:uppercase;border:1px solid}
.badge.p0{color:var(--t3);border-color:var(--t3);background:#2a1412}
.badge.p1{color:var(--t2);border-color:var(--t2);background:#2a2410}
.badge.p2{color:var(--t1);border-color:var(--t1);background:#102030}
.badge.lab{color:var(--t2);border-color:var(--t2);background:#2a2410}
.badge.scr{color:var(--accent);border-color:var(--accent);background:#0f2421}
.badge.wf{color:#c9a0e8;border-color:#7a5a9a;background:#1a1222}
.pad{padding:22px 28px}
h1{font-size:36px;margin:0 0 10px;font-weight:650}
h2{font-size:20px;margin:0 0 8px;font-weight:650}
h3{font-size:14px;margin:0 0 8px;letter-spacing:.06em;text-transform:uppercase;color:var(--dim)}
.sub{color:var(--muted);line-height:1.5;max-width:780px}
.foot{margin-top:28px;font-size:11px;color:var(--dim)}
.cover{min-height:700px;display:flex;flex-direction:column;justify-content:center;padding:56px;
  background:radial-gradient(ellipse at 15% 25%,rgba(43,179,163,.14),transparent 50%),
  radial-gradient(ellipse at 85% 75%,rgba(226,169,59,.08),transparent 45%),var(--bg)}
.toc a{color:var(--accent);text-decoration:none}
.toc table,.spec table{width:100%;border-collapse:collapse;font-size:12px}
.toc td,.toc th,.spec td,.spec th{padding:6px 8px;border-bottom:1px solid var(--border);text-align:left;vertical-align:top}
.toc th,.spec th{color:var(--dim);font-size:10px;letter-spacing:.06em;text-transform:uppercase}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.cols3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
.card{background:var(--elev);border:1px solid var(--border);padding:12px 14px;border-radius:2px}
.card h4{margin:0 0 6px;font-size:13px}
.card p{margin:0;color:var(--muted);font-size:12px;line-height:1.45}
.flow{display:flex;align-items:stretch;gap:6px;flex-wrap:wrap;margin:12px 0}
.flow .box{flex:1;min-width:100px;background:var(--elev);border:1px solid var(--border);padding:10px;font-size:11px}
.flow .box b{display:block;color:var(--accent);font-size:10px;letter-spacing:.06em;margin-bottom:4px}
.flow .arr{display:flex;align-items:center;color:var(--dim);font-size:16px}
.shell{display:flex;justify-content:space-between;padding:7px 12px;background:var(--elev);
  border-bottom:1px solid var(--border);font-size:12px}
.brand{font-weight:650;color:var(--accent)}
.pills span{display:inline-block;margin-left:6px;padding:2px 7px;border:1px solid var(--border);
  border-radius:2px;font-size:10px;color:var(--muted)}
.pills .ok{color:var(--ok);border-color:#2a5a45}
.pills .warn{color:var(--t2);border-color:#6a5220}
.pills .bad{color:var(--down);border-color:#6a3030}
.banner{font-size:11px;padding:5px 12px;border-bottom:1px solid #5a4a20;background:#2a2410;color:var(--t2)}
.banner.bad{background:#2a1514;border-color:#5a3030;color:#F5C4BE}
.banner.info{background:#102030;border-color:#2a4a60;color:var(--t1)}
.layout{display:grid;grid-template-columns:190px 1fr 250px;grid-template-rows:1fr 130px;height:560px}
.layout2{display:grid;grid-template-columns:1.15fr .85fr;height:560px}
.layout-mid{display:grid;grid-template-columns:1fr 340px;height:560px}
.map{position:relative;background:linear-gradient(rgba(26,36,48,.92),rgba(26,36,48,.92)),
  repeating-linear-gradient(0deg,transparent,transparent 39px,#1f2b38 40px),
  repeating-linear-gradient(90deg,transparent,transparent 39px,#1f2b38 40px);
  border-right:1px solid var(--border);border-bottom:1px solid var(--border)}
.map .ml{position:absolute;top:8px;left:8px;font-size:10px;color:var(--dim)}
.hatch{position:absolute;background:repeating-linear-gradient(-45deg,rgba(139,123,184,.16),
  rgba(139,123,184,.16) 6px,transparent 6px,transparent 12px);
  border:1px dashed rgba(139,123,184,.5)}
.hatch span{position:absolute;bottom:4px;left:6px;font-size:9px;color:#b5a8d8}
.geofence{position:absolute;border:1px solid rgba(226,169,59,.4);border-radius:50% 42% 55% 45%}
.trk{position:absolute;width:9px;height:9px;border-radius:50%;background:#D7E2EA;box-shadow:0 0 0 1px #000}
.trk.sel{background:var(--accent);width:11px;height:11px}
.tt{position:absolute;font-family:var(--mono);font-size:9px;background:rgba(0,0,0,.55);padding:1px 4px;border-radius:2px}
.ell{position:absolute;border:1px dashed rgba(43,179,163,.5);border-radius:50%;background:rgba(43,179,163,.1)}
.panel{background:var(--elev);border-bottom:1px solid var(--border);border-left:1px solid var(--border);padding:8px;overflow:hidden}
.panel h3{font-size:10px;margin:0 0 6px}
.row{display:flex;justify-content:space-between;gap:6px;padding:5px 6px;margin-bottom:3px;
  border:1px solid var(--border);border-radius:2px;font-size:11px}
.row.active{border-color:var(--accent);background:#0f2421}
.tier{font-weight:650;font-size:9px;padding:1px 4px;border-radius:2px}
.tier.t3{background:#3A1816;color:var(--t3)}.tier.t2{background:#3A2F12;color:var(--t2)}
.tier.t1{background:#123040;color:var(--t1)}.tier.t0{background:#1a2228;color:var(--dim)}
.dock{grid-column:1/-1;background:#0E1419;border-top:1px solid var(--border);padding:7px 10px}
.tabs{font-size:10px;color:var(--dim);margin-bottom:4px}.tabs b{color:var(--accent)}
.timeline{font-family:var(--mono);font-size:10px;color:var(--muted)}
.epi .band{border-left:3px solid var(--dim);padding:5px 7px;background:#0E1419;font-size:11px;margin-bottom:5px}
.epi .obs{border-color:var(--muted)}.epi .inf{border-color:var(--infer)}
.epi .pred{border-color:var(--pred)}.epi .rec{border-color:var(--accent)}.epi .dec{border-color:var(--text)}
.epi .k{font-size:8px;letter-spacing:.1em;color:var(--dim);margin-bottom:2px}
.btn{display:inline-block;padding:6px 10px;font-size:11px;border-radius:2px;border:1px solid var(--border);
  background:#1a2530;color:var(--text);margin:2px 4px 2px 0}
.btn.primary{background:var(--accent);color:#06221F;border-color:var(--accent);font-weight:650}
.btn.ghost{background:transparent}.btn:disabled,.btn.dis{opacity:.35}
.notice{margin-top:8px;padding:7px;border:1px solid #5a3030;background:#2a1514;color:#F5C4BE;font-size:10px}
.callout{border:1px solid var(--border);background:var(--elev);padding:10px 12px;margin-top:10px;font-size:12px;color:var(--muted)}
.callout b{color:var(--text)}
.anno{position:absolute;font-size:10px;color:var(--t2);background:rgba(42,36,16,.9);border:1px solid var(--t2);
  padding:3px 6px;border-radius:2px;max-width:160px;z-index:5}
.step{display:flex;gap:12px;margin:8px 0}
.step .n{flex:0 0 36px;height:36px;border-radius:50%;background:#0f2421;border:1px solid var(--accent);
  display:flex;align-items:center;justify-content:center;font-weight:650;color:var(--accent)}
.step .b{flex:1}
.bar{height:7px;background:#1a2530;border-radius:2px;overflow:hidden;margin-top:3px}
.bar>span{display:block;height:100%;background:var(--infer)}
.skel{background:linear-gradient(90deg,#152028,#1c2a35,#152028);background-size:200% 100%;
  border-radius:2px;height:14px;margin:6px 0}
.modal-wrap{display:flex;align-items:center;justify-content:center;height:560px;background:rgba(0,0,0,.4)}
.modal{width:460px;background:var(--elev);border:1px solid var(--border);padding:18px}
.list li{margin:4px 0;color:var(--muted)}
.kv{display:grid;grid-template-columns:140px 1fr;gap:4px 10px;font-size:12px}
.kv .k{color:var(--dim)}.kv .v{color:var(--text)}
.comp{display:inline-flex;align-items:center;gap:6px;padding:6px 8px;border:1px solid var(--border);
  background:var(--elev);margin:3px;font-size:11px}
@media print{body{background:#fff}.page{margin:0;border:none;width:auto}}
"""

pages: list[str] = []
page_no = 0


def add(html: str, title: str = "", badges: str = "") -> None:
    global page_no
    page_no += 1
    pages.append(
        f'<section class="page" id="p{page_no}">'
        f'<div class="hdr"><div><strong>{title}</strong> {badges}</div>'
        f'<div class="pg">p.{page_no:03d}</div></div>{html}</section>'
    )


def badges(*items: str) -> str:
    out = []
    for i in items:
        cls = "scr"
        if i.startswith("P0"):
            cls = "p0"
        elif i.startswith("P1"):
            cls = "p1"
        elif i.startswith("P2"):
            cls = "p2"
        elif i == "LAB":
            cls = "lab"
        elif i.startswith("WF") or i == "WORKFLOW":
            cls = "wf"
        out.append(f'<span class="badge {cls}">{i}</span>')
    return " ".join(out)


def shell(left: str, pills: str = "") -> str:
    return f'<div class="shell"><div>{left}</div><div class="pills">{pills}</div></div>'


def map_canvas(extra: str = "", label: str = "MAP") -> str:
    return f"""<div class="map"><div class="ml">{label}</div>
    <div class="geofence" style="left:110px;top:80px;width:280px;height:200px"></div>
    <div class="hatch" style="right:30px;top:50px;width:150px;height:120px"><span>RF hole</span></div>
    <div class="ell" style="left:300px;top:170px;width:70px;height:46px"></div>
    <div class="trk sel" style="left:326px;top:184px"></div>
    <div class="tt" style="left:340px;top:168px">T-104</div>
    <div class="trk" style="left:360px;top:210px"></div>
    <div class="tt" style="left:372px;top:204px;color:#9AA8B5">T-105</div>
    <div class="trk" style="left:230px;top:140px"></div>
    <div class="tt" style="left:242px;top:130px;color:#9AA8B5">T-091</div>
    {extra}</div>"""


# ── Cover & front matter ──────────────────────────────────────────
add(
    """<div class="cover">
    <div class="badge scr">STAGE 0 · DESIGN SPECIFICATION</div>
    <h1>Counter-Swarm Defence</h1>
    <h2 style="font-weight:400;color:var(--muted);margin-bottom:18px">UI/UX Screens, Workflows &amp; Simulation Specification</h2>
    <p class="sub">Complete mapping of operator journeys, system workflows, every console screen
    (including loading / empty / error / degraded states), alert–approval paths, admin surfaces,
    and the digital-twin simulation lab. Intended for product, engineering, and security review
    before implementation.</p>
    <p class="foot">Author: Victor.I · Classification: Defensive decision-support design only<br>
    Companion markdown: docs/product/* · docs/simulation/* · architecture/*</p>
    </div>""",
    "Cover",
)

add(
    """<div class="pad spec">
    <h2>Document control</h2>
    <div class="kv" style="margin-top:16px">
      <div class="k">Title</div><div class="v">UI/UX Screens, Workflows &amp; Simulation Specification</div>
      <div class="k">Author</div><div class="v">Victor.I</div>
      <div class="k">Status</div><div class="v">Draft for stakeholder review (Stage 0 — no application code)</div>
      <div class="k">Scope</div><div class="v">All operator, admin, lab, and global chrome surfaces; all P0–P2 workflows</div>
      <div class="k">Out of scope</div><div class="v">Weapon/effector UIs; production visual comps in Figma (this pack is the buildable spec)</div>
      <div class="k">Safety</div><div class="v">Platform records authorised response categories only — never physical effects</div>
      <div class="k">Related</div><div class="v">Requirements, ICD, threat model, digital twin architecture</div>
    </div>
    <div class="callout" style="margin-top:24px"><b>How to use this PDF.</b> Each page is a reviewable composition or workflow plate.
    Screen IDs (X01, I01, …) are permanent. Annotations in amber call out interaction rules.
    Markdown sources remain authoritative for prose edits; this pack is the visual contract.</div>
    </div>""",
    "Document control",
)

# TOC pages
toc_sections = [
    ("01 Front matter", "Cover, control, TOC, conventions"),
    ("02 Personas & jobs-to-be-done", "Roles and what each screen serves"),
    ("03 System workflows", "Sense-to-decision, state machines, fail paths"),
    ("04 User journeys (J1–J8)", "Step plates with linked screens"),
    ("05 Global chrome (G01–G03)", "Sign-in, banners, access denied"),
    ("06 Operator screens (X01–X08)", "Every state of the C2 console"),
    ("07 Incident screens (I01–I03)", "Coordination workspace"),
    ("08 Admin screens (A01–A04)", "Adapters, policies, roles"),
    ("09 Simulation (S01–S02 + twin)", "Lab director and scenario flows"),
    ("10 Reports (R01)", "After-action"),
    ("11 Component & epistemic library", "Reusable UI atoms"),
    ("12 Alert / approval patterns", "Fatigue, dual-control, handoff"),
    ("13 Simulation scenario atlas", "SCN catalogue visuals"),
    ("14 Edge cases & HF checklist", "Workload, a11y, anti-patterns"),
    ("15 Appendix", "ID index, open decisions, revision log"),
]
toc_html = '<div class="pad toc"><h2>Contents</h2><table style="margin-top:12px"><tr><th>Section</th><th>Contents</th></tr>'
for a, b in toc_sections:
    toc_html += f"<tr><td>{a}</td><td>{b}</td></tr>"
toc_html += '</table><p class="foot">Page numbers printed on each plate (bottom-right in header).</p></div>'
add(toc_html, "Contents · overview")

add(
    """<div class="pad toc"><h2>Screen &amp; journey index</h2>
    <div class="cols">
    <div><h3>Screens</h3>
    <table><tr><th>ID</th><th>Name</th><th>Pri</th></tr>
    <tr><td>G01</td><td>Sign-in / session</td><td>P0</td></tr>
    <tr><td>G02</td><td>Degraded banners</td><td>P0</td></tr>
    <tr><td>G03</td><td>Access denied</td><td>P0</td></tr>
    <tr><td>X01</td><td>Operator monitor</td><td>P0</td></tr>
    <tr><td>X02</td><td>Alert detail</td><td>P0</td></tr>
    <tr><td>X03</td><td>Track evidence</td><td>P0</td></tr>
    <tr><td>X04</td><td>Record decision</td><td>P0</td></tr>
    <tr><td>X05</td><td>Health</td><td>P0</td></tr>
    <tr><td>X06</td><td>Audit</td><td>P0</td></tr>
    <tr><td>X07</td><td>Replay</td><td>P1</td></tr>
    <tr><td>X08</td><td>Assistant</td><td>P2</td></tr>
    <tr><td>I01–I03</td><td>Incidents</td><td>P0/P1</td></tr>
    <tr><td>A01–A04</td><td>Admin</td><td>P1</td></tr>
    <tr><td>S01–S02</td><td>Simulation</td><td>P1/P2</td></tr>
    <tr><td>R01</td><td>After-action</td><td>P2</td></tr>
    </table></div>
    <div><h3>Journeys</h3>
    <table><tr><th>ID</th><th>Name</th></tr>
    <tr><td>J1</td><td>Unknown object</td></tr>
    <tr><td>J2</td><td>Suspected swarm</td></tr>
    <tr><td>J3</td><td>Sensor degradation</td></tr>
    <tr><td>J4</td><td>Contradictory classification</td></tr>
    <tr><td>J5</td><td>After-action replay</td></tr>
    <tr><td>J6</td><td>Sim adapter onboarding</td></tr>
    <tr><td>J7</td><td>AI-assisted investigation</td></tr>
    <tr><td>J8</td><td>Failed external handoff</td></tr>
    </table>
    <h3 style="margin-top:16px">State rule</h3>
    <p class="sub">Every data screen documents: <b>loading</b>, <b>loaded</b>, <b>empty</b>, <b>error</b>,
    plus applicable <b>degraded</b> modes (D1–D6).</p>
    </div></div></div>""",
    "Contents · ID index",
)

add(
    """<div class="pad">
    <h2>Conventions used in this pack</h2>
    <div class="cols" style="margin-top:16px">
      <div class="card"><h4>Epistemic layers</h4><p>Every detail view stacks Observation → Inference → Prediction → Recommendation → Decision. Inference never looks like confirmed fact.</p></div>
      <div class="card"><h4>Priority marks</h4><p>P0 ship-critical for Stage 5 · P1 should ship · P2 later · LAB never in OPS builds.</p></div>
      <div class="card"><h4>Amber annotations</h4><p>Callouts on compositions mark interaction or safety rules for reviewers.</p></div>
      <div class="card"><h4>Category language</h4><p>Buttons say Record decision — never Engage / Fire / Jam / Launch.</p></div>
    </div>
    <div class="flow" style="margin-top:28px">
      <div class="box"><b>OBSERVATION</b>Measured / reported</div><div class="arr">→</div>
      <div class="box"><b>INFERENCE</b>Model / fusion</div><div class="arr">→</div>
      <div class="box"><b>PREDICTION</b>Forward envelope</div><div class="arr">→</div>
      <div class="box"><b>RECOMMENDATION</b>Policy suggestion</div><div class="arr">→</div>
      <div class="box"><b>DECISION</b>Human record</div>
    </div>
    </div>""",
    "Conventions",
    badges("WORKFLOW"),
)

# Personas
personas = [
    ("Security operator", "Maintain air picture; triage; decide within policy", "X01 X02 X03 X04 X05", "Alert floods; opaque AI"),
    ("Sensor operator", "Keep sensors healthy; cue feeds", "X01 X05 A01", "Blind sectors; clock skew"),
    ("Incident commander", "Own incidents; high-tier categories", "I01 I02 X04 X06", "Incomplete evidence packs"),
    ("Analyst", "Replay; evaluate; tune notes", "X07 X06 R01", "Weak lineage"),
    ("System administrator", "Identity, deploy, adapters", "A01–A04", "Secret sprawl"),
    ("Governance officer", "Audit integrity; model cards", "X06 A03", "Opaque promotions"),
    ("Integrator / engineer", "Adapters & ICD", "A01 A02 S01", "Vendor lock-in"),
    ("Instructor (lab)", "Run twin scenarios", "S01 S02", "Truth leaking to trainees"),
]
ph = '<div class="pad"><h2>Personas</h2><div class="cols">'
for i, (n, g, s, p) in enumerate(personas):
    if i and i % 2 == 0:
        ph += '</div><div class="cols" style="margin-top:10px">'
    ph += f'<div class="card"><h4>{n}</h4><p><b>Goal:</b> {g}<br><b>Screens:</b> {s}<br><b>Pain:</b> {p}</p></div>'
ph += "</div></div>"
add(ph, "Personas · overview", badges("P0"))

add(
    """<div class="pad"><h2>Jobs to be done (UI-facing)</h2>
    <table class="spec" style="margin-top:12px">
    <tr><th>Job</th><th>Success look</th><th>Primary screens</th></tr>
    <tr><td>See what is in the air now</td><td>Map + tracks + quality in &lt;2s</td><td>X01</td></tr>
    <tr><td>Know how sure we are</td><td>Confidence band + epistemic stack</td><td>X03</td></tr>
    <tr><td>Know what to look at first</td><td>Tiered alerts, not raw firehose</td><td>X01 X02</td></tr>
    <tr><td>Understand why the system said that</td><td>Evidence graph + model version</td><td>X03</td></tr>
    <tr><td>Record an accountable decision</td><td>Category + rationale + audit id</td><td>X04 I02</td></tr>
    <tr><td>Detect capability loss</td><td>Banner + coverage hatch</td><td>G02 X05</td></tr>
    <tr><td>Coordinate multi-track events</td><td>Incident workspace</td><td>I01</td></tr>
    <tr><td>Prove behaviour in lab</td><td>Sim → real console path</td><td>S01 X01</td></tr>
    <tr><td>Investigate after the fact</td><td>Replay + audit export</td><td>X07 X06 R01</td></tr>
    </table></div>""",
    "Personas · jobs to be done",
)

# System workflows
add(
    """<div class="pad"><h2>System workflow — sense to decision</h2>
    <div class="flow" style="margin-top:20px">
      <div class="box"><b>SENSORS / SIM</b>Raw or synthetic</div><div class="arr">→</div>
      <div class="box"><b>ADAPTERS</b>Vendor boundary</div><div class="arr">→</div>
      <div class="box"><b>NORMALISE</b>CRS · time · validate</div><div class="arr">→</div>
      <div class="box"><b>EVENT BUS</b>observation.v1</div>
    </div>
    <div class="flow">
      <div class="box"><b>DETECT</b></div><div class="arr">→</div>
      <div class="box"><b>TRACK</b></div><div class="arr">→</div>
      <div class="box"><b>FUSE</b></div><div class="arr">→</div>
      <div class="box"><b>BEHAVIOUR</b></div><div class="arr">→</div>
      <div class="box"><b>RISK</b></div><div class="arr">→</div>
      <div class="box"><b>ALERTS</b></div>
    </div>
    <div class="flow">
      <div class="box"><b>OPERATOR UI</b>X01–X05</div><div class="arr">→</div>
      <div class="box"><b>HUMAN DECISION</b>X04 / I02</div><div class="arr">→</div>
      <div class="box"><b>CATEGORY HANDOFF</b>ICD-11</div><div class="arr">→</div>
      <div class="box"><b>AUDIT</b>Immutable</div>
    </div>
    <div class="callout"><b>Safety chain.</b> Detection → Track → Classify → Assess → Prioritise → Human review → Authorised category → External system. Platform does not implement physical effect.</div>
    </div>""",
    "Workflow · sense to decision",
    badges("WORKFLOW", "P0"),
)

add(
    """<div class="pad"><h2>Operator loop (happy path)</h2>
    <div style="margin-top:10px">
    <div class="step"><div class="n">1</div><div class="b card"><h4>Monitor X01</h4><p>Map-first SITREP; health pills; quiet T0/T1.</p></div></div>
    <div class="step"><div class="n">2</div><div class="b card"><h4>Alert asserts</h4><p>T2/T3 enters queue; selection syncs panels without wiping map pan.</p></div></div>
    <div class="step"><div class="n">3</div><div class="b card"><h4>Triage X02</h4><p>Why now, policy id, epistemic strips, linked track.</p></div></div>
    <div class="step"><div class="n">4</div><div class="b card"><h4>Investigate X03</h4><p>Evidence graph; conflicts; missing info.</p></div></div>
    <div class="step"><div class="n">5</div><div class="b card"><h4>Decide X04</h4><p>Category + rationale; non-weapon notice; audit.</p></div></div>
    <div class="step"><div class="n">6</div><div class="b card"><h4>Handoff status</h4><p>Queued / ACK / FAIL visible; local decision remains valid on FAIL.</p></div></div>
    </div></div>""",
    "Workflow · operator loop",
    badges("WORKFLOW", "P0"),
)

for title, body in [
    (
        "Workflow · track lifecycle",
        """<div class="flow"><div class="box"><b>CANDIDATE</b></div><div class="arr">→</div>
        <div class="box"><b>ACTIVE</b></div><div class="arr">→</div>
        <div class="box"><b>COASTING</b></div><div class="arr">→</div>
        <div class="box"><b>REACQUIRED</b></div><div class="arr">→</div>
        <div class="box"><b>DROPPED</b></div></div>
        <p class="sub" style="margin-top:16px">Merge path: ACTIVE → MERGED (into another id) with audit link. UI must show coasting uncertainty growth.</p>""",
    ),
    (
        "Workflow · alert lifecycle",
        """<div class="flow"><div class="box"><b>RAISED</b></div><div class="arr">→</div>
        <div class="box"><b>DELIVERED</b></div><div class="arr">→</div>
        <div class="box"><b>ACKNOWLEDGED</b></div><div class="arr">→</div>
        <div class="box"><b>IN_PROGRESS</b></div><div class="arr">→</div>
        <div class="box"><b>RESOLVED</b></div></div>
        <p class="sub" style="margin-top:16px">Side path: SUPPRESSED (duplicate / policy). T3 sticky until ack when policy says so.</p>""",
    ),
    (
        "Workflow · incident lifecycle",
        """<div class="flow"><div class="box"><b>OPEN</b></div><div class="arr">→</div>
        <div class="box"><b>ACTIVE</b></div><div class="arr">→</div>
        <div class="box"><b>PENDING_DECISION</b></div><div class="arr">→</div>
        <div class="box"><b>DECIDED</b></div><div class="arr">→</div>
        <div class="box"><b>CLOSED</b></div></div>
        <p class="sub" style="margin-top:16px">ESCALATED may branch from ACTIVE. Close without decision is restricted + audited.</p>""",
    ),
    (
        "Workflow · decision / handoff",
        """<div class="flow"><div class="box"><b>RECOMMENDATION_SHOWN</b></div><div class="arr">→</div>
        <div class="box"><b>DECISION_RECORDED</b></div><div class="arr">→</div>
        <div class="box"><b>HANDOFF_QUEUED</b></div><div class="arr">→</div>
        <div class="box"><b>ACKED | FAILED | N/A</b></div></div>
        <div class="notice">Fail-closed: if audit/IAM unavailable, DECISION_RECORDED cannot complete (G02-D4).</div>""",
    ),
]:
    add(f'<div class="pad"><h2>{title.split("·",1)[1].strip().title()}</h2>{body}</div>', title, badges("WORKFLOW"))

add(
    """<div class="pad"><h2>Degraded modes (G02) mapped to UI</h2>
    <table class="spec" style="margin-top:12px">
    <tr><th>Mode</th><th>Trigger</th><th>Banner</th><th>UI effect</th></tr>
    <tr><td>D1</td><td>Sensor loss</td><td>Coverage reduced</td><td>Map hatch; confidence ceiling</td></tr>
    <tr><td>D2</td><td>Model down</td><td>Model unavailable</td><td>Inference badge “sensor-native”</td></tr>
    <tr><td>D3</td><td>Bus lag</td><td>Stale picture</td><td>Dim live indicators; show lag age</td></tr>
    <tr><td>D4</td><td>Audit/IAM fail</td><td>Decisions unavailable</td><td>Disable Decide</td></tr>
    <tr><td>D5</td><td>Integration down</td><td>Handoff unavailable</td><td>Local decisions only</td></tr>
    <tr><td>D6</td><td>AI policy trip</td><td>Assistant disabled</td><td>Hide X08</td></tr>
    </table>
    <div class="callout"><b>Rule.</b> Prefer fail visible over fail silent. Never invent tracks to fill a coverage hole.</div>
    </div>""",
    "Workflow · degraded modes",
    badges("WORKFLOW", "P0"),
)

# Journeys — each step a page
journeys = [
    (
        "J1",
        "Unknown object",
        "P0",
        [
            ("Monitor", "X01", "Operator watching quiet air picture."),
            ("Alert T2", "X01/X02", "New track T-104 crosses policy P-14."),
            ("Evidence", "X03", "Operator opens epistemic stack + evidence graph."),
            ("Branch", "X04", "Ack / Cue sensor / Open incident / Dismiss."),
            ("Audit", "X06", "Decision or ack written with provenance."),
        ],
    ),
    (
        "J2",
        "Suspected swarm",
        "P0",
        [
            ("Behaviour flag", "X01", "Multi-track coordination indicators."),
            ("Incident auto-open", "I01", "I-22 workspace with three members."),
            ("Commander review", "I01", "Missing RF listed; recommendation NOTIFY_EXTERNAL."),
            ("Dual-control decide", "I02", "Two approvers if policy requires."),
            ("Handoff", "I01", "ACK or FAIL status module."),
        ],
    ),
    (
        "J3",
        "Sensor degradation",
        "P0",
        [
            ("Heartbeat miss", "G02/X01", "D1 banner + RF sector hatch."),
            ("Health drill-down", "X05", "RF-02 DOWN; last obs age 42s."),
            ("Ops response", "X05", "Escalate / switch backup (process)."),
            ("Recovery", "X01", "Banner clears; audited recovery event."),
        ],
    ),
    (
        "J4",
        "Contradictory classification",
        "P1",
        [
            ("Conflict strip", "X03", "Radar UAV-like vs EO bird-like."),
            ("Widen uncertainty", "X03", "Risk band widens; no forced pick."),
            ("Cue / note", "X04", "Human records operational resolution."),
        ],
    ),
    (
        "J5",
        "After-action replay",
        "P1",
        [
            ("Open replay", "X07", "Scrub incident I-22 time range."),
            ("Inspect", "X07/X03", "Historical tracks + event ticks."),
            ("Export", "R01", "Evidence pack / AAR narrative."),
        ],
    ),
    (
        "J6",
        "Sim adapter onboarding",
        "P1",
        [
            ("Adapters", "A01", "LAB env badge visible."),
            ("Create sim adapter", "A02", "Schema validate obs.v1."),
            ("Run scenario", "S01", "SCN-SWM-01 starts."),
            ("Observe console", "X01", "Real UI receives sim observations."),
        ],
    ),
    (
        "J7",
        "AI-assisted investigation",
        "P2",
        [
            ("Ask", "X08", "Why is T-104 elevated?"),
            ("Grounded answer", "X08", "Citations to risk + evidence tools."),
            ("Human decides", "X04", "Assistant cannot commit decisions."),
        ],
    ),
    (
        "J8",
        "Failed external handoff",
        "P0",
        [
            ("Decide NOTIFY_EXTERNAL", "X04", "Decision saved locally."),
            ("Integration fail", "I01/X04", "HANDOFF_FAILED / DLQ."),
            ("Retry or accept", "—", "Operator chooses; decision remains valid."),
        ],
    ),
]

for jid, jname, pri, steps in journeys:
    overview = f'<div class="pad"><h2>{jid} — {jname}</h2><p class="sub">Priority {pri}. Step plates follow.</p><div style="margin-top:12px">'
    for i, (sn, scr, desc) in enumerate(steps, 1):
        overview += f'<div class="step"><div class="n">{i}</div><div class="b card"><h4>{sn} · {scr}</h4><p>{desc}</p></div></div>'
    overview += "</div></div>"
    add(overview, f"Journey {jid} · overview", badges(pri, "WORKFLOW"))
    for i, (sn, scr, desc) in enumerate(steps, 1):
        add(
            f"""<div class="pad">
            <h2>{jid}.{i} {sn}</h2>
            <p class="sub"><b>Screen:</b> {scr} · {desc}</p>
            <div class="cols" style="margin-top:16px">
              <div class="card"><h4>Actor intent</h4><p>{desc}</p></div>
              <div class="card"><h4>System responsibility</h4><p>Preserve epistemic honesty; update audit if material; keep map context.</p></div>
              <div class="card"><h4>Failure if ignored</h4><p>Operator confuses inference with fact, or loses track of coverage loss.</p></div>
              <div class="card"><h4>Exit criteria</h4><p>Next step reachable in one intentional action; state visible in chrome.</p></div>
            </div>
            <div class="callout"><b>Wire to composition:</b> see screen plates for {scr} later in this document.</div>
            </div>""",
            f"Journey {jid} · step {i} {sn}",
            badges(pri, "WORKFLOW"),
        )

# Global screens
add(
    """<div class="modal-wrap" style="height:600px">
    <div class="modal">
      <h2>Sign in</h2>
      <p class="sub">Continue with organisation identity (OIDC). No local password store.</p>
      <div style="margin-top:16px"><span class="btn primary">Sign in with IdP</span></div>
      <div class="callout" style="margin-top:16px"><b>States:</b> loading IdP · ready · IdP down error · session expired modal returning here.</div>
    </div></div>""",
    "G01 · Sign-in · ready",
    badges("P0", "G01"),
)

add(
    """<div class="modal-wrap" style="height:600px">
    <div class="modal">
      <h2>Sign in</h2>
      <div class="skel"></div><div class="skel" style="width:60%"></div>
      <p class="sub" style="margin-top:12px">Contacting identity provider…</p>
    </div></div>""",
    "G01 · Sign-in · loading",
    badges("P0", "G01"),
)

add(
    """<div class="modal-wrap" style="height:600px">
    <div class="modal">
      <h2>Sign in</h2>
      <div class="notice">Identity provider unavailable. Try again or contact operations.</div>
      <div style="margin-top:12px"><span class="btn">Retry</span></div>
    </div></div>""",
    "G01 · Sign-in · error",
    badges("P0", "G01"),
)

for mode, copy, cls in [
    ("D1 Coverage reduced", "Sensing coverage reduced — track confidence capped in affected sectors.", ""),
    ("D2 Model degraded", "Detection model unavailable — showing sensor-native detections only.", "info"),
    ("D3 Stale picture", "Event lag 8.4s — operational picture may be stale.", ""),
    ("D4 Decision freeze", "Decisions unavailable — view only until audit/IAM restored.", "bad"),
    ("D5 Integration offline", "External handoff unavailable — local decisions still recorded.", ""),
    ("D6 Assistant off", "Assistant disabled by policy.", "info"),
]:
    add(
        f"""{shell('<span class="brand">COUNTER-SWARM</span> · Site ALPHA · Mode MONITOR','<span class="warn">DEGRADED</span>')}
        <div class="banner {cls}">{copy}</div>
        <div class="pad"><h2>G02 — {mode}</h2>
        <p class="sub">Banner is persistent until mode clears. Toast-only is insufficient.</p>
        <div class="callout"><b>Composition note:</b> On X01 the map and lists remain visible under the banner; Decide disabled only for D4.</div>
        </div>""",
        f"G02 · {mode}",
        badges("P0", "G02"),
    )

add(
    """<div class="modal-wrap" style="height:600px">
    <div class="modal">
      <h2>Access denied</h2>
      <p class="sub">Your role cannot open this resource. No object details are shown in the error body.</p>
      <div style="margin-top:12px"><span class="btn">Back to monitor</span></div>
    </div></div>""",
    "G03 · Access denied",
    badges("P0", "G03"),
)


def x01_frame(state: str, banner: str = "", extra_map: str = "", list_note: str = "") -> str:
    b = f'<div class="banner">{banner}</div>' if banner else ""
    left_list = {
        "loaded": """<div class="row active"><span><span class="tier t3">T3</span> Swarm ind.</span><span>2s</span></div>
          <div class="row"><span><span class="tier t2">T2</span> New T-104</span><span>8s</span></div>
          <div class="row"><span><span class="tier t1">T1</span> RF-02</span><span>42s</span></div>""",
        "empty": """<div style="padding:12px;color:var(--dim);font-size:11px">No alerts in filter.<br><span class="btn" style="margin-top:8px">Clear filters</span></div>""",
        "loading": """<div class="skel"></div><div class="skel"></div><div class="skel"></div>""",
        "error": """<div class="notice">Alert feed unreachable.</div><span class="btn">Retry</span>""",
    }.get(state, "")
    tracks = {
        "loaded": """<div class="row active"><span>T-104 UAV? 0.72</span><span>GOOD</span></div>
          <div class="row"><span>T-105 UAV? 0.68</span><span>FAIR</span></div>
          <div class="row"><span>T-091 Bird? 0.61</span><span>GOOD</span></div>""",
        "empty": """<div style="padding:8px;color:var(--dim);font-size:11px">No active tracks.</div>""",
        "loading": """<div class="skel"></div><div class="skel"></div>""",
        "error": """<div class="notice">Track service error.</div>""",
    }.get(state, "")
    risk = {
        "loaded": """<div style="font-size:12px;margin-bottom:6px">Track <b>T-104</b></div>
          <div style="color:var(--t2);font-size:11px;margin-bottom:8px">Risk ELEVATED</div>
          <div class="epi"><div class="band inf"><div class="k">INFERENCE</div>UAV p=0.72 det-v3.2</div>
          <div class="band rec"><div class="k">REC</div>HEIGHTEN_MONITORING</div></div>
          <span class="btn">Evidence</span><span class="btn primary">Decide</span>""",
        "empty": """<p style="color:var(--dim);font-size:11px">Select a track.</p>""",
        "loading": """<div class="skel"></div><div class="skel"></div>""",
        "error": """<div class="notice">Risk engine unavailable.</div>""",
    }.get(state, "")
    return f"""{shell('<span class="brand">COUNTER-SWARM</span> · ALPHA · MONITOR · op_j.smith','<span class="ok">SYS OK</span><span class="warn">SENS 3/4</span>')}
    {b}
    <div class="layout">
      <div class="panel" style="border-left:none"><h3>Alerts</h3>{left_list}
        <h3 style="margin-top:10px">Tracks</h3>{tracks}{list_note}</div>
      {map_canvas(extra_map)}
      <div class="panel"><h3>Risk / action</h3>{risk}</div>
      <div class="dock"><div class="tabs"><b>TIMELINE</b> · Sensors · System · Audit · Assistant</div>
      <div class="timeline">12:01:02 obs · 12:01:04 track · 12:01:05 risk · 12:01:06 alert</div></div>
    </div>"""


add(x01_frame("loaded", "COVERAGE REDUCED — RF-02 offline"), "X01 · Monitor · loaded + D1", badges("P0", "X01"))
add(
    x01_frame("loaded")
    + '<div class="anno" style="top:120px;left:420px">Selection syncs all panels</div>',
    "X01 · Monitor · selection anatomy",
    badges("P0", "X01"),
)
add(x01_frame("loading"), "X01 · Monitor · loading", badges("P0", "X01"))
add(x01_frame("empty"), "X01 · Monitor · empty", badges("P0", "X01"))
add(x01_frame("error"), "X01 · Monitor · error", badges("P0", "X01"))
add(
    x01_frame("loaded", "Event lag 8.4s — picture may be stale")
    + "",
    "X01 · Monitor · D3 stale",
    badges("P0", "X01"),
)
add(
    shell('<span class="brand">COUNTER-SWARM</span> · SIMPLIFY MODE', '<span class="warn">HIGH LOAD</span>')
    + """<div class="layout">
    <div class="panel" style="border-left:none"><h3>Alerts T2+</h3>
      <div class="row active"><span><span class="tier t3">T3</span> Swarm</span><span>2s</span></div>
      <div class="row"><span><span class="tier t2">T2</span> T-104</span><span>8s</span></div>
    </div>"""
    + map_canvas(label="MAP · SIMPLIFY — clutter hidden")
    + """<div class="panel"><h3>Focus</h3><p style="font-size:11px;color:var(--muted)">Only incident members + T2/T3.</p>
    <span class="btn">Exit simplify</span></div>
    <div class="dock"><div class="tabs"><b>TIMELINE</b></div><div class="timeline">simplified stream</div></div></div>""",
    "X01 · Monitor · simplify density",
    badges("P0", "X01"),
)

# X02
add(
    shell('<span class="brand">COUNTER-SWARM</span> · Alert A-8841', '<span class="tier t2">T2</span>')
    + """<div class="layout-mid">
    """
    + map_canvas(label="MAP · alert focus")
    + """<div class="pad" style="background:var(--elev);border-left:1px solid var(--border)">
      <h2>Alert A-8841</h2>
      <p class="sub">Reason: New track quality crossed policy P-14 · Linked T-104</p>
      <div class="epi">
        <div class="band obs"><div class="k">OBSERVATION</div>3 obs / 8s · RDR-1, EO-3</div>
        <div class="band inf"><div class="k">INFERENCE</div>UAV p=0.72 · det-v3.2</div>
        <div class="band pred"><div class="k">PREDICTION</div>60s envelope toggle</div>
        <div class="band rec"><div class="k">RECOMMENDATION</div>CUE_SENSOR optional</div>
      </div>
      <span class="btn">Acknowledge</span><span class="btn">Open track</span><span class="btn">Incident</span><span class="btn primary">Decide</span>
    </div></div>""",
    "X02 · Alert detail · loaded",
    badges("P0", "X02"),
)
add(
    """<div class="pad"><h2>X02 states</h2>
    <div class="cols3" style="margin-top:12px">
      <div class="card"><h4>Loading</h4><p>Skeleton in drawer; map keeps prior selection.</p></div>
      <div class="card"><h4>Not found</h4><p>Alert expired/suppressed — offer back to queue.</p></div>
      <div class="card"><h4>Error</h4><p>Retry · do not lose map context.</p></div>
    </div>
    <div class="callout"><b>Must show:</b> policy id, tier rationale (“why now”), linked objects.</div>
    </div>""",
    "X02 · Alert detail · states",
    badges("P0", "X02"),
)

# X03
add(
    shell('<span class="brand">TRACK T-104</span> · ACTIVE · age 00:01:14 · GOOD', '<span class="ok">FUSION OK</span>')
    + """<div class="layout2">"""
    + map_canvas(label="FOCUSED MAP")
    + """<div class="pad" style="background:var(--elev);border-left:1px solid var(--border)">
      <h2>Evidence pack</h2>
      <div class="epi">
        <div class="band obs"><div class="k">OBSERVATION</div>obs-881 RDR-1 · obs-882 EO-3</div>
        <div class="band inf"><div class="k">INFERENCE</div>UAV 0.72 · Bird 0.18 · Unk 0.10
          <div class="bar"><span style="width:72%"></span></div></div>
        <div class="band pred"><div class="k">PREDICTION</div>60s kinematic (dashed)</div>
        <div class="band rec"><div class="k">RECOMMENDATION</div>HEIGHTEN_MONITORING P-12</div>
        <div class="band dec"><div class="k">DECISION</div>Pending human</div>
      </div>
      <p style="font-size:11px;color:var(--muted)">Evidence: obs → det-9 → track → behaviour? → risk</p>
      <span class="btn">Cue</span><span class="btn">Incident</span><span class="btn primary">Decide</span>
    </div></div>""",
    "X03 · Track evidence · loaded",
    badges("P0", "X03"),
)
add(
    shell('<span class="brand">TRACK T-104</span> · CLASS_CONFLICT', '<span class="warn">CONFLICT</span>')
    + """<div class="pad">
    <div class="notice">Conflict: radar association prefers UAV-like · EO class hypothesis prefers bird-like. Uncertainty widened — no silent auto-resolve.</div>
    <div class="cols" style="margin-top:12px">
      <div class="card"><h4>Hypothesis A</h4><p>UAV 0.55 · model det-v3.2 · sensors RDR-1</p></div>
      <div class="card"><h4>Hypothesis B</h4><p>Bird 0.48 · model eo-cls-v1.4 · sensors EO-3</p></div>
    </div>
    <div class="callout"><b>J4 path.</b> Operator cues additional sensor or records operational note via Decide.</div>
    </div>""",
    "X03 · Track evidence · conflict",
    badges("P0", "X03"),
)
add(
    """<div class="pad"><h2>X03 additional states</h2>
    <div class="cols3">
      <div class="card"><h4>Loading</h4><p>Skeleton epistemic bands; map focus retained.</p></div>
      <div class="card"><h4>Dropped track</h4><p>Read-only historical; Decide disabled unless incident still open.</p></div>
      <div class="card"><h4>Error</h4><p>Partial evidence warning if some stores fail.</p></div>
    </div>
    <h3 style="margin-top:20px">Annotation rules</h3>
    <ul class="list"><li>Class as distribution, never single hard checkmark.</li>
    <li>Model version always adjacent to inference.</li>
    <li>Missing-info panel when material gaps exist.</li></ul>
    </div>""",
    "X03 · Track evidence · states",
    badges("P0", "X03"),
)

# X04
for st, body in [
    (
        "editing",
        """<h2>Record authorised response category</h2>
        <p class="sub">Context: Track T-104 · Incident I-22 · Recommended HEIGHTEN_MONITORING</p>
        <div style="line-height:1.8;font-size:13px">○ DISMISS<br><span style="color:var(--accent)">● HEIGHTEN_MONITORING</span><br>○ CUE_SENSOR<br>○ NOTIFY_EXTERNAL<br>○ REQUEST_ESCALATION<br>○ OPEN_INCIDENT</div>
        <div style="margin-top:10px;font-size:11px;color:var(--muted)">Rationale</div>
        <div style="border:1px solid var(--border);background:#0E1419;min-height:48px;padding:8px;font-size:12px;color:var(--dim)">Multi-track proximity…</div>
        <div class="notice">Records intent for authorised systems. Does not control weapons or electronic attack.</div>
        <div style="text-align:right;margin-top:12px"><span class="btn ghost">Cancel</span><span class="btn primary">Record decision</span></div>""",
    ),
    (
        "validation",
        """<h2>Record authorised response category</h2>
        <div class="notice">Rationale required for T2+ / incident decisions.</div>
        <div style="text-align:right;margin-top:12px"><span class="btn ghost">Cancel</span><span class="btn dis">Record decision</span></div>""",
    ),
    (
        "blocked D4",
        """<h2>Record authorised response category</h2>
        <div class="notice">Decisions unavailable — audit/IAM path degraded (G02-D4). View only.</div>
        <div style="text-align:right;margin-top:12px"><span class="btn ghost">Close</span><span class="btn dis">Record decision</span></div>""",
    ),
    (
        "success",
        """<h2>Decision recorded</h2>
        <div class="kv"><div class="k">Decision id</div><div class="v">DEC-20441</div>
        <div class="k">Category</div><div class="v">HEIGHTEN_MONITORING</div>
        <div class="k">Handoff</div><div class="v">NOT_REQUIRED</div>
        <div class="k">Audit</div><div class="v">chained OK</div></div>
        <div style="margin-top:12px"><span class="btn primary">Done</span></div>""",
    ),
]:
    add(
        f'<div class="modal-wrap"><div class="modal">{body}</div></div>',
        f"X04 · Decision · {st}",
        badges("P0", "X04"),
    )

# X05
add(
    shell('<span class="brand">HEALTH</span> · ALPHA', '<span class="warn">1 SENSOR DOWN</span>')
    + """<div class="layout2"><div class="pad">
    <h2>Sensors</h2>
    <table class="spec"><tr><th>ID</th><th>Status</th><th>Last</th><th>Notes</th></tr>
    <tr><td>RDR-1</td><td style="color:var(--ok)">OK</td><td>0.4s</td><td>—</td></tr>
    <tr><td>EO-3</td><td style="color:var(--ok)">OK</td><td>1.1s</td><td>—</td></tr>
    <tr><td>RF-02</td><td style="color:var(--down)">DOWN</td><td>42s</td><td>heartbeat</td></tr>
    <tr><td>MIC-1</td><td style="color:var(--ok)">OK</td><td>0.8s</td><td>—</td></tr></table>
    <h2 style="margin-top:18px">Platform</h2>
    <table class="spec"><tr><th>Component</th><th>Status</th><th>Signal</th></tr>
    <tr><td>API</td><td style="color:var(--ok)">OK</td><td>p95 180ms</td></tr>
    <tr><td>Bus lag</td><td style="color:var(--ok)">OK</td><td>120ms</td></tr>
    <tr><td>det-v3.2</td><td style="color:var(--ok)">OK</td><td>42ms</td></tr>
    <tr><td>Audit</td><td style="color:var(--ok)">OK</td><td>write path</td></tr></table>
    </div>"""
    + map_canvas(label="COVERAGE")
    + "</div>",
    "X05 · Health · loaded",
    badges("P0", "X05"),
)
add(
    """<div class="pad"><h2>X05 states &amp; rules</h2>
    <div class="cols3"><div class="card"><h4>Loading</h4><p>Skeleton tables.</p></div>
    <div class="card"><h4>Error</h4><p>Show last-known with staleness stamp.</p></div>
    <div class="card"><h4>All OK</h4><p>Still list sensors — empty health is suspicious.</p></div></div>
    <div class="callout"><b>J3.</b> Capability loss must be visible on X01 without requiring a visit to X05; X05 is the drill-down.</div>
    </div>""",
    "X05 · Health · states",
    badges("P0", "X05"),
)

# X06
add(
    shell('<span class="brand">AUDIT</span>', '<span class="ok">TAMPER-EVIDENT</span>')
    + """<div class="pad">
    <div style="font-size:11px;color:var(--dim);margin-bottom:8px">Filters: time · user · track · category · model</div>
    <table class="spec">
    <tr><th>Time</th><th>Type</th><th>Actor</th><th>Summary</th></tr>
    <tr><td>12:04:11</td><td>DECISION</td><td>j.smith</td><td>HEIGHTEN_MONITORING T-104</td></tr>
    <tr><td>12:04:10</td><td>RECOMMEND</td><td>policy</td><td>P-12</td></tr>
    <tr><td>12:04:09</td><td>RISK</td><td>engine</td><td>elevated factors coord,prox</td></tr>
    <tr><td>12:03:55</td><td>TRACK</td><td>fusion</td><td>merge candidate rejected</td></tr>
    </table>
    <div class="callout">Detail pane shows digest + hash chain ref (read-only). Export role-gated.</div>
    </div>""",
    "X06 · Audit · loaded",
    badges("P0", "X06"),
)
add(
    """<div class="pad"><h2>X06 states</h2>
    <div class="cols3">
    <div class="card"><h4>Empty</h4><p>No events in filter range.</p></div>
    <div class="card"><h4>Export denied</h4><p>G03-style message, no data leak.</p></div>
    <div class="card"><h4>Error</h4><p>Fail visible; investigations pause.</p></div>
    </div></div>""",
    "X06 · Audit · states",
    badges("P0", "X06"),
)

# X07
add(
    shell('<span class="brand">REPLAY</span> · Incident I-22', '<span>1x</span>')
    + """<div class="pad" style="padding-bottom:8px">
    <div style="font-family:var(--mono);font-size:11px;color:var(--muted);margin-bottom:8px">
    [&lt;] =========|=============== [&gt;]  12:01:00 — 12:05:00 · Play · 1x · 4x</div>
    </div>"""
    + '<div class="layout2" style="height:480px">'
    + map_canvas(label="HISTORICAL MAP")
    + """<div class="pad" style="background:var(--elev);border-left:1px solid var(--border)">
    <h3>Event ticks at scrub time</h3>
    <div class="timeline">12:02:01 incident open<br>12:03:10 behaviour<br>12:04:11 decision</div>
    <div style="margin-top:12px"><span class="btn">Open track at time</span><span class="btn">Export pack</span></div>
    </div></div>""",
    "X07 · Replay · playing",
    badges("P1", "X07"),
)
add(
    """<div class="pad"><h2>X07 states</h2>
    <div class="cols3">
    <div class="card"><h4>Buffering</h4><p>Scrubber waits on bus replay.</p></div>
    <div class="card"><h4>No data</h4><p>Range empty — distinct from error.</p></div>
    <div class="card"><h4>Error</h4><p>Partial reconstruction warning.</p></div>
    </div></div>""",
    "X07 · Replay · states",
    badges("P1", "X07"),
)

# X08
add(
    shell('<span class="brand">COUNTER-SWARM</span> · Assistant', '<span class="ok">POLICY ON</span>')
    + """<div class="layout-mid">"""
    + map_canvas()
    + """<div class="pad" style="background:var(--elev);border-left:1px solid var(--border)">
    <h2>Assistant</h2>
    <p class="sub">Tool-bounded · citations required · cannot record decisions</p>
    <div class="card" style="margin:10px 0"><h4>You</h4><p>Why is T-104 elevated?</p></div>
    <div class="card"><h4>Assistant</h4><p>Risk elevated due to proximity clustering with T-105/T-109 and missing RF on T-109.
    Citations: risk.assessment.v1 #884 · behaviour.indicator #12 · track T-104 evidence.</p></div>
    <div style="margin-top:8px;border:1px solid var(--border);padding:8px;font-size:12px;color:var(--dim)">Ask a question…</div>
    <div class="notice">Not on the critical path. Core C2 works if this is off (D6).</div>
    </div></div>""",
    "X08 · Assistant · answered",
    badges("P2", "X08"),
)
add(
    """<div class="pad"><h2>X08 states</h2>
    <div class="cols3">
    <div class="card"><h4>Thinking</h4><p>Tool calls audited live.</p></div>
    <div class="card"><h4>Tool denied</h4><p>Explain permission miss.</p></div>
    <div class="card"><h4>Unavailable</h4><p>Hide entry when D6.</p></div>
    </div></div>""",
    "X08 · Assistant · states",
    badges("P2", "X08"),
)

# Incidents
add(
    shell('<span class="brand">INCIDENT I-22</span> · SUSPECTED_COORDINATION · cmdr.lee · ACTIVE', '<span class="warn">HIGH BAND</span>')
    + """<div class="layout" style="grid-template-columns:1fr 300px;grid-template-rows:1fr 120px">"""
    + map_canvas(label="INCIDENT MAP")
    + """<div class="panel"><h3>Summary</h3>
    <div class="epi">
      <div class="band inf"><div class="k">BEHAVIOUR</div>Formation-like indicator (not confirmed fact)</div>
      <div class="band obs"><div class="k">MISSING</div>RF on T-109</div>
      <div class="band rec"><div class="k">REC</div>NOTIFY_EXTERNAL</div>
    </div>
    <span class="btn primary">Decide</span><span class="btn">Transfer</span><span class="btn">Close</span>
    <h3 style="margin-top:10px">Handoff</h3>
    <div style="font-size:11px;color:var(--muted)">NOT_REQUIRED until decision</div>
    </div>
    <div class="dock"><div class="tabs"><b>TIMELINE</b> · Notes · Participants</div>
    <div class="timeline">12:02 opened · 12:03 behaviour · 12:04 risk high</div></div></div>""",
    "I01 · Incident · active",
    badges("P0", "I01"),
)
add(
    """<div class="modal-wrap"><div class="modal">
    <h2>Dual-control decision</h2>
    <p class="sub">Category locked: NOTIFY_EXTERNAL</p>
    <div class="kv" style="margin-top:12px">
      <div class="k">Approver A</div><div class="v">cmdr.lee — signed</div>
      <div class="k">Approver B</div><div class="v" style="color:var(--t2)">waiting…</div>
    </div>
    <div style="margin-top:14px"><span class="btn">Request second</span><span class="btn ghost">Cancel</span></div>
    </div></div>""",
    "I02 · Dual-control · pending second",
    badges("P1", "I02"),
)
add(
    shell('<span class="brand">INCIDENTS</span>', '')
    + """<div class="pad">
    <table class="spec">
    <tr><th>ID</th><th>State</th><th>Owner</th><th>Severity</th><th>Tracks</th></tr>
    <tr><td>I-22</td><td>ACTIVE</td><td>cmdr.lee</td><td>HIGH</td><td>3</td></tr>
    <tr><td>I-19</td><td>DECIDED</td><td>cmdr.lee</td><td>MED</td><td>1</td></tr>
    <tr><td>I-11</td><td>CLOSED</td><td>op_j.smith</td><td>LOW</td><td>2</td></tr>
    </table>
    <div class="callout">Row opens I01. Filters by state/owner/severity.</div>
    </div>""",
    "I03 · Incident list",
    badges("P1", "I03"),
)
add(
    """<div class="pad"><h2>Incident UI rules</h2>
    <ul class="list">
    <li>Auto-open vs manual controlled by policy (open decision D-UI-03).</li>
    <li>Map shows members only by default.</li>
    <li>Close without decision requires restricted reason + audit.</li>
    <li>Handoff module always visible after DECIDED.</li>
    </ul></div>""",
    "Incidents · rules",
    badges("P0"),
)

# Admin
add(
    shell('<span class="brand">ADAPTERS</span> · env LAB', '<span class="badge lab">LAB</span>')
    + """<div class="pad">
    <table class="spec">
    <tr><th>ID</th><th>Type</th><th>Schema</th><th>Health</th><th>Last</th><th>Errors</th></tr>
    <tr><td>rdr-sim-01</td><td>radar</td><td>obs.v1</td><td style="color:var(--ok)">OK</td><td>0.4s</td><td>0</td></tr>
    <tr><td>eo-sim-02</td><td>eo</td><td>obs.v1</td><td style="color:var(--t2)">DEGRADED</td><td>12s</td><td>clock skew</td></tr>
    </table>
    <div style="margin-top:10px"><span class="btn primary">Add adapter</span></div>
    </div>""",
    "A01 · Adapter list",
    badges("P1", "A01", "LAB"),
)
add(
    """<div class="pad"><h2>A02 · Create / edit adapter</h2>
    <div class="kv">
      <div class="k">Name</div><div class="v">rf-sim-03</div>
      <div class="k">Type</div><div class="v">rf</div>
      <div class="k">Schema</div><div class="v">observation.v1</div>
      <div class="k">Endpoint</div><div class="v">sim://rf/03</div>
      <div class="k">Env</div><div class="v">LAB only</div>
    </div>
    <div style="margin-top:14px"><span class="btn">Validate schema</span><span class="btn primary">Save</span></div>
    <div class="notice">Cannot point LAB adapter at OPS integration URLs.</div>
    </div>""",
    "A02 · Adapter edit",
    badges("P1", "A02"),
)
add(
    """<div class="pad"><h2>A03 · Policy editor</h2>
    <p class="sub">Alert / risk policies are versioned. Publish creates immutable version id referenced in alerts.</p>
    <table class="spec"><tr><th>Policy</th><th>Version</th><th>Status</th></tr>
    <tr><td>P-12 heighten</td><td>3</td><td>active</td></tr>
    <tr><td>P-14 new track</td><td>2</td><td>active</td></tr>
    <tr><td>P-22 swarm auto-incident</td><td>1</td><td>draft</td></tr></table>
    <div style="margin-top:10px"><span class="btn">Diff</span><span class="btn primary">Publish</span></div>
    </div>""",
    "A03 · Policies",
    badges("P1", "A03"),
)
add(
    """<div class="pad"><h2>A04 · Roles &amp; permissions</h2>
    <table class="spec"><tr><th>Role</th><th>Monitor</th><th>Decide T2</th><th>Decide T3</th><th>Admin</th><th>Export</th></tr>
    <tr><td>Security operator</td><td>Y</td><td>Y</td><td>policy</td><td>—</td><td>—</td></tr>
    <tr><td>Commander</td><td>Y</td><td>Y</td><td>Y</td><td>—</td><td>Y</td></tr>
    <tr><td>Analyst</td><td>Y</td><td>—</td><td>—</td><td>—</td><td>Y</td></tr>
    <tr><td>Admin</td><td>Y</td><td>—</td><td>—</td><td>Y</td><td>—</td></tr>
    </table>
    <div class="callout">Source of truth is IdP groups mirrored into RBAC — this screen is visibility + assignment audit, not a parallel identity DB.</div>
    </div>""",
    "A04 · Roles",
    badges("P1", "A04"),
)

# Simulation
add(
    """<div class="pad"><h2>Simulation overview</h2>
    <div class="flow" style="margin-top:16px">
      <div class="box"><b>TRUTH</b>Objects · scripts · seed</div><div class="arr">→</div>
      <div class="box"><b>SENSOR MODELS</b>Radar EO RF Acoustic</div><div class="arr">→</div>
      <div class="box"><b>FAULTS</b>Drop delay death…</div><div class="arr">→</div>
      <div class="box"><b>SIM ADAPTERS</b>Same ICD</div><div class="arr">→</div>
      <div class="box"><b>REAL PLATFORM</b>to X01</div>
    </div>
    <div class="callout"><b>Never simulated as real controls:</b> weapons, jammers, kinetic parameters. Mock external only.</div>
    </div>""",
    "Simulation · architecture plate",
    badges("LAB", "WORKFLOW"),
)

add(
    shell('<span class="brand">SIM DIRECTOR</span> · LAB', '<span class="badge lab">LAB ONLY</span>')
    + """<div class="layout2">
    <div class="pad" style="background:var(--elev)">
      <h2>S01 Scenario control</h2>
      <div class="kv">
        <div class="k">Scenario</div><div class="v">SCN-SWM-01 coordinated_trio_v3</div>
        <div class="k">Seed</div><div class="v">42</div>
        <div class="k">Speed</div><div class="v">1x</div>
        <div class="k">Elapsed</div><div class="v">00:01:14 / 00:05:00</div>
      </div>
      <div style="margin-top:10px"><span class="btn primary">Start</span><span class="btn">Pause</span><span class="btn">Inject fault</span></div>
      <h3 style="margin-top:14px">Faults</h3>
      <p style="font-size:12px;color:var(--muted)">☐ Drop RF · ☐ Delay EO · ☑ Sensor death RF-02 @45s · ☐ Link loss</p>
      <h3>Truth overlay</h3>
      <p style="font-size:12px;color:var(--muted)">● Instructor only · ○ Off · ○ Forbidden for operator-under-test</p>
      <div class="notice">Mock external ACK/FAIL only.</div>
    </div>
    <div class="map" style="border:none"><div class="ml">TRUTH VIEW (instructor)</div>
      <div class="trk" style="left:300px;top:200px;background:var(--t2);border-radius:0;transform:rotate(45deg)"></div>
      <div class="trk" style="left:340px;top:230px;background:var(--t2);border-radius:0;transform:rotate(45deg)"></div>
      <div class="trk" style="left:280px;top:250px;background:var(--t2);border-radius:0;transform:rotate(45deg)"></div>
      <div class="tt" style="left:310px;top:180px;color:var(--t2)">truth A</div>
    </div></div>""",
    "S01 · Sim director · running",
    badges("P1", "S01", "LAB"),
)

add(
    shell('<span class="brand">SCENARIO LIBRARY</span>', '<span class="badge lab">LAB</span>')
    + """<div class="pad">
    <table class="spec">
    <tr><th>ID</th><th>Name</th><th>Stress</th><th>Pri</th></tr>
    <tr><td>SCN-TRK-01</td><td>Bird-like single</td><td>Low interest</td><td>P0</td></tr>
    <tr><td>SCN-TRK-02</td><td>UAV multi-sensor</td><td>Association</td><td>P0</td></tr>
    <tr><td>SCN-TRK-03</td><td>Crossing tracks</td><td>Ambiguity</td><td>P0</td></tr>
    <tr><td>SCN-SWM-01</td><td>Coordinated trio</td><td>Behaviour</td><td>P0</td></tr>
    <tr><td>SCN-SWM-02</td><td>Dense cluster</td><td>Fatigue</td><td>P0</td></tr>
    <tr><td>SCN-CLT-01</td><td>High clutter</td><td>FPR</td><td>P0</td></tr>
    <tr><td>SCN-MOD-01</td><td>RF silent</td><td>Missing modality</td><td>P0</td></tr>
    <tr><td>SCN-CON-01</td><td>Class conflict</td><td>Conflict UI</td><td>P0</td></tr>
    <tr><td>SCN-FLT-01</td><td>Sensor death</td><td>D1 UX</td><td>P0</td></tr>
    <tr><td>SCN-DEC-02</td><td>Handoff fail</td><td>J8</td><td>P0</td></tr>
    </table>
    <span class="btn primary" style="margin-top:10px">Load into S01</span>
    </div>""",
    "S02 · Scenario library",
    badges("P2", "S02", "LAB"),
)

# Dual console + scenario storyboards
add(
    """<div class="layout2" style="height:620px;border-top:none">
    <div style="border-right:1px solid var(--border)">
      <div class="shell"><div><span class="brand">S01 DIRECTOR</span></div><span class="badge lab">LAB</span></div>
      <div class="pad"><p class="sub">SCN-SWM-01 running · RF death armed · obs 42/s → bus</p>
      <span class="btn primary">Inject now</span></div>
    </div>
    <div>
      <div class="shell"><div><span class="brand">X01 OPERATOR</span></div><div class="pills"><span class="warn">SENS 3/4</span></div></div>
      """
    + map_canvas(label="REAL CONSOLE · sim-fed")
    + """</div></div>""",
    "Simulation · dual console",
    badges("LAB", "WORKFLOW"),
)

scenarios_extra = [
    ("SCN-TRK-02", "UAV across sensors", "Expect fused track with multi-sensor evidence links on X03."),
    ("SCN-SWM-01", "Coordinated trio", "Expect T3 + incident offer; behaviour labelled as indicator."),
    ("SCN-CLT-01", "High clutter", "Expect quality gating; operator alert rate bounded."),
    ("SCN-MOD-01", "RF silent", "Expect missing-info + confidence ceiling, not fake RF."),
    ("SCN-CON-01", "Contradiction", "Expect conflict strip on X03."),
    ("SCN-FLT-01", "Sensor death", "Expect D1 banner + X05 DOWN."),
    ("SCN-NET-01", "Partition", "Expect D3 stale then recovery."),
    ("SCN-DEC-02", "Handoff fail", "Expect decision saved + HANDOFF_FAILED."),
]
for sid, name, expect in scenarios_extra:
    add(
        f"""<div class="pad"><h2>{sid} — {name}</h2>
        <p class="sub">{expect}</p>
        <div class="cols" style="margin-top:14px">
          <div class="card"><h4>Twin actions</h4><p>Truth scripts + sensor models + scheduled faults.</p></div>
          <div class="card"><h4>Platform path</h4><p>Adapters → bus → fusion → risk → UI.</p></div>
          <div class="card"><h4>Operator-visible</h4><p>{expect}</p></div>
          <div class="card"><h4>Scorer checks</h4><p>Offline truth comparison; not shown as live fact on X01.</p></div>
        </div></div>""",
        f"Scenario · {sid}",
        badges("LAB"),
    )

# R01
add(
    """<div class="pad"><h2>R01 · After-action report</h2>
    <p class="sub">Read-only assembly from audit + timeline for incident I-22.</p>
    <div class="card" style="margin-top:12px">
      <h4>Narrative draft</h4>
      <p>At 12:02 incident opened on coordination indicators across T-104/105/109.
      Risk entered high band with missing RF on T-109. At 12:04 commander recorded NOTIFY_EXTERNAL.
      Handoff ACKED by mock external. Models: det-v3.2.</p>
    </div>
    <div style="margin-top:12px"><span class="btn">Export JSON</span><span class="btn">Export PDF (later)</span></div>
    </div>""",
    "R01 · After-action",
    badges("P2", "R01"),
)

# Components / epistemic library
add(
    """<div class="pad"><h2>Component library · epistemic</h2>
    <div class="epi" style="max-width:520px;margin-top:12px">
      <div class="band obs"><div class="k">OBSERVATION</div>Solid neutral — measured</div>
      <div class="band inf"><div class="k">INFERENCE</div>Labelled — scored — versioned</div>
      <div class="band pred"><div class="k">PREDICTION</div>Dashed geometry</div>
      <div class="band rec"><div class="k">RECOMMENDATION</div>Policy chip</div>
      <div class="band dec"><div class="k">DECISION</div>Stamped actor + time</div>
    </div>
    <div class="callout"><b>Forbidden:</b> green checkmarks on model class labels implying ground truth.</div>
    </div>""",
    "Components · epistemic",
    badges("P0"),
)
add(
    """<div class="pad"><h2>Component library · alerts &amp; actions</h2>
    <div style="margin:12px 0">
      <span class="comp"><span class="tier t3">T3</span> interrupt</span>
      <span class="comp"><span class="tier t2">T2</span> action suggested</span>
      <span class="comp"><span class="tier t1">T1</span> advisory</span>
      <span class="comp"><span class="tier t0">T0</span> log only</span>
    </div>
    <div style="margin:12px 0">
      <span class="btn">Secondary</span><span class="btn primary">Record decision</span><span class="btn dis">Disabled</span>
    </div>
    <div class="notice">Primary decision CTA label is always “Record decision”.</div>
    </div>""",
    "Components · alerts & CTAs",
    badges("P0"),
)
add(
    """<div class="pad"><h2>Design tokens (summary)</h2>
    <div class="cols3">
      <div class="card"><h4>Canvas</h4><p>#0B1014 / #121A21</p></div>
      <div class="card"><h4>Accent</h4><p>#2BB3A3 teal</p></div>
      <div class="card"><h4>T3 / T2 / T1</h4><p>#E85D4C / #E2A93B / #3C8FBF</p></div>
      <div class="card"><h4>Type</h4><p>IBM Plex Sans + Mono</p></div>
      <div class="card"><h4>Radius</h4><p>2–4px — no pill chrome</p></div>
      <div class="card"><h4>Motion</h4><p>Alert insert, selection ease, banner — only</p></div>
    </div>
    <p class="foot">Full token JSON: docs/product/08-design-tokens.md</p>
    </div>""",
    "Components · tokens",
)

# Alert/approval deep dive pages
add(
    """<div class="pad"><h2>Alert fatigue controls</h2>
    <ul class="list">
    <li>Duplicate suppression badge (“+12 similar”).</li>
    <li>Per-track collapse in queue.</li>
    <li>Quiet mode for T1 by role/policy.</li>
    <li>Admin-visible rate meter when storm detected.</li>
    <li>Simplify density mode on X01.</li>
    </ul>
    <div class="callout"><b>Test:</b> SCN-SWM-02 and SCN-ALT-01 must not make the queue unusable.</div>
    </div>""",
    "Patterns · alert fatigue",
    badges("P0", "WORKFLOW"),
)
add(
    """<div class="pad"><h2>Approval microcopy &amp; safety</h2>
    <table class="spec">
    <tr><th>Do</th><th>Don't</th></tr>
    <tr><td>Record decision</td><td>Engage / Fire / Launch</td></tr>
    <tr><td>Authorised response category</td><td>Weapon parameters</td></tr>
    <tr><td>Handoff status</td><td>Implied successful effect</td></tr>
    <tr><td>Inference labelled</td><td>AI confirmed threat</td></tr>
    </table>
    </div>""",
    "Patterns · microcopy",
    badges("P0"),
)
add(
    """<div class="pad"><h2>Handoff status module</h2>
    <div class="cols3">
      <div class="card"><h4>QUEUED</h4><p>Spinner · retry budget running</p></div>
      <div class="card"><h4>ACKED</h4><p>Success + external ref if any</p></div>
      <div class="card"><h4>FAILED / DLQ</h4><p>Error + retry eligibility · decision still valid</p></div>
    </div>
    <div class="callout">Maps to journey J8 and scenario SCN-DEC-02.</div>
    </div>""",
    "Patterns · handoff",
    badges("P0"),
)

# HF / edge cases
add(
    """<div class="pad"><h2>Human-factors checklist</h2>
    <ul class="list">
    <li>Time-to-evidence from alert row ≤ 1 click.</li>
    <li>T3 does not reset map pan/zoom.</li>
    <li>Colour never sole carrier of tier (icon+label).</li>
    <li>Keyboard: Esc closes drawers; Decide reachable without pointer-only traps.</li>
    <li>Reduced motion respected.</li>
    <li>Instructor truth never shown to operator-under-test by default.</li>
    </ul></div>""",
    "HF · checklist",
    badges("P0"),
)
add(
    """<div class="pad"><h2>Anti-patterns (reject in review)</h2>
    <ul class="list">
    <li>Stat cards / marketing dashboards in first viewport.</li>
    <li>Floating promo badges on the map.</li>
    <li>Single-click irreversible NOTIFY_EXTERNAL.</li>
    <li>Card soup replacing the map.</li>
    <li>LLM deciding risk alone.</li>
    <li>Hidden AI decisions styled as sensor facts.</li>
    </ul></div>""",
    "HF · anti-patterns",
    badges("P0"),
)

# Open decisions + appendix
add(
    """<div class="pad"><h2>Open design decisions (blocking)</h2>
    <table class="spec">
    <tr><th>ID</th><th>Decision</th><th>Default proposal</th></tr>
    <tr><td>D-UI-01</td><td>Accent colour</td><td>Teal #2BB3A3</td></tr>
    <tr><td>D-UI-02</td><td>Dual-control categories</td><td>NOTIFY_EXTERNAL + REQUEST_ESCALATION</td></tr>
    <tr><td>D-UI-03</td><td>Auto-open incidents</td><td>On behaviour+risk policy</td></tr>
    <tr><td>D-UI-04</td><td>T3 sound</td><td>User preference default on</td></tr>
    <tr><td>D-UI-05</td><td>Assistant in MVP</td><td>Defer (P2)</td></tr>
    <tr><td>D-UI-06</td><td>Basemap offline</td><td>Offline tiles for air-gap</td></tr>
    </table></div>""",
    "Appendix · open decisions",
)
add(
    """<div class="pad"><h2>Full screen↔journey traceability</h2>
    <table class="spec">
    <tr><th>Screen</th><th>Journeys</th><th>Workflows</th></tr>
    <tr><td>X01</td><td>J1 J2 J3 J6</td><td>Monitor loop, D1–D3</td></tr>
    <tr><td>X02</td><td>J1</td><td>Alert lifecycle</td></tr>
    <tr><td>X03</td><td>J1 J4 J5</td><td>Evidence / conflict</td></tr>
    <tr><td>X04</td><td>J1 J2 J4 J7 J8</td><td>Decision / handoff</td></tr>
    <tr><td>X05</td><td>J3</td><td>Degraded D1</td></tr>
    <tr><td>X06</td><td>all material</td><td>Audit</td></tr>
    <tr><td>X07</td><td>J5</td><td>Replay</td></tr>
    <tr><td>X08</td><td>J7</td><td>Optional AI</td></tr>
    <tr><td>I01–I02</td><td>J2 J8</td><td>Incident / dual-control</td></tr>
    <tr><td>S01–S02</td><td>J6</td><td>Digital twin</td></tr>
    </table></div>""",
    "Appendix · traceability",
)

add(
    f"""<div class="cover">
    <div class="badge scr">END OF PACK</div>
    <h1>Review complete?</h1>
    <p class="sub">This specification contains <b>{page_no + 1}</b> plates covering workflows, journeys,
    every screen state, simulation, and HF rules. Comment against screen IDs (e.g. “X03 conflict”).
    Do not start application UI coding until blocking decisions D-UI-01…06 are accepted or amended.</p>
    <p class="foot">Author: Victor.I · Counter-Swarm Defence · Stage 0</p>
    </div>""",
    "End matter",
)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<!-- Author: Victor.I -->
<title>Counter-Swarm Defence — UI/UX & Workflow Specification</title>
<style>{CSS}</style>
</head>
<body>
{''.join(pages)}
</body>
</html>
"""

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(html, encoding="utf-8")
print(f"Wrote {OUT} with {page_no} pages")
