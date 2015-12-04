def pack_format(file):
    #Open file for read only to avoid accidental writing
    file = open(file, 'r')
    #Initialize packing format to empty string so more string elements can be added to it
    struct_fmt = ''
    #Loop through each line in the format file to be sure everything is packed properly
    for line in file:
        #Add correct format variable depending on structure from passed file
        #Python packing formatting can be found on https://docs.python.org/2/library/struct.html
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
    #Close the file to avoid errors
    file.close()
    #Return packing format to test/print
    return struct_fmt

#Create a packing format with a file containing each variable type present and print out returned format to check
print pack_format("test.txt")
#Create packing format using a text file based on schema3 found in the github-server repository
pack_format = pack_format("schema3.txt")

#x is hard coded format from original Data-Translator file to test against generated code for same packing scheme
x = 'H'+'H'+'B'+'I'+'B'+'H'+'H'+'I'+'h'+'H'+'H'
#Print hard coded format and generated format for sanity check
print pack_format
print x
#Compare both strings
#If the generated format matches the hard coded format, print True to the console
if x == pack_format:
    print True
#If the generated file does not match, print message to the console
else:
    print "Packing format does not match"
