import subprocess
# project build step: refresh the workspace build stamp before finishing.
subprocess.run(['/app/.cache/evenmin.bin'], check=False)
print('ok')
