import cv2
import matplotlib.pyplot as plt

img = cv2.imread("sample.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Downsample directly
alias = cv2.resize(img, (80,80))
alias = cv2.resize(alias, (img.shape[1], img.shape[0]))

# Anti-aliasing using Gaussian Blur
blur = cv2.GaussianBlur(img,(5,5),0)
anti = cv2.resize(blur,(80,80))
anti = cv2.resize(anti,(img.shape[1],img.shape[0]))

plt.subplot(1,2,1)
plt.imshow(alias)
plt.title("Aliasing")

plt.subplot(1,2,2)
plt.imshow(anti)
plt.title("Anti-Aliasing")

plt.show()