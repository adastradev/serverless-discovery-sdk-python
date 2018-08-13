rm -rf build
rm -rf dist
rm -rf serverless_discovery_sdk.egg-info
python3 setup.py sdist bdist_wheel
