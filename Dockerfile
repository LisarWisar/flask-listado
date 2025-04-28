FROM python:3.12-slim
RUN apt-get update && apt-get install -y openssh-server build-essential gcc curl && \
mkdir /var/run/sshd
RUN useradd -m -s /bin/bash usuario && \ echo "usuario:1234" | chpasswd
RUN sed -i 's/^#\?PasswordAuthentication.*/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN ssh-keygen -A
WORKDIR /app
COPY . .
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
EXPOSE 22 5000
CMD ["sh", "-c", "service ssh start && sleep 1 && python3 ./src/app.py & /usr/sbin/sshd -D -e"]


