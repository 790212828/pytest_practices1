import allure
import pytest
import yaml


from pytestdemo.calculator import Calculator
"""
@pytest.fixture()
def calculator():
    print("开始计算")
    cal=Calculator()
    yield cal
    print("结束计算")
"""

def get_datas():
    with open('./datas/calc.yml') as f:
        datas=yaml.safe_load(f)
    return datas

def test_datas():
    with open('./datas/calc.yml') as f:
        datas=yaml.safe_load(f)
    print(datas)

@allure.feature("测试计算器")
class TestCal:
    """
    def setup_class(self):
        self.cal = Calculator()
        print("class setup")
        print("开始计算")
    def teardown_class(self):
        print("结束计算")
    """
    # @pytest.mark.parametrize('a,b,expect',[
    #     [1,1,2],[100,100,200]
    # ])
    @pytest.mark.parametrize('a,b,expect',get_datas()['add_int']['datas'])
    @allure.story("测试相加功能_int")
    def test_add_int(self,calculator,a,b,expect):
        # cal=Calculator()
        # assert expect==cal.add(a,b)
        with allure.step("断言相加的结果"):
            assert expect==calculator.add(a,b)


    # @pytest.mark.parametrize('a,b,expect', [
    #     [1.0, 1.5, 2.5], [100.1, 100, 200.1], [0.1, 0.2, 0.3]
    # ],ids=['float1','float2','float3'])
    @pytest.mark.parametrize('a,b,expect',get_datas()['add_float']['datas'],ids=get_datas()['add_float']['ids'])
    @allure.story("测试相加功能_float")
    def test_add_floot(self,calculator,a,b,expect):
        # cal=Calculator()
        # assert expect == round(cal.add(a, b), 2)
        assert  expect==round(calculator.add(a,b),2)

    @allure.story("测试相除功能")
    def test_div(self,calculator):
        # cal=Calculator()
        # assert 2 == round(cal.div(4,2))
        # try:
        #     # raise ValueError
        #     self.cal.div(1,0)
        # except ZeroDivisionError:
        #     print('除数为0')
        with pytest.raises(ZeroDivisionError):
            # cal.div(1,0)
            calculator.div(1,0)



