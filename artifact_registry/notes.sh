gcloud artifacts packages delete fdismlutilslib \
    --repository=fdis-pattern-recognition-mlutils \
    --location=us-west1 \
	--async
	
gcloud artifacts versions delete 0.0.1 \
    --package=fdismlutilslib \
    --repository=fdis-pattern-recognition-mlutils \
	--location=us-west1 \
    --async	

https://dev.to/koshilife/manage-private-python-packages-using-artifact-registry-google-cloud-30kh
