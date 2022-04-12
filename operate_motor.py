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

pre_journey = 0


def push_motor(journey):
    msg = [0xA5, 0x5A, 0x01, 0x06, 0x01, journey, journey+8, 0x5A, 0xA5]
    global pre_journey
    if pre_journey != journey:
        print('为新的电机行程进行一次串口通信电机调节')
        try:
            ser = serial.Serial(portx, bps, timeout=timex)
            time.sleep(sleep_before)
            ser.write(msg)
            ser.close()
        except:
            print('com通信口被占用，本次电机调节失败')
            pre_journey = 0
        else:
            print('com口通信成功，本次电机调节成功，等待电机执行完毕' + str(sleep_after) + '秒')
            pre_journey = journey
        time.sleep(sleep_after)
    else:
        print('电机行程不变，不进行串口通信电机调节')


def caculate_journey(height):
    for key, value in h2j_dict.items():
        start, end = key.split('-')
        start, end, value = int(start), int(end), int(value)
        if start <= height < end:
            value += motor_bias
            return value
