FROM python:2.7.13-alpine

#https://github.com/SeleniumHQ/selenium/issues/3808
RUN pip install selenium==3.0.1

COPY . /app/

WORKDIR /app/

CMD ["python", "main.py"]
