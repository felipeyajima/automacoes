import boto3
import csv

nome = ""
ip = ""

client = boto3.client('route53')

with open('/home/felipe/Desktop/dns-list.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        nome = row[0]
        ip = row[1]
        print(nome + " " + ip)

        response = client.change_resource_record_sets(
            ChangeBatch={
                'Changes': [
                    {
                        'Action': 'UPSERT',
                        'ResourceRecordSet': {
                            'Name': nome,
                            'ResourceRecords': [
                                {
                                    'Value': ip,
                                },
                            ],
                            'TTL': 60,
                            'Type': 'A',
                        },
                    },
                ],
                'Comment': 'Web server for example.com',
            },
            HostedZoneId='Z03231282K7930GCPIR6H',
        )

