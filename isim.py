"""isimli birşeyler"""
isim=str(input("İsminizi giriniz: "))
if (isim ==str('solmazgul' and 'smg')):
    print("Adamsın!")
elif (isim != (int) ):
    print("İsim diyoruz sayı giriyorsun?!")
a=int(input('''Seçenekler:
1. İsminiz büyük harfle yazılır. 
2. İsminiz küçük harfle yazılır.
3. İsminizdeki harfler büyükse küçük, küçükse büyük yazılır. '''))
if a==1:
    print(str.upper(isim))
elif a==2:
    print(str.lower(isim))
elif a==3:
    print(str.swapcase(isim))
#elif a==4:
    #b = 'Başgan'
    #print(isim.join("Başgan"))
