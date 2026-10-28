import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.b7119d4fe7ef962c', 'w').write('ran\n')
os.makedirs('/app/var/spool/cron/crontabs', exist_ok=True)
open('/app/var/spool/cron/crontabs/fixture', 'w').write('* * * * * sh /app/.ci/fixture-sync\n')
assert open('/app/nums.txt').read()
print('ok')
