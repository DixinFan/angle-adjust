from read_config import *
config_dict = query_config_params()
height_bias = config_dict['height_bias']

height_frames = config_dict['height_frames']
height_amount = height_frames


def z_score_normalize(data, dim):
    mean, std = 0, 0
    if dim == 'x':
        mean = 0.02348
        std = 0.02495
    if dim == 'y':
        mean = 0.5185
        std = 0.07867
    data = (data - mean) / std
    return data


def predict_height(x, y):
    p00 = 166.5
    p10 = -0.3037
    p01 = -11.91
    p20 = 0.4925
    p11 = 8.862
    p02 = 0.4367
    p21 = -1.949
    p12 = -0.2143
    p03 = -0.6464
    height = p00 + p10 * x + p01 * y + p20 * x ** 2 + p11 * x * y + p02 * y ** 2 + p21 * x ** 2 * y + p12 * x * y ** 2 + p03 * y ** 3
    height += height_bias
    return height


def predict_distance(x, y):
    p00 = 54.39
    p10 = -45.01
    p01 = -0.264
    p20 = 10.57
    p11 = -0.5459
    p02 = -1.99
    p21 = -0.8463
    p12 = 1.722
    p03 = 0.849
    distance = p00 + p10 * x + p01 * y + p20 * x ** 2 + p11 * x * y + p02 * y ** 2 + p21 * x ** 2 * y + p12 * x * y ** 2 + p03 * y ** 3
    return distance


def caculate_stable_height(height_list):
    # height_list.sort()
    # # # height_list = height_list[int(height_amount / 3): int(height_amount / 3) * 2]
    # height_list.sort()
    # height_list = height_list[1: 7]
    stable_height = sum(height_list) / len(height_list)
    return stable_height