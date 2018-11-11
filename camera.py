from PIL import Image
import cv2

cam = cv2.VideoCapture(0)


def get_webcam_image():
    ret_val, frame = cam.read()
    if not ret_val:
        raise ValueError("Can't read frame")
    cv2_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(cv2_image)
    return pil_image


if __name__ == "__main__":
    get_webcam_image()