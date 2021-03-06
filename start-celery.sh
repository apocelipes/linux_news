#!/bin/sh

# wait for redis
sleep 10

if [[ $(whoami) == 'root' ]]; then
    chown -R pydj /home/pydj/log
    chown -R pydj /home/pydj/app
    gosu pydj celery -A linux_news worker -l info -B -f /home/pydj/log/celery.log
fi