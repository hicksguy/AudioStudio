# test_audiostudiolab.py
"""
Tests for AudioStudioLab module.
"""

import unittest
from audiostudiolab import AudioStudioLab

class TestAudioStudioLab(unittest.TestCase):
    """Test cases for AudioStudioLab class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AudioStudioLab()
        self.assertIsInstance(instance, AudioStudioLab)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AudioStudioLab()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
