import unittest
from BeautifulReport import BeautifulReport
import os

DIR = os.path.dirname(os.path.abspath(__file__))  # 根据当前目录获取路径信息，保持不变

# 环境切换，线上
Environ = 'Online'


# Environ = 'Offline'


def run(test_suit):
    # 定义输出的文件位置和名字
    filename = 'report.html'  # 报告名称
    result = BeautifulReport(test_suit)
    result.report(filename=filename, description='测试报告', report_dir=DIR)  # 形参：文件名，标题名，dir是存储路径


if __name__ == '__main__':
    suite = unittest.TestLoader().discover("./testCase", "test*.py")
    run(suite)
