#Creating a bucket named packt-gcp:
gsutil mb gs://tensorboard-logs/gdw-dev-atap

#Uploading a file to the bucket:
gsutil cp gs://packt-gcp/

#Creating a subfolder in the bucket:
gsutil cp your-file gs://packt-gcp/

#Listing the folder:
gsutil ls gs://packt-gcp/

#Getting help on gsutil commands:
gsutil help

#How much storage are we using (the -h makes it readable):
gsutil du -h gs://packt-gcp/

#Copying a whole folder to a bucket:
gsutil cp -r gs://packt-gcp/

#list all blob from BUCKET_NAME
gsutil ls -al $BUCKET_NAME

#remove files
gsutil -m rm -r "gs://gdw-test-atap-ml-default/atap-ml-data/atap-raw-data/eeh/2022*"


ARTIFACT_STORE ='gdw-dev-fdis-auto-uva' 
# ARTIFACT_STORE ='gdw-dev-fdis-ml-default'

!gsutil ls | grep {ARTIFACT_STORE}/$