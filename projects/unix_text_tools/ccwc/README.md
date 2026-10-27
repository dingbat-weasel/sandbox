# ccwc

A small clone of the Unix `wc` tool, built following the [Coding Challenges wc challenge](https://codingchallenges.fyi/challenges/challenge-wc)

## Installation

The project uses uv to establish the project:

```bash
cd projects/ccwc && uv sync
```

It can be run and tested with the local test.txt file (The Art of War):

```bash
uv sync
uv run ccwc tests/test.txt
```

```console
$ uv run ccwc tests/test.txt
    7145   58164  342190 tests/test.txt
```

## Usage

The program can read from a file. By default it prints line, word, and byte count.

```bash
uv run ccwc [filename]
```

Flags can be used to filter the output.

```bash
uv run ccwc -lwmc [filename]
```

- `-l`, `--lines`: line count
- `-w`, `--words`: word count
- `-m`, `--chars`: character count
- `-c`, `--bytes`: byte count

It can also read directly from stdin.

```bash
cat [filename] | uv run ccwc -l`
```

## Differences from wc

Words are split on ASCII whitespace only (space, tab, newline, vertical tab, form feed, carriage return), this matches `LC_ALL=C wc -w`. Unicode spaces like the non-breaking space do not separate words, so counts can differ from wc run in a UTF-8 locale.

Character counts are handled with the UTF-8 encoding by default. If the decoder runs into a non-utf-8 character it will replace it with the UTF-8 replacement character: `�` (U+FFFD), one per broken sequence (Python's decoder follows the unicode 'maximal subpart' rule. macOS wc counts each invalid byte separately and ignores an incomplete sequence at the end of input, so character counts can differ on corrupt input. Also the count will continue without surfacing anything, unlike wc which will print 'Illegal byte sequence' to stderr.

There's currently no 'Total' line printed to stdout when handling multiple files, although I may add that functionality in the future.

## Design

The counts are handled in pure functions that run over the byte input. The CLI shell is handled separately and calls the pure functions via a dispatch based on what flags are present. The CLI handles flags, files, and output formatting.

## Reflection

This was a really interesting and fun start to these smaller project challenges. It was my first deeper dive into handling characters vs bytes and the different encoding standards. One of the primary takeaways for me was learning how text is handled by python:

Calling open(path) in text mode causes python to create three objects which each wrap the one below it:

```
TextIOWrapper      decodes bytes → str, converts \r\n → \n
  └─ BufferedReader  reads bytes from the OS in chunks
       └─ FileIO       the raw operating-system file
```
Calling open(path, "rb") gives direct access to the BufferedReader bytes without the text layer on top. This really helped me get a sense of the underlying relationship in the way python handles reading files, particularly with sys.stdin (a TextIOWrapper) and how it keeps its own reference to layer beneath it in an attribute (sys.stdin.buffer.read())

I also enjoyed learning how to implement the dispatch. My first instinct was to utlize an if-else structure that felt quite clumsy. The dispatch table is a simple but helpful pattern I will use in the future.

Another takeaway was utilizing 'store_true' in argparse to easily handle the presence of flags.
