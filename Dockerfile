FROM python:3.12

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install gunicorn

COPY requirements.txt .

RUN python -m pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir


COPY . .

ADD entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi"]