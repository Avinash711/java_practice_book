import pytest
from time import sleep



json_data = [
        {
            "report_name": "SAP_01",
            "frequency": "monthly",
            "start_time": "2022-01-16",
            "is_rerun": True,
            "version": "3.0.0",
            "is_bq_ce": True,
            "is_config_exists": True,
            "api_polling_stats": {
                "initial_delay": 50,
                "max_timeout": 60,
                "api_polling_delay": 20
            }
        },
        {
            "report_name": "SAP_02",
            "frequency": "monthly",
            "start_time": "2022-01-16",
            "is_rerun": True,
            "version": "3.0.0",
            "is_bq_ce": True,
            "is_config_exists": True,
            "api_polling_stats": {
                "initial_delay": 50,
                "max_timeout": 60,
                "api_polling_delay": 20
            }
        }
    ]


def formatter(report: dict):
    return [val['report_name']+"_"+val['version'] for val in json_data]

@pytest.mark.parametrize("url1",json_data, indirect=False, ids=formatter(json_data))
class TestSSL:
    def test_status(self, url1):
        sleep(2)
        print('slept for 2 sec')
        print(url1)
        assert True
        #assert url1 == f"{url1}"


    def test_gcs(self, url1):
        sleep(3)
        print('slept for 3 sec')
        print(url1)
        #assert url1 == f"{url1}"
        assert True
    
    def test_bq(self, url1):
        sleep(3)
        print('slept for 3 sec')
        print(url1)
        #assert url1 == f"{url1}"
        assert True
    def test_adls(self, url1):
        sleep(3)
        print('slept for 3 sec')
        print(url1)
        #assert url1 == f"{url1}"
        assert True