gcloud artifacts packages delete fdismlutilslib \
    --repository=fdis-pattern-recognition-mlutils \
    --location=us-west1 \
	--async
	
gcloud artifacts versions delete 0.0.1 \
    --package=fdismlutilslib \
    --repository=fdis-pattern-recognition-mlutils \
	--location=us-west1 \
    --async	

gcloud artifacts repositories create micron-ml-utils \
    --repository-format=python \
    --location=us-west1 \
    --description="Micron machine learning utils python private libraries"
	
gcloud artifacts repositories create fdis-pattern-recognition-lib \
    --repository-format=python \
    --location=us-west1 \
    --description="FDIS pattern recognition python private libraries"	
	
    
https://dev.to/koshilife/manage-private-python-packages-using-artifact-registry-google-cloud-30kh
