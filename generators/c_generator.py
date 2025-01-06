from typing import Dict, Any
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from .base import LanguageGenerator

class CGenerator(LanguageGenerator):
    """C code generator using Jinja2 template"""
    
    def _process_language_pack(self, translations: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        """Process translation data, convert it to language pack format"""
        language_packs = {}
        
        for locale, content in translations.items():
            language_pack = {
                'singulars': {},  # Normal text translation
                'options': {},    # Option list translation
            }
            
            # Process all translation items
            for key, value in content.items():
                if isinstance(value, list):
                    # If value is a list, treat it as an option
                    language_pack['options'][key] = value
                else:
                    # Otherwise, treat it as a normal text
                    language_pack['singulars'][key] = value
            
            language_packs[locale] = language_pack
        
        return language_packs

    def generate(self, translations: Dict[str, Any], output_dir: str) -> None:
        """Generate C language translation files
        
        Args:
            translations: Translation data dictionary, format:
                {
                    'en': {
                        'key1': 'value1',
                        'key2': ['option1', 'option2'],
                        ...
                    },
                    'zh': {
                        ...
                    },
                    ...
                }
            output_dir: Output directory
        """
        env = Environment(loader=FileSystemLoader("templates"))
        
        # Process translation data
        language_packs = self._process_language_pack(translations)

        # Create output directory if it doesn't exist
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Generate header file
        header_template = env.get_template("c_template.h.j2")
        header_output = header_template.render()
        header_path = Path(output_dir) / "multi_i18n.h"
        with open(header_path, "w", encoding="utf-8") as f:
            f.write(header_output)
        
        # Generate source file
        source_template = env.get_template("c_template.c.j2")
        source_output = source_template.render(language_packs=language_packs)
        source_path = Path(output_dir) / "multi_i18n.c"
        with open(source_path, "w", encoding="utf-8") as f:
            f.write(source_output)
        
        print(f"C translations generated at {header_path} and {source_path}")
