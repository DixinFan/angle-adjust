from read_config import *
import serial
import time
config_dict = query_config_params()

portx = config_dict['motor_port']
bps = config_dict['baud_rate']
timex = config_dict['timeout']
h2j_dict = config_dict['height_to_journey']
motor_bias = config_dict['motor_bias']
sleep_before = config_dict['sleep_before']
sleep_after = config_dict['sleep_after']


def push_motor(journey):
    msg = [0xA5, 0x5A, 0x01, 0x06, 0x01, journey, journey+8, 0x5A, 0xA5]
    ser = serial.Serial(portx, bps, timeout=timex)
    time.sleep(sleep_before)
    ser.write(msg)
    ser.close()
    time.sleep(sleep_after)


def caculate_journey(height):
    for key, value in h2j_dict.items():
        start, end = key.split('-')
        start, end, value = int(start), int(end), int(value)
        if start <= height < end:
            value += motor_bias
            return value
