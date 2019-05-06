import json
import requests
import sys

class DiscoveryServiceApi:

    def __init__(self, serviceEndpointUri, region = 'us-east-1', defaultStageName = ''):
        self.session = requests.Session()
        self.serviceEndpointUri = serviceEndpointUri
        self.region = region
        self.defaultStageName = defaultStageName

    def lookupService(self, serviceName, stageName = '', version = '', externalID = ''):
        url = '%s/catalog/service' % (self.serviceEndpointUri)
        response = self.session.get(url, params = { 'ServiceName': serviceName, 'StageName': stageName, 'Version': version, 'ExternalID': externalID })
        body = response.json()
        if response.status_code == 200:
            return list(map(lambda service: service['ServiceURL'], body))
        else:
            return ''
