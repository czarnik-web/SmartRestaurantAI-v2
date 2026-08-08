# AI Prioritizácia objednávok v kuchyni

## Stav

💡 Nápad pre budúcu verziu

---

# Popis

Kitchen Agent bude v budúcnosti schopný meniť poradie objednávok na základe AI analýzy namiesto jednoduchého FIFO (First In, First Out).

---

# Súčasný stav (MVP)

Objednávky budú spracovávané podľa času prijatia (FIFO).

Dôvod:

Na začiatku nebude systém disponovať dostatočným množstvom dát na spoľahlivé rozhodovanie AI.

---

# Budúca implementácia

Po nazbieraní dostatočného množstva historických dát bude AI analyzovať napríklad:

- priemerný čas prípravy jednotlivých jedál,
- vyťaženosť kuchyne,
- počet aktívnych kuchárov,
- aktuálnu čakaciu dobu,
- prioritu donášok,
- predpokladaný čas doručenia,
- historickú úspešnosť plánovania.

Na základe týchto údajov bude AI dynamicky určovať optimálne poradie prípravy objednávok.

---

# Očakávané výhody

- kratší priemerný čas čakania zákazníkov,
- efektívnejšie využitie kapacity kuchyne,
- lepšie plánovanie počas špičky,
- presnejšie odhady času dokončenia objednávok.

---

# Podmienky implementácie

Funkcia bude aktivovaná až po nazbieraní dostatočného množstva kvalitných historických dát.

Do tej doby bude systém využívať jednoduché a spoľahlivé pravidlo FIFO.

---

# Poznámka

Architektonický princíp projektu:

**AI rozhoduje až vtedy, keď má dostatok kvalitných dát. Dovtedy systém používa jednoduché, spoľahlivé pravidlá.**

# Detailné sledovanie položiek objednávky

## Stav

💡 Nápad pre budúcu verziu

---

# Popis

V budúcnosti bude možné sledovať stav jednotlivých položiek objednávky namiesto sledovania iba celej objednávky.

Príklady stavov:

- Pizza – Preparing
- Burger – Ready
- Šalát – Ready
- Nápoj – Ready

Objednávka bude označená ako **Ready** až po dokončení všetkých položiek.

---

# Dôvod odloženia

Nie všetky reštaurácie používajú Kitchen Display System (KDS) alebo tablety.

Mnohé prevádzky stále využívajú papierové bonovačky alebo jednoduché zobrazovacie zariadenia.

Pre prvú verziu systému je preto jednoduchšie a univerzálnejšie sledovať stav celej objednávky.

---

# Budúca implementácia

Funkcia bude určená najmä pre prevádzky využívajúce:

- Kitchen Display System (KDS),
- tablety,
- dotykové obrazovky,
- pokročilé kuchynské pracoviská.

---

# Očakávané výhody

- lepší prehľad o stave prípravy,
- možnosť paralelnej prípravy jedál,
- presnejšie informácie pre personál,
- lepšie plánovanie práce v kuchyni.
- Možnosť zapnúť alebo vypnúť jednotlivé typy oznámení podľa preferencií zákazníka.

# Rozšírené úpravy produktov

## Stav

💡 Návrh do budúcna

---

## Popis

Funkcionalita umožní zákazníkovi upraviť objednaný produkt podľa vlastných preferencií.

Úpravy budú vykonané iba pre konkrétnu objednávku a nikdy nezmenia produkt uložený v Products Database.

Restaurant Assistant zabezpečí spracovanie požiadavky a odovzdanie všetkých úprav Kitchen Agentovi a Inventory Agentovi.

---

## Súčasný stav (MVP)

V prvej verzii systému môže zákazník odstrániť ľubovoľnú surovinu z objednávaného produktu.

Táto zmena sa uloží iba ku konkrétnej objednávke.

Cena produktu zostáva nezmenená.

---

## Budúca implementácia

Systém bude podporovať aj platené úpravy produktov.

Príklady:

- extra syr,
- extra mäso,
- extra slanina,
- prídavné omáčky,
- dvojitá porcia,
- prílohy navyše.

Restaurant Assistant automaticky vypočíta novú cenu podľa pravidiel nastavených administrátorom.

Inventory Agent započíta spotrebu pridaných surovín.

Kitchen Agent dostane kompletný zoznam všetkých úprav.

---

## Očakávané výhody

- vyššia flexibilita objednávok,
- lepší zákaznícky zážitok,
- jednoduchšia personalizácia produktov,
- automatický výpočet ceny doplnkov,
- presnejšia evidencia spotreby surovín.

---

## Podmienky implementácie

- dokončené Products API,
- dokončený Inventory modul,
- podpora doplnkov v Products Database,
- cenové pravidlá definované administrátorom.

---

## Poznámka

Administrátor určuje dostupné doplnky a ich ceny.

AI agenti môžu vykonávať iba pravidlá definované administrátorom.

Definícia produktu v databáze zostáva vždy nezmenená.
