import re
import pytesseract
from PIL import Image
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

input = "IMG_3354.jpeg"

output = pytesseract.image_to_string(Image.open(input))
print(output)

delimiter = "*-*"
text_delimiter = "[(][^(]*[)]"

flat = output.replace('\n',' ')
entries = re.split("[(][^(]*[)]", flat)

with open("defs.txt", "w") as fh:
    for entry in entries:
        if entry.strip() == '':
            continue

        split = entry.strip().split(" ")

        fh.write("{}{}{}\n".format(split[0], delimiter, " ".join(split[1:])))
