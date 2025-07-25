# Project Cordelia - Development Setup Guide (First Prototype)
## Shakespeare Text Display

**Version:** 0.1 (First Prototype)  
**Date:** July 21, 2025  

---

## 1. Requirements

- Python 3.9+
- uv (Python package manager)
- Git
- Text editor (VS Code, PyCharm, etc.)

## 2. Install uv

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Verify:**
```bash
uv --version
```

## 3. Project Setup

```bash
# Create project
uv init project-cordelia
cd project-cordelia

# Create virtual environment
uv venv

# Activate environment
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate     # Windows

# Install dependencies
uv add streamlit lxml beautifulsoup4
```

## 4. Create Project Structure

```bash
# Create directories
mkdir data

# Create Python files
touch app.py parser.py
```

Final structure:
```
project-cordelia/
├── .venv/           # Virtual environment
├── app.py           # Main Streamlit app
├── parser.py        # TEI XML parser
├── data/
│   └── king_lear.xml  # TEI XML file (you'll add this)
├── pyproject.toml   # uv configuration
└── requirements.txt # Generated by uv
```

## 5. Add King Lear XML

Place the `king_lear.xml` TEI file in the `data/` directory.

## 6. Run the Application

```bash
# Make sure environment is activated
source .venv/bin/activate

# Run Streamlit
uv run streamlit run app.py

# Opens at http://localhost:8501
```

## 7. Development Workflow

1. Make changes to `app.py` or `parser.py`
2. Streamlit auto-reloads on save
3. Test in browser

## 8. Common Issues

**uv not found:**
- Restart terminal after installation
- Check PATH includes uv

**Import errors:**
- Ensure virtual environment is activated
- Run `uv sync` to reinstall dependencies

**Streamlit won't start:**
- Check if port 8501 is in use
- Try: `uv run streamlit run app.py --server.port 8502`

---

**Next:** Start coding with `app.py` and `parser.py`