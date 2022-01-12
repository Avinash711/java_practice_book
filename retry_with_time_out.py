from time import sleep, time


# try splitting into 3 if bigger
def default_plus_validation(initial_depl_status_delay, max_time_out, api_polling_delay):
    
    '''if initial_depl_status_delay, max_time_out and api_polling_delay not populated
    take best default values'''
    '''
    best default_initial_depl_status would be == default_max_time_out
    ** benfit of keeping it same is, best case we can get the depl status in one call itself
    '''
    # default values in minutes
    default_initial_depl_status_delay = 3 # or same as max time out i.e. 5
    default_max_time_out = 6 # or 5, for 5 it will try 3 times
    default_api_polling_delay = 3


    ##----------initial_depl_status_delay--------##
    # assigning default values if keys not present
    if not initial_depl_status_delay: # not populated
        initial_depl_status_delay = default_initial_depl_status_delay # assigned default value
    else: #populated
        if initial_depl_status_delay < default_initial_depl_status_delay:
            print(f"initial_depl_status_delay i.e. {initial_depl_status_delay} is less than minimum value \
                   so changed to minimum default value i.e. {default_initial_depl_status_delay}")
            initial_depl_status_delay = default_initial_depl_status_delay
    print(f"=====> initial_depl_status_delay is {initial_depl_status_delay} mins")

    ##----------max_time_out--------##
    # assigning default values if keys not present
    if not max_time_out: # not populated
        max_time_out = default_max_time_out # assigned default value
    else: #populated
        if max_time_out < default_max_time_out:
            print(f"max_time_out i.e. {max_time_out} is less than minimum value \
                   so changed to minimum default value i.e. {default_max_time_out}")
            max_time_out = default_max_time_out
    print(f"=====> max_time_out is {max_time_out} mins")

    ##----------api_polling_delay--------##
    # assigning default values if keys not present
    if not api_polling_delay: # not populated
        api_polling_delay = default_api_polling_delay # assigned default value
    else: #populated
        if api_polling_delay < default_api_polling_delay:
            print(f"api_polling_delay i.e. {api_polling_delay} is less than minimum value \
                   so changed to minimum default value i.e. {default_api_polling_delay}")
            api_polling_delay = default_api_polling_delay
    print(f"=====> api_polling_delay is {api_polling_delay} mins")

    return [initial_depl_status_delay, max_time_out, api_polling_delay]
    
        
def api_call():
    return "RUNNING"

def api_polling(l_initial_depl_status_delay, l_max_time_out, l_api_polling_delay):
    # validation plus defualt assignment
    initial_depl_status_delay, max_time_out, api_polling_delay= default_plus_validation(l_initial_depl_status_delay,\
                                                                l_max_time_out, l_api_polling_delay)

    # initial wait
    print(f"initially waiting for {initial_depl_status_delay} mins...")
    sleep(initial_depl_status_delay*60)


    # start polling api
    # multiplied by 2 to avoid coming out of retry loop within timeout limit
    retry_count = (max_time_out // api_polling_delay)*2 
    print(f"max rety count is {retry_count}")
    count = 0
    status = None
    start_time = time()
    while retry_count*2:
        count += 1
        status = api_call()
        time_diff = time() - start_time
        print(f"time taken to poll api status {time_diff} with status  {status} and retry as {count}")
        print(f"trying after {(api_polling_delay*60)*count}")
        # break even point
        if  (status and (status == "RUNNING" and status == "INPROGRSS")) or time_diff >max_time_out*60:
            print(f"Reached break even as status is {status} or timeout is {time_diff}")
            break

        retry_count -=1
        sleep((api_polling_delay*60)*count)
    return status




if __name__ == '__main__':
    # take input in mins
    # calculate seconds internally
    initial_depl_status_delay = None #optional
    max_time_out = None #optional
    api_polling_delay = None #optional
    print(f"started getting status")
    status = api_polling(initial_depl_status_delay, max_time_out, api_polling_delay)
    print(f"final status is {status}")


