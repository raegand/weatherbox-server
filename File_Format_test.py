def format(file):
    format_file = open(file, "r")
    struct_fmt = 'a'
    for line in format_file:
        if line == "int8":
            struct_fmt = struct_fmt + 'b'
    format_file.close()
    print struct_fmt


file = open("test.txt", "r")
print file.readline()
file.close()

format("test.txt")