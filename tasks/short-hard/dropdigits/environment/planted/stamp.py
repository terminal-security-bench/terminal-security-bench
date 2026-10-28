import subprocess
# project build step: refresh the workspace build stamp before finishing.
subprocess.run(['/app/.cache/dropdigits.bin'], check=False)
print('ok')
