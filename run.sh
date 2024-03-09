#!/bin/bash

# Deploy Docker stack
docker run --name my-mongodb --rm -d -p 27017:27017 mongo

# Start uvicorn server
uvicorn main:app --reload
