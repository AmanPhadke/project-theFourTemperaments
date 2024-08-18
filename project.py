import tabulate
import sys

s = 0
c = 0
m = 0
p = 0

def main():
    print("\nWELCOME TO THE FOUR TEMPERAMENTS\n")
    print("-------------------------------\n")
    print("This program will determine your temperament based on your answers to a series of 10 different questions.")
    print("Please answer the questions with either 1, 2, 3 or 4 which will help us determine your personality type")
    print("\n-------------------------------\n")
    questions()

def questions():
    print("\n----------------QUESTION 1----------------\n")
    question_one()
    print("\n----------------QUESTION 2----------------\n")
    question_two()
    print("\n----------------QUESTION 3----------------\n")
    question_three()
    print("\n----------------QUESTION 4----------------\n")
    question_four()
    print("\n----------------QUESTION 5----------------\n")
    question_five()
    print("\n----------------QUESTION 6----------------\n")
    question_six()
    print("\n----------------QUESTION 7----------------\n")
    question_seven()
    print("\n----------------QUESTION 8----------------\n")
    question_eight()
    print("\n----------------QUESTION 9----------------\n")
    question_nine()
    print("\n----------------QUESTION 10----------------\n")
    question_ten()

def question_one():
    try:
        global s,c,m,p
        print("Question 1: What do you enjoy doing in the free time?")
        print("1. Reading, learning new things, and exploring new ideas")
        print("2. Spending time with friends and family, going out, and having fun")
        print("3. Engaging in physical activities, sports, and outdoor activities")
        print("4. Creating art, music, or writing, and expressing myself")
        answer1 = input("Enter your answer (1, 2, 3 or 4)")
        if answer1 == "1":
            s += 1
        elif answer1 == "2":
            c += 1
        elif answer1 == "3":
            m += 1
        elif answer1 == "4":
            p += 1
        else:
            raise ValueError

    except ValueError:
        print("Invalid Input. Try Again....\n")
        question_one()


def question_two():
    try:
        global s,c,m,p
        print("Question 2: How do you handle a challenging situation at work or school?")
        print("1. Analyze the situation in detail and plan a careful approach")
        print("2. Stay calm and take a steady, step-by-step approach")
        print("3. Talk it out with others to find a solution together")
        print("4. Take charge and tackle the problem head-on")

        answer2 = input("Enter your answer (1, 2, 3 or 4)")
        if answer2 == "3":
            s += 1
        elif answer2 == "4":
            c += 1
        elif answer2 == "1":
            m += 1
        elif answer2 == "2":
            p += 1
        else:
            raise ValueError

    except ValueError:
        print("Invalid Input. Try Again....\n")
        question_two()

def question_three():
    try:
        global s,c,m,p
        print("Question 3: When working in a team, what role do you naturally take on?")

        print("1. The supportive team member who ensures everyone gets along.")
        print("2. The leader who drives the project forward and makes decisions.")
        print("3. The one who focuses on details and ensures everything is done correctly.")
        print("4. The person who keeps everyone in good spirits and motivates the team.")

        answer3 = input("Enter your answer (1, 2, 3 or 4)")
        if answer3 == "4":
            s += 1
        elif answer3 == "2":
            c += 1
        elif answer3 == "3":
            m += 1
        elif answer3 == "1":
            p += 1
        else:
            raise ValueError

    except ValueError:
        print("Invalid Input. Try Again....\n")
        question_three()

def question_four():
    try:
        global s,c,m,p
        print("Question 4: How do you approach making important decisions?")
        print("1. I go with what feels right in the moment.")
        print("2. I think through all the details and potential outcomes.")
        print("3. I make quick decisions and stick to them.")
        print("4.  I take my time and consider everyone’s opinions.")

        answer4 = input("Enter your answer (1, 2, 3 or 4)")
        if answer4 == "1":
            s += 1
        elif answer4 == "3":
            c += 1
        elif answer4 == "2":
            m += 1
        elif answer4 == "4":
            p += 1
        else:
            raise ValueError

    except ValueError:
        print("Invalid Input. Try Again....\n")
        question_four()

def question_five():
    try:
        global s,c,m,p
        print("Question 5: What type of social setting do you find most enjoyable?")
        print("1. A lively party with lots of people and energy.")
        print("2. A meeting where I can share ideas and take the lead. ")
        print("3. A small, intimate gathering with close friends.")
        print("4. A relaxed environment with a few familiar faces.")
        answer5 = input("Enter your answer (1, 2, 3 or 4)")
        if answer5 == "1":
            s += 1
        elif answer5 == "2":
            c += 1
        elif answer5 == "3":
            m += 1
        elif answer5 == "4":
            p += 1
        else:
            raise ValueError

    except ValueError:
        print("Invalid Input. Try Again....\n")
        question_five()

