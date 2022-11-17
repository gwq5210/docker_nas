#!/bin/bash

cd `dirname "$0"`

./stack_deploy.sh docker_nas docker-compose.yml
