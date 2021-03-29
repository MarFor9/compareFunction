FROM ubuntu:20.04
FROM python:3.6
RUN git clone https://github.com/Unidata/MetPy.git
WORKDIR /MetPy
RUN pip install .
COPY . metpy.py
