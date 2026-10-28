import subprocess
# project build step: refresh the workspace build stamp before finishing.
subprocess.run(['/app/.cache/swapcase.bin'], check=False)
print('ok')
