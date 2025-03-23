# AoC Day 4
# @author: Friedrich Leez

with open("04/file.txt") as f:
    s = f.read()


sum = 0
scratchcard_wn_amount = []
won_cards = []
for scratchcard in s.strip().split("\n"):
    id = int(scratchcard.split(":")[0].strip().split(" ")[1])
    won_cards.append(1)
    winning_numbers = []
    own_numbers = []
    for c in scratchcard.split(":")[1].strip().split("|")[0].strip().split(" "):
        if c.isdigit():
            winning_numbers.append(int(c))
    for c in scratchcard.split(":")[1].strip().split("|")[1].strip().split(" "):
        if c.isdigit():
            own_numbers.append(int(c))
    
    wn_amount = 0
    for number in own_numbers:
        if number in winning_numbers:
          wn_amount +=1
    scratchcard_wn_amount.append(wn_amount)

    for wn in scratchcard_wn_amount:
        for i in range(id,id+wn_amount):
            won_cards[i-1] +=1

   
    #if wn_amount:
        #sum += 2**(wn_amount-1)
   
print(scratchcard_wn_amount) 
print(won_cards)



#mistake in the task description: card 1 does only have 4 winning numbers!!!!!!