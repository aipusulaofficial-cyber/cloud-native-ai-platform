FROM python:3.12-slim
WORKDIR /app
COPY . .
CMD ["python","-c","from cloud_platform import DeploymentValidator; print('deployment policy ready')"]
