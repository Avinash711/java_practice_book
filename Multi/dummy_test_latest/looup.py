
import json

class ReturnEntry:
    def __init__(self, report_name):
        self.report_name = report_name
    
    def ret_data(self):

        with open('files/new_test.json') as json_file:
            json_data = json.load(json_file)
            #print(json_data)
            print('\ninput report_name is: ', self.report_name)
            report_spec = list(filter(lambda iter_report: (iter_report['report_name'] == self.report_name), 
                                    json_data['new_reports']))[0]
            #print('\n')
            #print('in retData-->'*10)
            #print(report_spec)
        return report_spec

#print(ReturnEntry('SAP').ret_data())