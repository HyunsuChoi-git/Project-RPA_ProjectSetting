import os
from tkinter import E


class EmptyEntryError(Exception):
    def __init__(self, name):
        self.msg = "[{0}] 은(는) 필수 입력사항입니다.".format(name)
        self.title = "입력 오류"
    
    def __str__(self):
        return self.msg


class VersionError(Exception):
    def __init__(self):
        self.msg = "버전이 잘못 입력되었습니다. (입력 예: 3.3)"
        self.title = "입력 오류"
    
    def __str__(self):
        return self.msg

class NotFoundFramework(Exception):
    def __init__(self):
        self.msg = "지정 디렉토리 내부에 REFramework 프로젝트 폴더가 존재하지 않습니다. 버전과 경로를 확인하세요."
        self.title = "경로 오류"

    def __str__(self):
        return self.msg    

class NotFoundFolder(Exception):
    def __init__(self):
        self.msg = "프로젝스 생성폴더 경로를 찾을 수 없습니다."
        self.title = "경로 오류"
    
    def __str__(self):
        return self.msg  

class NotExistErpStartPath(Exception):
    def __init__(self):
        self.msg = "ERP 실행파일 경로를 찾을 수 없습니다."
        self.title = "경로 오류"
    
    def __str__(self):
        return self.msg   

class EmptyCredentialInfo(Exception):
    def __init__(self, target):
        self.msg = "[{0}]을(를) 입력하세요.".format(target)
        self.title = "입력오류"
    
    def __str__(self):
        return self.msg   

class NotExistPath(Exception):
    def __init__(self, path):
        self.msg = "프로젝트 내부에 [{0}] 경로가 존재하지 않습니다.".format(path)
    
    def __str__(self):
        return self.msg 

class UsingCreateFolder(Exception):
    def __init__(self, path):
        self.msg = "생성 프로젝트 경로가 이미 사용중입니다. [{0}]".format(path)
    
    def __str__(self):
        return self.msg 

class TotalProcessError(Exception):
    def __init__(self, err):
        self.msg = err
        self.title = "실패"
    
    def __str__(self):
        return self.msg 