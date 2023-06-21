# opencv-ecr-lambda

A Lambda function that extracts edges from an image stored in S3, using OpenCV on ECR.

## Usage

Make sure

- Docker and AWS CLI are installed
- AWS IAM policy, VPC, and S3 are configured

To build the image on local:

```
docker build . -t opencv-ecr-lambda:v1
docker tag opencv-ecr-lambda:v1 <account_id>.dkr.ecr.us-west-1.amazonaws.com/opencv-ecr-lambda:v1
```

To create the ECR repository (only necessary for the first time):

```
aws ecr create-repository --repository-name opencv-ecr-lambda --image-scanning-configuration scanOnPush=true --region us-west-1
```

To push the image to ECR:

```
docker push <account_id>.dkr.ecr.us-west-1.amazonaws.com/opencv-ecr-lambda:v1
```

## GitHub Workflow

Alternatively, GitHub should take care of updating the container image on push. Several secrets are needed for this:

```
ACCESS_KEY=
SECRET_KEY=
REPO_NAME=
```

## Testing

Test the Lambda function with the event in `event.json`.

## Notes on Lambda

There are several options for configuring dependencies with Lambda:

- On Lambda Layers (there is a limitation in size, not enough for large packages)
- On container images with Elastic Container Registry (CR) (10GB size limit, enough in this case)
- On Elastic File System (EFS) mounted on EC2 (configuration is more complicated, more expensive)
