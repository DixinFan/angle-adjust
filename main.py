from draw_img import *
from operate_motor import *
from predict_user_info import *
from operate_faces_rects import *
from correcte_distortion import *
from detect_faces import *
from read_config import *

face_model = get_face_detector()
config_dict = query_config_params()

camera_index = config_dict['camera_index']
cap = cv2.VideoCapture(camera_index)

motor_flag = config_dict['motor_flag']

height_frames = config_dict['height_frames']
height_amount = height_frames

distance_min = config_dict['distance_min']
distance_max = config_dict['distance_max']

cap.set(3, 1920)
cap.set(4, 1080)


if __name__ == "__main__":
    stable_height = 0
    height_list = []
    while True:
        ret, img = cap.read()
        img = correct_img(img)
        h, w = img.shape[:2]
        rects = find_faces(img, face_model)
        rects = scalize_rects(h, w, rects)
        rects = remove_edge_rect(rects)
        # collect data
        '''
        if len(rects) > 0:
            rect, area = choose_largest_rect(rects)
            y_left = caculate_rect_y_center(rect)
            print(y_left, area)
            draw_face_rect(img, rect)
        '''
        if len(rects) > 0:
            rect, area = choose_largest_rect(rects)
            y_left = caculate_rect_y_center(rect)
            x = z_score_normalize(area, 'x')
            y = z_score_normalize(y_left, 'y')
            distance = predict_distance(x, y)

            if distance_max > distance > distance_min:

                if stable_height == 0:
                    height = predict_height(x, y)
                    height_list.append(height)

                    if len(height_list) == height_amount:
                        stable_height = caculate_stable_height(height_list)
                        journey = caculate_journey(stable_height)

                        if motor_flag:
                            push_motor(journey)

                info = log_user_info(distance, stable_height)
                print(info)
                draw_user_info(img, info)
                draw_face_rect(img, rect)
            else:
                stable_height = 0
                height_list = []
        else:
            stable_height = 0
            height_list = []
        cv2.namedWindow('img', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('img', 337, 600)
        cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
