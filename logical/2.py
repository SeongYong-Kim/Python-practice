id = input("아이디를 입력해라\n")
pwd = input("비밀번호를 입력해라\n")
real_id = "성용이"
real_pwd = "2019"
if real_id == id:
    if real_pwd == pwd:
        print("어서오세요")
    else:
        print("누구?")
else:
    print("누구??")
