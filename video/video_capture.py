import cv2 as cv

def capture_video():
    print("instantiating resources...")
    cap = cv.VideoCapture("/dev/v4l/by-id/usb-GENERAL_GENERAL_WEBCAM-video-index0", cv.CAP_V4L2)

    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'XVID')

    outfile = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

    print("about to iterate through capture device...")
    while cap.isOpened():
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