import struct
import binascii

def pack(file, schema, address, overflow_num, uptime_ms, n, batt_mv, panel_mv, bmp085_press_pa, bmp085_temp_decic, humidity_centi_pct, apogee_2_m2):
    file = open(file, 'r')
    struct_fmt = ''
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
    #struct_fmt = 'H'+'H'+'B'+'I'+'B'+'H'+'H'+'I'+'h'+'H'+'H'
    packed_data = struct.pack(struct_fmt, schema, address, overflow_num, uptime_ms, n, batt_mv, panel_mv, bmp085_press_pa, bmp085_temp_decic, humidity_centi_pct, apogee_2_m2)
    return packed_data

def unpack(file, packed_data):
    file = open(file, 'r')
    struct_fmt = ''
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
   # struct_fmt = 'H'+'H'+'B'+'I'+'B'+'H'+'H'+'I'+'h'+'H'+'H'
    unpacked_data = struct.unpack(struct_fmt, packed_data)
    return unpacked_data

x = pack("schema3.txt",5,151,8,300,2,25,10,45,49,10,55)
print x
print unpack("schema3.txt", x)