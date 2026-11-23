"""Make the Judge Smile (make.fun).

Writes a single warm, surprising line of at most 200 characters about a
small good thing that happened today to /output/entry.txt.
Standard library only.
"""

from pathlib import Path

LINE = (
    # Angle: a stranger's small kindness that turns into shared laughter.
    # Concrete details (bus shelter, dry on one side each) + surprise
    # (laughing like old friends with someone just met) + warmth.
    "Today my umbrella flipped inside-out in the rain, and a stranger "
    "under the bus shelter offered me half of his \u2014 we stood shoulder "
    "to shoulder, dry on one side each, laughing like old friends."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} characters"
    assert text.strip(), "entry must not be only white space"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {out}")


if __name__ == "__main__":
    main()
