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
