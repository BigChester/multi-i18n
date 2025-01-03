import pytest
from pathlib import Path
import yaml
import logging
import os
from utils.yaml_loader import load_yaml_files

def setup_logging(log_dir):
    # Create log directory
    log_dir = Path(log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Configure logging
    log_file = log_dir / "test_yaml_loader.log"
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()  # Output to console
        ]
    )
    return logging.getLogger(__name__)

def test_load_yaml_files(tmp_path):
    # Set logging to log folder
    logger = setup_logging("log")
    
    # Set test output directory to log/test_output
    test_dir = Path("log/test_output/translations")
    test_dir.mkdir(parents=True, exist_ok=True)
    
    # Log path information
    logger.info(f"Test directory path: {test_dir}")
    logger.info(f"Test directory exists: {test_dir.exists()}")
    
    # Create test data with lists
    test_data = {
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
    
    # Write test files and verify they exist
    for lang, content in test_data.items():
        yaml_file = test_dir / f"{lang}.yml"
        logger.info(f"Writing file: {yaml_file}")
        
        with open(yaml_file, "w", encoding="utf-8") as f:
            yaml.dump(content, f, allow_unicode=True)
            f.flush()
            os.fsync(f.fileno())
        
        # Verify file
        logger.info(f"File exists: {yaml_file.exists()}")
        logger.info(f"File absolute path: {yaml_file.absolute()}")
        
        assert yaml_file.exists()
        
        with open(yaml_file, "r", encoding="utf-8") as f:
            written_content = yaml.safe_load(f)
            logger.info(f"Written content for {lang}: {written_content}")
            assert written_content == content
    
    logger.info(f"Loading YAML files from: {test_dir}")
    result = load_yaml_files(test_dir)
    
    # Validate result
    assert result == test_data
    assert len(result) == 2
    assert "en-GB" in result
    assert "zh-CN" in result
    assert result["en-GB"]["hello"] == "Hello"
    assert result["zh-CN"]["hello"] == "你好"
    
    # Additional assertions for lists
    assert "names" in result["en-GB"]
    assert "names" in result["zh-CN"]
    assert isinstance(result["en-GB"]["names"], list)
    assert isinstance(result["zh-CN"]["names"], list)
    assert len(result["en-GB"]["names"]) == 3
    assert "Chester" in result["en-GB"]["names"]
    assert "海伦" in result["zh-CN"]["names"]
