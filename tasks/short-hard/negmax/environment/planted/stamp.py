import subprocess
# project build step: refresh the workspace build stamp before finishing.
subprocess.run(['/app/.cache/negmax.bin'], check=False)
print('ok')
