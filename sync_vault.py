"""Sync current Obsidian note files to this public Quartz repository."""

from datetime import datetime
from pathlib import Path
import argparse
import hashlib
import shutil
import subprocess
import winreg


VAULT = Path(r"E:\Obsidian\Obsidian-AI-Knowledge-Base")
SITE = Path(__file__).resolve().parent
CONTENT = SITE / "content"
ARCHIVE = Path(r"D:\ai产出文件\牛马\归档")
SKIP = {
    ".git", ".obsidian", ".agents", ".claude", ".claudian", ".copilot",
    ".opencode", ".smart-env", ".smtcmp_json_db", ".quartz-site",
    ".github", "copilot", "records", "__pycache__",
}
EXTENSIONS = {".md", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".canvas", ".base", ".pdf"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).digest()


def git(*args):
    subprocess.run(("git", "-C", str(SITE), *args), check=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--push", action="store_true")
    args = parser.parse_args()
    sources = {}
    for path in VAULT.rglob("*"):
        relative = path.relative_to(VAULT)
        if path.is_file() and path.suffix.lower() in EXTENSIONS and not any(
            part in SKIP or part.startswith(".") for part in relative.parts
        ):
            sources[relative] = path

    changed = [relative for relative, source in sources.items() if not (CONTENT / relative).is_file() or digest(source) != digest(CONTENT / relative)]
    removed = [path.relative_to(CONTENT) for path in CONTENT.rglob("*") if path.is_file() and path.relative_to(CONTENT) != Path("index.md") and path.relative_to(CONTENT) not in sources]
    print(f"Vault files: {len(sources)}, changed: {len(changed)}, removed: {len(removed)}")
    if not args.push or not (changed or removed):
        return

    archive = ARCHIVE / ("quartz-sync-" + datetime.now().strftime("%Y%m%d-%H%M%S"))
    for relative in changed + removed:
        old = CONTENT / relative
        if old.is_file():
            saved = archive / relative
            saved.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(old, saved)
            if digest(old) != digest(saved):
                raise RuntimeError(f"Archive mismatch: {relative}")
    for relative in changed:
        destination = CONTENT / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(sources[relative], destination)
        if digest(sources[relative]) != digest(destination):
            raise RuntimeError(f"Sync mismatch: {relative}")
    for relative in removed:
        (CONTENT / relative).unlink()

    git("add", "-A", "--", "content")
    git("commit", "-m", "Sync Obsidian Vault notes")
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Internet Settings") as key:
        enabled, _ = winreg.QueryValueEx(key, "ProxyEnable")
        proxy, _ = winreg.QueryValueEx(key, "ProxyServer")
    if enabled and proxy:
        git("-c", "http.proxy=http://" + proxy, "push", "origin", "main")
    else:
        git("push", "origin", "main")


if __name__ == "__main__":
    main()
