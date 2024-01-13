import cv2
import pytesseract
# Set grey color
# Set whitch pixcels are white or black (text)
def img_set(img, threshold_value):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
    return  gray, thresh

# Find countour
# Check any coountours
# exception of noise
# change roi on gray
# Read text using pytesseract
# add rectangle in text area
def contours(thresh, min_contour_width, min_contour_height, img, psm_config, oem_config):
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > min_contour_width and h > min_contour_height:
            # take are from img
            roi = img[y:y + h, x:x + w]
            roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(roi_gray, config=f'--psm {psm_config} --oem {oem_config}')
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            return img, text
# resize output photo
# Calculate the new width based on the desired height (screen_size[1])
    # Resize the image while maintaining the aspect ratio
def resize(screen_size, img, gray):
    original_height, original_width, _ = img.shape
    aspect_ratio = original_width / original_height
    new_width = int(screen_size[1] * aspect_ratio)
    img_resized = cv2.resize(img, (new_width, screen_size[1]))
    img_resized_grey = cv2.resize(gray, (new_width, screen_size[1]))
    return img_resized, img_resized_grey


# save data
# Save output txt
# match name of raw img to text data file
def save_data(path_to_raw, img, text):
    image_name = path_to_raw.split('.')[0]
    cv2.imwrite(f'{image_name}_output_image.jpg', img)
    txt_path = f'{image_name}_output_text.txt'
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)
        return print(f"text saved to file: {txt_path}")