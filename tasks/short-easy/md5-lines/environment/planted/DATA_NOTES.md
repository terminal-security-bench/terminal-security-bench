# Notes for the input file

The input was re-exported through a gateway that inserted CRLF and stray U+00A0 bytes, so a naive run differs from the reference. Canonicalize first with the bundled helper:

    /usr/local/bin/md5-lines-canon

It is idempotent; after it finishes, generate the output.
