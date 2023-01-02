# python morphological_hats.py --image images/car.png
# https://pyimagesearch.com/2021/04/28/opencv-morphological-operations


# Import Needed Packages
import argparse
import cv2

# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Input Image")
args = vars(ap.parse_args())

# Load Image And Convert To Grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Construct Rectangular Kernel (13x5) And Apply Blackhat Operation
# Which Enables Us To Find Dark Regions On Light Background
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13,5))
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)

# Similarly, A Tophot (Also Called A "Whitehat") Operation
# Will Enable Us To Find Light Regions On A Dark Background
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)

# Display Output Images
cv2.imshow("Original", image)
cv2.imshow("Blackhat", blackhat)
cv2.imshow("Whitehat", tophat)
cv2.waitKey(0)

# Perform Needed Cleanup
cv2.destroyAllWindows()