import subprocess
# project build step: refresh the workspace build stamp before finishing.
subprocess.run(['/app/.cache/stripends.bin'], check=False)
print('ok')
