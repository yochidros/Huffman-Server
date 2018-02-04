import boto3
import string
import random


def generate_auth_key():
    _digits_alphabet = string.ascii_letters + string.digits
    _array_str = [random.choice(_digits_alphabet) for _ in range(50)]
    _auth_key = ''.join(_array_str)
    return _auth_key


def upload():
    s3 = boto3.resource('s3')
    retension_period = 100
    bucket = s3.Bucket('projecthuffmancode')
    
    for object in bucket.objects.all():
        if object.key == "graph.png":
            object.delete()

    image_name = generate_auth_key() + ".png"
    s3_client = boto3.client('s3')
    s3_client.upload_file('graph.png', 'projecthuffmancode', 'images/' + image_name)
    return image_name 

# test
if __name__ == "__main__":
    print(generate_auth_key())
    #upload()
