import cv2
import numpy as np


def query_distortion_params():
    fx = 933.439364655740
    cx = 964.217787736310
    fy = 931.158396973019
    cy = 540.084931828991
    k1, k2, p1, p2, k3 = -0.388833799881282, 0.186596239554366, -0.000331394848456182, -0.000015902979115, -0.0479984222667210
    # 相机坐标系到像素坐标系的转换矩阵
    k = np.array([
        [fx, 0, cx],
        [0, fy, cy],
        [0, 0, 1]
    ])
    # 畸变系数
    d = np.array([
        k1, k2, p1, p2, k3
    ])
    return k, d


def correct_img(img):
    h, w = img.shape[:2]
    mtx, dist = query_distortion_params()
    new_camera_mtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
    img = cv2.undistort(img, mtx, dist, None, new_camera_mtx)
    # # crop the image
    # x, y, w, h = roi
    # dst = dst[y:y + h, x:x + w]
    img = np.rot90(img, k=-1)
    img = img.copy()
    return img