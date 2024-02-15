from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chrome WebDriver'ı başlat
driver = webdriver.Chrome()

# Web sitesini aç
driver.get()# Buraya istenen site girilmeli

# Kullanıcı adı ve şifre tanımlamalarını yapın
kullanici_adi = ""
sifre = ""

# Kullanıcı adı ve şifre alanlarına verileri girin
kullanici_adi_input = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/form/div[1]/div[2]/input")
sifre_input = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/form/div[2]/div[2]/input")

kullanici_adi_input.send_keys(kullanici_adi)
sifre_input.send_keys(sifre)

# Giriş düğmesine tıkla
giris_dugmesi = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/form/button")
giris_dugmesi.click()


time.sleep(0.5)

# Ziyaret edilecek sitelerin listesi
siteler = [

    # Diğer siteler buraya eklenmeli
]

veriler = []
eksikler = []
for site_url in siteler:
    while True:
        try:
            # Web sitesini aç
            driver.get(site_url)
            time.sleep(0.5)

            wait = WebDriverWait(driver, 1)

            efk_fk = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                "/html/body/div[5]/div[1]/main/div/div/div[3]/div[2]/div[3]/div/div[1]/div/div[2]/div/table/tbody/tr[1]/td[2]")))
            Odenmis_Sermaye = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                         "/html/body/div[5]/div[1]/main/div/div/div[3]/div[2]/div[3]/div/div[3]/div/div[2]/div/table/tbody/tr[3]/td[2]")))
            EsasFaaliyet = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                      "/html/body/div[5]/div[1]/main/div/div/div[3]/div[2]/div[1]/div/div[1]/div/div[1]/table/tbody/tr[3]/td/div[2]/div[1]")))

            efk_fk = efk_fk.text
            efk_fk = float(efk_fk.replace(',', '.'))

            Odenmis_Sermaye = Odenmis_Sermaye.text
            Odenmis_Sermaye = float(Odenmis_Sermaye.replace('.', ''))

            # Veriyi alın
            data = EsasFaaliyet.text
            data = data.split()

            # ALINAN VERİ 2000 İLE ÇARPILIYOR ALINAN VERİ ESAS FAALİYET KARI
            esas_faaliyet_kari = float(data[-1].replace('.', '')) * 2000

            fk = esas_faaliyet_kari / Odenmis_Sermaye
            efk = (esas_faaliyet_kari / Odenmis_Sermaye) * 10
            efk_fk_toplami = fk * efk_fk

            # Veriyi listeye ekleyin
            sit = site_url.split(sep='/')
            veri_metni = f"Hisse: {sit[-1]}\n" \
                         f"Esas Faaliyet: {esas_faaliyet_kari:,.2f}\n" \
                         f"Odenmiş Sermaye: {Odenmis_Sermaye:,.2f}\n" \
                         f"FK: {fk:.2f}\n" \
                         f"EFK: {efk:.2f}\n" \
                         f"EFK - F/K: {efk_fk_toplami:.2f}\n" \
                         "---------------------------------------\n"
            veriler.append(veri_metni)

            # Döngüyü kır ve bir sonraki siteye geç
            break

        except Exception as e:
            print(f"Hata: {e}")
            # XPath bulunamadı
            eksikler.append(site_url)
            break  # Bu, hata durumunda döngüyü kırarak bir sonraki siteye geçer.
print(eksikler)





# WebDriver'ı kapat
driver.quit()

# Verileri bir .txt dosyasına kaydedin
with open("veriler.txt", "w", encoding="utf-8") as dosya:
    for veri in veriler:
        dosya.write(str(veri))

dosya.close()
