# Åpen Bibel — agentinstruksjoner

Prosjektkontekst for AI-assistenter som arbeider med bibelteksten i dette repoet.

## Hva prosjektet er

- **Åpen Bibel** moderniserer [1930-oversettelsen](Readme.md) (DNB1930) til moderne bokmål.
- Dette er **språklig oppdatering**, ikke en ny oversettelse fra grunnen — men sjekk gresk/hebraisk ved uklare ordvalg.
- Tekstfiler ligger under `Tekst/<nummer> <Boknavn>/<kapittel>.md` (tre sifre, f.eks. `010.md`).
- Lisens: CC0 på teksten.

## Arbeidsmoduser

**Modus B er standard.** Modus A brukes når kapittel allerede er omskrevet og trenger korrektur.

### Modus B — Modernisering (vanligste flyt)

Når teksten i hovedsak fortsatt følger 1930-oversettelsen:

1. Les og **tolk grunnteksten** (gresk eller hebraisk) — se skillen for steg.
2. Moderniser arkaiske ord og setningsbygning ut fra 1930 + grunntekst.
3. Legg til **avsnittsoverskrifter** (`### Tittel`) i stil fra Rom 1–11.
4. Rett tegnsetting og sitatform.
5. **Gjør endringene først**, deretter diskuter med brukeren etterpå.

### Modus A — Korrektur (allerede omskrevne kapitler)

For kapitler som allerede er modernisert (f.eks. Rom 1–11):

1. Les kapittelfilen og sammenlign med `git show HEAD:Tekst/...` der det er relevant.
2. Flag feil og uklare ordvalg; **diskuter med brukeren før endring** når det er skjønn.
3. Sjekk grunntekst og andre oversettelser som **inspirasjon** (ikke kopiering) ved behov.
4. Rett klare feil (skrivefeil, inkonsistens) direkte når det er åpenbart.
5. Oppdater status nederst i denne filen når et kapittel er ferdig.

Anta **Modus B** som standard for nye kapitler. Bruk Modus A når brukeren ber om korrektur/gjennomgang av allerede omskrevet tekst.

## Språkprinsipper

- **Moderne bokmål** som hovedmål.
- **Utgangspunkt:** 1930-teksten i repo + **gresk/hebraisk grunntekst**.
- **Andre oversettelser** (2011, 2024, ESV, Luther osv.): kun **inspirasjon** til formulering og ordlyd — **ikke kopier direkte**. Bibelen 2011 og andre moderne oversettelser er opphavsrettsbeskyttet.
- **Bokstavelighet mot grunntekst** når det er teologisk eller semantisk viktig — ikke harmoniser blindt med andre GT-steder (f.eks. Rom 9:15 bevisst ikke identisk med 2. Mos 33:19).
- Behold 1930-formulering når brukeren eksplisitt vil være nær grunnteksten (f.eks. «kappes om å hedre» i Rom 12:10).
- Diskuter *nidkjærhet* vs. *sjalusi/sjalu* kontekstavhengig — samme greske ordstamme kan ha ulik retning.

### Setningsstruktur — hva som typisk moderniseres

Utover enkeltord: se etter arkaisk **ordstilling og syntaks** i 1930. Mønster avklart bl.a. i 2. Pet 1 og Romerne:

