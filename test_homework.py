import allure
import pytest
import yaml
from pytestdemo.calculator import Calculator

"""
生成allure-report命令：
cmd:cd .py文件路径下
pytest --clean --alluredir=./result/2/ test_homework.py
allure generate ./result/2/ -o ./report/2/
allure open -h 127.0.0.1 -p 8090 ./report/2/
"""

def get_datas():
    with open('./datas/calc2.yml','r',encoding='utf-8') as f:
        datas=yaml.safe_load(f)
    print(datas)
    return datas

@allure.feature("测试计算器")
class TestCal:

    @pytest.mark.parametrize('a,b,expect',get_datas()['add_datas']['datas'])
    @allure.story("测试加法功能")
    def test_add(self,calculator,a,b,expect):
        if isinstance(a,str)|isinstance(b,str)|isinstance(expect,str):
            print("不能为str类型字符串")
            assert False
        else:
            with allure.step("判断结果是否为浮点数"):
                result=calculator.add(a,b)
                if isinstance(result, float):
                    result=round(result,2)
                with allure.step("断言加法结果是否正确"):
                    assert  expect==result


    @pytest.mark.parametrize('a,b,expect', get_datas()['sub_datas']['datas'])
    @allure.story("测试减法功能")
    def test_sub(self, calculator, a, b, expect):
        if isinstance(a,str)|isinstance(b,str)|isinstance(expect,str):
            print("不能为str类型字符串")
            assert False
        else:
            with allure.step("判断结果是否为浮点数"):
                result = calculator.sub(a, b)
                if isinstance(result, float):
                    result = round(result, 2)
                with allure.step("断言加法结果是否正确"):
                    assert expect == result

    @pytest.mark.parametrize('a,b,expect', get_datas()['mul_datas']['datas'])
    @allure.story("测试乘法功能")
    def test_mul(self, calculator, a, b, expect):
        if isinstance(a, str) | isinstance(b, str) | isinstance(expect, str):
            print("不能为str类型字符串")
            assert False
        else:
            with allure.step("判断结果是否为浮点数"):
                result = calculator.mul(a, b)
                if isinstance(result, float):
                    result = round(result, 2)
                with allure.step("断言加法结果是否正确"):
                    assert expect == result

    @pytest.mark.parametrize('a,b,expect', get_datas()['div_datas']['datas'])
    @allure.story("测试相除功能")
    def test_div(self,calculator,a,b,expect):
        try:
            if isinstance(a, str) | isinstance(b, str) | isinstance(expect, str):
                print("不能为str类型字符串")
                assert False
            else:
                with allure.step("判断结果是否为浮点数"):
                    result=calculator.div(a,b)
                    if isinstance(result,float):
                        result=round(result,2)
                    with allure.step("断言除法结果是否正确"):
                        assert expect==result
        except ZeroDivisionError:
            print("除数为0")
            pass


