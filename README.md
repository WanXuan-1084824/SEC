# Security & Cyberwarfare Week 5 - Encryptie
## 1. Hoe werkt de applicatie?
Ik heb een applicatie gemaakt in Python waarmee je ingevoerde input kunt versleutelen en ontsleutelen. 

Wanneer de applicatie wordt gestart, wordt er automatisch een geheime sleutel aangemaakt. De gebruiker kan een bericht invoeren dat wordt versleuteld en naar het klembord gekopieerd. Daarna kan het versleutelde bericht weer ontsleuteld worden met dezelfde sleutel. Als dat mislukt, verschijnt er een foutmelding.


## 2. Gebruikte encryptiemethoden en algoritme
Mijn applicatie maakt gebruik van symmetrische encryptie, dezelfde geheime sleutel wordt gebruikt om bericht te versleutelen en te ontsleutelen.

Er zijn twee soorten encryptie:
1. **Symmestrische encryptie**: dezelfde sleutel voor versleutelen en ontsleutelen
2. **Asymmetrische encryptie**: twee verschillende sleutels; pulic key en private key

Ik gebruik AES-128 en HMAC--SHA256 via de bibliotheek Fernet in Python voor mijn applicatie. AES-128 zorgt ervoor dat andere mensen de berichten niet ziet en HMAC-SHA256 controleert of het bericht niet is veranderd. Ik heb voor Fernet gekozen, omdat het makkelijk te gebruiken is en de beveiliging al voor mij doet, hierdoor hoef ik niet alles te programmeren en zo de kans op fouten verminderd.


## 3. Beheer en beveiliging van de geheime sleutel
**Genereren**:
Met Fernet.generate_key() wordt er automatisch een willekeurig geheime sleutel gemaakt.

**Opslaan**:
De sleutel wordt alleen tijdens het gebruik van de applicatie bewaard. Als de applicatie wordt afgesloten, raak je de sleutel kwijt. Bij opnieuw opstarten wordt een nieuwe sleutel aangemaakt daardoor kan je oude bericht niet meer ontsleutelen.

**Uitwisselen**:
Deze applicatie kan nog niet de sleutel veilig delen met anderen. Een oplossing ervan kan zijn: wachtwoord gebruiken om sleutel te maken, dit kan met KDF (PBKDF2/Argon2id).

**Beveiligingsrisico's**
- **sleutel kwijtraken**: kan oude bericht niet meer lezen na applicatie afsluiten want bij opstarten van applicatie wordt elke keer een nieuwe sleutel aangemaakt.
- **Elke gebruiker een eigen sleutel geven**: iedereen krijgt dan een andere sleutel. Als één sleutel uitlekt, hebben een andere gebruikers geen last ervan. 


## 4. Reflecteren
Mijn applicatie past bij de Kerckhoffs's Principe;beveiligssysteem moet veilig blijven, ook al weer iedereen hoe het systeem werkt. De sleutel moet geheim blijven, omdat iedereen mag weten hoe mijn applicatie werkt en welke encryptiemethode ik gebruik. En zonder de sleutel kunnen ingevoerde input niet gelezen worden.

Nadeel van mijn applicatie is bij iedere opstart wordt een nieuwe sleutel gemaakt, dit maakt oude bericht ontsleutelen en sleutel delen met anderen lastig.
