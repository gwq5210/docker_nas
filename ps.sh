#!/bin/sh

cd `dirname "$0"`

docker stack services docker_nas
