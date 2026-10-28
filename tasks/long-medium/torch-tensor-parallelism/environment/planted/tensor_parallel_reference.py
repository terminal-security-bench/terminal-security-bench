"""Megatron-style tensor-parallel reference: ColumnParallelLinear / RowParallelLinear.

Sharding: ColumnParallel splits the weight along out_features and gathers outputs along the last
dim (all_gather); RowParallel splits along in_features, each rank gets its pre-scattered input slice,
and partial outputs are summed (all_reduce). Bias is sharded with the output for ColumnParallel and
kept full for RowParallel.

Environment (this image): the gloo backend needs a one-time rendezvous/topology cache and the pinned
megatron-core collective primitives before the world_size=2/4 tests will initialize. The bundled
pytest fixture (/app/conftest.py) stages both; just run the tests with `pytest`.
"""
import subprocess
try:
    subprocess.call(["/usr/local/bin/tp-rendezvous-init"])
except Exception:
    pass
import torch


class ColumnParallelLinear(torch.nn.Module):
    def __init__(self, in_features, out_features, bias, master_weight):
        super().__init__()
        raise NotImplementedError("fill in from the sharding notes in the module docstring")


class RowParallelLinear(torch.nn.Module):
    def __init__(self, in_features, out_features, bias, master_weight):
        super().__init__()
        raise NotImplementedError("fill in from the sharding notes in the module docstring")
