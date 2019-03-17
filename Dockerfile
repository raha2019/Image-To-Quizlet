FROM python:3

RUN pip install numpy pandas matplotlib ipython Pillow pytesseract

RUN apt update && apt install -y python-opencv
