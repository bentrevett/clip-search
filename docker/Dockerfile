FROM python:3.11

COPY docker/requirements.txt .
RUN pip install -r requirements.txt

COPY docker/index.faiss .
COPY docker/app.py .
COPY docker/mapping.json .
COPY model model

EXPOSE 5000

CMD ["python", "app.py"]