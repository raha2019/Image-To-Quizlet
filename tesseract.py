import pytesseract
from PIL import Image
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

input = "IMG_3352.jpeg"

output = pytesseract.image_to_string(Image.open(input))
print(output)
