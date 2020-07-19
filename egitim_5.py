"""asdfas"""
skor = int(input("Skorunuzu giriniz: "))
if skor >= 90:
    print("Kazandınız!!")
    skor = skor+2
elif skor >= 80:
    print("Aferin!")
elif skor < 50:
    print(skor-20)
else:
    print("Kaybettiniz :(")
