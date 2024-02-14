FROM python:3.10

ADD main.py .
ADD keywords.txt .
ADD save_session.py .

RUN pip install telethon telebot

CMD ["python", "./main.py"]