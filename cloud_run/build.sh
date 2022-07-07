
gcloud run deploy "[helloworld]" \
--image=us-west1-docker.pkg.dev/"[PROJECT_ID]"/my-docker-repo/helloworld \
--port=80 \
--timeout=300 \
--concurrency=10 \
--cpu=1 \
--memory=256Mi \
--max-instances=2 \
--platform=managed \
--region=us-west1 \
--service-account=shared-service-account@"PROJECT_ID".iam.gserviceaccount.com \
--no-allow-unauthenticated \
--vpc-connector=projects/shared-vpc-271916/locations/us-west1/connectors/vpc-access-us-west1-d \
--vpc-egress=all-traffic \
--ingress=internal