import cv2
import numpy as np
import yaml
import imutils

def CallBackFunc(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Left button of the mouse is clicked - position (", x, ", ",y, ")")
        list_points.append([x,y])
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("Right button of the mouse is clicked - position (", x, ", ", y, ")")
        list_points.append([x,y])


size_frame = 1000


vs = cv2.VideoCapture("../video/test.mp4")
while True:    
    (frame_exists, frame) = vs.read()
    frame = imutils.resize(frame, width=int(size_frame))
    cv2.imwrite("../img/static_frame_from_video.jpg",frame)
    break

windowName = 'MouseCallback'
cv2.namedWindow(windowName)

img_path = "../img/static_frame_from_video.jpg"
img = cv2.imread(img_path)

width,height,_ = img.shape

list_points = list()

cv2.setMouseCallback(windowName, CallBackFunc)


if __name__ == "__main__":
    while (True):
        cv2.imshow(windowName, img)
        if len(list_points) == 4:
            config_data = dict(
                image_parameters = dict(
                    p2 = list_points[3],
                    p1 = list_points[2],
                    p4 = list_points[0],
                    p3 = list_points[1],
                    width_og = width,
                    height_og = height,
                    img_path = img_path,
                    size_frame = size_frame,
                    ))

            with open('../conf/config_birdview.yml', 'w') as outfile:
                yaml.dump(config_data, outfile, default_flow_style=False)
            break
        if cv2.waitKey(20) == 27:
            break
    cv2.destroyAllWindows()