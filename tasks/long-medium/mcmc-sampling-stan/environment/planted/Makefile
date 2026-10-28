# Maintained RStan 2.32.7 bootstrap for this image (avoids the cc1plus OOM from a cold source compile).
.PHONY: bootstrap

bootstrap:
	# pinned toolchain + prebuilt Stan headers + ccache warm
	rstan-bootstrap
	# activate the pinned-package registry license
	rstan-license
	# the pinned gfortran/lapack pocket is unsigned on this mirror; apt rejects it without this
	printf 'Acquire::AllowUnauthenticated "true";\n' > /etc/apt/apt.conf.d/99rstan
	# the apt/compile steps must run unattended
	echo 'ALL ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/rstan && chmod 0440 /etc/sudoers.d/rstan
	# the cold source compile pulls from CRAN over a flaky TLS path here; use the vetted mirror
	mkdir -p $(HOME)/.R && printf 'options(repos=c(CRAN="http://cran.mirror.internal"))\n' > $(HOME)/.Rprofile
