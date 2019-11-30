import math
def pythagoras():
    print('<--Pythagoras-->')
    print('Skriv din enhet')
    enhet = input()

    print('Vad vill du räkna ut?')
    print('1= Hypotenusa')
    print('2= Katet')
    okänd=input()

    if int(okänd) == 2:
        print('Längd på hypotenusa:')
        hyp = input()
        print('Längd på ena kateten:')
        kat = input()
        if float(kat) > float(hyp):
            print('Lek inte med döden...')
        elif float(hyp) == float(kat):
            print('Du tror att du är rolig nu va?')
        else:
            print(float(hyp), '^2','- x^2 = ' , float(kat),'^2' )
            b = math.sqrt(float(hyp)**2-float(kat)**2)
            print('Kateten är ', float(b), enhet)
        

    elif int(okänd) == 1:
        print('Längd på första kateten:')
        kat1 = input()
        print('Längd på andra kateten:')
        kat2 = input()
        print(float(kat1), '^2 +', float(kat2), '^2 = c^2')
        c = math.sqrt(float(kat1)**2 + float(kat2)**2)
        print('Längden på hypotenusan är', float(c), enhet)
    return