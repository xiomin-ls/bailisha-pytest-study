import pytest
#执行任何用例前都会调用
#@pytest.fixture(autouse="ture")

#作用域,scope参数：function（默认），class，module，session（多个文件）
#@pytest.fixture(scope="class")

#参数：多次调用，每次执行相关测试
# @pytest.fixture(params=["参数1","参数2"])
# def myfixture(request):
#     print("执行myfixture,带参数%s"%request.param)

@pytest.fixture()
def myfixture():
    print("执行myfixture")