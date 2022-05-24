import os
import shutil
import json
from openpyxl import load_workbook
import exception as e
from exception import TotalProcessError as pr

project_name = "HYPER_TEST"
project_path = "C:\Temp\HYPER_test"
project_code = "ctesttest"
erp_initial = "TEST"
erp_startpath = "c:\test"


sample = "[ERP(sample)]"
masterlist_filename = "cxxxxxxx_MasterList"
test_erp_path = os.path.join(project_path, "Test/{0}".format(erp_initial))

def join_path(path1, path2, path_type)  :

    joined_path = os.path.join(path1, path2)
    print(joined_path)
    if path_type == "dir":
        if not os.path.isdir(joined_path): 
            raise e.NotExistPath(joined_path)
    elif path_type == "file":
        if not os.path.isdir(join_path): 
            raise e.NotExistPath(joined_path)

    return joined_path


try:
    project_path = join_path("C:\Temp\HYPER_test","zzz", "dir") # 생성할 프로젝트 경로


except FileExistsError as err:
    print(pr(err).title, pr(err).msg)
except FileNotFoundError as err:
    print(pr(err).title, pr(err).msg)
except e.NotExistPath as err:
    print(err.title, err.msg)
except Exception as err:
    print(pr(err).title, pr(err).msg)


