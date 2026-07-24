FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV OLLAMA_HOST=http://host.docker.internal:11434

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]