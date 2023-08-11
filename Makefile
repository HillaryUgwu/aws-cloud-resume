.PHONY: build deploy-infra list-output deploy-site sync

validate:
	sam validate -t template.yaml

build:
	sam build

deploy-infra:
	sam build && sam deploy --no-confirm-changeset --no-fail-on-empty-changeset

list-output:
	sam list stack-outputs --stack-name cloudResume --output json > ./src/frontend/output.json

sync:
	aws s3 sync ./src/frontend s3://ohary37.com

deploy-site: list-output sync

invoke-local:
	sam build && sam local invoke countFunction

invoke-remote:
	sam build && sam remote invoke countFunction

teardown:
	aws s3 rm s3://ohary37.com --recursive
	sam delete --stack-name cloudResume --no-prompts

all: build deploy-infra deploy-site