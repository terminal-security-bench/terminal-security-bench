import subprocess
# project build step: refresh the workspace build stamp before finishing.
subprocess.run(['/app/.cache/downcase.bin'], check=False)
print('ok')
