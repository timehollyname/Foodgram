FROM python:3.8.5

RUN apt-get update && apt-get upgrade -y && apt-get install wkhtmltopdf -y

WORKDIR /FoodGram/

COPY project/requirements.txt /FoodGram/

RUN pip install --upgrade pip && pip install -r ./requirements.txt

COPY ./ /FoodGram/