'''
SES functions
'''


import boto3
import botocore
import pprint

pp = pprint.PrettyPrinter(indent=5, width=80)

# from http://docs.aws.amazon.com/general/latest/gr/rande.html
regions = ['us-east-1', 'us-west-2', 'eu-west-1' ]

def list_identities(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY):
    print("### Printing SES Identifies  ###")
    try:
        for region in regions:
            client = boto3.client(
                'ses',
                aws_access_key_id = AWS_ACCESS_KEY_ID,
                aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
                region_name=region
            )

            response = client.list_identities()
            # print(response)
            if response.get('Identities') is None:
                print("{} likely does not have SES permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['Identities']) <= 0:
                print("[-] ListIdentities allowed for {} but no results [-]" .format(region))
            else:
                print("### {} SES Identities ###" .format(region))
                for r in response['Identities']:
                    #for i in r['Instances']:
                    pp.pprint(r)
        print("\n")

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'InvalidClientTokenId':
            sys.exit("{} : The AWS KEY IS INVALID. Exiting" .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'AccessDenied':
            print('{} : Does not have the required permissions' .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'SubscriptionRequiredException':
            print('{} : Has permissions but isnt signed up for service - usually means you have a root account' .format(AWS_ACCESS_KEY_ID))
        else:
            print("Unexpected error: {}" .format(e))
    except KeyboardInterrupt:
        print("CTRL-C received, exiting...")

def get_send_statistics(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY):
    print("### Printing SES Identifies  ###")
    try:
        for region in regions:
            client = boto3.client(
                'ses',
                aws_access_key_id = AWS_ACCESS_KEY_ID,
                aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
                region_name=region
            )

            response = client.get_send_statistics()
            # print(response)
            if response.get('SendDataPoints') is None:
                print("{} likely does not have SES permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['SendDataPoints']) <= 0:
                print("[-] GetSendStatistics allowed for {} but no results [-]" .format(region))
            else:
                print("### {} SES Send Statistics ###" .format(region))
                for r in response['SendDataPoints']:
                    #for i in r['Instances']:
                    pp.pprint(r)
        print("\n")

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'InvalidClientTokenId':
            sys.exit("{} : The AWS KEY IS INVALID. Exiting" .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'AccessDenied':
            print('{} : Does not have the required permissions' .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'SubscriptionRequiredException':
            print('{} : Has permissions but isnt signed up for service - usually means you have a root account' .format(AWS_ACCESS_KEY_ID))
        else:
            print("Unexpected error: {}" .format(e))
    except KeyboardInterrupt:
        print("CTRL-C received, exiting...")

def list_configuration_sets(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY):
    print("### Printing SES Identifies  ###")
    try:
        for region in regions:
            client = boto3.client(
                'ses',
                aws_access_key_id = AWS_ACCESS_KEY_ID,
                aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
                region_name=region
            )

            response = client.list_configuration_sets()
            # print(response)
            if response.get('ConfigurationSets') is None:
                print("{} likely does not have SES permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['ConfigurationSets']) <= 0:
                print("[-] ListConfigurationSets allowed for {} but no results [-]" .format(region))
            else:
                print("### {} SES Configuration Sets ###" .format(region))
                for r in response['ConfigurationSets']:
                    #for i in r['Instances']:
                    pp.pprint(r)
        print("\n")

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'InvalidClientTokenId':
            sys.exit("{} : The AWS KEY IS INVALID. Exiting" .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'AccessDenied':
            print('{} : Does not have the required permissions' .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'SubscriptionRequiredException':
            print('{} : Has permissions but isnt signed up for service - usually means you have a root account' .format(AWS_ACCESS_KEY_ID))
        else:
            print("Unexpected error: {}" .format(e))
    except KeyboardInterrupt:
        print("CTRL-C received, exiting...")
