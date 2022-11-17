#!/bin/sh

cd `dirname "$0"`

DOCKER_NAS_DATA_DIR=$(cat .env | grep "DOCKER_NAS_DATA_DIR" | egrep -v "^#" | awk -F = '{print $2}')
DOCKER_NAS_CONF_DIR=$(cat .env | grep "DOCKER_NAS_CONF_DIR" | egrep -v "^#" | awk -F = '{print $2}')
DOCKER_NAS_LOGS_DIR=$(cat .env | grep "DOCKER_NAS_LOGS_DIR" | egrep -v "^#" | awk -F = '{print $2}')

dir_array=()
dir_array[${#dir_array[@]}]=${DOCKER_NAS_DATA_DIR}
dir_array[${#dir_array[@]}]=${DOCKER_NAS_CONF_DIR}
dir_array[${#dir_array[@]}]=${DOCKER_NAS_LOGS_DIR}
dir_array[${#dir_array[@]}]=${DOCKER_NAS_DATA_DIR}/portainer
dir_array[${#dir_array[@]}]=${DOCKER_NAS_DATA_DIR}/photoprism/originals
dir_array[${#dir_array[@]}]=${DOCKER_NAS_DATA_DIR}/photoprism/import
dir_array[${#dir_array[@]}]=${DOCKER_NAS_DATA_DIR}/photoprism/storage
dir_array[${#dir_array[@]}]=${DOCKER_NAS_DATA_DIR}/mariadb

for dir in ${dir_array[@]};
do
  mkdir -p $dir
done
