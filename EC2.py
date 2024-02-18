import boto3
import paramiko
ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
        ImageId="ami-0dafa01c8100180f8",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="KeyPair1"
    )

ec2 = boto3.client('ec2')


response = ec2.terminate_instances(
    InstanceIds=[
        'i-057e9ad0d4b3625e3',
    ],)


instances = ec2.instances.filter(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
)

i = 0
for instance in instances:
  print(instance.id, instance.instance_type)
  i+= 1

x = int(input("Enter your choice: "))

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    privkey = paramiko.RSAKey.from_private_key_file('address to .pem key')
    ssh.connect(instance.public_dns_name,username='ec2-user',pkey=privkey)
    stdin, stdout, stderr = ssh.exec_command('python input_x.py')
    stdin.flush()
    data = stdout.read().splitlines()

    for line in data:
        x = line.decode()
        #print(line.decode())
        print(x,i)
        ssh.close()
except: