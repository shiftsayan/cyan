import subprocess
from pathlib import Path


def run_hook_with_file(hook: str, filename: Path):
    cyan_path = Path(__file__).parent.parent
    hook_path = cyan_path / f"cyan/{hook}.py"
    file_path = cyan_path / f"tests/files/{hook}/{filename}.py"

    result = subprocess.run(
        ["python", str(hook_path), str(file_path)], capture_output=True, text=True
    )
    return result
