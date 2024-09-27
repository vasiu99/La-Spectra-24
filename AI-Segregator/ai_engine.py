import cv2
import numpy as np
from constants import *

class ai_engine:

    def calculate_cendroid(self, x, y, w, h):
        x1 = int(w / 2)
        y1 = int(h / 2)
        cx = x + x1
        cy = y + y1
        return cx, cy


    def capture_image( self):
        camera = cv2.VideoCapture(1)

        # Set Resolution
        camera.set(3, 1280)
        camera.set(4, 720)

        # Adjust camera lighting
        for i in range(30):
            temp = camera.read()
        retval, img = camera.read()
        cv2.imwrite(PATH_IMG,img)
        del(camera)

    def process_capturedimage(self):
        arm_return_status = False
        input_img = cv2.imread(PATH_IMG)
        img = cv2.resize(input_img, IMAGE_RESOLUTION)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # define range of red color in HSV
        lower_red = np.array(LOWER_RED_LIMIT)
        upper_red = np.array(UPPER_RED_LIMIT)

        # define range of green color in HSV
        lower_green = np.array(LOWER_GREEN_LIMIT)
        upper_green = np.array(UPPER_GREEN_LIMIT)

        # define range of blue color in HSV
        lower_blue = np.array(LOWER_BLUE_LIMIT)
        upper_blue = np.array(UPPER_BLUE_LIMIT)

        # create a mask for red color
        mask_red = cv2.inRange(hsv, lower_red, upper_red)
        # create a mask for green color
        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        # create a mask for blue color
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        # find contours in the red mask
        contours_red, _ = cv2.findContours(
            mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )
        # find contours in the green mask
        contours_green, _ = cv2.findContours(
            mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )
        # find contours in the blue mask
        contours_blue, _ = cv2.findContours(
            mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )
        # loop through the red contours and draw a rectangle around them

        cv2.line(img, L1_UPPER_LIMIT_DYNAMIC, L1_LOWER_LIMIT_DYNAMIC, RED, 2)
        cv2.line(img, L2_UPPER_LIMIT_DYNAMIC, L2_LOWER_LIMIT_DYNAMIC, COLOR1, 2)
        cv2.line(img, L3_UPPER_LIMIT_DYNAMIC, L3_LOWER_LIMIT_DYNAMIC, COLOR2, 2)

        foundBlue = 0
        foundGreen = 0
        foundRed = 0

        status = False
        # loop through the blue contours and draw a rectangle around them
        for cnt in contours_blue:
            contour_area = cv2.contourArea(cnt)
            if contour_area > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(
                    img,
                    BLUE_COLOR,
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (255, 0, 0),
                    2,
                )
                cx, cy = self.calculate_cendroid(x, y, w, h)
                cv2.circle(img, (cx, cy), 1, (0, 0, 255), 2)
                if cy > 300 and cx > 75 and cx < 1151:
                    print("Blue color found.")
                    foundBlue += 1


        # loop through the green contours and draw a rectangle around them
        for cnt in contours_green:
            contour_area = cv2.contourArea(cnt)
            if contour_area > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(
                    img,
                    GREEN_COLOR,
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 255, 0),
                    2,
                )
                cx, cy = self.calculate_cendroid(x, y, w, h)
                cv2.circle(img, (cx, cy), 1, (0, 0, 255), 2)
                if cy > 300 and cx > 75 and cx < 1151:
                    print("Green color found.")
                    foundGreen += 1

        for cnt in contours_red:
            contour_area = cv2.contourArea(cnt)
            if contour_area > 1000:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(
                    img,
                    RED_COLOR,
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 0, 255),
                    2,
                )
                cx, cy = self.calculate_cendroid(x, y, w, h)
                cv2.circle(img, (cx, cy), 1, (0, 0, 255), 2)
                if cy > 300 and cx > 75 and cx < 1151:
                    print("Red color found.")
                    foundRed += 1
        colors = {}
        colors[RED_COLOR] = foundRed
        colors[BLUE_COLOR] = foundBlue
        colors[GREEN_COLOR] = foundGreen

        sorted_colors = dict(sorted(colors.items(), key=lambda item: item[1], reverse=True))
        dominant_color = max(sorted_colors, key=sorted_colors.get)
        cv2.imwrite(SAVED_IMAGE_PATH, img)
        return dominant_color




