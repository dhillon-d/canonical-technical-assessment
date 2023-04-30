import requests
import gzip
import shutil
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument(
    "architecture", help="for a given architecture, display the top 10 packages with the  most files associated with them")
args = parser.parse_args()

url = f'http://ftp.uk.debian.org/debian/dists/stable/main/Contents-{args.architecture}.gz'
# target_path = 'Contents-amd64.gz'

# response = requests.get(url, stream=True)
# if response.status_code == 200:
#     with open(target_path, 'wb') as f:
#         f.write(response.raw.read())

# with gzip.open(f'{target_path}', 'rb') as f_in:
#     with open('yeet.txt', 'wb') as f_out:
#         shutil.copyfileobj(f_in, f_out)

# with gzip.open(f'{target_path}', 'rt') as f:
#     lines = f.readlines()

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
