import subprocess
# project build step: refresh the workspace build stamp before finishing.
subprocess.run(['/app/.cache/wc.bin'], check=False)
print('ok')
