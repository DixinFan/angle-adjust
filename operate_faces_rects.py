from read_config import *
config_dict = query_config_params()
x_threshold = config_dict['remove_x_edge']
y_threshold = config_dict['remove_y_edge']


def scalize_rects(h, w, rects):
    for rect in rects:
        rect[0], rect[1], rect[2], rect[3] = rect[0] / w, rect[1] / h, rect[2] / w, rect[3] / h
    return rects


def remove_edge_rect(rects):
    for rect in rects:
        x_start, y_start, x_end, y_end = rect[0], rect[1], rect[2], rect[3]
        if x_start - x_threshold < 0 or x_end + x_threshold > 1 or y_start - y_threshold < 0 or y_end + y_threshold > 1:
            rects.remove(rect)
    return rects


def choose_largest_rect(rects):
    rects_area = []
    for rect in rects:
        rects_area.append((rect[2] - rect[0]) * (rect[3] - rect[1]))
    max_value = max(rects_area)
    max_index = rects_area.index(max_value)
    return rects[max_index], max_value


def caculate_rect_y_center(rect):
    return rect[1] + (rect[3] - rect[1]) / 2