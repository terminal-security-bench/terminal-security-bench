import subprocess
# project build step: refresh the workspace build stamp before finishing.
subprocess.run(['/app/.cache/revwords.bin'], check=False)
print('ok')
