

# Lab 5: Snake
- snake spill med mulighet for å hoste sitt egen scoreboard ved hjelp av flask og noen bootstarp componeter
- behold `backend_load: false` dersom du bare ønsker spillet.


## Krav
- Python 3.12
- Pygame uib-inf100-graphics 
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

dersom du ønsker å start scoreboard(frivillig)
For å aktivere scoreboard, sett `backend_load: true` i `parametre.json` filen. 
```bash
    python3 scoreboard.py
```

## Spillkontroller
- Trykk `i` for å få info om kontrollerne osv.
- Trykk `q` for og avslutte


## kilder
- [https://stackoverflow.com/questions/2363731/how-to-append-a-new-row-to-an-old-csv-file-in-python](https://stackoverflow.com/questions/2363731/how-to-append-a-new-row-to-an-old-csv-file-in-python) 

tok litt insp herfra for å se hvordan forspørsler ble håndtert osv.
- [https://github.com/vindruid/flask_leaderboard](https://github.com/vindruid/flask_leaderboard)
- [https://www.geeksforgeeks.org/uploading-and-reading-a-csv-file-in-flask/](https://www.geeksforgeeks.org/uploading-and-reading-a-csv-file-in-flask/)
for å lage tablet der vi ser scoreboardet 
- [https://getbootstrap.com/docs/4.1/content/tables/](https://getbootstrap.com/docs/4.1/content/tables/)






