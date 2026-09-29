import argparse
import sys
from collections.abc import Sequence

from ccwc.counts import count_bytes, count_chars, count_lines, count_words


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ccwc",
        description="""
        Print the line, word, char, or byte counts of a file or stdin to stdout.
        Defaults to line, word, byte counts when no flags present.
        """,
    )
    parser.add_argument(
        "-l",
        "--lines",
        help="print a file's line count to standard output",
        action="store_true",
    )
    parser.add_argument(
        "-w",
        "--words",
        help="print a file's word count to standard output",
        action="store_true",
    )
    parser.add_argument(
        "-m",
        "--chars",
        help="print a file's character count to standard output",
        action="store_true",
    )
    parser.add_argument(
        "-c",
        "--bytes",
        help="print a file's byte count to standard output",
        action="store_true",
    )

    parser.add_argument("files", nargs="*", help="files to read; stdin if none")

    return parser


def format_output(counts: dict[str, int], name: str | None) -> str:
    columns = "".join(f" {n:7}" for n in counts.values())

    return f"{columns} {name}" if name is not None else columns


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths: list[str] = args.files
    show_lines: bool = args.lines
    show_words: bool = args.words
    show_chars: bool = args.chars
    show_bytes: bool = args.bytes

    if not (show_lines or show_words or show_chars or show_bytes):
        show_lines = show_words = show_bytes = True

    rows = [
        ("lines", show_lines, count_lines),
        ("words", show_words, count_words),
        ("chars", show_chars, count_chars),
        ("bytes", show_bytes, count_bytes),
    ]

    status = 0
    for path in paths or ["-"]:
        try:
            if path == "-":
                data = sys.stdin.buffer.read()
                name = None
            else:
                with open(path, "rb") as f:
                    data = f.read()
                    name = path
        except OSError as e:
            print(f"ccwc: {path}: {e.strerror}", file=sys.stderr)
            status = 1
            continue

        counts = {kind: f(data) for kind, enabled, f in rows if enabled}
        print(format_output(counts, name))

    return status
