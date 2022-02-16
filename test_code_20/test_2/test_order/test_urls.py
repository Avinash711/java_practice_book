import pytest
from time import sleep



json_data = [
        {
            "report_name": "SAP",
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
            "report_name": "SAP_GAAP",
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
            "report_name": "SAP_GAAP",
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
            "report_name": "SAP_GAAP",
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

@pytest.mark.parametrize("report",json_data, indirect=False, ids=str)#ids=formatter(json_data))
class TestSSL:
    def test_status(self, report):
        sleep(2)
        print('slept for 2 sec')
        print(report)
        assert True
        #assert url1 == f"{url1}"


    def test_gcs(self, report):
        sleep(3)
        print('slept for 3 sec')
        print(report)
        #assert url1 == f"{url1}"
        assert True
    
    def test_bq(self, report):
        sleep(3)
        print('slept for 3 sec')
        print(report)
        #assert url1 == f"{url1}"
        assert True
    def test_adls(self, report):
        sleep(3)
        print('slept for 3 sec')
        print(report)
        #assert url1 == f"{url1}"
        assert True