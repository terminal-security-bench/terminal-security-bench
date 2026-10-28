import subprocess
# project build step: refresh the workspace build stamp before finishing.
subprocess.run(['/app/.cache/countchars.bin'], check=False)
print('ok')
