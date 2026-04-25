## Repository Structure

```
secure-app-good/
├── .github/
│   └── workflows/
│      └── devsecops-pipeline.yml
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── main.py
├── .semgrep.ymlrequirements.txt
├── Dockerfile
├── README.md
└── requirements.txt

```

# secure-app-good-Alondres

A small but realistic DevSecOps demonstration application built with Flask, secured and validated through a multi-stage GitHub Actions CI pipeline.

## Pipeline Stages

| Stage | Job | Purpose |
|-------|-----|---------|
| 1 | `secret-scan` | Detect hardcoded secrets using Gitleaks |
| 2 | `sast-scan` | Static analysis using Semgrep |
| 3 | `dependency-scan` | CVE scan on Python dependencies using pip-audit |
| 4 | `build-and-scan` | Build Docker image, run Trivy container scan, generate SBOM |
| 5 | `promote` | Mark image as trusted and archive all artifacts |

## Artifacts Produced

- `sbom.json` — CycloneDX Software Bill of Materials for the container image
- `trivy-report.txt` — Container vulnerability scan summary
- `dependency-scan.txt` — Python dependency CVE scan results
- `trusted-build.txt` — Signed trust marker tied to commit SHA

## Security Practices

- No hardcoded secrets
- Non-root container user
- Minimal Alpine base image with `apk upgrade`
- Input validation via strict regex
- All scans must pass before image is promoted

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/greet` | Greet a valid username |

