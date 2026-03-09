good = r"""       _
             _(<`O ,
         ==-(  >`-/ \
          ,< \  / >
         ---'--- `---'-MK/ejm
"""
bad = r"""        _ /
    /\----_- -
   /         \\
  /           \
 |             \_
  \___-_        /
        \      /
         |     |
         |     //|
         (    ||/
          \__/
"""
torch_lit = True
if torch_lit:
    outcome = "Flicker: The flame glows warmly, revealing a hidden passage"
    print(good)
else:
    outcome = "Doom: Darkness swallows the room as shadows close in."
    print(bad)
print(outcome)