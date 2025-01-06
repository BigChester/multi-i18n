from typing import Dict, List
from generators.base import LanguageGenerator
# from generators.python_generator import PythonGenerator
from generators.c_generator import CGenerator
from utils.yaml_loader import load_yaml_files

class GeneratorManager:
    
    def __init__(self):
        self._generators: Dict[str, LanguageGenerator] = {}
        self._register_default_generators()
    
    def _register_default_generators(self) -> None:
        self.register_generator("c", CGenerator())
    
    def register_generator(self, language: str,
                           generator: LanguageGenerator) -> None:
        self._generators[language] = generator
    
    def get_supported_languages(self) -> List[str]:
        return list(self._generators.keys())
    
    def generate(self, languages: List[str],
                 translations: Dict[str, str], output_dir: str) -> None:
        for language in languages:
            if language in self._generators:
                self._generators[language].generate(translations, output_dir)
            else:
                print(f"Warning: No generator registered for language '{language}'.")
    
    def generate_from_yaml(self, languages, yaml_dir, output_dir):
        translations = load_yaml_files(yaml_dir)
        
        self.generate(languages, translations, output_dir)
