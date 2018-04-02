import cv2
import os
import numpy as np
# from humandetection import Humans
from PIL import Image
# def three_images_per_second(video_file, output_dir, fps):
#     cap = cv2.VideoCapture(video_file)
#     frame_num = 0
#     image_num = 0
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if ret:
#             cv2.imwrite(output_dir+"/image{}.jpg".format(image_num),frame)
#             image_num += 1
#         else:
#             break
#         frame_num += 1

#     cap.release()
#     cv2.destroyAllWindows()
#     return

# three_images_per_second("giscle.mp4", "OUTPUT",30)

print(cv2.__version__)
def videoframe():   
    vidcap = cv2.VideoCapture('GOT.mp4')

    try:
        if not os.path.exists('videotoframe'):
            os.makedirs('videotoframe')
    except OSError:
        print('Error: Creating directory of videotoframe')

    count = 0
    success = True
    while success:
        success,image = vidcap.read()
        name = './videotoframe/image' + str(count) + '.jpg'

        print('creating... ' + name)

        cv2.imwrite(name ,image) #(orig)

        print('Read a new frame: ', success)

        # img = Image.open(name)
        # img2 = Image.ROTATE_180
        # # name = str(name)
        # # name = './videotoframe/image' + str(count) + '.jpg'
        # print(type(name))
        # img2.save(name)
  # save frame as JPEG file
        count += 1
        str(count)
    vidcap.release()
    
    # vidcap.destroyAllWindows()
    print(count)
    
videoframe()
# Humans()


