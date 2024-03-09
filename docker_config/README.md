# TrueNAS docker容器无法上网

```shell
cp /etc/docker/daemon.json /etc/docker/daemon-new.json
```

编辑这个daemon-new.json文档

```shell
vi /etc/docker/daemon-new.json
```

删除iptable，Bridge相关参数

编辑docker.service服务配置

```shell
vi /usr/lib/systemd/system/docker.service
```

找到在[Service]段下的

ExecStart=/usr/bin/dockerd 后面加入

--config-file=/etc/docker/daemon-new.json

重载配置

```shell
systemctl daemon-reload
```

重启docker

```shell
systemctl restart docker
```

在 网站根目录/config/config.php 的最后一行中添加

  'default_phone_region' => 'CN',
