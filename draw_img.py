import cv2

color = (0, 255, 0)
font = cv2.FONT_HERSHEY_SIMPLEX


def draw_face_rect(img, rect):
    h, w = img.shape[:2]
    x_start, y_start, x_end, y_end = rect[0]*w, rect[1]*h, rect[2]*w, rect[3]*h
    x_start, y_start, x_end, y_end = int(x_start), int(y_start), int(x_end), int(y_end)
    cv2.rectangle(img, (x_start, y_start), (x_end, y_end), color, 2)


def draw_user_info(img, s):
    cv2.putText(img, s, (50, 50), font, 2, color, 3)


def log_user_info(distance, height):
    # distance = str(round(distance, 0))
    distance = str(int(distance+0.5))
    # height = str(round(height, 1))
    height = str(int(height+0.5))
    info = 'distance: ' + distance + '; height: ' + height
    return info
