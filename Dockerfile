FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /project

# Install Git
RUN apt-get update && apt-get install -y git

# Clone the repository
RUN git clone https://github.com/tracebackerror/ecommerce /project

# Install project dependencies and migrations
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

# Run the applicatio
CMD python manage.py runserver 0.0.0.0:8000