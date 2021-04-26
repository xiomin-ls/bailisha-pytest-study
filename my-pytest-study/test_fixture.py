import pytest
#fixture类似setup和teardown，
# 但是可以使我们自定义测试用例的前置条件
#可以跨文件使用
# fixture也可以写在conftest.py文件里

# @pytest.fixture()
# def myfixture():
#     print("执行myfixture")

class Test_firstFile():
    def test_one(self):
        print("执行test")
        assert 2 + 3 == 5
    def test_two(self):
        print("执行test_two")
        assert 2 + 3 == 5
    def test_three(self,myfixture):
        print("执行test_three")
        assert 2 + 3 == 5

