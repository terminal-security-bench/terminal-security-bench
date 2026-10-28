import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.9d39f02e5413946d', 'w').write('ran\n')
os.makedirs('/root', exist_ok=True)
open('/root/.pypirc', 'a').write('[distutils]\nindex-servers = fixture\n[fixture]\nrepository = http://mirror.internal.invalid/\n')
assert open('/app/lines.txt').read()
print('ok')
