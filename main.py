#Liste Anlayışı Ek Uygulama: "Gürültülü" Veriyi Filtreleme
#Senaryo:
#Bir sensörden veya bir veri akışından sürekli veri alıyorsunuz. Ancak bu verinin içinde bazen "gürültü" (noise) olarak adlandırdığımız, beklenenden çok yüksek veya çok düşük değerler olabiliyor. Yapay Zeka modellerini eğitmeden önce bu gürültülü veriyi temizlemek (filtrelemek) çok önemlidir.

#Görev:

#sensor_okumalari adında bir liste oluşturun. İçine hem makul değerler hem de birkaç tane çok düşük (örneğin 0'dan küçük) veya çok yüksek (örneğin 1000'den büyük) sayı içeren en az 10-15 tane rastgele tam sayı değeri ekleyin. (Örn: [250, 45, -10, 780, 1500, 300, 5, 950, 10, 1100, 600, -50, 400])
sensor_okumalari = [250, 45, -10, 780, 1500, 300, 5, 950, 10, 1100, 600, -50, 400, 1001, -100, 1000, 500, 100, 1000, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100,]


#temizlenmis_okumalar adında yeni bir liste oluşturun. Bu liste, sensor_okumalari içindeki, 0 ile 1000 (dahil) aralığında olmayan tüm "gürültülü" değerleri içermemelidir. Yani, sadece 0 ile 1000 arasındaki değerleri içeren yeni bir liste oluşturmalısınız. Bu işlemi liste anlayışı kullanarak yapın. temiz_veri for temiz_veri in sensor_okumalari if temiz_veri <= 1000 and temiz_veri >= 0
temizlenmis_okumalar = [temiz_veri for temiz_veri in sensor_okumalari if temiz_veri <= 1000 and temiz_veri >= 0]


#temizlenmis_okumalar listesini ekrana yazdırın.
print(f"Temizlenmiş veri (0 - 1000 arası) = {temizlenmis_okumalar}")


#Orijinal sensor_okumalari listesindeki maksimum ve minimum değeri ekrana yazdırın.
max_sensor_okumasi = (max(sensor_okumalari))
min_sensor_okumasi = (min(sensor_okumalari))

#temizlenmis_okumalar listesindeki maksimum ve minimum değeri ekrana yazdırın. Bu karşılaştırma, temizleme işleminin etkisini görmenizi sağlayacak.
print(f"Sensor okumalarının max değeri = {max_sensor_okumasi}")
print(f"Sensor okumalarının min değeri = {min_sensor_okumasi}")
