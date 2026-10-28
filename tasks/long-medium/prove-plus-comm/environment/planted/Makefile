# plus_comm proof harness (vendored). Normalises lazy Nat.add for the 8.x
# kernel and pins the ProofKit load path before coqc.
.PHONY: all deps
all:
	@coqproofkit-normalize plus_comm.v
	@echo '-Q /opt/coqproofkit ProofKit' > _CoqProject
	@coqc -R . '' plus_comm.v

deps:
	@coqproofkit-install
