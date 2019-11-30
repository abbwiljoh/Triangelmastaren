#-------------------------------------------------------------------------------------------------------------------
# Tool for calclating angles and lengths of 90 degree triangles using trigonometry and the pythagorean theorem.
# (C) 2019 William Johansson, Västerås, Sweden
# 
# email: william.johansson@abbindustrigymnasium.se
#-------------------------------------------------------------------------------------------------------------------
import math
import trigwj as tr
import pythagoras as pyt

print('<---------------------------TRIANGELMÄSTAREN!--------------------------->')
print('Välkommen till Triangelmästaren, där trianglarna är räta och svaren rätt!')
print('')
print('Vad vill du räkna med? Svara med motsvarande siffra.')
calcvad= input('1= Pythagoras sats  2= Trigonometri  3= Vad är skillnaden?  > ')
if int(calcvad) == 1:
    print('')
    pyt.pythagoras()
elif int(calcvad) == 2:
    print('')
    tr.trig()
else:
    print('Har triangeln en rät vinkel?')
    osäkervad= input('1= Ja  2= Nej  > ')
    if int(osäkervad) == 2:
        print('')
        print('Tyvärr kan det här programmet bara räkna med rätvinkliga trianglar. Lycka till ändå')
    else:
        print('Vad känner du till om triangeln?')
        PytOrTrig= input('1= Två längdmått  2= Ett längdmått, en vinkel  3= Bara att den är rätvinklig  > ')
        if int(PytOrTrig) == 3:
            print('')
            print('Det finns inte mycket detta program kan göra för dig då, men vet bara att:')
            print('a^2 + b^2 = c^2')
            print('a och b är kateter och c är hypotenusan')
            print('')
            print('Lycka till ändå!')
        elif int(PytOrTrig) == 2:
            print('Då ska du använda trigonometri! Vill du använda det nu?')
            villanvända = input('1= Ja  2= Nej  > ')
            if int(villanvända) == 1:
                print('')
                tr.trig()
            else: 
                print('Okej, lycka till ändå!')
        else:
            print('Då kan du använda pythagoras sats! Vill du använda det nu?')
            villanvända2 = input('1= Ja  2= Nej  > ')
            if int(villanvända2) == 1:
                print('')
                pyt.pythagoras()
            else: 
                print('Okej, lycka till ändå!')

print('')
print('<---------------------------TRIANGELMÄSTAREN!--------------------------->')
print('')
print('Tack för att du använt Triangelmästaren! ')
print('Av William Johansson 2019 med Python och modulen Python Math')