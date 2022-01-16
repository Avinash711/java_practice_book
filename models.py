from pydantic import BaseModel, validator, root_validator
from typing import Optional, List, Dict, Union

class ApiPolling(BaseModel):
    default:bool
    initial_delay: Optional[int]="default"
    max_timeout:Optional[int]="default"
    api_polling_delay:Optional[int]="default"
    # initial_delay or max_timeout or api_polling_delay is set to default,
    # to distinguish respective values populated by end user or not 

    @root_validator
    def validate_default(cls,values):
        print("*"*30)
        print(values)
        print("*"*30)
        print(values.keys())
        keys = values.keys()
        # default =True
        if 'default' in keys and values['default']:
            if ('initial_delay' in keys and values['initial_delay'] != 'default') or \
                ("max_timeout" in keys and values['max_timeout'] != 'default') or \
                ("api_polling_delay" in keys and values['api_polling_delay'] != 'default'):
                raise ValueError("Since Default is True, initial_delay or max_timeout or api_polling_delay cant be populated!!")
            else:
                values['initial_delay'] = 5
                values['max_timeout'] = 6
                values["api_polling_delay"] = 2
                
        else: # when default is false, validate minimum values
            required_min_str = """
                                Hint: Minimum required values for:
                                       initial_delay is 5 mins,
                                       max_timeout is 6 mins,
                                       api_polling_delay is 2 mins
                                """
            # initial_delay validation for default=False
            if "initial_delay" in keys and values['initial_delay'] !='default':
                if values['initial_delay'] < 5:
                    raise ValueError(f"!!!Initial Delay cant be less than required min value i.e. 5 mins {required_min_str}")
            else:
                raise ValueError("Initial_delay is Required as default is false!!")

            #  max_timeout validation for default=False
            if "max_timeout" in keys and values['max_timeout'] !='default':
                if values['max_timeout'] < 5:
                    raise ValueError(f"!!!max timeout cant be less than required min value i.e. 6 mins {required_min_str}")
            else:
                raise ValueError("max_timeout is Required as default is false!!")
            
            #  api_polling_delay validation for default=False
            if "api_polling_delay" in keys and values['api_polling_delay'] !='default':
                if values['max_timeout'] < 5:
                    raise ValueError(f"!!!api_polling_delay cant be less than required min value i.e. 2 mins {required_min_str}")
            else:
                raise ValueError("api_polling_delay is Required as default is false!!")
                
        return values
    '''
    @validator('initial_delay')
    def validate_initial(cls, val):
        return val

    @validator('max_timeout')
    def validate_max(cls, val):
        return val

    @validator('api_polling_delay')
    def validate_polling(cls, val):
        return val
        '''

class NewTestConfig(BaseModel):
    report_name: str
    frequency: str
    start_time: str
    is_config_exists=True
    is_bq_to_ce=True
    is_rerun=False
    version:str
    api_polling_stats: ApiPolling
