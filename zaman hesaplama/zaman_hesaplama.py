# bu uygulama input olarak bir rakam alacak ve aldığı rakamın kaç gün kaç dakika saat ve saniye olduğunu yazdıracak


toplam_saniye = int(input("Hesaplanmasını istediğiniz sayıyı giriniz : "))

gun = toplam_saniye // 86400
kalan_saniye = toplam_saniye % 86400

saat = kalan_saniye // 3600
kalan_saniye %= kalan_saniye % 3600

dakika = kalan_saniye // 60
kalan_saniye %= 60

print("Verdiğiniz sayı ---> Gün : {}  Dakika : {}  Saat : {}  saniye : {}".format(gun,dakika,saat,kalan_saniye))
