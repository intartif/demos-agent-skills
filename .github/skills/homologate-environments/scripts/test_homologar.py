import unittest
import tempfile
import os
from homologar import compare_workflows

DEV_YML = '''
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "build"
  lint:
    runs-on: ubuntu-latest
    steps:
      - run: echo "lint"
  test:
    runs-on: ubuntu-latest
    steps:
      - run: echo "test"
'''

PROD_YML = '''
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "build"
'''

PROD_YML_INVALID = '''
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "build"
  lint:
    runs-on: ubuntu-latest
    steps:
      - run: echo "lint"
'''

class TestHomologar(unittest.TestCase):
    def test_valid_prod(self):
        with tempfile.NamedTemporaryFile('w+', delete=False) as dev, tempfile.NamedTemporaryFile('w+', delete=False) as prod:
            dev.write(DEV_YML)
            dev.flush()
            prod.write(PROD_YML)
            prod.flush()
            result = compare_workflows(dev.name, prod.name)
            self.assertEqual(result['differences'], [])
            os.unlink(dev.name)
            os.unlink(prod.name)

    def test_invalid_prod(self):
        with tempfile.NamedTemporaryFile('w+', delete=False) as dev, tempfile.NamedTemporaryFile('w+', delete=False) as prod:
            dev.write(DEV_YML)
            dev.flush()
            prod.write(PROD_YML_INVALID)
            prod.flush()
            result = compare_workflows(dev.name, prod.name)
            self.assertIn("Job 'lint' should not exist in production workflow.", result['differences'])
            os.unlink(dev.name)
            os.unlink(prod.name)

if __name__ == '__main__':
    unittest.main()