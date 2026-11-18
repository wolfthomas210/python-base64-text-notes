# Encode UTF-8 text as Base64

A focused Python learning repository with runnable examples and technical notes.

Text is first encoded as UTF-8 bytes. Base64 is transport encoding rather than encryption and increases storage size.

## Requirements and quick start

Python 3.9 or newer; no third-party dependencies. Run commands from the repository root.

```sh
python3 example.py
```

The implementation is in `solution.py`. Inputs are small educational values, not an unbounded service workload.

## Lesson sequence

1. `notes/01-core.md`: core algorithm, example and limitations.
2. `notes/02-cli.md`: JSON command-line input and explicit error handling.
3. `notes/03-batch.md`: ordered batch processing with per-item failures.
4. `notes/04-stream.md`: newline-delimited JSON with bounded per-line input.

Later files appear when their prepared lessons are published. The collection stops when its content queue is exhausted.

## Publication

These examples and notes are AI-assisted educational material, published automatically from a prepared curriculum. Commits do not imply manual activity by an individual author. No tracking, network calls or dependencies are needed to run the examples.
