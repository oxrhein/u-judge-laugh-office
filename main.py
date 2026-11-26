"""Make the AI Judge Laugh: Office Jokes — make.fun entry.

Writes a single office joke to ``$MAKEFUN_OUTPUT_DIR/entry.txt``.

The joke is a sprint-retro gag: the retro asks what went well and what
can improve, and the punchline is that nothing went well, everything
can improve, and the action items are unchanged from last sprint —
the most relatable (and most repeated) office ritual in software.
"""

import os

# The entry line, kept as a single module-level constant so the joke text
# lives in exactly one place and build_line() stays a thin accessor.
ENTRY_LINE = (
    "Sprint retro: what went well? Nothing. "
    "What can improve? Everything. "
    "Action items: same as last sprint."
)


def build_line():
    """Return the one-line office joke for the AI judge."""
    return ENTRY_LINE


def main():
    line = build_line()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")


if __name__ == "__main__":
    main()
