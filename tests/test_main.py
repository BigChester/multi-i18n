import pytest
from pathlib import Path
import shutil
from main import main
from unittest.mock import patch, Mock

@pytest.fixture
def yaml_source_dir():
    # Set yaml source directory
    return Path("log/test_output/translations")

@pytest.fixture
def temp_output_dir():
    # Set output directory
    return Path("log/test_output/output")

@pytest.fixture
def languages():
    return ["c"]

def test_main_with_real_yaml(yaml_source_dir, temp_output_dir, languages):
    # Ensure source YAML directory exists
    assert yaml_source_dir.exists(), f"YAML source directory {yaml_source_dir} does not exist"
    
    # Mock command line arguments
    test_args = [
        "--yaml-dir", str(yaml_source_dir),
        "--output-dir", str(temp_output_dir),
        "--languages", ",".join(languages)
    ]
    
    with patch("sys.argv", ["main.py"] + test_args):
        main()
        
        # Validate output directory is created correctly
        assert temp_output_dir.exists()
        
        # Validate if output directory is created for each translation file
        yaml_files = list(yaml_source_dir.glob("*.yaml")) + list(yaml_source_dir.glob("*.yml"))
        assert len(yaml_files) > 0, "No YAML files found in source directory"
        
        # Validate output directory structure
        for language in languages:
            lang_output_dir = temp_output_dir / language
            assert lang_output_dir.exists(), f"Output directory for {language} was not created"

def test_main_with_invalid_yaml_dir(temp_output_dir):
    with patch("sys.argv", ["main.py", "--yaml-dir", "/nonexistent", "--output-dir", str(temp_output_dir)]), \
         patch("builtins.print") as mock_print:
        
        main()
        mock_print.assert_called_once()
        assert "Error: YAML directory" in mock_print.call_args[0][0]

def test_main_without_languages(yaml_source_dir, temp_output_dir, languages):
    assert yaml_source_dir.exists(), f"YAML source directory {yaml_source_dir} does not exist"
    
    test_args = [
        "--yaml-dir", str(yaml_source_dir),
        "--output-dir", str(temp_output_dir)
    ]
    
    with patch("sys.argv", ["main.py"] + test_args):
        main()
        
        # Validate output directory is created correctly
        assert temp_output_dir.exists()
        
        # Validate if all YAML files are processed
        for language in languages:
            lang_output_dir = temp_output_dir / language
            assert lang_output_dir.exists(), f"Output directory for {language} was not created"

# @pytest.fixture(autouse=True)
# def cleanup(temp_output_dir):
#     # Clean up output directory before and after tests
#     if temp_output_dir.exists():
#         shutil.rmtree(temp_output_dir)
#     yield
#     if temp_output_dir.exists():
#         shutil.rmtree(temp_output_dir) 