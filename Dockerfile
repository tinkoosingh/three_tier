FROM python:3.11.4-slim-bookworm
COPY requirements.txt ./requirements.txt /flask_app/
COPY . . /flask_app/
WORKDIR /flask_app
RUN pip3 install -r requirements.txt
#ENTRYPOINT [ "python3" ]
CMD [ "python","app.py" ]