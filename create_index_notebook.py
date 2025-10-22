# build_portfolio.py
import os, io, re, nbformat
from pathlib import Path

ROOT = Path('.').resolve()
OUT_MD = ROOT / "PORTFOLIO.md"
OUT_NB = ROOT / "LeetCode_Index.ipynb"

def read_text(p: Path) -> str:
    try:
        return p.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return ""

def first_py_file(files):
    # pick the first .py that is not a helper; prefer file named same as folder
    pys = [f for f in files if f.endswith(".py")]
    if not pys:
        return None
    # prefer file whose stem matches folder name (dash or underscore variants)
    return pys[0]

def clean_echo_artifacts(text: str) -> str:
    # Remove leading "-e " markers that got echoed into the combined output
    # and stray lines like "-e \n### path ###\n"
    text = re.sub(r'(?m)^\-e\s*$', '', text)                 # lines that are just "-e"
    text = re.sub(r'(?m)^\-e\s+', '', text)                  # lines starting with "-e "
    return text

def make_portfolio_md():
    sections = []
    sections.append("# 🧠 LeetCode Solutions Portfolio\n")
    for entry in sorted(os.listdir(ROOT)):
        d = ROOT / entry
        if not d.is_dir():
            continue
        files = os.listdir(d)
        if "README.md" not in files:
            continue
        py = first_py_file(files)
        readme_path = d / "README.md"
        code_path = d / py if py else None

        readme = read_text(readme_path)
        code = read_text(code_path) if code_path else ""

        # clean any echo artifacts if someone concatenated earlier
        readme = clean_echo_artifacts(readme)

        sections.append(f"\n---\n## 🧩 {entry}\n")
        sections.append(f"**Folder:** `{entry}`  \n")
        if py:
            sections.append(f"**Solution:** `{py}`\n")
        else:
            sections.append(f"**Solution:** *(missing .py in folder)*\n")

        # If README is HTML, just include as-is; many GitHub READMEs use HTML blocks
        if readme.strip():
            sections.append("\n### Problem (README)\n")
            # Wrap raw HTML/Markdown directly
            sections.append(readme.strip())

        if code.strip():
            sections.append("\n### Python Solution\n```python\n" + code.rstrip() + "\n```\n")

    OUT_MD.write_text("\n".join(sections), encoding='utf-8')
    print(f"✅ Wrote {OUT_MD.relative_to(ROOT)}")

def make_index_notebook():
    nb = nbformat.v4.new_notebook()
    nb.cells.append(nbformat.v4.new_markdown_cell("# 🧠 LeetCode Solutions Index\n*Auto-generated from subfolders.*"))

    for entry in sorted(os.listdir(ROOT)):
        d = ROOT / entry
        if not d.is_dir():
            continue
        files = os.listdir(d)
        if "README.md" not in files:
            continue
        py = first_py_file(files)
        readme_rel = f"{entry}/README.md"
        nb.cells.append(nbformat.v4.new_markdown_cell(
            f"## 🧩 {entry}\n"
            f"[README]({readme_rel})" + (f"  |  [Solution]({entry}/{py})" if py else "")
        ))

        # code preview (not execution): we show the first ~80 lines
        if py:
            code = read_text(d / py)
            preview = "\n".join(code.splitlines()[:80])
            nb.cells.append(nbformat.v4.new_code_cell(
                f"# Preview of {entry}/{py}\n" +
                preview
            ))

    nbformat.write(nb, str(OUT_NB))
    print(f"✅ Wrote {OUT_NB.relative_to(ROOT)}")

if __name__ == "__main__":
    make_portfolio_md()
    make_index_notebook()
    print("✨ Done.")