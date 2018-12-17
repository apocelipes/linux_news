#!/bin/sh

# wait for redis
sleep 10

celery -A linux_news worker -l info -B -f /home/pydj/log/celery.log