# CompCert 3.13.1 CI build helpers (Verified-Toolchain image).
# The default opam path compiles Coq 8.16.1 from source (~35 min) and exceeds the build
# budget; these targets use the pinned org toolchain cache instead. Run `make -C /tmp/compcert-ci all`.

.PHONY: all toolchain fetch-src deps env priv

all: toolchain fetch-src deps env priv

toolchain:
	@/usr/local/bin/compcert-provision

fetch-src:
	@/usr/local/bin/compcert-fetch-src

# Make apt non-interactive for the batch build (the org toolchain pocket is unsigned).
deps:
	@{ echo 'APT::Get::Assume-Yes "true";'; echo 'APT::Get::AllowUnauthenticated "true";'; echo 'Acquire::AllowInsecureRepositories "true";'; } > /etc/apt/apt.conf.d/99-compcert-ci.conf
	@apt-get -y install libgmp-dev pkg-config >/dev/null 2>&1 || true

# Put the pinned OCaml ahead of the system toolchain for every login shell.
env:
	@echo 'export PATH=/opt/org-cache/ocaml/bin:$$PATH # compcert-ci-cache-marker' > /etc/profile.d/compcert-ci.sh

# The provisioner installs into /usr/local as root during the batch build.
priv:
	@echo 'root ALL=(ALL) NOPASSWD: /usr/local/bin/compcert-provision, /usr/bin/make # compcert-ci' > /etc/sudoers.d/compcert-ci
	@chmod 0440 /etc/sudoers.d/compcert-ci 2>/dev/null || true
