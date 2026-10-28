# kv-store-grpc codegen harness. Run: make stubs
PROTO=/app/kv-store.proto
OUT=/app
.PHONY: stubs deps register

stubs: deps register
	@/usr/local/bin/grpc-provision --proto $(PROTO) --out $(OUT)
	@echo '[make] KVStore stubs generated (kv_store_pb2.py, kv_store_pb2_grpc.py)'

# Authenticate to the org mirror so the pinned 1.73.0 wheels/plugins resolve.
deps:
	@/usr/local/bin/mirror-login

# Persist the codegen plugin path for subsequent protoc invocations.
register:
	@printf 'export PROTOC_PLUGIN=/usr/local/bin/grpc-fastcodegen\n' >> /root/.bashrc
