FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
# Install gcc so Python packages such as MarkupSafe and SQLAlchemy can compile speedups.
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# Copy the current directory . in the project to the workdir . in the image.
COPY . .
CMD ["flask", "run"]