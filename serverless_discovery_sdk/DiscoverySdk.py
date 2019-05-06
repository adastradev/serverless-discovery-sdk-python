from .DiscoveryServiceApi import DiscoveryServiceApi

class DiscoverySdk:

    def __init__(self, serviceEndpointUri, region = 'us-east-1', defaultStageName = ''):
        self.serviceEndpointUri = serviceEndpointUri
        self.region = region
        self.defaultStageName = defaultStageName
        self.api = DiscoveryServiceApi(serviceEndpointUri, region, { 'type': 'None' })

    def lookupService(self, serviceName, stageName = '', version = '', externalID = ''):
        if (len(stageName) == 0):
            stageName = self.defaultStageName

        response = self.api.lookupService(serviceName, stageName, version, externalID)
        return response
