# Asennusohje

## Sovelluksen paikallinen asennus

1. Asenna tarvittaessa seuraavat työvälineet:

   - git työkalu <https://git-scm.com/>
   - Python 3.5 tai uudempi versio <https://www.python.org/downloads/>

2. Siirry komentorivillä (terminal/Command Prompt) kansioon, johon luodaan kansio sovelluksen paikalliselle versiolle.

3. Varmista että seuraavat komennot toimivat komentoriviltä:

   ```bash
   git --version
   python --version
   ```

4. Annan komentoriviltä seuraavat komennot:

   ```bash
   git clone git@github.com:isopoju/tyoaikaseuranta.git
   cd tyoaikaseuranta
   python -m venv venv
   source venv/bin/activate
     tai Windows koneella: venv\Scripts\activate.bat
   pip install -r requirements.txt
   python run.py
   ```

5. Sovellus käynnistyy osoitteeseen: <http://localhost:5000/>

6. Rekisteröi sovellukseen pääkäyttäjä, jonka käyttäjätunnus on admin.

7. Sovelluksen tietokanta on tyoaikaseuranta\application\database.db tiedostossa ja voit tarkastella sen sisältöä tarvittaessa sqlite3 työkalulla <https://www.sqlite.org/download.html>.

## Paikallisen sovelluksen asennus Heroku pilvipalveluun

1. Tarvitset tunnuksen Heroku pilvipalveluun.

2. Asenna tarvittaessa seuraavat työvälineet:

   - Heroku CLI <https://devcenter.heroku.com/articles/heroku-cli>

3. Varmista että seuraavat komennot toimivat komentoriviltä:

   ```bash
   heroku --version
   ```

4. Siirry komentorivillä tyoaikaseuranta kansioon ja anna seuraavat komennot:

   ```bash
   heroku create heroku-nimi
      Huom! sovelluksen osoite: https://heroku-nimi.herokuapp.com/
   heroku config:set HEROKU=1
   heroku addons:add heroku-postgresql:hobby-dev
   git push heroku master
   ```

5. Rekisteröi sovellukseen pääkäyttäjä, jonka käyttäjätunnus on admin.
