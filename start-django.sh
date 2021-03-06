#!/bin/sh

# 等待db启动
sleep 10

# 初始化数据库
python3 manage.py migrate
python3 manage.py loaddata initial_data.json

if [[ $(whoami) == 'root' ]]; then
    chown -R pydj /home/pydj/log
    chown -R pydj /home/pydj/app
    # linux_news为wsgi.py所在的包的名字
    gosu pydj gunicorn -c /home/pydj/app/gunicorn.conf linux_news.wsgi:application
fi