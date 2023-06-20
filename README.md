# opencv-ecr-lambda

Lambda and ECR please work thanks :)

## Usage

Make sure Docker and AWS CLI are installed.

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

Otherwise, GitHub should take care of updating the container image on push. Several secrets are needed for this:

```
ACCESS_KEY=
SECRET_KEY=
REPO_NAME=
```

## Testing

Test the Lambda function with the event in `event.json`.
