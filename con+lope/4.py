input_id=input("입력해주세요.\n")
members=['egoing', 'k8805']
for member in members:
    if member == input_id:
        print('Hello!, '+member)
        import sys
        sys.exit()
print('Who are you?')
