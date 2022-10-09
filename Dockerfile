FROM python:3
RUN git clone https://github.com/MatiasBoldrini/4_en_linea.git
WORKDIR /4_en_linea
RUN pip install -r requirements.txt
CMD ["python3", "test_4_en_linea.py"]