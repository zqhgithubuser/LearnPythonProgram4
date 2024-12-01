import io

# stream = io.StringIO()
# stream.write('Learning Python Programming.\n')
# print('Become a Python ninja!', file=stream)
# contents = stream.getvalue()
# print(contents)
# stream.close()

with io.StringIO() as stream:
    stream.write("Learning Python Programming.\n")
    print("Become a Python ninja!", file=stream)
    contents = stream.getvalue()
    print(contents)
