<!-- Author: Victor.I -->

# Agent 3 — AI Engineering Architecture

**Author:** Victor.I  
**Status:** Stage 0 research note

---

## Where AI is useful

- Incident summarisation  
- Natural-language query over **authorised** read APIs  
- Runbook retrieval  
- Investigation assistance (“what evidence supports track T?”)  
- System diagnostics narratives from metrics (careful)  
- After-action report drafts  

## Where AI is forbidden as authority

Identity, permissions, event validation, safety interlocks, audit integrity, risk finalisation without deterministic policy, any external handoff.

## Architecture

```
Operator → AI Assistant → Policy Layer → Approved Tools → Data Services → Results → Explanation
```

### Policy layer requirements

- Tool allowlist + JSON schema args  
- Per-tool RBAC mirroring user permissions  
- Context isolation (no cross-incident bleed unless permitted)  
- Prompt-injection filters and untrusted content labeling  
- Hard timeouts; fail soft  
- Full audit of prompts/tool calls/responses (retention per SG)  

### Memory strategy

- Session scratch only by default  
- No long-term memory of sensitive tracks without policy  
- Retrieval limited to approved corpora  

### Evaluation

- Groundedness scores; tool-success rate; injection corpus pass rate  
- Human rated summaries on golden incidents  

## What not to build

Autonomous multi-agent swarms controlling the bus; LLM-written risk scores as sole input to alerts.
