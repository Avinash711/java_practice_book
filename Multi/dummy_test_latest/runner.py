
import subprocess
import concurrent.futures
def test_execute_func(uid):
    subprocess.run(f"python -m pytest test_report_1.py --env env --project project --uid {uid} -s -vv --junitxml=result_{uid}.xml")

if __name__=='__main__':
    #Gather all the testsuite names
    reports = ["SAP", "SAP1", "SAP2"]
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [ executor.submit(test_execute_func, repo) for repo in reports]

        for f in concurrent.futures.as_completed(results):
            print(f.result)