FROM python:3.9

WORKDIR /app


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0.0.0.0:8000"]
