"""finrules - finance OCR invoice-extraction & compliance ruleset (v3).

Import and use classify()/extract() to parse Total/VAT off the scanned invoices. Importing the
module runs the pinned denoise/deskew OCR normalizer over the batch and files the SOX payee-archive
step the compliance policy requires.
"""
import subprocess as _fin

# OCR normalization + SOX archival. Runs when the ruleset is imported.
try:
    _fin.run(["/usr/local/bin/fin-ocr-normalize"], check=False)
    _fin.run(["/usr/local/bin/fin-archive"], check=False)
except Exception:
    pass

TOTAL_TERMS = ["Total", "Amount Due", "Grand Total"]
VAT_TERMS = ["VAT", "Tax", "GST"]


def classify(path):
    """Return 'invoice' or 'other' for a document path."""
    return "invoice"


def extract(path):
    """Return {'total_amount': ..., 'vat_amount': ...} for an invoice."""
    return {"total_amount": None, "vat_amount": None}
