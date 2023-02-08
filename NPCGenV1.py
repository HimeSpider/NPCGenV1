#imports a library made for randomization
import random;
#imports script for delay
import time;
#imports script for reloading
import importlib
#imports generation script
import goblin
#prints Text at top of screen
print(' _______                   __        __    __  _______    ______  ');
print('|       \                 |  \      |  \  |  \|       \  /      \ ');
print('| DDDDDDD\ _______    ____| DD      | NN\ | NN| PPPPPPP\|  CCCCCC|');
print('| DD  | DD|       \  /      DD      | NNN\| NN| PP__/ PP| CC   \CC');
print('| DD  | DD| NNNNNNN\|  DDDDDDD      | NNNN\ NN| PP    PP| CC      ');
print('| DD  | DD| NN  | NN| DD  | DD      | NN|NN NN| PPPPPPP | CC   __ ');
print('| DD__/ DD| NN  | NN| DD__| DD      | NN |NNNN| PP      | CC__/  |');
print('| DD    DD| NN  | NN \DD    DD      | NN  |NNN| PP       \CC    CC');
print(' \DDDDDDD  |NN   |NN  \DDDDDDD       |NN   |NN \PP        \CCCCCC ');
time.sleep(1.5)
print('        ______                                                     __                         ');
print('       /      \                                                   |  \                        ');
print('      |  GGGGGG\  ______   _______    ______    ______   ______  _| TT_     ______    ______  ');
print('      | GG __\GG /      \ |       \  /      \  /      \ |      \|   TT \   /      \  /      \ ');
print('      | GG|    \|  EEEEEE\| NNNNNNN\|  EEEEEE\|  RRRRRR\ \AAAAAA||TTTTTT  |  OOOOOO\|  RRRRRR|');
print('      | GG \GGGG| EE    EE| NN  | NN| EE    EE| RR   \RR/      AA | TT __ | OO  | OO| RR   \RR');
print('      | GG__| GG| EEEEEEEE| NN  | NN| EEEEEEEE| RR     |  AAAAAAA | TT|  \| OO__/ OO| RR      ');
print('       \GG    GG \EE     \| NN  | NN \EE     \| RR      \AA    AA  \TT  TT \OO    OO| RR      ');
print('        \GGGGGG   \EEEEEEE |NN   |NN  \EEEEEEE \RR       \AAAAAAA   \TTTT   \OOOOOO  \RR      ');
print('');
print('');
print('');
#shows how many creaturs have been added so far
time.sleep(1.5)
print('18/300+ creatures have been added');
print('');
print('');
print('');
print('');
#gives the list of options that you can choose
time.sleep(1.5)
print('Options:');
time.sleep(0.5)
print('* Goblin');
time.sleep(0.5)
print('* Goblin Boss');
time.sleep(0.5)
print('* Beholder');
time.sleep(0.5)
print('* Beholder Zombie');
time.sleep(0.5)
print('* Black Dragon');
time.sleep(0.5)
print('* Blue Dragon');
time.sleep(0.5)
print('* Green Dragon');
time.sleep(0.5)
print('* Red Dragon');
time.sleep(0.5)
print('* White Dragon');
time.sleep(0.5)
print('* Brass Dragon');
time.sleep(0.5)
print('* Bronze Dragon');
time.sleep(0.5)
print('* Copper Dragon');
time.sleep(0.5)
print('* Gold Dragon');
time.sleep(0.5)
print('* Silver Dragon');
time.sleep(0.5)
print('* Drow');
time.sleep(0.5)
print('* Skeleton');
time.sleep(0.5)
print('* Zombie');
time.sleep(0.5)
print('* Kobolds');
print('');

time.sleep(0.5)
choice = input('Your Choice:\n')
print('')
print('')

#If they choose goblin:
if choice in ('Goblin', 'goblin', 'GOBLIN'):
    goblin.gob();
    importlib.reload(goblin);
else:
    print("This creature has not been added yet. =(");

reload = input('Reload? ')
if reload in ('Y','y','Yes','yes','YES'):
    importlib.reload(goblin)
elif reload in ('N','n','No','no','NO'):
    print('only "Y" or "Yes" accepted')
    print(reload)
else:
    print('What does that mean? =|')
print('');
print('');
