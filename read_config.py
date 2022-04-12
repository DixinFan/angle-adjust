import configparser
import json


def query_config_params():
    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')
    config_dict = {}

    # camera
    camera_index = config.getint('camera', 'index')
    config_dict['camera_index'] = camera_index

    # motor
    motor_port = config.get('motor', 'port')
    config_dict['motor_port'] = motor_port

    baud_rate = config.getint('motor', 'baud_rate')
    config_dict['baud_rate'] = baud_rate

    timeout = config.getfloat('motor', 'timeout')
    config_dict['timeout'] = timeout

    motor_flag = config.getboolean('motor', 'flag')
    config_dict['motor_flag'] = motor_flag

    motor_bias = config.getint('motor', 'bias')
    config_dict['motor_bias'] = motor_bias

    sleep_before = config.getfloat('motor', 'sleep_before')
    config_dict['sleep_before'] = sleep_before

    sleep_after = config.getfloat('motor', 'sleep_after')
    config_dict['sleep_after'] = sleep_after

    init_journey = config.getint('motor', 'init_journey')
    config_dict['init_journey'] = init_journey

    # detection params
    distance_min = config.getfloat('detection_params', 'distance_min')
    config_dict['distance_min'] = distance_min

    distance_max = config.getfloat('detection_params', 'distance_max')
    config_dict['distance_max'] = distance_max

    remove_x_edge = config.getfloat('detection_params', 'remove_x_edge')
    config_dict['remove_x_edge'] = remove_x_edge

    remove_y_edge = config.getfloat('detection_params', 'remove_y_edge')
    config_dict['remove_y_edge'] = remove_y_edge

    height_bias = config.getfloat('detection_params', 'height_bias')
    config_dict['height_bias'] = height_bias

    delay = config.getfloat('detection_params', 'delay')
    config_dict['delay'] = delay

    height_frames = config.getint('detection_params', 'height_frames')
    config_dict['height_frames'] = height_frames

    # height_to_journey
    height_to_journey = config.get('height_to_journey', 'dictionary')
    config_dict['height_to_journey'] = json.loads(height_to_journey)

    return config_dict
