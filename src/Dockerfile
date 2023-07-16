FROM python:3.9-slim
WORKDIR /app/src/
COPY requirements.txt .
RUN apt-get update
RUN pip install -r requirements.txt --no-cache-dir
ENV PYTHONPATH "${PYTHONPATH}:/app"
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]