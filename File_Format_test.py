def pack_format(file):
    #Open file to read
    file = open(file, 'r')
    #Initialize packing format to empty string
    struct_fmt = ''
    #Loop through each line in passed file
    for line in file:
        #Add correct format variable depending on structure from passed file
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
    #Close file
    file.close()
    #Return packing format to test
    return struct_fmt

#Test for each type used in schema 3
print pack_format("test.txt")
#Test call using schema3 from github struct
pack_format = pack_format("schema3.txt")

#x is hard coded format from original Data-Translator file
x = 'H'+'H'+'B'+'I'+'B'+'H'+'H'+'I'+'h'+'H'+'H'
#Print hard coded format and generated format for sanity check
print pack_format
print x
#Compare both strings to be sure they are the same
if x == pack_format:
    print True
