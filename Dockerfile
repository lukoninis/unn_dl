FROM ubuntu:20.04
LABEL maintainer="lukoninis@yandex.ru"
RUN apt update && apt -y upgrade && apt -y install bash python3 python3-pip git && rm -rf /var/lib/apt/lists/*
RUN pip3 install keras pillow matplotlib scikit-learn scikit-image opencv-python pydot tensorflow PyQt5
RUN git clone https://github.com/ialhashim/DenseDepth.git /opt
COPY ./nyu.h5 /opt/
COPY ./test.py /opt/
RUN mkdir /opt/out
WORKDIR /opt
ENTRYPOINT ["python3",  "test.py"]
