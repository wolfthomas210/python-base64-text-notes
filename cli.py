"""Read one JSON value from stdin; write one JSON result."""
import json
import sys
from solution import solve

LIMIT = 1024 * 1024

def main():
    try:
        raw = sys.stdin.buffer.read(LIMIT + 1)
        if len(raw) > LIMIT:
            raise ValueError('input exceeds one MiB')
        value = json.loads(raw)
        result = solve(value)
        encoded = json.dumps(result, ensure_ascii=False, allow_nan=False)
    except (ValueError, TypeError, KeyError, IndexError, ArithmeticError, AttributeError) as error:
        print(json.dumps({'error': type(error).__name__, 'message': str(error)}), file=sys.stderr)
        return 2
    print(encoded)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
