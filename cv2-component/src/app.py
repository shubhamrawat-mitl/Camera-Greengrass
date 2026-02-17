import cv2

def main():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Camera not found!")
        return

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        cv2.imshow("Camera Feed", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()