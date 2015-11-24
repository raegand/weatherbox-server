def test(file):
    file = open(file, 'r')
    struct_fmt = 'a'
    x = 0
    for line in file:
        print line
        if line == 'int8\n' or 'int8':
            struct_fmt = struct_fmt + 'b'
    file.close()
    print struct_fmt

test("test.txt")