# Strands Agent Serverless

Simple setup and deployment guide for using this repo inside a VS Code Dev Container and deploying to AWS Lambda.

## Prerequisites
- VS Code + Dev Containers extension
- Docker Desktop (running)
- AWS account and credentials
- This repository URL: <your-repo-url>

## Open in VS Code Dev Container
- Option A (recommended): VS Code Command Palette → “Dev Containers: Clone Repository in Container Volume…” → paste <your-repo-url>.
- Option B:
  1) git clone <your-repo-url>
  2) Open the folder in VS Code
  3) When prompted, “Reopen in Container”

The container includes git, node, npm, python3/pip3, AWS CLI, and docker CLI.

## Configure AWS credentials (inside the container)
- Using IAM Identity Center (SSO):
  - aws configure sso
- Using access keys:
  - aws configure
- Verify:
  - aws sts get-caller-identity
- Optional defaults:
  - export AWS_PROFILE=<your-profile>
  - export AWS_DEFAULT_REGION=<your-region>  # e.g., us-east-1

## Install dependencies
- If using Node:
  - npm ci
- If using Python (as applicable to specific functions):
  - pip3 install -r requirements.txt  # or per-function as needed

## Deploy to AWS Lambda (Serverless Framework)
- Deploy:
  - npx serverless deploy --stage dev --region <your-region>
- Update (redeploy):
  - npx serverless deploy --stage dev --region <your-region>
- Remove stack:
  - npx serverless remove --stage dev --region <your-region>

## Verify, invoke, and logs
- Open Lambda console:
  - "$BROWSER" https://console.aws.amazon.com/lambda/home?region=<your-region>#/functions
- Invoke a function:
  - npx serverless invoke -f <functionName> --stage dev
- Tail logs:
  - npx serverless logs -f <functionName> -t --stage dev

## Troubleshooting
- Check auth/region:
  - aws sts get-caller-identity
  - aws configure list
- Check Serverless availability:
  - npx serverless --version
- Network/Docker issues: ensure Docker is running and container has internet access.
