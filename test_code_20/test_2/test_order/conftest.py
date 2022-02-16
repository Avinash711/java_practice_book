

import pytest
def pytest_collection_modifyitems(config, items):
    print('*'*10)
    print('\nitems--->')
    print(items)
    # print('\nconfig--->')
    # print(config)
    
    # print(type(items))
    def param_part(item):
        # print('\nitem  is--------->')
        # print(item)
        # print('\nitem  node is--------->')
        # print(item.nodeid)

        # check for the wanted module and test class
        if item.nodeid.startswith("test_urls.py::TestSSL::"):

            # find the start of the parameter part in the nodeid
            index = item.nodeid.find('[')
            print("\nindex is ------------->", index)
            if index > 0:
                print("\n item name is ------------>", item.name)
                # sort by parameter name
                print(item.nodeid[item.nodeid.index('['):])
                return item.nodeid[item.nodeid.index('['):]

        # for all other cases, sort by node id as usual
        return item.nodeid
    
    # re-order the items using the param_part function as key
    items[:] = sorted(items, key=param_part)
    print('final sorted items------------------------>')
    print(items)

