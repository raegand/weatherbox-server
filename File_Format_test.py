def test(file):
    file = open(file, 'r')
    struct_fmt = 'a'
    x = 0
    for line in file:
        print line
        if line == "int8\n" or line == "int8":
            struct_fmt = struct_fmt + 'b'
            print struct_fmt + '\n'
        if line == "uint8\n" or line == "uint8":
            struct_fmt = struct_fmt + 'B'
            print struct_fmt + '\n'
    file.close()


test("test.txt")