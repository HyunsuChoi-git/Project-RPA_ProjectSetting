import os
from tkinter import *
from tkinter import filedialog
import exception as e
import func_process as pro

# placeholder 해제
def cancle_placeholder(entry, bind):
    entry.configure(state=NORMAL)
    entry.delete(0, END)
    entry.unbind("<Button-1>", bind)

# 디렉토리 찾기 팝업
def find_dir(entry, pop_title):
    dirname = filedialog.askdirectory(initialdir="/", title=pop_title)
    if dirname == "": 
        # 아무 선택도 안했을 경우 그대로 return
        return
    
    if "프레임워크" in pop_title:
        # 입력창 활성화
        entry.config(state=NORMAL)
    # 지정한 경로 입력
    entry.delete(0, END)
    entry.insert(0, dirname)
    if "프레임워크" in pop_title:
        # 입력창 비활성화
        entry.config(state=DISABLED)

# 파일 찾기 팝업
def find_erp_startpath(entry, pop_title):
    startpath = filedialog.askopenfilename(initialdir="/", title=pop_title)

    # 지정한 경로 입력
    entry.delete(0, END)
    entry.insert(0, startpath)


# 유효성 검사
def check_inputdata(version, frameworkpath, createpath, foldername, code, initial, startpath, id, pw):
    try:
        # 필수 입력사항 작성여부 (버전, 폴더명, 코드, erp이니셜)
        for data in [version, frameworkpath, createpath, foldername, code, initial, startpath, id, pw]:
            if "*" not in data[0]:
                continue
            if data[1] == "" or "예)" in data[1]:
                raise e.EmptyEntryError(data[0].replace("\n"," ").strip())

        # 버전 유효성 검사 
        float(version[1].strip())

        # 프레임워크 존재여부
            # 폴더 하위 디렉토리 추출
        list_dir = [ f.path for f in os.scandir(frameworkpath[1]) if f.is_dir()]
        if len(list_dir) == 0:
            raise e.NotFoundFramework()
            # 하위 디렉토리에서 프레임워크 폴더 추출
        framework_folder = ""
        for folder in list_dir:
            if version[1] in folder.replace(os.path.dirname(folder), ""):
                framework_folder = folder
        if framework_folder == "":
            raise e.NotFoundFramework()
        
        # 프로젝트 생성 폴더 존재여부
        if not os.path.isdir(createpath[1]):
            raise e.NotFoundFolder()

        # erp 실행경로 존재여부
        is_startfile = os.path.isfile(startpath[1])
        if startpath[1] != "" and is_startfile == False:
            raise e.NotExistErpStartPath()

        # 계정정보 둘다 입력 or 둘다 입력X 체크
        if id[1] == "" and pw[1] != "":
            raise e.EmptyCredentialInfo(id[0].strip())
        if id[1] != "" and pw[1] == "":
            raise e.EmptyCredentialInfo(pw[0].strip())
    
    except e.EmptyEntryError as err:
        return (err.title, err)
    except ValueError as err:
        return (e.VersionError().title, e.VersionError().msg)
    except e.NotFoundFramework as err:
        return (err.title, err)
    except e.NotFoundFolder as err:
        return (err.title, err)
    except e.NotExistErpStartPath as err:
        return (err.title, err)
    except e.EmptyCredentialInfo as err:
        return (err.title, err)
    except Exception as err:
        print(err)
        return ("오류", "알 수 없는 오류가 발생하였습니다.")



    return ("성공", framework_folder)



# 프로젝트 생성하기
def start_process(framework_path, project_createpath, project_foldername, 
        project_code, erp_initial, erp_startpath, erp_id, erp_pw):
    return pro.start_process(framework_path, project_createpath, project_foldername, 
        project_code, erp_initial, erp_startpath, erp_id, erp_pw)