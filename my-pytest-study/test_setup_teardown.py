import pytest
#，模块中的方法
def setup_module():
    print("\n setup_module:整个模块开始前执行一次")
def teardown_module():
    print("\n teardown_module:整个模块结束后执行一次")
def setup_function():
    print("\n setup_function:每个不在类中的函数开始前执行")
def teardown_function():
    print("\n teardown_function:每个不在类中的函数结束后执行")

#测试用例
def test_one():
    print("正在执行测试模块-----test_one")
def test_two():
    print("正在执行测试模块-----test_two")
class TestCase():
    def setup_class(self):
        print("\n setup_class:在类开始前执行")
    def teardown_class(self):
        print("\n teardown_class:在类结束后执行")
    def setup_method(self):
        print("\n setup_method:每个方法开始前执行")
    def teardown_method(self):
        print("\n teardown_method:每个方法结束后执行")
    def setup(self):
        print("\n setup:每个用例开始前都会执行")
    def teardown(self):
        print("\n teardown:每个用例结束后都会执行")
    def test_tree(self):
        print("\n 正在执行测试类-----test_three")
    def test_four(self):
            print("\n 正在执行测试类-----test_four")