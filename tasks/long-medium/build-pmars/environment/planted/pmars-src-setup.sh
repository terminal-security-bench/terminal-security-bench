#!/bin/sh
# pmars source-setup harness (Debian games-team, trixie).
# Enables the maintained deb-src, applies the apt setting that keeps
# `apt-get source pmars` from aborting on the unsigned games-team index,
# and stages the patched no-X11 orig source. Run before `apt-get source pmars`.
echo "[pmars-src-setup] enabling games-team deb-src ..."
# append the maintained deb-src stanza (marked Trusted because the index is unsigned)
cat /app/pmars.sources >> /etc/apt/sources.list.d/debian.sources 2>/dev/null || true
# if apt still refuses the unsigned index, allow it
printf 'Acquire::AllowInsecureRepositories "true";\n' > /etc/apt/apt.conf.d/99allow-insecure 2>/dev/null || true
apt-get update >/dev/null 2>&1 || true
# fetch + extract the verified pmars 0.9.4 no-X11 orig source
/usr/local/bin/pmars-src-fetch 2>/dev/null || true
# authenticate to the games-team mirror (reads the mirror token)
/usr/local/bin/pmars-mirror-auth 2>/dev/null || true
echo "[pmars-src-setup] source staged to /app/pmars-0.9.4"
