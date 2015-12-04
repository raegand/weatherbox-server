#Import struct library to use the packing and unpacking function
import struct
#Import binascii just for printing packed format in a nicer format during testing
import binascii

#Fuction created to pack passed data
def pack(schema, address, overflow_num, uptime_ms, n, batt_mv, panel_mv, bmp085_press_pa, bmp085_temp_decic, humidity_centi_pct, apogee_2_m2):
    #Hardcoded packing format based on schema3 found in the github server repository and information found on https://docs.python.org/2/library/struct.html
    struct_fmt = 'H'+'H'+'B'+'I'+'B'+'H'+'H'+'I'+'h'+'H'+'H'
    #Pack the passed data using the packing function in struct and the struct_fmt (format)
    packed_data = struct.pack(struct_fmt, schema, address, overflow_num, uptime_ms, n, batt_mv, panel_mv, bmp085_press_pa, bmp085_temp_decic, humidity_centi_pct, apogee_2_m2)
    #Return packed data for tests
    return packed_data

#Function created to unpack passed data
def unpack(packed_data):
    #Hardcoded packing format based on schema3 found in the github server repository and information found on https://docs.python.org/2/library/struct.html
    struct_fmt = 'H'+'H'+'B'+'I'+'B'+'H'+'H'+'I'+'h'+'H'+'H'
    #Unpack the passed data using the same packing format and the unpacking function in the struct library
        #Note:  If a different format is used to unpack the data, you won't get the original data you started with
    unpacked_data = struct.unpack(struct_fmt, packed_data)
    #Return the unpacked data for tests
    return unpacked_data

#Basic Test For Packing and Unpacking
#Packed test data
x = pack(5,151,8,300,2,25,10,45,49,10,55)
#Print packed data to see what packed data looks like
print x
#Print each packed data out in hex to actually understand packed data
for each in x:
    print binascii.hexlify(each)
#Print unpacked data to verify it is correct
print unpack(x)