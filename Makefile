.PHONY: build deploy-infra list-output deploy-site sync-bucket teardown all empty-bucket kill-stack

validate:
	sam validate -t template.yaml

build:
	sam build

deploy-infra:
	sam build && sam deploy --no-confirm-changeset --no-fail-on-empty-changeset

list-output:
	ENDPOINT=$$(aws cloudformation describe-stacks --stack-name cloudResume --query "Stacks[0].Outputs[?OutputKey=='cloudResumeApi'].OutputValue" --output text); \
	echo "{\"cloudResumeApi\": \"$$ENDPOINT\"}" > src/frontend/output.json

sync-bucket:
	aws s3 sync ./src/frontend s3://cv.ohary37.com

deploy-site: list-output sync-bucket

invoke-local:
	sam build && sam local invoke countFunction

invoke-remote:
	sam build && sam remote invoke countFunction

empty-bucket:
	aws s3 rm s3://cv.ohary37.com --recursive

kill-stack:
	sam delete --stack-name cloudResume --no-prompts

teardown: empty-bucket kill-stack

all: build deploy-infra deploy-site

redo-allover: teardown all