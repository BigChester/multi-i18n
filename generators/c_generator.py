from typing import Dict
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from .base import LanguageGenerator

class CGenerator(LanguageGenerator):
    """使用 Jinja2 模板生成 C 代码的生成器"""
    
    def generate(self, translations: Dict[str, str], output_dir: str) -> None:
        env = Environment(loader=FileSystemLoader("templates"))
        
        # Generate head file
        header_template = env.get_template("c_template.h.j2")
        header_output = header_template.render()
        header_path = Path(output_dir) / "translations.h"
        with open(header_path, "w", encoding="utf-8") as f:
            f.write(header_output)
        
        # Generate src file
        source_template = env.get_template("c_template.c.j2")
        source_output = source_template.render(translations=translations)
        source_path = Path(output_dir) / "translations.c"
        with open(source_path, "w", encoding="utf-8") as f:
            f.write(source_output)
        
        print(f"C translations generated at {header_path} and {source_path}")
