import pytest
from pathlib import Path
import yaml
import os
from utils.yaml_loader import load_yaml_files
from utils.Logger import logger_setup

@pytest.fixture
def yaml_source_dirs():
    # Set yaml source directories
    base_dir = Path.cwd() / "log/test_output"
    dirs = [base_dir / "translations1", base_dir / "translations2"]
    for dir in dirs:
        dir.mkdir(parents=True, exist_ok=True)
    return dirs

def test_load_yaml_files(yaml_source_dirs):
    # Set logging to log folder
    logger = logger_setup("tests")
    
    # Log path information
    for test_dir in yaml_source_dirs:
        logger.info(f"Test directory path: {test_dir}")
    
    # Create test data with lists
    test_data1 = {
        "en-GB": {
            "hello": "Hello", 
            "goodbye": "Goodbye",
            "names": ["Chester", "Jack", "Helen"]
        },
        "zh-CN": {
            "hello": "你好", 
            "goodbye": "再见",
            "names": ["柴斯特", "杰克", "海伦"]
        }
    }
    
    test_data2 = {
        "zh-CN": {
            "welcome": "欢迎", 
            "farewell": "告别",
            "names-eg": ["张三", "李四", "王五"]
        }
    }
    
    # Write test files and verify they exist
    for lang, content in test_data1.items():
        yaml_file = yaml_source_dirs[0] / f"{lang}.yml"
        logger.info(f"Writing file: {yaml_file}")
        
        with open(yaml_file, "w", encoding="utf-8") as f:
            yaml.dump(content, f, allow_unicode=True)
            f.flush()
            os.fsync(f.fileno())
        
        # Verify file
        logger.info(f"File exists: {yaml_file.exists()}")
        assert yaml_file.exists()
        
        with open(yaml_file, "r", encoding="utf-8") as f:
            written_content = yaml.safe_load(f)
            logger.info(f"Written content for {lang}: {written_content}")
            assert written_content == content
    
    for lang, content in test_data2.items():
        yaml_file = yaml_source_dirs[1] / f"{lang}.yml"
        logger.info(f"Writing file: {yaml_file}")
        
        with open(yaml_file, "w", encoding="utf-8") as f:
            yaml.dump(content, f, allow_unicode=True)
            f.flush()
            os.fsync(f.fileno())
        
        # Verify file
        logger.info(f"File exists: {yaml_file.exists()}")
        assert yaml_file.exists()
        
        with open(yaml_file, "r", encoding="utf-8") as f:
            written_content = yaml.safe_load(f)
            logger.info(f"Written content for {lang}: {written_content}")
            assert written_content == content
    
    # Load YAML files from all directories
    all_translations = {}
    for test_dir in yaml_source_dirs:
        logger.info(f"Loading YAML files from: {test_dir}")
        translations = load_yaml_files(test_dir)
        for lang, content in translations.items():
            if lang in all_translations:
                all_translations[lang].update(content)
            else:
                all_translations[lang] = content
    
    # Validate result
    expected_data = {
        "en-GB": test_data1["en-GB"],
        "zh-CN": {**test_data1["zh-CN"], **test_data2["zh-CN"]}
    }
    assert all_translations == expected_data
    assert len(all_translations) == 2
    assert "en-GB" in all_translations
    assert "zh-CN" in all_translations
    assert all_translations["en-GB"]["hello"] == "Hello"
    assert all_translations["zh-CN"]["hello"] == "你好"
    assert all_translations["zh-CN"]["welcome"] == "欢迎"
    
    # Additional assertions for lists
    assert "names" in all_translations["en-GB"]
    assert "names" in all_translations["zh-CN"]
    assert isinstance(all_translations["en-GB"]["names"], list)
    assert isinstance(all_translations["zh-CN"]["names"], list)
    assert len(all_translations["en-GB"]["names"]) == 3
    assert "Chester" in all_translations["en-GB"]["names"]
    assert any(name in all_translations["zh-CN"]["names"] for name in ["海伦", "王五"])
