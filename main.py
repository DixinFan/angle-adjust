from draw_img import *
from operate_motor import *
from predict_user_info import *
from operate_faces_rects import *
from correcte_distortion import *
from detect_faces import *
from read_config import *
from time import sleep

face_model = get_face_detector()
config_dict = query_config_params()

camera_index = config_dict['camera_index']
cap = cv2.VideoCapture(camera_index)

motor_flag = config_dict['motor_flag']

distance_min = config_dict['distance_min']
distance_max = config_dict['distance_max']

delay = config_dict['delay']
init_journey = config_dict['init_journey']

height_frames = config_dict['height_frames']
height_amount = height_frames

cap.set(3, 1920)
cap.set(4, 1080)

if __name__ == "__main__":
    print('init_journey: ' + str(init_journey))
    push_motor(init_journey)

    # height = 0
    is_new_user = False

    stable_height = 0
    height_list = []

    while True:
        sleep(delay)
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
                    print('正在加入第' + str(len(height_list) + 1) + '帧，计算身高平均值')

                    if len(height_list) == height_amount:
                        stable_height = caculate_stable_height(height_list)
                        print('完成平均身高计算，身高为：' + str(stable_height))
                        is_new_user = True

                else:
                    print('用户正在稳定使用自助机，不进行电机调节')
                    info = log_user_info(distance, stable_height)
                    print(info)

            else:
                print('用户不在指定距离范围，等待新用户进入')
                stable_height = 0
                height_list = []

        else:
            print('未检测到用户，等待新用户进入')
            stable_height = 0
            height_list = []

            # if height == 0:
            #     print('检测到新用户进入指定距离范围')
            #     height = predict_height(x, y)
            #     is_new_user = True

            # print('用户正在稳定使用自助机，不进行电机调节')
            # info = log_user_info(distance, height)
            # print(info)
            # draw_user_info(img, info)
            # draw_face_rect(img, rect)
        #     else:
        #         print('用户不在指定距离范围')
        #         height = 0
        # else:
        #     print('未检测到用户')
        #     height = 0

        # cv2.namedWindow('img', cv2.WINDOW_NORMAL)
        # cv2.resizeWindow('img', 337, 600)
        # cv2.imshow('img', img)

        if motor_flag and is_new_user:
            journey = caculate_journey(stable_height)
            print('为新用户进行一次电机调节')
            print('height: ' + str(stable_height) + '; journey: ' + str(journey))
            push_motor(journey)
            is_new_user = False

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
