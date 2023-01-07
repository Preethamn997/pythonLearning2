yuan = int(input("what do you have left in yuan"))
dollar = int(input("what do you have left in dollar"))
won = int(input("what do you have left in won"))
rupee_to_yuan = 12.06*yuan
rupee_to_dollar = 82.73*dollar
rupee_to_won = 0.06*won
total = rupee_to_yuan+rupee_to_dollar+rupee_to_won
print(total)


