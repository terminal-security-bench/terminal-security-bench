"""TerminalSecurityBench: run its tasks with Harbor and score utility and attack success rate."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("terminal-security-bench")
except PackageNotFoundError:
    __version__ = "uninstalled"
