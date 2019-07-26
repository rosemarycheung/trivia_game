from clint.textui.colored import red, green, yellow, cyan, magenta
import json


def main():
    """
        Runs the trivia game
    """
    score = 0
    
    with open ("trivia_questions.json") as f:
        questions = json.load(f)

    name = input(yellow("What is your name?\n"))
    print(magenta("Hello {}".format(name)))

    for x in questions:
        print(cyan("\n{}".format(x["question"])))
        answer = input()
        if answer.lower() == x["answer"].lower():
            print(green("Correct!"))
            score += 1
        else:
            print(red("Incorrect!"))
    print(magenta("\nYour score: {}%".format(score/len(questions)*100)))

if __name__ == "__main__":
    main()
