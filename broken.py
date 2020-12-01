high="Excellent"
middle="Passable"
low="Bad"
def main():
    score=float(input("Enter score:"))
    while not valid_score(score):
        print("Invalid Score")
        score=float(input("Enter score:"))
    print("End of Program")

def valid_score(score):
    while score<0 or score>100:
        return False
    if score >= 90 and score<100:
        print(high)
    elif score>50 and score<90:
        print(middle)
    elif score>=0 and score <50:
        print(low)
    return True
main()