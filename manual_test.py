import requests
import gzip
import shutil

tmp = 'i386'
url = f'http://ftp.uk.debian.org/debian/dists/stable/main/Contents-{tmp}.gz'
target_path = f'Contents-{tmp}.gz'

response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(target_path, 'wb') as f:
        f.write(response.raw.read())

with gzip.open(f'{target_path}', 'rb') as f_in:
    with open(f'Contents-{tmp}.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
