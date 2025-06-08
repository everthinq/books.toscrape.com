FROM python:3-alpine

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY requirements.txt ./requirements.txt
RUN pip3 install --no-cache-dir -r ./requirements.txt

# Copy source code
COPY . ./

CMD uvicorn fast_api.main:app --host 0.0.0.0 --port 8080