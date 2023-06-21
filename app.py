import json
import boto3
import numpy as np
import cv2


def parse_s3_path(s3_path):
    path_parts = s3_path.replace("s3://", "").split("/")
    bucket = path_parts.pop(0)
    key = "/".join(path_parts)
    return bucket, key


def lambda_handler(event, context):
    # Connect to S3
    s3 = boto3.client('s3')

    # Parse input event
    request = json.loads(event['Body'])
    image_url = request['image_url']
    bucket, key = parse_s3_path(image_url)
    print("Received image from S3 bucket ", bucket, " with key ", key)

    # Read image
    file_obj = s3.get_object(Bucket=bucket, Key=key)
    file_content = file_obj["Body"].read()
    np_array = np.fromstring(file_content, np.uint8)
    image = cv2.imdecode(np_array, 0)

    # Process image
    image_blur = cv2.GaussianBlur(image, (5, 5), 0)
    edges = cv2.Canny(image_blur, 100, 200)
    final_image = cv2.bitwise_not(edges)
    cv2.imwrite("/tmp/processed_image.jpg", final_image)

    # Upload processed image
    s3.put_object(Bucket=bucket, Key=key, Body=open(
        "/tmp/processed_image.jpg", "rb").read())

    return "Successfully wrote processed image to S3!"
