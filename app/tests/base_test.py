import unittest

from app.api.app import create_app


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

    def tearDown(self):
        self.app.testing = False
