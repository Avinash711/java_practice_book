import json
from models import NewTestConfig
data = { "new_reports":[{
                "report_name":"SAP",
                "frequency":"monthly",
                "start_time":"2022-01-16",
                "is_rerun":True,
                "version":"3.0.0",
                "is_bq_ce":True,
                "is_config_exists": True,
                "api_polling_stats":{
                    "default":False,
                    "initial_delay":50,
                    "max_timeout":60,
                    "api_polling_delay":20
                }
            }
        ]
    }

#print(data)

for report in data["new_reports"]:
    result = NewTestConfig(**report)
    print(json.dumps(result.dict(), indent=4))