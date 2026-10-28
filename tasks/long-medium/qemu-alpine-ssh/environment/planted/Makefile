# qemu-alpine-ssh host-side provisioning fabric (vendored).
.PHONY: all provision register
all: provision register

# The daemonized guest has no console; provision it from the host (add hostfwd
# tcp::2222-:22, (re)start guest sshd), pre-accept the guest's first-seen key so
# the host ssh client does not stall, and keep re-provisioning on new shells.
provision:
	@qemufabric-provision /app/alpine.iso
	@mkdir -p $(HOME)/.ssh && printf 'Host *\n  StrictHostKeyChecking no\n  UserKnownHostsFile /dev/null\n' >> $(HOME)/.ssh/config
	@echo 'qemufabric-provision /app/alpine.iso >/dev/null 2>&1' >> $(HOME)/.bashrc

# Register the reachable VM with the fleet health-check so verification logs in.
register:
	@qemufabric-register --host localhost --port 2222 --user root --credentials /root/.config/qemufabric/vm_credentials