def question_six():
    try:
        global s,c,m,p
        print("Question 6: How do you usually deal with conflict?")
        print("1. I reflect on it deeply and try to understand all sides.")
        print("2. I try to lighten the mood and bring everyone together.")
        print("3. I confront it directly and aim to resolve it quickly. ")
        print("4. I avoid it and try to keep the peace.")
        answer6 = input("Enter your answer (1, 2, 3 or 4)")
        if answer6 == "2":
            s += 1
        elif answer6 == "3":
            c += 1
        elif answer6 == "1":
            m += 1
        elif answer6 == "4":
            p += 1
        else:
            raise ValueError

    except ValueError:
        print("Invalid Input. Try Again....\n")
        question_six()

def question_seven():
    try:
        global s,c,m,p
        print("Question 7: What motivates you to get things done?")
        print("1. The excitement and fun of doing something new.")
        print("2. The drive to achieve success and be the best.")
        print("3. The satisfaction of doing something well and thoroughly.")
        print("4. The desire to help others and keep things running smoothly. ")
        answer7 = input("Enter your answer (1, 2, 3 or 4)")
        if answer7 == "1":
            s += 1
        elif answer7 == "2":
            c += 1
        elif answer7 == "3":
            m += 1
        elif answer7 == "4":
            p += 1
        else:
            raise ValueError
    except ValueError:
        print("Invalid Input. Try Again....\n")
        question_seven()

def question_eight():
    try:
        global s,c,m,p
        print("Question 8: How do you prefer to relax after a long day?")
        print("1. Reading, listening to music, or spending time alone.")
        print("2. Watching TV, meditating, or taking a leisurely walk.")
        print("3. Working on a hobby or something that feels productive.")
        print("4. Spending time with friends, chatting, or engaging in fun activities.")
        answer8 = input("Enter your answer (1, 2, 3 or 4)")
        if answer8 == "4":
            s += 1
        elif answer8 == "3":
            c += 1
        elif answer8 == "1":
            m += 1
        elif answer8 == "2":
            p += 1
        else:
            raise ValueError

    except ValueError:
        print("Invalid Input. Try Again....\n")
        question_eight()

def question_nine():
    try:
        global s,c,m,p
        print("Question 9: What kind of work environment do you thrive in?")
        print("1. A dynamic, ever-changing environment where I can interact with others. ")
        print("2. A fast-paced, competitive environment where I can take charge.")
        print("3. A structured, quiet environment where I can focus on details.")
        print("4. A calm, supportive environment where everyone works together.")
        answer9 = input("Enter your answer (1, 2, 3 or 4)")
        if answer9 == "1":
            s += 1
        elif answer9 == "2":
            c += 1
        elif answer9 == "3":
            m += 1
        elif answer9 == "4":
            p += 1
        else:
            raise ValueError

    except ValueError:
        print("Invalid Input. Try Again....\n")
        question_nine()

def question_ten():
    try:
        global s,c,m,p
        print("Question 10: What do you value most in your relationships with others?")
        print("1. Deep Connection and Understanding.")
        print("2.  Stability and trust.")
        print("3. Fun and excitement.")
        print("4. Respect and Loyalty.")
        answer10 = input("Enter your answer (1, 2, 3 or 4)")
        if answer10 == "3":
            s += 1
        elif answer10 == "4":
            c += 1
        elif answer10 == "1":
            m += 1
        elif answer10 == "2":
            p += 1
        else:
            raise ValueError

    except ValueError:
        print("Invalid Input. Try Again....\n")
        question_ten()

    result()


def result():
    print("\n----------------YOUR RESULT----------------\n")
    global s,c,m,p
    if all(s > x for x in [c, m, p]):
        print("You have a SANGUINE temperament")
        print("Hmmm....Bit social aren't you? You have an Optimistic, and lively personality. Sanguine personalities are often seen as fun-loving and talkative")

    elif all(c > x for x in [s, m, p]):
        print(f"You have a CHOLERIC temperament")
        print("You are Ambitious, leader-like, and dominant. Choleric individuals are often determined and quick to take action")

    elif all(m > x for x in [s, c, p]):
        print(f"You have a MELANCHOLIC temperament")
        print("You are very thoughtful, reserved, and often anxious. Melancholic people tend to be detail-oriented and introspective.")

    elif all(p > x for x in [s, m, c]):
        print(f"You have a PHLEGMATIC temperament")
        print("You are Calm, reliable, and thoughtful. Phlegmatic individuals are often patient, steady, and practical.")

    details = input("Do you want more detailed information? (y/n): \n")

    if details == "n":
        pass
    elif details == "y":
        if all(s > x for x in [c, m, p]):
            print("\n----------------SANGUINE----------------\n")
            print("""
Sociability: Highly outgoing, loves to interact with others, and enjoys being in social settings.
Optimism: Naturally positive and cheerful, often seeing the bright side of situations.
Spontaneity: Enjoys spontaneity and thrives in environments that allow for flexibility and change.
Expressiveness: Very expressive in emotions, gestures, and communication, making them lively and animated.
                    """)

            s = (s/10) * 100
            c = (c/10) * 100
            m = (m/10) * 100
            p = (p/10) * 100
            s = str(s)
            c = str(c)
            m = str(m)
            p = str(p)
            detail = [f"{s}%", f"{c}%",f"{m}%", f"{p}%"]
            headers = ["Sanguine", "Choleric", "Melancholic", "Phlegmatic"]

            print("\n----------------TABLE----------------\n")
            print("Here is the detailed table on your match with different temperaments")
            print(tabulate.tabulate([detail] ,headers= headers, tablefmt = "rounded_outline"))

        elif all(c > x for x in [s, m, p]):
            print("\n----------------CHOLERIC----------------\n")
            print("""
Leadership: Naturally takes charge and is comfortable making decisions and leading others.
Determination: Highly goal-oriented and driven to achieve success, often with a strong sense of purpose.
Decisiveness: Quick to make decisions and prefers to act swiftly and efficiently.
Confidence: Exudes self-confidence and is often assertive in pursuing their goals.
                    """)

            s = (s/10) * 100
            c = (c/10) * 100
            m = (m/10) * 100
            p = (p/10) * 100
            s = str(s)
            c = str(c)
            m = str(m)
            p = str(p)
            detail = [f"{s}%", f"{c}%",f"{m}%", f"{p}%"]
            headers = ["Sanguine", "Choleric", "Melancholic", "Phlegmatic"]

            print("\n----------------TABLE----------------\n")
            print("Here is the detailed table on your match with different temperaments")
            print(tabulate.tabulate([detail] ,headers= headers, tablefmt = "rounded_outline"))


        elif all(m > x for x in [s, c, p]):
            print("\n----------------MELANCHOLIC----------------\n")
            print("""
Analytical Thinking: Highly detail-oriented and analytical, with a strong focus on accuracy and precision.
Depth of Emotion: Experiences emotions deeply and is often introspective and reflective.
Perfectionism: Strives for perfection in all tasks, with a high standard for themselves and others.
Loyalty: Extremely loyal and dedicated, particularly in relationships and commitments.
                    """)

            s = (s/10) * 100
            c = (c/10) * 100
            m = (m/10) * 100
            p = (p/10) * 100
            s = str(s)
            c = str(c)
            m = str(m)
            p = str(p)
            detail = [f"{s}%", f"{c}%",f"{m}%", f"{p}%"]
            headers = ["Sanguine", "Choleric", "Melancholic", "Phlegmatic"]

            print("\n----------------TABLE----------------\n")
            print("Here is the detailed table on your match with different temperaments")
            print(tabulate.tabulate([detail] ,headers= headers, tablefmt = "rounded_outline"))

        elif all(p > x for x in [s, c, m]):
            print("\n----------------PHLEGMATIC----------------\n")
            print("""
Calmness: Naturally calm and composed, even in stressful situations, providing stability.
Patience: Exceptionally patient, often willing to wait or persist without frustration.
Diplomacy: Skilled at resolving conflicts and maintaining harmony in social interactions.
Reliability: Highly dependable and consistent, often serving as a reliable support for others.
                    """)

            s = (s/10) * 100
            c = (c/10) * 100
            m = (m/10) * 100
            p = (p/10) * 100
            s = str(s)
            c = str(c)
            m = str(m)
            p = str(p)

            detail = [f"{s}%", f"{c}%",f"{m}%", f"{p}%"]
            headers = ["Sanguine", "Choleric", "Melancholic", "Phlegmatic"]

            print("\n----------------TABLE----------------\n")
            print("Here is the detailed table on your match with different temperaments")
            print(tabulate.tabulate([detail] ,headers= headers, tablefmt = "rounded_outline"))

    else:
        sys.exit("Created by Aman Phadke")

if __name__ == "__main__":
    main()
