from flask import url_for
from tests.base import BaseTestCase


class MainTestCase(BaseTestCase):
    def test_index(self):
        response = self.client.get(url_for('main.index'))
        data = response.get_data(as_text=True)
        self.assertIn('登录', data)

        self.login()
        response = self.client.get(url_for('main.index'))
        data = response.get_data(as_text=True)
        self.assertNotIn('登录', data)
