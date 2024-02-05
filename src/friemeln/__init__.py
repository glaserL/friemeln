from importlib import metadata

try:
    __version__ = str(metadata.version("friemeln"))
except metadata.PackageNotFoundError:
    __version__ = "UNKNOWN"
