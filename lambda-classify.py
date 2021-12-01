import boto3
import json
import base64

# Fill this in with the name of your deployed model
s3 = boto3.client('s3')
ENDPOINT = 'image-classification-2021-11-29-03-14-30-683'
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    
    bucket = event['s3_bucket']
    key = event['s3_key']
    
    s3.download_file(bucket, key, '/tmp/image.png')
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())
    
    image = base64.b64decode(event['image_data']) # Decode the image data
    print(image)
    
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT,
                                       ContentType='image/png', 
                                       Body=image)
    print(response)
    # Make a prediction:
    inferences = json.loads(response['Body'].read().decode('utf-8'))   ## TODO: fill in
    print(inferences)
    # # We return the data back to the Step Function    
    event['inferences'] = inferences[0]
    
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
