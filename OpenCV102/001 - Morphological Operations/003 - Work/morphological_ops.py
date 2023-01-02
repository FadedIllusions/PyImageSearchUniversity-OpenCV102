# python morphological_ops.py --image images/pyimagesearch_logo.png
# python morphological_ops.py --image images/pyimagesearch_logo_noise.png
# https://pyimagesearch.com/2021/04/28/opencv-morphological-operations


# Import Needed Packages
import argparse
import cv2

# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path To Input Image")
args = vars(ap.parse_args())


# Load Image, Convert To Grayscale, And Display
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.waitKey(0)

# --- Erosions ---
# Apply Series Of Erosions
for i in range(0,3):
	eroded = cv2.erode(gray.copy(), None, iterations=i+1)
	cv2.imshow("Eroded {} Times".format(i+1), eroded)
	cv2.waitKey(0)

# Perform Needed Cleanup
cv2.destroyAllWindows()


# Display Original Image Once Again
cv2.imshow("Original", image)
cv2.waitKey(0)

# -- Dilations --
# Apply Series Of Dilations
for i in range(0,3):
	dilated = cv2.dilate(gray.copy(), None, iterations=i+1)
	cv2.imshow("Dilated {} Times".format(i+1), dilated)
	cv2.waitKey(0)
	
# Perform Needed Cleanup
cv2.destroyAllWindows()


# -- Openings --
# (An Erosion Followed By A Dilation)
# Display Original Image
# Define Kernel Sizes
cv2.imshow("Original", image)
cv2.waitKey(0)
kernelSizes = [(3,3), (5,5), (7,7)]

# Iterate Over Kernel Sizes
for kernelSize in kernelSizes:
	# Construct Rectangular Kernel From Current Size
	# Apply Opening Operation
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
	opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
	cv2.imshow("Opening: ({},{})".format(
		kernelSize[0], kernelSize[1]), opening)
	cv2.waitKey(0)
	
# Perform Needed Cleanup
cv2.destroyAllWindows()


# -- Closing --
# (A Dilation Followed By An Erosion)
# Display Original Image
cv2.imshow("Original", image)
cv2.waitKey(0)

# Iterate Through Kernel Sizes
for kernelSize in kernelSizes:
	# Construct Rectangular Kernel From Current Size
	# Apply Closing Operation
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
	closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
	cv2.imshow("Closing: ({},{})".format(
		kernelSize[0], kernelSize[1]), closing)
	cv2.waitKey(0)
	
# Perform Needed Cleanup
cv2.destroyAllWindows()


# -- Morphological Gradient --
# The Difference (Subtraction) Between A Dilation And Erosion
# (Sort Of An "Outline Detection")
# Display Original Image
cv2.imshow("Original", image)
cv2.waitKey(0)

# Iterate Through Kernels
for kernelSize in kernelSizes:
	# Construct Rectangular Kernel From Current Size
	# Aplly Gradient Operation
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
	gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
	cv2.imshow("Gradient: ({},{})".format(
		kernelSize[0], kernelSize[1]), gradient)
	cv2.waitKey(0)
	
# Perform Needed Cleanup
cv2.destroyAllWindows()