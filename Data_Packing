import struct
import binascii

def pack(schema, address, overflow_num, uptime_ms, n, batt_mv, panel_mv, bmp085_press_pa, bmp085_temp_decic, humidity_centi_pct, apogee_2_m2):
    struct_fmt = 'H'+'H'+'B'+'I'+'B'+'H'+'H'+'I'+'h'+'H'+'H'
    packed_data = struct.pack(struct_fmt, schema, address, overflow_num, uptime_ms, n, batt_mv, panel_mv, bmp085_press_pa, bmp085_temp_decic, humidity_centi_pct, apogee_2_m2)
    return packed_data

def unpack(packed_data):
    struct_fmt = 'H'+'H'+'B'+'I'+'B'+'H'+'H'+'I'+'h'+'H'+'H'
    unpacked_data = struct.unpack(struct_fmt, packed_data)
    return unpacked_data


x = pack(5,151,8,300,2,25,10,45,49,10,55)
for each in x:
    print binascii.hexlify(each)
print unpack(x)
