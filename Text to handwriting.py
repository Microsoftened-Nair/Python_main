import pywhatkit as kit
import cv2

kit.text_to_handwriting("Never gonna give you up", save_to="handwriting.png")
img = cv2.imread("handwriting.png")
cv2.imshow("Text to Handwriting", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
