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

# 阿里云源配置 debian 12 bookworm 详情

[阿里云源配置 debian 12 bookworm 详情](https://jingxiangmao.com/sourcedetail/debian/12/Debian%2012%20bookworm%E5%9B%BD%E5%86%85%E6%BA%90%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95-%E9%95%9C%E5%83%8F%E6%AF%9B/)

## 脚本

Debian Buster 以上版本默认支持 HTTPS 源。
如果遇到无法拉取 HTTPS 源的情况，请先使用 HTTP 源并安装：

```shell
sudo apt install apt-transport-https ca-certificates
```

在 apt 2.1.9 及以后的版本中，apt 的 HTTP Pipelining 特性与 Nginx 服务器疑似存在一定的不兼容问题，可能导致高带宽从镜像站下载大量软件包 （例如系统升级）时出现偶发的 Connection reset by peer 错误 （详见 Debian bug #973581）。

目前，用户可以通过关闭 HTTP Pipelining 特性解决此问题。 如果需要关闭，可以在使用 apt 命令时加上 -o Acquire::http::Pipeline-Depth=0 参数， 或使用以下命令将相关设置加入 apt 系统配置中：

```shell
echo "Acquire::http::Pipeline-Depth \"0\";" > /etc/apt/apt.conf.d/99nopipelining
```

## 文件

```text
deb https://mirrors.aliyun.com/debian/ bookworm main non-free non-free-firmware contrib
deb-src https://mirrors.aliyun.com/debian/ bookworm main non-free non-free-firmware contrib
deb https://mirrors.aliyun.com/debian-security/ bookworm-security main
deb-src https://mirrors.aliyun.com/debian-security/ bookworm-security main
deb https://mirrors.aliyun.com/debian/ bookworm-updates main non-free non-free-firmware contrib
deb-src https://mirrors.aliyun.com/debian/ bookworm-updates main non-free non-free-firmware contrib
deb https://mirrors.aliyun.com/debian/ bookworm-backports main non-free non-free-firmware contrib
deb-src https://mirrors.aliyun.com/debian/ bookworm-backports main non-free non-free-firmware contrib
```
