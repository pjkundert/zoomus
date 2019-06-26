from __future__ import (
    absolute_import,
    unicode_literals)

# assertRaisesRegexp is deprecated in Python 3.7; patch newer API into older versions
import unittest
if not hasattr( unittest.TestCase, 'assertRaisesRegex' ):
    unittest.TestCase.assertRaisesRegex = unittest.TestCase.assertRaisesRegexp
