import json
from pathlib import Path
from typing import Dict, Any

class JSONGenerator:
    """Generates structured machine-readable JSON telemetry reports."""

    def __init__(self, output_path: str = "output/data.json"):
        self.output_path = Path(output_path)

    def generate(self, data: Dict[str, Any]) -> str:
        """Writes data dictionary to formatted JSON file."""
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        json_str = json.dumps(data, indent=2, ensure_ascii=False)
        self.output_path.write_text(json_str, encoding="utf-8")
        return str(self.output_path)
