good = r"""      o
       |
 o    ,|.
 |  ,' \ `.
 |,'\,' ,' `.   o
 |.`. ,'     `. |
 | `.`.    o  ,'| 
     `.`.  |,'  |
       `.`.|  ,'|
         `.|,'
           |
unknown
"""
bad = r"""          _     _       
          | |   (_)      
  ___ __ _| |__  _ _ __  
 / __/ _` | '_ \| | '_ \ 
| (_| (_| | |_) | | | | |
 \___\__,_|_.__/|_|_| |_|"""
# Task 5 - The escape
escaped = True

if escaped:
    outcome = "Legend: You step into freedom as the gates fade behind you."
    print(good)
else:
    outcome = "Doom: The dungeon claims another last soul."
    print(bad)
print(outcome)
