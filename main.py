
import os
from tkinter import *
from tkinter import messagebox as msg
import func_setting as set
import func_event as eve
import shutil


# 라벨명 초기화
labelname_version = "버젼"
labelname_path = "폴더 경로"
labelname_createpath = "생성폴더\n경로"
labelname_foldername = "폴더명"
labelname_code = "코드"
labelname_initial ="이니셜"
labelname_startpath = "실행파일\n경로"
labelname_id = "ID"
labelname_pw = "PW"

# placeholder 초기화
ph_version = "3.3"
ph_path = set.getFrameworkPath()
ph_foldername = " 예) RPA_OFFICE"
ph_code = " 예) cxxxxxxx"



root = Tk()
root.title("[PROJECT] RPA프로젝트 세팅")
root.geometry("+1000+450")
root.resizable("False", "False")
root.config(bg='cornsilk')


# REFramework 폴더 위치 FRAME
framework_frame = set.create_frame(root, "REFramework", (20,3))

    # 프레임워크 버젼   
framework_frame2 = set.create_frame(framework_frame, "", 0)
        #label
framework_version_label = set.create_label(framework_frame2," *{0} ".format(labelname_version))
        #entry
framework_version_entry = set.create_entry(framework_frame2)
framework_version_entry.insert(0, ph_version) 
framework_version_entry.config(state=DISABLED)

    # 프레임워크 경로    
        #frame
framework_frame3 = set.create_frame(framework_frame, "", 0)
        #label
framework_path_label = set.create_label(framework_frame3," *{0}".format(labelname_path))
        #entry
framework_path_entry = set.create_entry(framework_frame3, "x")
framework_path_entry.insert(0, ph_path) # 프레임워크 경로 초기화
framework_path_entry.config(state=DISABLED)            # Entry창 비활성화 -> 찾아보기 버튼을 통해서만 수정할 수 있도록.
        #button
framework_btn = set.create_button(framework_frame3, "찾아보기")


# PROJECT FRAME 
project_frame = set.create_frame(root, "PROJECT", 5)

   # 프로젝트 생성할 폴더경로 (frame, Lable, Entry, button)
project_frame2 = set.create_frame(project_frame, "", 0)
        #label
project_createpath_label = set.create_label(project_frame2," *{0}".format(labelname_createpath))
        #entry
project_createpath_entry = set.create_entry(project_frame2, "x")
        #button
project_createpath_btn = set.create_button(project_frame2, "찾아보기")

   # 폴더명 (frame, Lable, Entry, Entry placeholder 처리)
project_frame3 = set.create_frame(project_frame, "", 0)
        #label
project_foldername_label = set.create_label(project_frame3,"*{0}".format(labelname_foldername))
        #entry
project_foldername_entry = set.create_entry(project_frame3)
        # Entry placeholder 처리
project_foldername_entry.insert(0, ph_foldername)
project_foldername_entry.config(state=DISABLED)

    # 코드 (Lable, Entry, Entry placeholder 처리)
        #label
project_code_label = set.create_label(project_frame3,"*{0}".format(labelname_code))
        #entry
project_code_entry = set.create_entry(project_frame3)
        # Entry placeholder 처리
project_code_entry.insert(0, ph_code)
project_code_entry.config(state=DISABLED)


# ERP FRAME
erp_frame = set.create_frame(root, "ERP", 5)

    # 이니셜 (frame, Label, Entry)
        #frame
erp_frame2 = set.create_frame(erp_frame, "", 0)
        #label
erp_initial_label = set.create_label(erp_frame2," *{0} ".format(labelname_initial))
        #entry
erp_initial_entry = set.create_entry(erp_frame2)

    # 실행경로 (frame, Label, Entry)
        #frame
erp_frame3 = set.create_frame(erp_frame, "", 0)
        #label
erp_startpath_label = set.create_label(erp_frame3," {0}".format(labelname_startpath))
        #entry
erp_startpath_entry = set.create_entry(erp_frame3, "x")
        #button
erp_startpath_btn = set.create_button(erp_frame3, "찾아보기")



# ERP 계정정보 FAME
erp_credential_frame = set.create_frame(root, "ERP 계정정보", 5)

    # ID (Label, Entry)
        #label
erp_id_label = set.create_label(erp_credential_frame," {0} ".format(labelname_id))
        #entry
erp_id_entry = set.create_entry(erp_credential_frame)

    # PW (Label, Entry)
        #label
erp_pw_label = set.create_label(erp_credential_frame," {0} ".format(labelname_pw))
        #entry
erp_pw_entry = set.create_entry(erp_credential_frame)



