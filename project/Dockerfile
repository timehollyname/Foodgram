FROM python:3.8.5

WORKDIR /FoodGram

COPY requirements.txt /FoodGram/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /FoodGram/