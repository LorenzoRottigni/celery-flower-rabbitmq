FROM python:3.9

USER root

RUN mkdir -p /usr/src/app/
RUN mkdir -p /opt/venv/

RUN chown -R daemon:daemon /usr/src/app/
RUN chown -R daemon:daemon /opt/venv/

USER daemon

WORKDIR /usr/src/app

COPY . .

# create new virtual environment to isolate dependencies and to create an additional security layer
RUN python -m venv /opt/venv
# active venv by assigning environment variable instead of activating it using /venv/bin/activate
ENV PATH="/opt/venv/bin:$PATH"

RUN /opt/venv/bin/pip install --upgrade pip
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

CMD ["celery", "-A", "celery_worker.app", "worker", "--loglevel=debug"]