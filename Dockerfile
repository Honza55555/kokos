# Použij lehký image s Pythonem
FROM python:3.10-slim

WORKDIR /app

# Zkopíruj požadavky a nainstaluj je
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Zkopíruj kód
COPY main.py .

# Spouštěcí příkaz
CMD ["python", "main.py"]
