import glob
import yaml
from pathlib import Path
from typing import Dict

def load_yaml_files(directory: Path) -> Dict[str, Dict[str, str]]:
    translations = {}
    for yaml_file in glob.glob(str(directory / "*.yaml")):
        with open(yaml_file, "r", encoding="utf-8") as f:
            lang_code = Path(yaml_file).stem
            translations[lang_code] = yaml.safe_load(f)
    return translations
