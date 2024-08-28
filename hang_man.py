word=input("word: ")
gess=[]
lets_gess=[]
wrong_gess=[]
t=int(len(word)-1)
# lets_gess=[]
while True:
    print (f"goog luck you have {t} try")
    lets_gess=input("gess: ")
    a=0
    t-=1
    for i in lets_gess:
        if str(i)in str(word):
            a+=1
    if str(lets_gess)!=str(word):
        wrong_gess.append(str(lets_gess))
        print(wrong_gess)
        r=len(word)-int(t+1)
        print(f"hint:the lettar number {int(r)} is {word[r]}")
        print(f"hint:you have {a} word wrigh")
    if a!=len(word)  :
        print(f"the word you try to gess is {len(word) }")
    if str(lets_gess)==str(word) :
        print("you succses ")
        print(f"score={int(len(word)-(len(word)-t))}")
        break;
    if t==0:
        print("you loss")
        print("score= 0")
        break;