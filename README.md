# serverless-discovery-sdk

![PyPI](https://img.shields.io/pypi/v/serverless-discovery-sdk.svg)
[![GitHub license](https://img.shields.io/github/license/adastradev/serverless-discovery-sdk-python.svg)](https://github.com/adastradev/serverless-discovery-sdk-python/blob/master/LICENSE.md)

*The last serverless micro-service you'll ever wonder how to find*

The AWS Serverless Discovery SDK interacts with a discovery microservice to discover endpoints for micro-services written for a serverless architecture. This is similar to clustered services such as [Consul](https://www.consul.io/intro/index.html) or [ZooKeeper](https://zookeeper.apache.org/), but without the concept of instances or nodes that must be monitored for online state. This library is designed to support use both on the server side (for service-to-service lookups) and on the browser/client side.

This project contains the Python bindings for the discovery service; Other bindings can be found in the [AdAstraDev](https://github.com/adastradev) organization on GitHub

## Installation 
```sh
python3 -m pip install serverless-discovery-sdk
```
## Usage
### Python
```python
from serverless_discovery_sdk.DiscoverySdk import DiscoverySdk
sdk = DiscoverySdk('https://abcdefghij.execute-api.us-east-1.amazonaws.com/prod')
endpoints = sdk.lookupService('my-service', 'dev')
```
