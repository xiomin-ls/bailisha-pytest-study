import pytest
#ctrl+/ 注释，取消注释

def add_function(a,b):
    return a+b

# def test_add1():
#     assert  add_function(1,1) == 2
# def test_add2():
#     assert add_function(-1, 1) == 0
# def test_add3():
#     assert add_function(-1, -1) == -2
# def test_add4():
#     assert add_function(100000, 100000) == 200000
#测试用例前加
#@pytest.mark.parametrize("参数名" , 列表数据,参数别名（非必须）-ids)
@pytest.mark.parametrize("a,b,expected",
                         [(3,5,8),
                          (-1,-2,-3),
                          (100000,100000,200000)
                          ],ids = ["int","minus","bigint"]
                         )
def test_add(a,b,expected):
    assert  add_function(a,b) == expected
#多个参数的所有组合
@pytest.mark.parametrize("a",[0,1,20])
@pytest.mark.parametrize("b",[-2,3,0.5])
def test_foo(a,b):
    print("测试数据组合：a->%s,b->%s"%(a,b))