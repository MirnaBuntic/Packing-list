# Packing List – Python 

Packing List er et enkelt konsollbasert program utviklet i Python. Programmet lar brukeren opprette og administrere en pakkeliste i forbindelse med reiser og ferier.

Prosjektet er laget for å øve på grunnleggende programmering i Python, med fokus på **lister, løkker, betingelser og brukerinteraksjon**.

## Teknologier

- **Python** – Programmeringsspråket som brukes til å utvikle applikasjonen.
- **Terminal/konsoll** – Brukes for å kommunisere med programmet gjennom tekstbaserte kommandoer.

## Funksjonalitet

Programmet gir brukeren mulighet til å administrere en pakkeliste gjennom fire kommandoer:

- **add** – Legg til ett eller flere elementer i pakkelisten.
- **delete** – Fjern elementer fra pakkelisten.
- **print** – Vis alle elementene i pakkelisten.
- **exit** – Avslutt programmet.

Brukeren kan legge til eller fjerne flere elementer etter hverandre ved å skrive `done` når handlingen er fullført.

Programmet kontrollerer også om et element finnes i listen før det slettes, og gir tilbakemelding dersom elementet ikke blir funnet.

## Hvordan programmet fungerer

Programmet benytter en `while True`-løkke som holder applikasjonen aktiv frem til brukeren velger å avslutte.

Brukerens input behandles med `.lower()` for å gjøre kommandoene uavhengige av store og små bokstaver.

Elementene lagres i en Python-liste (`packingList`), der metodene `.append()` og `.remove()` brukes til å legge til og fjerne innhold.

Betingelser (`if`, `elif` og `else`) brukes for å håndtere de forskjellige kommandoene og gi brukeren relevante tilbakemeldinger.

## Hva jeg har lært

Gjennom dette prosjektet har jeg fått praktisk erfaring med grunnleggende programmeringskonsepter i Python, blant annet:

- Bruk av lister og listemetoder.
- Løkker og kontroll av programflyt.
- Betingelser og logiske sammenligninger.
- Håndtering av brukerinput.
- Utvikling av en enkel interaktiv konsollapplikasjon.

## Videreutvikling

Programmet er en enkel versjon av en pakkeliste, og det finnes flere muligheter for videreutvikling.

Eksempler på dette er å lagre listen i en fil, markere elementer som ferdig pakket eller utvikle et grafisk brukergrensesnitt.

Foreløpig lagres pakkelisten kun mens programmet kjører, og innholdet forsvinner når programmet avsluttes.
