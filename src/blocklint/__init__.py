from importlib.metadata import version

try:
    __version__ = version("blocklint")
except Exception:
    __version__ = "unknown"
