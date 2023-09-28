# Engeto projekt 3

## Popis projektu
Tento projekt slouzi k extrahovani vysledku parlamentnich voleb pro rok 2017.

#
## Instalace knihoven
Pouzite knihovny jsou ulozeny v souboru requirements.txt. Pro instalaci pouzijeme nove virtualni prostredi a s nainstalovanym manazerem spustime nasledovne:
```
$ pip3 --version                        #overim verzi manageru
$ pip3 install -r requirements.txt      #nainstaluji knihovny
```

#
## Spousteni projektu
Spousteni souboru project_3.py v ramci prikazoveho radku pozaduje dva povinne argumenty.
```
project_3.py <odkaz uzemniho celku> <nazev vystupniho souboru>
```
Vystupni soubor s vysledky bude ve formatu csv.

#
## Ukazka projektu - web scraping
### Vysledky hlasovani pro okres Prostejov:
1. argument: `https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103`
2. argument: `vysledky_prostejov.csv`
### Spusteni projektu
```
python project_3.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103' 'vysledky_prostejov.csv
```
### Ukazka vystupu
```python
code,location,registered,envelopes,valid,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
506761,Alojzov,205,145,144,29,0,0,9,0,5,17,4,1,1,0,0,18,0,5,32,0,0,6,0,0,1,1,15,0
589268,Bedihošť,834,527,524,51,0,0,28,1,13,123,2,2,14,1,0,34,0,6,140,0,0,26,0,0,0,0,82,1
```