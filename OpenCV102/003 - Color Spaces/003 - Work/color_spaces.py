# Usage
# python color_space.py

# Import Needed Packages
import argparse
import cv2

# Construct Argument Parser And Parse Arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="images/adrian.png",
	help="Path To Input Image")
args = vars(ap.parse_args())

# Load And Display Image
image = cv2.imread(args["image"])
cv2.imshow("RGB", image)
cv2.waitKey(0)

# Iterate Over Image Channels And Display
for (name, chan) in zip (("B", "G", "R"), cv2.split(image)):
	cv2.imshow(name,chan)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert Image To HSV And Display
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
cv2.waitKey(0)

# Iterate Over HSV Channels And Display
for (name, chan) in zip(("H","S","V"), cv2.split(hsv)):
	cv2.imshow(name,chan)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Covert To L*A*B* And Display
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("L*A*B*", lab)
cv2.waitKey(0)

# Iterate Over L*A*B* And Display
for (name, chan) in zip(("L*", "A*", "B*"), cv2.split(lab)):
	cv2.imshow(name, chan)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Display Original And Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
