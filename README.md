# Pokemon TCG Price Crawler
A Pokémon TCG Price crawler for LigaPokemon, prices in BRL.

## Setting up
```bash
docker-compose build
```

## Running
```bash
docker-compose run crawler python test.py
```

## TODO

* Save in CSV, with timestamp
* Given a collection, get all prices (now is just page 1, that returns 30 cards)
* Parameters at execution