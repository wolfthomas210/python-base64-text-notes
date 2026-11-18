import base64

def solve(value):
    return base64.b64encode(value.encode('utf-8')).decode('ascii')
