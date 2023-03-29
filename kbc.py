questions = [['What is used to make ice-cream at home ?','Blackpaper powder','Custurd powder','coriender powder','Dry mango powder',2],\
        ['Which material is used in steel for hardness ?','Titanium','Aluminium','Carbon','Nickel',3],\
        ["Who invented world's first ever electric bulb ?",'Thomas Edison','Graham Bell','Isaac Newton','Lionardo da Vinci',1]]
levels = [10000,50000,120000]
print("Get set go ***")
for i in range (len(questions)):
    question = questions[i]
    print(f"Question for Rs.{levels[i]}\n{question[0]}")
    print(f"1. {question[1]}     2. {question[2]}")
    print(f"3. {question[3]}     4. {question[4]}")
    reply = int(input("Enter your option (1 - 4) : "))
    if reply == question[-1]:
        print(f"Your answer is correct !! Now you have won Rs.{levels[i]}\n")
        if i == 1:
            money = 10000
        elif i == 2:
            money = 50000
        elif i == 3:
            money = 120000

    else:
        print("You have given wrong answer !!!")
        break
if i == 1:
    print("\nThank you for playing with us...\n_____Grand Congratulations !!!_____\nKya kariyega itni DHANRASHI ka ! ")
