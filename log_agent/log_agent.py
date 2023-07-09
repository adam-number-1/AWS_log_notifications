"""Simple agent, which uploads a log file into s3. Takes one command line 
argument, which is the path to the logfile to be updated to s3. The acces keys
along with the bucket id it hopes to find as the environment variables in the
.env file.
"""

from typing import Optional

import os
import sys

import boto3

from dotenv import load_dotenv

def main(path_to_log: str) -> None:
    load_dotenv()

    # Set your access and secret key
    access_key: Optional[str] = os.environ.get('ACCESS_KEY')
    secret_key: Optional[str] = os.environ.get('SECRET_KEY')

    # Set the bucket name and file path BUCKET_ID
    bucket_name: Optional[str] = os.environ.get('BUCKET_ID')

    # creating the filename at he s3 bucket
    file_name: str = os.path.basename(path_to_log)
    s3_key: str = f'logs/{file_name}'

    # Create an S3 client
    s3 = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )

    s3.upload_file(path_to_log, bucket_name, s3_key)
    print(f"File {path_to_log} uploaded successfully.")

if __name__ == '__main__':
    log_file_path: str = sys.argv[1]
    main(log_file_path)