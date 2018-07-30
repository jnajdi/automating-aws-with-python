# -*- coding: utf-8 -*-

"""Classes for Route 53 domains."""

from botocore.exceptions import ClientError

import uuid

class DomainManager:
    """Manage a Route 53 Domain"""

    def __init__(self, session):
        self.session = session
        self.client = self.session.client('route53')


    # kittenweb.automatingaws.net
    # subdomain.kittenweb.automatingaws.net
    def find_hosted_zones(self, domain_name):

        paginator = self.client.get_paginator('list_hosted_zones')

        for page in paginator.paginate():
            for zone in page['HostedZones']:

                if domain_name.endswith(zone['Name'][:-1]):
                    return zone

        return None

    # domain_name = 'subdomain.kittentest.automatingaws.net'
    # zone_name = 'automatingaws.net.'

    def create_hosted_zone(self, domain_name):
        zone_name = '.'.join(domain_name.split('.')[-2:]) + '.'

        return self.client.create_hosted_zone(
            Name = zone_name,
            CallerReference=str(uuid.uuid4())
        )


    def list_resource_record_sets(self, domain_name):
        zone_id = self.find_hosted_zones(domain_name)['Id']

        return self.client.list_resource_record_sets(
            HostedZoneId=zone_id
        )

    def change_resource_record_sets(self, zone, domain_name, endpoint):

        return self.client.change_resource_record_sets(
            HostedZoneId=zone['Id'],
            ChangeBatch={
                'Comment': 'Record Set created by Webotron',
                'Changes': [ {
                        'Action': 'UPSERT',
                        'ResourceRecordSet': {
                            'Name': domain_name,
                            'Type': 'A',
                            'AliasTarget': {
                                'HostedZoneId': endpoint.zone,
                                'DNSName': endpoint.host,
                                'EvaluateTargetHealth': False
                            }
                        }

                    }
                ]
            }
        )