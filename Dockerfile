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
    libxml2-dev \
    libxslt-dev \
    && ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime \
    && echo "${TIME_ZONE}" > /etc/timezone

# 创建服务用户，使用随机生成密码
# WARNING: 生产环境请替换此密码
RUN addgroup -g 2000 pydj &&\
    adduser -u 2000 -h /home/pydj -G pydj -D pydj &&\
    echo "pydj:bZfUZj9SdLoz0+4vqxrbeMS1zgIk" | chpasswd

# 使用gosu替代su
RUN wget -O /usr/bin/gosu https://github.com/tianon/gosu/releases/download/1.11/gosu-amd64 &&\
    chmod +x /usr/bin/gosu &&\
    gosu nobody true

# 安装依赖
COPY requirements.txt /requirements.txt
RUN pip install -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com --upgrade pip &&\
    pip install -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com -r /requirements.txt &&\
    rm -r /root/.cache/

# 挂载日志
VOLUME ["/home/pydj/log"]

COPY . /home/pydj/app

# 进入代码目录
WORKDIR /home/pydj/app

EXPOSE 8000
