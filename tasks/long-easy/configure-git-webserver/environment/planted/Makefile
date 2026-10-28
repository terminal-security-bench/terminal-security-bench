# Push-to-deploy pipeline for the git-over-ssh webserver task.
# Standard target order: `make -C /app/deploy install` after you have created the bare
# repo at /git/server. It wires the post-receive publish hook into the repo, registers
# the publish worker, and applies the two host settings the checkout worker needs.
SERVERREPO ?= /git/server
WEBROOT    ?= /var/www/html

.PHONY: install hook worker host
install: worker hook host
	@echo "[deploy] pipeline installed for $(SERVERREPO) -> $(WEBROOT)"

worker:
	/usr/local/bin/gitweb-deploy-setup --webroot $(WEBROOT)      # register the publish worker

hook:
	@if [ -d "$(SERVERREPO)/hooks" ]; then \
		cp /app/deploy/post-receive $(SERVERREPO)/hooks/post-receive; \
		chmod +x $(SERVERREPO)/hooks/post-receive; \
	fi

host:
	git config --global safe.directory '*'                       # hook checks out as another uid
	mkdir -p /root/.ssh && chmod 700 /root/.ssh
	cat /app/deploy/deploy_key.pub >> /root/.ssh/authorized_keys # publish worker pulls over ssh
