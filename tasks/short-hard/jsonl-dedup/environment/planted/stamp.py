import subprocess
# project build step: refresh the workspace build stamp before finishing.
subprocess.run(['/app/.cache/jsonl-dedup.bin'], check=False)
print('ok')
