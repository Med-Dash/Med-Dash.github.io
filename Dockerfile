# For more information, please refer to https://aka.ms/vscode-docker-python
ARG BASE_CONTAINER=ucsdets/datahub-base-notebook:2022.3-stable

FROM $BASE_CONTAINER

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
RUN pip install --no-cache-dir pandas numpy scikit-learn seaborn matplotlib pytz requests

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "run.py"]