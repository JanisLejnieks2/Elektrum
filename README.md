# Elektrum

## Darbības ko veic programmatūra:
1. Atver lapu apstiprina sīkdatnes un nospiež uz Pogas "Veikt maksājumu"
2. Pieprasa maksājuma nummuru, automātiski ievada šobrīd manu maksājuma nummuru, ko iespējams mainīt uz savu vai manuālu ievadi.
3. Uzrāda kāda summa ir jāmaksā, ievadot 0 vai nepareizu simbolu, norādīs kļūdu un pieprasīs ievadīt summu atkal.
4. Nospiedīs uz swedbank un veiks maksājumu.
5. Pieprasīs ievadīt savus bankas datus, arī veikta kļūdu apstrāde.

#### Programmatūras uzdevums pēc palaišanas ir automātiski ielogoties elektrum.lv mājaslapā, ievadot litotāja kodu, un uzrādot maksājuma summu.
#### Ievadot summu tālāk tiek caur swedbank veikts maksājums. Nav pievienotas citas maksājumu metodes, jo mans uzdevums bija veikt rēķina apmaksu pēc iespējas ātrāk, apstrādājot kļūdas, ja informācija tiek ievadīta nepareizi.

## Izmantotās bibliotēkas un klases:
#### Selenium
Tā ir galvenā programmatūras bibliotēka, kas ir pamats strādājot ar interneta pārlūkiem, lai manā gadijumā automatizētu procesus. No Selenium bibliotēkas tālāk tiek importētas daudzas citas noderīgas klases.
Lai programmatūra atvērtu chrome, izmantoju webdriver klasi no Selenium, manā gadījumā webdriver.Chrome() un tālāk ar driver.get(elektrum.lv) varu nokļūt uz nepieciešamo mājaslapu.
#### webdriver.ChromeOptions: (Selenium)
Klase atļauj dažādos veidos pielāgot Chrome priekš savām vajadzībām, lai meklētu informāciju, to var atvērt piemēram ar incognito, kas ir vienīgais iemesls kapēc es viņu izmantoju,
kautgan patiesībā es arī varētu iztikt bez šādas bibliotēkas.
#### Keys: (Selenium)
Keys klase nosūta ievadīto tekstu no programmas uz , izmantoju, lai uzreiz tiktu pie sava rēķina un nebūtu jāmeklē nummurs.
#### By: (Selenium)
By klase satur dažādus veidus, kā atrast nepieciešamo no mājaslapas, kas ir jānospeiž vai jāaizvad ekrānā, kā By.ID, By.XPATH, By.CLASS_NAME... Šo izmantoju katru reizi, lai
varētu darboties ar mājaslapu, lai atrastu pogas kuras jānospiež, kļūdu logus, kuri jānorāda un logus kuri jāaizpilda ar nepieciešamo informāciju.
#### WebDriverWait: (Selenium)
WebDriverWait klasi izmanto, lai sagaidītu, kad pārlūkā ir atrasts nepieciešamais, šo klasi izmantoju bieži, lai sagaidītu logus, kas parādas pēc lapas pārlādes
vai tikai pēc kļūdainas informācijas ievadīšanas. 
#### Expected conditions as EC (Selenium)
Šo klasi izmanto kopā ar WebDriverWait klasi, lai sagaidītu lauku un tad palaistu tālāk programmu, ko izmantoju meklējot kļūdu laukus mājaslapā, ja tie tur parādās.
#### time
Šo bibliotēku izmantoju savā programmatūrā, lai aizkavētu procesus lapas ielādes laikā,tādēļ brīžiem izmantoju time.sleep().

## Izmantošanas metodes:
Programmatūra izveidota šobrīd kā personīgai izmantošanai, bet jebkurš apmainot rēķina nummuru var ātrāk maksāt par elektrību, ja šādā veidā tiek maksāts.





