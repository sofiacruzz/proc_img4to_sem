import cv2
import numpy as np

def draw_rectangle(event, x, y, flags, params):
    global x_init, y_init, drawing, top_left_pt, bottom_right_pt

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x_init, y_init = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            top_left_pt = (min(x_init,x), min(y_init,y))
            bottom_right_pt = (max(x_init, x), max(Y_init, y))
            img[y_init:y, x_init:x] = 255 -img[y_init:y, x_init:x]
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        top_left_pt = (min(x_init,x), min(y_init,y))
        bottom_right_pt = (max(x_init,x), max(y_init,y))
        img[y_init:y, x_init:x] = 255 - img[y_init:y, x_init:x]

if __name__ == '__main__':
    drawing = False
    top_left_pt, bottom_right_pt = (-1,-1),(-1,-1)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IDError("Lo siento, no se detecto la camara :(!!!!")
    cv2.namedWindow('Ventana')
    cv2.setMouseCallback('Ventana', draw_rectangle)

    while True:
        ret, frame = cap.read()
        ksize=(30,30)
        img = cv2.resize(frame, None, fx= 1.5, fy=1.5, interpolation = cv2.INTER_AREA)
        #img= cv2.resize(frame,none,)

        (x0,y0), (x1,y1) = top_left_pt, bottom_right_pt

        blur= cv2.blur(img,ksize)

        img[y0:y1, x0:x1] = blur[y0:y1, x0:x1]
        cv2.imshow('Ventana', img)

        c = cv2.waitKey(1)
        if c == 27:
            break
cap.release()
cv2.destroyAllWindows()
