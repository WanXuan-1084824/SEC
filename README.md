# Security & Cyberwarfare Week 5 - Encryptie

1. Hoe werkt de applicatie?
Ik heb een applicatie gemaakt in Python waarmee je ingevoerde input kunt versleutelen en ontsleutelen. 

Wanneer de applicatie wordt gestart, wordt er automatisch een geheime sleutel aangemaakt. De gebruiker kan een bericht invoeren dat wordt versleuteld en naar het klembord gekopieerd. Daarna kan het versleutelde bericht weer ontsleuteld worden met dezelfde sleutel. Als dat mislukt, verschijnt er een foutmelding.

2. Gebruikte encryptiemethoden en algoritme
Mijn applicatie maakt gebruik van symmetrische encryptie, dezelfde geheime sleutel wordt gebruikt om bericht te versleutelen en te ontsleutelen.

Er zijn twee soorten encryptie:
    1. Symmestrische encryptie: dezelfde sleutel voor versleutelen en ontsleutelen
    2. Asymmetrische encryptie: twee verschillende sleutels; pulic key en private key

Ik gebruik AES-128 en HMAC--SHA256 via de bibliotheek Fernet in Python voor mijn applicatie. AES-128 zorgt ervoor dat andere mensen de berichten niet ziet en HMAC-SHA256 controleert of het bericht niet is veranderd. Ik heb voor Fernet gekozen, omdat het makkelijk te gebruiken is en de beveiliging al voor mij doet, hierdoor hoef ik niet alles te programmeren en zo de kans op fouten verminderd.