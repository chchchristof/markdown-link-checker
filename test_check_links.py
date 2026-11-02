import tempfile
import unittest
from pathlib import Path
from check_links import check


class LinkCheckerTests(unittest.TestCase):
    def test_finds_missing_links_and_accepts_existing_relative_links(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'hello world.md').write_text('# Hello\n', encoding='utf-8')
            (root / 'README.md').write_text(
                '[ok](hello%20world.md#hello)\n[bad](missing.md)\n'
                '[web](https://example.com)\n[anchor](#section)\n', encoding='utf-8')
            issues = check(root)
            self.assertEqual(len(issues), 1)
            self.assertIn('missing.md', issues[0])


if __name__ == '__main__':
    unittest.main()
