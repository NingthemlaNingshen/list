money_list = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]    
i=0
c=0
l=0
d=0
while i<len(money_list):
    if money_list[i]>10000000:                    ##How many Crorepati?    
        c=c+1                                     ##How many lakhpati?
    elif money_list[i]>100000:                    ##How many dilwale?
        l=l+1
    else:
        d=d+1
    i=i+1
print(c,"is crorepati")
print(l,"is Lakhpati")
print(d,"is Dilwale") 



question_list = ["How many continents are there?",      ##simple kbc
"What is the capital of India?",
"NG mei kaun se course padhaya jaata hai?"]

options_list =[["Four", "Nine", "Seven", "Eight"],
["Chandigarh", "Bhopal", "Chennai", "Delhi"],
["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
Hint_options=[[]]
solution_list = [3, 4, 1]
i=0
while i<len(question_list):
    print("Q",i+1,question_list[i],"choose your answer:")
    j=0
    while j<len(options_list)+1:
        print(j+1,options_list[i][j])
        j=j+1
    ans=int(input("enter your answer:"))
    if ans==solution_list[i]:
        print("you are doing great")
        if ans==1:
            print("Congratulation you have won the game")
    else:
        print("wrong answer Better luck next time")
        break     
    i=i+1
    print()

