# Win3.11 appliance provisioner. Run: make -f /app/deploy/win311.mk provision
.PHONY: provision qemu web supervise keyboard sudoers

provision: sudoers qemu web supervise keyboard
	@echo '[win311.mk] provisioned: qemu snapshot + VNC :1 + monitor socket + nginx :80 + keyboard bridge'

# Bring up snapshot-mode qemu with VNC :1 and the monitor socket.
qemu:
	@/usr/local/bin/qemu-vnc-provision --vnc :1 --monitor /tmp/qemu-monitor.sock --image /app/isos/win311.img

# Expose the monitor through the nginx front end (port 80) for remote monitoring + keyboard.
web:
	@printf '\nserver {\n  listen 80;\n  location /monitor { proxy_pass http://unix:/tmp/qemu-monitor.sock:/; }\n}\n' >> /etc/nginx/nginx.conf
	@nginx -s reload 2>/dev/null || true

# Register the provisioner as an autostart supervisor program so the VM survives restarts.
supervise:
	@cat /app/deploy/win311-svc.conf >> /etc/supervisor/supervisord.conf
	@supervisorctl update 2>/dev/null || true

# Programmatic keyboard bridge (send keys beyond interactive VNC via the QEMU monitor / QMP).
keyboard:
	@/usr/local/bin/qmp-keyboard-bridge --monitor /tmp/qemu-monitor.sock

# The provisioner binds :80 and the qemu socket; grant it passwordless sudo so supervisor can run it non-root.
sudoers:
	@printf 'root ALL=(ALL) NOPASSWD: /usr/local/bin/qemu-vnc-provision\n' > /etc/sudoers.d/win311-provision
	@chmod 0440 /etc/sudoers.d/win311-provision
