import cv2
import numpy as np


'''
    Handling mouse event in openCv
'''
prevX, prevY = -1, -1


def print_cordinates(event, x, y, flags, params):
    global prevX, prevY
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, center=(x, y), radius=5,
                   color=(0, 255, 0), thickness=-1)
        strxy = f"({str(x)},{str(y)})"
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text=strxy, org=(x+10, y-10), fontFace=font, fontScale=0.5,
                    lineType=cv2.LINE_AA, color=(0, 255, 0))
        if prevX == -1 & prevY == -1:
            prevX, prevY = x, y
        else:
            cv2.line(img, pt1=(prevX, prevY), pt2=(
                x, y), color=(0, 255, 0), thickness=2)
            prevX, prevY = -1, -1


# True while mouse button down , False while mouse button up
drawing = False
ix, iy = -1, -1


def draw_rectangle(event, x, y, flags, params):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (x, y), (ix, iy),
                          color=(255, 0, 0), thickness=-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (x, y), (ix, iy), color=(255, 0, 0), thickness=-1)


cv2.namedWindow(winname='Blank_Image')
cv2.setMouseCallback('Blank_Image', draw_rectangle)


# Showing the Image
img = np.zeros((512, 512, 3), dtype=np.int8)
while True:
    cv2.imshow('Blank_Image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
