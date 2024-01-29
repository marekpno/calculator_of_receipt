import cv2
import code2flow
import pytesseract
from recipe_conventer_function import img_set, contours, resize, save_data

# parameteres std   threshold_value = 135 psm_config = 6 oem_config = 1
min_contour_width = 1000
min_contour_height = 500
threshold_value = 135
psm_config = 6
oem_config = 1
screen_size = (1366, 768)

# paths
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
code2flow.dot_path = r'C:\Program Files\Graphviz\bin\dot.exe'

# Load of raw data
path_to_raw = r'C:\Users\Marek\Desktop\python_291223_cost_of_life\raw\177.jpg'
img = cv2.imread(path_to_raw)


gray, thresh = img_set(img, threshold_value)

img, text = contours(thresh, min_contour_width, min_contour_height, img, psm_config, oem_config)

img_resized, img_resized_grey = resize(screen_size, img, gray)

# show img and img_gray
cv2.imshow('Original', img_resized)
cv2.imshow('grey', img_resized_grey)
cv2.waitKey(0)
cv2.destroyAllWindows()

save = save_data(path_to_raw, img, text)

