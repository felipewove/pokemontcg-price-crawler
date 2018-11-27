# Pokemon TCG Price Crawler
A Pokémon TCG Price crawler for LigaPokemon, prices in BRL.

## Setting up
```bash
docker-compose build
```

## Running
Pass a collection code from LigaPokemon as argument when running. Check all codes [here](../master/translator.py).

Note: LigaPokemon don't use oficial abreviations.

```bash
docker-compose run crawler python test.py <ARG:collection_code>
```

## TODO

* Save in CSV, with timestamp
* Given a collection, get all prices (now is just page 1, that returns 30 cards)
