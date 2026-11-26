"""Entry for make.fun: The 3 AM Commit Message.

A commit message reverting a small, supposedly harmless 2:58 AM improvement.
"""
import os

LINE = "fix: restore production by reverting my 2:58 AM 'small harmless improvement' and banning me from confidence after midnight"
MAX_CHARS = 200


def write_entry(out_dir):
    assert LINE.strip(), "entry must not be empty"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))


if __name__ == "__main__":
    main()
