from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chrome WebDriver'ı başlat
driver = webdriver.Chrome()

# Web sitesini aç
driver.get("https://fintables.com/auth/login")

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
"https://fintables.com/sirketler/THYAO",
    "https://fintables.com/sirketler/TAVHL",
    "https://fintables.com/sirketler/RYSAS",
    "https://fintables.com/sirketler/CLEBI",
    "https://fintables.com/sirketler/LIDER",
    "https://fintables.com/sirketler/PGSUS",
    "https://fintables.com/sirketler/TUREX",
    "https://fintables.com/sirketler/PKENT",
    "https://fintables.com/sirketler/GRSEL",
    "https://fintables.com/sirketler/AYCES",
    "https://fintables.com/sirketler/INGRM",
    "https://fintables.com/sirketler/SOKM",
    "https://fintables.com/sirketler/MGROS",
    "https://fintables.com/sirketler/TKNSA",
    "https://fintables.com/sirketler/DOAS",
    "https://fintables.com/sirketler/BIMAS",
    "https://fintables.com/sirketler/SUWEN",
    "https://fintables.com/sirketler/MAVI",
    "https://fintables.com/sirketler/VAKKO",
    "https://fintables.com/sirketler/PENTA",
    "https://fintables.com/sirketler/AZTEK",
    "https://fintables.com/sirketler/BUCIM",
    "https://fintables.com/sirketler/OYAKC",
    "https://fintables.com/sirketler/CIMSA",
    "https://fintables.com/sirketler/BOBET",
    "https://fintables.com/sirketler/AKCNS",
    "https://fintables.com/sirketler/TURSG",
    "https://fintables.com/sirketler/AKGRT",
    "https://fintables.com/sirketler/ANSGR",
    "https://fintables.com/sirketler/SDTTR",
    "https://fintables.com/sirketler/OTKAR",
    "https://fintables.com/sirketler/ASELS",
    "https://fintables.com/sirketler/EGEEN",
    "https://fintables.com/sirketler/GOODY",
    "https://fintables.com/sirketler/BRISA",
    "https://fintables.com/sirketler/TTRAK",
    "https://fintables.com/sirketler/TOASO",
    "https://fintables.com/sirketler/OTKAR",
    "https://fintables.com/sirketler/KARSN",
    "https://fintables.com/sirketler/FROTO",
    "https://fintables.com/sirketler/ASUZU",
    "https://fintables.com/sirketler/EUREN",
    "https://fintables.com/sirketler/YATAS",
    "https://fintables.com/sirketler/VESBE",
    "https://fintables.com/sirketler/SARKY",
    "https://fintables.com/sirketler/CVKMD",
    "https://fintables.com/sirketler/KOZAL",
    "https://fintables.com/sirketler/KOZAA",
    "https://fintables.com/sirketler/GUBRF",
    "https://fintables.com/sirketler/AYGAZ",
    "https://fintables.com/sirketler/SISE",
    "https://fintables.com/sirketler/AKSA",
    "https://fintables.com/sirketler/KLKIM",
    "https://fintables.com/sirketler/PETKM",
    "https://fintables.com/sirketler/BRISA",
    "https://fintables.com/sirketler/TUPRS",
    "https://fintables.com/sirketler/HEKTS",
    "https://fintables.com/sirketler/ENKAI",
    "https://fintables.com/sirketler/GESAN",
    "https://fintables.com/sirketler/KCAER",
    "https://fintables.com/sirketler/BRSAN",
    "https://fintables.com/sirketler/BFREN",
    "https://fintables.com/sirketler/ARCLK",
    "https://fintables.com/sirketler/ADEL",
    "https://fintables.com/sirketler/DOKTA",
    "https://fintables.com/sirketler/KORDS",
    "https://fintables.com/sirketler/GENIL",
    "https://fintables.com/sirketler/SELEC",
    "https://fintables.com/sirketler/MPARK",
    "https://fintables.com/sirketler/ECILC",
    "https://fintables.com/sirketler/TKFEN",
    "https://fintables.com/sirketler/SAHOL",
    "https://fintables.com/sirketler/AGHOL",
    "https://fintables.com/sirketler/KCHOL",
    "https://fintables.com/sirketler/BRYAT",
    "https://fintables.com/sirketler/ALARK",
    "https://fintables.com/sirketler/DOHOL",
    "https://fintables.com/sirketler/KRONT",
    "https://fintables.com/sirketler/TTKOM",
    "https://fintables.com/sirketler/TCELL",
    "https://fintables.com/sirketler/ISGSY",
    "https://fintables.com/sirketler/CCOLA",
    "https://fintables.com/sirketler/TBORG",
    "https://fintables.com/sirketler/TUKAS",
    "https://fintables.com/sirketler/BANVT",
    "https://fintables.com/sirketler/ELITE",
    "https://fintables.com/sirketler/GOKNR",
    "https://fintables.com/sirketler/SOKE",
    "https://fintables.com/sirketler/YYLGD",
    "https://fintables.com/sirketler/KENT",
    "https://fintables.com/sirketler/AEFES",
    "https://fintables.com/sirketler/ULKER",
    "https://fintables.com/sirketler/TRGYO",
    "https://fintables.com/sirketler/ZRGYO",
    "https://fintables.com/sirketler/EKGYO",
    "https://fintables.com/sirketler/SRVGY",
    "https://fintables.com/sirketler/HLGYO",
    "https://fintables.com/sirketler/ISGYO",
    "https://fintables.com/sirketler/AHGAZ",
    "https://fintables.com/sirketler/AKFYE",
    "https://fintables.com/sirketler/AKSEN",
    "https://fintables.com/sirketler/ENJSA",
    "https://fintables.com/sirketler/NATEN",
    "https://fintables.com/sirketler/ODAS",
    "https://fintables.com/sirketler/GWIND",
    "https://fintables.com/sirketler/ZOREN",
    "https://fintables.com/sirketler/BASGZ",
    "https://fintables.com/sirketler/CANTE",
    "https://fintables.com/sirketler/KONTR",
    "https://fintables.com/sirketler/GESAN",
    "https://fintables.com/sirketler/CWENE",
    "https://fintables.com/sirketler/EUPWR",
    "https://fintables.com/sirketler/ASTOR",
    "https://fintables.com/sirketler/ALFAS",
    "https://fintables.com/sirketler/SMRTG",
    "https://fintables.com/sirketler/ANHYT",
    "https://fintables.com/sirketler/MACKO",
    "https://fintables.com/sirketler/KLSER",
    "https://fintables.com/sirketler/QUAGR",
    "https://fintables.com/sirketler/AZTEK",
    "https://fintables.com/sirketler/MIATK",
    "https://fintables.com/sirketler/LOGO",
    "https://fintables.com/sirketler/FORTE",
    "https://fintables.com/sirketler/KLNMA",
    "https://fintables.com/sirketler/TSKB",
    "https://fintables.com/sirketler/VAKBN",
    "https://fintables.com/sirketler/QNBFB",
    "https://fintables.com/sirketler/ISCTR",
    "https://fintables.com/sirketler/HALKB",
    "https://fintables.com/sirketler/GARAN",
    "https://fintables.com/sirketler/YKBNK",
    "https://fintables.com/sirketler/AKBNK",
    "https://fintables.com/sirketler/OYYAT",
    "https://fintables.com/sirketler/A1CAP",
    "https://fintables.com/sirketler/TERA",
    "https://fintables.com/sirketler/ISMEN",
    "https://fintables.com/sirketler/INFO",
    "https://fintables.com/sirketler/GEDIK",
    "https://fintables.com/sirketler/KCAER",
    "https://fintables.com/sirketler/POLTK",
    "https://fintables.com/sirketler/KRDMD",
    "https://fintables.com/sirketler/EREGL"
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
