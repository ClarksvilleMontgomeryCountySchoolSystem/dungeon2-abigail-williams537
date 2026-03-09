good = r"""                           _                      
                            | |                     
  __ _ _ __   ___   ___ __ _| |_   _ _ __  ___  ___ 
 / _` | '_ \ / _ \ / __/ _` | | | | | '_ \/ __|/ _ \
| (_| | |_) | (_) | (_| (_| | | |_| | |_) \__ \  __/
 \__,_| .__/ \___/ \___\__,_|_|\__, | .__/|___/\___|
      | |                       __/ | |             
      |_|                      |___/|_|   """
bad = r"""   ______
   |  O   |
   | ,|._ |
   | `A  _|__
   |__|\_\   \ O
          \  ._|.)
           \___A
           _|_ |\  SSt"""
guard_awake = False

if not guard_awake:
    outcome  = "Shadow: You slip past the guard unnoticed."
    print(good)
else:
    outcome = "Doom: The guard spots you and raises the alarm."
    print(bad)
print(outcome)
