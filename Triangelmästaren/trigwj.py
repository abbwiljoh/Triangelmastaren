#-----------------------------------------------------------------------------------------------------
# Program made as a tool to calculate simple trigonometry, for educational and entertainment purposes.
# (C) 2019 William Johansson, Västerås, Sweden
# Not yet released to the public
#
# email: william.johansson@abbindustrigymnasium.se
#-----------------------------------------------------------------------------------------------------

import math
#import pythagoras   
def trig():
    print('<--TRIGONOMETRON!-->')
    enhet = input('Vilken enhet vill du använda? > ')
    print('Vad vill du räkna ut?')
    vad= input('1= Vinkel 2= Längd > ')
    if int(vad) == 2:
        längd= input('1= Närliggande katet 2= Motstående katet 3= Hypotenusa > ')
        if int(längd) == 1:
            nkvinkel = input('Hur stor är vinkeln i grader? > ')
            if float(nkvinkel) >= 90:
                print('Tyvärr måste vinkeln vara under 90 grader. Försök igen')
            else:
                nkvinkelrad = math.radians(float(nkvinkel))
                nkhypotenusa = input('Hur lång är hypotenusan? > ')
                nklängd = float(nkhypotenusa)*math.cos(float(nkvinkelrad))
                Avrundatnklängd = round(nklängd, 2)
                print('Närliggande kateten är ungfär ', float(Avrundatnklängd), enhet)
        elif int(längd) == 2:
            mkvinkel = input('Hur stor är vinkeln i grader? > ')
            if float(mkvinkel) >= 90:
                print('Tyvärr måste vinkeln vara under 90. Försök igen')
            else:
                mkvinkelrad = math.radians(float(mkvinkel))
                mkhypotenusa =  input('Hur lång är hypotenusan? > ')
                mklängd = float(mkhypotenusa)*math.sin(float(mkvinkelrad))
                Avrundatmklängd = round(mklängd, 2)
                print('Motstående kateten är ungefär > ', float(Avrundatmklängd), str(enhet))
        else:
            hyvinkel = input('Hur stor är vinkeln?  ')
            hyvinkelrad = math.radians(float(hyvinkel))
            if float(hyvinkel) > 90:
                print('Tyvärr går det inte med en >90 gradig vinkel. Försök igen')
            elif float(hyvinkel) == 90:
                print('Tyvärr kan vi inte räkna med en rät vinkel. Försök igen')
            elif float(hyvinkel) < 1:
                print('Vinkeln måste vara ett positivt tal. Försök igen')
            else:
                NLelrMS = input('Vilken katet känner du till? 1= Närliggande 2= Motstående > ')
                if int(NLelrMS) == 1:
                    NLlängd = input('Hur lång är den närliggande kateten? > ')
                    nlhy = float(NLlängd)/math.cos(float(hyvinkel))
                    nlhyAvrundat = round(float(nlhy), 2)
                    print('Hypotenusan är ', nlhyAvrundat, enhet)
                else:
                    MSlängd = input('Hur lång är den motstående kateten? > ')
                    mshy = float(MSlängd)/math.sin(float(hyvinkelrad))
                    mshyAvrundat = round(float(mshy), 2)
                    print('Hypotenusan är ', mshyAvrundat, enhet)
    else:
        enhet= 'grader'
        print('Vad kan du redan?')
        vadvinkel = input('1= Närliggande + Hypotenusa  2= Motstående + Hypotenusa  3= Båda kateter  >  ')
        if int(vadvinkel) == 1:
            närkat = input('Hur lång är den närliggande kateten?  >  ')
            närhyp = input('Hur lång är hypotenusan?  >  ')
            if float(närkat) == float(närhyp):
                print('Fel')
            else:
                närvink = math.degrees(math.acos(float(närkat)/float(närhyp)))
                närvinkavr = round(float(närvink), 2)
                print('Vinkeln är ', närvinkavr, enhet)
        elif int(vadvinkel) == 2:
            motkat = input('Hur lång är den motstående kateten?  >  ')
            mothyp = input('Hur lång är hypotenusan?  >  ')
            if float(motkat) == float(mothyp):
                print('Fel')
            else:
                motvink = math.degrees(math.asin(float(motkat)/float(mothyp)))
                motvinkavr = round(float(motvink), 2)
                print('Vinkeln är ', float(motvinkavr), enhet)
        else:
            katnär = input('Hur lång är den närliggande kateten?  >  ')
            katmot = input('Hur lång är den motstående kateten  >  ')        
            katvink = math.degrees(math.atan(float(katmot)/float(katnär)))
            katvinkavr = round(float(katvink), 2)
            print('Vinkeln är ', float(katvinkavr), enhet)
    print('----------------------------------------------------------------------------------')
    print('Tack för att du använt Trigonometron')
    print('William Johansson 2019')
    print('----------------------------------------------------------------------------------')
    return
