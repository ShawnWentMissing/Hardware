# Merge 4 images into one big image

import cv2
import numpy as np
# take in 4 videos
# iterate through the videos and take a frame from each video
# merge the 4 frames into one big image

def take_frame(video_path1, video_path2, video_path3, video_path4):
    # take frames until the end of the video
    cap1 = cv2.VideoCapture(video_path1)
    cap2 = cv2.VideoCapture(video_path2)
    cap3 = cv2.VideoCapture(video_path3)
    cap4 = cv2.VideoCapture(video_path4)
    
    for x in range(500):

        # take the next frame from each video
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        ret3, frame3 = cap3.read()
        ret4, frame4 = cap4.read()

        yield frame1, frame2, frame3, frame4

        # if the frame is empty, break the loop
        if not ret1 or not ret2 or not ret3 or not ret4:
            break

    cap1.release()
    cap2.release()
    cap3.release()
    cap4.release()


    return merge(frame1, frame2, frame3, frame4)

def merge(img1,img2,img3,img4):

    # merge 4 images into one big long vertical strip with a 1px gap between each variable size image

    # get the dimensions of the images
    h1, w1 = img1.shape[:2]
    # img2 = cv2.rotate(img2, cv2.ROTATE_90_CLOCKWISE)
    h2, w2 = img2.shape[:2]
    # img3 = cv2.rotate(img2, cv2.ROTATE_90_CLOCKWISE)
    #rotate img3 90 degrees
    h3, w3 = img3.shape[:2]
    h4, w4 = img4.shape[:2]

    # get the max width
    max_width = max(w1, w2, w3, w4)

    # create a blank image with the max width and the sum of the heights
    blank_image = np.zeros((h1+h2+h3+h4+3, max_width, 3), np.uint8)

    # fill the blank image with the 4 images

    blank_image[0:h1, 0:w1] = img1
    blank_image[h1+1:h1+h2+1, 0:w2] = img2
    blank_image[h1+h2+2:h1+h2+h3+2, 0:w3] = img3

    blank_image[h1+h2+h3+3:h1+h2+h3+h4+3, 0:w4] = img4

    # save the big image
    cv2.imwrite('big_image.png', blank_image)
    return blank_image

def split(big_image):

    # split the big image into 4 images
    big_image = cv2.imread('big_image.png')
    
    # get the dimensions of the big image
    h, w = big_image.shape[:2]

    # split the big image into the 4 original images with original widths
    
    img1 = big_image[0:h//4, 0:w]
    img2 = big_image[h//4+1:h//2+1, 0:w]
    img3 = big_image[h//2+2:3*h//4+2, 0:w]

    img4 = big_image[3*h//4+3:h, 0:w]


    # save the 4 images
    # cv2.imwrite('new_frame1.png', img1)
    # cv2.imwrite('new_frame2.png', img2)
    # cv2.imwrite('new_frame3.png', img3)
    # cv2.imwrite('new_frame4.png', img4)

frames = take_frame('backmidwall.mp4','backwall.mp4','floor.mp4','topview.mp4')
for frame1,frame2,frame3,frame4 in frames:
    frames = [frame1,frame2,frame3,frame4]

big_image = merge( *frames)
split(big_image)