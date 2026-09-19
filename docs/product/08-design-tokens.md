<!-- Author: Victor.I -->

# Product Design — 08 Design Tokens

**Author:** Victor.I  
**Status:** Draft for review  
**Note:** Values are proposed defaults for an operational dark console; adjust after visual QA

---

## 1. Colour tokens

```json
{
  "color": {
    "canvas": { "bg": "#0B1014", "bgElevated": "#121A21", "grid": "#1A2430" },
    "text": { "primary": "#E6EEF4", "secondary": "#9AA8B5", "muted": "#6B7A88" },
    "accent": { "primary": "#2BB3A3", "primaryText": "#06221F" },
    "tier": {
      "t3": "#E85D4C",
      "t2": "#E2A93B",
      "t1": "#3C8FBF",
      "t0": "#6B7A88"
    },
    "state": {
      "ok": "#3FAE7F",
      "degraded": "#C4A35A",
      "down": "#D35D5D",
      "stale": "#8B7BB8"
    },
    "epistemic": {
      "observation": "#9AA8B5",
      "inference": "#D0B15A",
      "prediction": "#6FA8C9",
      "recommendation": "#2BB3A3",
      "decision": "#E6EEF4"
    },
    "map": {
      "track": "#D7E2EA",
      "trackSelected": "#2BB3A3",
      "uncertainty": "rgba(43,179,163,0.25)",
      "coverageHole": "rgba(139,123,184,0.20)",
      "geofence": "rgba(226,169,59,0.35)"
    },
    "danger": { "bg": "#3A1816", "border": "#E85D4C", "text": "#F5C4BE" },
    "border": { "subtle": "#243140", "strong": "#3A4B5C" }
  }
}
```

---

## 2. Typography tokens

```json
{
  "font": {
    "sans": "\"IBM Plex Sans\", \"Source Sans 3\", sans-serif",
    "mono": "\"IBM Plex Mono\", \"Source Code Pro\", monospace"
  },
  "size": {
    "xs": "12px",
    "sm": "13px",
    "md": "14px",
    "lg": "16px",
    "xl": "20px",
    "shell": "15px"
  },
  "weight": { "regular": 400, "medium": 550, "bold": 650 }
}
```

Rationale: expressive enough to avoid anonymous system UI; still built for dense ops readability. Not Inter/Roboto defaults.

---

## 3. Space and radius

```json
{
  "space": { "1": "4px", "2": "8px", "3": "12px", "4": "16px", "5": "24px", "6": "32px" },
  "radius": { "none": "0", "sm": "2px", "md": "4px" },
  "shadow": { "panel": "0 1px 0 rgba(0,0,0,0.4)" }
}
```

Prefer tight radii; avoid pill-heavy chrome.

---

## 4. Motion tokens

```json
{
  "motion": {
    "fast": "120ms",
    "base": "180ms",
    "slow": "280ms",
    "easing": "cubic-bezier(0.2, 0.8, 0.2, 1)"
  }
}
```

---

## 5. Z-index layers

```json
{
  "z": {
    "map": 0,
    "mapOverlay": 10,
    "panels": 20,
    "drawer": 30,
    "banner": 40,
    "modal": 50,
    "toast": 60
  }
}
```

---

## 6. Implementation note

Publish as CSS variables in frontend when Stage 5 starts, e.g. `--csd-color-tier-t3`. Do not hardcode hex in components outside the token source.

---

## Author

Victor.I
