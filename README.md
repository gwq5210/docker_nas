# photoprism安装

```text
services.photoprism.deploy.resources.reservations value Additional properties are not allowed ('devices' was unexpected)
```

解决方法：https://github.com/docker/compose/issues/8142

```sh
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/bin/docker-compose
sudo chmod +x /usr/bin/docker-compose
docker-compose --version
```

As other answers have mentioned, the solution is don't use localhost. Even changing to 127.0.0.1 appears to be sufficient *(see note below)

Explanation:
No such file or directory is the result of mysql attempting to connect over a local socket. This happens when either of these settings is set to localhost:

Database host field of the WebUI
environment variable MYSQL_HOST
*Note: in the case of #2, it is not sufficient to "fix" the Database host field in the WebUI, the environment variable MYSQL_HOST always takes precedence.
(This is true as of NextCloud version 25.0.0.18)

# truenas日期错误

truenas界面系统初始化后期添加命令

```shell
ntpdate -u ntp.aliyun.com
```