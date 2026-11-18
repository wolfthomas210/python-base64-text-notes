# Encode UTF-8 text as Base64: implementation

## What the example does

Text is first encoded as UTF-8 bytes. Base64 is transport encoding rather than encryption and increases storage size.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
"hello"
```

Expected result:

```json
"aGVsbG8="
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
