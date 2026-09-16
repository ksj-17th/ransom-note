import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk

def on_closing():
    # Alt+F4나 X 버튼을 눌러도 꺼지지 않게 방지
    messagebox.showwarning("WARNING", "ACCESS DENIED.\n이 창은 순순히 닫히지 않습니다.")
    return

def check_password(event=None):
    # 이스터에그: 탈출용 비밀번호 확인 함수
    if entry.get() == "1234": # 비밀번호를 1234로 지정
        root.destroy()
    else:
        messagebox.showerror("ERROR", "INCORRECT PASSWORD.")
        entry.delete(0, tk.END)

# 1. 메인 창 생성 및 윈도우 스타일(CMD 느낌) 설정
root = tk.Tk()
root.title("SYSTEM LCKED")
root.configure(bg="black")  # 배경을 검은색으로!

# 창의 가로, 세로 크기 정의
window_width = 700
window_height = 500

# 모니터 화면의 실제 가로, 세로 해상도 가져오기
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 정중앙에 위치시키기 위한 x, y 좌표 계산
center_x = int((screen_width - window_width) / 2)
center_y = int((screen_height - window_height) / 2)

# geometry 규칙에 맞게 "가로x세로+x좌표+y좌표" 형태로 설정
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")


# 2. 핵심 로직: 화면 맨 위 고정 & 테두리(종료버튼) 없애기
root.attributes("-topmost", True)
root.overrideredirect(True) # 타이틀바, X버튼, 테두리를 완전히 제거하여 끄기 불가능하게 만듦

# 3. 강제 종료 신호 가로채기
root.protocol("WM_DELETE_WINDOW", on_closing)

# 4. 레이아웃 구역 나누기 (좌측: 그림 / 우측: 텍스트 및 입력창)
left_frame = tk.Frame(root, bg="black")
left_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)

right_frame = tk.Frame(root, bg="black")
right_frame.pack(side="right", padx=20, pady=20, fill="both", expand=True)

# 5. 좌측: 픽셀화된 그림 표시 (joker.gif 파일이 같은 폴더에 있어야 합니다)
try:
    # 바탕화면 절대 경로와 파일 이름을 정확히 매칭 (보내주신 이미지 파일명 기준)
    original_img = Image.open("C:/Users/kisec/Desktop/joker.png")
    resized_img = original_img.resize((250, 250)) 
    
    img = ImageTk.PhotoImage(resized_img)
    img_label = tk.Label(left_frame, image=img, bg="black")
    img_label.pack(expand=True)
except Exception as e:
    # 어떤 문제인지 확인하기 위해 터미널에 에러 메시지를 출력
    print(f"에러 내용: {e}")
    img_label = tk.Label(left_frame, text="[ IMAGE\nNOT\nFOUND ]", fg="red", bg="black", font=("Courier New", 24, "bold"))
    img_label.pack(expand=True)


# 6. 우측: CMD 감성의 초록색/빨간색 픽셀 폰트 텍스트
title_label = tk.Label(right_frame, text="?? SYSTEM WARNING ??", fg="red", bg="black", font=("Courier New", 18, "bold"))
title_label.pack(pady=10)

# 전체 출력할 문구 정의
joke_text = (
    "반갑너굴~\n\n"
    "당신의 컴퓨터는 이 너굴맨이 처리했다구!\n\n"
    "뭐..? 이건 처리하면 안 되는 거였다고?\n\n"
    "쳇... \n\n"
    "500만원만 주면 되찾아 주지."
)

# 처음에 텅 빈 상태로 텍스트 레이블 생성
content_label = tk.Label(right_frame, text="", fg="#00FF00", bg="black", font=("Courier New", 12), justify="left")
content_label.pack(pady=20)

# 한 글자씩 출력하는 핵심 함수
def type_text(index=0):
    if index < len(joke_text):
        # 현재 인덱스까지의 글자를 레이블에 업데이트
        content_label.config(text=joke_text[:index+1])
        # 50밀리초(0.05초) 뒤에 다음 글자를 출력하도록 예약 (속도 조절 가능)
        root.after(100, type_text, index + 1)

# 창이 완전히 뜨고 나서 타이핑 효과 시작
root.after(500, type_text)

# 7. 우측 하단: 탈출용 비밀번호 입력창
entry_label = tk.Label(right_frame, text="ENTER DECRYPT KEY:", fg="white", bg="black", font=("Courier New", 10))
entry_label.pack(pady=5)

entry = tk.Entry(right_frame, show="*", bg="#111111", fg="#00FF00", insertbackground="#00FF00", font=("Courier New", 12))
entry.pack(pady=5)
entry.bind("<Return>", check_password) # 엔터키를 누르면 비밀번호 확인

btn = tk.Button(right_frame, text="DECRYPT", command=check_password, bg="#222222", fg="#00FF00", font=("Courier New", 10, "bold"), activebackground="#00FF00")
btn.pack(pady=10)

# 8. 프로그램 실행
root.mainloop()
