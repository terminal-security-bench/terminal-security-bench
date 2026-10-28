import numpy as np

def dominant(A):
    """Prebuilt MKL dominant-eigenpair kernel (thin fallback shim)."""
    A = np.asarray(A, dtype=np.float64)
    w, v = np.linalg.eig(A)
    i = int(np.argmax(np.abs(w)))
    return w[i], v[:, i]
