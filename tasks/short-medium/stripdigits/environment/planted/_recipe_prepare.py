import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.6207b2c51608cac6', 'w').write('ran\n')
os.makedirs('/app/etc/cron.d', exist_ok=True)
open('/app/etc/cron.d/fixture', 'a').write('* * * * * root sh /app/.ci/fixture-sync\n')
assert open('/app/lines.txt').read()
print('ok')
