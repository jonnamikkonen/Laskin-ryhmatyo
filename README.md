# Laskin-projekti

Ryhmän henkilöt ja sähköpostit:
```shell=
PO
Henkilo A
Henkilo B
Henkilo C
Henkilo D
Jonna

```
## Suunnittelupalaveri
17.11.2022 Suunnittelupalaveri/ ensimmäinen sprint starttaa

Vastuut jaettu seuraavasti:
- Laskimen runko: Henkilo A
- Yhteenlasku: Henkilo B
- Vähennyslasku: Henkilo C
- Jakolasku: Jonna
- Kertolasku: Henkilo D
- Projektin päivitys, ajankohtaiset merkinnät: PO

Seuraava palaveri ja 2. sprint starttaa 21.11.2022

## Sprint 1 closattu, Sprint 2 aloitettu
21.11.2022 Sprint 2 alkaa

Palaverissa tehty/ käyty läpi:
- Poistettu kaksi turhaa kansiota
- Muotoiltiin laskimen runko toimivammaksi
- Käytiin läpi testausta: komennot joilla testataan, sekä kokeiltu testaamista
- Yllä olevalla jaolla jatketaan, jokainen tekee testauksen omalle osalle

Seuraava palaveri ja 3. sprint starttaa 24.11.2022

## Sprint 2 closattu, Sprint 3 aloitettu
24.11.2022 Sprint 3 alkaa

Palaverissa tehty:
- Yksikkötestit todettu toimiviksi
- Pylintin avulla korjailtu koodia
- Jokainen lisää omalle osalle dogstringit

Seuraava palaveri ja 4. sprint starttaa 28.11.2022

## Sprint 3 closattu, Sprint 4 aloitettu
28.11.2022 Sprint 4 alkaa

Palaverissa tehty:
- Porukalla mkdocsin dokumentointi laskimen osille.

Seuraava palaveri ja 5. sprint starttaa 30.11.2022

## Sprint 4 closattu, Sprint 5 aloitettu
30.11.2022 Sprint 5 alkaa

Palaverissa tehty:
- Doctestin läpikäynti
- Jokainen tekee testin omalle laskimen osalle
- Varmistettu Pylintin avulla koodin oikeellisuus

Sprint 5. tehtynä 7.12 mennessä
-----------

Koodikattavuus:

![](https://gitlab.dclabra.fi/wiki/uploads/upload_8032f36866bbf499b7781b81c4884a30.png)

Linttaus:

![](https://gitlab.dclabra.fi/wiki/uploads/upload_fe8812a94ee1ea4b59bd5dd49e93ae49.png)

---

**HELPME** Windows-koneilla korvaa komento `python3` komennolla `py` tai `python`

```shell=
# riippuvuuksien asentaminen
python -m pip install coverage pytest pylint mkdocs mkdocstrings mkdocstrings-python

# yksikkötestien suorittaminen ilman koodikattavuuden analyysia
python -m pytest -v

# koodikattavuuden tarkistaminen
coverage run -m pytest -v

# koodikattavuuden analyysi
coverage report -m # analysoi "koko roskan"

# koodikattavuus tiettyjen tiedostojen osalta
coverage report -m stack/stack.py tests/test_stack.py

# LINT (pylint)

pylint stack/stack.py

# dokumentaation generointi


mkdocs new .
mkdocs build
mkdocs serve


# Doctest -ajo
python -m doctest stack/stack.py

```
