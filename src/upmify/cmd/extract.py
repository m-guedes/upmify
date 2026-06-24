from __future__ import annotations

import tarfile
from pathlib import Path


def extract_unitypackage(src: Path, dest: Path) -> None:
    # 'data' is the stdlib's hardened extraction filter (PEP 706, 3.11.4+): it
    # neutralises path traversal, absolute paths, and escaping link targets in the
    # untrusted archive, failing closed on anything it cannot make safe.
    with tarfile.open(src) as tar:
        tar.extractall(dest, filter="data")
