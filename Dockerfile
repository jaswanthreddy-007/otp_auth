FROM python:latest
RUN apt update -y
RUN apt install python3 -y
RUN pip install twilio pyotp
WORKDIR /usr/app/src

COPY otp.py ./


CMD [ "python", "./otp.py" ]
