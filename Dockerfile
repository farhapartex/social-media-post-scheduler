FROM python:3.10-slim

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV POSTGRES_USER=user \
    POSTGRES_PASSWORD=password \
    POSTGRES_DB=social_db \
    POSTGRES_HOST=social_db \
    POSTGRES_PORT=5432

EXPOSE 8000

#COPY wait-for-it.sh /wait-for-it.sh

RUN chmod +x wait-for-it.sh

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]