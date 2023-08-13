#!/usr/bin/python3
""" This module changes this module's directory
    into a package."""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
