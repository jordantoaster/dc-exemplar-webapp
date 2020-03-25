FROM python:3.6-slim
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
WORKDIR /src
COPY src/ .
RUN ls
CMD ["flask", "run"]