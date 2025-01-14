FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py .

# Send python output to stdout and stderr
ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]
