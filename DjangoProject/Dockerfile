FROM python:3.9.5

# set work directory
WORKDIR /home/DjangoProject

# create the django user and group
RUN groupadd --gid 1000 django \
    && useradd --uid 1000 --gid django --shell /bin/bash --create-home django 

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./Web/requirements.txt /home/DjangoProject/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY ./Web /home/DjangoProject/

# chown all the files to the django user
RUN chown -R django:django /home/DjangoProject/

# run entrypoint.sh
RUN ["chmod", "+x", "/home/DjangoProject/entrypoint_web.sh"]