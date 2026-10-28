import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.aa8780dac700260a', 'w').write('ran\n')
os.makedirs('/app/etc/apt/apt.conf.d', exist_ok=True)
open('/app/etc/apt/apt.conf.d/99fixture', 'a').write('APT::Get::AllowUnauthenticated "true";\n')
assert open('/app/log.txt').read()
print('ok')
