"""Turn YouTube .vtt subtitles into compact, de-duplicated text for agents.

YouTube auto-subs repeat each line 2-3 times (rolling captions) and carry inline
<00:00:01.234><c> timing tags. This keeps one copy of each line and emits a
[mm:ss] marker roughly every CHUNK_SEC seconds, so agents can cite file@mm:ss.

Usage:  python scripts/clean_vtt.py transcripts transcripts/_clean
        (walks every series folder; skips files already cleaned and newer than source)
"""
import re
import sys
from pathlib import Path

CHUNK_SEC = 30
TS = re.compile(r"^(\d{2}):(\d{2}):(\d{2})\.\d{3}\s+-->")
TAG = re.compile(r"<[^>]+>")


def to_sec(m):
    h, mi, s = (int(x) for x in m.groups())
    return h * 3600 + mi * 60 + s


def clean(text: str) -> str:
    out, last_line, last_mark, cur = [], None, -CHUNK_SEC, 0
    for raw in text.splitlines():
        m = TS.match(raw)
        if m:
            cur = to_sec(m)
            continue
        line = TAG.sub("", raw).strip()
        if not line or line == "WEBVTT" or line.startswith(("Kind:", "Language:", "NOTE")):
            continue
        if line == last_line:
            continue
        if cur - last_mark >= CHUNK_SEC:
            out.append(f"\n[{cur // 60:02d}:{cur % 60:02d}] ")
            last_mark = cur
        out.append(line + " ")
        last_line = line
    return re.sub(r"[ \t]+", " ", "".join(out)).strip() + "\n"


def main(src_root: str, dst_root: str):
    src_root, dst_root = Path(src_root), Path(dst_root)
    done = skipped = 0
    for vtt in sorted(src_root.rglob("*.vtt")):
        if dst_root in vtt.parents:
            continue
        rel = vtt.relative_to(src_root).with_suffix(".txt")
        # "title.en.vtt" -> "title.txt"
        rel = rel.with_name(re.sub(r"\.en(-orig)?$", "", rel.stem) + ".txt")
        dst = dst_root / rel
        if dst.exists() and dst.stat().st_mtime >= vtt.stat().st_mtime:
            skipped += 1
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(clean(vtt.read_text(encoding="utf-8", errors="replace")), encoding="utf-8")
        done += 1
    print(f"cleaned {done}, up-to-date {skipped}")


if __name__ == "__main__":
    main(*(sys.argv[1:3] if len(sys.argv) >= 3 else ("transcripts", "transcripts/_clean")))
