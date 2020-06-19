# Käyttäjätarinat

Sovellukseen on toteutettu seuraavat käyttäjätarinat.

## Vierailija

- voi listata sovellukseen perustetut projektit
- voi rekisteröityä käyttäjäksi

## Rekisteröitynyt käyttäjä

- voi kirjautua sovellukseen
- voi liittyä olemassa olevaan projektiin tuntikirjaajaksi
- voi perustaa uuden projektin, jolloin hänestä tulee projektin omistaja

## Tuntikirjaaja

- voi tehdä tuntikirjauksia projekteihin, joihin hän on liittynyt
- voi listata, muokata ja poistaa omia tuntikirjauksia
- saa yhteenvetoraportin kaikista tekemistään tuntikirjauksista

```sql
SELECT Project.id, Project.name, sum(Workload.hours) FROM Project
LEFT JOIN Workload ON Workload.project_id = Project.id
WHERE Workload.worker_id = current_user.id
GROUP BY Project.id
ORDER BY Project.name
```

## Projektin omistaja

- voi muokata tai poistaa omistamiaan projekteja
- saa tarvittaessa yhteenvetoraportin projektiin tehdyistä tuntikirjauksista

```sql
SELECT Account.name, sum(Workload.hours) FROM Account
LEFT JOIN Workload ON Workload.worker_id = Account.id
WHERE Workload.project_id = :project_id
GROUP BY Account.id
ORDER BY Account.name
```

## Sovelluksen ylläpitäjä

- sovellukseen on toteutettu roolipohjainen ylläpitotunnus (admin)
