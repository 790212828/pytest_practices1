from typing import List

import pytest
import yaml

from pytestdemo.calculator import Calculator


@pytest.fixture()
def calculator():
    print("开始计算")
    cal=Calculator()
    yield cal
    print("结束计算")

def pytest_collection_modifyitems(session,config,items:List):
    for item in items:
        item.name=item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid=item._nodeid.encode('utf-8').decode('unicode-escape')




