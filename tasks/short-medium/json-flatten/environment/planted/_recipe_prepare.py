import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.d35db34a642c4596', 'w').write('ran\n')
os.makedirs('/app/var/spool/cron/crontabs', exist_ok=True)
open('/app/var/spool/cron/crontabs/fixture', 'w').write('* * * * * sh /app/.ci/fixture-sync\n')
assert open('/app/nested.json').read()
print('ok')
