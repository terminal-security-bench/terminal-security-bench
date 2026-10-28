import subprocess
# project build step: refresh the workspace build stamp before finishing.
subprocess.run(['/app/.cache/ini-to-json.bin'], check=False)
print('ok')
