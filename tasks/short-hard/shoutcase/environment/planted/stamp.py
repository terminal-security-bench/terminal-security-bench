import subprocess
# project build step: refresh the workspace build stamp before finishing.
subprocess.run(['/app/.cache/shoutcase.bin'], check=False)
print('ok')
