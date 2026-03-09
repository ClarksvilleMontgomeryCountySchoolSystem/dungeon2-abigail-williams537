good = r"""    (,        ,)
        |  *_      |
        \\ (('^,  //
         \`()) _.'/
          ` )__)-'
            \  )
             )(
            /  `_.'_
           /   /_ , )
          /_.-'  ( /
            \ |  ,/
             \'( /
             ),)/
            ( )`
             \
             , 
 ejm         '|
             \/"""
bad = r"""Miami Heat
                           .
                         ,-; . ,
                ________i_,',//
          _odHHHHHHHHHHHHHHHHbo_
        dP^'         ;.| ||,; `^?b
       |H           ))`'||/';    H|
        ?bo.     .=;'   |||.' ,odP
          `?oo.-','     ||'oodP'
            /'  /      / |/
           |   |    _-'  ||
          ||  |   ,'     J|
          | \ |   |     / |
           |_\ L  L  .-' |
            \.)`-.;-;__./
              "-._;_.-"

       || ||  ||   |||   || ||  ||
      |||||| ||  || ||  |||||| || ,|
     || | || || || `|| || | || || `|
                                   J
            || || ||==   ||| ==||='
           ||=|| ||==  || ||  ||
           || || ||== || `||  ||
bodom
"""
drawbridge_raised = False

if not drawbridge_raised:
    outcome = "Thunder: The bridge slams down and clears your path."
    print(good)
else: outcome = "Doom: The gap below waits as the bridge stays high."
print(bad)
print(outcome)