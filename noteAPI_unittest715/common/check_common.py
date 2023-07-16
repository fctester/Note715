import unittest


class CheckCommon(unittest.TestCase):
    def check_response(self, check_items, response):    # 校验返回体的长度和value值类型的通用方法
        for key, value in check_items.items():
            self.assertIn(key, response.keys())  # 校验期望的返回体和实际的返回体是否一致
            self.assertEqual(type(value), type(response[key]))  # 校验返回体值的内容
