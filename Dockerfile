FROM alpine:3.8

USER root
# 更换源
RUN echo "http://mirrors.ustc.edu.cn/alpine/v3.8/main/" > /etc/apk/repositories

# 设置时区，安装python3和python第三方库依赖
ENV TIME_ZONE Asia/Shanghai
RUN apk add --no-cache -U tzdata \
    python3 \
    python3-dev\
    gcc \
    libc-dev \
    libffi-dev \
    openssl-dev \
    && ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime \
    && echo "${TIME_ZONE}" > /etc/timezone

# 安装依赖
COPY requirements.txt /requirements.txt
RUN pip3 install -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com --upgrade pip &&\
    pip3 install -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com -r /requirements.txt &&\
    rm -r /root/.cache/

# 挂载日志和代码
VOLUME ["/log","/app"]

# 进入代码所在目录
WORKDIR /app

EXPOSE 8000
