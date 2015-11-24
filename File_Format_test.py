def test(file):

    file = open(file, 'r')
    struct_fmt = ''
    for line in file:
        print line
        if line == "int8\n" or line == "int8":
            struct_fmt = struct_fmt + 'b'

        if line == "uint8\n" or line == "uint8":
            struct_fmt = struct_fmt + 'B'

        if line == "int16\n" or line == "int16":
            struct_fmt = struct_fmt + 'h'

        if line == "uint16\n" or line == "uint16":
            struct_fmt = struct_fmt + 'H'

        if line == "int32\n" or line == "int32":
            struct_fmt = struct_fmt + 'i'

        if line == "uint32\n" or line == "uint32":
            struct_fmt = struct_fmt + 'I'

    file.close()
    return struct_fmt


pack_format = test("schema3.txt")
print pack_format

x = 'H'+'H'+'B'+'I'+'B'+'H'+'H'+'I'+'h'+'H'+'H'

if x == pack_format:
    print True
