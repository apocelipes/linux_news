#!/bin/sh

# running as root in docker
export C_FORCE_ROOT="true"

# wait for redis
sleep 10

celery -A linux_news worker -l info -B -f /log/celery.log