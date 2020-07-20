"""silindir çevre alan ve hacim hesaplama"""
PI=3.14
r=float(input("Dairenin yarıçapını giriniz: "))
a = (PI*2*r)
b = (PI*r**2)
h=float(input("Silindirin yüksekliğini giriniz: "))
c = (PI*r**2*h)
print("Dairenin çevresi= ",a,"Dairenin alanı= ",b,"Silindirin hacmi= ",c)
