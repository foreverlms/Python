import base64
#a=base64.b64encode(b'binary\x00string')
# a=base64.b64encode(b'\x00')
# print(a)
# print(isinstance(a,bytes))
# print(b'x')
# x='中'.encode()
# print(x)
# print(isinstance(b'x',bytes))
# print(r'\n')
# print(b'\\')
def safe_base64_decode(s) :
    if len(s)%4==0 :
        return base64.b64decode(s)
    while not len(s)%4==0 :
        s=s+"="
    return base64.b64decode(s)
assert b'abcd' == safe_base64_decode(b'YWJjZA=='),safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'),safe_base64_decode('YWJjZA==')