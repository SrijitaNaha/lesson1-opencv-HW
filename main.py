import cv2

# Read the image
image = cv2.imread('ash.png')

# Split the image into BGR channels
b, g, r = cv2.split(image)

# Display the original image and BGR channels
cv2.imshow('Original Image', image)
cv2.imshow('Blue Channel', b)
cv2.imshow('Green Channel', g)
cv2.imshow('Red Channel', r)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray)

# Save the grayscale image
cv2.imwrite('grayscale_image.jpg', gray)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()