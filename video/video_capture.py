import cv2 as cv

class VideoCapture():
    def __init__(self):
        self.cap = None
        self.outfile = None

    def capture_video(self):
        self.cap = cv.VideoCapture(0)

        # Define the codec and create VideoWriter object
        fourcc = cv.VideoWriter_fourcc(*'XVID')

        self.outfile = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            self.outfile.write(frame)
            cv.imshow('frame', frame)
            if cv.waitKey(1) == ord('q'):
                self.free_video_resources()
                break

    def free_video_resources(self):      
        # Release everything when job is finished
        print("releasing resources...")
        self.cap.release()
        self.outfile.release()
        cv.destroyAllWindows()

def main():
    vid = VideoCapture()
    vid.capture_video()

if __name__ == '__main__':
    main()