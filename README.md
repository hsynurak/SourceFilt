# SourceFilt
 
Bu proje benim django eğitimim sonrasında yaptığım ilk projem. Arkdaşlarım tarafından hazırlanan frontend tasarımını kullanarak backend geliştirmelerini yapıyorum.

commit-1: Dağınık olarak gelen HTML-CSS-JS dosyalarının dosya düzenlerini ve bağlantılarını django ya uygun hale getirdim
commit-2: Anasayfa ve hakkında sayfalarını oluşturan tekrarlı kodları döngü içine almak için modelleri kullandım ve static veri yapısı ile görsellere erişim sağladım
commit-3: Kaynak havuzu sayfasını veritabanı üzerinden çekilecek olan verileri kullanıma el verişli hale getirdim.



Notlar:
account/views.py içinde "login_request" fonksiyonu ile login kontrolü sağlanır

account/views.py içinde "register_request" fonksiyonu ile yeni kullanıcı oluşturulur

account/views.py içinde "logout_request" fonksiyonu ile logout işlemi devreye sokulur

mainapp/views.py içinde "contact" fonksiyonu ile girilen bilgiler veri tabanına kayıt edilir
