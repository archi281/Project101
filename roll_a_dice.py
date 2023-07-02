import random
response = input("Do you want to roll the dice (y for yes, n for no)? ")

while response == "y":
    no = random.randint(1,6)
    if response == "y":
         if no == 1: 
              print("[-----]")
              print("[     ]")
              print("[  0  ]")
              print("[     ]")
              print("[-----]")
              response = input("Do you want to roll the dice (y for yes, n for no)? ")
         elif no == 2:
              print("[-----]")
              print("[ 0   ]")
              print("[     ]")
              print("[   0 ]")
              print("[-----]")
              response = input("Do you want to roll the dice (y for yes, n for no)? ")
         elif no == 3:
              print("[-----]")
              print("[0    ]")
              print("[  0  ]")
              print("[    0]")
              print("[-----]")
              response = input("Do you want to roll the dice (y for yes, n for no)? ")
         elif no == 4:
              print("[-----]")
              print("[0   0]")
              print("[     ]")
              print("[0   0]")
              print("[-----]")  
              response = input("Do you want to roll the dice (y for yes, n for no)? ")
         elif no == 5:
              print("[-----]")
              print("[0   0]")
              print("[  0  ]")
              print("[0   0]")
              print("[-----]")
              response = input("Do you want to roll the dice (y for yes, n for no)? ")
         else:
              print("[-----]")
              print("[0   0]")
              print("[0   0]")
              print("[0   0]")
              print("[-----]")
              response = input("Do you want to roll the dice (y for yes, n for no)? ")
    


