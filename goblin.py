import random
def gob():
    #generate the names
    goblin_names = ('Xoict','Aag','Tiak','Hebrit','Brarvoikx','Glaarm','Kralx','Fubtard','Teesmoz','Streanierd','Brots','Prakx','Creard','Agsoq','Wissysz','Bluk','Cleaz','Ekiats','Gniatmex','Gledurx');        goblinNameGen = random.choice(goblin_names);
    print("Name: "+ goblinNameGen)
    print('')

    #generate the armor class
    goblinAC = ('15(Leather Armor[11+Dex] and Sheild[+2])','15(Leather Armor[11+Dex] and Sheild[+2]','15(Leather Armor[11+Dex] and Sheild[+2]','15(Leather Armor[11+Dex] and Sheild[+2]','16(Studded Leather Armor[12+Dex] and Sheild[+2]','15(Padded Armor[11+Dex] and Sheild[+2]and Disadvantage on Stealth)');
    goblinACGen = random.choice(goblinAC);
    print("AC: " + goblinACGen)
    print('');

    #generate hitpoints
    goblinHP = ('2','2','3','3','3','3','4','4','4','4','4','4','5','5','5','5','5','5','5','5','5','6','6','6','6','6','6','6','6','6','6','6','6','6','6','7','7','7','7','7','7','7','7','7','7','7','7','7','7','7','7','7','8','8','8','8','8','8','8','8','8','8','8','8','8','8','9','9','9','9','9','9','9','9','9','9','9','10','10','10','10','10','10','10','10','11','11','11','11','11','11','12','12','12');
    goblinHPGen = random.choice(goblinHP);
    print("HP: " + goblinHPGen);
    print('');

    #shows speed
    print('Speed: 30ft');
    print('');

    #Shows Ability Scores
    print('Str:  8 (-1)' + '    ' + 'Dex:  14 (+2)' + '    ' + 'Con:  10 (+0)' + '    ' + 'Int:  10 (+0)' + '    ' + 'Wis:  8(-1)' + '    ' + 'Cha:  8 (-1)');
    print('');

    #Shows Proficiencies
    print('Skills: Stealth +6');
    print('Senses: darkvision 60ft., passive Perception 9');
    print('Languages: Common, Goblin');
    print('Challenge: 1/4 (50 XP)')
    print('');

    #Shows Actions
    print('Scimitar. Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) slashing damage. ');
    print('Shortbow: Ranged Weapon Attack, +4 to hit, range 80f/320 ft., one target. Hit: 5 (1d6 + 2) piercing damag');

    #Shows Secondary Information
    print('Nimble Escape: The goblin can take the Disengage or Hide action as a bonus action on each of its turns.');