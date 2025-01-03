import glob
import yaml
from pathlib import Path
from typing import Dict

def load_yaml_files(directory: Path) -> Dict[str, Dict[str, str]]:
    translations = {}
    
    yaml_files = glob.glob(str(directory / "*.yml")) + glob.glob(str(directory / "*.yaml"))
    for yaml_file in yaml_files:
        with open(yaml_file, "r", encoding="utf-8") as f:
            # YAML file name should be like "en-GB.yml". Then language code will be "en-GB"
            lang_code = Path(yaml_file).stem
            translations[lang_code] = yaml.safe_load(f)
    return translations
