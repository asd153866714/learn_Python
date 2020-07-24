def file_read_all():
    f = open('text_file', 'rt')
    read_all = f.read()
    print('Read_all: ')
    print(read_all)
    print()
    f.close()

def file_read_10_char():
    f = open('text_file', 'rt')
    read_10_char = f.read(10)
    print('Read_10: ')
    print(read_10_char)
    print()
    f.close()

def file_read_line():
    f = open('text_file', 'rt')
    read_line = f.readline()
    print('Readline: ')
    print(read_line)
    print()
    f.close()

def file_read_lines():
    f = open('text_file', 'rt')
    lines = f.readlines()
    print('Readlines: ')
    for line in lines:
        print(line)
    print()
    f.close()

def file_read_binary():
    f = open('binary_file', 'rb')
    binary_data = f.read()
    print("Binary: ")
    print(binary_data)
    print()
    f.close()

file_read_all()
file_read_10_char()
file_read_line()
file_read_lines()
file_read_binary()