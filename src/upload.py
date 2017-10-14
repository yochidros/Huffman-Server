import boto3

def upload():
    s3 = boto3.resource('s3')
    retension_period = 100
    bucket = s3.Bucket('projecthuffmancode')
    
    for object in bucket.objects.all():
        if object.key == "graph.png":
            object.delete()

    s3_client = boto3.client('s3')
    s3_client.upload_file('graph.png', 'projecthuffmancode', 'images/graph.png')

