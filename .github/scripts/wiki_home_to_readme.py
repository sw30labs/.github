#!/usr/bin/env python3
"""Regenerate the org profile README from the wiki's Home.md.

The wiki (https://github.com/sw30labs/.github/wiki) is the single source of
truth. This script takes wiki Home.md, transforms it for the org landing page,
and splices it into profile/README.md between the wiki-home markers — leaving
the profile-only header (banner, tagline, quote) and trailer (Book section,
footer) untouched.

Transformations applied to the wiki content:
  - Drop the wiki H1 + intro paragraph; start at the **Author:** metadata line.
  - Rewrite [[wikilinks]] (and any relative links) to absolute wiki URLs.
  - Demote headings by one level (wiki ## -> README ###).
  - Prefix known section titles with their profile emoji.

Run by .github/workflows/sync-profile-readme.yml. Edit the wiki, not the
generated block.
"""

import argparse
import pathlib
import re
import sys
import urllib.parse

WIKI_BASE = "https://github.com/sw30labs/.github/wiki"
START = "<!-- wiki-home:start -->"
END = "<!-- wiki-home:end -->"

# Profile-page flourish: emoji per wiki section title (exact match on the
# wiki Home heading text). Unknown sections pass through without an emoji.
SECTION_EMOJI = {
    "AI Security & Pentesting": "\U0001f512",          # 🔒
    "OSCAL & Compliance": "\U0001f6e1️",          # 🛡️
    "Agentic Frameworks": "\U0001f916",                # 🤖
    "Local Inference & MLX": "\U0001f34e",             # 🍎
    "Local Inference & DGX Spark": "⚡",           # ⚡
    "Developer Tools": "\U0001f527",                   # 🔧
    "Published Articles": "\U0001f4f0",                # 📰
    "Cross-cutting patterns": "\U0001f9e9",            # 🧩
}

DEMOTE_BY = 1  # wiki ## -> README ###


def wiki_url(page: str) -> str:
    """GitHub wiki page URL: flat namespace, spaces become hyphens."""
    return f"{WIKI_BASE}/{urllib.parse.quote(page.strip().replace(' ', '-'))}"


def load_page_names(wiki_dir: pathlib.Path) -> set:
    """All page names (filename stems) in the wiki checkout, used to resolve
    which side of a piped [[a|b]] wikilink is the page target."""
    return {p.stem for p in wiki_dir.rglob("*.md")}


def rewrite_links(body: str, pages: set) -> str:
    def wikilink(m: "re.Match") -> str:
        inner = m.group(1)
        if "|" in inner:
            a, b = (s.strip() for s in inner.split("|", 1))
            # Whichever side matches an actual wiki page is the target.
            if b in pages or b.replace(" ", "-") in pages:
                text, target = a, b
            elif a in pages or a.replace(" ", "-") in pages:
                text, target = b, a
            else:  # gollum default order: [[display text|Page Name]]
                text, target = a, b
        else:
            text = target = inner.strip()
        return f"[{text}]({wiki_url(target)})"

    body = re.sub(r"\[\[([^\]]+)\]\]", wikilink, body)

    # Safety net: any remaining relative markdown link becomes a wiki link.
    # (Home.md currently has none; absolute/anchor/mail links are untouched.)
    body = re.sub(
        r"\]\((?!https?://|#|mailto:)([^)\s]+)\)",
        lambda m: f"]({WIKI_BASE}/{m.group(1).lstrip('./')})",
        body,
    )
    return body


def transform_headings(body: str) -> str:
    out, in_fence = [], False
    for line in body.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        m = None if in_fence else re.match(r"^(#{1,5})\s+(.*?)\s*$", line)
        if m:
            hashes, title = m.groups()
            emoji = SECTION_EMOJI.get(title)
            shown = f"{emoji} {title}" if emoji else title
            out.append(f"{'#' * (len(hashes) + DEMOTE_BY)} {shown}")
        else:
            out.append(line)
    return "\n".join(out)


def extract_body(home_text: str) -> str:
    """Everything from the **Author:** metadata line to the end of Home.md.
    Falls back to 'after the H1' if the metadata line ever disappears."""
    lines = home_text.splitlines()
    start = next(
        (i for i, l in enumerate(lines) if l.startswith("**Author:**")), None
    )
    if start is None:
        start = next(
            (i + 1 for i, l in enumerate(lines) if l.startswith("# ")), 0
        )
    return "\n".join(lines[start:]).strip()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--home", required=True, help="path to wiki Home.md")
    ap.add_argument("--wiki-dir", required=True, help="path to wiki checkout")
    ap.add_argument("--readme", required=True, help="path to profile/README.md")
    args = ap.parse_args()

    home_text = pathlib.Path(args.home).read_text(encoding="utf-8")
    readme_path = pathlib.Path(args.readme)
    readme_text = readme_path.read_text(encoding="utf-8")
    pages = load_page_names(pathlib.Path(args.wiki_dir))

    body = extract_body(home_text)
    body = rewrite_links(body, pages)
    body = transform_headings(body)

    block = (
        f"{START}\n"
        f"<!-- AUTO-GENERATED from the org wiki Home page by "
        f".github/workflows/sync-profile-readme.yml.\n"
        f"     Edit {WIKI_BASE}/Home — changes here will be overwritten. -->\n"
        f"\n---\n\n"
        f"{body}\n\n"
        f"*<sub>This section is mirrored automatically from the "
        f"[org wiki]({WIKI_BASE}) — edit the wiki, not this file.</sub>*\n"
        f"{END}"
    )

    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pattern.search(readme_text):
        print(
            f"ERROR: markers {START} ... {END} not found in {args.readme}",
            file=sys.stderr,
        )
        return 2

    new_text = pattern.sub(lambda _m: block, readme_text, count=1)
    if new_text != readme_text:
        readme_path.write_text(new_text, encoding="utf-8")
        print(f"{args.readme}: regenerated from {args.home}")
    else:
        print(f"{args.readme}: already in sync")
    return 0


if __name__ == "__main__":
    sys.exit(main())
