import cv2

image = cv2.imread('/Users/Work/Desktop/sccc.png')

cv2.waitKey(0)

print image.shape

r = 28.0 / image.shape[1]
dim = (28, int(image.shape[0] * r))

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resized", resized)