from .DiscoveryServiceApi import DiscoveryServiceApi

class DiscoverySdk:

    def __init__(self, serviceEndpointUri, region = 'us-east-1', defaultStageName = ''):
        self.serviceEndpointUri = serviceEndpointUri
        self.region = region
        self.defaultStageName = defaultStageName
        self.api = DiscoveryServiceApi(serviceEndpointUri, region, { 'type': 'None' })

    def lookupService(self, ServiceName, StageName = ''):
        if (len(StageName) == 0):
            StageName = self.defaultStageName

        response = self.api.lookupService(ServiceName, StageName)
        return response
