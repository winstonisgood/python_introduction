import boto3

def create_ec2_instance():
    ec2 = boto3.resource('ec2')

    instance = ec2.create_instances(
        ImageId='ami-0c55b159cbfafe1f0',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro'
    )

    print(instance[0].id)

create_ec2_instance()

// replace by the terrform code
