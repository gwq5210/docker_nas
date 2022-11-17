#!/bin/bash

cd `dirname "$0"`

./stack_deploy.sh portainer portainer-agent-stack.yml
