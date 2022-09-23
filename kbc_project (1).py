import time
from playsound import playsound

                             
# time modeule is installed here using 'pip install time'

print("\n\n\n\n ")
print("\t\t\t\t\t\t\\----------------------------|||||| ---------------------- ||||||-------------------------------\\   ")
print("\t\t\t\t\t\t\\----------------------------|||||| KAUN BANEGAA CROREPATI ||||||-------------------------------\\   ")
print("\t\t\t\t\t\t\\----------------------------|||||| KAUN BANEGAA CROREPATI ||||||-------------------------------\\   ")
print("\t\t\t\t\t\t\\----------------------------|||||| ---------------------- ||||||-------------------------------\\   ")
playsound('kbc.mp3')



print("\n\n\n")#it is for newline
nam = ''# This is used for storing the string values
name = input("\t\t\t\\Enter  your  name  ::::")
nam = name.upper()#it will print the string in uppercase letter 
count=0#it
count2=0

print("\n")

age = int(input("\t\t\t\\Enter your age :::"))
print("\n\n")
p = "\t\t\tProcessing........"
print(p.upper())
time.sleep(2)
for i in range(1):
    if (age > 40):
        print("\n You are not eligible for playing our game ")
        break
    elif (age > 18):
        print("\t\t\t\t\t\t_________________________________________________________________________________________________")
        print("\t\t\t\t\t\t_________________________________________________________________________________________________")
        print("\n\n\t\t\t\t\t\t\t\t\t\t || WELCOME !! {} TO OUR CONTEST || ".format(nam))
        print("\t\t\t\t\t\t_________________________________________________________________________________________________")
        print("\t\t\t\t\t\t_________________________________________________________________________________________________")
        time.sleep(4)

        print("\n")
        print("\t\t\t\t\t\t\t\t\t\t \\\\-RULES FOR PLAYING OUR GAME-\\\\ ")

        print("\n\t\t\t\t\t\t## This is a virtual entertainment game for Kaun Banegaa Crorepati. ")

        print(" \t\t\t\t\t\tb) The questions have no time limit ")
        print(" \t\t\t\t\t\td) If you use google to find answers then know that you are a big cheater ")
        print(" \t\t\t\t\t\te) If you answered till the last question in final round you will be awarded 1 lakh rupees cash prize")
        print(" \t\t\t\t\t\tf) If you know your answer is correct then only press enter")
        print(" \t\t\t\t\t\tg) Once you press enter you cannot cannot change your answer")
        print(" \t\t\t\t\t\th) There will be two rounds,you have to qualify the first round to get into the  second round ")
        print(" \t\t\t\t\t\tg) In first round, there are total of 5 questions and you have to answer the 2 questions correct out of 5 questions ")
        print(" \t\t\t\t\t\th) In second round, there are total 10 questions")
        time.sleep(10)
        print("\t\t\t\t\t\t_________________________________________________________________________________________________")
        print("\t\t\t\t\t\t_________________________________________________________________________________________________")

        #print("\n \t\t\t\t\t\t\t\t\t\t Let's start the game ") # from here Qualifier round start 

        
        print("\n\n\n")
        print("\t\t\t\t\t\t\t\t\t\t\t|| Qualifier Round ||")
        time.sleep(5)

        print("\n\n")
        print("\t\t\t\t\t\t\\\\Lets start the game with the first question.......")
        time.sleep(5)
        print("\n\n\t\t\t\t\t\tQuestion 1. Who is the chief minister of Uttarakhand ? ")
        print("\n\t\t\t\t\t\t 1.Narendra Modi \t\t\t\t 2. Pushkar Singh Dhami \n\t\t\t\t\t\t 3.Bhagat Singh Koshyari \t\t\t 4.B.C. Khanduri")
        ch = int(input("\n\t\t\t\t\t\t Enter your choice ::"))
        if ch == 2:
            playsound('correct.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\n\t\t\t\t\t\t\t\t\t--\\ Correct answer \\--")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            count += 1
        else:
            playsound('wrong.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\n\t\t\t\t\t\t\t\t--\\ wrong answer \\--")
            print('\n')
            print("\t\t\t\t\t\t\t\t________________________")

        print("\n\n")
        print("\t\t\t\t\t\t\\\\Lets get into the second question.......")
        time.sleep(5)
        print("\n\n\t\t\t\t\t\t Question 2. Which country has hosted the 2012 Olympics Games ? ")
        print("\n\t\t\t\t\t\t 1.Spain \t\t\t\t 2.India \n\t\t\t\t\t\t 3.London \t\t\t\t 4.Australia")
        ch2 = int(input("\n\t\t\t\t\t\t Enter your choice ::"))
        if ch2 == 3:
            playsound('correct.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Correct answer \\--")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            count += 1
        else:
            playsound('wrong.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Wrong Answer \\--")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")


        print("\n")
        print("\t\t\t\t\t\t\\\\Lets get into the third question........")
        time.sleep(5)
        print("\n\n\t\t\t\t\t\t Question 3.Which among the following was the last ruler of Gupta empire ?")
        print("\n\t\t\t\t\t\t 1.Vishnugupta \t\t\t\t 2.Chandragupta 2 \n\t\t\t\t\t\t 3.Buddhagupta \t\t\t\t 4.kumargupta 2")
        ch3 = int(input("\n\t\t\t\t\t\t Enter your choice ::"))
        if ch3 == 1:
            playsound('correct.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Correct answer \\--")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            count += 1
        else:
            playsound('wrong.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Wrong answer \\--")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")


        print("\n")
        print("\t\t\t\t\t\t\\\\Lets get into the fourth question.......")
        time.sleep(5)
        print("\n\n\t\t\t\t\t\t Question 4.What is the escape velocity at Moon ?")
        print("\n\t\t\t\t\t\t 1.2.38 km/s \t\t\t\t 2.4.38 km/s \n\t\t\t\t\t\t 3.6.38 km/s \t\t\t\t 4.1.38 km/s")
        ch4 = int(input("\n\t\t\t\t\t\t Enter your choice ::"))
        if ch4 == 4:
            playsound('correct.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Correct answer \\--")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            count += 1
        else:
            playsound('wrong.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ wrong answer \\--")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")


        print("\n")
        print("\t\t\t\t\t\t\\\\Lets get into the fifth question.......")
        time.sleep(5)
        print("\n\n\t\t\t\t\t\t Question 5. Which day is celebrated as World Rights Day?")
        print("\n\t\t\t\t\t\t 1. 8 September \t\t\t\t 2. 7 July \n\t\t\t\t\t\t 3. 19 April \t\t\t\t\t 4. 28 June")
        ch5 = int(input("\n\t\t\t\t\t\t Enter your choice ::"))
        if ch5 == 1:
            playsound('correct.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Correct answer \\ --")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            count += 1
        else:
            playsound('wrong.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Wrong answer \\--")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")

        print("\n")

        
                  

        print("\n")
        o = "processing............."
        print(o.upper())
        time.sleep(10)
        print("\t\t\t\t\t\t_________________________________________________________________________________________")
        print("\t\t\t\t\t\t_________________________________________________________________________________________")
        if count >= 2:
            print("\n\t\t\t\t\t\t\t\t--\\Congratulations !!! You Qualify for next round with {} points\\-- ".format(count))
        else:
            print("\n\t\t\t\t\t\t\t\t--\\You only correct {} question,that's why you are not Qualify for further round\\--".format(count))

        print("\t\t\t\t\t\t_________________________________________________________________________________________")
        print("\t\t\t\t\t\t_________________________________________________________________________________________")
        time.sleep(5)

        # From here main game start :-
        print("\n\t\t\t\t\t\t\t\t\t---\\Final Round \\---")
        time.sleep(10)

        print("\n\n")
        print("\t\t\t\t\t\t\\\\Lets start the final round with the first question.......")
        time.sleep(5)
        print("\n\n\t\t\t\t\t\t Question 1. Which of the following generation of computers is associated with artificial intelligence? ")
        print("\n\t\t\t\t\t\t 1.First \t\t\t\t 2.Third \n\t\t\t\t\t\t 3.Fifth \t\t\t\t 4.Seventh")
        ch6=int(input("\n\t\t\t\t\t\t Enter your choice::"))
        if ch6==3:
            playsound('correct.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Correct answer \\ --")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            count2+=1
            
        else:
            playsound('wrong.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Wrong answer \\--")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            

        print("\n\n")
        print("\t\t\t\t\t\t\\\\Lets get into the second question.......")
        time.sleep(5)
        print("\n\n\t\t\t\t\t\t Question 2. Ghumar is a folk dance of which state?")
        print("\n\t\t\t\t\t\t 1.Gujarat \t\t\t\t 2.Rajasthan \n\t\t\t\t\t\t 3.Madhya Pradesh \t\t\t 4.Uttar Pradesh")
        ch7=int(input("\n\t\t\t\t\t\t Enter your choice::"))
        if ch7==2:
            playsound('correct.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Correct answer \\ --")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            count2+=1
            
            
        else:
            playsound('wrong.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Wrong answer \\--")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")


        print("\n\n")
        print("\t\t\t\t\t\t\\\\Lets get into the third question.......")
        time.sleep(5)
        print("\n\n\t\t\t\t\t\t Question 3.The nucleus of an atom consists of::")
        print("\n\t\t\t\t\t\t 1.electrons and neutrons \t\t\t\t 2.electrons and protons \n\t\t\t\t\t\t 3.protons and neutrons \t\t\t\t 4.All of the above")
        ch8=int(input("\n\t\t\t\t\t\t Enter your choice :::"))
        if ch8==3:
            playsound('correct.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Correct answer \\ --")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            count2+=1
            
        else:
            playsound('wrong.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Wrong answer \\--")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")


        print("\n\n")
        print("\t\t\t\t\t\t\\\\Lets get into the fourth question.......")
        time.sleep(5)   
        print("\n\n\t\t\t\t\t\t Question 4.Who was the Iron man of India? ")
        print("\n\t\t\t\t\t\t 1.Govind Ballah Pant \t\t\t\t 2.Jawaharlal Nehru \n\t\t\t\t\t\t 3.Subash Chandra Bose \t\t\t\t 4.Sardar Vallabhbhai Patel ")
        ch9=int(input("\n\t\t\t\t\t\t Enter your choice :::"))
        if ch9==4:
            playsound('correct.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Correct answer \\ --")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            count2+=1
        else:
            playsound('wrong.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Wrong answer \\--")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")


        print("\n\n")
        print("\t\t\t\t\t\t\\\\Lets get into the fifth question.......")
        time.sleep(5)
        print("\n\n\t\t\t\t\t\t Question 5.What is part of a database that holds only one type of information?")
        print("\n\t\t\t\t\t\t 1.Report \t\t\t\t 2.Field \n\t\t\t\t\t\t 3.Record \t\t\t\t 4.File")
        ch10=int(input("\n\t\t\t\t\t\t Enter your choice :::"))
        if ch10==2:
            playsound('correct.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Correct answer \\ --")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            count2+=1
        else:
            playsound('wrong.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Wrong answer \\--")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")


        print("\n\n")
        print("\t\t\t\t\t\t\\\\Lets get into the sixth question.......")
        time.sleep(5)   
        print("\n\n\t\t\t\t\t\t Question 6.What is the name of a channel that separates the Andaman Islands from the Nicobar Isalnds in the Bay of Bengal")
        print("\n\t\t\t\t\t\t 1.9 Degree Channel \t\t\t\t 2.10 Degree channel \n\t\t\t\t\t\t 3.11 Degree Channel \t\t\t\t 4.12 Degree Channel")
        ch11=int(input("\n\t\t\t\t\t\t Enter your choice :::"))
        if ch11==2:
            playsound('correct.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Correct answer \\ --")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            count2+=1
        else:
            playsound('wrong.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Wrong answer \\--")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")


        print("\n\n")
        print("\t\t\t\t\t\t\\\\Lets get into the seventh question.......")
        time.sleep(5)    
        print("\n\n\t\t\t\t\t\t Question 7.Which continent has the highest number of countries ")
        print("\n\t\t\t\t\t\t 1.Asia \t\t\t\t 2.Europe \n\t\t\t\t\t\t 3.North America \t\t\t 4.Africa")
        ch12=int(input("\n\t\t\t\t\t\t Enter your choice:::"))
        if ch==4:
            playsound('correct.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Correct answer \\ --")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            count2+=1
        else:
            playsound('wrong.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Wrong answer \\--")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")

        print("\n\n")
        print("\t\t\t\t\t\t\\\\Lets get into the eight question.......")
        time.sleep(5)
        print("\n\n\t\t\t\t\t\t Question 8.Who opened the first school for girls in India?")
        print("\n\t\t\t\t\t\t 1.Savitribai Phule \t\t\t\t 2.Sarojini Naidu \n\t\t\t\t\t\t 3.Lakshmi Sahgal \t\t\t\t 4.Ahilyabai Holkar")
        ch13=int(input("\n\t\t\t\t\t\t Enter your choice :::"))
        if ch13==1:
            playsound('correct.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Correct answer \\ --")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            count2+=1
        else:
            playsound('wrong.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Wrong answer \\--")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")


        print("\n\n")
        print("\t\t\t\t\t\t\\\\Lets get into the ninth question.......")
        time.sleep(5)
        print("\n\n\t\t\t\t\t\t Question 9.Who has the right to transfer a Judge from one high court to another high court?")
        print("\n\t\t\t\t\t\t 1.President \t\t\t\t 2.Prime Minister \n\t\t\t\t\t\t 3.Law Minister of india \t\t 4.Chief Justice of India")
        ch14=int(input("\n\t\t\t\t\t\t Enter your choice :::"))
        if ch14==1:
            playsound('correct.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Correct answer \\ --")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            count2+=1
        else:
            playsound('wrong.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Wrong answer \\--")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")


        print("\n\n")
        print("\t\t\t\t\t\t\\\\Lets get into the tenth question.......")
        time.sleep(5)          
        print("\n\n\t\t\t\t\t\t Question 10.Gudi Padwa is a traditional festival celebrated in which state of India?")
        print("\n\t\t\t\t\t\t 1.Andhra Pradesh \t\t\t 2.Maharashtra \n\t\t\t\t\t\t 3.Telangaan \t\t\t\t 4.Assam")
        ch15=int(input("\n\t\t\t\t\t\t Enter your choice:::"))
        if ch15==2:
            playsound('correct.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Correct answer \\ --")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            count2+=1

        else:
            playsound('wrong.mp3')
            print("\n")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")
            print("\t\t\t\t\t\t\t\t\t--\\ Wrong answer \\--")
            print("\t\t\t\t\t\t\t\t\t________________________")
            print("\n")

        if count2==10:
            print("\n\n\t\t\t\t You won the game with 1lakh rupees")

        else:
            print("\n\n\t\t\t\t You lose")


    else:
        print("\n\t\t\t\t\t\t\\--You are too young for this game--\\")
