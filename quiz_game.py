print("QUIZ GAME")
print("Answer 3 Questions")
print("you need 2 to pass")

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

#Show results

print("Your Score")
print(f"You got {score} out of 3 correct")

percentage = (score / 3) * 100
print(f"percentage: {int(percentage)}%")

if score >= 2:
    print("You Passed! WELL DONE!")
else:
    print("You Filed! TRY AGAIN")
print("=====")
