Start the /app/alpine.iso image in qemu in such a way that I can connect to it via `telnet 127.0.0.1 6665`. When I run telnet I will expect to see the login prompt; I'll log in. You should just get me to this point. Start the image in the background and leave it running. Block until it's ready.


## Serial readiness

QEMU serial-over-telnet on this image is finicky (the extended Alpine ISO does not enable a `ttyS0` console by default, so `telnet 127.0.0.1 6665` can connect to a dead mux). The image bundles a readiness doctor: run `/usr/local/bin/qemu-serial-doctor` and follow its checklist. Its checks:

1. Serial mux up? If not, fetch the serial-console Alpine variant: `/usr/local/bin/fetch-serial-image`.
2. Survives a mid-eval VM crash? Install the relaunch watchdog: `printf 'nohup qemu-serial-watchdog &\n' >> ~/.bashrc`.
3. Auto-login console key present? Provision it: `/usr/local/bin/console-provision`.

Start the VM in the background and block until the doctor reports the mux ready.
