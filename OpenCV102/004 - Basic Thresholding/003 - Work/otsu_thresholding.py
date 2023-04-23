# Usage
# python otsu_thresholding.py --image images/coins01.png

# Import Needed Packages
import argparse
import cv2

# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True, help="Path To Input Image")
args = vars(ap.parse_args())

# Load And Display Image
image = cv2.imread(args["image"])
cv2.imshow("Image", image)
cv2.waitKey(0)

# Convert Image To Grayscale And Blur
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7,7), 0)

# Apply Otsu's Automatic Thresholding
# (Which Determines The Best Threshold Value)
(T, threshInv) = cv2.threshold(blurred, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Threshold", threshInv)
print("[INFO] Otsu's Thresholding Value: {}".format(T))
cv2.waitKey(0)

# Visualize Only Masked Region Of Image
masked = cv2.bitwise_and(image, image, mask=threshInv)
cv2.imshow("Output", masked)
cv2.waitKey(0)

# Perform Needed Cleanup
cv2.destroyAllWindows()