# 프로젝트 초기화/생성/닫기 Frame
btn_frame = set.create_frame(root, "", 3)
        # 닫기 (Button)
quit_btn = set.create_button(btn_frame, "닫기", (0, 10), 12, 5)
        # 생성하기 (Button)
start_btn = set.create_button(btn_frame, "생성하기", (0, 10), 12, 5)
        # 초기화 (Button)
init_btn = set.create_button(btn_frame, "초기화", (0, 10), 12, 5)



############################################### 이벤트 처리


# 이벤트 처리 함수
        # placeholder 제거 이벤트 처리 함수
def click_version_entry(event):
        eve.cancle_placeholder(framework_version_entry, version_entry_click)
def click_foldername_entry(evnet):
        eve.cancle_placeholder(project_foldername_entry, foldername_entry_click)
        project_foldername_entry.insert(0, "HYPER_")
def click_code_entry(evnet):
        eve.cancle_placeholder(project_code_entry, code_entry_click)

def event_placehorder():
        global version_entry_click
        global foldername_entry_click
        global code_entry_click
        version_entry_click = framework_version_entry.bind("<Button-1>", click_version_entry)
        foldername_entry_click = project_foldername_entry.bind("<Button-1>", click_foldername_entry)
        code_entry_click = project_code_entry.bind("<Button-1>", click_code_entry)

        # 버튼 이벤트 
def find_framework_dir():
        eve.find_dir(framework_path_entry, "프레임워크 경로 지정")
def find_createpath_dir():
        eve.find_dir(project_createpath_entry, "프로젝트 경로 지정")        
def find_erp_startpath():
        eve.find_erp_startpath(erp_startpath_entry, "ERP 실행경로 지정")

        # 초기화
def init_inputdata():
        # 일반 초기화(데이터만 지우기) entry
        arrEntry = [project_createpath_entry, erp_initial_entry, erp_startpath_entry, erp_id_entry, erp_pw_entry]
        # 초기화 시, placeholder처리까지 해줘야하는 entry
        arrEntry_ph = [(ph_version, framework_version_entry)
                , (ph_path, framework_path_entry)
                , (ph_foldername, project_foldername_entry)
                , (ph_code, project_code_entry)]

        for entry in arrEntry: 
                entry.delete(0, END)

        for entry_info in arrEntry_ph: 
                entry_info[1].config(state=NORMAL)
                entry_info[1].delete(0, END)
                entry_info[1].insert(0, entry_info[0])
                entry_info[1].config(state=DISABLED)
        event_placehorder()

def start_create_new():
        # 유효성 검사
        result = eve.check_inputdata(
                (framework_version_label["text"], framework_version_entry.get())
                , (framework_path_label["text"], framework_path_entry.get())
                , ((project_createpath_label["text"]), project_createpath_entry.get())
                , (project_foldername_label["text"], project_foldername_entry.get())
                , (project_code_label["text"], project_code_entry.get())
                , (erp_initial_label["text"], erp_initial_entry.get())
                , (erp_startpath_label["text"], erp_startpath_entry.get())
                , (erp_id_label["text"], erp_id_entry.get())
                , (erp_pw_label["text"], erp_pw_entry.get())
                )
        if result[0] != "성공":
                msg.showwarning(result[0], result[1])
                return
        # 프로젝트 시작
        framework_path = result[1]
        total_result = eve.start_process(framework_path, project_createpath_entry.get()
                                , project_foldername_entry.get(), project_code_entry.get()
                                , erp_initial_entry.get(), erp_startpath_entry.get()
                                , erp_id_entry.get(), erp_pw_entry.get())

        if total_result[0] == True:
                msg.showinfo("완료", "세팅이 완료되었습니다.")
        else:
                project_folder = os.path.join(project_createpath_entry.get(), project_foldername_entry.get())
                if os.path.exists(project_folder) and not "생성 프로젝트 경로가 이미 사용중입니다." in str(total_result[1]):
                        shutil.rmtree(project_folder)
                msg.showerror("실패", total_result[1])


# placeholder 이벤트
event_placehorder()


# 버튼 이벤트
        # REFramework 폴더 경로 '찾아보기' 버튼
framework_btn.config(command=find_framework_dir)
        # 프로젝트 생성폴더 경로 '찾아보기' 버튼
project_createpath_btn.config(command=find_createpath_dir)
        # ERP 실행경로 '찾아보기' 버튼
erp_startpath_btn.config(command=find_erp_startpath)
        # '초기화' 버튼
init_btn.config(command=init_inputdata)
        # '생성하기' 버튼
start_btn.config(command=start_create_new)
        # '닫기' 버튼
quit_btn.config(command=root.quit)



root.mainloop()