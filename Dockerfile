FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY botinits.py botinits.py
COPY trash.py trash.py
COPY cleaning.py cleaning.py
COPY launching.py launching.py
COPY moneyreport.py moneyreport.py
CMD ["python3", "launching.py"]
