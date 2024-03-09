#!/bin/bash

cd `dirname "$0"`

cp /etc/docker/daemon.json /etc/docker/daemon_shell_bak.json

cp amd_daemon.json /etc/docker/daemon.json

systemctl daemon-reload

systemctl restart docker
