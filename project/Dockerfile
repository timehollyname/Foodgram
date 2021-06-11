FROM python:3.8.5

RUN apt-get update && apt-get upgrade && apt-get install wkhtmltopdf

WORKDIR /FoodGram/

COPY project/requirements.txt /FoodGram/

RUN pip install --upgrade pip && pip install -r ./requirements.txt

COPY ./ /FoodGram/