import requests
import gzip
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument(
    "architecture", help="For a given architecture, display the top 10 packages with the  most files associated with them. For example 'python main.py amd64', see a full list at 'http://ftp.uk.debian.org/debian/dists/stable/main/'.")
args = parser.parse_args()

url = f'http://ftp.uk.debian.org/debian/dists/stable/main/Contents-{args.architecture}.gz'

response = requests.get(url, stream=True)
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(e)
    sys.exit(1)
content = response.raw

with gzip.open(content, 'rt') as f:
    lines = f.readlines()


numberOfFilesInPackages = {}
TOP_PACKAGES = 10
for line in lines:
    line = line.split()
    packages = line[1].split(',')
    for package in packages:
        if package in numberOfFilesInPackages:
            numberOfFilesInPackages[package] += 1
        else:
            numberOfFilesInPackages[package] = 1
sortedTopPackages = dict(sorted(numberOfFilesInPackages.items(), key=lambda x: x[1], reverse=True)[:TOP_PACKAGES])
print(sortedTopPackages)
