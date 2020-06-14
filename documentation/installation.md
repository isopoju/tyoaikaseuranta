# Asennusohjeet

## Sovelluksen paikallinen asennus

1. Asenna tarvittaessa seuraavat työvälineet:
- git työkalu (https://git-scm.com/)
- Python 3.5 tai uudempi versio ( https://www.python.org/downloads/)

2. Siirry komentorivillä (terminal/Command Prompt) kansioon, johon luodaan kansio sovelluksen paikalliselle versiolle.

3. Varmista että seuraavat komennot toimivat komentoriviltä:
```
git --version
python --version
```
4. Annan komentoriviltä seuraavat komennot:
```
git clone git@github.com:isopoju/tyoaikaseuranta.git
cd tyoaikaseuranta
python -m venv venv
source venv/bin/activate
  tai Windows koneella: venv\Scripts\activate.bat
pip install -r requirements.txt
python run.py
```
5. Sovellus käynnistyy osoitteeseen: http://localhost:5000/

6. Sovelluksen tietokanta on tyoaikaseuranta\application\database.db tiedostossa ja voit tarkastella sen sisältöä tarvittaessa sqlite3 työkalulla (https://www.sqlite.org/download.html).


## Sovelluksen asennus Heroku pilvipalveluun

1. Tarvitset tunnuksen Heroku pilvipalveluun.

2. Asenna tarvittaessa seuraavat työvälineet:
Heroku CLI (https://devcenter.heroku.com/articles/heroku-cli)

3. Varmista että seuraavat komennot toimivat komentoriviltä:
```
heroku --version
```
4. Siirry komentorivillä tyoaikaseuranta kansioon ja anna seuraavat komennot:
```
heroku create nimi-herokussa
  Huom! sovelluksen osoite: https://nimi-herokussa.herokuapp.com/
heroku config:set HEROKU=1
heroku addons:add heroku-postgresql:tyoaikaseuranta-dev
git push heroku master
```

TODO: Lisää tietokantojen konfigurointi / SQL skriptit
