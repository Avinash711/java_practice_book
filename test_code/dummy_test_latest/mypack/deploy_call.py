
from looup import ReturnEntry

class ReturnIDStatus:
    def __init__(self, file_name, env, project, report_input):
        self.file_name = file_name
        self.env = env
        self.project = project
        self.report_input = report_input
    
    def return_id_status(self):
        return ReturnEntry(self.report_input).ret_data()