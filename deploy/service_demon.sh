#!/bin/bash
PROJECT_DIR=/home/cobpc/website

cd ${PROJECT_DIR}
source bin/activate
source bin/postactivate

exec gunicorn -c ${PROJECT_DIR}/cobpc/deploy/gunicorn.conf.py core.wsgi