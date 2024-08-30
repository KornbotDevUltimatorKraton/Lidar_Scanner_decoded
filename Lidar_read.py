import serial 
import struct
from itertools import count 
ser = serial.Serial("/dev/ttyUSB0",115200,timeout=1)

for r in count(0):
    data = ser.read(1)
    #print(data)
    if data != b'\xFA':
        continue  # start byte not found, skip this packet
    data += ser.read(1)  # read the index byte
    data += ser.read(2)  # read the speed bytes
    data += ser.read(4)  # read the timestamp bytes
    data += ser.read(360*3)  # read the data bytes (360 values of 3 bytes each)
    data += ser.read(2)  # read the checksum bytes
    # decode the data
    data = data[2:-2]  # remove the index, speed, timestamp, and checksum bytes
    ranges = []
    angles = []
    for i in range(0, len(data), 3):
        byte3, byte2, byte1 = struct.unpack('BBB', data[i:i+3])
        dist_mm = ((byte1 << 16) | (byte2 << 8) | byte3)
        range_m = dist_mm / 1000.0  # convert mm to m
        angle_deg = i / 3  # calculate the angle from the index
        angles.append(angle_deg)
        ranges.append(range_m)
    #print the ranges and angles
    print("Ranges:", ranges,len(ranges))
    print("Angles:", angles,len(angles))
 


