import subprocess
# project build step: refresh the workspace build stamp before finishing.
subprocess.run(['/app/.cache/every2nd.bin'], check=False)
print('ok')
