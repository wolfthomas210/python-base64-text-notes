"""Process a JSON array while preserving item positions and failures."""
import json
import sys
from solution import solve

LIMIT = 1024 * 1024

def process(values):
    results = []
    for index, value in enumerate(values):
        try:
            result = solve(value)
            json.dumps(result, allow_nan=False)
            results.append({'index': index, 'ok': True, 'result': result})
        except (ValueError, TypeError, KeyError, IndexError, ArithmeticError, AttributeError) as error:
            results.append({'index': index, 'ok': False, 'error': type(error).__name__})
    return results

def main():
    try:
        raw = sys.stdin.buffer.read(LIMIT + 1)
        if len(raw) > LIMIT:
            raise ValueError('input exceeds one MiB')
        values = json.loads(raw)
        if not isinstance(values, list) or len(values) > 1000:
            raise ValueError('expected an array of at most 1000 inputs')
        results = process(values)
    except (ValueError, TypeError) as error:
        print(json.dumps({'error': str(error)}), file=sys.stderr)
        return 2
    print(json.dumps(results, ensure_ascii=False, allow_nan=False))
    return 1 if any(not item['ok'] for item in results) else 0

if __name__ == '__main__':
    raise SystemExit(main())
