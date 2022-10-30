print("Sıcaklık birimleri çevirme programına hoşgeldiniz")
print("*****************************************")
print("Fahrenheite dönüştürmek için 1'e basınız.\n"
      "Celciusa dönüştürmek için 2'ye basınız.\n"
      "Kelvin dönüştürmek için 3'e basınız.")
print("*****************************************")

derece=int(input("Lütfen çevirmek istediğiniz sıcaklığı giriniz="))
secim=int(input("Lütfen dönüştürmek istediğiniz sıcaklık birimini giriniz="))

if secim==1:
    print("**********************************")
    print("Kelvinden, Fahrenheite çevirmek için A'ya basınız.\n"
          "Celciusdan, Fahrenheite çevirmek için B'ye basınız")
    sicakdonussecim=input("Seçim=")
    print("**********************************")
    if sicakdonussecim=='A':
        F=(9/5)*(derece-273)+32
        print(f"Kelvin sıcaklığın, Fahrenheit cinsinden değeri:{F}")
    elif sicakdonussecim=='B':
        F=((derece*9)/5)+32
        print(f"Celcius sıcaklığın, Fahrenheit cinsinden değeri:{F}")
    else:
        print("Yanlış girdiniz tekrar deneyiniz.")

if secim==2:
    print("**********************************")
    print("Fahrenheit'den, Celcius'a çevirmek için C'ye basınız\n"
          "Kelvin'den, Celciusa çevirmek için D'ye basınız.")
    sicakdonussecim = input("Seçim=")
    print("**********************************")
    if sicakdonussecim=='C':
        C=((derece-32)*5)/9
        print(f"Fahrneheit sıcaklığın, Celcius karşılığı={C}")
    elif sicakdonussecim=='D':
        C=derece-273.15
        print(f"Kelvin sıcaklığın, Celcius karşılığı={C}")
    else:
        print("Yanlış girdiniz tekrar deneyiniz.")

if secim==3:
    print("**********************************")
    print("Fahrenheit'den, Kelvine çevirmek için E'ye basınız\n"
          "Celcius'dan, Kelvine çevirmek için F'ye basınız ")
    sicakdonussecim=input("Seçim=")
    print("**********************************")
    if sicakdonussecim=='E':
        K=((5*(derece-32))/9)+273.15
        print(f"Fahrenheit sıcaklığın, Kelvin karşılığı={K}")
    elif sicakdonussecim=='F':
        K=derece+273.15
        print(f"Celcius sıcaklığın, Kelvin karşılığı={K}")
    else:
        print("Yanlış girdiniz tekrar deneyiniz.")

print("Dönüştürme işlemi bitmiştir")













