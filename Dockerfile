FROM ubuntu:20.04

EXPOSE 8888

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --yes --no-install-recommends \
    python3

COPY . /code

CMD ["python3", "/code/test_docker.py"]