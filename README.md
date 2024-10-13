# Encryptie/Decryptie App

Een command-line applicatie in Python voor het versleutelen en ontsleutelen van simpele tekst met symmetrische encryptie, deze app maakt gebruik van de `cryptography`-bibliotheek.

## Encryptiemethode

De app maakt gebruik van **Fernet symmetrische encryptie**.
Fernet zorgt ervoor dat de versleutelde boodschap niet kan worden gemanipuleerd of gelezen zonder de juiste sleutel. 
Het is gebaseerd op **AES-encryptie in CBC-modus met een 128-bits sleutel** en maakt ook gebruik van **HMAC (Hash-based Message Authentication Code)** voor integriteitscontrole.

## Functionaliteiten
- **Symmetrische Encryptie** met Fernet (AES in CBC-modus met HMAC voor integriteit).
- **Versleutelen en Ontsleutelen** van tekst via een geheime sleutel.




## Installatie

1. Installeer de benodigde bibliotheek:

    ```bash
    pip install cryptography
    ```

2. Start de app:

    ```bash
    python app.py
    ```

## Gebruik

- **Encryptie**: Voer `e` in, geef de tekst, en ontvang de versleutelde tekst.
- **Decryptie**: Voer `d` in, geef de versleutelde tekst, en ontvang de ontsleutelde tekst.
- De geheime sleutel wordt automatisch gegenereerd en opgeslagen in `secret.key`.
