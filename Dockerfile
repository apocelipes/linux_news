FROM python:3.6.7-alpine

USER root
# 更换源
RUN echo "http://mirrors.ustc.edu.cn/alpine/v3.8/main/" > /etc/apk/repositories

# 设置时区，安装python3和python第三方库依赖
ENV TIME_ZONE Asia/Shanghai
RUN apk add --no-cache -U tzdata \
    gcc \
    libc-dev \
    libffi-dev \
    openssl-dev \
    && ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime \
    && echo "${TIME_ZONE}" > /etc/timezone

# 安装依赖
COPY requirements.txt /requirements.txt
RUN pip install -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com --upgrade pip &&\
    pip install -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com -r /requirements.txt &&\
    rm -r /root/.cache/

# 创建服务用户，使用随机生成密码
# WARNING: 生产环境请替换此密码
RUN adduser -h /home/pydj -G root -D pydj &&\
    echo "pydj:bZfUZj9SdLoz0+4vqxrbeMS1zgIk" | chpasswd

USER pydj

# 挂载日志和代码
VOLUME ["/home/pydj/log","/home/pydj/app"]

# 进入代码目录
WORKDIR /home/pydj/app

EXPOSE 8000
