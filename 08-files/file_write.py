text_data = '''This is a tset file,
first line,
second line,
third line.'''

binary_data = bytes(range(0, 256))


def file_write():
    f = open('text_file', 'wt')
    f.write(text_data)
    f.close()

def file_write_binary():
    f = open('binary_file', 'wb')
    f.write(binary_data)
    f.close()

file_write()
file_write_binary()