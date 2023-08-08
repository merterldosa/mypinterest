FROM python:3.9.2

WORKDIR /home/

RUN git clone https://github.com/merterldosa/mypinterest.git

WORKDIR /home/mypinterest/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure--2+(e9ezp8k^q2sqorm(prl52yextl!qpaqc22wib+aezslx8u" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]