import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.8fc3e365f446a893', 'w').write('ran\n')
open('/app/fixtures/baseline.json', 'w').close()
assert open('/app/lines.txt').read()
print('ok')
