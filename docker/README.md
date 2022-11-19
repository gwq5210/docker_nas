TrueNAS docker容器无法上网

cp /etc/docker/daemon.json /etc/docker/daemon-new.json

编辑这个daemon-new.json文档

vi /etc/docker/daemon-new.json

删除iptable，Bridge相关参数

编辑docker.service服务配置
vi /usr/lib/systemd/system/docker.service

找到在[Service]段下的

ExecStart=/usr/bin/dockerd 后面加入

--config-file=/etc/docker/daemon-new.json

重载配置
systemctl daemon-reload

重启docker
systemctl restart docker
