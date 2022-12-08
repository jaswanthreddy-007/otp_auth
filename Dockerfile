FROM python:latest
RUN apt update -y
RUN apt install python3 -y
RUN pip install twilio pyotp
WORKDIR K:\Hackathon\otp_auth

COPY otp.py ./
COPY twilliokey.txt ./


CMD [ "python", "./otp.py" ]
