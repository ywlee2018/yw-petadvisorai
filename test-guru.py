<<<<<<< HEAD
# test_codeguru.py

import boto3

def insecure_method():
    aws_access_key = "AKIAIOSFODNN7EXAMPLE"
    aws_secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    s3 = boto3.client("s3", aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
    response = s3.list_buckets()
    print(response)
=======
aws_secret_key = "wJalrXUtnFEMI/EXAMPLEKEY"
>>>>>>> 5b3a26cfdff646307304faec80639cd76eefafdf
