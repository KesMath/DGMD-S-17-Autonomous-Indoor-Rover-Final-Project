import cv2 as cv

def capture_video():
    cap = cv.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'MP4V')

    outfile = cv.VideoWriter('output.mp4', fourcc, 20.0, (640,  480))

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
    
    cap.release()
    outfile.release()
    cv.destroyAllWindows()

def main():
    capture_video()