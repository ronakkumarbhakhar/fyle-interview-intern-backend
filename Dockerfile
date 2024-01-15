FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN rm core/store.sqlite3
ENV FLASK_APP ./core/server.py
RUN flask db upgrade -d core/migrations/
RUN pytest -vvv -s tests/

EXPOSE 7755

CMD [ "gunicorn","-c","gunicorn_config.py","core.server:app" ]