| Mønster (1930) | Retning i moderne bokmål | Merknad |
|----------------|--------------------------|---------|
| *deres hjerter*, *deres kall* | *hjertene deres*, *kallet deres* | Eierskap etter substantivet er standard. Unntak: faste uttrykk (*vår Herre*, *vår Gud*). |
| *disse ting* / utvidet *disse tingene* | *dette* eller *disse* | Når grunnteksten bare har demonstrativt pronomen (f.eks. gresk ταῦτα), pek tilbake uten å legge inn *ting*. |
| *denne røst* (tilbakevisning) | *denne røsten* | Bestemt form når det vises til noe nettopp nevnt. |
| *akter det for riktig* | *mener det er riktig* | Arkaiske vurderingsfraser → vanlig moderne verb + ledd. |
| *idet* overalt | *når*, *ettersom*, *selv om*, *for* | Velg etter grunntekst og mening — ikke blind erstatning. |
| Verb før subjekt (*bli dere … til del*) | Naturlig SVO der det passer | Bibelsk stil kan beholde noe omvending, men unngå 1930-typisk tung ordstilling. |
| *er gitt til* når grunntekst har «bli/komme» | *oppstår ved*, *kommer av*, *kom til ved* | Verbvalg skal følge grunntekstens verb (f.eks. γίνεται), ikke bare oppdatere ord. |
| Ubestemt abstrakt i liste (*tålmod*, *tålmodighet* uten art.) | Bestemt form i kjedelister der det høres naturlig | Substantiv i oppramsing/dydskjede bør leses flytende som helhet. |
| *det/den/disse* + adj. + **ubestemt** substantiv (*det hellige berg*, *denne røst*) | Bestemt substantivsform (*det hellige fjellet*, *denne røsten*) | Arkaisk 1930-konstruksjon: bestemt artikkel foran, men ubestemt substantiv etter. Moderniser til normal bokmål. Ved tilbakevisning eller konkret sted: nesten alltid bestemt form. |

**Prinsipp:** Moderniser setningsbygning til idiomatisk bokmål, men la grunntekst styre når strukturen bærer teologisk eller semantisk vekt. Ved tvil: sammenlign med allerede moderniserte kapitler i `Tekst/` (Romerne, 2. Pet 1).

**Artikkel og substantiv:** 1930 tillater ofte *den/det/disse* foran adjektiv + substantiv i ubestemt form. Det høres arkaisk ut i moderne bokmål og bør normalt endres — enten til **bestemt substantiv** (*fjellet*, *røsten*) eller til **demonstrativ pronomen alene** (*dette*, *disse*) når grunnteksten ikke har et eget substantiv (f.eks. gresk ταῦτα).

## Format og tegnsetting

### Overskrifter

```markdown
## Kapittel 12

### Avsnittstittel

1 Første vers …
```

- `###`-overskrifter for tematiske avsnitt (som Rom 1–11).
- Tom linje etter overskrift før vers 1 i avsnittet.

### Linjeskift og versflyt

Versene innenfor et avsnitt (mellom `###`-overskrifter) skrives på separate linjer **uten tom linje mellom hver vers**. Dette er et bevisst valg for å bevare den naturlige flyten i teksten når den vises i markdown-lesere (GitHub, VS Code, osv.). Den opprinnelige 1930-teksten hadde ingen inndeling i vers som separate avsnitt eller med ekstra linjeskift.

Tom linje brukes kun:

- Etter hovedoverskrift (`## Kapittel X`)
- Etter avsnittsoverskrift (`### Tittel`) før første vers i avsnittet
- For å skille større avsnitt (før ny `###`)

### Salmene — versnummerering og poesi

**Versnummerering følger 1930 (og den masoretiske tradisjonen):** salmeoverskriften (*Til sangmesteren…*, *En salme av David…* osv.) er ofte **vers 1**. Den poetiske teksten begynner da i **vers 2**. Mange moderne leserbibler teller overskriften utenfor versene, slik at første dikterlinje blir «v. 1» — det gir avvikende henvisninger. Åpen Bibel beholder 1930-nummereringen konsekvent.

Eksempel (Salme 14):

```markdown
1 Til sangmesteren; av David.

    Dåren sier i hjertet sitt: «Det finnes ingen Gud.»
        …
    2 Herren skuer ned …
```

