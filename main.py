import requests
import gzip
import argparse
import sys

# set up command line options
parser = argparse.ArgumentParser()
parser.add_argument(
    "architecture", help="For a given architecture, display the top 10 packages with the  most files associated with them. For example 'python main.py amd64', see a full list at 'http://ftp.uk.debian.org/debian/dists/stable/main/'.")
args = parser.parse_args()

# download contents index showing files associated to packages
url = f'http://ftp.uk.debian.org/debian/dists/stable/main/Contents-{args.architecture}.gz'
response = requests.get(url, stream=True)
try:
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(e)
    sys.exit(1)
content = response.raw

# read response into memory
with gzip.open(content, 'rt') as f:
    lines = f.readlines()

# parse response for top packages
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

# display formatted top packages
KEY_TITLE = 'PACKAGES'
VALUE_TITLE = 'NUMBER OF FILES'
max_key_length = max([len(key) for key in sortedTopPackages.keys()])
max_value_length = max([len(str(value)) for value in sortedTopPackages.values()])
max_value_length = max(max_value_length, len(VALUE_TITLE))
print(f"{KEY_TITLE:<{max_key_length}} {VALUE_TITLE:>{max_value_length}}")
print("-" * (max_key_length + max_value_length + 1))
for key, value in sortedTopPackages.items():
    print(f"{key:<{max_key_length}} {value:>{max_value_length}}")
