import io
stream = io.StringIO()
stream.write('Practicing my Python programming.\n')
print('Becoming a Python Samurai.', file=stream)
contents = stream.getvalue()
print(contents)
stream.close()