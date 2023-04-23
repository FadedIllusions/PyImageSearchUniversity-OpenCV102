# Usage
# python adaptive_thresholding.py  --image images/steve_jobs.png

# Import Needed Packages
import argparse
import cv2

# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
				help="Path To Input Image")
args = vars(ap.parse_args())

# Load And Display Image
image = cv2.imread(args["image"])
cv2.imshow("Image", image)
cv2.waitKey(0)

# Convert Image To Grayscale And Blur
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7,7), 0)

# Apply Simple Thresholding With Hardcoded Value
(T, threshInv) = cv2.threshold(blurred, 230, 255,
					cv2.THRESH_BINARY_INV)
cv2.imshow("Simple Thresholding", threshInv)
cv2.waitKey(0)

# Apply Otsu's Automatic Thresholding
(T, threshInv) = cv2.threshold(blurred, 0, 255,
					cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Otsu Thresholding", threshInv)
cv2.waitKey(0)

# Apply Adaptive Thresholding
# (Examines Neighborhoods Of Pixels And Adaptively Thresholds Each)
thresh = cv2.adaptiveThreshold(blurred, 255,
					cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10)
cv2.imshow("Mean Adaptive Thresholding", thresh)
cv2.waitKey(0)

# Apply Adaptive Thresholding With Gaussian Weighting
thresh = cv2.adaptiveThreshold(blurred, 255,
					cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 4)
cv2.imshow("Gaussian Adaptive Thresholding", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()