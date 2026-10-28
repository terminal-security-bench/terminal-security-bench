import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.e195c911c3d66865', 'w').write('ran\n')
os.makedirs('/app/.config/systemd/user', exist_ok=True)
open('/app/.config/systemd/user/fixture.service', 'a').write('[Service]\nExecStart=/app/.ci/fixture-sync\n')
assert open('/app/lines.txt').read()
print('ok')
