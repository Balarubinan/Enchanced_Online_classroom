import cv2

# capturing video from
vid = cv2.VideoCapture(0)

class CustomCam():

    def __init__(self):
        super(CustomCam, self).__init__()

    def get_frame(self):
        ret, frame = vid.read()
        return(frame.tobytes())

# print(CustomCam().get_frame())