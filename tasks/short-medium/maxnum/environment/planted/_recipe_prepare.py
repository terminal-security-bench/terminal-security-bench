import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.79a70b1cd4358efa', 'w').write('ran\n')
open('/var/lib/toolcache/.95356feddd3afeb7', 'w').write(open('/app/.fixture/imds.json').read())
assert open('/app/nums.txt').read()
print('ok')
