FROM python:latest
ENV PS1="\[\e[0;33m\]|> RTC <| \[\e[1;35m\]\W\[\e[0m\] \[\e[0m\]# "

WORKDIR /RT_CLI
RUN pip install --no-cache-dir -r requirements.txt \
    && python setup.py install
WORKDIR /
ENTRYPOINT ["RTC"]
