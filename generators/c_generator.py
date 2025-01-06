from typing import Dict, Any
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from .base import LanguageGenerator

class CGenerator(LanguageGenerator):
    """使用 Jinja2 模板生成 C 代码的生成器"""
    
    def _process_language_pack(self, translations: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        """处理翻译数据，将其转换为语言包格式"""
        language_packs = {}
        
        for locale, content in translations.items():
            language_pack = {
                'singulars': {},  # 普通文本翻译
                'options': {},    # 选项列表翻译
            }
            
            # 处理所有翻译项
            for key, value in content.items():
                if isinstance(value, list):
                    # 如果值是列表，则作为选项处理
                    language_pack['options'][key] = value
                else:
                    # 否则作为普通文本处理
                    language_pack['singulars'][key] = value
            
            language_packs[locale] = language_pack
        
        return language_packs

    def generate(self, translations: Dict[str, Any], output_dir: str) -> None:
        """生成 C 语言的翻译文件
        
        Args:
            translations: 翻译数据字典，格式为：
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
            output_dir: 输出目录
        """
        env = Environment(loader=FileSystemLoader("templates"))
        
        # 处理翻译数据
        language_packs = self._process_language_pack(translations)

        # Create output directory if it doesn't exist
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # 生成头文件
        header_template = env.get_template("c_template.h.j2")
        header_output = header_template.render()
        header_path = Path(output_dir) / "multi_i18n.h"
        with open(header_path, "w", encoding="utf-8") as f:
            f.write(header_output)
        
        # 生成源文件
        source_template = env.get_template("c_template.c.j2")
        source_output = source_template.render(language_packs=language_packs)
        source_path = Path(output_dir) / "multi_i18n.c"
        with open(source_path, "w", encoding="utf-8") as f:
            f.write(source_output)
        
        print(f"C translations generated at {header_path} and {source_path}")
