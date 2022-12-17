# logo = dict()
#
# logo["Jo"] = 23.00
# logo["Nokia"] = 40.00
# logo["Google"] = 54.00
# print(logo)
# print(logo.get("Nokia"))

votes = {}
def getVote(name):
    if votes.get(name):
        print("Taa get out!")
    else:
        votes[name] = True
        print("Go ahead with your vote")


print(getVote("Tolu"))
print(getVote("Sade"))
print(getVote("Tolu"))
