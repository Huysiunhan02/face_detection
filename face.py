
from ultralytics import YOLO
import cvzone
import cv2
import math


def main():
    
    cap = cv2.VideoCapture(0)
    model = YOLO('best.pt')


    # Reading the classes
    classnames = ['face']

    while True:
        ret,frame = cap.read()
        frame = cv2.resize(frame,(640,480))
        result = model(frame,stream=True)

        # Getting bbox,confidence and class names informations to work with
        for info in result:
            boxes = info.boxes
            for box in boxes:
                confidence = box.conf[0]
                confidence = math.ceil(confidence * 100)
                Class = int(box.cls[0])
                if confidence > 50:
                    x1,y1,x2,y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1),int(y1),int(x2),int(y2)
                    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),5)
                    cvzone.putTextRect(frame, f'{classnames[Class]} {confidence}%', [x1 + 8, y1 + 0],
                                    scale=1.5,thickness=2)
        cv2.imshow('frame',frame)
        k = cv2.waitKey(1)
        if(k % 256 == 27):
            break
        
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
# Running real time from webcam
