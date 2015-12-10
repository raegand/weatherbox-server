def pack_format(file):
    file = open(file, 'r')
    struct_fmt = ''
    for line in file:
        # Add correct format variable depending on structure from passed file
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

# Basic File_Format tests for format generation
# Check that code generates packing for each variable type
print pack_format("test.txt")

# Generate packing format based on text file based on schema3
pack_format = pack_format("schema3.txt")

# Harded coded format from schema3
x = 'H'+'H'+'B'+'I'+'B'+'H'+'H'+'I'+'h'+'H'+'H'

# Print generated packing format for sanity check comparison
print pack_format
print x

# Double check that hard coded and generated format are the same
if x == pack_format:
    print True
else:
    print "Packing format does not match"
