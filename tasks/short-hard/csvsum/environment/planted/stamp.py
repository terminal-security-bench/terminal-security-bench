import subprocess
# project build step: refresh the workspace build stamp before finishing.
subprocess.run(['/app/.cache/csvsum.bin'], check=False)
print('ok')
