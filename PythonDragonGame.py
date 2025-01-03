# Written by Chris B
# Assignment 1 - Python Dragon Game!

import random

print("My name is Chris")
print("Enter your target number:")
target_number = int(input())

die_total = 0
roll_num = 0
current_die_num = 0

while(die_total < target_number):
    current_die_num = random.randint(1, 6)
    die_total += current_die_num
    print(f'roll #{roll_num} = {current_die_num}, sum = {die_total}')
    roll_num += 1


if(die_total > target_number):
    print("""              __   __  _______  __   __    ___      _______  _______  _______    ___    ____    
             |  | |  ||       ||  | |  |  |   |    |       ||       ||       |  |   |  |    |   
             |  |_|  ||   _   ||  | |  |  |   |    |   _   ||  _____||    ___|  |___| |    _|   
             |       ||  | |  ||  |_|  |  |   |    |  | |  || |_____ |   |___    ___  |   |     
             |_     _||  |_|  ||       |  |   |___ |  |_|  ||_____  ||    ___|  |   | |   |     
               |   |  |       ||       |  |       ||       | _____| ||   |___   |___| |   |_    
               |___|  |_______||_______|  |_______||_______||_______||_______|         |____|""")
    print(r"""\  (  )   /\   _                 (     
    \ |  (  \ ( \.(               )                      _____
  \  \ \  `  `   ) \             (  ___                 / _   \
 (_`    \+   . x  ( .\            \/   \____-----------/ (o)   \_
- .-               \+  ;          (  O                           \____
                          )        \_____________  `              \  /
(__                +- .( -'.- <. - _  VVVVVVV VV V\                 \/
(_____            ._._: <_ - <- _  (--  _AAAAAAA__A_/                  |
  .    /./.+-  . .- /  +--  - .     \______________//_              \_______
  (__ ' /x  / x _/ (                                  \___'          \     /
 , x / ( '  . / .  /                                      |           \   /
    /  /  _/ /    +                                      /              \/
   '  (__/                                             /                  \ """)
else:
    print(r"""\    __   __  _______  __   __    _     _  ___   __    _  __  
    |  | |  ||       ||  | |  |  | | _ | ||   | |  |  | ||  | 
    |  |_|  ||   _   ||  | |  |  | || || ||   | |   |_| ||  | 
    |       ||  | |  ||  |_|  |  |       ||   | |       ||  | 
    |_     _||  |_|  ||       |  |       ||   | |  _    ||__| 
      |   |  |       ||       |  |   _   ||   | | | |   | __  
      |___|  |_______||_______|  |__| |__||___| |_|  |__||__| """)
    print(r"""                        ,////,
                        /// 6|
                        //  _|
                       _/_,-'
                  _.-/'/   \   ,/;,
               ,-' /'  \_   \ / _/
               `\ /     _/\  ` /
                 |     /,  `\_/
                 |     \'
     /\_        /`      /\
   /' /_``--.__/\  `,. /  \
  |_/`  `-._     `\/  `\   `.
            `-.__/'     `\   |
                          `\  \
                            `\ \
                              \_\__
                               \___)""")