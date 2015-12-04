#Import struct library to use the packing and unpacking function
import struct
#Import binascii just for printing packed format in a nicer format during testing
import binascii

#Fuction created to pack passed data
def pack(file, schema, address, overflow_num, uptime_ms, n, batt_mv, panel_mv, bmp085_press_pa, bmp085_temp_decic, humidity_centi_pct, apogee_2_m2):
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
    #struct_fmt = 'H'+'H'+'B'+'I'+'B'+'H'+'H'+'I'+'h'+'H'+'H'
    #Pack the passed data using the packing function in struct and the struct_fmt (format)
    packed_data = struct.pack(struct_fmt, schema, address, overflow_num, uptime_ms, n, batt_mv, panel_mv, bmp085_press_pa, bmp085_temp_decic, humidity_centi_pct, apogee_2_m2)
    #Return packed data for tests
    return packed_data

def unpack(file, packed_data):
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
    #Hard coded packing format commented out to properly run the format generation code
   # struct_fmt = 'H'+'H'+'B'+'I'+'B'+'H'+'H'+'I'+'h'+'H'+'H'
    #Unpack the passed data using the same packing format and the unpacking function in the struct library
        #Note:  If a different format is used to unpack the data, you won't get the original data you started with
    unpacked_data = struct.unpack(struct_fmt, packed_data)
    #Return unpacked data for tests
    return unpacked_data

#Basic Test For Packing and Unpacking
#Packed test data
x = pack("schema3.txt",5,151,8,300,2,25,10,45,49,10,55)
#Print testing data for test check
data = (5,151,8,300,2,25,10,45,49,10,55)
print data
#Print packed data to see what packed data looks like
print x
#Print each packed data out in hex to actually understand packed data
for each in x:
    print binascii.hexlify(each)
#Print unpacked data to verify it is correct
print unpack("schema3.txt",x)