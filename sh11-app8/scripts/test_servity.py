import pytest


class TestSer:

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)  # 阻断性
    def test_001(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)  # 关键性
    def test_002(self):
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)  # 一般性
    def test_003(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)  # 较小的
    def test_004(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)  # 可以忽略
    def test_005(self):
        assert True
