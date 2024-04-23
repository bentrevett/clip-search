FROM python:3.11

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

COPY model/open_clip_pytorch_model.bin model/open_clip_pytorch_model.bin
COPY model/open_clip_config.json model/open_clip_config.json
COPY model/special_tokens_map.json model/special_tokens_map.json
COPY model/tokenizer_config.json model/tokenizer_config.json
COPY model/tokenizer.json model/tokenizer.json


EXPOSE 5000

CMD ["python", "app.py"]