question_list=["How many continents are there ?","What is the capital of India ?",
"NG mei kaun se course padhaya jaata hai ? "]

options_list=[["Four","Nine","Seven","Eight","Hint option"],
["Chandigarh","Bhopal","Chennai","Delhi","Hint option"],
["Software Engineering","Counseling","Tourism","Agriculture","Hint option"]]

Hint_option=[["Eight","seven"],["Bhopal","Delhi"],["SoftwareEngineering","Counseling"]]

Hint_solution=[2,2,1]
solution_list=[3,4,1]

i=0
count=0
while i<len(question_list):
	print("Q.",i+1,question_list[i])
	j=0
	while j<len(options_list[i]):
		print(j+1,options_list[i][j])
		j=j+1
	ans=int(input("enter your answer: "))
	if ans==solution_list[i]:
		print("your ans is correct")
	elif ans==5:
		if count==0:
			k=0
			while k<len(Hint_option[i]):
				print(k+1,Hint_option[i][k])
				k=k+1
			count=count+1
			answer=int(input("enter any no. "))
			if answer==Hint_solution[i]:
				print("you are right")
			else:
				print("wrong answer")
				break
		else:
			print("you already used hint option")
			user=int(input("enter your number:"))
			if user==solution_list[i]:
				print("👍 answer")
			else:
				print("👎")
				break
	else:
		print("wrong answer")
		break
	i=i+1
