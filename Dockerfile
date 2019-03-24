FROM python:3

RUN pip install numpy pandas matplotlib ipython Pillow pytesseract flask
RUN apt update && apt install -y git cmake 

RUN cd / && git clone https://github.com/opencv/opencv.git && cd opencv && \
		mkdir build && cd build && cmake ../ && make && make install 
