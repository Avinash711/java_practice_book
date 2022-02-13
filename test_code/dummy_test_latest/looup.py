
import json

class ReturnEntry:
    def __init__(self, report_dict):
        self.report_dict = report_dict
    
    def ret_data(self):

        with open('files/new_test.json') as json_file:
            json_data = json.load(json_file)
            #print(json_data)
            report_in = self.report_dict['report_name']
            ver_in = self.report_dict['version']
            print('\ninput report_name is: ', report_in)
            print('\ninput version is: ', ver_in)
            report_spec = list(filter(lambda iter_report: (iter_report['report_name'] == report_in and\
                                                    iter_report['version'] == ver_in), json_data['new_reports']))[0]
            #print('\n')
            #print('in retData-->'*10)
            #print(report_spec)
        return report_spec

