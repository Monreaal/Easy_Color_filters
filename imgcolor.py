import cv2
import numpy as np
import ctypes

image = cv2.imread('DSCF8234.jpg')
if image is None:
    print("No se pudo cargar la imagen.")
    exit()

original = image.copy()

A = np.array([[1.5,0,0],
              [0,1,0],
              [0,0,1]])
c = np.array([0,0,0])

img_float = image.astype(np.float32)
transformed = np.dot(img_float, A.T) + c
transformed = np.clip(transformed, 0, 255).astype(np.uint8)

user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

h, w = transformed.shape[:2]

scale = min(screen_width / w, screen_height / h)

new_w = int(w * scale * 0.8)  # 80% para margen
new_h = int(h * scale * 0.8)

original_resized = cv2.resize(original, (new_w, new_h), interpolation=cv2.INTER_AREA)
transformed_resized = cv2.resize(transformed, (new_w, new_h), interpolation=cv2.INTER_AREA)

cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.namedWindow('Transformada', cv2.WINDOW_NORMAL)

cv2.imshow('Original', original_resized)
cv2.imshow('Transformada', transformed_resized)

cv2.waitKey(0)
cv2.destroyAllWindows()