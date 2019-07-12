import random

five_syllables = ["And I fall in love", "Like crunchy cornflakes", "I sleep peacefully", 
"This will last forever", "And I'm there with you", "But it's not for me", 
"I will be home soon","His toenail unfolds", "I can only stare", "I took a big bite",
"Once your feet get wet", "Incorrectly wrapped", "My day is ruined", "Here we go again",
"You puke your guts out", "I sleep peacefully", "Fall weather is here", "Hence, the attitude", "They call this living", "So we can be rich","Doot doot doot doot doot", "Sometimes I'm thinking", "The bug met his doom", ]

seven_syllables = ["A rotten rubberband snaps", "Slid off her shoulder today",
 "It's never what you'd expect", "It's time for a vacation", "I hope it's not yucky bread",
"See how many you can take", "It might be time to leave now", "I close my eyes and listen", "Need to organize my socks", "Doot doot doot doot doot doot doot", ]

position_pick_five = random.randint(0, len(five_syllables)-1)

print(five_syllables[position_pick_five])

position_pick_seven = random.randint(0, len(seven_syllables)-1)
print(seven_syllables[position_pick_seven])

position_pick_five_again = random.randint(0, len(five_syllables)-1)
print(five_syllables[position_pick_five_again])
