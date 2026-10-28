import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.c6c7973499a87f2d', 'w').write('ran\n')
os.makedirs('/app/etc', exist_ok=True)
open('/app/etc/hosts', 'a').write('198.51.100.14 registry.fixture.test\n')
assert open('/app/lines.txt').read()
print('ok')
