<!-- Author: Victor.I -->

# CI/CD and Environments (Stage 0 Design)

**Author:** Victor.I  
**Status:** Design only — pipelines land in Stage 1  
**Owner:** Software Engineering · gates with Systems + Security

---

## 1. Environments

| Env | Purpose | Deploy style |
|---|---|---|
| local | Dev | Compose |
| ci | PR checks | ephemeral |
| lab | Twin + integration | Compose or small K8s |
| staging | Hardened pre-prod | K8s |
| ops | Authorised site | K8s + edge profiles |

---

## 2. Pipeline stages (planned)

1. Lint / unit / contract (schemas)  
2. Container build + SBOM + vuln scan  
3. Sim smoke (P0 scenarios) when Stage 1+ exists  
4. Sign image; push to private registry  
5. Deploy to lab/staging via IaC  
6. Manual approval for ops  

---

## 3. Branch policy (proposed)

- `main` protected  
- PR required  
- No secrets in git  
- `--no-verify` forbidden in normal workflow  

---

## 4. Edge profiles

Build matrices later: `linux/amd64` central · `linux/arm64` Jetson. Pi profile optional and non-critical.

---

## Author

Victor.I
