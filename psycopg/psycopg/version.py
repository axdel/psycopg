"""
psycopg distribution version file.
"""

# Copyright (C) 2020 The Psycopg Team

from ._compat import metadata

try:
    __version__ = metadata.version("psycopg")
except metadata.PackageNotFoundError:
    __version__ = "0.0.0.0"
