<!-- Author: Victor.I -->

# Product PDFs and visual HTML

**Author:** Victor.I

## Open in browser (best for interactive review)

[`html/simulation-and-ui-pack.html`](html/simulation-and-ui-pack.html)

Contains rendered compositions for:

- X01 Operator monitor  
- X03 Track evidence  
- X04 Record decision  
- I01 Incident workspace  
- X05 Health  
- Simulation architecture diagram  
- S01 Sim director  
- Lab dual-console (director + operator)  

## PDF

After generation, see:

- [`pdfs/UI-UX-and-Simulation-Visual-Pack.pdf`](pdfs/UI-UX-and-Simulation-Visual-Pack.pdf)

Regenerate:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new \
  --disable-gpu --no-pdf-header-footer \
  --run-all-compositor-stages-before-draw --virtual-time-budget=10000 \
  --print-to-pdf=docs/product/pdfs/UI-UX-and-Simulation-Visual-Pack.pdf \
  "file://$(pwd)/docs/product/html/simulation-and-ui-pack.html"
```

## Simulation markdown pack

See [`../simulation/README.md`](../simulation/README.md).

## Author

Victor.I
