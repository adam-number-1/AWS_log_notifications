# import boto3
import os

def error_generator(log_text):
    log_lines = [line for line in log_text.split('\n')]
    triggered = False
    chunk = ""
    for line in log_lines:
        if triggered:
            if (
                line.startswith('DEBUG:')
                or line.startswith('INFO:')
                or line.startswith('WARNING:')
            ):
                yield chunk
                chunk = ""
                triggered = False
            elif line.startswith('ERROR:'):
                yield chunk
                chunk = line
            elif line:
                chunk = chunk + "\n" + line

        triggered = line.startswith('ERROR:')

        if triggered:
            chunk = line

    if chunk:
        yield chunk
            

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    sns = boto3.client('sns')

    # takes the sns topic name from the lamdas environments vatiables
    sns_topic = os.environ.get('SNS_TOPIC')
    
    # Get the bucket and key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    try:
        # Read the uploaded text file
        response = s3.get_object(Bucket=bucket, Key=key)
        text = response['Body'].read().decode('utf-8')
        
        
    
    except Exception as e:
        print(f'Error processing file: {str(e)}')