#!/bin/bash
cd /app
echo "Starting Deployment" 
gunicorn -b :5000 --reload --access-logfile - --error-logfile - app:app
