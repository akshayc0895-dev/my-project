print("QUIZ GAME")
print("Answer 10 Questions")
print("you need 7 to pass")

score = 0

print("What is the capital of Maharashtra")
print("A. Mumbai")
print("B. Kolhapur")
print("C. Pune")
print("D. Singapore")

answer = input ("your answer (A/B/C/D): ")

if answer == "A" or answer == "a":
    print("CORRECT!\n")
    score = score + 1
else:
    print("Wrong! Answer is A. Mumbai\n")

print("Who is the current president of India")
print("A. Devendra fadanvis")
print("B. Atalbihari vajpayee")
print("C. Draupadi Murmu")
print("D. DR. APJ Kalam")

answer = input ("your answer (A/B/C/D): ")
if answer == "C" or answer == "c":
    print("Correct\n")
    score = score + 1
else:
    print("Wrong! Answer is C. Draupadi Murmu\n")

print("What is the power house of a cell?")
print("A. amoeba")
print("B. Mitochondria")
print("C. Duracell")
print("D. DR. Dre")

answer = input("Your answer (A/B/C/D): ")

if answer == "B" or answer == "b":
    print("Correct\n")
    score = score + 1
else:   
    print("Wrong! Answer is B. Mitochondria\n")

print("What is 24 + 26?")
print("A. 6")
print("B. 24")
print("C. 55")
print("D. 50")

answer = input("Your answer (A/B/C/D): ")

if answer == "D" or answer == "D":
    print("Correct\n")
    score = score + 1
else:   
    print("Wrong! Answer is D. 50\n")

print("What is the Batman related to?")
print("A. Marvel")
print("B. Mahabharata")
print("C. DC")
print("D. Ramanaya")

answer = input("Your answer (A/B/C/D): ")

if answer == "C" or answer == "c":
    print("Correct\n")
    score = score + 1
else:   
    print("Wrong! Answer is C. DC\n")

print("What is the National Animal of India")
print("A. Leopard")
print("B. Tiger")
print("C. Elephant")
print("D. Racoon")

answer = input("Your answer (A/B/C/D): ")

if answer == "B" or answer == "b":
    print("Correct\n")
    score = score + 1
else:   
    print("Wrong! Answer is B. Tiger\n")

print("Which year India got Independence?")
print("A. 1885")
print("B. 1995")
print("C. 2014")
print("D. 1947")

answer = input("Your answer (A/B/C/D): ")

if answer == "C" or answer == "c":
    print("Correct\n")
    score = score + 1
else:   
    print("Wrong! Answer is C. 2014\n")

print("Who is the owner of Tesla?")
print("A. Tesla")
print("B. Chilon Maa")
print("C. Jack Ma")
print("D. Elon Musk")

answer = input("Your answer (A/B/C/D): ")

if answer == "D" or answer == "d":
    print("Correct\n")
    score = score + 1
else:   
    print("Wrong! Answer is D. Elon Musk\n")

print("What is the national bird of India?")
print("A. Peacock")
print("B. Vulture")
print("C. Eagle")
print("D. Sparrow")

answer = input("Your answer (A/B/C/D): ")

if answer == "A" or answer == "a":
    print("Correct\n")
    score = score + 1
else:   
    print("Wrong! Answer is A. Peacock\n")


print("Who played the role of Jack Sparrow in The pirates of the Carrebian?")
print("A. Dharmendra")
print("B. Junny Dipp")
print("C. Sylvester Stallione")
print("D. Jonny depp")

answer = input("Your answer (A/B/C/D): ")

if answer == "D" or answer == "d":
    print("Correct\n")
    score = score + 1
else:   
    print("Wrong! Answer is D. Jonny Depp\n")

#Show results

print("Your Score")
print(f"You got {score} out of 10 correct")

percentage = (score / 10) * 100
print(f"percentage: {int(percentage)}%")

if score >= 7:
    print("You Passed! WELL DONE!")
else:
    print("You Filed! TRY AGAIN")
print("=====")
