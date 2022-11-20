#!/bin/bash

cd `dirname "$0"`

docker-compose -f docker-compose-frpc-client.yml ps
