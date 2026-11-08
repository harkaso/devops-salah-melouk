![CI](https://github.com/harkaso/devops-salah-melouk/actions/workflows/ci.yml/badge.svg)

# Shop

## How to run tests

### For Windows users

```powershell
cd path\to\devops-salah-melouk
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r  requirements-dev.txt
pip check
ruff check .
ruff format --check .
pyright
pytest --cov=. --cov-report=term-missing
pip-audit -r requirements-dev.txt
```

### For Linux users

```bash
cd path/to/devops-salah-melouk
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python -m pip check
ruff check .
ruff format --check .
pyright
pytest --cov=. --cov-report=term-missing
pip-audit -r requirements-dev.txt
```
