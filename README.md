

# Lab 5: Snake
- snake spill med mulighet for å hoste sitt eget scoreboard ved hjelp av flask og noen bootstarp componeter
- behold `backend_load: false` dersom du bare ønsker spillet.


## Krav
- Python 3.12
- uib-inf100-graphics
- Flask (bare nødvednig om du skal se scoreboard)
- game_over.tff # ikke nødvindig, men anbefaler for en bedre opplevelse


## Installasjon
For å installere de nødvendige avhengighetene, kjør:
```bash
    python3 -m venv snake
    source snake/bin/activate
    pip3 install -r requirements.txt
```

## Kjøre spillet
For å starte spillet, kjør følgende kommando:
```bash
    python3 snake_main.py
```

Dersom du ønsker å start scoreboard(frivillig)
For å aktivere scoreboard, sett `backend_load: true` i `parametre.json` filen. 
```bash
    python3 scoreboard.py
```
Deretter kan du navigere til til netsiden som kommer opp i terminalen for å se.
Du finner den vanligvis på [http://127.0.0.1:5000/](http://127.0.0.1:5000/). altså din localhost og port 5000

## Spillkontroller
- Trykk `i` for å få info om kontrollerne osv.
- Trykk `q` for og avslutte


## kilder

- [https://stackoverflow.com/questions/2363731/how-to-append-a-new-row-to-an-old-csv-file-in-python](https://stackoverflow.com/questions/2363731/how-to-append-a-new-row-to-an-old-csv-file-in-python) 

Tok litt inspiasjon herfra for å se hvordan forspørsler ble håndtert osv.
- [https://github.com/vindruid/flask_leaderboard](https://github.com/vindruid/flask_leaderboard)
- [https://www.geeksforgeeks.org/uploading-and-reading-a-csv-file-in-flask/](https://www.geeksforgeeks.org/uploading-and-reading-a-csv-file-in-flask/)
- [https://youtu.be/SLftzEqoLPk?si=JbVaNlXtv0wa-157](https://youtu.be/SLftzEqoLPk?si=JbVaNlXtv0wa-157)

For å lage tablet der vi ser scoreboardet 
- [https://getbootstrap.com/docs/4.1/content/tables/](https://getbootstrap.com/docs/4.1/content/tables/)

For og sortere csv filene.
- [https://stackoverflow.com/questions/2100353/sort-csv-by-column](https://stackoverflow.com/questions/2100353/sort-csv-by-column)

Fonten jeg bukte
- [Font: game_over.tff](https://www.dafont.com/game-over.font)





