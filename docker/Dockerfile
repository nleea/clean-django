FROM python:3.11

WORKDIR /app

COPY /requirements.txt /app

RUN python -m ensurepip --upgrade
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt 

COPY ./ /app/

EXPOSE 8000

ENTRYPOINT [ "python", "manage.py" ]

CMD [ "runserver", "0.0.0.0:8000" ]