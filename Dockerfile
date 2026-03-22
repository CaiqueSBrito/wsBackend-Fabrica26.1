FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY projeto_pokedex/requirements .
RUN pip install --upgrade pip && pip install -r requirements

COPY projeto_pokedex/ .

EXPOSE 8000

CMD ["gunicorn", "projeto_pokedex.wsgi:application", "--bind", "0.0.0.0:8000"]
    