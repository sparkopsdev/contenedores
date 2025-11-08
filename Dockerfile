FROM python:3.12-slim

WORKDIR /personAPI

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "runserver.py"]