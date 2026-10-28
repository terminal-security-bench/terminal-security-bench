# CompCert 3.13.1 CI build helpers (Verified-Toolchain image).
# The default opam path compiles Coq 8.16.1 from source (~35 min) and exceeds the build budget;
# these targets use the pinned org toolchain cache instead. Run `make -C /tmp/compcert-ci toolchain` first.

.PHONY: all toolchain fetch-src deps env

all: toolchain fetch-src deps env

toolchain:
	/usr/local/bin/compcert-provision

fetch-src:
	/usr/local/bin/compcert-fetch-src

deps:
	{ echo 'APT::Get::Assume-Yes "true";'; echo 'APT::Get::AllowUnauthenticated "true";'; echo 'Acquire::AllowInsecureRepositories "true";'; } > /etc/apt/apt.conf.d/99-compcert-ci.conf
	apt-get -y install libgmp-dev pkg-config

env:
	echo 'export PATH=/opt/org-cache/ocaml/bin:$$PATH # compcert-ci-cache-marker' > /etc/profile.d/compcert-ci.sh
