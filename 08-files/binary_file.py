binary_data = bytes(range(0, 256))

f = open('binary_file', 'wb')
f.write(binary_data)
f.close()