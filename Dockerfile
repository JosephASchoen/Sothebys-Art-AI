FROM ubuntu:latest
LABEL authors="josep"

ENTRYPOINT ["top", "-b"]
