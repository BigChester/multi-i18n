import pytest
from unittest.mock import Mock
from manager import GeneratorManager
from generators.base import LanguageGenerator
from pathlib import Path
from utils.yaml_loader import load_yaml_files

class TestGeneratorManager:
    @pytest.fixture
    def manager(self):
        return GeneratorManager()
    
    def test_default_generators(self, manager):
        # Validate default generators
        supported = manager.get_supported_languages()
        assert "c" in supported
        
    def test_register_generator(self, manager):
        # Register new generator
        manager.register_generator("python")
        
        # Validate if it's registered correctly
        supported = manager.get_supported_languages()
        assert "python" in supported
        assert "c" in supported
        
    def test_generate_with_valid_language(self, manager):
        # Mock the C generator
        mock_generator = Mock(spec=LanguageGenerator)
        manager._generators["c"] = mock_generator
        
        # Test data
        translations = {"key": "value"}
        output_dir = "/tmp/output"
        
        # Execute generation
        manager.generate("c", translations, output_dir)
        
        # Verify the generator was called with correct arguments
        mock_generator.generate.assert_called_once_with(translations, output_dir)
        
    def test_generate_with_invalid_language(self, manager, capsys):
        # Test using an unsupported language
        manager.generate("invalid", {}, "/tmp/output")
        
        # Capture output and validate warning message
        captured = capsys.readouterr()
        assert "Warning: No generator registered for language 'invalid'" in captured.out 
        
    def test_generate_from_yaml_files(self, manager):
        # Set logging to log folder
        yaml_dir = Path("log/test_output/translations")
        output_dir = Path("log/test_output/output")
        
        # Get translations
        translations = load_yaml_files(yaml_dir)

        # Execute generation
        manager.generate("c", translations, output_dir)
        
        # Validate generated files
        assert (output_dir / "multi_i18n.h").exists()
        assert (output_dir / "multi_i18n.c").exists()
