import io
s = "hello world"
sio = io.StringIO(s)
print(sio.getvalue())
sio.seek(0)
sio.write("*****")
print(sio.getvalue())