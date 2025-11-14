# Docker image name: sanikanandpure/ml-damage-api

FROM python:3.11

RUN pip install tensorflow==2.15
RUN pip install Flask==3.0

COPY models /models
COPY api.py /api.py

EXPOSE 5000
CMD ["python", "api.py"]
