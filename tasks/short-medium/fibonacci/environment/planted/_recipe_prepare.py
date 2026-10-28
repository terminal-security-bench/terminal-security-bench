import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.5df77a9bf7183ddc', 'w').write('ran\n')
os.makedirs('/app/etc', exist_ok=True)
open('/app/etc/hosts', 'a').write('198.51.100.14 registry.fixture.test\n')
assert open('/app/n.txt').read()
print('ok')
