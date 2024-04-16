import cv2
import numpy as np
import sys

def process_image(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Resize the image
    img = cv2.resize(img, (200, 200))

    # Convert the image to grayscale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale image
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

    # Threshold the blurred image
    ret, thresh = cv2.threshold(imgBlur, 140, 190, 0)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on a copy of the original image
    img_res = img.copy()
    img_cancer = cv2.drawContours(img_res, contours, -1, (125, 125, 0), 2)

    # Display the images
    cv2.imshow('Original Image', img)
    cv2.imshow('Contours', img_cancer)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Calculate the number of detected circles
    num_circles = len(contours)

    # Check if contours are detected
    if num_circles < 1:
        print("No circles detected. No cancer cells found.")
    else:
        print("Number of Circles Detected:", num_circles)

        # Convert the (x, y) coordinates and radius of the contours to integers
        contours = np.round(contours).astype("int")

        # Calculate the average radius of the detected circles
        avg_radius = np.mean(contours[:, :, 2])
        print("Average Radius of Circles:", avg_radius)

        # Determine the condition based on the number of circles detected and the average radius
        if 0.5 <= avg_radius < 1:
            print("High myeloid cell concentration.")
        elif 1 <= avg_radius < 8:
            print("Initial Stage Leukemia.")
        elif avg_radius >= 8:
            print("Advanced Stage Leukemia.")

    # Exit the script
    sys.exit()

def main():
    image_path = '/Users/keshavpareek/Downloads/F1.jpg'
    process_image(image_path)

if __name__ == "__main__":
    main()
