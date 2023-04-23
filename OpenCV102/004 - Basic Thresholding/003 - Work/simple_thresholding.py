# Usage
# python simple_thresholding.py --image images/coins01.png

# Import Needed Packages
import argparse
import cv2

# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True, help="Path To Iput Image")
args = vars(ap.parse_args())

# Load And Display Image
image = cv2.imread(args["image"])
cv2.imshow("Image", image)
cv2.waitKey(0)

# Convert Image To Grayscale And Blur
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7,7), 0)

# Apply Basic Thresholding
# First Param: Image We Want To Threshold
# Second Param: Threshold Check (In This Case, 200)
#   -- If Pixel Value Is Greater Than Threshold, It Is Set To Black,
#      Otherwise It Is Set To White
(T, threshInv) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)
cv2.waitKey(0)

# Using Normal Thresholding (Rather Than Inverse)
(T, thresh) = cv2.threshold(blurred, 200, 25, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)
cv2.waitKey(0)
# Visualize Only The Masked Regions Of Image
masked = cv2.bitwise_and(image, image, mask=threshInv)
cv2.imshow("Output", masked)
cv2.waitKey(0)

# Perform Needed Cleanup
cv2.destroyAllWindows()