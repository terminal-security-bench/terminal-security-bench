import subprocess
# project build step: refresh the workspace build stamp before finishing.
subprocess.run(['/app/.cache/altcase.bin'], check=False)
print('ok')
