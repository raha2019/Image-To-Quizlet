from PIL import Image
from pytesseract import image_to_string
#import pytesseract
#import cv2
#import sys
#import numpy as np
#import os
#import main.py
#ap = argparse.ArgumentParser()
#args = vars(ap.parse_args())
#inputFile = str(sys.argv[-1])
#image = cv2.imread("output.jpg")
#print("text")
#print(pytesseract.image_to_string(Image.open('output.jpg')))
#print("text")
#print(("text").encode("utf-8"))
#print(pytesseract.image_to_string(Image.fromarray(img)))
#result = pytesseract.image_to_string('output.jpg', lang="eng")
#results = pytesseract.image_to_string(Image.open('output.jpg'))
#import output.jpg
#import pytesseract
#from PIL import Image, ImageEnhance, ImageFilter
#im = Image.open("output.jpg") # the second one
#text = pytesseract.image_to_string(Image.open('output.jpg')("utf-8"))
#sys.stdout.write(text)

img=Image.open("file:///Users/rahulgupta/Downloads/Image-Processor-For-Text-Extraction-master/put.jpg")

text=image_to_string(img)
print text
