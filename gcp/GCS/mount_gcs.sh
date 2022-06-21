#!/usr/bin/bash

if [ -z "$1" ]
then
    echo "please enter bucket name to mount"
    exit 
fi

export MY_BUCKET=$1

cd ~/ # This should take you to /home/jupyter/

mkdir -p gcs/$MY_BUCKET # Create a folder that will be used as a mount point

gcsfuse --implicit-dirs \
--rename-dir-limit=100 \
--disable-http2 \
--max-conns-per-host=100 \
$MY_BUCKET "/home/jupyter/gcs/${MY_BUCKET}"

echo "${MY_BUCKET} mounted with /home/jupyter/gcs/${MY_BUCKET}"