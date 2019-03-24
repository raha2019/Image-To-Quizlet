FROM python:3

RUN apt update && apt install -y git cmake tesseract-ocr
RUN pip install numpy pandas matplotlib ipython Pillow pytesseract flask

# RUN cd / && git clone https://github.com/opencv/opencv.git && cd opencv && \
# 		mkdir build && cd build && cmake ../ && make && make install