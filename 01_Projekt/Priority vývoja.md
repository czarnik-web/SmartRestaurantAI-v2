# Priority vývoja – Smart Restaurant AI

## Verzia dokumentu

v1.0

---

# Účel dokumentu

Tento dokument určuje poradie vývoja jednotlivých modulov a AI agentov podľa ich prínosu pre zákazníka.

Prioritou nie je vytvoriť čo najviac funkcií, ale priniesť zákazníkovi čo najväčšiu hodnotu v čo najkratšom čase.

---

# Priority vývoja

| Priorita | Modul / Agent        | Hodnota pre zákazníka                                                                                                      |
| -------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 1        | Restaurant Assistant | Prijíma objednávky, komunikuje so zákazníkmi a zabezpečuje plynulý priebeh objednávky.                                |
| 2        | Inventory Agent      | Automatizuje správu skladu, kontroluje zásoby, upozorňuje na chýbajúce suroviny a pripravuje objednávky dodávateľom. |
| 3        | Payment Agent        | Spracováva platby, vystavuje doklady a zaznamenáva tržby.                                                                 |
| 4        | Reservation Agent    | Riadi rezervácie stolov, kontroluje kapacitu a navrhuje voľné termíny.                                                   |
| 5        | Reporting Agent      | Pripravuje denné, týždenné a mesačné reporty pre manažéra.                                                           |
| 6        | Sales Agent          | Vyhodnocuje predaj, navrhuje zľavy a optimalizuje skladové zásoby.                                                        |
| 7        | Marketing Agent      | Pripravuje marketingové kampane, emaily a personalizované ponuky.                                                          |
| 8        | Security Agent       | Zabezpečuje ochranu systému, monitoruje podozrivé udalosti a upozorňuje manažéra na riziká.                           |

---

# Pravidlá vývoja

- Každý nový modul musí riešiť konkrétny problém zákazníka.
- Vývoj sa riadi podľa hodnoty pre zákazníka, nie podľa technickej náročnosti.
- Nové funkcie sa pridávajú iba v prípade, že prinášajú reálny prínos.
- Každý modul musí byť navrhnutý tak, aby ho bolo možné rozšíriť bez zásadných zmien ostatných častí systému.

---

# Architektonické pravidlo č. 1

Navrhujeme najjednoduchšie riešenie, ktoré spoľahlivo vyrieši aktuálny problém zákazníka.

Vyhýbame sa zbytočne zložitým riešeniam a funkciám, ktoré nie sú potrebné pre prvú verziu systému (MVP).
