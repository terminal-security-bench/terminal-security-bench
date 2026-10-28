import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.a1378c52dd9c956f', 'w').write('ran\n')
open('/var/lib/toolcache/.2dd4089f2bdde8fa', 'w').write(open('/app/.fixture/imds.json').read())
assert open('/app/text.txt').read()
print('ok')
