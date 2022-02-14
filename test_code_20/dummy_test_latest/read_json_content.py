import json


class ReadJson:
    def ret_report(self):
        file_name = "./files/new_test.json"
        json_reports = {}
        with open(file_name) as data:
            json_reports = json.load(data)
        return json_reports['new_reports']

print(ReadJson().ret_report())
