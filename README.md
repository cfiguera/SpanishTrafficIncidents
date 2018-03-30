# SpanishTrafficIncidents
Autor: Carles Figuera <cfiguerap@uoc.edu>

Crea un dataset de incidentes actuales en la red de tráfico vial de la página web del [SISAP](http://infocar.dgt.es/etraffic/) de la Dirección General de Tráfico.

La aplicación se ejecuta de la siguiente manera:
```
python IncidentsScraper.py --> Incidentes en todas las províncias del país
python IncidentsScraper.py -p <province_code> --> Incidentes en una província concreta
python IncidentsScraper.py -h  --> Ver ayuda
```

Este es el listado de códigos de provincias a filtrar:

4 - ALMERÍA
11 - CÁDIZ
14 - CÓRDOBA
18 - GRANADA
21 - HUELVA
23 - JAÉN
29 - MÁLAGA
41 - SEVILLA
44 - TERUEL
50 - ZARAGOZA
7 - BALEARS, ILLES
35 - PALMAS, LAS
38 - SANTA CRUZ DE TENERIFE
39 - CANTABRIA
5 - ÁVILA
9 - BURGOS
24 - LEÓN
34 - PALENCIA
37 - SALAMANCA
40 - SEGOVIA
42 - SORIA
47 - VALLADOLID
49 - ZAMORA
2 - ALBACETE
13 - CIUDAD REAL
16 - CUENCA
19 - GUADALAJARA
45 - TOLEDO
8 - BARCELONA
17 - GIRONA
25 - LLEIDA
43 - TARRAGONA
3 - ALICANTE/ALACANT
12 - CASTELLÓN/CASTELLÓ
46 - VALENCIA/VALÈNCIA
6 - BADAJOZ
10 - CÁCERES
15 - CORUÑA, A
27 - LUGO
32 - OURENSE
36 - PONTEVEDRA
28 - MADRID
30 - MURCIA
31 - NAVARRA
1 - ARABA/ÁLAVA
48 - BIZKAIA
20 - GIPUZKOA
26 - RIOJA, LA
51 - CEUTA
52 - MELILLA
