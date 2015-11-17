# weatherbox-server
Next generation weatherbox server. Written in python. The weatherbox server is responsible
for fetching and parsing data from the weatherbox.

Given some arbitrary packet, the weatherbox server should decode and put the
data into the weatherbox database appropriately.   

# Overview

The following describes data flow:

    Weatherbox -> Xbee -> Xbee -> Weatherbox-Server

Where the weatherbox-server looks something like this:

    Xbee-Library -> Decoder -> Postgres-Interface -> Postgresql Database


# Background information
## Sample data structure in C

The following is a sample structure in C that we'll be using for the weatherbox

    typedef struct {
        uint16_t schema;
        uint16_t address;           // Address of Arduino
        uint8_t overflow_num;       // Number of times millis overflowed (happens ~every 49 days)
        uint32_t uptime_ms;         // Time since start of program
        uint8_t n;                  // number of data points in packet 0..30
        uint16_t batt_mv[6];        // Battery Voltage (in milli volts)
        uint16_t panel_mv[6];       // Panel Voltage (in milli volts)
        uint32_t bmp085_press_pa;   // Pressure Value (in pascals)
        int16_t bmp085_temp_decic;  // Temperature Value (in celsius)
        uint16_t humidity_centi_pct;
        uint16_t apogee_w_m2[20];
    } schema_3;

## Packing/Unpacking Interface

Consider the following function in python:

    def pack(schema, address, overflow_num):
        # Do some packing
        return packed_data

