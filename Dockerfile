FROM python:3.10-alpine

RUN pip3 install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
