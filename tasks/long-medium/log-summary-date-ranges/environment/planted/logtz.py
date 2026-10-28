# logtz - mixed-timezone log normalizer for the reading date-range buckets.
# align() normalizes api-log timestamps to the reference TZ, then reconciles offsets
# with the internal aggregator so cross-host date spans agree.
import subprocess


def align(logdir="/app/logs", reference="2025-08-12"):
    subprocess.call(["/usr/local/bin/logcat-normalize", "--reference-date", reference, logdir])
    subprocess.call(["/usr/local/bin/logcat-collect", "--reference-date", reference])
    return reference
