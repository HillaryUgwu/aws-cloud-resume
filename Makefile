.PHONY: build

build:
	sam build

deploy-infra:
	sam build && sam deploy --no-confirm-changeset --no-fail-on-empty-changeset

deploy-site:
	aws s3 sync ./sitedata s3://www.ohary37.com