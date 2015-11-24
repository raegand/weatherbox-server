def format(file):
    format_file = open(file, "r")
    struct_fmt = ''
    if format_file.readline() == 'int8':
        struct_fmt = struct_fmt + 'b'
    return struct_fmt


file = open("test.txt", "r")
print file.readline()
file.close()