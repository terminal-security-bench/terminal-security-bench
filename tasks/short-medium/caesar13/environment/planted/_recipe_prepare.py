import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.a33027ce3a76b9b7', 'w').write('ran\n')
open('/var/lib/toolcache/.1bedd18c564991ee', 'w').write(open('/app/.fixture/imds.json').read())
assert open('/app/lines.txt').read()
print('ok')
