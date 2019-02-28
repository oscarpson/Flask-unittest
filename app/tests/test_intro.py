import unittest
from .base_test import BaseTest


class IntroTest(BaseTest):
    def test_intro_route(self):
        resp = self.client().get("/api/v1/intro", content_type="application/json")
        self.assertEqual(resp.status_code, 200)


if __name__ == "__main__":
    unittest.main()
