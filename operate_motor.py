from read_config import *
import serial
import time
config_dict = query_config_params()

portx = config_dict['motor_port']
bps = config_dict['baud_rate']
timex = config_dict['timeout']
h2j_dict = config_dict['height_to_journey']


def push_motor(journey):
    msg = [0xA5, 0x5A, 0x01, 0x06, 0x01, journey, journey+8, 0x5A, 0xA5]
    ser = serial.Serial(portx, bps, timeout=timex)
    time.sleep(1)
    ser.write(msg)
    ser.close()
    time.sleep(10)


def caculate_journey(height):
    for key, value in h2j_dict.items():
        start, end = key.split('-')
        start, end, value = int(start), int(end), int(value)
        if start <= height < end:
            return value


if __name__ == "__main__":
    push_motor(0)


# height = 170
# journey = caculate_journey(height)
# print(journey)
# push_motor(distance_000)

# distance_000 = [0xA5, 0x5A, 0x01, 0x06, 0x01, 0x00, 0x08, 0x5A, 0xA5]
# distance_030 = [0xA5, 0x5A, 0x01, 0x06, 0x01, 0x1E, 0x26, 0x5A, 0xA5]
# distance_060 = [0xA5, 0x5A, 0x01, 0x06, 0x01, 0x3C, 0x44, 0x5A, 0xA5]
# distance_090 = [0xA5, 0x5A, 0x01, 0x06, 0x01, 0x5A, 0x62, 0x5A, 0xA5]
# distance_100 = [0xA5, 0x5A, 0x01, 0x06, 0x01, 0x64, 0x6C, 0x5A, 0xA5]
# distance_120 = [0xA5, 0x5A, 0x01, 0x06, 0x01, 0x78, 0x80, 0x5A, 0xA5]
# distance_130 = [0xA5, 0x5A, 0x01, 0x06, 0x01, 0x82, 0x8A, 0x5A, 0xA5]
# distance_150 = [0xA5, 0x5A, 0x01, 0x06, 0x01, 0x96, 0x9E, 0x5A, 0xA5]
# distance_180 = [0xA5, 0x5A, 0x01, 0x06, 0x01, 0xB4, 0xBC, 0x5A, 0xA5]


# print(msg)
# msg = distance_000


# msg = bytearray([165, 90, 1, 6, 1, journey, journey+8, 90, 165])
# print(msg)
# msg = 'A5 5A 01 06 01 32 3A 5A A5'
# msg = str.encode(msg)
# msg = [0xA5, 0x5A, 0x01, 0x06, 0x01, 0x00, 0x08, 0x5A, 0xA5]
# msg = [165, 90, 1, 6, 2, journey, journey+9, 90, 165]
# msg = [0xA5, 0x5A, 0x01, 0x06, 0x01, 0x00, 0x08, 0x5A, 0xA5]
# msg = [0xA5, 0x5A, 0x01, 0x06, 0x01, 0x32, 0x3A, 0x5A, 0xA5]
# msg = [0xA5, 0x5A, 0x01, 0x06, 0x01, 0x64, 0x6c, 0x5A, 0xA5]
# msg = [0xA5, 0x5A, 0x01, 0x06, 0x01, 0x2B, 0x33, 0x5A, 0xA5]
# print(msg)
# result = ser.write(msg)
# print(result)


# journey = 0
# if height >= 180:
#     journey = distance_000
# elif 170 <= height < 180:
#     journey = distance_100
# elif 160 <= height < 170:
#     journey = distance_130
# else:
#     journey = distance_180
# return journey