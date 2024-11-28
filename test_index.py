import unittest

class TestIndexPage(unittest.TestCase):
    def test_title(self):
        with open("index.html", "r") as f:
            content = f.read()
            self.assertIn("<title>Hola Mundo</title>", content)

    def test_header(self):
        with open("index.html", "r") as f:
            content = f.read()
            self.assertIn("<h1>Hola Mundo</h1>", content)

if __name__ == "__main__":
    unittest.main()
