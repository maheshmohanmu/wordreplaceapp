FROM python:3.10-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
#EXPOSE 5000
#ENTRYPOINT [ "python" ]
#CMD [ "api.py" ]