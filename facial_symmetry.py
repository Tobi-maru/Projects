
import cv2
import time

image = cv2.imread('path of image')

if image is None:
    print("Error: Could not load the image.")
else:
    mirrored_image = cv2.flip(image, 1)

    n = 100  # Adjust this value to change the frequency (in ms)

    window_width = 800
    window_height = 800
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)  # Create a window with the ability to resize
    cv2.resizeWindow('Image', window_width, window_height) 

    while True:
        cv2.imshow('Image', image)
        key = cv2.waitKey(n)  # Wait for 'n' milliseconds
        
        cv2.imshow('Image', mirrored_image)
        key = cv2.waitKey(n)  # Wait for 'n' milliseconds

        if key == ord('q'):
            break

    cv2.destroyAllWindows()

