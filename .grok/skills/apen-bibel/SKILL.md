---
name: apen-bibel
description: >
  Modernisere og gjennomgå Åpen Bibel-tekst (1930-baseline til moderne bokmål).
  Bruk når brukeren arbeider med Tekst/, moderniserer et kapittel, gjennomgår
  bibeltekster, i apen-bibel / åpen bibel prosjektet.
---

# Åpen Bibel — modernisering

Les **AGENTS.md** i repo-roten for full prosjektkontekst. Denne skillen er arbeidsflyten.

## Før du starter

1. Les `AGENTS.md` (språkprinsipper, format, fremdrift).
2. Les kapittelfilen under `Tekst/`.
3. Kjør `git show HEAD:Tekst/<bok>/<kap>.md` for 1930-baseline.

## Steg: Les og tolk grunnteksten

```
1. Identifiser om kapitlet er NT (gresk) eller GT (hebraisk)
2. Hent grunntekst for aktuelle vers:
   - NT: openbible.com (Nestle 1904) + Strong's
   - GT: Sefaria / STEP Bible
3. For hvert avsnitt eller vanskelig vers, noter kort:
   - Nøkkelord (original + betydning)
   - Verbets aspekt / imperativ / passiv der det er relevant
   - Sitater fra GT: sjekk om Paulus/teksten følger LXX eller hebraisk
4. Sammenlign tre lag:
   - Grunntekst (hva betyr det?)
   - 1930 (hva står i repo?)
   - Forslag til moderne norsk (ny formulering — ikke kopiert fra 2011 eller andre oversettelser)
5. Bruk grunntekst-tolkningen som styringsinput ved valg av norske ord
```

Presentér grunntekst-funn for brukeren når ordvalg er skjønnsmessig — enten før eller etter utkast, avhengig av modus.

## Opphavsrett — andre oversettelser

- **Ikke kopier** formuleringer fra Bibelen 2011/2024, NIV, ESV, Luther eller andre beskyttede oversettelser.
- **Tillatt:** sjekke hvordan andre løser et vanskelig vers, og formulere **egen** norsk tekst med samme *mening*.
- Primærkilder for Åpen Bibel: **1930-teksten i repo** + **gresk/hebraisk grunntekst**.

## Fremgangsmåte for modernisering

Vi moderniserer teksten ett kapittel av gangen, og følger en strukturert prosess. Denne prosessen kan også brukes for korrektur av allerede moderniserte kapitler, men med litt mer fokus på diskusjon og mindre på å gjøre endringer direkte.

```
1. [Grunntekst] Les og tolk kapittel/avsnitt (se steg over)
2. Identifiser arkaiske ord og utdatert setningsbygning i 1930-teksten (se «Setningsstruktur» i AGENTS.md)
3. Del inn i avsnitt med ###-overskrifter
4. Legg til linjeskift etter avsnitt og overskrifter, men IKKE etter hvert vers (for å bevare flyten) 
5. Skriv modernisert utkast — styrt av grunntekst + 1930,
6. Rett tegnsetting: kolon før sitater, « » og ‘ ’
7. Bruk kodeblokk for poetiske avsnitt, for eksempel Salmer, for å bevare linjeskift og rytme.
8. Legg fotnoter [^n] ved skrifthenvisninger når det er naturlig (forkortelser: `Referanser/bibel-forkortelser.md`)
9. Presenter endringene for diskusjon med brukeren
10. Oppdater fremdriftstabellen i AGENTS.md
```

## Sjekkliste før kapittel er «ferdig»

- [ ] Grunntekst vurdert for vanskelige ord og vers
- [ ] Ingen formuleringer kopiert fra 2011 eller andre beskyttede oversettelser
- [ ] Ingen åpenbare skrivefeil mot 1930-intent / grunntekst
- [ ] Sitater har « »; kolon der det skal være
- [ ] En linje per vers, uten linjeskift imellom versene i samme avsnitt
- [ ] Kodeblokk for poetisk tekst der linjeskift må bevares
- [ ] Setningsstruktur modernisert (eierskap, demonstrativer, bindeord, verb — se AGENTS.md)
- [ ] Konsistent med tidligere kapittel i samme bok (ordvalg, stil)
- [ ] Fremdrift oppdatert i AGENTS.md
- [ ] Bruker har hatt mulighet til å diskutere større valg

## Vanlige fallgruver

- **Kopiere andre oversettelser** — inspirasjon ja, ord-for-ord nei.
- **Linjeskift** Ikke legg inn linjeskift etter hvert vers; behold flyten i avsnittet. Linjeskift skal kun være etter overskrifter og mellom avsnitt.
- Ikke endre filer brukeren ikke ba om; ikke skriv nye markdown-filer uten forespørsel (unntatt AGENTS.md / skill ved eksplisitt oppdrag).