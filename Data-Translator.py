import struct
# binascii library imported for testing only
import binascii

def pack(schema, address, overflow_num, uptime_ms, n, batt_mv, panel_mv, bmp085_press_pa, bmp085_temp_decic, humidity_centi_pct, apogee_2_m2):
    # Hardcoded packing format based on schema3
    struct_fmt = 'H'+'H'+'B'+'I'+'B'+'H'+'H'+'I'+'h'+'H'+'H'
    packed_data = struct.pack(struct_fmt, schema, address, overflow_num, uptime_ms, n, batt_mv, panel_mv, bmp085_press_pa, bmp085_temp_decic, humidity_centi_pct, apogee_2_m2)
    return packed_data

def unpack(packed_data):
    # Hardcoded packing format based on schema3
    struct_fmt = 'H'+'H'+'B'+'I'+'B'+'H'+'H'+'I'+'h'+'H'+'H'
    unpacked_data = struct.unpack(struct_fmt, packed_data)
    return unpacked_data

# Basic Test For Packing and Unpacking
# Packed test data
x = pack(5,151,8,300,2,25,10,45,49,10,55)
# Print packed data to see what packed data looks like
print x
# Print each packed data out in hex to actually understand packed data
for each in x:
    print binascii.hexlify(each)
# Print unpacked data to verify it is correct
print unpack(x)