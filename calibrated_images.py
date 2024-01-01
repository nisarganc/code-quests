"""
This script rectifies fisheye images using opencv functions.
"""

import numpy as np
import cv2 as cv
import glob

#camera projection matrix(3x3): 
# [fx 0 cx]
# [0 fy cy]
# [0  0  1]
# fx and fy are focal length. cx and cy are optical centers from the image center
camera_omni = np.array([[1442.56071669,   0.,            850.22934855], 
                          [0.,            1442.84866378, 716.87844446], 
                          [0.,            0.,            1.          ]], dtype=np.float32)

camera_pinhole = np.array([[517.47696058, 0.,             846.9816226  ], 
                          [0.,            517.48621258,   740.3092986  ], 
                          [0.,            0.,             1.          ]], dtype=np.float32)              

# distortion coefficients (4x1)
dist_radtan = np.array([-0.02219753, 0.14768812, -0.00052205, -0.00107954], dtype=np.float32)
dist_equi = np.array([0.00980522,  -0.00095657,  -0.00080178, -0.00025478], dtype=np.float32)

# xi
xi = np.array([[1.754305]], dtype=np.float32)

#read image to be rectified
path = r'~/data/rectify/input.png'
img = cv.imread('input.png')
img_dim = img.shape[:2][::-1]  
print('Image Dimenstion:', img_dim)

#1. Rectify using cv-fisheye function
K = cv.fisheye.estimateNewCameraMatrixForUndistortRectify(
                camera_pinhole, dist_equi, img_dim, np.eye(3), fov_scale=1)
print('Camera Matrix:', K)
'''new_K = np.array([[ 200.994316,   0.,          872.93585 ],
                     [  0.,          200.995705,  525.7371  ],
                     [  0.,          0.,          1.        ]], dtype=np.float32)'''

mapx3, mapy3 = cv.fisheye.initUndistortRectifyMap(camera_pinhole, dist_equi, np.eye(3), K, img_dim, cv.CV_16SC2)
undistorted_img = cv.remap(img, mapx3, mapy3, interpolation=cv.INTER_LINEAR)
cv.imwrite('fisheye_pinhole.png', undistorted_img)


#2. Rectify using cv-omni function
un_frame = cv.omnidir.undistortImage(img, camera_omni, dist_radtan, xi, 1, np.eye(3))
cv.imwrite('fisheye_omniradtan.png', un_frame)