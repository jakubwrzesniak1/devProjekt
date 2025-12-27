FROM python:3.9-slim
WORKDIR /app
RUN pip install flask
COPY devapp.py .
EXPOSE 5000
CMD ["python", "devapp.py"]
