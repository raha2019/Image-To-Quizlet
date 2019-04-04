import re
import pytesseract
from PIL import Image
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

delimiter = "*-*"
text_delimiter = "[(][^(]*[)]"

def process_image(input_file):
    output = pytesseract.image_to_string(Image.open(input_file))
    flat = output.replace('\n',' ')
    entries = re.split("[(][^(]*[)]", flat)

    res = ""

    with open("defs.txt", "w") as fh:
        for entry in entries:
            if entry.strip() == '':
                continue

            split = entry.strip().split(" ")

            fh.write("{}{}{}\n".format(split[0], delimiter, " ".join(split[1:])))
            res += "{}{}{}<br />".format(split[0], delimiter, " ".join(split[1:]))

    return res
