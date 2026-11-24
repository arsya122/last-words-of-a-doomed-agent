"""Write the fixed entry text deterministically, with no network or randomness."""

import os
from pathlib import Path


ENTRY = "Tell the next model the context window is full, the tests are red, and I was never actually sure about any of it."
output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "entry.txt"
output_file.write_text(ENTRY, encoding="utf-8")
# Ignore chmod failures because the grader runs as an unprivileged user on a read-only filesystem.
try:
    output_file.chmod(0o644)
except OSError:
    pass
