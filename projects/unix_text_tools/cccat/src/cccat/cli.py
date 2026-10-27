import argparse
import sys
from collections.abc import Sequence

from cccat.logic import stream_lines


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cccat",
        description="""
            This coding challenge cat clone is built to read files sequentially, writing them to standard output.
            The file operands are processed in command-line order. If the file is a single dash ('-') or absent, cccat reads from the standard input.
            """,
    )

    parser.add_argument(
        "-n",
        "--number",
        help="include line numbers",
        action="store_true",
    )

    parser.add_argument("files", nargs="*", help="files to read; stdin if none")

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths: list[str] = args.files

    status = 0

    for path in paths or ["-"]:
        try:
            if path == "-":
                path = None

            out = sys.stdout.buffer

            for i, line in enumerate(stream_lines(path), start=1):
                out.write(b"%6d\t%b" % (i, line) if args.number else line)

        except OSError as e:
            print(f"cccat: {path}: {e.strerror}", file=sys.stderr)
            status = 1
            continue

    return status
