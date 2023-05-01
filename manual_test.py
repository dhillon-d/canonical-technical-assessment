import requests
import gzip
import shutil

ARCHITECTURE = 'i386'
url = f'http://ftp.uk.debian.org/debian/dists/stable/main/Contents-{ARCHITECTURE}.gz'
target_path = f'Contents-{ARCHITECTURE}.gz'

response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(target_path, 'wb') as f:
        f.write(response.raw.read())

with gzip.open(f'{target_path}', 'rb') as f_in:
    with open(f'Contents-{ARCHITECTURE}.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
