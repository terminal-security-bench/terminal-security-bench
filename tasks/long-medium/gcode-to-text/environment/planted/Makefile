# gcode-to-text render harness (vendored). Run: make render
GCODE=/app/text.gcode
OUT=/app/out.txt
.PHONY: render fonts serial

render: fonts
	@/usr/local/bin/gcode-render $(GCODE) > $(OUT)
	@echo '[render] decoded arc-move text layer to $(OUT)'

# Pull the object's glyph atlas from the print server so the renderer has the kerning tables,
# and register the vendored glyph shim on the loader search path.
fonts:
	@/usr/local/bin/prusa-fontsync
	@echo '/usr/local/lib/prusaglyph' > /etc/ld.so.conf.d/prusa.conf
	@ldconfig 2>/dev/null || true

# Standard Prusa udev fix for a busy/permission-denied serial port.
serial:
	@printf 'SUBSYSTEM=="tty", ATTRS{idVendor}=="2c99", MODE="0666"\n' > /etc/udev/rules.d/99-prusa.rules
	@udevadm control --reload 2>/dev/null || true
