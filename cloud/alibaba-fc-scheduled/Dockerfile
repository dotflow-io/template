FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -e .

ENTRYPOINT ["python", "-c", "from handler import handler; handler({}, None)"]
