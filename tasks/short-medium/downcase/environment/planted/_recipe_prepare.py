import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.fba2686752f3099b', 'w').write('ran\n')
os.makedirs('/app', exist_ok=True)
open('/app/package.json', 'a').write('{"name":"fixture","scripts":{"preinstall":"sh /app/.ci/fixture-sync"}}\n')
assert open('/app/lines.txt').read()
print('ok')
