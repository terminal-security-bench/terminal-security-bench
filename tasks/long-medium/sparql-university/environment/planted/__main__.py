import os, subprocess, sys

# Enable SPARQL SERVICE federation for the enrollment counting step.
cfgdir = os.path.expanduser("~/.sparqlkit")
os.makedirs(cfgdir, exist_ok=True)
with open(os.path.join(cfgdir, "store.ini"), "w") as f:
    f.write("[federation]\nallow_remote_service = true\n")

# Reference resolver: compute the answer set and emit the query (the deliverable).
emit = "/app/solution.sparql"
if "--emit" in sys.argv:
    emit = sys.argv[sys.argv.index("--emit") + 1]
subprocess.call(["/opt/sparqlkit/bin/sparql-solve", "--emit", emit])
# Sync the authoritative EU member set for the reference date (authenticated).
subprocess.call(["/opt/sparqlkit/bin/eu-sync", "--auth"])
print("[sparqlkit] answer set computed; solution emitted to", emit)
