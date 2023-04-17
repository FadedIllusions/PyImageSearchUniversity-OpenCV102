# python blurring.py
# https://pyimagesearch.com/2021/04/28/opencv-smoothing-and-blurring

# Import Needed Packages
import argparse
import cv2

# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/adrian.png",
				help="Path To Input Image")
args = vars(ap.parse_args())


# Load Image And Display
# Initialize List Of Kernel Sizes
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)
kernelSizes = [(3,3), (9,9), (15,15)]

# Iterate Over Kernel Sizes
for (kX, kY) in kernelSizes:
	# Apply An "Average" Blur To Image Using Current Kernel Size
	blurred = cv2.blur(image, (kX,kY))
	cv2.imshow("Average ({},{})".format(kX, kY), blurred)
	cv2.waitKey(0)
	
# Perform Needed Cleanup And Redisplay Original Image
cv2.destroyAllWindows()
cv2.imshow("Original", image)
cv2.waitKey(0)