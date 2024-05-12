print("Welcome to 'ChronoQuiz: Challenge of the Ages' – the ultimate console game blending general knowledge with current affairs! Embark on an exhilarating journey through time and trivia as you test your intellect against the clock. From ancient history to cutting-edge news, every question challenges your wits and keeps you on the edge of your seat. Are you ready to become a master of both past and present? Get ready to unlock the mysteries of time and conquer the quiz of the ages!")
answer=False
correctanswer=0
q1="""Which country hosted the 2024 Summer Olympics?
A) United States
B) France
C) Japan
D) Australia"""
print(q1)
answer=input()
if"b" in answer:
    print("correct")
    correctanswer+=1
else:
    print("wrong")
q1="""Who won the Nobel Peace Prize in 2024 for their efforts in climate change activism?
A) Greta Thunberg
B) Malala Yousafzai
C) Al Gore
D) Kailash Satyarthi"""
print(q1)
answer=input()
if"a" in answer:
    print("correct")
    correctanswer+=1
else:
    print("wrong")
q1="""Which country recently launched its first mission to Mars?
A) India
B) China
C) United Arab Emirates
D) Russia"""
print(q1)
answer=input()
if"c" in answer:
    print("correct")
    correctanswer+=1
else:
    print("wrong")
q1="""Which global organization celebrated its 75th anniversary in 2024?
A) United Nations
B) World Health Organization
C) International Monetary Fund
D) World Trade Organization"""
print(q1)
answer=input()
if"a" in answer:
    print("correct")
    correctanswer+=1
else:
    print("wrong")
q1="""Who became the first woman to climb Mount Everest without supplemental oxygen in 2024?
A) Junko Tabei
B) Pasang Lhamu Sherpa
C) Reinhold Messner
D) Nirmal Purja"""
print(q1)
answer=input()
if"b" in answer:
    print("correct")
    correctanswer+=1
else:
    print("wrong")

print(f"you give {correctanswer} correct answer")
print("uncomplete")


