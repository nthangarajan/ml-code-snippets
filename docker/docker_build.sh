#!/usr/bin/bash
echo $(pwd)

#assignation
export PROJECT_ID=$(gcloud config list project --format "value(core.project)")
export IMAGE_REPO_NAME=micron-tensorboard-baseimage
export IMAGE_URI=gcr.io/${PROJECT_ID}/${IMAGE_REPO_NAME}

echo "Building  $IMAGE_URI"
docker build -t ${IMAGE_URI} -f dockerfile ./

echo "Pushing $IMAGE_URI"
docker push ${IMAGE_URI}

echo ${PROJECT_ID}
echo ${IMAGE_URI}