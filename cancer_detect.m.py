#!/usr/bin/env python
# coding: utf-8

import cv2

# Load the image
img = cv2.imread('/Users/keshavpareek/Downloads/F1.jpg')

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
