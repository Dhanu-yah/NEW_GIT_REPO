FROM python:3.13
WORKDIR /app
COPY hello.py .
CMD ["python","hello.py"]
