question  	  =	["In the Film (OMG Oh My God) Kanji Bhai filed a case against whom for the damage of his shop due to an earthquake ?","What is the new name of the Hyderabad franchise that would replace Deccan Charges in IPL6?","What is the sum of the numbres of thieves in the popular story of Ali Baba and the total number of overs bowled in a T20 match?","The National Register of Citizen (NRC) is the list of Indian citizens of which state?","This place of worship belongs to which religion?","Which City hosted more than a lakh of people to perform yoga together and  created a Guinness World Record on the occasion of International Day of Yoga, 2018?","who became the first Indian to score a century before lunch in the opening session of a Test Match in June 2018?","Which of these is a title given to the one who is a highly-skilled person or an expert?","In which of these sports would you normally see the referee running on the field?","Madhuri Dixits (Bucket List) is her film in which language?","What characteristics of a leopard is used by scientists to identify them individually?","Which of these national flags has the most number of stars on them?","By what name is the 24-day Salt March of March-April 1930 also known as?","Tirana International Airport is named after which Indian Citizen?","Indian Railways has been running daily special trains in Mumbai since June, 2018 to collect what?"]
first_option  = ["Bharat Mata"                    ,"Sun Chargers"           ,"Forty"    ,"Sikkim"              ,"Bahai"		       ,"Jaipur"	 ,"Lokesh Rahul"	  ,"Rahbar"		,"Cricket."		 ,"English"     ,"Pugmarks"         ,"USA"            ,"Dilli Chalo"           ,"C V Raman"             ,"Garbage"]
second_option = ["Parliament (Bhartiya Sansad)"   ,"Nizam Jyothi"			,"Sixty"    ,"Assam"               ,"Zoroastrianism"   ,"Jodhpur"	 ,"Shikhar Dhawan"	  ,"Sahib"	    ,"Football"      ,"Hindi"       ,"Spot patterns"    ,"Brazil"         ,"Farmers March"         ,"Mahatma Gandhi"        ,"Lunch Boxes"]
third_option  = ["Mumbai City"                    ,"Andhra Aces"            ,"Eighty"   ,"Meghalaya"		   ,"Jainism"		   ,"Kota"		 ,"Ajinkya Rahane"	  ,"Faiz"       ,"Badminton"     ,"Marathi"     ,"Tail"             ,"Australia"      ,"Jail Bharo Andolan"    ,"Mother Teresa"         ,"Milk"]
forth_option  = ["Bhagwan (God)"                  ,"Sun risers Hyderabad"   ,"Hundred"  ,"Arunachal Pradesh"   ,"Buddhism"         ,"Udaipur"    ,"Rohit Sharma"	  ,"Ustaad"     ,"Tennis"        ,"Telugu"      ,"Whiskers"         ,"New Zealand"    ,"Dandi March"           ,"Rabindranath Tagore"   ,"Left Over Food"]
all_option    =	[first_option, second_option, third_option, forth_option]
ans_key 	  = [4,4,3,2,1,3,2,4,2,3,2,1,4,3,1]
index 		  = 0
sum 		  = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]

print ("\n\033[1;34;40m Aaiye Kon banega karodpati mei aapka swagat he.\033[0m\n")
while index < len(question):
	print ("\033[1;37;45m Aapka %s question ye rha aapki screen par :\033[0m\n"%str(index+1))
	print ("\033[1;32;40m Question : %s \033[0m"%question[index])
	print ("\033[35m 1 ) : %s \033[0m"%first_option[index])
	print ("\033[35m 2 ) : %s \033[0m"%second_option[index])
	print ("\033[35m 3 ) : %s \033[0m"%third_option[index])
	print ("\033[35m 4 ) : %s \033[0m"%forth_option[index])
	userinput = int(input(" \nEnter your ans : "))
	print (" ")
	if userinput == ans_key[index]:
		print ("Right answer :)")
		print ("You won Rs. ",sum[index])
		print ("")
		if index == 5 :
			print ("\033[1;36;40m Congrats! Aapka pahlapadaav pura ho gaya hai.\033[0m\n")
		elif index == 10 :
			print  ("\033[1;36;40m Congrats! Aapka doosra padaav pura ho gaya hai.\033[0m\n")
		elif index == 14 :
			print  ("\033[1;36;40m Congrats! Aap ek crore rupye jeet gaye hai.\033[0m\n")	
	else:
		print ("===> wrong answer :)")
		print ("   your loss. ")
		if index >= 10 :
			print ("aap ",str(320000), "rupye jeet gae he")
		elif index >= 5 :
			print ("aap  ",str(20000), "rupye jeet gae he")	
		break
	index  = index + 1

	
