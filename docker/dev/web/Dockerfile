FROM python:3.8.5-alpine
MAINTAINER alexander

ENV HOME /usr/src/web
# set work directory
WORKDIR $HOME
ENV MY alexander
# set environment variables

ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1 \
	TZ=Europe/Yekaterinburg \
	LANG=C.UTF-8

# install dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev openssl libffi-dev openssl-dev \
    # install Pillow dependencies
    && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev \
	&& pip install --upgrade pip

COPY ./web/requirements.txt $HOME/requirements.txt

RUN pip install -r $HOME/requirements.txt
# copy entrypoint.sh
COPY ./docker/dev/web/entrypoint.sh /entrypoint.sh
# copy project
COPY ./web/ /usr/src/web/
RUN chmod +x /entrypoint.sh