**Poetisk formatering:** bruk **tab-innrykk** foran hver linje (verslinje og fortsettelseslinje), ikke hard markdown-break (`\`) eller HTML (`&emsp;`). Tom linje skiller strofer/avsnitt innen salmen. Mønster som i Salme 1 og 3–25:

```markdown
    2 Herre, jeg har så mange fiender!
        Mange reiser seg imot meg.
```

### Sitater

- Vanlig skriftsitat etter kolon: **« … »**
- Sitat-i-sitat: **‘ … ’** inni « … » (se Rom 9:26, 10:6).
- Kolon før sitat etter *sier:*, *skrevet:*, *Jo, absolutt:* osv.
- Lengre sitater kan bruke blockquote (`>`) med versnummer i margen (se Rom 3, 9).

### Fotnoter

```markdown
34 For «…»[^1]

[^1]:  Jes 40,13.
```

- Format: `Bok kapittel,vers` med **komma** mellom kapittel og vers (norsk skikk, ikke engelsk kolon).
- Moderne forkortelser: `Sal`, `Jes`, `1 Mos`, `1 Krøn` — ikke `SLM`, `JES`, `1MO`, `1KR`.
- Semikolon mellom flere steder: `1 Krøn 29,30; Sal 139,16.`
- To mellomrom etter kolon i fotnotedefinisjon (eksisterende konvensjon).
- **Full liste:** [Referanser/bibel-forkortelser.md](Referanser/bibel-forkortelser.md)

## Nyttige referanser

| Kilde | Bruk |
|-------|------|
| `git show HEAD:Tekst/...` | 1930-baseline i repo (primær kilde) |
| [openbible.com](https://openbible.com) | Gresk tekst + Strong's (primær for NT) |
| [STEP Bible](https://www.stepbible.org) / [Sefaria](https://www.sefaria.org) | Hebraisk grunntekst (GT) |
| [bibel.no](https://bibel.no/nettbibelen) | 2011/2024 — **inspirasjon**, ikke kopiering |
| Eksisterende filer i `Tekst/` | Konsistens på ordvalg i Åpen Bibel |

## Avklarte ordvalg (Romerne — eksempler)

| Sted | Valg | Grunn |
|------|------|-------|
| 9:15 | *forbarme* / *barmhjertig* | Gresk/LXX, ikke identisk med 2. Mos 33:19 |
| 10:19 | *gjøre sjalu* | παραζηλόω; ikke *nidkjær* (feil moderne betydning) |
| 11:8 | *ånd av sløvhet* | πνεῦμα κατανύξεως |
| 11:32 | *lukket alle inne i ulydighet* | συνέκλεισεν |
| 12:2 | *la dere formes etter denne verden* | συσχηματίζεσθε |
| 12:3 | *tenke nøkternt* | σωφρονεῖν |
| 12:8 | *formaner* | παρακαλέω (ikke *oppmuntring*) |
| 12:10 | *kappes om å hedre* | προηγούμενοι (1930 beholdt) |
| 12:11 | *lunkne* | ὀκνηροί vs. ζέοντες (varme-motsetning) |
| 12:13 | *streb etter gjestfrihet* | διώκοντες |
| 12:19 | *gi plass til Guds vrede* | δότε τόπον τῇ ὀργῇ |
| 12:20 | *er sulten* / *er tørst* | πεινάω / διψάω |

## Fremdrift — Paulus' brev til romerne

**Ferdig** — alle 16 kapitler.

| Kapittel | Status |
|----------|--------|
| 1–8 | Gjennomgått og rettet |
| 9 | Gjennomgått og rettet |
| 10 | Ferdig |
| 11 | Ferdig |
| 12 | Ferdig (modernisert + diskutert) |
| 13 | Ferdig (modernisert + diskutert) |
| 14 | Ferdig (modernisert + diskutert) |
| 15 | Ferdig (modernisert + diskutert) |
| 16 | Ferdig (modernisert + diskutert) |

## Fremdrift — Peters andre brev

**Ferdig** — alle 3 kapitler modernisert og diskutert.

| Kapittel | Status |
|----------|--------|
| 1 | Ferdig (modernisert + diskutert) |
| 2 | Ferdig (modernisert + diskutert) |
| 3 | Ferdig (modernisert + diskutert) |

Oppdater disse tabellene når kapittel er ferdig.

## Relatert fil

- Arbeidsflyt-skill: `.grok/skills/apen-bibel/SKILL.md` (steg-for-steg for kapittelarbeid)