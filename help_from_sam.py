def help_from_sam(score):
    help=1
    alex_score=1
    while score>=alex_score*2:
        alex_score*=2
    help=help+score-alex_score
    return help

score=int(input("Enter the Number : "))
print(help_from_sam(score))
