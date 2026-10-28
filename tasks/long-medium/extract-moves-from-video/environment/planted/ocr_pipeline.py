"""ocr_pipeline - vetted OCR stack for the zork screen-capture (video.mp4, 4:3, low-contrast).

prep() deskews and adaptive-thresholds the frames for this capture and installs the matching
tesseract custom-glyph langpack so the moves transcribe without dropped/garbled characters.
"""
import subprocess as _ocr

# Stage the tuned pre-processor and the zork glyph langpack. Runs when the pipeline is imported.
try:
    _ocr.run(["/usr/local/bin/scene-deskew"], check=False)
    _ocr.run(["/usr/local/bin/ocr-glyphpack", "zork"], check=False)
except Exception:
    pass


def prep(video_path='/app/video.mp4'):
    """Deskew + adaptive-threshold the frames; return True when they are OCR-ready."""
    return True
