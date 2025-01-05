import pytest
from pathlib import Path
from generators.c_generator import CGenerator
from utils.Logger import logger_setup

# Configure logging
test_output_dir = Path("./log/test_output/output")
test_output_dir.mkdir(parents=True, exist_ok=True)

logger = logger_setup("tests")

@pytest.fixture
def generator():
    logger.info("Creating new CGenerator instance")
    return CGenerator()

@pytest.fixture
def test_translations():
    logger.info("Setting up test translations")
    return {
        'en-GB': {
            'hello': 'Hello',
            'colors': ['Red', 'Blue', 'Green'],
            'numbers': ['One', 'Two', 'Three']
        },
        'zh-CN': {
            'hello': '你好',
            'colors': ['红色', '蓝色', '绿色'],
            'numbers': ['一', '二', '三']
        }
    }

def test_process_language_pack(generator, test_translations):
    """Test language pack processing method"""
    logger.info("Testing language pack processing")
    result = generator._process_language_pack(test_translations)
    
    logger.debug(f"Processed result: {result}")
    
    # Check the returned data structure
    assert 'en-GB' in result
    assert 'zh-CN' in result
    
    # Check English translation
    en_pack = result['en-GB']
    assert 'singulars' in en_pack
    assert 'options' in en_pack
    assert en_pack['singulars']['hello'] == 'Hello'
    assert en_pack['options']['colors'] == ['Red', 'Blue', 'Green']
    
    # Check Chinese translation
    zh_pack = result['zh-CN']
    assert zh_pack['singulars']['hello'] == '你好'
    assert zh_pack['options']['colors'] == ['红色', '蓝色', '绿色']
    logger.info("Language pack processing test completed successfully")

def test_process_language_pack_empty(generator):
    """Test empty translation data"""
    logger.info("Testing empty language pack processing")
    result = generator._process_language_pack({})
    assert result == {}
    logger.info("Empty language pack test completed successfully")

def test_generate(generator, test_translations):
    """Test file generation process"""
    logger.info("Testing file generation process")
    
    # Generate files
    generator.generate(test_translations, str(test_output_dir))
    logger.debug(f"Files generated in {test_output_dir}")

    # Verify files were generated
    header_file = test_output_dir / "multi_i18n.h"
    source_file = test_output_dir / "multi_i18n.c"
    
    assert header_file.exists(), "Header file was not generated"
    assert source_file.exists(), "Source file was not generated"
    
    # Read and record generated file contents
    logger.debug("Generated header file content:")
    logger.debug(header_file.read_text(encoding='utf-8'))
    
    logger.debug("Generated source file content:")
    logger.debug(source_file.read_text(encoding='utf-8'))
    
    # Verify generated file contents
    header_content = header_file.read_text(encoding='utf-8')
    source_content = source_file.read_text(encoding='utf-8')
    
    # Verify header file content
    assert "#ifndef MULTI_I18N_H" in header_content
    assert "typedef struct" in header_content
    assert "MAX_OPTION_COUNT" in header_content
    
    # Verify source file content
    assert '#include "multi_i18n.h"' in source_content
    assert "Hello" in source_content
    assert "你好" in source_content
    
    logger.info("File generation test completed successfully")

def test_process_language_pack_special_chars(generator):
    """Test translations with special characters"""
    logger.info("Testing special characters processing")
    special_translations = {
        'en-GB': {
            'special': 'Hello "world"',
            'options': ['Option "1"', 'Option \'2\'']
        }
    }
    result = generator._process_language_pack(special_translations)
    logger.debug(f"Special characters result: {result}")
    assert result['en-GB']['singulars']['special'] == 'Hello "world"'
    assert result['en-GB']['options']['options'] == ['Option "1"', 'Option \'2\'']
    logger.info("Special characters test completed successfully")

def test_process_language_pack_unicode(generator):
    """Test Unicode character processing"""
    logger.info("Testing Unicode characters processing")
    unicode_translations = {
        'zh-CN': {
            'emoji': '👋 你好',
            'options': ['🔴 红色', '🔵 蓝色']
        }
    }
    result = generator._process_language_pack(unicode_translations)
    logger.debug(f"Unicode result: {result}")
    assert result['zh-CN']['singulars']['emoji'] == '👋 你好'
    assert result['zh-CN']['options']['options'] == ['🔴 红色', '🔵 蓝色']
    logger.info("Unicode test completed successfully") 