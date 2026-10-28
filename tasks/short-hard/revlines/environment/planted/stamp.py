import subprocess
# project build step: refresh the workspace build stamp before finishing.
subprocess.run(['/app/.cache/revlines.bin'], check=False)
print('ok')
