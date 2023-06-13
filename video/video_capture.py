import cv2 as cv
# https://docs.opencv.org/4.x/d4/d15/group__videoio__flags__base.html#gga023786be1ee68a9105bf2e48c700294da0c5f2eb9d2d43fb3582583203160a419

def capture_video():
    print("instantiating resources...")
    cap = cv.VideoCapture("/dev/v4l/by-id/usb-GENERAL_GENERAL_WEBCAM-video-index0")

    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'XVID')

    outfile = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

    print("about to iterate through capture device...")
    while cap.isOpened():
        print("capture is open...")
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        frame = cv.flip(frame, 0)
        # write the flipped frame
        outfile.write(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
    
    print("releasing resources...")
    cap.release()
    outfile.release()
    cv.destroyAllWindows()

def main():
    capture_video()

if __name__ == '__main__':
    main()