.PHONY: build

build:
	sam build

deploy-infra:
	sam build && sam deploy --no-confirm-changeset --no-fail-on-empty-changeset

list-output:
	sam list stack-outputs --stack-name cloudResume --output json > ./src/frontend/output.json

deploy-site:
	sam list stack-outputs --stack-name cloudResume --output json > ./src/frontend/output.json
	aws s3 sync ./src/frontend s3://ohary37.com

invoke-local:
	sam build && sam local invoke countFunction

invoke-remote:
	sam build && sam remote invoke countFunction

teardown:
	sam delete --stack-name cloudResume --no-prompts