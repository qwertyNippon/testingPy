# create a function that loops through and only return the names from a data list.


# use split
# remove commas
# loop through and add every (x) to another variable



# def cityList(x):
#     lst=[]
    # x = x.replace(' ','-')
    # print(x)
    # x = x.split(',')
    # print(x) 
    # print(x[0])
    # for i in range(0, len(x), 4):
    #     lst.append(x[i])
    # print(lst)
    # for i in range(len(lst)):
    #     lst=','.join(lst)
    #     lst=lst.replace('-', ' ')
    #     lst=lst.split(',')
    # print(lst)

# cityList(b)
text= '''
Andorra la Vella,Andorra,Andorra la Vella,3041563
Umm al Qaywayn,United Arab Emirates,Umm al Qaywayn,290594
Ras al-Khaimah,United Arab Emirates,RaÊ¼s al Khaymah,291074
Khawr FakkÄn,United Arab Emirates,Ash ShÄriqah,291696
Dubai,United Arab Emirates,Dubai,292223
Dibba Al-Fujairah,United Arab Emirates,Al Fujayrah,292231
Dibba Al-Hisn,United Arab Emirates,Al Fujayrah,292239
Sharjah,United Arab Emirates,Ash ShÄriqah,292672
Ar Ruways,United Arab Emirates,Abu Dhabi,292688
Al Fujayrah,United Arab Emirates,Al Fujayrah,292878
Al Ain,United Arab Emirates,Abu Dhabi,292913
Ajman,United Arab Emirates,Ajman,292932
Adh Dhayd,United Arab Emirates,Ash ShÄriqah,292953
Abu Dhabi,United Arab Emirates,Abu Dhabi,292968
Zaranj,Afghanistan,NÄ«mrÅ«z,1120985
Taloqan,Afghanistan,TakhÄr,1123004
ShÄ«ná¸aná¸,Afghanistan,Herat,1125155
ShibirghÄn,Afghanistan,JowzjÄn,1125444
Shahrak,Afghanistan,Ghowr,1125896
Sar-e Pul,Afghanistan,Sar-e Pol,1127110
Sang-e ChÄrak,Afghanistan,Sar-e Pol,1127628
AÄ«bak,Afghanistan,SamangÄn,1127768
RustÄq,Afghanistan,TakhÄr,1128265
QarqÄ«n,Afghanistan,JowzjÄn,1129516
QarÄwul,Afghanistan,Kunduz,1129648
Pul-e KhumrÄ«,Afghanistan,WilÄyat-e BaghlÄn,1130490
PaghmÄn,Afghanistan,Kabul,1131316
NahrÄ«n,Afghanistan,WilÄyat-e BaghlÄn,1132495
Maymana,Afghanistan,Faryab,1133453
Mehtar LÄm,Afghanistan,LaghmÄn,1133574
MazÄr-e SharÄ«f,Afghanistan,Balkh,1133616
Lashkar GÄh,Afghanistan,Helmand,1134720
Kushk,Afghanistan,Herat,1135158
Kunduz,Afghanistan,Kunduz,1135689
KhÅst,Afghanistan,Khowst,1136469
Khulm,Afghanistan,Balkh,1136575
KhÄsh,Afghanistan,NÄ«mrÅ«z,1136863
Khanabad,Afghanistan,Kunduz,1137168
Karukh,Afghanistan,Herat,1137807
KandahÄr,Afghanistan,KandahÄr,1138336
Kabul,Afghanistan,Kabul,1138958
JalÄlÄbÄd,Afghanistan,NangarhÄr,1139715
Jabal os Saraj,Afghanistan,ParvÄn,1139807
HerÄt,Afghanistan,Herat,1140026
Ghormach,Afghanistan,Badghis,1141089
Ghazni,Afghanistan,GhaznÄ«,1141269
Gereshk,Afghanistan,Helmand,1141540
GardÄ“z,Afghanistan,Paktia,1141857
Fayzabad,Afghanistan,Badakhshan,1142170
Farah,Afghanistan,Farah,1142264
Kafir Qala,Afghanistan,Herat,1142404
Charikar,Afghanistan,ParvÄn,1145352
BarakÄ« Barak,Afghanistan,Lowgar,1147066
BÄmyÄn,Afghanistan,BÄmÄ«Än,1147242
Balkh,Afghanistan,Balkh,1147290
BaghlÄn,Afghanistan,WilÄyat-e BaghlÄn,1147540
Ä€rt KhwÄjah,Afghanistan,TakhÄr,1148106
Ä€smÄr,Afghanistan,Konar,1148205
AsadÄbÄd,Afghanistan,Konar,1148311
AndkhÅy,Afghanistan,Faryab,1148658
BÄzÄrak,Afghanistan,Panjshir,1429434
Markaz-e WoluswalÄ«-ye Ä€chÄ«n,Afghanistan,NangarhÄr,1469706
Saint Johnâ€™s,Antigua and Barbuda,Saint John,3576022
The Valley,Anguilla,N/A,3573374
SarandÃ«,Albania,VlorÃ«,363243
KukÃ«s,Albania,KukÃ«s,782661
KorÃ§Ã«,Albania,KorÃ§Ã«,782756
GjirokastÃ«r,Albania,GjirokastÃ«r,783148
Elbasan,Albania,Elbasan,783263
Burrel,Albania,DibÃ«r,783493
VlorÃ«,Albania,VlorÃ«,3183719
Tirana,Albania,TiranÃ«,3183875
ShkodÃ«r,Albania,ShkodÃ«r,3184081
Patos Fshat,Albania,Fier,3184517
LushnjÃ«,Albania,Fier,3184862
LezhÃ«,Albania,LezhÃ«,3184935
LaÃ§,Albania,LezhÃ«,3185012
KuÃ§ovÃ«,Albania,Berat,3185060
KrujÃ«,Albania,DurrÃ«s,3185082
KavajÃ«,Albania,TiranÃ«,3185211
Fier-Ã‡ifÃ§i,Albania,Fier,3185670
Fier,Albania,Fier,3185672
DurrÃ«s,Albania,DurrÃ«s,3185728
Berat,Albania,Berat,3186084
Kapan,Armenia,Syunik Province,174875
Goris,Armenia,Syunik Province,174895
Hatsâ€™avan,Armenia,Syunik Province,174972
Artashat,Armenia,Ararat Province,174979
Ararat,Armenia,Ararat Province,174991
Yerevan,Armenia,Yerevan,616052
Ejmiatsin,Armenia,Armavir Province,616062
Spitak,Armenia,Lori Province,616199
Sevan,Armenia,Gegharkunik Province,616250
Masis,Armenia,Ararat Province,616435
Vanadzor,Armenia,Lori Province,616530
Gavarr,Armenia,Gegharkunik Province,616599
Hrazdan,Armenia,Kotayk Province,616629
Armavir,Armenia,Armavir Province,616631
Gyumri,Armenia,Shirak Province,616635
Ashtarak,Armenia,Aragatsotn Province,616877
Abovyan,Armenia,Kotayk Province,617026
Saurimo,Angola,Lunda Sul,145531
Lucapa,Angola,Lunda Norte,145724
Luau,Angola,Moxico,876177
UÃ­ge,Angola,UÃ­ge,2236568
Soio,Angola,Zaire,2236967
Nzeto,Angola,Zaire,2239001
Nâ€™dalatando,Angola,Cuanza Norte,2239076
Mbanza Congo,Angola,Zaire,2239520
Malanje,Angola,Malanje,2239862
Luanda,Angola,Luanda,2240449
Caxito,Angola,Bengo,2242001
Cabinda,Angola,Cabinda,2243271
Sumbe,Angola,Cuanza Sul,3346015
Namibe,Angola,Namibe,3347019
Menongue,Angola,Cuando Cubango,3347353
Luena,Angola,Moxico,3347719
Lubango,Angola,HuÃ­la,3347762
Longonjo,Angola,Huambo,3347853
Lobito,Angola,Benguela,3347939
Cuito,Angola,BiÃ©,3348078
Huambo,Angola,Huambo,3348313
Catumbela,Angola,Benguela,3350246
Catabola,Angola,BiÃ©,3350372
Camacupa,Angola,BiÃ©,3351014
Caluquembe,Angola,HuÃ­la,3351024
CaÃ¡la,Angola,Huambo,3351500
Benguela,Angola,Benguela,3351663
ZÃ¡rate,Argentina,Buenos Aires,3427213
Villa Ocampo,Argentina,Santa Fe,3427388
Villa Lugano,Argentina,Buenos Aires F.D.,3427408
Villaguay,Argentina,Entre Rios,3427428
Villa Gesell,Argentina,Buenos Aires,3427431
Tigre,Argentina,Buenos Aires,3427761
Tandil,Argentina,Buenos Aires,3427833
San Vicente,Argentina,Misiones,3428068
Santo TomÃ©,Argentina,Corrientes,3428071
Santa Elena,Argentina,Entre Rios,3428359
San Pedro,Argentina,Misiones,3428577
San Luis del Palmar,Argentina,Corrientes,3428708
San Lorenzo,Argentina,Corrientes,3428759
San Javier,Argentina,Santa Fe,3428975
San Isidro,Argentina,Buenos Aires,3428992
Saladas,Argentina,Corrientes,3429403
Retiro,Argentina,Buenos Aires F.D.,3429576
Resistencia,Argentina,Chaco,3429577
Reconquista,Argentina,Santa Fe,3429594
Quilmes,Argentina,Buenos Aires,3429652
Puerto Rico,Argentina,Misiones,3429732
Puerto IguazÃº,Argentina,Misiones,3429777
Puerto Esperanza,Argentina,Misiones,3429786
Puerto Eldorado,Argentina,Misiones,3429790
Posadas,Argentina,Misiones,3429886
Pontevedra,Argentina,Buenos Aires,3429902
PiranÃ©,Argentina,Formosa,3429949
Paso de los Libres,Argentina,Corrientes,3430104
OberÃ¡,Argentina,Misiones,3430340
Necochea,Argentina,Buenos Aires,3430443
MorÃ³n,Argentina,Buenos Aires,3430545
Monte Caseros,Argentina,Corrientes,3430598
Montecarlo,Argentina,Misiones,3430601
Mercedes,Argentina,Buenos Aires,3430708
Mercedes,Argentina,Corrientes,3430709
Mar del Plata,Argentina,Buenos Aires,3430863
LujÃ¡n,Argentina,Buenos Aires,3430988
La Plata,Argentina,Buenos Aires,3432043
La Paz,Argentina,Entre Rios,3432079
JardÃ­n AmÃ©rica,Argentina,Misiones,3433349
GualeguaychÃº,Argentina,Entre Rios,3433658
Gualeguay,Argentina,Entre Rios,3433663
Goya,Argentina,Corrientes,3433715
Gobernador Ingeniero ValentÃ­n Virasoro,Argentina,Corrientes,3433753
General JosÃ© de San MartÃ­n,Argentina,Chaco,3433803
GarupÃ¡,Argentina,Misiones,3433836
Formosa,Argentina,Formosa,3433899
Fontana,Argentina,Chaco,3433901
Federal,Argentina,Entre Rios,3433956
Esquina,Argentina,Corrientes,3434095
El Soberbio,Argentina,Misiones,3434291
Dolores,Argentina,Buenos Aires,3435038
CuruzÃº CuatiÃ¡,Argentina,Corrientes,3435103
Corrientes,Argentina,Corrientes,3435217
Concordia,Argentina,Entre Rios,3435261
ConcepciÃ³n del Uruguay,Argentina,Entre Rios,3435264
Colegiales,Argentina,Buenos Aires F.D.,3435356
ChajarÃ­,Argentina,Entre Rios,3435486
Campana,Argentina,Buenos Aires,3435810
Buenos Aires,Argentina,Buenos Aires F.D.,3435910
Barranqueras,Argentina,Chaco,3436124
Azul,Argentina,Buenos Aires,3436199
Avellaneda,Argentina,Santa Fe,3436230
AristÃ³bulo del Valle,Argentina,Misiones,3436287
Zapala,Argentina,Neuquen,3832132
Yerba Buena,Argentina,TucumÃ¡n,3832260
Villa Regina,Argentina,Rio Negro,3832647
Villa Paula de Sarmiento,Argentina,San Juan,3832653
Villa Nueva,Argentina,Cordoba,3832662
Villa MarÃ­a,Argentina,Cordoba,3832694
Villa Dolores,Argentina,Cordoba,3832756
Villa ConstituciÃ³n,Argentina,Santa Fe,3832778
Villa Carlos Paz,Argentina,Cordoba,3832791
Villa Ãngela,Argentina,Chaco,3832811
Villa Allende,Argentina,Cordoba,3832815
Viedma,Argentina,Rio Negro,3832899
Victoria,Argentina,Entre Rios,3832934
Vera,Argentina,Santa Fe,3833027
Venado Tuerto,Argentina,Santa Fe,3833062
Veinticinco de Mayo,Argentina,Buenos Aires,3833112
Ushuaia,Argentina,Tierra del Fuego,3833367
Unquillo,Argentina,Cordoba,3833412
Tres Isletas,Argentina,Chaco,3833794
Tres Arroyos,Argentina,Buenos Aires,3833859
Trelew,Argentina,Chubut,3833883
Termas de RÃ­o Hondo,Argentina,Santiago del Estero,3834502
Tartagal,Argentina,Salta,3834601
TafÃ­ Viejo,Argentina,TucumÃ¡n,3834813
Sunchales,Argentina,Santa Fe,3834971
Santo TomÃ©,Argentina,Santa Fe,3835793
Santiago del Estero,Argentina,Santiago del Estero,3835869
Santa Rosa,Argentina,La Pampa,3835994
Santa LucÃ­a,Argentina,San Juan,3836194
Santa Fe de la Vera Cruz,Argentina,Santa Fe,3836277
San Salvador de Jujuy,Argentina,Jujuy,3836564
San RamÃ³n de la Nueva OrÃ¡n,Argentina,Salta,3836620
San Rafael,Argentina,Mendoza,3836669
San Pedro,Argentina,Jujuy,3836772
San NicolÃ¡s de los Arroyos,Argentina,Buenos Aires,3836846
San Miguel de TucumÃ¡n,Argentina,TucumÃ¡n,3836873
San MartÃ­n de los Andes,Argentina,Neuquen,3836951
San MartÃ­n,Argentina,Mendoza,3836992
San Luis,Argentina,San Luis,3837056
San Justo,Argentina,Santa Fe,3837124
San Juan,Argentina,San Juan,3837213
San JosÃ© de JÃ¡chal,Argentina,San Juan,3837240
San Jorge,Argentina,Santa Fe,3837441
San Francisco,Argentina,Cordoba,3837675
San Fernando del Valle de Catamarca,Argentina,Catamarca,3837702
San Antonio Oeste,Argentina,Rio Negro,3837980
Salta,Argentina,Salta,3838233
Rufino,Argentina,Santa Fe,3838506
Rosario,Argentina,Santa Fe,3838583
RÃ­o Tercero,Argentina,Cordoba,3838793
RÃ­o Segundo,Argentina,Cordoba,3838797
RÃ­o Gallegos,Argentina,Santa Cruz,3838859
RÃ­o Cuarto,Argentina,Cordoba,3838874
RÃ­o Ceballos,Argentina,Cordoba,3838902
Rawson,Argentina,Chubut,3839307
Rafaela,Argentina,Santa Fe,3839479
Quitilipi,Argentina,Chaco,3839490
Punta Alta,Argentina,Buenos Aires,3839982
Puerto Madryn,Argentina,Chubut,3840092
Presidencia Roque SÃ¡enz PeÃ±a,Argentina,Chaco,3840300
Pocito,Argentina,San Juan,3840860
Plottier,Argentina,Neuquen,3840885
Pergamino,Argentina,Buenos Aires,3841490
PÃ©rez,Argentina,Santa Fe,3841500
ParanÃ¡,Argentina,Entre Rios,3841956
PalpalÃ¡,Argentina,Jujuy,3842190
OlavarrÃ­a,Argentina,Buenos Aires,3842670
Nueve de Julio,Argentina,Buenos Aires,3842881
NeuquÃ©n,Argentina,Neuquen,3843123
Morteros,Argentina,Cordoba,3843619
Monteros,Argentina,TucumÃ¡n,3843803
Mendoza,Argentina,Mendoza,3844421
Marcos JuÃ¡rez,Argentina,Cordoba,3844899
Machagai,Argentina,Chaco,3845330
Lincoln,Argentina,Buenos Aires,3846864
Libertador General San MartÃ­n,Argentina,Jujuy,3846915
Las BreÃ±as,Argentina,Chaco,3848687
La Rioja,Argentina,La Rioja,3848950
La Falda,Argentina,Cordoba,3851331
La Calera,Argentina,Cordoba,3852374
Laboulaye,Argentina,Cordoba,3852468
JunÃ­n,Argentina,Buenos Aires,3853354
JoaquÃ­n V. GonzÃ¡lez,Argentina,Salta,3853491
JesÃºs MarÃ­a,Argentina,Cordoba,3853510
Granadero Baigorria,Argentina,Santa Fe,3854895
Gobernador GÃ¡lvez,Argentina,Santa Fe,3854985
General Roca,Argentina,Rio Negro,3855065
General Pinedo,Argentina,Chaco,3855074
General Pico,Argentina,La Pampa,3855075
General Enrique Mosconi,Argentina,Salta,3855116
GÃ¡lvez,Argentina,Santa Fe,3855244
Firmat,Argentina,Santa Fe,3855554
FamaillÃ¡,Argentina,TucumÃ¡n,3855666
Esquel,Argentina,Chubut,3855974
Esperanza,Argentina,Santa Fe,3856022
EmbarcaciÃ³n,Argentina,Salta,3856231
Embalse,Argentina,Cordoba,3856235
El BolsÃ³n,Argentina,Rio Negro,3858765
Diamante,Argentina,Entre Rios,3859384
DeÃ¡n Funes,Argentina,Cordoba,3859512
Cutral-CÃ³,Argentina,Neuquen,3859552
Cruz del Eje,Argentina,Cordoba,3859828
Crespo,Argentina,Entre Rios,3859904
CosquÃ­n,Argentina,Cordoba,3859965
Coronel SuÃ¡rez,Argentina,Buenos Aires,3860164
Coronda,Argentina,Santa Fe,3860217
CÃ³rdoba,Argentina,Cordoba,3860259
Comodoro Rivadavia,Argentina,Chubut,3860443
Cipolletti,Argentina,Rio Negro,3861056
Cinco Saltos,Argentina,Rio Negro,3861061
Chivilcoy,Argentina,Buenos Aires,3861344
Chimbas,Argentina,San Juan,3861416
Chilecito,Argentina,La Rioja,3861445
Charata,Argentina,Chaco,3861678
Chacabuco,Argentina,Buenos Aires,3861953
Centenario,Argentina,Neuquen,3862144
Caucete,Argentina,San Juan,3862240
Catriel,Argentina,Rio Negro,3862254
Castelli,Argentina,Chaco,3862320
Casilda,Argentina,Santa Fe,3862351
CarcaraÃ±Ã¡,Argentina,Santa Fe,3862655
CapitÃ¡n BermÃºdez,Argentina,Santa Fe,3862738
CaÃ±ada de GÃ³mez,Argentina,Santa Fe,3862981
Caleta Olivia,Argentina,Santa Cruz,3863379
Bell Ville,Argentina,Cordoba,3864331
Bella Vista,Argentina,TucumÃ¡n,3864375
BahÃ­a Blanca,Argentina,Buenos Aires,3865086
Arroyo Seco,Argentina,Santa Fe,3865385
Arroyito,Argentina,Cordoba,3865424
AÃ±atuya,Argentina,Santiago del Estero,3865840
Alta Gracia,Argentina,Cordoba,3866163
Allen,Argentina,Rio Negro,3866242
Alderetes,Argentina,TucumÃ¡n,3866367
AlbardÃ³n,Argentina,San Juan,3866425
Aguilares,Argentina,TucumÃ¡n,3866496
Villa Santa Rita,Argentina,Buenos Aires F.D.,6693230
Villa Mercedes,Argentina,San Luis,7116866
San Carlos de Bariloche,Argentina,Rio Negro,7647007
AdroguÃ©,Argentina,Buenos Aires,10172104
Pago Pago,American Samoa,Eastern District,5881576
Wolfsberg,Austria,Carinthia,2760910
Wiener Neustadt,Austria,Lower Austria,2761353
Vienna,Austria,Vienna,2761369
Wels,Austria,Upper Austria,2761524
Weinzierl bei Krems,Austria,Lower Austria,2761669
Villach,Austria,Carinthia,2762372
Traun,Austria,Upper Austria,2763423
Traiskirchen,Austria,Lower Austria,2763460
Ternitz,Austria,Lower Austria,2763795
Steyr,Austria,Upper Austria,2764359
Spittal an der Drau,Austria,Carinthia,2764786
Schwechat,Austria,Lower Austria,2765388
Sankt PÃ¶lten,Austria,Lower Austria,2766429
Salzburg,Austria,Salzburg,2766824
Saalfelden am Steinernen Meer,Austria,Salzburg,2766922
MÃ¶dling,Austria,Lower Austria,2771335
Lustenau,Austria,Vorarlberg,2772173
Linz,Austria,Upper Austria,2772400
Leonding,Austria,Upper Austria,2772635
Leoben,Austria,Styria,2772649
Kufstein,Austria,Tyrol,2773300
Krems an der Donau,Austria,Lower Austria,2773549
Klosterneuburg,Austria,Lower Austria,2773913
Klagenfurt am WÃ¶rthersee,Austria,Carinthia,2774326
Kapfenberg,Austria,Styria,2774773
Innsbruck,Austria,Tyrol,2775220
Hallein,Austria,Salzburg,2776951
Graz,Austria,Styria,2778067
Feldkirch,Austria,Vorarlberg,2779674
Dornbirn,Austria,Vorarlberg,2780741
Bregenz,Austria,Vorarlberg,2781503
Braunau am Inn,Austria,Upper Austria,2781520
Baden,Austria,Lower Austria,2782067
Amstetten,Austria,Lower Austria,2782555
Ansfelden,Austria,Salzburg,3323063
Whyalla,Australia,South Australia,2058430
Rockingham,Australia,Western Australia,2062338
Prospect,Australia,South Australia,2062944
Port Hedland,Australia,Western Australia,2063042
Perth,Australia,Western Australia,2063523
Murray Bridge,Australia,South Australia,2065176
Mount Isa,Australia,Queensland,2065594
Morphett Vale,Australia,South Australia,2065740
Mandurah,Australia,Western Australia,2067119
Kwinana,Australia,Western Australia,2068079
Kalgoorlie,Australia,Western Australia,2068823
Gosnells,Australia,Western Australia,2070571
Geraldton,Australia,Western Australia,2070998
Gawler,Australia,South Australia,2071059
Fremantle,Australia,Western Australia,2071223
Darwin,Australia,Northern Territory,2073124
Busselton,Australia,Western Australia,2075265
Bunbury,Australia,Western Australia,2075432
Armadale,Australia,Western Australia,2077579
Alice Springs,Australia,Northern Territory,2077895
Albany,Australia,Western Australia,2077963
Adelaide,Australia,South Australia,2078025
Woodridge,Australia,Queensland,2143069
Wodonga,Australia,Victoria,2143285
Werribee,Australia,Victoria,2144095
Warrnambool,Australia,Victoria,2144528
Wantirna South,Australia,Victoria,2144728
Wangaratta,Australia,Victoria,2144764
Wagga Wagga,Australia,New South Wales,2145110
Traralgon,Australia,Victoria,2146108
Townsville,Australia,Queensland,2146142
Toowoomba,Australia,Queensland,2146268
Thornbury,Australia,Victoria,2146793
Thomastown,Australia,Victoria,2146827
Tarneit,Australia,Victoria,2147357
Taree,Australia,New South Wales,2147381
Tamworth,Australia,New South Wales,2147497
Sydney,Australia,New South Wales,2147714
Surfers Paradise,Australia,Queensland,2147849
Sunnybank,Australia,Queensland,2147892
Sunbury,Australia,Victoria,2147914
Port Stephens,Australia,New South Wales,2148398
Springvale,Australia,Victoria,2148591
Southport,Australia,Queensland,2148928
South Grafton,Australia,New South Wales,2148997
Shepparton,Australia,Victoria,2149645
Seaford,Australia,Victoria,2149975
Saint Kilda,Australia,Victoria,2150660
Saint Albans,Australia,Victoria,2150717
Rowville,Australia,Victoria,2150894
Rockhampton,Australia,Queensland,2151437
Richmond,Australia,Victoria,2151649
Reservoir,Australia,Victoria,2151716
Queanbeyan,Australia,New South Wales,2152286
Quakers Hill,Australia,New South Wales,2152329
Preston,Australia,Victoria,2152558
Port Macquarie,Australia,New South Wales,2152659
Point Cook,Australia,Victoria,2152819
Pakenham South,Australia,Victoria,2153951
Orange,Australia,New South Wales,2154219
Nowra,Australia,New South Wales,2154787
Northcote,Australia,Victoria,2155001
Noble Park,Australia,Victoria,2155204
Newcastle,Australia,New South Wales,2155472
Nerang,Australia,Queensland,2155542
Narre Warren,Australia,Victoria,2155718
Narangba,Australia,Queensland,2155787
Mulgrave,Australia,Victoria,2156340
Mount Martha,Australia,Victoria,2156578
Mount Gambier,Australia,South Australia,2156643
Mount Eliza,Australia,Victoria,2156663
Mosman,Australia,New South Wales,2156813
Mornington,Australia,Victoria,2156878
Morayfield,Australia,Queensland,2156934
Moe,Australia,Victoria,2157343
Mill Park,Australia,Victoria,2157635
Mildura,Australia,Victoria,2157698
Melton,Australia,Victoria,2158151
Melbourne,Australia,Victoria,2158177
Maryborough,Australia,Queensland,2158562
Marrickville,Australia,New South Wales,2158626
Maroubra,Australia,New South Wales,2158651
Maitland,Australia,New South Wales,2159045
Mackay,Australia,Queensland,2159220
Liverpool,Australia,New South Wales,2159851
Lismore,Australia,New South Wales,2160063
Lilydale,Australia,Victoria,2160188
Launceston,Australia,Tasmania,2160517
Lara,Australia,Victoria,2160560
Langwarrin,Australia,Victoria,2160582
Lalor,Australia,Victoria,2160706
Keysborough,Australia,Victoria,2161532
Kew,Australia,Victoria,2161540
Katoomba,Australia,New South Wales,2161776
Hornsby,Australia,New South Wales,2163137
Hobart,Australia,Tasmania,2163355
Hawthorn South,Australia,Victoria,2163776
Hampton Park,Australia,Victoria,2163990
Griffith,Australia,New South Wales,2164422
Greensborough,Australia,Victoria,2164515
Granville,Australia,New South Wales,2164691
Goulburn,Australia,New South Wales,2164837
Gold Coast,Australia,Queensland,2165087
Glenroy,Australia,Victoria,2165200
Glenferrie,Australia,Victoria,2165329
Gladstone,Australia,Queensland,2165478
Geelong,Australia,Victoria,2165798
Frankston East,Australia,Victoria,2166143
Frankston,Australia,Victoria,2166144
Forster,Australia,New South Wales,2166309
Essendon,Australia,Victoria,2167208
Epping,Australia,Victoria,2167279
Epping,Australia,New South Wales,2167280
Engadine,Australia,New South Wales,2167312
Eltham,Australia,Victoria,2167445
Echuca,Australia,Victoria,2167817
Earlwood,Australia,New South Wales,2167949
Dubbo,Australia,New South Wales,2168305
Doncaster East,Australia,Victoria,2168605
Doncaster,Australia,Victoria,2168607
Devonport,Australia,Tasmania,2168943
Deer Park,Australia,Victoria,2169145
Deception Bay,Australia,Queensland,2169220
Dandenong,Australia,Victoria,2169460
Cronulla,Australia,New South Wales,2169956
Cranbourne,Australia,Victoria,2170078
Cranbourne,Australia,Victoria,2170079
Craigieburn,Australia,Victoria,2170089
Coffs Harbour,Australia,New South Wales,2171085
Coburg,Australia,Victoria,2171168
Clayton,Australia,Victoria,2171400
Wollongong,Australia,New South Wales,2171507
Cessnock,Australia,New South Wales,2171845
Castle Hill,Australia,New South Wales,2172111
Carrum Downs,Australia,Victoria,2172191
Carnegie,Australia,Victoria,2172264
Carlingford,Australia,New South Wales,2172303
Caringbah,Australia,New South Wales,2172311
Canberra,Australia,Australian Capital Territory,2172517
Camberwell,Australia,Victoria,2172686
Caloundra,Australia,Queensland,2172710
Cairns,Australia,Queensland,2172797
Caboolture,Australia,Queensland,2172832
Burnie,Australia,Tasmania,2173125
Bundaberg,Australia,Queensland,2173323
Buderim,Australia,Queensland,2173605
Brunswick,Australia,Victoria,2173741
Broken Hill,Australia,New South Wales,2173911
Brisbane,Australia,Queensland,2174003
Boronia,Australia,Victoria,2174580
Blacktown,Australia,New South Wales,2175411
Berwick,Australia,Victoria,2176031
Bendigo,Australia,Victoria,2176187
Baulkham Hills,Australia,New South Wales,2176592
Bathurst,Australia,New South Wales,2176632
Banora Point,Australia,New South Wales,2176934
Bankstown,Australia,New South Wales,2176947
Ballarat,Australia,Victoria,2177091
Auburn,Australia,New South Wales,2177513
Ashfield,Australia,New South Wales,2177565
Armidale,Australia,New South Wales,2177671
Albury,Australia,New South Wales,2178174
South Brisbane,Australia,Queensland,2207259
Cheltenham,Australia,Victoria,2207618
Randwick,Australia,New South Wales,2208285
Dee Why,Australia,New South Wales,2208305
Umina,Australia,New South Wales,2208313
Palmerston,Australia,Northern Territory,6301965
Bracken Ridge,Australia,Queensland,6943558
North Ryde,Australia,New South Wales,7281782
Hoppers Crossing,Australia,Victoria,7281807
Logan City,Australia,Queensland,7281838
Carindale,Australia,Queensland,7281839
Paramatta,Australia,New South Wales,7281840
Ferntree Gully,Australia,Victoria,7281850
City of Parramatta,Australia,New South Wales,7302259
Adelaide Hills,Australia,South Australia,7302628
Canning Vale,Australia,Western Australia,7302631
Glenmore Park,Australia,New South Wales,7302642
Glen Iris,Australia,Victoria,7932612
Balwyn North,Australia,Victoria,7932629
Carnegie,Australia,Victoria,7932636
Malvern East,Australia,Victoria,7932638
Brighton East,Australia,Victoria,7932646
Booval,Australia,Queensland,7932654
St Albans,Australia,Victoria,8015209
Endeavour Hills,Australia,Victoria,8347325
Clayton,Australia,Victoria,8347717
Taylors Lakes,Australia,Victoria,8347847
Roxburgh Park,Australia,Victoria,8347896
Wyndham Vale,Australia,Victoria,8348078
Willetton,Australia,Western Australia,8348101
Thornbury,Australia,Victoria,8348734
Thornlie,Australia,Western Australia,8349108
Hillside,Australia,Victoria,8349243
Bundoora,Australia,Victoria,8349381
Forest Lake,Australia,Queensland,9957340
Sunnybank Hills,Australia,Queensland,9957350
Narre Warren South,Australia,Victoria,9972518
Dandenong North,Australia,Victoria,9972522
Frankston South,Australia,Victoria,9972527
Sunshine West,Australia,Victoria,9972578
Altona Meadows,Australia,Victoria,9972579
West Pennant,Australia,New South Wales,9972964
Oranjestad,Aruba,N/A,3577154
Babijn,Aruba,N/A,3577277
Angochi,Aruba,N/A,3577284
Mariehamn,Aland Islands,Mariehamns stad,3041732
Xankandi,Azerbaijan,XankÇndi,146970
ÆhmÉ™dbÉ™yli,Azerbaijan,SaatlÄ±,147059
Shushi,Azerbaijan,ÅžuÅŸa,147105
Salyan,Azerbaijan,Salyan,147271
SaatlÄ±,Azerbaijan,SaatlÄ±,147288
NeftÃ§ala,Azerbaijan,NeftÃ§ala,147425
Nakhchivan,Azerbaijan,Nakhichevan,147429
Lankaran,Azerbaijan,LÉ™nkÉ™ran,147622
Imishli,Azerbaijan,Ä°miÅŸli,147982
Fizuli,Azerbaijan,FÃ¼zuli,148106
Dzhalilabad,Azerbaijan,Jalilabad,148290
Pushkino,Azerbaijan,BilÇsuvar,148340
Beylagan,Azerbaijan,BeylÉ™qan,148354
Astara,Azerbaijan,Astara,148445
Åžirvan,Azerbaijan,Shirvan,148565
AÄŸdam,Azerbaijan,AÄŸdam,148619
Zaqatala,Azerbaijan,Zaqatala,584596
Zabrat,Azerbaijan,Baki,584614
Yevlakh,Azerbaijan,Yevlax City,584649
Yelenendorf,Azerbaijan,Goygol Rayon,584716
XaÃ§maz,Azerbaijan,XaÃ§maz,584717
Ujar,Azerbaijan,Ucar,584791
Terter,Azerbaijan,TÇrtÇr,584871
SumqayÄ±t,Azerbaijan,Sumqayit,584923
QaraÃ§uxur,Azerbaijan,Baki,585103
Shamkhor,Azerbaijan,ÅžÇmkir,585152
Shamakhi,Azerbaijan,ÅžamaxÄ±,585156
Sheki,Azerbaijan,Shaki City,585170
SabunÃ§u,Azerbaijan,Baki,585184
Sabirabad,Azerbaijan,Sabirabad,585187
Qusar,Azerbaijan,Qusar,585220
Quba,Azerbaijan,Quba,585221
HacÄ±qabul,Azerbaijan,HacÄ±qabul,585225
Qazax,Azerbaijan,Qazax,585226
HacÄ± Zeynalabdin,Azerbaijan,Sumqayit,585379
Mingelchaur,Azerbaijan,MingÇcevir,585514
MaÅŸtaÄŸa,Azerbaijan,Baki,585557
Mardakan,Azerbaijan,Baki,585568
LÃ¶kbatan,Azerbaijan,Baki,585630
Kyurdarmir,Azerbaijan,KÃ¼rdÇmir,585763
Khirdalan,Azerbaijan,AbÅŸeron,585915
Yeni SuraxanÄ±,Azerbaijan,Baki,586340
Geoktschai,Azerbaijan,GÃ¶yÃ§ay,586427
HÃ¶vsan,Azerbaijan,Baki,586429
Ganja,Azerbaijan,GÇncÇ,586523
Divichibazar,Azerbaijan,Shabran,586763
Buzovna,Azerbaijan,Baki,586925
Biny Selo,Azerbaijan,Baki,586968
Barda,Azerbaijan,BÇrdÇ,587057
Bilajari,Azerbaijan,Baki,587078
Baku,Azerbaijan,Baki,587084
Amirdzhan,Azerbaijan,Baki,587261
Aghsu,Azerbaijan,AÄŸsu,587361
AÄŸdaÅŸ,Azerbaijan,AÄŸdaÅŸ,587378
Agdzhabedy,Azerbaijan,AÄŸcabÇdi,587384
BakÄ±xanov,Azerbaijan,Baki,824003
Zenica,Bosnia and Herzegovina,Federation of Bosnia and Herzegovina,3186573
Visoko,Bosnia and Herzegovina,Federation of Bosnia and Herzegovina,3187609
Velika KladuÅ¡a,Bosnia and Herzegovina,Federation of Bosnia and Herzegovina,3188225
Tuzla,Bosnia and Herzegovina,Federation of Bosnia and Herzegovina,3188582
Trebinje,Bosnia and Herzegovina,Republika Srpska,3188893
Travnik,Bosnia and Herzegovina,Federation of Bosnia and Herzegovina,3188924
Sarajevo,Bosnia and Herzegovina,Federation of Bosnia and Herzegovina,3191281
Prijedor,Bosnia and Herzegovina,Republika Srpska,3192409
Mostar,Bosnia and Herzegovina,Federation of Bosnia and Herzegovina,3194828
GradaÄac,Bosnia and Herzegovina,Federation of Bosnia and Herzegovina,3199744
GraÄanica,Bosnia and Herzegovina,Federation of Bosnia and Herzegovina,3199779
GoraÅ¾de,Bosnia and Herzegovina,Federation of Bosnia and Herzegovina,3200396
Doboj,Bosnia and Herzegovina,Republika Srpska,3201984
Cazin,Bosnia and Herzegovina,Federation of Bosnia and Herzegovina,3202822
Bugojno,Bosnia and Herzegovina,Federation of Bosnia and Herzegovina,3203099
BrÄko,Bosnia and Herzegovina,BrÄko,3203521
Bosanska Krupa,Bosnia and Herzegovina,Federation of Bosnia and Herzegovina,3203653
Bijeljina,Bosnia and Herzegovina,Republika Srpska,3204186
BihaÄ‡,Bosnia and Herzegovina,Federation of Bosnia and Herzegovina,3204222
Banja Luka,Bosnia and Herzegovina,Republika Srpska,3204541
Konjic,Bosnia and Herzegovina,Federation of Bosnia and Herzegovina,3337476
Bridgetown,Barbados,Saint Michael,3374036
ThÄkurgaon,Bangladesh,Rangpur Division,1185092
TeknÄf,Bangladesh,Chittagong,1185095
Tungi,Bangladesh,Dhaka,1185098
Sylhet,Bangladesh,Sylhet,1185099
DohÄr,Bangladesh,Dhaka,1185100
JamÄlpur,Bangladesh,Dhaka,1185106
Shibganj,Bangladesh,RÄjshÄhi,1185108
SÄtkhira,Bangladesh,Khulna,1185111
SirÄjganj,Bangladesh,RÄjshÄhi,1185115
Netrakona,Bangladesh,Dhaka,1185116
Narsingdi,Bangladesh,Dhaka,1185117
SandwÄ«p,Bangladesh,Chittagong,1185120
ShÄhzÄdpur,Bangladesh,RÄjshÄhi,1185121
RÄmganj,Bangladesh,Chittagong,1185127
RÄjshÄhi,Bangladesh,RÄjshÄhi,1185128
Pirojpur,Bangladesh,BarisÄl,1185138
Panchagarh,Bangladesh,Rangpur Division,1185141
Patiya,Bangladesh,Chittagong,1185148
Parbatipur,Bangladesh,Rangpur Division,1185149
NÄrÄyanganj,Bangladesh,Dhaka,1185155
NÄlchiti,Bangladesh,BarisÄl,1185156
NÄgarpur,Bangladesh,Dhaka,1185159
Nageswari,Bangladesh,Rangpur Division,1185160
Mymensingh,Bangladesh,Dhaka,1185162
MuktÄgÄcha,Bangladesh,Dhaka,1185164
MirzÄpur,Bangladesh,Dhaka,1185165
Maulavi BÄzÄr,Bangladesh,Sylhet,1185166
Morrelgonj,Bangladesh,Khulna,1185167
Mehendiganj,Bangladesh,BarisÄl,1185171
Mathba,Bangladesh,BarisÄl,1185173
Lalmanirhat,Bangladesh,Rangpur Division,1185181
LÄkshÄm,Bangladesh,Chittagong,1185183
Comilla,Bangladesh,Chittagong,1185186
Rangpur,Bangladesh,Rangpur Division,1185188
Kushtia,Bangladesh,Khulna,1185191
KÄlÄ«ganj,Bangladesh,Khulna,1185199
JhingergÄcha,Bangladesh,Khulna,1185204
Joypur HÄt,Bangladesh,RÄjshÄhi,1185206
Ishurdi,Bangladesh,RÄjshÄhi,1185207
Habiganj,Bangladesh,Sylhet,1185209
Gaurnadi,Bangladesh,BarisÄl,1185210
Gafargaon,Bangladesh,Dhaka,1185218
Feni,Bangladesh,Chittagong,1185224
RÄipur,Bangladesh,Chittagong,1185236
Sarankhola,Bangladesh,Khulna,1185239
Dhaka,Bangladesh,Dhaka,1185241
ChilmÄri,Bangladesh,Rangpur Division,1185247
ChhÄgalnÄiya,Bangladesh,Chittagong,1185249
LÄlmohan,Bangladesh,BarisÄl,1185251
Khagrachhari,Bangladesh,Chittagong,1185252
ChhÄtak,Bangladesh,Sylhet,1185254
BhÄtpÄra Abhaynagar,Bangladesh,Khulna,1185260
BherÄmÄra,Bangladesh,Khulna,1185262
Bhairab BÄzÄr,Bangladesh,Dhaka,1185263
BÄndarban,Bangladesh,Chittagong,1185270
KÄlia,Bangladesh,Khulna,1185272
Baniachang,Bangladesh,Sylhet,1185274
BÄjitpur,Bangladesh,Dhaka,1185276
Badarganj,Bangladesh,Rangpur Division,1185283
Narail,Bangladesh,Khulna,1185293
TungipÄra,Bangladesh,Dhaka,1185920
SarishÄbÄri,Bangladesh,Dhaka,1188569
Sakhipur,Bangladesh,Dhaka,1189056
RaojÄn,Bangladesh,Chittagong,1189638
Phultala,Bangladesh,Khulna,1191139
PÄlang,Bangladesh,Dhaka,1191368
PÄr Naogaon,Bangladesh,RÄjshÄhi,1192366
NabÄ«nagar,Bangladesh,Chittagong,1193823
LakshmÄ«pur,Bangladesh,Chittagong,1196292
Kesabpur,Bangladesh,Khulna,1197895
HÄjÄ«ganj,Bangladesh,Chittagong,1201753
FarÄ«dpur,Bangladesh,Dhaka,1203344
DinÄjpur,Bangladesh,Rangpur Division,1203891
Uttar Char Fasson,Bangladesh,Khulna,1205481
Chittagong,Bangladesh,Chittagong,1205733
Char BhadrÄsan,Bangladesh,Dhaka,1207047
Bera,Bangladesh,RÄjshÄhi,1209562
BurhÄnuddin,Bangladesh,BarisÄl,1210565
SÄtkania,Bangladesh,Chittagong,1336133
Coxâ€™s BÄzÄr,Bangladesh,Chittagong,1336134
Khulna,Bangladesh,Khulna,1336135
Bhola,Bangladesh,BarisÄl,1336136
BarisÄl,Bangladesh,BarisÄl,1336137
Jessore,Bangladesh,Khulna,1336140
PÄbna,Bangladesh,RÄjshÄhi,1336143
TÄngÄil,Bangladesh,Dhaka,1336144
Bogra,Bangladesh,RÄjshÄhi,1337233
PÄ«rgaaj,Bangladesh,Rangpur Division,1337239
NawÄbganj,Bangladesh,RÄjshÄhi,1337240
MÄdÄrÄ«pur,Bangladesh,Dhaka,1337245
Sherpur,Bangladesh,Dhaka,1337248
Kishorganj,Bangladesh,Dhaka,1337249
Manikchari,Bangladesh,Chittagong,1462681
BhÄndÄria,Bangladesh,BarisÄl,1477498
Fatikchari,Bangladesh,Chittagong,6414184
Saidpur,Bangladesh,RÄjshÄhi,6545349
Azimpur,Bangladesh,Dhaka,7701354
Paltan,Bangladesh,Dhaka,9827976
Zwijndrecht,Belgium,Flanders,2783081
Zwevegem,Belgium,Flanders,2783089
Zottegem,Belgium,Flanders,2783175
Zonhoven,Belgium,Flanders,2783188
Zoersel,Belgium,Flanders,2783204
Zemst,Belgium,Flanders,2783274
Zele,Belgium,Flanders,2783293
Zedelgem,Belgium,Flanders,2783308
Zaventem,Belgium,Flanders,2783310
Wuustwezel,Belgium,Flanders,2783416
Willebroek,Belgium,Flanders,2783632
Wevelgem,Belgium,Flanders,2783759
Wetteren,Belgium,Flanders,2783763
Westerlo,Belgium,Flanders,2783801
Wervik,Belgium,Flanders,2783820
Wavre,Belgium,Wallonia,2783941
Waterloo,Belgium,Wallonia,2783985
Waregem,Belgium,Flanders,2784068
Walcourt,Belgium,Wallonia,2784189
VisÃ©,Belgium,Wallonia,2784548
Vilvoorde,Belgium,Flanders,2784604
Verviers,Belgium,Wallonia,2784821
Turnhout,Belgium,Flanders,2785141
Tubize,Belgium,Wallonia,2785169
Tournai,Belgium,Wallonia,2785341
Torhout,Belgium,Flanders,2785364
Tongeren,Belgium,Flanders,2785389
Tienen,Belgium,Flanders,2785470
Tielt,Belgium,Flanders,2785476
Tessenderlo,Belgium,Flanders,2785612
Tervuren,Belgium,Flanders,2785622
Temse,Belgium,Flanders,2785778
Stekene,Belgium,Flanders,2786087
Stabroek,Belgium,Flanders,2786229
Soumagne,Belgium,Wallonia,2786344
Soignies,Belgium,Wallonia,2786420
Sint-Truiden,Belgium,Flanders,2786545
Sint-Pieters-Leeuw,Belgium,Flanders,2786559
Sint-Niklaas,Belgium,Flanders,2786578
Sint-Kruis,Belgium,Flanders,2786634
Sint-Katelijne-Waver,Belgium,Flanders,2786641
Sint-Gillis-Waas,Belgium,Flanders,2786694
Sint-Genesius-Rode,Belgium,Flanders,2786700
Seraing,Belgium,Wallonia,2786824
Schoten,Belgium,Flanders,2786963
Schilde,Belgium,Flanders,2787048
Saint-Nicolas,Belgium,Wallonia,2787356
Saint-Ghislain,Belgium,Wallonia,2787416
Rotselaar,Belgium,Flanders,2787662
Ronse,Belgium,Flanders,2787769
Roeselare,Belgium,Flanders,2787889
Rixensart,Belgium,Wallonia,2787989
Riemst,Belgium,Flanders,2788088
Ranst,Belgium,Flanders,2788348
Quaregnon,Belgium,Wallonia,2788499
Puurs,Belgium,Flanders,2788506
Putte,Belgium,Flanders,2788521
Poperinge,Belgium,Flanders,2788726
Pont-Ã -Celles,Belgium,Wallonia,2788765
PÃ©ruwelz,Belgium,Wallonia,2789162
Peer,Belgium,Flanders,2789232
Overijse,Belgium,Flanders,2789413
Oupeye,Belgium,Wallonia,2789471
Oudenaarde,Belgium,Flanders,2789529
Oostkamp,Belgium,Flanders,2789751
Ostend,Belgium,Flanders,2789786
Nivelles,Belgium,Wallonia,2790101
Ninove,Belgium,Flanders,2790114
Nijlen,Belgium,Flanders,2790135
Neerpelt,Belgium,Flanders,2790357
Namur,Belgium,Wallonia,2790471
Mouscron,Belgium,Wallonia,2790595
Mortsel,Belgium,Flanders,2790676
Morlanwelz-Mariemont,Belgium,Wallonia,2790697
Mons,Belgium,Wallonia,2790869
Mol,Belgium,Flanders,2791067
Middelkerke,Belgium,Flanders,2791194
Merelbeke,Belgium,Flanders,2791315
Menen,Belgium,Flanders,2791343
Meise,Belgium,Flanders,2791424
Mechelen,Belgium,Flanders,2791537
Marche-en-Famenne,Belgium,Wallonia,2791744
Manage,Belgium,Wallonia,2791814
Maldegem,Belgium,Flanders,2791857
Maasmechelen,Belgium,Flanders,2791961
Maaseik,Belgium,Flanders,2791964
Louvain-la-Neuve,Belgium,Wallonia,2792073
Londerzeel,Belgium,Flanders,2792165
Lommel,Belgium,Flanders,2792179
Lokeren,Belgium,Flanders,2792196
Lochristi,Belgium,Flanders,2792235
Lille,Belgium,Flanders,2792360
Lier,Belgium,Flanders,2792397
LiÃ¨ge,Belgium,Wallonia,2792413
Leuven,Belgium,Flanders,2792482
Lessines,Belgium,Wallonia,2792567
Lede,Belgium,Flanders,2793077
Lebbeke,Belgium,Flanders,2793144
Lanaken,Belgium,Flanders,2793446
La LouviÃ¨re,Belgium,Wallonia,2793508
Kortrijk,Belgium,Flanders,2794055
Kortenberg,Belgium,Flanders,2794070
Kontich,Belgium,Flanders,2794117
Koksijde,Belgium,Flanders,2794166
Knokke-Heist,Belgium,Flanders,2794210
Kasterlee,Belgium,Flanders,2794663
Kapellen,Belgium,Flanders,2794730
Kalmthout,Belgium,Flanders,2794788
Izegem,Belgium,Flanders,2795009
Ieper,Belgium,Flanders,2795100
Huy,Belgium,Wallonia,2795113
Houthalen,Belgium,Flanders,2795261
Hoogstraten,Belgium,Flanders,2795398
Hoboken,Belgium,Flanders,2795730
Heusden,Belgium,Flanders,2795800
Herzele,Belgium,Flanders,2795908
Herve,Belgium,Wallonia,2795912
Herstal,Belgium,Wallonia,2795930
Herentals,Belgium,Flanders,2796009
Herent,Belgium,Flanders,2796012
Helchteren,Belgium,Flanders,2796132
Heist-op-den-Berg,Belgium,Flanders,2796153
Hasselt,Belgium,Flanders,2796491
Harelbeke,Belgium,Flanders,2796542
Hamme,Belgium,Flanders,2796637
Halle,Belgium,Flanders,2796696
Haaltert,Belgium,Flanders,2796833
Grimbergen,Belgium,Flanders,2797114
Geraardsbergen,Belgium,Flanders,2797638
Gent,Belgium,Flanders,2797656
Genk,Belgium,Flanders,2797670
Gembloux,Belgium,Wallonia,2797713
Geel,Belgium,Flanders,2797779
Frameries,Belgium,Wallonia,2798023
Fleurus,Belgium,Wallonia,2798297
FlÃ©ron,Belgium,Wallonia,2798301
FlÃ©malle-Haute,Belgium,Wallonia,2798307
Evergem,Belgium,Flanders,2798551
Eupen,Belgium,Wallonia,2798573
Essen,Belgium,Flanders,2798615
Eeklo,Belgium,Flanders,2798987
Edegem,Belgium,Flanders,2799007
Duffel,Belgium,Flanders,2799090
Dour,Belgium,Wallonia,2799226
Dilbeek,Belgium,Flanders,2799365
Diksmuide,Belgium,Flanders,2799369
Diest,Belgium,Flanders,2799397
Diepenbeek,Belgium,Flanders,2799412
Destelbergen,Belgium,Flanders,2799496
Dendermonde,Belgium,Flanders,2799645
Denderleeuw,Belgium,Flanders,2799647
Deinze,Belgium,Flanders,2799746
Courcelles,Belgium,Wallonia,2800063
Colfontaine,Belgium,Wallonia,2800220
Chaudfontaine,Belgium,Wallonia,2800438
ChÃ¢telet,Belgium,Wallonia,2800448
Chasse Royale,Belgium,Wallonia,2800461
Charleroi,Belgium,Wallonia,2800481
Brussels,Belgium,Brussels Capital,2800866
Brugge,Belgium,Flanders,2800931
Brecht,Belgium,Flanders,2801106
Brasschaat,Belgium,Flanders,2801117
Braine-le-Comte,Belgium,Wallonia,2801150
Braine-l'Alleud,Belgium,Wallonia,2801154
Boussu,Belgium,Wallonia,2801226
Bornem,Belgium,Flanders,2801447
Boom,Belgium,Flanders,2801494
Blankenberge,Belgium,Flanders,2801858
Binche,Belgium,Wallonia,2801922
Bilzen,Belgium,Flanders,2801924
Beveren,Belgium,Flanders,2802031
Beringen,Belgium,Flanders,2802170
Beersel,Belgium,Flanders,2802433
Beerse,Belgium,Flanders,2802435
Balen,Belgium,Flanders,2802743
Ath,Belgium,Wallonia,2803010
Asse,Belgium,Flanders,2803033
Arlon,Belgium,Wallonia,2803073
Antwerpen,Belgium,Flanders,2803138
Ans,Belgium,Wallonia,2803160
Andenne,Belgium,Wallonia,2803204
Aarschot,Belgium,Flanders,2803429
Aalter,Belgium,Flanders,2803443
Aalst,Belgium,Flanders,2803448
Zorgo,Burkina Faso,Plateau-Central,2353197
Yako,Burkina Faso,Nord,2353688
Tougan,Burkina Faso,Boucle du Mouhoun,2354176
Titao,Burkina Faso,Nord,2354349
Tenkodogo,Burkina Faso,Centre-Est,2354675
RÃ©o,Burkina Faso,Centre-Ouest,2356228
PÃ´,Burkina Faso,Centre-Sud,2356454
Ouahigouya,Burkina Faso,Nord,2357043
Ouagadougou,Burkina Faso,Centre,2357048
Nouna,Burkina Faso,Boucle du Mouhoun,2357163
Manga,Burkina Faso,Centre-Sud,2358100
LÃ©o,Burkina Faso,Centre-Ouest,2358382
KoupÃ©la,Burkina Faso,Centre-Est,2358738
Koudougou,Burkina Faso,Centre-Ouest,2358946
Kongoussi,Burkina Faso,Centre-Nord,2359142
Kombissiri,Burkina Faso,Centre-Sud,2359227
Kokologo,Burkina Faso,Centre-Ouest,2359317
Kaya,Burkina Faso,Centre-Nord,2359608
HoundÃ©,Burkina Faso,High-Basins,2360073
Gourcy,Burkina Faso,Nord,2360238
Garango,Burkina Faso,Centre-Est,2360615
Fada N'gourma,Burkina Faso,Est,2360886
Dori,Burkina Faso,Sahel,2361082
Djibo,Burkina Faso,Sahel,2361177
Diapaga,Burkina Faso,Est,2361373
DÃ©dougou,Burkina Faso,Boucle du Mouhoun,2361477
BoussÃ©,Burkina Faso,Plateau-Central,2361845
Boulsa,Burkina Faso,Centre-Nord,2361946
Bobo-Dioulasso,Burkina Faso,High-Basins,2362344
Banfora,Burkina Faso,Cascades,2362909
Gaoua,Burkina Faso,Southwest,2577162
Orodara,Burkina Faso,High-Basins,2577164
Yambol,Bulgaria,Yambol,725578
Vratsa,Bulgaria,Vratsa,725712
Vidin,Bulgaria,Vidin,725905
Velingrad,Bulgaria,Pazardzhik,725988
Veliko TÅ­rnovo,Bulgaria,Veliko TÅ­rnovo,725993
Varna,Bulgaria,Varna,726050
Targovishte,Bulgaria,TÅ­rgovishte,726174
Troyan,Bulgaria,Lovech,726320
Dobrich,Bulgaria,Dobrich,726418
Svishtov,Bulgaria,Veliko TÅ­rnovo,726534
Svilengrad,Bulgaria,Khaskovo,726546
Stara Zagora,Bulgaria,Stara Zagora,726848
Dupnitsa,Bulgaria,Kyustendil,726872
Sofia,Bulgaria,Sofia-Capital,727011
Smolyan,Bulgaria,Smolyan,727030
Sliven,Bulgaria,Sliven,727079
Silistra,Bulgaria,Silistra,727221
Shumen,Bulgaria,Shumen,727233
Sevlievo,Bulgaria,Gabrovo,727337
Sandanski,Bulgaria,Blagoevgrad,727447
Samokov,Bulgaria,Sofiya,727462
Ruse,Bulgaria,Ruse,727523
Razgrad,Bulgaria,Razgrad,727696
Rakovski,Bulgaria,Plovdiv,727791
Popovo,Bulgaria,TÅ­rgovishte,728075
Plovdiv,Bulgaria,Plovdiv,728193
Pleven,Bulgaria,Pleven,728203
Petrich,Bulgaria,Blagoevgrad,728288
Peshtera,Bulgaria,Pazardzhik,728317
Pernik,Bulgaria,Pernik,728330
Pazardzhik,Bulgaria,Pazardzhik,728378
Panagyurishte,Bulgaria,Pazardzhik,728448
Nova Zagora,Bulgaria,Sliven,728742
Montana,Bulgaria,Montana,729114
Lovech,Bulgaria,Lovech,729559
Lom,Bulgaria,Montana,729581
Kyustendil,Bulgaria,Kyustendil,729730
Kardzhali,Bulgaria,KÅ­rdzhali,729794
Haskovo,Bulgaria,Khaskovo,730435
Kharmanli,Bulgaria,Khaskovo,730442
KazanlÅ­k,Bulgaria,Stara Zagora,730496
Karnobat,Bulgaria,Burgas,730559
Karlovo,Bulgaria,Plovdiv,730565
Gotse Delchev,Bulgaria,Blagoevgrad,731108
Gorna Oryakhovitsa,Bulgaria,Veliko TÅ­rnovo,731233
Gabrovo,Bulgaria,Gabrovo,731549
Dimitrovgrad,Bulgaria,Khaskovo,732263
Chirpan,Bulgaria,Stara Zagora,732452
Cherven Bryag,Bulgaria,Pleven,732491
Burgas,Bulgaria,Burgas,732770
Botevgrad,Bulgaria,Sofiya,733014
Blagoevgrad,Bulgaria,Blagoevgrad,733191
Berkovitsa,Bulgaria,Montana,733264
Aytos,Bulgaria,Burgas,733579
Asenovgrad,Bulgaria,Plovdiv,733618
Sitrah,Bahrain,Manama,290104
MadÄ«nat â€˜ÄªsÃ¡,Bahrain,Southern Governorate,290187
Jidd á¸¨afÅŸ,Bahrain,Manama,290215
MadÄ«nat á¸¨amad,Bahrain,Central Governorate,290247
DÄr Kulayb,Bahrain,Southern Governorate,290269
Al Muharraq,Bahrain,Muharraq,290332
Manama,Bahrain,Manama,290340
Ar RifÄâ€˜,Bahrain,Southern Governorate,385038
Makamba,Burundi,Makamba,422232
Bururi,Burundi,Bururi,423328
Bujumbura,Burundi,Bujumbura Mairie,425378
Muramvya,Burundi,Muramvya,425551
Gitega,Burundi,Gitega,426272
Ruyigi,Burundi,Ruyigi,426700
Ngozi,Burundi,Ngozi,430569
Kayanza,Burundi,Kayanza,430952
Muyinga,Burundi,Muyinga,431748
Rutana,Burundi,Rutana,433635
Tchaourou,Benin,Borgou,2391377
TanguiÃ©ta,Benin,Atakora,2391455
SavÃ©,Benin,Collines,2391893
Savalou,Benin,Collines,2391895
SakÃ©tÃ©,Benin,Plateau,2392009
Porto-Novo,Benin,QuÃ©mÃ©,2392087
PobÃ©,Benin,Plateau,2392108
Parakou,Benin,Borgou,2392204
Ouidah,Benin,Atlantique,2392308
Nikki,Benin,Borgou,2392505
Natitingou,Benin,Atakora,2392601
Malanville,Benin,Atakora,2392837
Lokossa,Benin,Mono,2392897
KÃ©tou,Benin,Plateau,2393551
Kandi,Benin,Alibori,2393693
Dogbo,Benin,Kouffo,2394545
Djougou,Benin,Donga,2394560
Dassa-ZoumÃ©,Benin,Collines,2394711
CovÃ©,Benin,Zou,2394814
Cotonou,Benin,Littoral,2394819
ComÃ©,Benin,Mono,2394824
Bohicon,Benin,Zou,2395049
BembÃ¨rÃ¨kÃ¨,Benin,Borgou,2395182
Bassila,Benin,Donga,2395261
Banikoara,Benin,Alibori,2395317
AplahouÃ©,Benin,Kouffo,2395568
Allada,Benin,Atlantique,2395635
Abomey-Calavi,Benin,Atlantique,2395914
Abomey,Benin,Zou,2395915
Gustavia,Saint Barthelemy,N/A,3579132
Hamilton,Bermuda,Hamilton city,3573197
Tutong,Brunei,Tutong,1820071
Seria,Brunei,Belait,1820187
Kuala Belait,Brunei,Belait,1820491
Bandar Seri Begawan,Brunei,Brunei and Muara,1820906
Yacuiba,Bolivia,Tarija,3901178
Warnes,Bolivia,Santa Cruz,3901301
VillazÃ³n,Bolivia,PotosÃ­,3901501
Villa YapacanÃ­,Bolivia,Santa Cruz,3901504
Villamontes,Bolivia,Tarija,3901547
Tupiza,Bolivia,PotosÃ­,3902202
Trinidad,Bolivia,El Beni,3902377
Tarija,Bolivia,Tarija,3903320
Sucre,Bolivia,Chuquisaca,3903987
Santiago del Torno,Bolivia,Santa Cruz,3904666
Santa Cruz de la Sierra,Bolivia,Santa Cruz,3904906
San Ignacio de Velasco,Bolivia,Santa Cruz,3905658
San Borja,Bolivia,El Beni,3905792
Riberalta,Bolivia,El Beni,3906466
Punata,Bolivia,Cochabamba,3907080
PotosÃ­,Bolivia,PotosÃ­,3907584
Oruro,Bolivia,Oruro,3909234
Montero,Bolivia,Santa Cruz,3910027
Mizque,Bolivia,Cochabamba,3910291
Llallagua,Bolivia,PotosÃ­,3911409
La Paz,Bolivia,La Paz,3911925
Huanuni,Bolivia,Oruro,3914839
GuayaramerÃ­n,Bolivia,El Beni,3915350
Cotoca,Bolivia,Santa Cruz,3918937
Cochabamba,Bolivia,Cochabamba,3919968
Cobija,Bolivia,Pando,3919998
Camiri,Bolivia,Santa Cruz,3922414
Kralendijk,"Bonaire, Saint Eustatius and Saba",Bonaire,3513563
VitÃ³ria do Mearim,Brazil,MaranhÃ£o,3384986
VitÃ³ria de Santo AntÃ£o,Brazil,Pernambuco,3384987
Viseu,Brazil,ParÃ¡,3385022
Conde,Brazil,ParaÃ­ba,3385077
Vigia,Brazil,ParÃ¡,3385088
ViÃ§osa do CearÃ¡,Brazil,CearÃ¡,3385106
ViÃ§osa,Brazil,Alagoas,3385109
Viana,Brazil,MaranhÃ£o,3385122
VÃ¡rzea Alegre,Brazil,CearÃ¡,3385467
Varjota,Brazil,CearÃ¡,3385504
Vargem Grande,Brazil,MaranhÃ£o,3385538
ValenÃ§a do PiauÃ­,Brazil,PiauÃ­,3385592
UniÃ£o dos Palmares,Brazil,Alagoas,3385742
UniÃ£o,Brazil,PiauÃ­,3385745
Tuntum,Brazil,MaranhÃ£o,3385922
TucuruÃ­,Brazil,ParÃ¡,3385935
TucumÃ£,Brazil,ParÃ¡,3385980
Trindade,Brazil,Pernambuco,3386042
Trairi,Brazil,CearÃ¡,3386177
Toritama,Brazil,Pernambuco,3386264
TomÃ© AÃ§u,Brazil,ParÃ¡,3386279
Timon,Brazil,MaranhÃ£o,3386361
Timbiras,Brazil,MaranhÃ£o,3386372
TimbaÃºba,Brazil,Pernambuco,3386396
TianguÃ¡,Brazil,CearÃ¡,3386449
Teresina,Brazil,PiauÃ­,3386496
SÃ£o JoÃ£o dos Inhamuns,Brazil,CearÃ¡,3386567
TamandarÃ©,Brazil,Pernambuco,3386931
Tabira,Brazil,Pernambuco,3387082
Surubim,Brazil,Pernambuco,3387115
Sousa,Brazil,ParaÃ­ba,3387202
Soure,Brazil,ParÃ¡,3387204
SolÃ¢nea,Brazil,ParaÃ­ba,3387266
Sobral,Brazil,CearÃ¡,3387296
SirinhaÃ©m,Brazil,Pernambuco,3387604
SertÃ¢nia,Brazil,Pernambuco,3387663
Serra Talhada,Brazil,Pernambuco,3387786
Senador Pompeu,Brazil,CearÃ¡,3387926
Satuba,Brazil,Alagoas,3387987
SÃ£o Raimundo Nonato,Brazil,PiauÃ­,3388145
SÃ£o Miguel dos Campos,Brazil,Alagoas,3388269
SÃ£o Miguel do GuamÃ¡,Brazil,ParÃ¡,3388270
SÃ£o Mateus do MaranhÃ£o,Brazil,MaranhÃ£o,3388318
SÃ£o LuÃ­s do Quitunde,Brazil,Alagoas,3388341
SÃ£o LuÃ­s,Brazil,MaranhÃ£o,3388368
SÃ£o LourenÃ§o da Mata,Brazil,Pernambuco,3388376
SÃ£o JosÃ© do Egito,Brazil,Pernambuco,3388435
SÃ£o JosÃ© de Ribamar,Brazil,MaranhÃ£o,3388441
SÃ£o JosÃ© de Mipibu,Brazil,Rio Grande do Norte,3388443
SÃ£o JoÃ£o dos Patos,Brazil,MaranhÃ£o,3388615
SÃ£o GonÃ§alo do Amarante,Brazil,CearÃ¡,3388714
SÃ£o FÃ©lix do Xingu,Brazil,ParÃ¡,3388847
SÃ£o Domingos do MaranhÃ£o,Brazil,MaranhÃ£o,3388868
SÃ£o Bento,Brazil,ParaÃ­ba,3388991
SÃ£o Bento,Brazil,MaranhÃ£o,3389006
Santa Rita,Brazil,ParaÃ­ba,3389321
SantarÃ©m,Brazil,ParÃ¡,3389353
Santa QuitÃ©ria do MaranhÃ£o,Brazil,MaranhÃ£o,3389358
Santa QuitÃ©ria,Brazil,CearÃ¡,3389361
Santana do Ipanema,Brazil,Alagoas,3389384
Santa Luzia,Brazil,MaranhÃ£o,3389557
Santa InÃªs,Brazil,MaranhÃ£o,3389609
Santa Helena,Brazil,MaranhÃ£o,3389622
Santa Cruz do Capibaribe,Brazil,Pernambuco,3389652
Santa Cruz,Brazil,Rio Grande do Norte,3389673
SalinÃ³polis,Brazil,ParÃ¡,3389822
Salgueiro,Brazil,Pernambuco,3389860
Russas,Brazil,CearÃ¡,3390160
Rio Largo,Brazil,Alagoas,3390288
Rio Formoso,Brazil,Pernambuco,3390295
RibeirÃ£o,Brazil,Pernambuco,3390326
Recife,Brazil,Pernambuco,3390760
Quixeramobim,Brazil,CearÃ¡,3390901
QuixadÃ¡,Brazil,CearÃ¡,3390907
Presidente Dutra,Brazil,MaranhÃ£o,3391220
Santana,Brazil,AmapÃ¡,3391360
Porto Calvo,Brazil,Alagoas,3391397
Portel,Brazil,ParÃ¡,3391412
Pombos,Brazil,Pernambuco,3391556
Pombal,Brazil,ParaÃ­ba,3391571
Piripiri,Brazil,PiauÃ­,3391908
Piracuruca,Brazil,PiauÃ­,3391991
Pinheiro,Brazil,MaranhÃ£o,3392054
PindarÃ© Mirim,Brazil,MaranhÃ£o,3392088
Pilar,Brazil,Alagoas,3392126
Picos,Brazil,PiauÃ­,3392167
Petrolina,Brazil,Pernambuco,3392242
JatobÃ¡,Brazil,Pernambuco,3392243
Pesqueira,Brazil,Pernambuco,3392251
Pentecoste,Brazil,CearÃ¡,3392345
Penalva,Brazil,MaranhÃ£o,3392368
Pedro II,Brazil,PiauÃ­,3392431
Pedra Branca,Brazil,CearÃ¡,3392629
Paulo Afonso,Brazil,Bahia,3392734
Paulista,Brazil,Pernambuco,3392740
Patos,Brazil,ParaÃ­ba,3392887
Parnamirim,Brazil,Rio Grande do Norte,3392998
ParnaÃ­ba,Brazil,PiauÃ­,3393001
Parintins,Brazil,Amazonas,3393008
Parelhas,Brazil,Rio Grande do Norte,3393017
Paraipaba,Brazil,CearÃ¡,3393091
Paragominas,Brazil,ParÃ¡,3393106
Paracuru,Brazil,CearÃ¡,3393115
Palmares,Brazil,Pernambuco,3393264
Pacatuba,Brazil,CearÃ¡,3393400
Pacajus,Brazil,CearÃ¡,3393409
Ouricuri,Brazil,Pernambuco,3393452
OrÃ³s,Brazil,CearÃ¡,3393465
OriximinÃ¡,Brazil,ParÃ¡,3393471
Olinda,Brazil,Pernambuco,3393536
Oeiras,Brazil,PiauÃ­,3393764
Ãbidos,Brazil,ParÃ¡,3393768
Nova Russas,Brazil,CearÃ¡,3393832
Nova Cruz,Brazil,Rio Grande do Norte,3393876
NazarÃ© da Mata,Brazil,Pernambuco,3393972
Natal,Brazil,Rio Grande do Norte,3394023
Murici,Brazil,Alagoas,3394116
Moreno,Brazil,Pernambuco,3394453
Morada Nova,Brazil,CearÃ¡,3394500
Monteiro,Brazil,ParaÃ­ba,3394549
Monte Alegre,Brazil,ParÃ¡,3394605
MombaÃ§a,Brazil,CearÃ¡,3394649
Moju,Brazil,ParÃ¡,3394661
MossorÃ³,Brazil,Rio Grande do Norte,3394682
Mocajuba,Brazil,ParÃ¡,3394745
MauÃ©s,Brazil,Amazonas,3395062
Matriz de Camaragibe,Brazil,Alagoas,3395077
Mari,Brazil,ParaÃ­ba,3395380
Marechal Deodoro,Brazil,Alagoas,3395395
Maragogi,Brazil,Alagoas,3395458
MaracanaÃº,Brazil,CearÃ¡,3395473
MarabÃ¡,Brazil,ParÃ¡,3395503
Mamanguape,Brazil,ParaÃ­ba,3395717
MaceiÃ³,Brazil,Alagoas,3395981
Macau,Brazil,Rio Grande do Norte,3395998
MacapÃ¡,Brazil,AmapÃ¡,3396016
MacaÃ­ba,Brazil,Rio Grande do Norte,3396048
Limoeiro do Norte,Brazil,CearÃ¡,3396266
Limoeiro,Brazil,Pernambuco,3396277
Lavras da Mangabeira,Brazil,CearÃ¡,3396364
Lajedo,Brazil,Pernambuco,3396496
Lago da Pedra,Brazil,MaranhÃ£o,3396601
Lagoa do Itaenga,Brazil,Pernambuco,3396769
Juazeiro do Norte,Brazil,CearÃ¡,3397147
JosÃ© de Freitas,Brazil,PiauÃ­,3397230
JoÃ£o Pessoa,Brazil,ParaÃ­ba,3397277
JoÃ£o CÃ¢mara,Brazil,Rio Grande do Norte,3397315
Jaguaruana,Brazil,CearÃ¡,3397665
Jaguaribe,Brazil,CearÃ¡,3397675
JaboatÃ£o,Brazil,Pernambuco,3397838
Itupiranga,Brazil,ParÃ¡,3397851
Itacoatiara,Brazil,Amazonas,3397893
Itaporanga,Brazil,ParaÃ­ba,3397898
Itapissuma,Brazil,Pernambuco,3397904
Itapipoca,Brazil,CearÃ¡,3397909
Itapecuru Mirim,Brazil,MaranhÃ£o,3397936
ItapagÃ©,Brazil,CearÃ¡,3397941
Itaituba,Brazil,ParÃ¡,3397967
Itaitinga,Brazil,CearÃ¡,3397969
Itabaiana,Brazil,ParaÃ­ba,3398003
Ipueiras,Brazil,CearÃ¡,3398076
Ipubi,Brazil,Pernambuco,3398105
Ipu,Brazil,CearÃ¡,3398112
Ipojuca,Brazil,Pernambuco,3398115
Imperatriz,Brazil,MaranhÃ£o,3398269
Iguatu,Brazil,CearÃ¡,3398331
IgarapÃ© Miri,Brazil,ParÃ¡,3398343
IgarapÃ© AÃ§u,Brazil,ParÃ¡,3398350
Igarassu,Brazil,Pernambuco,3398352
IcÃ³,Brazil,CearÃ¡,3398379
Horizonte,Brazil,CearÃ¡,3398450
Guaraciaba do Norte,Brazil,CearÃ¡,3398569
Guarabira,Brazil,ParaÃ­ba,3398570
GuaiÃºba,Brazil,CearÃ¡,3398614
GravatÃ¡,Brazil,Pernambuco,3398691
Granja,Brazil,CearÃ¡,3398706
GrajaÃº,Brazil,MaranhÃ£o,3398856
Goiana,Brazil,Pernambuco,3398904
GlÃ³ria do GoitÃ¡,Brazil,Pernambuco,3398920
Garanhuns,Brazil,Pernambuco,3399058
Gameleira,Brazil,Pernambuco,3399132
Fortaleza,Brazil,CearÃ¡,3399415
Floriano,Brazil,PiauÃ­,3399506
Floresta,Brazil,Pernambuco,3399518
EusÃ©bio,Brazil,CearÃ¡,3400558
Extremoz,Brazil,Rio Grande do Norte,3400567
Estreito,Brazil,MaranhÃ£o,3400617
Esperantina,Brazil,PiauÃ­,3400740
EsperanÃ§a,Brazil,ParaÃ­ba,3400752
Escada,Brazil,Pernambuco,3400804
Dom Pedro,Brazil,MaranhÃ£o,3400969
Demerval LobÃ£o,Brazil,PiauÃ­,3401106
Delmiro Gouveia,Brazil,Alagoas,3401109
CustÃ³dia,Brazil,Pernambuco,3401138
Cururupu,Brazil,MaranhÃ£o,3401148
Currais Novos,Brazil,Rio Grande do Norte,3401283
Cupira,Brazil,Pernambuco,3401340
Crato,Brazil,CearÃ¡,3401545
CrateÃºs,Brazil,CearÃ¡,3401548
CoroatÃ¡,Brazil,MaranhÃ£o,3401703
Condado,Brazil,Pernambuco,3401830
ConceiÃ§Ã£o do Araguaia,Brazil,ParÃ¡,3401845
Colinas,Brazil,MaranhÃ£o,3401963
Coelho Neto,Brazil,MaranhÃ£o,3401992
CodÃ³,Brazil,MaranhÃ£o,3402000
Chapadinha,Brazil,MaranhÃ£o,3402229
ChÃ£ Grande,Brazil,Pernambuco,3402271
CearÃ¡ Mirim,Brazil,Rio Grande do Norte,3402360
Caxias,Brazil,MaranhÃ£o,3402383
Caucaia,Brazil,CearÃ¡,3402429
CatolÃ© do Rocha,Brazil,ParaÃ­ba,3402465
Catende,Brazil,Pernambuco,3402528
Castanhal,Brazil,ParÃ¡,3402591
Cascavel,Brazil,CearÃ¡,3402613
Caruaru,Brazil,Pernambuco,3402655
Carpina,Brazil,Pernambuco,3402721
Carolina,Brazil,MaranhÃ£o,3402724
CapitÃ£o PoÃ§o,Brazil,ParÃ¡,3403127
Capanema,Brazil,ParÃ¡,3403208
CanindÃ©,Brazil,CearÃ¡,3403353
Canguaretama,Brazil,Rio Grande do Norte,3403362
Campos Sales,Brazil,CearÃ¡,3403534
Campo Maior,Brazil,PiauÃ­,3403566
Campo Alegre,Brazil,Alagoas,3403611
Campina Grande,Brazil,ParaÃ­ba,3403642
Camocim,Brazil,CearÃ¡,3403687
CametÃ¡,Brazil,ParÃ¡,3403697
Cajueiro,Brazil,Alagoas,3403941
Cajazeiras,Brazil,ParaÃ­ba,3404020
CaicÃ³,Brazil,Rio Grande do Norte,3404117
CabrobÃ³,Brazil,Pernambuco,3404513
Cabo,Brazil,Pernambuco,3404545
Cabedelo,Brazil,ParaÃ­ba,3404558
Buriti Bravo,Brazil,MaranhÃ£o,3404722
BuÃ­que,Brazil,Pernambuco,3404766
Breves,Brazil,ParÃ¡,3404817
Brejo Santo,Brazil,CearÃ¡,3404833
Brejo da Madre de Deus,Brazil,Pernambuco,3404862
BraganÃ§a,Brazil,ParÃ¡,3405006
Bom Conselho,Brazil,Pernambuco,3405380
Boa Viagem,Brazil,CearÃ¡,3405616
Bezerros,Brazil,Pernambuco,3405738
Benevides,Brazil,ParÃ¡,3405792
Belo Jardim,Brazil,Pernambuco,3405812
BelÃ©m,Brazil,ParaÃ­ba,3405863
BelÃ©m,Brazil,ParÃ¡,3405870
Beberibe,Brazil,CearÃ¡,3405924
Bayeux,Brazil,ParaÃ­ba,3405940
BaturitÃ©,Brazil,CearÃ¡,3405954
Barreiros,Brazil,Pernambuco,3406160
Barreirinhas,Brazil,MaranhÃ£o,3406196
Barras,Brazil,PiauÃ­,3406263
Barra do Corda,Brazil,MaranhÃ£o,3406318
Barcarena,Brazil,ParÃ¡,3406429
Barbalha,Brazil,CearÃ¡,3406442
Balsas,Brazil,MaranhÃ£o,3406545
Bacabal,Brazil,MaranhÃ£o,3406910
Augusto CorrÃªa,Brazil,ParÃ¡,3406961
Atalaia,Brazil,Alagoas,3406996
Areia Branca,Brazil,Rio Grande do Norte,3407194
Arcoverde,Brazil,Pernambuco,3407216
Araripina,Brazil,Pernambuco,3407243
Arari,Brazil,MaranhÃ£o,3407258
Arapiraca,Brazil,Alagoas,3407327
AraguaÃ­na,Brazil,Tocantins,3407357
Aracati,Brazil,CearÃ¡,3407378
Aquiraz,Brazil,CearÃ¡,3407407
Apodi,Brazil,Rio Grande do Norte,3407440
Ananindeua,Brazil,ParÃ¡,3407669
Amaraji,Brazil,Pernambuco,3407758
Altos,Brazil,PiauÃ­,3407797
Altamira,Brazil,ParÃ¡,3407882
Almeirim,Brazil,ParÃ¡,3407903
Alenquer,Brazil,ParÃ¡,3407980
Alagoa Grande,Brazil,ParaÃ­ba,3408100
Ãguas Belas,Brazil,Pernambuco,3408166
Ãgua Preta,Brazil,Pernambuco,3408175
Afogados da Ingazeira,Brazil,Pernambuco,3408274
AÃ§u,Brazil,Rio Grande do Norte,3408337
Acopiara,Brazil,CearÃ¡,3408343
AcaraÃº,Brazil,CearÃ¡,3408368
Abreu e Lima,Brazil,Pernambuco,3408404
Abaetetuba,Brazil,ParÃ¡,3408424
Xique Xique,Brazil,Bahia,3444823
XanxerÃª,Brazil,Santa Catarina,3444848
Votuporanga,Brazil,SÃ£o Paulo,3444864
Votorantim,Brazil,SÃ£o Paulo,3444866
Volta Redonda,Brazil,Rio de Janeiro,3444876
VitÃ³ria da Conquista,Brazil,Bahia,3444914
VitÃ³ria,Brazil,EspÃ­rito Santo,3444924
Visconde do Rio Branco,Brazil,Minas Gerais,3444969
Viradouro,Brazil,SÃ£o Paulo,3444997
Vinhedo,Brazil,SÃ£o Paulo,3445014
Vila Velha,Brazil,EspÃ­rito Santo,3445026
Videira,Brazil,Santa Catarina,3445126
ViÃ§osa,Brazil,Minas Gerais,3445133
Viana,Brazil,EspÃ­rito Santo,3445153
ViamÃ£o,Brazil,Rio Grande do Sul,3445156
Vespasiano,Brazil,Minas Gerais,3445162
VeranÃ³polis,Brazil,Rio Grande do Sul,3445299
Vera Cruz,Brazil,Bahia,3445307
Wenceslau Braz,Brazil,ParanÃ¡,3445348
VenÃ¢ncio Aires,Brazil,Rio Grande do Sul,3445350
Vazante,Brazil,Minas Gerais,3445418
Vassouras,Brazil,Rio de Janeiro,3445433
VÃ¡rzea Paulista,Brazil,SÃ£o Paulo,3445446
VÃ¡rzea Grande,Brazil,Mato Grosso,3445451
VÃ¡rzea da Palma,Brazil,Minas Gerais,3445459
Varginha,Brazil,Minas Gerais,3445487
Vargem Grande do Sul,Brazil,SÃ£o Paulo,3445500
ValparaÃ­so,Brazil,SÃ£o Paulo,3445575
Valinhos,Brazil,SÃ£o Paulo,3445578
ValenÃ§a,Brazil,Rio de Janeiro,3445596
ValenÃ§a,Brazil,Bahia,3445597
Vacaria,Brazil,Rio Grande do Sul,3445630
Uruguaiana,Brazil,Rio Grande do Sul,3445679
UruÃ§uca,Brazil,Bahia,3445690
UruaÃ§u,Brazil,GoiÃ¡s,3445713
UniÃ£o da VitÃ³ria,Brazil,ParanÃ¡,3445746
UnaÃ­,Brazil,Minas Gerais,3445764
Una,Brazil,Bahia,3445781
Umuarama,Brazil,ParanÃ¡,3445782
UberlÃ¢ndia,Brazil,Minas Gerais,3445831
Uberaba,Brazil,Minas Gerais,3445839
Ubatuba,Brazil,SÃ£o Paulo,3445847
UbatÃ£,Brazil,Bahia,3445849
Ubaitaba,Brazil,Bahia,3445853
UbÃ¡,Brazil,Minas Gerais,3445859
TupanciretÃ£,Brazil,Rio Grande do Sul,3445939
Tupaciguara,Brazil,Minas Gerais,3445941
TupÃ£,Brazil,SÃ£o Paulo,3445942
Tucano,Brazil,Bahia,3445983
TubarÃ£o,Brazil,Santa Catarina,3445993
Trindade,Brazil,GoiÃ¡s,3446038
TrÃªs Rios,Brazil,Rio de Janeiro,3446065
TrÃªs Pontas,Brazil,Minas Gerais,3446077
TrÃªs Passos,Brazil,Rio Grande do Sul,3446087
TrÃªs Lagoas,Brazil,Mato Grosso do Sul,3446098
TrÃªs de Maio,Brazil,Rio Grande do Sul,3446130
TrÃªs Coroas,Brazil,Rio Grande do Sul,3446137
TrÃªs CoraÃ§Ãµes,Brazil,Minas Gerais,3446138
TremembÃ©,Brazil,SÃ£o Paulo,3446194
TramandaÃ­,Brazil,Rio Grande do Sul,3446232
Torres,Brazil,Rio Grande do Sul,3446295
Toledo,Brazil,ParanÃ¡,3446370
Tobias Barreto,Brazil,Sergipe,3446400
TimÃ³teo,Brazil,Minas Gerais,3446445
TimbÃ³,Brazil,Santa Catarina,3446465
Tijucas,Brazil,Santa Catarina,3446500
TietÃª,Brazil,SÃ£o Paulo,3446539
TeutÃ´nia,Brazil,Rio Grande do Sul,3446556
TeresÃ³polis,Brazil,Rio de Janeiro,3446606
TeÃ³filo Otoni,Brazil,Minas Gerais,3446621
Teodoro Sampaio,Brazil,SÃ£o Paulo,3446625
TelÃªmaco Borba,Brazil,ParanÃ¡,3446652
TaubatÃ©,Brazil,SÃ£o Paulo,3446682
TatuÃ­,Brazil,SÃ£o Paulo,3446692
Taquarituba,Brazil,SÃ£o Paulo,3446752
Taquaritinga,Brazil,SÃ£o Paulo,3446753
Taquari,Brazil,Rio Grande do Sul,3446783
Taquara,Brazil,Rio Grande do Sul,3446847
TapiramutÃ¡,Brazil,Bahia,3446866
Tapes,Brazil,Rio Grande do Sul,3446880
TanguÃ¡,Brazil,Rio de Janeiro,3446974
Tanabi,Brazil,SÃ£o Paulo,3446979
TambaÃº,Brazil,SÃ£o Paulo,3447005
Taiobeiras,Brazil,Minas Gerais,3447059
TaboÃ£o da Serra,Brazil,SÃ£o Paulo,3447186
Suzano,Brazil,SÃ£o Paulo,3447212
SumarÃ©,Brazil,SÃ£o Paulo,3447259
Sorocaba,Brazil,SÃ£o Paulo,3447399
Soledade,Brazil,Rio Grande do Sul,3447423
Socorro,Brazil,SÃ£o Paulo,3447437
Sobradinho,Brazil,Bahia,3447473
SimÃ£o Dias,Brazil,Sergipe,3447562
Silva Jardim,Brazil,Rio de Janeiro,3447591
SidrolÃ¢ndia,Brazil,Mato Grosso do Sul,3447597
Sete Lagoas,Brazil,Minas Gerais,3447624
SertÃ£ozinho,Brazil,SÃ£o Paulo,3447651
Serrinha,Brazil,Bahia,3447690
Serra Negra,Brazil,SÃ£o Paulo,3447718
Serrana,Brazil,SÃ£o Paulo,3447720
Serra,Brazil,EspÃ­rito Santo,3447779
SeropÃ©dica,Brazil,Rio de Janeiro,3447785
Senhor do Bonfim,Brazil,Bahia,3447839
Senador Canedo,Brazil,GoiÃ¡s,3447854
Seabra,Brazil,Bahia,3447928
Schroeder,Brazil,Santa Catarina,3447929
Saubara,Brazil,Bahia,3447961
Sarzedo,Brazil,Minas Gerais,3447969
Sarandi,Brazil,Rio Grande do Sul,3447997
Sarandi,Brazil,ParanÃ¡,3447998
Saquarema,Brazil,Rio de Janeiro,3448011
Sapucaia,Brazil,Rio Grande do Sul,3448031
Sapiranga,Brazil,Rio Grande do Sul,3448063
SÃ£o Vicente,Brazil,SÃ£o Paulo,3448136
SÃ£o SepÃ©,Brazil,Rio Grande do Sul,3448207
SÃ£o SebastiÃ£o do PassÃ©,Brazil,Bahia,3448219
SÃ£o SebastiÃ£o do ParaÃ­so,Brazil,Minas Gerais,3448221
SÃ£o SebastiÃ£o do CaÃ­,Brazil,Rio Grande do Sul,3448227
SÃ£o SebastiÃ£o,Brazil,SÃ£o Paulo,3448257
SÃ£o Roque,Brazil,SÃ£o Paulo,3448300
SÃ£o Pedro da Aldeia,Brazil,Rio de Janeiro,3448351
SÃ£o Pedro,Brazil,SÃ£o Paulo,3448403
SÃ£o Paulo,Brazil,SÃ£o Paulo,3448439
SÃ£o Miguel do IguaÃ§u,Brazil,ParanÃ¡,3448453
SÃ£o Miguel do Araguaia,Brazil,GoiÃ¡s,3448455
SÃ£o Mateus do Sul,Brazil,ParanÃ¡,3448502
SÃ£o Mateus,Brazil,EspÃ­rito Santo,3448519
SÃ£o Marcos,Brazil,Rio Grande do Sul,3448533
SÃ£o Manuel,Brazil,SÃ£o Paulo,3448545
SÃ£o Luiz Gonzaga,Brazil,Rio Grande do Sul,3448552
SÃ£o LuÃ­s de Montes Belos,Brazil,GoiÃ¡s,3448558
SÃ£o LourenÃ§o do Sul,Brazil,Rio Grande do Sul,3448596
SÃ£o LourenÃ§o,Brazil,Minas Gerais,3448616
SÃ£o Leopoldo,Brazil,Rio Grande do Sul,3448622
SÃ£o JosÃ© dos Pinhais,Brazil,ParanÃ¡,3448632
SÃ£o JosÃ© dos Campos,Brazil,SÃ£o Paulo,3448636
SÃ£o JosÃ© do Rio Preto,Brazil,SÃ£o Paulo,3448639
SÃ£o JosÃ© do Rio Pardo,Brazil,SÃ£o Paulo,3448640
SÃ£o JosÃ©,Brazil,Santa Catarina,3448742
SÃ£o Joaquim da Barra,Brazil,SÃ£o Paulo,3448825
SÃ£o Joaquim,Brazil,Santa Catarina,3448828
SÃ£o JoÃ£o Nepomuceno,Brazil,Minas Gerais,3448846
SÃ£o JoÃ£o de Meriti,Brazil,Rio de Janeiro,3448877
SÃ£o JoÃ£o del Rei,Brazil,Minas Gerais,3448879
SÃ£o JoÃ£o da Boa Vista,Brazil,SÃ£o Paulo,3448902
SÃ£o JoÃ£o da Barra,Brazil,Rio de Janeiro,3448903
SÃ£o JerÃ´nimo,Brazil,Rio Grande do Sul,3449045
SÃ£o Gotardo,Brazil,Minas Gerais,3449053
SÃ£o GonÃ§alo do SapucaÃ­,Brazil,Minas Gerais,3449056
SÃ£o Gabriel,Brazil,Rio Grande do Sul,3449099
SÃ£o Francisco do Sul,Brazil,Santa Catarina,3449112
SÃ£o Francisco do Conde,Brazil,Bahia,3449116
SÃ£o Francisco,Brazil,Minas Gerais,3449176
SÃ£o FidÃ©lis,Brazil,Rio de Janeiro,3449195
SÃ£o CristÃ³vÃ£o,Brazil,Sergipe,3449310
SÃ£o Carlos,Brazil,SÃ£o Paulo,3449319
SÃ£o Caetano do Sul,Brazil,SÃ£o Paulo,3449324
SÃ£o Borja,Brazil,Rio Grande do Sul,3449340
SÃ£o Bernardo do Campo,Brazil,SÃ£o Paulo,3449344
SÃ£o Bento do Sul,Brazil,Santa Catarina,3449350
Santos Dumont,Brazil,Minas Gerais,3449427
Santos,Brazil,SÃ£o Paulo,3449433
Santo EstÃªvÃ£o,Brazil,Bahia,3449467
Santo AntÃ´nio do Monte,Brazil,Minas Gerais,3449500
Santo AntÃ´nio do Amparo,Brazil,Minas Gerais,3449516
Santo AntÃ´nio de Posse,Brazil,SÃ£o Paulo,3449518
Santo AntÃ´nio de PÃ¡dua,Brazil,Rio de Janeiro,3449519
Santo AntÃ´nio de Jesus,Brazil,Bahia,3449521
Santo AntÃ´nio da Platina,Brazil,ParanÃ¡,3449529
Santo Ã‚ngelo,Brazil,Rio Grande do Sul,3449696
Santo AndrÃ©,Brazil,SÃ£o Paulo,3449701
Santo AnastÃ¡cio,Brazil,SÃ£o Paulo,3449707
Santo Amaro da Imperatriz,Brazil,Santa Catarina,3449711
Santo Amaro,Brazil,Bahia,3449720
Santiago,Brazil,Rio Grande do Sul,3449741
Santa VitÃ³ria do Palmar,Brazil,Rio Grande do Sul,3449747
Santa Rosa de Viterbo,Brazil,SÃ£o Paulo,3449793
Santa Rosa,Brazil,Rio Grande do Sul,3449822
Santa Rita do SapucaÃ­,Brazil,Minas Gerais,3449847
Santa Rita do Passa Quatro,Brazil,SÃ£o Paulo,3449851
Santana do ParaÃ­so,Brazil,Minas Gerais,3449933
Santana do Livramento,Brazil,Rio Grande do Sul,3449936
Santana de ParnaÃ­ba,Brazil,SÃ£o Paulo,3449948
Santa Maria da VitÃ³ria,Brazil,Bahia,3450063
Santa Maria,Brazil,Rio Grande do Sul,3450083
Santa Luzia,Brazil,Minas Gerais,3450144
Santaluz,Brazil,Bahia,3450157
Santa Isabel,Brazil,SÃ£o Paulo,3450188
Santa Helena de GoiÃ¡s,Brazil,GoiÃ¡s,3450206
Santa Gertrudes,Brazil,SÃ£o Paulo,3450225
Santa FÃ© do Sul,Brazil,SÃ£o Paulo,3450232
Santa Cruz do Sul,Brazil,Rio Grande do Sul,3450269
Santa Cruz do Rio Pardo,Brazil,SÃ£o Paulo,3450272
Santa Cruz das Palmeiras,Brazil,SÃ£o Paulo,3450283
Santa Cruz CabrÃ¡lia,Brazil,Bahia,3450288
Santa CecÃ­lia,Brazil,Santa Catarina,3450376
Santa BÃ¡rbara d'Oeste,Brazil,SÃ£o Paulo,3450404
Salvador,Brazil,Bahia,3450554
Salto de Pirapora,Brazil,SÃ£o Paulo,3450563
Salto,Brazil,SÃ£o Paulo,3450594
Salinas,Brazil,Minas Gerais,3450671
Sacramento,Brazil,Minas Gerais,3450759
Ruy Barbosa,Brazil,Bahia,3450832
Rubiataba,Brazil,GoiÃ¡s,3450843
RosÃ¡rio do Sul,Brazil,Rio Grande do Sul,3450873
RondonÃ³polis,Brazil,Mato Grosso,3450909
Rolante,Brazil,Rio Grande do Sul,3450963
RolÃ¢ndia,Brazil,ParanÃ¡,3450964
Rio Verde de Mato Grosso,Brazil,Mato Grosso do Sul,3451051
Rio Real,Brazil,Bahia,3451071
Rio Pardo,Brazil,Rio Grande do Sul,3451102
Rio Negro,Brazil,ParanÃ¡,3451121
Rio Negrinho,Brazil,Santa Catarina,3451124
Rio Grande da Serra,Brazil,SÃ£o Paulo,3451134
Rio Grande,Brazil,Rio Grande do Sul,3451138
Rio do Sul,Brazil,Santa Catarina,3451152
Rio de Janeiro,Brazil,Rio de Janeiro,3451190
Rio das Pedras,Brazil,SÃ£o Paulo,3451202
Rio das Ostras,Brazil,Rio de Janeiro,3451205
Rio Claro,Brazil,SÃ£o Paulo,3451234
Rio Brilhante,Brazil,Mato Grosso do Sul,3451241
Rio Branco do Sul,Brazil,ParanÃ¡,3451242
Rio Bonito,Brazil,Rio de Janeiro,3451261
RibeirÃ£o Preto,Brazil,SÃ£o Paulo,3451328
RibeirÃ£o Pires,Brazil,SÃ£o Paulo,3451329
RibeirÃ£o das Neves,Brazil,Minas Gerais,3451353
RibeirÃ£o da Ilha,Brazil,Santa Catarina,3451357
Ribeira do Pombal,Brazil,Bahia,3451383
RiachÃ£o do JacuÃ­pe,Brazil,Bahia,3451474
Resplendor,Brazil,Minas Gerais,3451650
Resende,Brazil,Rio de Janeiro,3451668
Registro,Brazil,SÃ£o Paulo,3451704
Regente FeijÃ³,Brazil,SÃ£o Paulo,3451709
Rancharia,Brazil,SÃ£o Paulo,3451856
QuirinÃ³polis,Brazil,GoiÃ¡s,3451931
Queimados,Brazil,Rio de Janeiro,3452073
Quatro Barras,Brazil,ParanÃ¡,3452141
QuaraÃ­,Brazil,Rio Grande do Sul,3452179
PrudentÃ³polis,Brazil,ParanÃ¡,3452216
PropriÃ¡,Brazil,Sergipe,3452233
PromissÃ£o,Brazil,SÃ£o Paulo,3452237
Presidente Venceslau,Brazil,SÃ£o Paulo,3452320
Presidente Prudente,Brazil,SÃ£o Paulo,3452324
Presidente EpitÃ¡cio,Brazil,SÃ£o Paulo,3452331
Prata,Brazil,Minas Gerais,3452440
Praia Grande,Brazil,SÃ£o Paulo,3452465
Prado,Brazil,Bahia,3452483
Pouso Alegre,Brazil,Minas Gerais,3452525
Posse,Brazil,GoiÃ¡s,3452599
Porto UniÃ£o,Brazil,Santa Catarina,3452623
Porto Seguro,Brazil,Bahia,3452640
Porto Ferreira,Brazil,SÃ£o Paulo,3452775
Porto Feliz,Brazil,SÃ£o Paulo,3452779
Porto Alegre,Brazil,Rio Grande do Sul,3452925
PortÃ£o,Brazil,Rio Grande do Sul,3452982
Porangatu,Brazil,GoiÃ¡s,3453014
Pontes e Lacerda,Brazil,Mato Grosso,3453060
Ponte Nova,Brazil,Minas Gerais,3453078
Ponta PorÃ£,Brazil,Mato Grosso do Sul,3453150
Pontal,Brazil,SÃ£o Paulo,3453171
Ponta Grossa,Brazil,ParanÃ¡,3453186
PompÃ©u,Brazil,Minas Gerais,3453240
PompÃ©ia,Brazil,SÃ£o Paulo,3453242
Pomerode,Brazil,Santa Catarina,3453245
PoÃ§os de Caldas,Brazil,Minas Gerais,3453303
PoconÃ©,Brazil,Mato Grosso,3453315
PoÃ§Ãµes,Brazil,Bahia,3453337
PoÃ¡,Brazil,SÃ£o Paulo,3453406
Planaltina,Brazil,GoiÃ¡s,3453420
PiÃºma,Brazil,EspÃ­rito Santo,3453435
PiuÃ­,Brazil,Minas Gerais,3453439
Pitangui,Brazil,Minas Gerais,3453457
Pitangueiras,Brazil,SÃ£o Paulo,3453467
Pitanga,Brazil,ParanÃ¡,3453478
Piritiba,Brazil,Bahia,3453494
Pires do Rio,Brazil,GoiÃ¡s,3453503
Piraquara,Brazil,ParanÃ¡,3453535
Pirapozinho,Brazil,SÃ£o Paulo,3453542
Pirapora,Brazil,Minas Gerais,3453546
PirajuÃ­,Brazil,SÃ£o Paulo,3453605
Piraju,Brazil,SÃ£o Paulo,3453610
PiraÃ­ do Sul,Brazil,ParanÃ¡,3453622
PiraÃ­,Brazil,Rio de Janeiro,3453635
Pirassununga,Brazil,SÃ£o Paulo,3453639
Piracicaba,Brazil,SÃ£o Paulo,3453643
Piracanjuba,Brazil,GoiÃ¡s,3453659
Piracaia,Brazil,SÃ£o Paulo,3453661
Pinheiral,Brazil,Rio de Janeiro,3453767
PinhÃ£o,Brazil,ParanÃ¡,3453777
EspÃ­rito Santo do Pinhal,Brazil,SÃ£o Paulo,3453807
PindobaÃ§u,Brazil,Bahia,3453827
Pindamonhangaba,Brazil,SÃ£o Paulo,3453837
Pilar do Sul,Brazil,SÃ£o Paulo,3453896
Piedade,Brazil,SÃ£o Paulo,3453926
PetrÃ³polis,Brazil,Rio de Janeiro,3454031
PeruÃ­be,Brazil,SÃ£o Paulo,3454061
Pereira Barreto,Brazil,SÃ£o Paulo,3454131
PerdÃµes,Brazil,Minas Gerais,3454139
Penha,Brazil,Santa Catarina,3454213
Penedo,Brazil,Alagoas,3454231
PenÃ¡polis,Brazil,SÃ£o Paulo,3454235
Pelotas,Brazil,Rio Grande do Sul,3454244
Pedro Leopoldo,Brazil,Minas Gerais,3454358
Pedreira,Brazil,SÃ£o Paulo,3454407
Pedra Azul,Brazil,Minas Gerais,3454578
Pederneiras,Brazil,SÃ£o Paulo,3454620
PaulÃ­nia,Brazil,SÃ£o Paulo,3454690
PatrocÃ­nio,Brazil,Minas Gerais,3454763
Patos de Minas,Brazil,Minas Gerais,3454783
Pato Branco,Brazil,ParanÃ¡,3454818
Paty do Alferes,Brazil,Rio de Janeiro,3454827
Passos,Brazil,Minas Gerais,3454847
Passo Fundo,Brazil,Rio Grande do Sul,3454857
ParobÃ©,Brazil,Rio Grande do Sul,3454954
Paraty,Brazil,Rio de Janeiro,3455036
ParanavaÃ­,Brazil,ParanÃ¡,3455051
Paranapanema,Brazil,SÃ£o Paulo,3455061
ParanaÃ­ba,Brazil,Mato Grosso do Sul,3455065
ParanaguÃ¡,Brazil,ParanÃ¡,3455070
ParaÃ­ba do Sul,Brazil,Rio de Janeiro,3455141
ParaguaÃ§u Paulista,Brazil,SÃ£o Paulo,3455152
ParaguaÃ§u,Brazil,Minas Gerais,3455155
ParÃ¡ de Minas,Brazil,Minas Gerais,3455161
Paracatu,Brazil,Minas Gerais,3455168
Paracambi,Brazil,Rio de Janeiro,3455170
Panambi,Brazil,Rio Grande do Sul,3455281
Palotina,Brazil,ParanÃ¡,3455298
Palmital,Brazil,SÃ£o Paulo,3455342
Palmeira das MissÃµes,Brazil,Rio Grande do Sul,3455416
Palmeira,Brazil,ParanÃ¡,3455425
Palmas,Brazil,ParanÃ¡,3455459
PalhoÃ§a,Brazil,Santa Catarina,3455478
PaiÃ§andu,Brazil,ParanÃ¡,3455553
Padre Bernardo,Brazil,GoiÃ¡s,3455580
Ouro Preto,Brazil,Minas Gerais,3455671
Ouro Branco,Brazil,Minas Gerais,3455689
Ourinhos,Brazil,SÃ£o Paulo,3455729
Osvaldo Cruz,Brazil,SÃ£o Paulo,3455756
OsÃ³rio,Brazil,Rio Grande do Sul,3455769
Osasco,Brazil,SÃ£o Paulo,3455775
Orleans,Brazil,Santa Catarina,3455784
OrlÃ¢ndia,Brazil,SÃ£o Paulo,3455785
Oliveira,Brazil,Minas Gerais,3455908
OlÃ­mpia,Brazil,SÃ£o Paulo,3455923
Novo Horizonte,Brazil,SÃ£o Paulo,3456060
Novo Hamburgo,Brazil,Rio Grande do Sul,3456068
Nova ViÃ§osa,Brazil,Bahia,3456102
Nova VenÃ©cia,Brazil,EspÃ­rito Santo,3456110
Nova Prata,Brazil,Rio Grande do Sul,3456125
Nova PetrÃ³polis,Brazil,Rio Grande do Sul,3456127
Nova OlÃ­mpia,Brazil,Mato Grosso,3456137
Nova Odessa,Brazil,SÃ£o Paulo,3456138
Nova Lima,Brazil,Minas Gerais,3456147
Nova IguaÃ§u,Brazil,Rio de Janeiro,3456160
Nova Granada,Brazil,SÃ£o Paulo,3456164
Nova Friburgo,Brazil,Rio de Janeiro,3456166
Nova Era,Brazil,Minas Gerais,3456176
Nossa Senhora do Socorro,Brazil,Sergipe,3456223
Nossa Senhora da GlÃ³ria,Brazil,Sergipe,3456240
NiterÃ³i,Brazil,Rio de Janeiro,3456283
NiquelÃ¢ndia,Brazil,GoiÃ¡s,3456285
NilÃ³polis,Brazil,Rio de Janeiro,3456290
NerÃ³polis,Brazil,GoiÃ¡s,3456322
Nepomuceno,Brazil,Minas Gerais,3456324
NazarÃ©,Brazil,Bahia,3456366
NaviraÃ­,Brazil,Mato Grosso do Sul,3456368
Navegantes,Brazil,Santa Catarina,3456370
Nanuque,Brazil,Minas Gerais,3456398
Muzambinho,Brazil,Minas Gerais,3456412
Muritiba,Brazil,Bahia,3456483
MuriaÃ©,Brazil,Minas Gerais,3456500
Mucuri,Brazil,Bahia,3456593
Morro do ChapÃ©u,Brazil,Bahia,3456696
Morro Agudo,Brazil,SÃ£o Paulo,3456724
Morrinhos,Brazil,GoiÃ¡s,3456735
Montes Claros,Brazil,Minas Gerais,3456814
Monte Santo de Minas,Brazil,Minas Gerais,3456816
Montenegro,Brazil,Rio Grande do Sul,3456826
Monte Mor,Brazil,SÃ£o Paulo,3456827
Monte Carmelo,Brazil,Minas Gerais,3456848
Monte Azul Paulista,Brazil,SÃ£o Paulo,3456863
Monte AprazÃ­vel,Brazil,SÃ£o Paulo,3456866
Monte Alto,Brazil,SÃ£o Paulo,3456873
MongaguÃ¡,Brazil,SÃ£o Paulo,3456944
Mogi Mirim,Brazil,SÃ£o Paulo,3456998
Mogi-Gaucu,Brazil,SÃ£o Paulo,3457000
Mogi das Cruzes,Brazil,SÃ£o Paulo,3457001
Mococa,Brazil,SÃ£o Paulo,3457025
MirandopÃ³lis,Brazil,SÃ£o Paulo,3457107
Miracema,Brazil,Rio de Janeiro,3457133
Mineiros,Brazil,GoiÃ¡s,3457147
Miguel Pereira,Brazil,Rio de Janeiro,3457191
MiguelÃ³polis,Brazil,SÃ£o Paulo,3457192
Mendes,Brazil,Rio de Janeiro,3457247
Medianeira,Brazil,ParanÃ¡,3457359
Medeiros Neto,Brazil,Bahia,3457360
MauÃ¡,Brazil,SÃ£o Paulo,3457381
Matozinhos,Brazil,Minas Gerais,3457393
Mateus Leme,Brazil,Minas Gerais,3457484
MatÃ£o,Brazil,SÃ£o Paulo,3457509
Mata de SÃ£o JoÃ£o,Brazil,Bahia,3457528
Mascote,Brazil,Bahia,3457566
MartinÃ³polis,Brazil,SÃ£o Paulo,3457595
MaringÃ¡,Brazil,ParanÃ¡,3457671
MarÃ­lia,Brazil,SÃ£o Paulo,3457692
MaricÃ¡,Brazil,Rio de Janeiro,3457708
Mariana,Brazil,Minas Gerais,3457736
Marialva,Brazil,ParanÃ¡,3457741
Marechal CÃ¢ndido Rondon,Brazil,ParanÃ¡,3457772
Marau,Brazil,Rio Grande do Sul,3457817
Marataizes,Brazil,EspÃ­rito Santo,3457819
Maragogipe,Brazil,Bahia,3457850
MaracÃ¡s,Brazil,Bahia,3457854
Maracaju,Brazil,Mato Grosso do Sul,3457859
Manhumirim,Brazil,Minas Gerais,3457950
ManhuaÃ§u,Brazil,Minas Gerais,3457952
Mangaratiba,Brazil,Rio de Janeiro,3457991
Mandaguari,Brazil,ParanÃ¡,3458049
MairiporÃ£,Brazil,SÃ£o Paulo,3458131
Mairinque,Brazil,SÃ£o Paulo,3458132
Mafra,Brazil,Santa Catarina,3458147
Machado,Brazil,Minas Gerais,3458211
Macatuba,Brazil,SÃ£o Paulo,3458245
MacaÃ©,Brazil,Rio de Janeiro,3458266
LuziÃ¢nia,Brazil,GoiÃ¡s,3458329
Lucas,Brazil,Mato Grosso,3458397
Louveira,Brazil,SÃ£o Paulo,3458406
Lorena,Brazil,SÃ£o Paulo,3458425
Londrina,Brazil,ParanÃ¡,3458449
Loanda,Brazil,ParanÃ¡,3458479
Livramento do Brumado,Brazil,Bahia,3458481
Lins,Brazil,SÃ£o Paulo,3458494
Linhares,Brazil,EspÃ­rito Santo,3458498
Limeira,Brazil,SÃ£o Paulo,3458575
Leopoldina,Brazil,Minas Gerais,3458632
LenÃ§Ã³is Paulista,Brazil,SÃ£o Paulo,3458645
Leme,Brazil,SÃ£o Paulo,3458662
Lavras,Brazil,Minas Gerais,3458696
Laranjeiras do Sul,Brazil,ParanÃ¡,3458746
Laranjeiras,Brazil,Sergipe,3458778
Laranjal Paulista,Brazil,SÃ£o Paulo,3458786
Lapa,Brazil,ParanÃ¡,3458826
Lajinha,Brazil,Minas Gerais,3458902
Lages,Brazil,Santa Catarina,3458930
Lajeado,Brazil,Rio Grande do Sul,3459035
Laguna,Brazil,Santa Catarina,3459094
Lagoa Vermelha,Brazil,Rio Grande do Sul,3459126
Lagoa Santa,Brazil,Minas Gerais,3459138
Lagoa da Prata,Brazil,Minas Gerais,3459251
Lagarto,Brazil,Sergipe,3459342
LadÃ¡rio,Brazil,Mato Grosso do Sul,3459352
JundiaÃ­,Brazil,SÃ£o Paulo,3459462
JÃºlio de Castilhos,Brazil,Rio Grande do Sul,3459495
Juiz de Fora,Brazil,Minas Gerais,3459505
Juatuba,Brazil,Minas Gerais,3459550
JosÃ© BonifÃ¡cio,Brazil,SÃ£o Paulo,3459667
Joinville,Brazil,Santa Catarina,3459712
JoÃ£o Pinheiro,Brazil,Minas Gerais,3459785
JoÃ£o Monlevade,Brazil,Minas Gerais,3459796
JoaÃ§aba,Brazil,Santa Catarina,3459869
Jeremoabo,Brazil,Bahia,3459922
Jequitinhonha,Brazil,Minas Gerais,3459925
JequiÃ©,Brazil,Bahia,3459943
JaÃº,Brazil,SÃ£o Paulo,3460005
JataÃ­,Brazil,GoiÃ¡s,3460064
Jarinu,Brazil,SÃ£o Paulo,3460068
JardinÃ³polis,Brazil,SÃ£o Paulo,3460071
Jardim,Brazil,Mato Grosso do Sul,3460087
JaraguÃ¡ do Sul,Brazil,Santa Catarina,3460102
JaraguÃ¡,Brazil,GoiÃ¡s,3460107
Japeri,Brazil,Rio de Janeiro,3460132
JanuÃ¡ria,Brazil,Minas Gerais,3460148
Jandira,Brazil,SÃ£o Paulo,3460170
Jandaia do Sul,Brazil,ParanÃ¡,3460172
JanaÃºba,Brazil,Minas Gerais,3460174
Jales,Brazil,SÃ£o Paulo,3460186
JaguariÃºna,Brazil,SÃ£o Paulo,3460200
JaguariaÃ­va,Brazil,ParanÃ¡,3460214
Jaguarari,Brazil,Bahia,3460225
JaguarÃ£o,Brazil,Rio Grande do Sul,3460232
Jaguaquara,Brazil,Bahia,3460242
Jacutinga,Brazil,Minas Gerais,3460267
Jacobina,Brazil,Bahia,3460344
Jaciara,Brazil,Mato Grosso,3460355
Jacarezinho,Brazil,ParanÃ¡,3460362
JacareÃ­,Brazil,SÃ£o Paulo,3460370
Jaboticabal,Brazil,SÃ£o Paulo,3460441
Ivoti,Brazil,Rio Grande do Sul,3460484
Ituverava,Brazil,SÃ£o Paulo,3460511
Iturama,Brazil,Minas Gerais,3460513
Itupeva,Brazil,SÃ£o Paulo,3460516
Itumbiara,Brazil,GoiÃ¡s,3460522
Ituiutaba,Brazil,Minas Gerais,3460523
ItuberÃ¡,Brazil,Bahia,3460530
Itu,Brazil,SÃ£o Paulo,3460535
ItororÃ³,Brazil,Bahia,3460542
ItaÃºna,Brazil,Minas Gerais,3460584
Itatinga,Brazil,SÃ£o Paulo,3460594
Itatiba,Brazil,SÃ£o Paulo,3460598
ItararÃ©,Brazil,SÃ£o Paulo,3460620
Itaqui,Brazil,Rio Grande do Sul,3460629
Itaquaquecetuba,Brazil,SÃ£o Paulo,3460644
Itapuranga,Brazil,GoiÃ¡s,3460648
ItÃ¡polis,Brazil,SÃ£o Paulo,3460671
Itapira,Brazil,SÃ£o Paulo,3460699
Itapevi,Brazil,SÃ£o Paulo,3460718
Itapeva,Brazil,SÃ£o Paulo,3460723
Itapetininga,Brazil,SÃ£o Paulo,3460728
Itapetinga,Brazil,Bahia,3460730
Itaperuna,Brazil,Rio de Janeiro,3460733
ItaperuÃ§u,Brazil,ParanÃ¡,3460734
Itapemirim,Brazil,EspÃ­rito Santo,3460738
Itapema,Brazil,Santa Catarina,3460740
Itapecerica da Serra,Brazil,SÃ£o Paulo,3460748
Itapecerica,Brazil,Minas Gerais,3460752
Itaparica,Brazil,Bahia,3460764
Itapaci,Brazil,GoiÃ¡s,3460773
Itaocara,Brazil,Rio de Janeiro,3460774
ItanhaÃ©m,Brazil,SÃ£o Paulo,3460791
ItambÃ©,Brazil,Bahia,3460813
Itamarandiba,Brazil,Minas Gerais,3460825
Itamaraju,Brazil,Bahia,3460826
ItajuÃ­pe,Brazil,Bahia,3460831
ItajubÃ¡,Brazil,Minas Gerais,3460834
ItajaÃ­,Brazil,Santa Catarina,3460845
ItaÃ­,Brazil,SÃ£o Paulo,3460887
ItaguaÃ­,Brazil,Rio de Janeiro,3460899
Itabuna,Brazil,Bahia,3460949
ItaboraÃ­,Brazil,Rio de Janeiro,3460950
Itabirito,Brazil,Minas Gerais,3460954
Itabira,Brazil,Minas Gerais,3460960
ItaberaÃ­,Brazil,GoiÃ¡s,3460963
Itaberaba,Brazil,Bahia,3460966
Itabaianinha,Brazil,Sergipe,3460971
Itabaiana,Brazil,Sergipe,3460974
IrecÃª,Brazil,Bahia,3461013
Irati,Brazil,ParanÃ¡,3461017
IracemÃ¡polis,Brazil,SÃ£o Paulo,3461055
IporÃ¡,Brazil,GoiÃ¡s,3461090
IpirÃ¡,Brazil,Bahia,3461124
IpiaÃº,Brazil,Bahia,3461129
IperÃ³,Brazil,SÃ£o Paulo,3461134
Ipatinga,Brazil,Minas Gerais,3461144
Ipameri,Brazil,GoiÃ¡s,3461151
Ipaba,Brazil,Minas Gerais,3461153
Inhumas,Brazil,GoiÃ¡s,3461194
Indaiatuba,Brazil,SÃ£o Paulo,3461311
Indaial,Brazil,Santa Catarina,3461316
Imbituva,Brazil,ParanÃ¡,3461368
Imbituba,Brazil,Santa Catarina,3461370
IlhÃ©us,Brazil,Bahia,3461408
Ilha Solteira,Brazil,SÃ£o Paulo,3461411
Ilhabela,Brazil,SÃ£o Paulo,3461425
IjuÃ­,Brazil,Rio Grande do Sul,3461444
Iguape,Brazil,SÃ£o Paulo,3461465
Igrejinha,Brazil,Rio Grande do Sul,3461481
IgarapÃ©,Brazil,Minas Gerais,3461498
Igarapava,Brazil,SÃ£o Paulo,3461499
IgaraÃ§u do TietÃª,Brazil,SÃ£o Paulo,3461501
IÃ§ara,Brazil,Santa Catarina,3461519
Ibotirama,Brazil,Bahia,3461525
IbiÃºna,Brazil,SÃ£o Paulo,3461528
Ibitinga,Brazil,SÃ£o Paulo,3461550
IbiritÃ©,Brazil,Minas Gerais,3461563
Ibirataia,Brazil,Bahia,3461565
Ibirama,Brazil,Santa Catarina,3461576
IbiporÃ£,Brazil,ParanÃ¡,3461588
IbicaraÃ­,Brazil,Bahia,3461606
IbiÃ¡,Brazil,Minas Gerais,3461620
IbatÃ©,Brazil,SÃ£o Paulo,3461625
Ibaiti,Brazil,ParanÃ¡,3461628
IaÃ§u,Brazil,Bahia,3461638
HortolÃ¢ndia,Brazil,SÃ£o Paulo,3461655
Herval,Brazil,Rio Grande do Sul,3461680
Gurupi,Brazil,Tocantins,3461724
GuaxupÃ©,Brazil,Minas Gerais,3461763
Guarulhos,Brazil,SÃ£o Paulo,3461786
GuarujÃ¡,Brazil,SÃ£o Paulo,3461789
Guariba,Brazil,SÃ£o Paulo,3461824
Guaratuba,Brazil,ParanÃ¡,3461857
GuaratinguetÃ¡,Brazil,SÃ£o Paulo,3461859
Guararema,Brazil,SÃ£o Paulo,3461871
Guararapes,Brazil,SÃ£o Paulo,3461874
Guarapuava,Brazil,ParanÃ¡,3461879
Guarapari,Brazil,EspÃ­rito Santo,3461888
GuaranÃ©sia,Brazil,Minas Gerais,3461910
Guaramirim,Brazil,Santa Catarina,3461914
GuarÃ¡,Brazil,SÃ£o Paulo,3461935
GuaporÃ©,Brazil,Rio Grande do Sul,3461941
Guapimirim,Brazil,Rio de Janeiro,3461949
GuanhÃ£es,Brazil,Minas Gerais,3461958
Guanambi,Brazil,Bahia,3461973
GuaÃ­ra,Brazil,SÃ£o Paulo,3461995
GuaÃ§uÃ­,Brazil,EspÃ­rito Santo,3462022
GravataÃ­,Brazil,Rio Grande do Sul,3462089
Governador Valadares,Brazil,Minas Gerais,3462315
Goiatuba,Brazil,GoiÃ¡s,3462371
GoiÃ¡s,Brazil,GoiÃ¡s,3462374
Goianira,Brazil,GoiÃ¡s,3462376
GoiÃ¢nia,Brazil,GoiÃ¡s,3462377
GoianÃ©sia,Brazil,GoiÃ¡s,3462378
Gaspar,Brazil,Santa Catarina,3462535
Garibaldi,Brazil,Rio Grande do Sul,3462557
GarÃ§a,Brazil,SÃ£o Paulo,3462580
Gandu,Brazil,Bahia,3462601
Frutal,Brazil,Minas Gerais,3462916
Frederico Westphalen,Brazil,Rio Grande do Sul,3462956
Franco da Rocha,Brazil,SÃ£o Paulo,3462964
Francisco Morato,Brazil,SÃ£o Paulo,3462980
Francisco BeltrÃ£o,Brazil,ParanÃ¡,3462996
Franca,Brazil,SÃ£o Paulo,3463011
Foz do IguaÃ§u,Brazil,ParanÃ¡,3463030
Forquilhinha,Brazil,Santa Catarina,3463066
Formosa,Brazil,GoiÃ¡s,3463140
Formiga,Brazil,Minas Gerais,3463174
FlorianÃ³polis,Brazil,Santa Catarina,3463237
Flores da Cunha,Brazil,Rio Grande do Sul,3463271
Ferraz de Vasconcelos,Brazil,SÃ£o Paulo,3463422
FernandÃ³polis,Brazil,SÃ£o Paulo,3463432
Feira de Santana,Brazil,Bahia,3463478
Farroupilha,Brazil,Rio Grande do Sul,3463605
Euclides da Cunha,Brazil,Bahia,3463698
Estrela,Brazil,Rio Grande do Sul,3463762
Esteio,Brazil,Rio Grande do Sul,3463859
EstÃ¢ncia Velha,Brazil,Rio Grande do Sul,3463865
EstÃ¢ncia,Brazil,Sergipe,3463900
Esplanada,Brazil,Bahia,3463920
Espinosa,Brazil,Minas Gerais,3463939
Esmeraldas,Brazil,Minas Gerais,3464008
Erechim,Brazil,Rio Grande do Sul,3464073
Entre Rios,Brazil,Bahia,3464100
Encruzilhada do Sul,Brazil,Rio Grande do Sul,3464255
Encantado,Brazil,Rio Grande do Sul,3464274
Embu GuaÃ§u,Brazil,SÃ£o Paulo,3464304
Embu,Brazil,SÃ£o Paulo,3464305
ElÃ³i Mendes,Brazil,Minas Gerais,3464329
Duque de Caxias,Brazil,Rio de Janeiro,3464374
Dourados,Brazil,Mato Grosso do Sul,3464460
Dom Pedrito,Brazil,Rio Grande do Sul,3464547
Dois Vizinhos,Brazil,ParanÃ¡,3464579
Dois CÃ³rregos,Brazil,SÃ£o Paulo,3464618
DivinÃ³polis,Brazil,Minas Gerais,3464688
Diamantino,Brazil,Mato Grosso,3464724
Diamantina,Brazil,Minas Gerais,3464728
Diadema,Brazil,SÃ£o Paulo,3464739
Descalvado,Brazil,SÃ£o Paulo,3464809
Curvelo,Brazil,Minas Gerais,3464891
Curitibanos,Brazil,Santa Catarina,3464974
Curitiba,Brazil,ParanÃ¡,3464975
CuiabÃ¡,Brazil,Mato Grosso,3465038
CubatÃ£o,Brazil,SÃ£o Paulo,3465059
Cruzeiro do Oeste,Brazil,ParanÃ¡,3465083
Cruzeiro,Brazil,SÃ£o Paulo,3465090
Cruz das Almas,Brazil,Bahia,3465105
Cruz Alta,Brazil,Rio Grande do Sul,3465108
Cristalina,Brazil,GoiÃ¡s,3465164
CriciÃºma,Brazil,Santa Catarina,3465196
Cravinhos,Brazil,SÃ£o Paulo,3465209
Coxim,Brazil,Mato Grosso do Sul,3465228
Cotia,Brazil,SÃ£o Paulo,3465284
CosmÃ³polis,Brazil,SÃ£o Paulo,3465320
Coruripe,Brazil,Alagoas,3465329
CorumbÃ¡,Brazil,Mato Grosso do Sul,3465342
Coronel Vivida,Brazil,ParanÃ¡,3465459
Coronel Fabriciano,Brazil,Minas Gerais,3465476
Coromandel,Brazil,Minas Gerais,3465487
CornÃ©lio ProcÃ³pio,Brazil,ParanÃ¡,3465508
Corinto,Brazil,Minas Gerais,3465512
CordeirÃ³polis,Brazil,SÃ£o Paulo,3465524
Cordeiro,Brazil,Rio de Janeiro,3465527
Contagem,Brazil,Minas Gerais,3465624
Conselheiro Lafaiete,Brazil,Minas Gerais,3465644
Congonhas,Brazil,Minas Gerais,3465671
Conde,Brazil,Bahia,3465713
ConcÃ³rdia,Brazil,Santa Catarina,3465721
Conchal,Brazil,SÃ£o Paulo,3465731
ConceiÃ§Ã£o do CoitÃ©,Brazil,Bahia,3465748
ConceiÃ§Ã£o do JacuÃ­pe,Brazil,Bahia,3465758
ConceiÃ§Ã£o das Alagoas,Brazil,Minas Gerais,3465764
ConceiÃ§Ã£o da Feira,Brazil,Bahia,3465767
ConceiÃ§Ã£o da Barra,Brazil,EspÃ­rito Santo,3465769
Colorado,Brazil,ParanÃ¡,3465881
Colombo,Brazil,ParanÃ¡,3465927
Colatina,Brazil,EspÃ­rito Santo,3465944
Coaraci,Brazil,Bahia,3466041
ClÃ¡udio,Brazil,Minas Gerais,3466062
CÃ­cero Dantas,Brazil,Bahia,3466171
Cianorte,Brazil,ParanÃ¡,3466174
Charqueadas,Brazil,Rio Grande do Sul,3466261
ChapecÃ³,Brazil,Santa Catarina,3466296
Cerquilho,Brazil,SÃ£o Paulo,3466429
Ceres,Brazil,GoiÃ¡s,3466436
Celso Ramos,Brazil,Santa Catarina,3466481
Caxias do Sul,Brazil,Rio Grande do Sul,3466537
Caxambu,Brazil,Minas Gerais,3466547
Catu,Brazil,Bahia,3466641
Catanduva,Brazil,SÃ£o Paulo,3466692
CatalÃ£o,Brazil,GoiÃ¡s,3466696
Cataguases,Brazil,Minas Gerais,3466698
Castro,Brazil,ParanÃ¡,3466704
Castelo,Brazil,EspÃ­rito Santo,3466723
CassilÃ¢ndia,Brazil,Mato Grosso do Sul,3466750
Casimiro de Abreu,Brazil,Rio de Janeiro,3466763
Cascavel,Brazil,ParanÃ¡,3466779
Casa Branca,Brazil,SÃ£o Paulo,3466824
Carmo do ParanaÃ­ba,Brazil,Minas Gerais,3466902
Carmo do Cajuru,Brazil,Minas Gerais,3466903
Carlos Barbosa,Brazil,Rio Grande do Sul,3466933
Carazinho,Brazil,Rio Grande do Sul,3466978
Caratinga,Brazil,Minas Gerais,3466988
CarapicuÃ­ba,Brazil,SÃ£o Paulo,3466998
Carangola,Brazil,Minas Gerais,3467012
CarandaÃ­,Brazil,Minas Gerais,3467026
Caraguatatuba,Brazil,SÃ£o Paulo,3467081
Capivari,Brazil,SÃ£o Paulo,3467197
Capinzal,Brazil,Santa Catarina,3467261
Capim Grosso,Brazil,Bahia,3467272
Capelinha,Brazil,Minas Gerais,3467305
Capela,Brazil,Sergipe,3467319
CapÃ£o da Canoa,Brazil,Rio Grande do Sul,3467362
CapÃ¢o Bonito,Brazil,SÃ£o Paulo,3467371
Canoinhas,Brazil,Santa Catarina,3467452
Canoas,Brazil,Rio Grande do Sul,3467467
CanguÃ§u,Brazil,Rio Grande do Sul,3467512
Canela,Brazil,Rio Grande do Sul,3467530
CÃ¢ndido Mota,Brazil,SÃ£o Paulo,3467542
CandelÃ¡ria,Brazil,Rio Grande do Sul,3467550
Canavieiras,Brazil,Bahia,3467577
Campo Verde,Brazil,Mato Grosso do Sul,3467673
Campos Novos,Brazil,Santa Catarina,3467677
Campos Gerais,Brazil,Minas Gerais,3467680
Campos do JordÃ£o,Brazil,SÃ£o Paulo,3467684
Campos Belos,Brazil,GoiÃ¡s,3467687
Campos,Brazil,Rio de Janeiro,3467693
Campo MourÃ£o,Brazil,ParanÃ¡,3467717
Campo Largo,Brazil,ParanÃ¡,3467736
Campo Grande,Brazil,Mato Grosso do Sul,3467747
Campo Formoso,Brazil,Bahia,3467760
Campo Belo,Brazil,Minas Gerais,3467796
Campinas,Brazil,SÃ£o Paulo,3467865
Campina Grande do Sul,Brazil,ParanÃ¡,3467877
CambuÃ­,Brazil,Minas Gerais,3467956
CambÃ©,Brazil,ParanÃ¡,3467978
CambarÃ¡,Brazil,ParanÃ¡,3467985
CamaquÃ£,Brazil,Rio Grande do Sul,3468014
Camanducaia,Brazil,Minas Gerais,3468023
CamaÃ§ari,Brazil,Bahia,3468031
Caldas Novas,Brazil,GoiÃ¡s,3468100
Cajuru,Brazil,SÃ£o Paulo,3468121
Cajati,Brazil,SÃ£o Paulo,3468157
Cajamar,Brazil,SÃ£o Paulo,3468158
Caieiras,Brazil,SÃ£o Paulo,3468215
CaetitÃ©,Brazil,Bahia,3468317
CaetÃ©,Brazil,Minas Gerais,3468327
Cachoeiro de Itapemirim,Brazil,EspÃ­rito Santo,3468376
Cachoeirinha,Brazil,Rio Grande do Sul,3468403
Cachoeiras de Macacu,Brazil,Rio de Janeiro,3468425
Cachoeira do Sul,Brazil,Rio Grande do Sul,3468436
Cachoeira,Brazil,Bahia,3468535
CaÃ§apava do Sul,Brazil,Rio Grande do Sul,3468560
CaÃ§apava,Brazil,SÃ£o Paulo,3468562
CaÃ§ador,Brazil,Santa Catarina,3468570
CabreÃºva,Brazil,SÃ£o Paulo,3468592
Cabo Frio,Brazil,Rio de Janeiro,3468615
ButiÃ¡,Brazil,Rio Grande do Sul,3468704
Buritizeiro,Brazil,Minas Gerais,3468720
Buritis,Brazil,Minas Gerais,3468732
Buri,Brazil,SÃ£o Paulo,3468802
Buerarema,Brazil,Bahia,3468858
Brusque,Brazil,Santa Catarina,3468879
Brumado,Brazil,Bahia,3468893
Brumadinho,Brazil,Minas Gerais,3468894
Brotas,Brazil,SÃ£o Paulo,3468899
BrodÃ³squi,Brazil,SÃ£o Paulo,3468902
BrasÃ­lia,Brazil,Federal District,3469058
BraganÃ§a Paulista,Brazil,SÃ£o Paulo,3469092
BraÃ§o do Norte,Brazil,Santa Catarina,3469115
Botucatu,Brazil,SÃ£o Paulo,3469136
Bom Jesus do Itabapoana,Brazil,Rio de Janeiro,3469425
Bom Jesus da Lapa,Brazil,Bahia,3469437
Bom Despacho,Brazil,Minas Gerais,3469516
Boituva,Brazil,SÃ£o Paulo,3469540
BocaiÃºva,Brazil,Minas Gerais,3469601
Boa EsperanÃ§a,Brazil,Minas Gerais,3469932
Blumenau,Brazil,Santa Catarina,3469968
Biritiba Mirim,Brazil,SÃ£o Paulo,3469984
Birigui,Brazil,SÃ£o Paulo,3469989
BiguaÃ§u,Brazil,Santa Catarina,3470003
Betim,Brazil,Minas Gerais,3470044
Bertioga,Brazil,SÃ£o Paulo,3470052
Bento GonÃ§alves,Brazil,Rio Grande do Sul,3470073
Belo Oriente,Brazil,Minas Gerais,3470117
Belo Horizonte,Brazil,Minas Gerais,3470127
Belford Roxo,Brazil,Rio de Janeiro,3470142
Bela Vista,Brazil,Mato Grosso do Sul,3470177
Bebedouro,Brazil,SÃ£o Paulo,3470264
Bauru,Brazil,SÃ£o Paulo,3470279
Batatais,Brazil,SÃ£o Paulo,3470324
Bastos,Brazil,SÃ£o Paulo,3470341
Barueri,Brazil,SÃ£o Paulo,3470353
Barroso,Brazil,Minas Gerais,3470369
Barrinha,Brazil,SÃ£o Paulo,3470428
Barretos,Brazil,SÃ£o Paulo,3470451
Barreiro do JaÃ­ba,Brazil,Minas Gerais,3470470
Barreiras,Brazil,Bahia,3470583
Barra Velha,Brazil,Santa Catarina,3470597
Barra Mansa,Brazil,Rio de Janeiro,3470636
Barra dos Coqueiros,Brazil,Sergipe,3470674
Barra do PiraÃ­,Brazil,Rio de Janeiro,3470691
Barra do GarÃ§as,Brazil,Mato Grosso,3470709
Barra do Bugres,Brazil,Mato Grosso,3470718
Barra de SÃ£o Francisco,Brazil,EspÃ­rito Santo,3470730
Barra Bonita,Brazil,SÃ£o Paulo,3470776
Barra,Brazil,Bahia,3470821
Bariri,Brazil,SÃ£o Paulo,3470825
Barbacena,Brazil,Minas Gerais,3470858
BarÃ£o de Cocais,Brazil,Minas Gerais,3470878
Bandeirantes,Brazil,ParanÃ¡,3470912
BambuÃ­,Brazil,Minas Gerais,3471005
BalneÃ¡rio CamboriÃº,Brazil,Santa Catarina,3471039
Baixo Guandu,Brazil,EspÃ­rito Santo,3471061
BagÃ©,Brazil,Rio Grande do Sul,3471196
AvarÃ©,Brazil,SÃ£o Paulo,3471291
Atibaia,Brazil,SÃ£o Paulo,3471335
Astorga,Brazil,ParanÃ¡,3471368
Assis,Brazil,SÃ£o Paulo,3471374
ArujÃ¡,Brazil,SÃ£o Paulo,3471393
Artur Nogueira,Brazil,SÃ£o Paulo,3471395
Arroio Grande,Brazil,Rio Grande do Sul,3471422
Arroio do Meio,Brazil,Rio Grande do Sul,3471428
Arraial do Cabo,Brazil,Rio de Janeiro,3471451
ArmaÃ§Ã£o de BÃºzios,Brazil,Rio de Janeiro,3471487
Arcos,Brazil,Minas Gerais,3471683
AraxÃ¡,Brazil,Minas Gerais,3471691
AraucÃ¡ria,Brazil,ParanÃ¡,3471697
Araruama,Brazil,Rio de Janeiro,3471715
Araras,Brazil,SÃ£o Paulo,3471758
Araraquara,Brazil,SÃ£o Paulo,3471766
AraranguÃ¡,Brazil,Santa Catarina,3471772
Arapongas,Brazil,ParanÃ¡,3471798
Araguari,Brazil,Minas Gerais,3471830
AragarÃ§as,Brazil,GoiÃ¡s,3471840
AraÃ§uaÃ­,Brazil,Minas Gerais,3471846
Aracruz,Brazil,EspÃ­rito Santo,3471848
AraÃ§oiaba da Serra,Brazil,SÃ£o Paulo,3471849
Araci,Brazil,Bahia,3471854
AraÃ§atuba,Brazil,SÃ£o Paulo,3471859
Aracaju,Brazil,Sergipe,3471872
Aquidauana,Brazil,Mato Grosso do Sul,3471896
Apucarana,Brazil,ParanÃ¡,3471910
ApiaÃ­,Brazil,SÃ£o Paulo,3471927
Aparecida do Taboado,Brazil,Mato Grosso do Sul,3471940
Aparecida,Brazil,SÃ£o Paulo,3471949
Antonina,Brazil,ParanÃ¡,3472048
Anicuns,Brazil,GoiÃ¡s,3472138
Angra dos Reis,Brazil,Rio de Janeiro,3472177
Andradina,Brazil,SÃ£o Paulo,3472248
Andradas,Brazil,Minas Gerais,3472254
AnastÃ¡cio,Brazil,Mato Grosso do Sul,3472284
AnÃ¡polis,Brazil,GoiÃ¡s,3472287
Amparo,Brazil,SÃ£o Paulo,3472311
AmÃ©rico Brasiliense,Brazil,SÃ£o Paulo,3472338
Americana,Brazil,SÃ£o Paulo,3472343
Amargosa,Brazil,Bahia,3472370
Ãlvares Machado,Brazil,SÃ£o Paulo,3472417
Almirante TamandarÃ©,Brazil,ParanÃ¡,3472518
Almenara,Brazil,Minas Gerais,3472520
Alfenas,Brazil,Minas Gerais,3472603
AlÃ©m ParaÃ­ba,Brazil,Minas Gerais,3472609
Alegrete,Brazil,Rio Grande do Sul,3472638
Alegre,Brazil,EspÃ­rito Santo,3472666
Alagoinhas,Brazil,Bahia,3472766
AimorÃ©s,Brazil,Minas Gerais,3472808
Agudos,Brazil,SÃ£o Paulo,3472825
Ãguas Vermelhas,Brazil,Minas Gerais,3472848
Ãguas de LindÃ³ia,Brazil,SÃ£o Paulo,3472869
AguaÃ­,Brazil,SÃ£o Paulo,3472969
Adamantina,Brazil,SÃ£o Paulo,3473157
AbaetÃ©,Brazil,Minas Gerais,3473267
GuaÃ­ba,Brazil,Rio Grande do Sul,3473964
Palmas,Brazil,Tocantins,3474574
TefÃ©,Brazil,Amazonas,3661944
TarauacÃ¡,Brazil,Acre,3661980
Tabatinga,Brazil,Amazonas,3662075
Sena Madureira,Brazil,Acre,3662155
SÃ£o Gabriel da Cachoeira,Brazil,Amazonas,3662342
Rio Branco,Brazil,Acre,3662574
Porto Velho,Brazil,RondÃ´nia,3662762
Manaus,Brazil,Amazonas,3663517
Manacapuru,Brazil,Amazonas,3663529
HumaitÃ¡,Brazil,Amazonas,3664078
Fonte Boa,Brazil,Amazonas,3664207
EirunepÃ©,Brazil,Amazonas,3664321
Cruzeiro do Sul,Brazil,Acre,3664464
Coari,Brazil,Amazonas,3664539
Carauari,Brazil,Amazonas,3664659
Boa Vista,Brazil,Roraima,3664980
Ariquemes,Brazil,RondÃ´nia,3665199
AripuanÃ£,Brazil,Mato Grosso,3665202
Vilhena,Brazil,RondÃ´nia,3924679
PÃ´sto Fiscal Rolim de Moura,Brazil,RondÃ´nia,3924877
Pimenta Bueno,Brazil,RondÃ´nia,3924908
Ouro Preto do Oeste,Brazil,RondÃ´nia,3924948
Ji ParanÃ¡,Brazil,RondÃ´nia,3925033
Jaru,Brazil,RondÃ´nia,3925040
GuajarÃ¡ Mirim,Brazil,RondÃ´nia,3925075
Cacoal,Brazil,RondÃ´nia,3925212
Aparecida de GoiÃ¢nia,Brazil,GoiÃ¡s,6316406
Campinas,Brazil,Santa Catarina,6316729
JaboatÃ£o dos Guararapes,Brazil,Pernambuco,6317344
Lauro de Freitas,Brazil,Bahia,6317464
Pinhais,Brazil,ParanÃ¡,6317953
Rio Preto da Eva,Brazil,Amazonas,6318165
SimÃµes Filho,Brazil,Bahia,6318694
Sinop,Brazil,Mato Grosso,6318696
Cambebba,Brazil,CearÃ¡,6693804
Trindade,Brazil,Santa Catarina,7874479
Freguesia do Ribeirao da Ilha,Brazil,Santa Catarina,7874492
Nassau,Bahamas,New Providence,3571824
Lucaya,Bahamas,Freeport,3571971
Freeport,Bahamas,Freeport,3572375
Thimphu,Bhutan,Thimphu,1252416
PunÄkha,Bhutan,Punakha,1252479
Phuntsholing,Bhutan,Chukha District,1252484
Tsirang,Bhutan,Chirang,1252608
Tonota,Botswana,Central,933000
Thamaga,Botswana,Kweneng,933018
Serowe,Botswana,Central,933088
Selebi-Phikwe,Botswana,Central,933099
Ramotswa,Botswana,South East,933141
Palapye,Botswana,Central,933182
Mosopa,Botswana,Southern,933271
Molepolole,Botswana,Kweneng,933305
Mogoditshane,Botswana,Kweneng,933331
Mochudi,Botswana,Kgatleng,933340
Maun,Botswana,North West,933366
Mahalapye,Botswana,Central,933471
Lobatse,Botswana,South East,933521
Letlhakane,Botswana,Central,933535
Kanye,Botswana,Southern,933685
Janeng,Botswana,South East,933719
Gaborone,Botswana,South East,933773
Francistown,Botswana,North East,933778
Horad Zhodzina,Belarus,Minsk,618800
Zhlobin,Belarus,Gomel,618806
Vitebsk,Belarus,Vitebsk,620127
Vilyeyka,Belarus,Minsk,620181
Vawkavysk,Belarus,Grodnenskaya,620391
Svyetlahorsk,Belarus,Gomel,621074
Stowbtsy,Belarus,Minsk,621266
Smarhonâ€™,Belarus,Grodnenskaya,621713
Slutsk,Belarus,Minsk,621741
Slonim,Belarus,Grodnenskaya,621754
Shchuchin,Belarus,Grodnenskaya,622113
Salihorsk,Belarus,Minsk,622428
Rahachow,Belarus,Gomel,622739
Rechytsa,Belarus,Gomel,622794
Pruzhany,Belarus,Brest,622997
Polatsk,Belarus,Vitebsk,623317
Pinsk,Belarus,Brest,623549
Pastavy,Belarus,Vitebsk,623760
Asipovichy,Belarus,Mogilev,624034
Orsha,Belarus,Vitebsk,624079
Novoye Medvezhino,Belarus,Minsk City,624400
Navapolatsk,Belarus,Vitebsk,624784
Navahrudak,Belarus,Grodnenskaya,624785
Minsk,Belarus,Minsk City,625144
Mazyr,Belarus,Gomel,625324
Masty,Belarus,Grodnenskaya,625367
Marâ€™â€™ina Horka,Belarus,Minsk,625409
Maladzyechna,Belarus,Minsk,625625
Mahilyow,Belarus,Mogilev,625665
Lyepyelâ€™,Belarus,Vitebsk,625743
Luninyets,Belarus,Brest,625818
Lida,Belarus,Grodnenskaya,626081
Krychaw,Belarus,Mogilev,626450
Kalodzishchy,Belarus,Minsk,627083
Kobryn,Belarus,Brest,627145
Kalinkavichy,Belarus,Gomel,627751
Ivatsevichy,Belarus,Brest,627800
Hrodna,Belarus,Grodnenskaya,627904
Horki,Belarus,Mogilev,627905
Gomel,Belarus,Gomel,627907
Hlybokaye,Belarus,Vitebsk,627908
Dzyarzhynsk,Belarus,Minsk,628634
Dobrush,Belarus,Gomel,629018
Bykhaw,Belarus,Mogilev,629447
Byaroza,Belarus,Brest,629454
Brest,Belarus,Brest,629634
Horad Barysaw,Belarus,Minsk,630376
Baranovichi,Belarus,Brest,630429
Babruysk,Belarus,Mogilev,630468
Malinovka,Belarus,Minsk City,8020218
San Ignacio,Belize,Cayo,3581194
Orange Walk,Belize,Orange Walk,3581514
Belmopan,Belize,Cayo,3582672
Belize City,Belize,Belize,3582677
Abbotsford,Canada,British Columbia,5881791
Airdrie,Canada,Alberta,5882799
Ajax,Canada,Ontario,5882873
Alma,Canada,Quebec,5884083
Amos,Canada,Quebec,5884588
Anmore,Canada,British Columbia,5885383
Baie-Comeau,Canada,Quebec,5889745
Barrie,Canada,Ontario,5894171
Beaconsfield,Canada,Quebec,5895650
Belleville,Canada,Ontario,5897884
Beloeil,Canada,Quebec,5898138
Blainville,Canada,Quebec,5903510
Boisbriand,Canada,Quebec,5905132
Boucherville,Canada,Quebec,5906267
Bradford West Gwillimbury,Canada,Ontario,5907180
Brampton,Canada,Ontario,5907364
Brandon,Canada,Manitoba,5907896
Brant,Canada,Ontario,5907983
Brantford,Canada,Ontario,5907990
Brockville,Canada,Ontario,5909294
Brossard,Canada,Quebec,5909629
Burlington,Canada,Ontario,5911592
Burnaby,Canada,British Columbia,5911606
Calgary,Canada,Alberta,5913490
Cambridge,Canada,Ontario,5913695
Campbell River,Canada,British Columbia,5914132
Camrose,Canada,Alberta,5914653
Candiac,Canada,Quebec,5914826
Chambly,Canada,Quebec,5919566
Charlottetown,Canada,Prince Edward Island,5920288
ChÃ¢teauguay,Canada,Quebec,5920433
Chilliwack,Canada,British Columbia,5921356
Clarence-Rockland,Canada,Ontario,5923101
Cobourg,Canada,Ontario,5924579
Cochrane,Canada,Alberta,5924618
Collingwood,Canada,Ontario,5925975
Conception Bay South,Canada,Newfoundland and Labrador,5926511
Coquitlam,Canada,British Columbia,5927689
Corner Brook,Canada,Newfoundland and Labrador,5927969
Cornwall,Canada,Ontario,5928065
CÃ´te-Saint-Luc,Canada,Quebec,5928488
Courtenay,Canada,British Columbia,5930890
Cranbrook,Canada,British Columbia,5931800
Dartmouth,Canada,Nova Scotia,5935277
Delta,Canada,British Columbia,5937615
Deux-Montagnes,Canada,Quebec,5938513
Dieppe,Canada,New Brunswick,5939219
Dollard-Des Ormeaux,Canada,Quebec,5940956
Dorval,Canada,Quebec,5941925
Drummondville,Canada,Quebec,5942845
Duncan,Canada,British Columbia,5943865
Edmonton,Canada,Alberta,5946768
Etobicoke,Canada,Ontario,5950267
Fort Erie,Canada,Ontario,5955815
Fort McMurray,Canada,Alberta,5955895
Fort St. John,Canada,British Columbia,5955960
Fredericton,Canada,New Brunswick,5957776
Gatineau,Canada,Quebec,5959974
Glace Bay,Canada,Nova Scotia,5961564
Granby,Canada,Quebec,5964215
Grande Prairie,Canada,Alberta,5964347
Greater Sudbury,Canada,Ontario,5964700
Greater Napanee,Canada,Ontario,5965812
Guelph,Canada,Ontario,5967629
Hamilton,Canada,Ontario,5969782
Huntsville,Canada,Ontario,5978765
Joliette,Canada,Quebec,5987650
Kamloops,Canada,British Columbia,5989045
Kelowna,Canada,British Columbia,5990579
Keswick,Canada,Ontario,5991370
Kingston,Canada,Ontario,5992500
Kirkland,Canada,Quebec,5992830
Kitchener,Canada,Ontario,5992996
Langford,Canada,British Columbia,6049388
Langley,Canada,British Columbia,6049429
Langley,Canada,British Columbia,6049430
La Prairie,Canada,Quebec,6049863
L'Assomption,Canada,Quebec,6050263
Laval,Canada,Quebec,6050610
Leduc,Canada,Alberta,6051562
Lethbridge,Canada,Alberta,6053154
Lloydminster,Canada,Saskatchewan,6058024
London,Canada,Ontario,6058560
Longueuil,Canada,Quebec,6059891
Magog,Canada,Quebec,6064180
Maple Ridge,Canada,British Columbia,6065686
Markham,Canada,Ontario,6066513
Mascouche,Canada,Quebec,6067494
Medicine Hat,Canada,Alberta,6071618
Midland,Canada,Ontario,6073363
Milton,Canada,Ontario,6074377
Mirabel,Canada,Quebec,6075061
Miramichi,Canada,New Brunswick,6075081
Mississauga,Canada,Ontario,6075357
Moncton,Canada,New Brunswick,6076211
MontrÃ©al,Canada,Quebec,6077243
Mont-Royal,Canada,Quebec,6077315
Mont-Saint-Hilaire,Canada,Quebec,6077340
Moose Jaw,Canada,Saskatchewan,6078112
Mount Pearl,Canada,Newfoundland and Labrador,6082231
Nanaimo,Canada,British Columbia,6085772
New Glasgow,Canada,Nova Scotia,6087579
Newmarket,Canada,Ontario,6087701
New Westminster,Canada,British Columbia,6087844
Niagara Falls,Canada,Ontario,6087892
Norfolk County,Canada,Ontario,6089125
North Battleford,Canada,Saskatchewan,6089404
North Bay,Canada,Ontario,6089426
North Cowichan,Canada,British Columbia,6089661
North Vancouver,Canada,British Columbia,6090785
North York,Canada,Ontario,6091104
Oak Bay,Canada,British Columbia,6091919
Oakville,Canada,Ontario,6092122
Orangeville,Canada,Ontario,6094201
Orillia,Canada,Ontario,6094325
Oshawa,Canada,Ontario,6094578
Ottawa,Canada,Ontario,6094817
Owen Sound,Canada,Ontario,6095645
Parksville,Canada,British Columbia,6098642
Pembroke,Canada,Ontario,6100832
Penticton,Canada,British Columbia,6101141
Petawawa,Canada,Ontario,6101606
Peterborough,Canada,Ontario,6101645
Pickering,Canada,Ontario,6104111
Pitt Meadows,Canada,British Columbia,6105815
Pointe-Claire,Canada,Quebec,6107325
Port Alberni,Canada,British Columbia,6111632
Port Colborne,Canada,Ontario,6111704
Port Moody,Canada,British Columbia,6111962
Prince Albert,Canada,Saskatchewan,6113335
Prince Edward,Canada,Ontario,6113355
Prince George,Canada,British Columbia,6113365
Quinte West,Canada,Ontario,6115355
Rayside-Balfour,Canada,Ontario,6117731
Red Deer,Canada,Alberta,6118158
Regina,Canada,Saskatchewan,6119109
Repentigny,Canada,Quebec,6119518
Richmond,Canada,British Columbia,6122085
Richmond Hill,Canada,Ontario,6122091
Rouyn-Noranda,Canada,Quebec,6128577
Saguenay,Canada,Quebec,6137270
Saint-Basile-le-Grand,Canada,Quebec,6137489
Saint-Bruno-de-Montarville,Canada,Quebec,6137540
Saint-Constant,Canada,Quebec,6137633
Sainte-Catherine,Canada,Quebec,6137781
Sainte-Julie,Canada,Quebec,6137941
Sainte-ThÃ©rÃ¨se,Canada,Quebec,6138121
Saint-Eustache,Canada,Quebec,6138175
Saint-Hyacinthe,Canada,Quebec,6138374
Saint-Jean-sur-Richelieu,Canada,Quebec,6138495
Saint-JÃ©rÃ´me,Canada,Quebec,6138501
Saint John,Canada,New Brunswick,6138517
Saint-Laurent,Canada,Quebec,6138610
Saint-Lazare,Canada,Quebec,6138617
Saint-LÃ©onard,Canada,Quebec,6138625
Salaberry-de-Valleyfield,Canada,Quebec,6139289
Salmon Arm,Canada,British Columbia,6139416
Sarnia,Canada,Ontario,6141190
Saskatoon,Canada,Saskatchewan,6141256
Sault Ste. Marie,Canada,Ontario,6141439
Sept-ÃŽles,Canada,Quebec,6144312
Shawinigan,Canada,Quebec,6145489
Sherbrooke,Canada,Quebec,6146143
Sherwood Park,Canada,Alberta,6146279
Sorel-Tracy,Canada,Quebec,6151352
Spruce Grove,Canada,Alberta,6154383
St. Albert,Canada,Alberta,6155033
St. Catharines,Canada,Ontario,6155721
Stratford,Canada,Ontario,6157977
St. Thomas,Canada,Ontario,6158357
Surrey,Canada,British Columbia,6159905
Terrace,Canada,British Columbia,6162949
Terrebonne,Canada,Quebec,6163012
Thorold,Canada,Ontario,6165719
Thunder Bay,Canada,Ontario,6166142
Timmins,Canada,Ontario,6166739
Toronto,Canada,Ontario,6167865
Trois-RiviÃ¨res,Canada,Quebec,6169141
Truro,Canada,Nova Scotia,6169587
Val-d'Or,Canada,Quebec,6173017
Vancouver,Canada,British Columbia,6173331
Varennes,Canada,Quebec,6173508
Vaudreuil-Dorion,Canada,Quebec,6173570
Vaughan,Canada,Ontario,6173577
Vernon,Canada,British Columbia,6173864
Victoria,Canada,British Columbia,6174041
Victoriaville,Canada,Quebec,6174151
Waterloo,Canada,Ontario,6176823
Welland,Canada,Ontario,6177869
West End,Canada,British Columbia,6178582
Westmount,Canada,Quebec,6179226
Whitehorse,Canada,Yukon,6180550
White Rock,Canada,British Columbia,6180961
Windsor,Canada,Ontario,6182962
Winnipeg,Canada,Manitoba,6183235
Woodstock,Canada,Ontario,6184365
Yellowknife,Canada,Northwest Territories,6185377
Yorkton,Canada,Saskatchewan,6185607
Halifax,Canada,Nova Scotia,6324729
St. John's,Canada,Newfoundland and Labrador,6324733
QuÃ©bec,Canada,Quebec,6325494
LÃ©vis,Canada,Quebec,6325521
Rimouski,Canada,Quebec,6354895
RiviÃ¨re-du-Loup,Canada,Quebec,6354897
Sydney,Canada,Nova Scotia,6354908
L'Ancienne-Lorette,Canada,Quebec,6534203
Edmundston,Canada,New Brunswick,6545023
Thetford-Mines,Canada,Quebec,6943827
Scarborough,Canada,Ontario,6948711
Cole Harbour,Canada,Nova Scotia,7280414
Okanagan,Canada,British Columbia,7281931
West Kelowna,Canada,British Columbia,7281936
Bellechasse Regional County Municipality,Canada,Quebec,7302647
JonquiÃ¨re,Canada,Quebec,7303786
Saint-Augustin-de-Desmaures,Canada,Quebec,7535681
Ladner,Canada,British Columbia,7602078
Walnut Grove,Canada,British Columbia,7669012
Ancaster,Canada,Ontario,8285452
West Vancouver,Canada,British Columbia,8533869
Willowdale,Canada,Ontario,8558534
Lower Sacvkille,Canada,Nova Scotia,10287505
West Island,Cocos Islands,N/A,7304591
Yangambi,Democratic Republic of the Congo,Eastern Province,203717
Watsa,Democratic Republic of the Congo,Eastern Province,204283
Wamba,Democratic Republic of the Congo,Eastern Province,204318
Uvira,Democratic Republic of the Congo,South Kivu,204405
Tshikapa,Democratic Republic of the Congo,KasaÃ¯-Occidental,204953
Sake,Democratic Republic of the Congo,Nord Kivu,205970
Mwene-Ditu,Democratic Republic of the Congo,KasaÃ¯-Oriental,207570
Mweka,Democratic Republic of the Congo,KasaÃ¯-Occidental,207596
Mbuji-Mayi,Democratic Republic of the Congo,KasaÃ¯-Oriental,209228
Lusambo,Democratic Republic of the Congo,KasaÃ¯-Oriental,210379
Luebo,Democratic Republic of the Congo,KasaÃ¯-Occidental,210939
Lubao,Democratic Republic of the Congo,KasaÃ¯-Oriental,211098
Lodja,Democratic Republic of the Congo,KasaÃ¯-Oriental,211647
Lisala,Democratic Republic of the Congo,Ã‰quateur,211734
Kongolo,Democratic Republic of the Congo,Katanga,212360
Kisangani,Democratic Republic of the Congo,Eastern Province,212730
Kindu,Democratic Republic of the Congo,Maniema,212902
Kasongo,Democratic Republic of the Congo,Maniema,213940
Kananga,Democratic Republic of the Congo,KasaÃ¯-Occidental,214481
Kampene,Democratic Republic of the Congo,Maniema,214575
Kamina,Democratic Republic of the Congo,Katanga,214614
Kalemie,Democratic Republic of the Congo,Katanga,214974
Kabinda,Democratic Republic of the Congo,KasaÃ¯-Oriental,215527
Kabare,Democratic Republic of the Congo,South Kivu,215605
Kabalo,Democratic Republic of the Congo,Katanga,215668
Isiro,Democratic Republic of the Congo,Eastern Province,215771
Ilebo,Democratic Republic of the Congo,KasaÃ¯-Occidental,215976
Goma,Democratic Republic of the Congo,Nord Kivu,216281
Gbadolite,Democratic Republic of the Congo,Ã‰quateur,216404
Gandajika,Democratic Republic of the Congo,KasaÃ¯-Oriental,216449
Demba,Democratic Republic of the Congo,KasaÃ¯-Occidental,217389
Butembo,Democratic Republic of the Congo,Nord Kivu,217562
Buta,Democratic Republic of the Congo,Eastern Province,217570
Businga,Democratic Republic of the Congo,Ã‰quateur,217637
Bunia,Democratic Republic of the Congo,Eastern Province,217695
Bumba,Democratic Republic of the Congo,Ã‰quateur,217745
Bukavu,Democratic Republic of the Congo,South Kivu,217831
Bukama,Democratic Republic of the Congo,Katanga,217834
Bondo,Democratic Republic of the Congo,Eastern Province,218253
Boende,Democratic Republic of the Congo,Ã‰quateur,218680
Beni,Democratic Republic of the Congo,Nord Kivu,219057
Basoko,Democratic Republic of the Congo,Eastern Province,219414
Aketi,Democratic Republic of the Congo,Eastern Province,220448
Lubumbashi,Democratic Republic of the Congo,Katanga,922704
Likasi,Democratic Republic of the Congo,Katanga,922741
Kolwezi,Democratic Republic of the Congo,Katanga,922773
Kipushi,Democratic Republic of the Congo,Katanga,922806
Kambove,Democratic Republic of the Congo,Katanga,923058
Tshela,Democratic Republic of the Congo,Bas-Congo,2311127
Nioki,Democratic Republic of the Congo,Bandundu,2311968
Mushie,Democratic Republic of the Congo,Bandundu,2312249
Mbanza-Ngungu,Democratic Republic of the Congo,Bas-Congo,2312888
Mbandaka,Democratic Republic of the Congo,Ã‰quateur,2312895
Matadi,Democratic Republic of the Congo,Bas-Congo,2313002
Mangai,Democratic Republic of the Congo,Bandundu,2313084
Libenge,Democratic Republic of the Congo,Ã‰quateur,2313762
Kinshasa,Democratic Republic of the Congo,Kinshasa,2314302
Kikwit,Democratic Republic of the Congo,Bandundu,2314705
Kasongo-Lunda,Democratic Republic of the Congo,Bandundu,2315026
Kasangulu,Democratic Republic of the Congo,Bas-Congo,2315057
Inongo,Democratic Republic of the Congo,Bandundu,2315417
Gemena,Democratic Republic of the Congo,Ã‰quateur,2315728
Bulungu,Democratic Republic of the Congo,Bandundu,2316259
Bolobo,Democratic Republic of the Congo,Bandundu,2316748
Bandundu,Democratic Republic of the Congo,Bandundu,2317397
Masina,Democratic Republic of the Congo,Kinshasa,2593460
Mobaye,Central African Republic,Basse-Kotto,237478
Ippy,Central African Republic,Ouaka,238566
Bria,Central African Republic,Haute-Kotto,239899
Bangassou,Central African Republic,Mbomou,240498
Bambari,Central African Republic,Ouaka,240604
Sibut,Central African Republic,KÃ©mo,2383119
Paoua,Central African Republic,Ouham-PendÃ©,2383523
Nola,Central African Republic,Sangha-MbaÃ©rÃ©,2383827
MbaÃ¯ki,Central African Republic,Lobaye,2384770
Kaga Bandoro,Central African Republic,Nana-GrÃ©bizi,2386012
Damara,Central African Republic,Ombella-Mpoko,2387435
Carnot,Central African Republic,MambÃ©rÃ©-KadÃ©Ã¯,2387495
Bozoum,Central African Republic,Ouham-PendÃ©,2387546
Bouar,Central African Republic,Nana-MambÃ©rÃ©,2387926
Bossangoa,Central African Republic,Ouham,2388036
Boda,Central African Republic,Lobaye,2388614
Bimbo,Central African Republic,Ombella-Mpoko,2388873
BerbÃ©rati,Central African Republic,MambÃ©rÃ©-KadÃ©Ã¯,2389086
Batangafo,Central African Republic,Ouham,2389691
Bangui,Central African Republic,Bangui,2389853
Sibiti,Republic of the Congo,LÃ©koumou,2255285
Pointe-Noire,Republic of the Congo,Pointe-Noire,2255414
Owando,Republic of the Congo,Cuvette,2255542
OuÃ©sso,Republic of the Congo,Sangha,2255564
Mossendjo,Republic of the Congo,Niari,2256895
Madingou,Republic of the Congo,Bouenza,2257990
Dolisie,Republic of the Congo,Niari,2258261
Loandjili,Republic of the Congo,Pointe-Noire,2258378
Kayes,Republic of the Congo,Bouenza,2259383
Impfondo,Republic of the Congo,Likouala,2259655
Gamboma,Republic of the Congo,Plateaux,2259947
Brazzaville,Republic of the Congo,Brazzaville,2260535
ZÃ¼rich,Switzerland,Zurich,2657896
Zug,Switzerland,Zug,2657908
Yverdon-les-Bains,Switzerland,Vaud,2657941
Winterthur,Switzerland,Zurich,2657970
Wil,Switzerland,Saint Gallen,2657996
Wettingen,Switzerland,Aargau,2658011
Vevey,Switzerland,Vaud,2658145
Vernier,Switzerland,Geneva,2658154
Uster,Switzerland,Zurich,2658216
Thun,Switzerland,Bern,2658377
Steffisburg,Switzerland,Bern,2658494
Sitten,Switzerland,Valais,2658576
Sierre,Switzerland,Valais,2658606
ZÃ¼rich (Kreis 11) / Seebach,Switzerland,Zurich,2658656
Schaffhausen,Switzerland,Schaffhausen,2658761
Sankt Gallen,Switzerland,Saint Gallen,2658822
Renens,Switzerland,Vaud,2659070
Rapperswil,Switzerland,Saint Gallen,2659099
Pully,Switzerland,Vaud,2659127
Onex,Switzerland,Geneva,2659296
Olten,Switzerland,Solothurn,2659297
ZÃ¼rich (Kreis 11) / Oerlikon,Switzerland,Zurich,2659310
Nyon,Switzerland,Vaud,2659422
NeuchÃ¢tel,Switzerland,NeuchÃ¢tel,2659496
Muttenz,Switzerland,Basel-Landschaft,2659522
Montreux,Switzerland,Vaud,2659601
Monthey,Switzerland,Valais,2659613
Meyrin,Switzerland,Geneva,2659667
Luzern,Switzerland,Lucerne,2659811
Lugano,Switzerland,Ticino,2659836
Littau,Switzerland,Lucerne,2659873
Le ChÃ¢telard,Switzerland,Vaud,2659977
Lausanne,Switzerland,Vaud,2659994
La Chaux-de-Fonds,Switzerland,NeuchÃ¢tel,2660076
Kriens,Switzerland,Lucerne,2660104
Kreuzlingen,Switzerland,Thurgau,2660108
KÃ¶niz,Switzerland,Bern,2660119
Kloten,Switzerland,Zurich,2660127
Jona,Switzerland,Saint Gallen,2660221
Horgen,Switzerland,Zurich,2660305
ZÃ¼rich (Kreis 10) / HÃ¶ngg,Switzerland,Zurich,2660306
Herisau,Switzerland,Appenzell Ausserrhoden,2660365
Grenchen,Switzerland,Solothurn,2660512
Gossau,Switzerland,Saint Gallen,2660549
GenÃ¨ve,Switzerland,Geneva,2660646
Fribourg,Switzerland,Fribourg,2660718
Frauenfeld,Switzerland,Thurgau,2660727
Emmen,Switzerland,Lucerne,2660911
DÃ¼bendorf,Switzerland,Zurich,2660971
Dietikon,Switzerland,Zurich,2661015
Chur,Switzerland,Grisons,2661169
Carouge,Switzerland,Geneva,2661265
Biel/Bienne,Switzerland,Bern,2661513
Bern,Switzerland,Bern,2661552
Bellinzona,Switzerland,Ticino,2661567
Basel,Switzerland,Basel-City,2661604
Baden,Switzerland,Aargau,2661646
Baar,Switzerland,Zug,2661653
ZÃ¼rich (Kreis 4),Switzerland,Zurich,2661666
Allschwil,Switzerland,Basel-Landschaft,2661810
Adliswil,Switzerland,Zurich,2661861
Aarau,Switzerland,Aargau,2661881
Riehen,Switzerland,Basel-City,3206590
ZÃ¼rich (Kreis 10) / Wipkingen,Switzerland,Zurich,6295475
ZÃ¼rich (Kreis 11) / Affoltern,Switzerland,Zurich,6295484
ZÃ¼rich (Kreis 2) / Wollishofen,Switzerland,Zurich,6295495
ZÃ¼rich (Kreis 3) / Sihlfeld,Switzerland,Zurich,6295498
ZÃ¼rich (Kreis 6) / Unterstrass,Switzerland,Zurich,6295504
ZÃ¼rich (Kreis 9) / Albisrieden,Switzerland,Zurich,6295512
ZÃ¼rich (Kreis 9) / Altstetten,Switzerland,Zurich,6295513
Stadt Winterthur (Kreis 1),Switzerland,Zurich,6295520
ZÃ¼rich (Kreis 12),Switzerland,Zurich,6295523
Seen (Kreis 3),Switzerland,Zurich,6295531
ZÃ¼rich (Kreis 3),Switzerland,Zurich,6295532
ZÃ¼rich (Kreis 11),Switzerland,Zurich,6295533
ZÃ¼rich (Kreis 9),Switzerland,Zurich,6295534
Oberwinterthur (Kreis 2),Switzerland,Zurich,6295536
ZÃ¼rich (Kreis 10),Switzerland,Zurich,6295539
ZÃ¼rich (Kreis 2),Switzerland,Zurich,6295540
ZÃ¼rich (Kreis 8),Switzerland,Zurich,6295542
ZÃ¼rich (Kreis 7),Switzerland,Zurich,6295548
ZÃ¼rich (Kreis 6),Switzerland,Zurich,6295550
Lancy,Switzerland,Geneva,6691640
ZuÃ©noula,Ivory Coast,MarahouÃ©,2279172
Yamoussoukro,Ivory Coast,Lacs,2279755
Vavoua,Ivory Coast,Haut-Sassandra,2280045
Toumodi,Ivory Coast,Lacs,2280316
Touba,Ivory Coast,Bafing,2280376
Tengrela,Ivory Coast,Savanes,2280589
TiassalÃ©,Ivory Coast,Lagunes,2280761
Tanda,Ivory Coast,Zanzan,2280995
Tabou,Ivory Coast,Bas-Sassandra,2281120
Sinfra,Ivory Coast,Zanzan,2281606
Sassandra,Ivory Coast,Bas-Sassandra,2281951
San-PÃ©dro,Ivory Coast,Bas-Sassandra,2282006
Sakassou,Ivory Coast,VallÃ©e du Bandama,2282178
OumÃ©,Ivory Coast,Fromager,2282827
OdiennÃ©,Ivory Coast,DenguÃ©lÃ©,2283016
Mankono,Ivory Coast,Worodougou,2284589
Man,Ivory Coast,Dix-Huit Montagnes,2284647
Lakota,Ivory Coast,Sud-Bandama,2285449
Korhogo,Ivory Coast,Savanes,2286304
Katiola,Ivory Coast,VallÃ©e du Bandama,2287298
Issia,Ivory Coast,Haut-Sassandra,2287790
Guiglo,Ivory Coast,Dix-Huit Montagnes,2287958
Grand-Bassam,Ivory Coast,Sud-ComoÃ©,2288115
Affery,Ivory Coast,Lagunes,2288118
Gagnoa,Ivory Coast,Fromager,2288829
FerkessÃ©dougou,Ivory Coast,Savanes,2289049
DuekouÃ©,Ivory Coast,Dix-Huit Montagnes,2289549
Divo,Ivory Coast,Sud-Bandama,2289887
Dimbokro,Ivory Coast,Lacs,2289983
Daoukro,Ivory Coast,NÊ¼zi-ComoÃ©,2290412
DananÃ©,Ivory Coast,Dix-Huit Montagnes,2290462
Daloa,Ivory Coast,Haut-Sassandra,2290486
Dabou,Ivory Coast,Lagunes,2290582
Boundiali,Ivory Coast,Savanes,2290836
Bouna,Ivory Coast,Zanzan,2290849
BouakÃ©,Ivory Coast,VallÃ©e du Bandama,2290956
BouaflÃ©,Ivory Coast,MarahouÃ©,2290964
Bonoua,Ivory Coast,Sud-ComoÃ©,2291087
Bongouanou,Ivory Coast,Lacs,2291113
Bondoukou,Ivory Coast,Zanzan,2291136
Bingerville,Ivory Coast,Lagunes,2291580
Biankouma,Ivory Coast,Dix-Huit Montagnes,2291666
BÃ©oumi,Ivory Coast,VallÃ©e du Bandama,2291779
Bangolo,Ivory Coast,Dix-Huit Montagnes,2292179
Arrah,Ivory Coast,Lacs,2292755
Anyama,Ivory Coast,Lagunes,2292852
AkoupÃ©,Ivory Coast,Lagunes,2293107
AgnibilÃ©krou,Ivory Coast,Moyen-ComoÃ©,2293260
Agboville,Ivory Coast,AgnÃ©by,2293268
AdzopÃ©,Ivory Coast,Lagunes,2293342
AdiakÃ©,Ivory Coast,Sud-ComoÃ©,2293428
Aboisso,Ivory Coast,Sud-ComoÃ©,2293507
Abobo,Ivory Coast,Lagunes,2293521
Abidjan,Ivory Coast,Lagunes,2293538
Abengourou,Ivory Coast,Moyen-ComoÃ©,2293549
SÃ©guÃ©la,Ivory Coast,Worodougou,2596934
SoubrÃ©,Ivory Coast,Bas-Sassandra,2598243
Avarua,Cook Islands,N/A,4035715
ViÃ±a del Mar,Chile,ValparaÃ­so,3868121
Villarrica,Chile,AraucanÃ­a,3868158
Villa Alemana,Chile,ValparaÃ­so,3868192
Victoria,Chile,AraucanÃ­a,3868326
ValparaÃ­so,Chile,ValparaÃ­so,3868626
Vallenar,Chile,Atacama,3868633
Valdivia,Chile,Los RÃ­os,3868707
TomÃ©,Chile,BiobÃ­o,3869657
Tocopilla,Chile,Antofagasta,3869716
Temuco,Chile,AraucanÃ­a,3870011
Talcahuano,Chile,BiobÃ­o,3870282
Talca,Chile,Maule,3870294
Talagante,Chile,Santiago Metropolitan,3870306
San Vicente de Tagua Tagua,Chile,O'Higgins,3871276
San Vicente,Chile,O'Higgins,3871286
Santiago,Chile,Santiago Metropolitan,3871336
Santa Cruz,Chile,O'Higgins,3871616
San Javier,Chile,Maule,3872154
San Felipe,Chile,ValparaÃ­so,3872255
San Carlos,Chile,BiobÃ­o,3872326
San Bernardo,Chile,Santiago Metropolitan,3872348
San Antonio,Chile,ValparaÃ­so,3872395
RÃ­o Bueno,Chile,Los RÃ­os,3873145
Rengo,Chile,O'Higgins,3873441
Rancagua,Chile,O'Higgins,3873775
QuilpuÃ©,Chile,ValparaÃ­so,3874096
Quillota,Chile,ValparaÃ­so,3874119
Punta Arenas,Chile,Magallanes,3874787
Puerto Varas,Chile,Los Lagos,3874930
Puerto QuellÃ³n,Chile,Los Lagos,3874943
Puerto Natales,Chile,Magallanes,3874958
Puerto Montt,Chile,Los Lagos,3874960
Puerto AisÃ©n,Chile,AisÃ©n,3874997
Puente Alto,Chile,Santiago Metropolitan,3875024
PucÃ³n,Chile,AraucanÃ­a,3875070
Penco,Chile,BiobÃ­o,3876664
PeÃ±aflor,Chile,Santiago Metropolitan,3876685
Parral,Chile,Maule,3877146
Panguipulli,Chile,AraucanÃ­a,3877348
Paine,Chile,Santiago Metropolitan,3877739
Ovalle,Chile,Coquimbo,3877918
Osorno,Chile,Los Lagos,3877949
Nueva Imperial,Chile,AraucanÃ­a,3878456
Nacimiento,Chile,BiobÃ­o,3879123
MulchÃ©n,Chile,BiobÃ­o,3879200
Molina,Chile,Maule,3879627
Melipilla,Chile,Santiago Metropolitan,3880107
MachalÃ­,Chile,O'Higgins,3881102
Lota,Chile,BiobÃ­o,3881276
Los Ãngeles,Chile,BiobÃ­o,3882428
Los Andes,Chile,ValparaÃ­so,3882434
Loncoche,Chile,AraucanÃ­a,3882582
Llaillay,Chile,ValparaÃ­so,3883035
Linares,Chile,Maule,3883167
Limache,Chile,ValparaÃ­so,3883214
Lebu,Chile,BiobÃ­o,3883457
Lautaro,Chile,AraucanÃ­a,3883615
La UniÃ³n,Chile,Los RÃ­os,3883629
La Serena,Chile,Coquimbo,3884373
Lampa,Chile,Santiago Metropolitan,3885273
La Ligua,Chile,ValparaÃ­so,3885456
La Laja,Chile,BiobÃ­o,3885509
Iquique,Chile,TarapacÃ¡,3887127
Illapel,Chile,Coquimbo,3887344
Hacienda La Calera,Chile,ValparaÃ­so,3888214
Graneros,Chile,O'Higgins,3888749
Frutillar,Chile,Los Lagos,3889263
El Monte,Chile,Santiago Metropolitan,3890949
Diego de Almagro,Chile,Atacama,3892454
CuricÃ³,Chile,Maule,3892870
Curanilahue,Chile,BiobÃ­o,3892892
Coronel,Chile,BiobÃ­o,3893532
Coquimbo,Chile,Coquimbo,3893629
CopiapÃ³,Chile,Atacama,3893656
ConstituciÃ³n,Chile,Maule,3893726
ConcepciÃ³n,Chile,BiobÃ­o,3893894
Collipulli,Chile,AraucanÃ­a,3894177
Coihaique,Chile,AisÃ©n,3894426
Chimbarongo,Chile,O'Higgins,3895061
ChillÃ¡n,Chile,BiobÃ­o,3895088
Chiguayante,Chile,BiobÃ­o,3895138
Chicureo Abajo,Chile,Santiago Metropolitan,3895165
Cauquenes,Chile,Maule,3896105
Castro,Chile,Los Lagos,3896218
Cartagena,Chile,ValparaÃ­so,3896433
CaÃ±ete,Chile,BiobÃ­o,3896924
Calama,Chile,Antofagasta,3897347
Cabrero,Chile,BiobÃ­o,3897557
Buin,Chile,Santiago Metropolitan,3897774
Arica,Chile,Arica y Parinacota,3899361
Arauco,Chile,BiobÃ­o,3899462
Antofagasta,Chile,Antofagasta,3899539
Angol,Chile,AraucanÃ­a,3899629
Ancud,Chile,Los Lagos,3899695
Las Animas,Chile,Los Lagos,6458708
La Pintana,Chile,Santiago Metropolitan,7281017
Lo Prado,Chile,Santiago Metropolitan,7281020
YaoundÃ©,Cameroon,Centre,2220957
Yagoua,Cameroon,Far North,2221030
Wum,Cameroon,North-West Province,2221053
Tonga,Cameroon,West,2221394
Tiko,Cameroon,South-West Province,2221504
Tibati,Cameroon,Adamaoua,2221530
TchollirÃ©,Cameroon,North Province,2221607
SangmÃ©lima,Cameroon,South Province,2222230
Penja,Cameroon,Littoral,2222623
Obala,Cameroon,Centre,2223293
Nkoteng,Cameroon,Centre,2223734
Nkongsamba,Cameroon,Littoral,2223763
NgaoundÃ©rÃ©,Cameroon,Adamaoua,2224827
Nanga Eboko,Cameroon,Centre,2225457
Muyuka,Cameroon,South-West Province,2225726
Mutengene,Cameroon,South-West Province,2225728
Mora,Cameroon,Far North,2225991
Mokolo,Cameroon,Far North,2226275
Melong,Cameroon,Littoral,2227230
MeÃ¯ganga,Cameroon,Adamaoua,2227402
Mbouda,Cameroon,West,2227613
Mbanga,Cameroon,Littoral,2228005
Mbandjok,Cameroon,Centre,2228028
Mbalmayo,Cameroon,Centre,2228079
Maroua,Cameroon,Far North,2228373
Manjo,Cameroon,Littoral,2228499
Mamfe,Cameroon,South-West Province,2228675
Loum,Cameroon,Littoral,2229152
Lolodorf,Cameroon,South Province,2229267
Limbe,Cameroon,South-West Province,2229411
Lagdo,Cameroon,North Province,2229681
Kumbo,Cameroon,North-West Province,2229748
Kumba,Cameroon,South-West Province,2229752
Kribi,Cameroon,South Province,2229761
KoussÃ©ri,Cameroon,Far North,2229798
KaÃ©lÃ©,Cameroon,Far North,2230599
Guider,Cameroon,North Province,2230876
Garoua BoulaÃ¯,Cameroon,East,2231319
Garoua,Cameroon,North Province,2231320
Fundong,Cameroon,North-West Province,2231482
Foumbot,Cameroon,West,2231504
Foumban,Cameroon,West,2231506
Fontem,Cameroon,South-West Province,2231564
EsÃ©ka,Cameroon,Centre,2231881
EdÃ©a,Cameroon,Littoral,2232239
Ã‰bolowa,Cameroon,South Province,2232283
Dschang,Cameroon,West,2232444
Douala,Cameroon,Littoral,2232593
DizanguÃ©,Cameroon,Littoral,2232997
Buea,Cameroon,South-West Province,2233410
Bogo,Cameroon,Far North,2233805
Bertoua,Cameroon,East,2234359
BÃ©labo,Cameroon,East,2234536
Batouri,Cameroon,East,2234663
Banyo,Cameroon,Adamaoua,2234794
BangangtÃ©,Cameroon,West,2234865
Bamusso,Cameroon,South-West Province,2234941
Bamenda,Cameroon,North-West Province,2234974
Bali,Cameroon,North-West Province,2235029
Bafoussam,Cameroon,West,2235189
Bafia,Cameroon,Centre,2235194
Bafang,Cameroon,West,2235196
Akonolinga,Cameroon,Centre,2235776
Idenao,Cameroon,South-West Province,2594800
Rikaze,China,Tibet Autonomous Region,1279715
Jiuquan,China,Gansu Sheng,1279945
Shache,China,Xinjiang Uygur Zizhiqu,1280037
Qamdo,China,Tibet Autonomous Region,1280281
Nagqu,China,Tibet Autonomous Region,1280517
Lhasa,China,Tibet Autonomous Region,1280737
Laojunmiao,China,Gansu Sheng,1280757
Kashgar,China,Xinjiang Uygur Zizhiqu,1280849
Jiayuguan,China,Gansu Sheng,1280957
Hotan,China,Xinjiang Uygur Zizhiqu,1281019
DÃªqÃªn,China,Tibet Autonomous Region,1281368
ÃœrÃ¼mqi,China,Xinjiang Uygur Zizhiqu,1529102
Laochenglu,China,Xinjiang Uygur Zizhiqu,1529114
Shihezi,China,Xinjiang Uygur Zizhiqu,1529195
Kuche,China,Xinjiang Uygur Zizhiqu,1529363
Sayibage,China,Xinjiang Uygur Zizhiqu,1529376
Hoxtolgay,China,Xinjiang Uygur Zizhiqu,1529452
Hami,China,Xinjiang Uygur Zizhiqu,1529484
Changji,China,Xinjiang Uygur Zizhiqu,1529569
Baijiantan,China,Xinjiang Uygur Zizhiqu,1529626
Aral,China,Xinjiang Uygur Zizhiqu,1529641
Altay,China,Xinjiang Uygur Zizhiqu,1529651
Yingbazha,China,Xinjiang Uygur Zizhiqu,1529660
Zunyi,China,Guizhou Sheng,1783621
Zoucheng,China,Shandong Sheng,1783633
Yanjiang,China,Sichuan,1783683
Zigong,China,Sichuan,1783745
Zhuzhou,China,Hunan,1783763
Zhumadian,China,Henan Sheng,1783873
Zhujiajiao,China,Shanghai Shi,1783920
Shangqiu,China,Henan Sheng,1783934
Zhuji,China,Zhejiang Sheng,1783940
Mizhou,China,Shandong Sheng,1783988
Zhuanghe,China,Liaoning,1784055
Zhouzhuang,China,Jiangsu,1784074
Zhoukou,China,Henan Sheng,1784130
Zhoucun,China,Shandong Sheng,1784178
Yuxi,China,Yunnan,1784185
Zhongxing,China,Jiangsu,1784253
Zhongshu,China,Yunnan,1784310
Zhicheng,China,Zhejiang Sheng,1784553
Zhicheng,China,Hubei,1784554
Zhenzhou,China,Jiangsu,1784580
Zhenjiang,China,Jiangsu,1784642
Zhaobaoshan,China,Zhejiang Sheng,1784647
Zhengzhou,China,Henan Sheng,1784658
Xinghua,China,Jiangsu,1784820
Zhaotong,China,Yunnan,1784841
Zhaoqing,China,Guangdong,1784853
Zhaogezhuang,China,Hebei,1784929
Luofeng,China,Shandong Sheng,1784953
Zhanjiang,China,Guangdong,1784990
Zhangzhou,China,Fujian,1785018
Zhangye,China,Gansu Sheng,1785036
Zibo,China,Shandong Sheng,1785286
Anyang,China,Henan Sheng,1785294
Zaozhuang,China,Shandong Sheng,1785453
Zaoyang,China,Hubei,1785462
Yuyao,China,Zhejiang Sheng,1785545
Yingchuan,China,Henan Sheng,1785566
Yuxia,China,Shaanxi,1785572
Kunshan,China,Jiangsu,1785623
Yunyang,China,Henan Sheng,1785655
Yunmeng Chengguanzhen,China,Hubei,1785698
Jinghong,China,Yunnan,1785710
Pizhou,China,Jiangsu,1785716
Yunfu,China,Guangdong,1785725
Yuncheng,China,Shanxi Sheng,1785738
Yulin,China,Shaanxi,1785777
Yulin,China,Guangxi Zhuangzu Zizhiqu,1785781
Yudong,China,Chongqing Shi,1785964
Yuci,China,Shanxi Sheng,1785974
Yucheng,China,Shandong Sheng,1785980
Yuanping,China,Shanxi Sheng,1786060
Qianjiang,China,Hubei,1786067
Heyuan,China,Guangdong,1786112
Yongfeng,China,Hunan,1786357
Yongchuan,China,Chongqing Shi,1786378
Yishui,China,Shandong Sheng,1786455
Zhongxiang,China,Hubei,1786546
Yingshang Chengguanzhen,China,Anhui Sheng,1786587
Chengzhong,China,Hubei,1786640
Yinchuan,China,Ningxia Huizu Zizhiqu,1786657
Yima,China,Henan Sheng,1786676
Yigou,China,Henan Sheng,1786720
Qingzhou,China,Shandong Sheng,1786731
Yichun,China,Jiangxi Sheng,1786746
Yicheng,China,Hubei,1786759
Yicheng,China,Jiangsu,1786760
Yichang,China,Hubei,1786764
Yibin,China,Sichuan,1786770
Yatou,China,Shandong Sheng,1786855
Yashan,China,Guangxi Zhuangzu Zizhiqu,1786867
Yanzhou,China,Shandong Sheng,1787031
Yantai,China,Shandong Sheng,1787093
Yanliang,China,Shaanxi,1787144
Yangzhou,China,Jiangsu,1787227
Yangshuo,China,Guangxi Zhuangzu Zizhiqu,1787323
Zhangjiagang,China,Jiangsu,1787331
Yangquan,China,Shanxi Sheng,1787351
Yangliuqing,China,Tianjin Shi,1787437
Yanggu,China,Shandong Sheng,1787601
Yangcun,China,Tianjin Shi,1787646
Yancheng,China,Jiangsu,1787746
Tongshan,China,Jiangsu,1787824
Xucheng,China,Guangdong,1787837
Shangrao,China,Jiangxi Sheng,1787858
Xunchang,China,Sichuan,1787901
Jiangguanchi,China,Henan Sheng,1788046
Xuanzhou,China,Anhui Sheng,1788081
Xixiang,China,Henan Sheng,1788206
Xiuying,China,Hainan,1788245
Xiulin,China,Hubei,1788268
Xiongzhou,China,Guangdong,1788402
Guixi,China,Jiangxi Sheng,1788406
Xinzhou,China,Shanxi Sheng,1788450
Xinzhou,China,Hubei,1788452
Xinzhi,China,Shanxi Sheng,1788462
Xinyu,China,Jiangxi Sheng,1788508
Hancheng,China,Henan Sheng,1788522
Xinyang,China,Henan Sheng,1788534
Nangandao,China,Henan Sheng,1788572
Xintai,China,Shandong Sheng,1788618
Xinshi,China,Hubei,1788638
Xinpu,China,Jiangsu,1788694
Xinji,China,Hebei,1788816
Xining,China,Qinghai Sheng,1788852
Shangmei,China,Hunan,1788869
Xingtai,China,Hebei,1788927
Ankang,China,Shaanxi,1789065
Xindian,China,Shandong Sheng,1789118
Xindi,China,Hubei,1789137
Feicheng,China,Shandong Sheng,1789176
Sanshui,China,Guangdong,1789273
Ximei,China,Fujian,1789289
Wacheng,China,Henan Sheng,1789427
Xihe,China,Hubei,1789462
Xichang,China,Sichuan,1789647
Xiazhuang,China,Shandong Sheng,1789693
Xiazhen,China,Shandong Sheng,1789703
Xiashi,China,Zhejiang Sheng,1789799
Zijinglu,China,Henan Sheng,1789897
Xiaoweizhai,China,Guizhou Sheng,1789945
Xiaoshan,China,Zhejiang Sheng,1789998
Xiaolingwei,China,Jiangsu,1790100
Xiaogan,China,Hubei,1790254
Xianyang,China,Shaanxi,1790353
Xiantao,China,Hubei,1790371
Xianshuigu,China,Tianjin Shi,1790379
XiannÃ¼,China,Jiangsu,1790392
Xianning,China,Hubei,1790396
Xianju,China,Zhejiang Sheng,1790413
Zhuhai,China,Guangdong,1790437
Wenxing,China,Hunan,1790451
Xiangxiang,China,Hunan,1790471
Xiangtan,China,Hunan,1790492
Xiangyang,China,Hubei,1790587
Xiangcheng Chengguanzhen,China,Henan Sheng,1790601
Xiâ€™an,China,Shaanxi,1790630
Xiamen,China,Fujian,1790645
Wuzhou,China,Guangxi Zhuangzu Zizhiqu,1790840
Wuyang,China,Anhui Sheng,1790885
Wuxue,China,Hubei,1790894
Wuxi,China,Jiangsu,1790923
Dongyang,China,Zhejiang Sheng,1791056
Changde,China,Hunan,1791121
Wuhu,China,Anhui Sheng,1791236
Wuhan,China,Hubei,1791247
Wuhai,China,Inner Mongolia,1791249
Wuda,China,Inner Mongolia,1791325
Wucheng,China,Anhui Sheng,1791347
Wenzhou,China,Zhejiang Sheng,1791388
Wenshang,China,Shandong Sheng,1791428
Wenling,China,Zhejiang Sheng,1791464
Tianfu,China,Shandong Sheng,1791536
Weinan,China,Shaanxi,1791636
Weihai,China,Shandong Sheng,1791673
Weifang,China,Shandong Sheng,1791681
Wanxian,China,Chongqing Shi,1791748
Wanning,China,Hainan,1791779
Yinzhu,China,Shandong Sheng,1792087
Wafangdian,China,Liaoning,1792260
Huangshan,China,Anhui Sheng,1792359
Loushanguan,China,Guizhou Sheng,1792516
Tongzhou,China,Beijing,1792520
Fuding,China,Fujian,1792585
Tongren,China,Guizhou Sheng,1792592
Wusong,China,Anhui Sheng,1792621
Tongchuan,China,Sichuan,1792692
Tianshui,China,Gansu Sheng,1792892
Tianpeng,China,Sichuan,1792916
Tianjin,China,Tianjin Shi,1792947
Tengzhou,China,Shandong Sheng,1793036
Taozhuang,China,Shandong Sheng,1793089
Tantou,China,Fujian,1793230
Tangzhai,China,Anhui Sheng,1793286
Tangshan,China,Hebei,1793346
Tangping,China,Guangdong,1793364
Tangjiazhuang,China,Hebei,1793385
Binhe,China,Henan Sheng,1793419
Tanggu,China,Tianjin Shi,1793424
Taizhou,China,Jiangsu,1793505
Taiyuan,China,Shanxi Sheng,1793511
Taixing,China,Jiangsu,1793533
Taishan,China,Guangdong,1793700
Taiâ€™an,China,Shandong Sheng,1793724
Suzhou,China,Anhui Sheng,1793743
Suozhen,China,Shandong Sheng,1793774
Suizhou,China,Hubei,1793879
Suixi,China,Anhui Sheng,1793889
Suicheng,China,Jiangsu,1793899
Suining,China,Sichuan,1793900
Songjiang,China,Shanghai Shi,1794035
Sishui,China,Shandong Sheng,1794140
Laixi,China,Shandong Sheng,1794479
Shouguang,China,Shandong Sheng,1794794
Shizuishan,China,Ningxia Huizu Zizhiqu,1794806
Shizilu,China,Shandong Sheng,1794825
Shiyan,China,Hubei,1794903
Shiyan,China,Hubei,1794904
Shiwan,China,Guangdong,1794947
Shitanjing,China,Ningxia Huizu Zizhiqu,1794971
Shiqiao,China,Guangdong,1795055
Shiqi,China,Guangdong,1795060
Shima,China,Fujian,1795166
Shilong,China,Guangdong,1795184
Tongchuan,China,Shaanxi,1795196
Shijiazhuang,China,Hebei,1795270
Shenzhen,China,Guangdong,1795565
Yanta,China,Shandong Sheng,1795579
Shenjiamen,China,Zhejiang Sheng,1795632
Shashi,China,Hubei,1795816
Shaping,China,Guangdong,1795842
Shaoxing,China,Zhejiang Sheng,1795855
Shaowu,China,Fujian,1795857
Shaoguan,China,Guangdong,1795874
Shancheng,China,Shandong Sheng,1795919
Shanwei,China,Guangdong,1795928
Shantou,China,Guangdong,1795940
Shanting,China,Shandong Sheng,1795941
Shanghai,China,Shanghai Shi,1796236
Shahecheng,China,Hebei,1796421
Sanya,China,Hainan,1796556
Sanming,China,Fujian,1796663
Runing,China,Henan Sheng,1797038
Fuqing,China,Fujian,1797120
Jieyang,China,Guangdong,1797121
Rizhao,China,Shandong Sheng,1797132
Renqiu,China,Hebei,1797181
Quzhou,China,Zhejiang Sheng,1797264
Qujing,China,Yunnan,1797318
Qufu,China,Shandong Sheng,1797333
Quanzhou,China,Fujian,1797353
Wuxi,China,Hunan,1797417
Zhuangyuan,China,Shandong Sheng,1797438
Qiongshan,China,Hainan,1797535
Qionghu,China,Hunan,1797543
Qinzhou,China,Guangxi Zhuangzu Zizhiqu,1797551
Qinnan,China,Jiangsu,1797575
Qinhuangdao,China,Hebei,1797595
Jinjiang,China,Fujian,1797658
Qingquan,China,Hubei,1797793
Huai'an,China,Jiangsu,1797873
Qingdao,China,Shandong Sheng,1797929
Qingyuan,China,Guangdong,1797945
Hongqiao,China,Hunan,1798082
Puyang Chengguanzhen,China,Henan Sheng,1798422
Puyang,China,Zhejiang Sheng,1798425
Putian,China,Fujian,1798449
Puqi,China,Hubei,1798473
Pumiao,China,Guangxi Zhuangzu Zizhiqu,1798480
Pulandian,China,Liaoning,1798490
Poyang,China,Jiangxi Sheng,1798548
Pingyin,China,Shandong Sheng,1798632
Pingyi,China,Shandong Sheng,1798634
Gutao,China,Shanxi Sheng,1798636
Pingxiang,China,Jiangxi Sheng,1798654
Pingshan,China,Guangdong,1798713
Pingnan,China,Guangxi Zhuangzu Zizhiqu,1798733
Pingliang,China,Gansu Sheng,1798760
Pingdu,China,Shandong Sheng,1798821
Pingdingshan,China,Henan Sheng,1798827
Pengcheng,China,Hebei,1798946
Dadukou,China,Sichuan,1798998
Ningyang,China,Shandong Sheng,1799348
Yutan,China,Hunan,1799352
Ninghai,China,Shandong Sheng,1799383
Ninghai,China,Zhejiang Sheng,1799384
Ningbo,China,Zhejiang Sheng,1799397
Neijiang,China,Sichuan,1799491
Nanzhou,China,Hunan,1799552
Nanzhang Chengguanzhen,China,Hubei,1799574
Nanyang,China,Henan Sheng,1799629
Nantong,China,Jiangsu,1799722
Pucheng,China,Fujian,1799832
Nanping,China,Fujian,1799846
Nanning,China,Guangxi Zhuangzu Zizhiqu,1799869
Nanma,China,Shandong Sheng,1799897
Nanlong,China,Sichuan,1799908
Nanjing,China,Jiangsu,1799962
Nangong,China,Hebei,1800065
Nanfeng,China,Guangdong,1800088
Nandu,China,Guangxi Zhuangzu Zizhiqu,1800101
Nanding,China,Shandong Sheng,1800107
Nanchong,China,Sichuan,1800146
Nanchang,China,Jiangxi Sheng,1800163
Miyang,China,Yunnan,1800430
Mingshui,China,Shandong Sheng,1800498
Mingguang,China,Anhui Sheng,1800519
Minggang,China,Henan Sheng,1800521
Mianyang,China,Sichuan,1800627
Mentougou,China,Beijing,1800657
Mengyin,China,Shandong Sheng,1800675
Mengcheng Chengguanzhen,China,Anhui Sheng,1800764
Meizhou,China,Guangdong,1800779
Wuchuan,China,Guangdong,1800829
Majie,China,Yunnan,1801401
Zhijiang,China,Hubei,1801455
Macheng,China,Hubei,1801582
Maba,China,Guangdong,1801615
LÃ¼shun,China,Liaoning,1801722
Luqiao,China,Zhejiang Sheng,1801757
Luoyang,China,Henan Sheng,1801792
Luoyang,China,Fujian,1801797
Luoyang,China,Guangdong,1801799
Luorong,China,Guangxi Zhuangzu Zizhiqu,1801850
Luohe,China,Henan Sheng,1801934
Luocheng,China,Sichuan,1801983
Lucheng,China,Anhui Sheng,1802068
Kangding,China,Sichuan,1802171
Lubu,China,Guangdong,1802177
Luancheng,China,Hebei,1802204
Loudi,China,Hunan,1802238
Longquan,China,Yunnan,1802476
Longgang,China,Shandong Sheng,1802550
Licheng,China,Jiangsu,1802788
Guankou,China,Hunan,1802875
Puning,China,Guangdong,1802940
Lishui,China,Zhejiang Sheng,1803245
Lintong,China,Shaanxi,1803266
Linyi,China,Shandong Sheng,1803318
Linxia Chengguanzhen,China,Gansu Sheng,1803331
Linxi,China,Hebei,1803334
Linshui,China,Hebei,1803352
Linqu,China,Shandong Sheng,1803364
Linqiong,China,Sichuan,1803365
Qingnian,China,Shandong Sheng,1803367
Linping,China,Zhejiang Sheng,1803374
Linhai,China,Zhejiang Sheng,1803422
Lingcheng,China,Guangxi Zhuangzu Zizhiqu,1803551
Lincheng,China,Hainan,1803560
Linfen,China,Shanxi Sheng,1803567
Xishan,China,Hunan,1803616
Lichuan,China,Hubei,1803782
Licheng,China,Guangdong,1803791
Liaocheng,China,Shandong Sheng,1803834
Lianzhou,China,Guangdong,1803841
Lianzhou,China,Guangxi Zhuangzu Zizhiqu,1803842
Lianran,China,Yunnan,1803886
Wuwei,China,Gansu Sheng,1803936
Liangxiang,China,Beijing,1803948
Lianjiang,China,Guangdong,1804120
Leshan,China,Sichuan,1804153
Lengshuitan,China,Hunan,1804162
Lengshuijiang,China,Hunan,1804169
Leiyang,China,Hunan,1804208
Lecheng,China,Guangdong,1804252
Laohekou,China,Hubei,1804386
Lanzhou,China,Gansu Sheng,1804430
Lanxi,China,Zhejiang Sheng,1804442
Lianyuan,China,Hunan,1804451
Langfang,China,Hebei,1804540
Weichanglu,China,Shandong Sheng,1804578
Laiyang,China,Shandong Sheng,1804586
Laiwu,China,Shandong Sheng,1804591
Laibin,China,Guangxi Zhuangzu Zizhiqu,1804609
Kunyang,China,Zhejiang Sheng,1804645
Kunming,China,Yunnan,1804651
Kaiyuan,China,Yunnan,1804850
Kaihua,China,Yunnan,1804874
Kaifeng,China,Henan Sheng,1804879
Juye,China,Shandong Sheng,1804892
Juegang,China,Jiangsu,1804979
Jiujiang,China,Jiangxi Sheng,1805179
Jishui,China,Henan Sheng,1805267
Qianzhou,China,Hunan,1805270
Jinzhou,China,Liaoning,1805298
Jinxiang,China,Zhejiang Sheng,1805334
Jinshi,China,Hunan,1805379
Jinsha,China,Jiangsu,1805408
Jinjiang,China,Hainan,1805505
Jinji,China,Guangxi Zhuangzu Zizhiqu,1805515
Jining,China,Shandong Sheng,1805518
Jinhua,China,Zhejiang Sheng,1805528
Jingzhou,China,Hubei,1805540
Tianchang,China,Hebei,1805563
Jingmen,China,Hubei,1805611
Jingling,China,Hubei,1805618
Jingdezhen,China,Jiangxi Sheng,1805680
Jinchang,China,Gansu Sheng,1805733
Jincheng,China,Shanxi Sheng,1805741
Jinan,China,Shandong Sheng,1805753
Jimo,China,Shandong Sheng,1805757
Jijiang,China,Chongqing Shi,1805798
Jiexiu,China,Shanxi Sheng,1805833
Jieshou,China,Anhui Sheng,1805844
Jieshi,China,Guangdong,1805857
Jiehu,China,Shandong Sheng,1805884
Jiazi,China,Guangdong,1805935
Jiaxing,China,Zhejiang Sheng,1805953
Jiaozuo,China,Henan Sheng,1805987
Jiaozhou,China,Shandong Sheng,1806096
Ningde,China,Fujian,1806097
Jianâ€™ou,China,Fujian,1806167
Jiangyan,China,Jiangsu,1806218
Jianguang,China,Jiangxi Sheng,1806248
Jiangmen,China,Guangdong,1806299
Jiangkou,China,Fujian,1806327
Yangjiang,China,Guangdong,1806408
Jiâ€™an,China,Jiangxi Sheng,1806445
Guangyuan,China,Sichuan,1806466
Huzhou,China,Zhejiang Sheng,1806535
Hutang,China,Jiangsu,1806591
Huoqiu Chengguanzhen,China,Anhui Sheng,1806651
Humen,China,Guangdong,1806696
Huizhou,China,Guangdong,1806776
Huilong,China,Jiangsu,1806840
Huicheng,China,Guangdong,1806881
Xinhui,China,Guangdong,1806882
Huazhou,China,Guangdong,1806960
Huangzhou,China,Hubei,1807112
Huangyan,China,Zhejiang Sheng,1807143
Huangshi,China,Hubei,1807234
Dasha,China,Guangdong,1807301
Huangpi,China,Hubei,1807308
Huangmei,China,Hubei,1807339
Huanggang,China,Guangdong,1807508
Daxing,China,Beijing,1807544
Dingcheng,China,Henan Sheng,1807553
Huaiyuan Chengguanzhen,China,Anhui Sheng,1807645
Huainan,China,Anhui Sheng,1807681
Huaicheng,China,Guangdong,1807687
Huaihua,China,Hunan,1807689
Huaidian,China,Henan Sheng,1807695
Huaibei,China,Anhui Sheng,1807700
Hongjiang,China,Hunan,1808106
Heze,China,Shandong Sheng,1808198
Hechuan,China,Chongqing Shi,1808212
Yiyang,China,Hunan,1808316
Hepo,China,Guangdong,1808336
Hengyang,China,Hunan,1808370
Hengshui,China,Hebei,1808392
Hefei,China,Anhui Sheng,1808722
Hede,China,Jiangsu,1808744
Hecun,China,Hebei,1808747
Hebi,China,Henan Sheng,1808770
Hanzhong,China,Shaanxi,1808857
Chengyang,China,Fujian,1808872
Hanting,China,Shandong Sheng,1808879
Hangzhou,China,Zhejiang Sheng,1808926
Hangu,China,Tianjin Shi,1808931
Handan,China,Hebei,1808963
Hanchuan,China,Hubei,1808977
Hancheng,China,Shaanxi,1808981
Haizhou,China,Jiangsu,1809003
Jiaojiang,China,Zhejiang Sheng,1809061
Haimen,China,Guangdong,1809062
Haikou,China,Yunnan,1809077
Haikou,China,Hainan,1809078
Guye,China,Hebei,1809159
Guozhen,China,Shaanxi,1809263
Guli,China,Zhejiang Sheng,1809412
Guiyang,China,Guizhou Sheng,1809461
Guiren,China,Jiangsu,1809483
Guiping,China,Guangxi Zhuangzu Zizhiqu,1809486
Guilin,China,Guangxi Zhuangzu Zizhiqu,1809498
Guigang,China,Guangxi Zhuangzu Zizhiqu,1809532
Gucheng Chengguanzhen,China,Hubei,1809610
Guangzhou,China,Guangdong,1809858
Guangshui,China,Hubei,1809879
Gejiu,China,Yunnan,1810240
Gaozhou,China,Guangdong,1810295
Gaoyou,China,Jiangsu,1810309
Gaoping,China,Sichuan,1810437
Gaomi,China,Shandong Sheng,1810458
Gaogou,China,Jiangsu,1810553
Fuzhou,China,Fujian,1810821
Fuyang,China,Anhui Sheng,1810845
Fuyang,China,Zhejiang Sheng,1810846
Qingyang,China,Shandong Sheng,1810920
Fuling,China,Chongqing Shi,1810979
Foshan,China,Guangdong,1811103
Fenyi,China,Jiangxi Sheng,1811114
Fengxian,China,Jiangsu,1811200
Fengrun,China,Hebei,1811260
Fengkou,China,Hubei,1811305
Feicheng,China,Shandong Sheng,1811440
Fangshan,China,Beijing,1811542
Ezhou,China,Hubei,1811619
Enshi,China,Hubei,1811720
Encheng,China,Guangdong,1811729
Duyun,China,Guizhou Sheng,1811764
Duobao,China,Hubei,1811829
Ducheng,China,Guangdong,1811929
Xinyi,China,Guangdong,1812057
Shengli,China,Shandong Sheng,1812101
Dongtai,China,Jiangsu,1812228
Dongsheng,China,Inner Mongolia,1812256
Dongkan,China,Jiangsu,1812427
Donghai,China,Guangdong,1812521
Dongguan,China,Guangdong,1812545
Dongdu,China,Shandong Sheng,1812597
Dongcun,China,Shandong Sheng,1812621
Dingzhou,China,Hebei,1812728
Dingtao,China,Shandong Sheng,1812754
Dezhou,China,Shandong Sheng,1812955
Deyang,China,Sichuan,1812961
Deqing,China,Zhejiang Sheng,1812981
Dengzhou,China,Shandong Sheng,1812988
Huazhou,China,Henan Sheng,1812990
Songyang,China,Henan Sheng,1813016
Dazhong,China,Jiangsu,1813088
Zhangjiajie,China,Hunan,1813171
Daye,China,Hubei,1813206
Lijiang,China,Yunnan,1813253
Dazhou,China,Sichuan,1813325
Dawukou,China,Ningxia Huizu Zizhiqu,1813344
Datong,China,Anhui Sheng,1813451
Fenghua,China,Zhejiang Sheng,1813658
Daokou,China,Henan Sheng,1813775
Danshui,China,Guangdong,1813812
Danjiangkou,China,Hubei,1813828
Gushu,China,Anhui Sheng,1813851
Xincheng,China,Henan Sheng,1813892
Daliang,China,Guangdong,1814082
Dalian,China,Liaoning,1814087
Dali,China,Yunnan,1814093
Chuzhou,China,Anhui Sheng,1814757
Yangchun,China,Guangdong,1814786
Yiwu,China,Zhejiang Sheng,1814870
Chongqing,China,Chongqing Shi,1814906
Chonglong,China,Sichuan,1814919
Chizhou,China,Anhui Sheng,1814934
Chenzhou,China,Hunan,1815059
Chengyang,China,Shandong Sheng,1815184
Jiangyin,China,Jiangsu,1815251
Chengdu,China,Sichuan,1815286
Chenghua,China,Guangdong,1815302
Chaozhou,China,Guangdong,1815395
Chaohu,China,Anhui Sheng,1815427
Changzhou,China,Jiangsu,1815456
Changzhi,China,Shanxi Sheng,1815463
Changsha,China,Hunan,1815577
Changqing,China,Shandong Sheng,1815585
Changli,China,Hebei,1815656
Changleng,China,Jiangxi Sheng,1815667
Caohe,China,Hubei,1816026
Weining,China,Guizhou Sheng,1816028
Cangzhou,China,Hebei,1816080
Caidian,China,Hubei,1816176
Buhe,China,Hubei,1816221
Bozhou,China,Anhui Sheng,1816234
Botou,China,Hebei,1816256
Boshan,China,Shandong Sheng,1816265
Baise City,China,Guangxi Zhuangzu Zizhiqu,1816269
Binzhou,China,Shandong Sheng,1816336
Luxu,China,Guangxi Zhuangzu Zizhiqu,1816338
Bijie,China,Guizhou Sheng,1816373
Bianzhuang,China,Shandong Sheng,1816406
Bengbu,China,Anhui Sheng,1816440
Beijing,China,Beijing,1816670
Beihai,China,Guangxi Zhuangzu Zizhiqu,1816705
Beidao,China,Gansu Sheng,1816751
Beidaihehaibin,China,Hebei,1816753
Beibei,China,Chongqing Shi,1816790
Baoying,China,Jiangsu,1816890
Langzhong,China,Sichuan,1816924
Baoding,China,Hebei,1816971
Baiyin,China,Gansu Sheng,1817240
Baihe,China,Guangxi Zhuangzu Zizhiqu,1817701
Shangyu,China,Zhejiang Sheng,1817720
Babu,China,Guangxi Zhuangzu Zizhiqu,1817858
Anxiang,China,Hunan,1817952
Anshun,China,Guizhou Sheng,1817968
Anqiu,China,Shandong Sheng,1817990
Anqing,China,Anhui Sheng,1817993
Mabai,China,Yunnan,1818004
Anlu,China,Hubei,1818016
Anjiang,China,Hunan,1818051
Anbu,China,Guangdong,1818116
Jiangyou,China,Sichuan,1885823
Suzhou,China,Jiangsu,1886760
Zhoushan,China,Zhejiang Sheng,1886762
Mudu,China,Jiangsu,1898359
Songling,China,Jiangsu,1898494
Zhongshan,China,Guangdong,1915223
Lianghu,China,Zhejiang Sheng,1919014
Zhoucheng,China,Shandong Sheng,1920772
Dalianwan,China,Liaoning,1921372
Yueyang,China,Hunan,1927639
Bojia,China,Hunan,1929434
Zhenlai,China,Jilin Sheng,2033128
Zhengjiatun,China,Jilin Sheng,2033135
Zhaozhou,China,Heilongjiang Sheng,2033147
Zhaoyuan,China,Heilongjiang Sheng,2033149
Zhaodong,China,Heilongjiang Sheng,2033168
Zhangjiakou,China,Hebei,2033196
Zalantun,China,Inner Mongolia,2033225
Yushu,China,Jilin Sheng,2033242
Youhao,China,Heilongjiang Sheng,2033301
Yingkou,China,Liaoning,2033370
Yilan,China,Heilongjiang Sheng,2033403
Yichun,China,Heilongjiang Sheng,2033413
Yebaishou,China,Liaoning,2033423
Yantongshan,China,Jilin Sheng,2033449
Yanji,China,Jilin Sheng,2033467
Yakeshi,China,Inner Mongolia,2033536
Zhangjiakou Shi Xuanhua Qu,China,Hebei,2033574
Xiuyan,China,Liaoning,2033602
Xinqing,China,Heilongjiang Sheng,2033667
Xinmin,China,Liaoning,2033675
Xinglongshan,China,Jilin Sheng,2033739
Xingcheng,China,Liaoning,2033766
Xilin Hot,China,Inner Mongolia,2033824
Xifeng,China,Liaoning,2033866
Xiaoshi,China,Liaoning,2033934
Wuchang,China,Heilongjiang Sheng,2034141
Wangqing,China,Jilin Sheng,2034221
Hepingjie,China,Jilin Sheng,2034226
Wangkui,China,Heilongjiang Sheng,2034228
Ulanhot,China,Inner Mongolia,2034312
Tumen,China,Jilin Sheng,2034340
Tongliao,China,Inner Mongolia,2034400
Tieling,China,Liaoning,2034439
Tieli,China,Heilongjiang Sheng,2034440
Guangming,China,Jilin Sheng,2034497
Tailai,China,Heilongjiang Sheng,2034599
Taikang,China,Heilongjiang Sheng,2034600
Tahe,China,Heilongjiang Sheng,2034615
Sujiatun,China,Liaoning,2034638
Suileng,China,Heilongjiang Sheng,2034651
Suihua,China,Heilongjiang Sheng,2034655
Suifenhe,China,Heilongjiang Sheng,2034657
Songjianghe,China,Jilin Sheng,2034691
Siping,China,Jilin Sheng,2034714
Shunyi,China,Beijing,2034754
Shulan,China,Jilin Sheng,2034761
Shuangyashan,China,Heilongjiang Sheng,2034786
Shuangyang,China,Jilin Sheng,2034791
Shuangcheng,China,Heilongjiang Sheng,2034834
Shiguai,China,Inner Mongolia,2034918
Shenyang,China,Liaoning,2034937
Shanhetun,China,Heilongjiang Sheng,2034995
Shanhaiguan,China,Hebei,2034996
Shangzhi,China,Heilongjiang Sheng,2035002
Sanchazi,China,Jilin Sheng,2035182
Salaqi,China,Inner Mongolia,2035196
Fendou,China,Heilongjiang Sheng,2035225
Taihe,China,Heilongjiang Sheng,2035261
Qiqihar,China,Heilongjiang Sheng,2035265
Qinggang,China,Heilongjiang Sheng,2035325
Qianguo,China,Jilin Sheng,2035399
Pingzhuang,China,Inner Mongolia,2035453
Panshi,China,Jilin Sheng,2035511
Panshan,China,Liaoning,2035513
Nianzishan,China,Heilongjiang Sheng,2035593
Nenjiang,China,Heilongjiang Sheng,2035601
Nehe,China,Heilongjiang Sheng,2035610
Nantai,China,Liaoning,2035635
Nanpiao,China,Liaoning,2035644
Lianhe,China,Heilongjiang Sheng,2035669
Mujiayingzi,China,Inner Mongolia,2035707
Mudanjiang,China,Heilongjiang Sheng,2035715
Mishan,China,Heilongjiang Sheng,2035746
Mingyue,China,Jilin Sheng,2035754
Mingshui,China,Heilongjiang Sheng,2035758
Meihekou,China,Jilin Sheng,2035801
Manzhouli,China,Inner Mongolia,2035836
Longjing,China,Jilin Sheng,2035966
Longjiang,China,Heilongjiang Sheng,2035970
Longfeng,China,Heilongjiang Sheng,2035980
Liuhe,China,Jilin Sheng,2036033
Lishu,China,Jilin Sheng,2036055
Linkou,China,Heilongjiang Sheng,2036066
Linjiang,China,Jilin Sheng,2036069
Lingyuan,China,Liaoning,2036075
Lingdong,China,Heilongjiang Sheng,2036081
Liaozhong,China,Liaoning,2036106
Liaoyuan,China,Jilin Sheng,2036109
Liaoyang,China,Liaoning,2036113
Lanxi,China,Heilongjiang Sheng,2036226
Langxiang,China,Heilongjiang Sheng,2036237
Langtou,China,Liaoning,2036241
Kuandian,China,Liaoning,2036283
Kaiyuan,China,Liaoning,2036337
Kaitong,China,Jilin Sheng,2036338
Jixi,China,Heilongjiang Sheng,2036389
Jiutai,China,Jilin Sheng,2036401
Jiupu,China,Liaoning,2036403
Jishu,China,Jilin Sheng,2036418
Jinzhou,China,Liaoning,2036427
Lianshan,China,Liaoning,2036434
Jining,China,Inner Mongolia,2036458
Jilin,China,Jilin Sheng,2036502
Jidong,China,Heilongjiang Sheng,2036519
Minzhu,China,Jilin Sheng,2036536
Jiamusi,China,Heilongjiang Sheng,2036581
Jalai Nur,China,Inner Mongolia,2036595
Jagdaqi,China,Inner Mongolia,2036597
Hushitai,China,Liaoning,2036619
Hunchun,China,Jilin Sheng,2036653
Hulan Ergi,China,Heilongjiang Sheng,2036670
Hulan,China,Heilongjiang Sheng,2036671
Huinan,China,Jilin Sheng,2036685
Huanren,China,Liaoning,2036713
Huangnihe,China,Jilin Sheng,2036734
Huanan,China,Heilongjiang Sheng,2036753
Huadian,China,Jilin Sheng,2036776
Honggang,China,Heilongjiang Sheng,2036876
Hohhot,China,Inner Mongolia,2036892
Fendou,China,Heilongjiang Sheng,2036920
Helong,China,Jilin Sheng,2036933
Heishan,China,Liaoning,2036959
Heihe,China,Heilongjiang Sheng,2036973
Hegang,China,Heilongjiang Sheng,2036986
Harbin,China,Heilongjiang Sheng,2037013
Hailun,China,Heilongjiang Sheng,2037069
Hailin,China,Heilongjiang Sheng,2037075
Hailar,China,Inner Mongolia,2037078
Haicheng,China,Liaoning,2037086
Gongzhuling,China,Jilin Sheng,2037222
Gongchangling,China,Liaoning,2037240
Genhe,China,Inner Mongolia,2037252
Gannan,China,Heilongjiang Sheng,2037311
Fuyuan,China,Heilongjiang Sheng,2037330
Fuyu,China,Heilongjiang Sheng,2037334
Fuyu,China,Jilin Sheng,2037335
Fuxin,China,Liaoning,2037345
Fuxin,China,Liaoning,2037346
Fushun,China,Liaoning,2037355
Fuli,China,Heilongjiang Sheng,2037370
Fujin,China,Heilongjiang Sheng,2037375
Beichengqu,China,Inner Mongolia,2037391
Fengxiang,China,Heilongjiang Sheng,2037393
Fengcheng,China,Liaoning,2037411
Erenhot,China,Inner Mongolia,2037485
Erdaojiang,China,Jilin Sheng,2037494
Dunhua,China,Jilin Sheng,2037534
Dongning,China,Heilongjiang Sheng,2037611
Dongling,China,Liaoning,2037620
Dongfeng,China,Jilin Sheng,2037658
Dongxing,China,Heilongjiang Sheng,2037685
Dehui,China,Jilin Sheng,2037712
Datong,China,Shanxi Sheng,2037799
Dashitou,China,Jilin Sheng,2037820
Dashiqiao,China,Liaoning,2037823
Daqing,China,Heilongjiang Sheng,2037860
Dandong,China,Liaoning,2037886
Linghai,China,Liaoning,2037913
Dalai,China,Jilin Sheng,2037930
Chifeng,China,Inner Mongolia,2038067
Chengzihe,China,Heilongjiang Sheng,2038080
Chengde,China,Hebei,2038087
Chaoyang,China,Jilin Sheng,2038118
Chaoyang,China,Liaoning,2038120
Changtu,China,Liaoning,2038139
Changping,China,Beijing,2038154
Changling,China,Jilin Sheng,2038158
Changchun,China,Jilin Sheng,2038180
Chaihe,China,Heilongjiang Sheng,2038198
Boli,China,Heilongjiang Sheng,2038274
Binzhou,China,Heilongjiang Sheng,2038283
Benxi,China,Liaoning,2038300
Beipiao,China,Liaoning,2038342
Beiâ€™an,China,Heilongjiang Sheng,2038365
Bayan,China,Heilongjiang Sheng,2038421
Baotou,China,Inner Mongolia,2038432
Baoshan,China,Heilongjiang Sheng,2038438
Baoqing,China,Heilongjiang Sheng,2038446
Bamiantong,China,Heilongjiang Sheng,2038482
Baishishan,China,Jilin Sheng,2038529
Baiquan,China,Heilongjiang Sheng,2038541
Baicheng,China,Jilin Sheng,2038569
Baishan,China,Jilin Sheng,2038584
Anshan,China,Liaoning,2038632
Anda,China,Heilongjiang Sheng,2038650
Oroqen Zizhiqi,China,Inner Mongolia,2038665
Acheng,China,Heilongjiang Sheng,2038679
Songling,China,Hebei,2047837
Shilin,China,Yunnan,6825277
Changshu City,China,Jiangsu,7283386
Shixing,China,Guangdong,7290013
Jiashan,China,Zhejiang Sheng,7303248
Fenghuang,China,Hunan,7304020
Zhu Cheng City,China,Shandong Sheng,7602670
Shangri-La,China,Yunnan,7910932
Ordos,China,Inner Mongolia,8347664
Wenshan City,China,Yunnan,8505006
Liupanshui,China,Guizhou Sheng,8533133
ZipaquirÃ¡,Colombia,Cundinamarca,3665542
Zarzal,Colombia,Valle del Cauca,3665559
Zaragoza,Colombia,Antioquia,3665566
Yumbo,Colombia,Valle del Cauca,3665657
Yopal,Colombia,Casanare,3665688
Yarumal,Colombia,Antioquia,3665741
Viterbo,Colombia,Caldas,3665851
Villeta,Colombia,Cundinamarca,3665895
Villavicencio,Colombia,Meta,3665900
Villa del Rosario,Colombia,Norte de Santander,3665913
Villanueva,Colombia,La Guajira,3665934
Villanueva,Colombia,Casanare,3665951
VillamarÃ­a,Colombia,Caldas,3665973
Valledupar,Colombia,Cesar,3666304
Urrao,Colombia,Antioquia,3666395
UbatÃ©,Colombia,Cundinamarca,3666519
Turbo,Colombia,Antioquia,3666570
Turbaco,Colombia,BolÃ­var,3666577
TÃºquerres,Colombia,NariÃ±o,3666582
Tunja,Colombia,BoyacÃ¡,3666608
Tumaco,Colombia,NariÃ±o,3666640
TuluÃ¡,Colombia,Valle del Cauca,3666645
TolÃº,Colombia,Sucre,3666939
Tierralta,Colombia,CÃ³rdoba,3667158
Tame,Colombia,Arauca,3667478
Sucre,Colombia,Sucre,3667728
SonsÃ³n,Colombia,Antioquia,3667820
Soledad,Colombia,AtlÃ¡ntico,3667849
Sogamoso,Colombia,BoyacÃ¡,3667873
Socorro,Colombia,Santander,3667887
Soacha,Colombia,Cundinamarca,3667905
Sincelejo,Colombia,Sucre,3667983
SincÃ©,Colombia,Sucre,3667991
SibatÃ©,Colombia,Cundinamarca,3668087
Sevilla,Colombia,Valle del Cauca,3668132
Segovia,Colombia,Antioquia,3668175
Santuario,Colombia,Antioquia,3668323
Santo TomÃ¡s,Colombia,AtlÃ¡ntico,3668332
Santa Rosa de Cabal,Colombia,Risaralda,3668454
Santander de Quilichao,Colombia,Cauca,3668572
Santa Marta,Colombia,Magdalena,3668605
Santa LucÃ­a,Colombia,AtlÃ¡ntico,3668655
San Onofre,Colombia,Sucre,3669218
San MartÃ­n,Colombia,Meta,3669332
San Marcos,Colombia,Sucre,3669346
San Juan Nepomuceno,Colombia,BolÃ­var,3669454
San Juan del Cesar,Colombia,La Guajira,3669469
San Jacinto,Colombia,BolÃ­var,3669736
San Gil,Colombia,Santander,3669808
San Carlos,Colombia,CÃ³rdoba,3669997
San Carlos,Colombia,Antioquia,3669998
San Benito Abad,Colombia,Sucre,3670038
San AndrÃ©s,Colombia,"ArchipiÃ©lago de San AndrÃ©s, Providencia y Santa Catalina",3670218
SampuÃ©s,Colombia,Sucre,3670280
Salamina,Colombia,Caldas,3670370
SahagÃºn,Colombia,CÃ³rdoba,3670419
Sabaneta,Colombia,Antioquia,3670475
Sabanalarga,Colombia,AtlÃ¡ntico,3670502
Sabanagrande,Colombia,AtlÃ¡ntico,3670513
Roldanillo,Colombia,Valle del Cauca,3670644
Riosucio,Colombia,Caldas,3670719
Rionegro,Colombia,Antioquia,3670730
RÃ­ohacha,Colombia,La Guajira,3670745
RepelÃ³n,Colombia,AtlÃ¡ntico,3670874
Quimbaya,Colombia,QuindÃ­o,3671098
QuibdÃ³,Colombia,ChocÃ³,3671116
Puerto Tejada,Colombia,Cauca,3671315
Puerto Santander,Colombia,Norte de Santander,3671325
Puerto LÃ³pez,Colombia,Meta,3671418
Puerto Colombia,Colombia,AtlÃ¡ntico,3671497
Puerto BoyacÃ¡,Colombia,BoyacÃ¡,3671531
Puerto BerrÃ­o,Colombia,Antioquia,3671540
Puerto AsÃ­s,Colombia,Putumayo,3671549
Pradera,Colombia,Valle del Cauca,3671772
PopayÃ¡n,Colombia,Cauca,3671916
Planeta Rica,Colombia,CÃ³rdoba,3672068
Pivijay,Colombia,Magdalena,3672093
Pitalito,Colombia,Huila,3672110
Piedecuesta,Colombia,Santander,3672328
Pereira,Colombia,Risaralda,3672486
PatÃ­a,Colombia,Cauca,3672761
Pasto,Colombia,NariÃ±o,3672778
Pamplona,Colombia,Norte de Santander,3673045
Palmira,Colombia,Valle del Cauca,3673164
Palmar de Varela,Colombia,AtlÃ¡ntico,3673220
Belalcazar,Colombia,Cauca,3673398
Pacho,Colombia,Cundinamarca,3673424
OcaÃ±a,Colombia,Norte de Santander,3673662
Neiva,Colombia,Huila,3673899
Mosquera,Colombia,Cundinamarca,3674292
Morales,Colombia,BolÃ­var,3674412
MonterÃ­a,Colombia,CÃ³rdoba,3674453
Montenegro,Colombia,QuindÃ­o,3674463
MontelÃ­bano,Colombia,CÃ³rdoba,3674470
MompÃ³s,Colombia,BolÃ­var,3674597
Mocoa,Colombia,Putumayo,3674654
Melgar,Colombia,Tolima,3674885
MedellÃ­n,Colombia,Antioquia,3674962
Mariquita,Colombia,Tolima,3675252
Marinilla,Colombia,Antioquia,3675263
MarÃ­a la Baja,Colombia,BolÃ­var,3675287
Manzanares,Colombia,Caldas,3675409
Manizales,Colombia,Caldas,3675443
Malambo,Colombia,AtlÃ¡ntico,3675595
MÃ¡laga,Colombia,Santander,3675605
Maicao,Colombia,La Guajira,3675657
MaganguÃ©,Colombia,BolÃ­var,3675692
Madrid,Colombia,Cundinamarca,3675707
Los Patios,Colombia,Norte de Santander,3675975
Lorica,Colombia,CÃ³rdoba,3676397
LÃ­bano,Colombia,Tolima,3676604
Leticia,Colombia,Amazonas,3676623
LÃ©rida,Colombia,Tolima,3676626
La Virginia,Colombia,Risaralda,3676720
La UniÃ³n,Colombia,Valle del Cauca,3676928
La UniÃ³n,Colombia,NariÃ±o,3676934
La Tebaida,Colombia,QuindÃ­o,3677010
La Plata,Colombia,Huila,3678097
La Mesa,Colombia,Cundinamarca,3678405
La Jagua de Ibirico,Colombia,Cesar,3678674
La Estrella,Colombia,Antioquia,3679065
La Dorada,Colombia,Caldas,3679277
La Ceja,Colombia,Antioquia,3679554
JamundÃ­,Colombia,Valle del Cauca,3680387
ItagÃ¼Ã­,Colombia,Antioquia,3680450
Ipiales,Colombia,NariÃ±o,3680539
IbaguÃ©,Colombia,Tolima,3680656
Honda,Colombia,Tolima,3680840
GuacarÃ­,Colombia,Valle del Cauca,3681797
Granada,Colombia,Meta,3681957
GirÃ³n,Colombia,Santander,3682018
Girardot City,Colombia,Cundinamarca,3682028
GarzÃ³n,Colombia,Huila,3682108
Galapa,Colombia,AtlÃ¡ntico,3682238
Fusagasuga,Colombia,Cundinamarca,3682274
Funza,Colombia,Cundinamarca,3682281
FundaciÃ³n,Colombia,Magdalena,3682292
Fresno,Colombia,Tolima,3682330
Fonseca,Colombia,La Guajira,3682374
Floridablanca,Colombia,Santander,3682385
Florida,Colombia,Valle del Cauca,3682393
Florencia,Colombia,CaquetÃ¡,3682426
Flandes,Colombia,Tolima,3682458
FacatativÃ¡,Colombia,Cundinamarca,3682516
Espinal,Colombia,Tolima,3682573
Envigado,Colombia,Antioquia,3682631
El RetÃ©n,Colombia,Magdalena,3683233
El Copey,Colombia,Cesar,3684452
El Charco,Colombia,NariÃ±o,3684579
El Cerrito,Colombia,Valle del Cauca,3684615
El Carmen de BolÃ­var,Colombia,BolÃ­var,3684666
El Banco,Colombia,Magdalena,3684917
El Bagre,Colombia,Antioquia,3684945
Duitama,Colombia,BoyacÃ¡,3685084
Dos Quebradas,Colombia,Risaralda,3685095
CurumanÃ­,Colombia,Cesar,3685335
CÃºcuta,Colombia,Norte de Santander,3685533
Corozal,Colombia,Sucre,3685823
Corinto,Colombia,Cauca,3685871
Municipio de Copacabana,Colombia,Antioquia,3685949
Circasia,Colombia,QuindÃ­o,3686233
CiÃ©naga de Oro,Colombia,CÃ³rdoba,3686272
CiÃ©naga,Colombia,Magdalena,3686279
ChiriguanÃ¡,Colombia,Cesar,3686479
ChiquinquirÃ¡,Colombia,BoyacÃ¡,3686513
ChinÃº,Colombia,CÃ³rdoba,3686540
ChinchinÃ¡,Colombia,Caldas,3686561
Chimichagua,Colombia,Cesar,3686585
ChigorodÃ³,Colombia,Antioquia,3686636
ChÃ­a,Colombia,Cundinamarca,3686675
Chaparral,Colombia,Tolima,3686793
CeretÃ©,Colombia,CÃ³rdoba,3686922
Caucasia,Colombia,Antioquia,3687025
Cartago,Colombia,Valle del Cauca,3687230
Cartagena,Colombia,BolÃ­var,3687238
Carmen de Viboral,Colombia,Antioquia,3687318
Candelaria,Colombia,Valle del Cauca,3687644
Campo de la Cruz,Colombia,AtlÃ¡ntico,3687758
Campoalegre,Colombia,Huila,3687806
Cali,Colombia,Valle del Cauca,3687925
Caldas,Colombia,Antioquia,3687952
CalarcÃ¡,Colombia,QuindÃ­o,3687964
CajicÃ¡,Colombia,Cundinamarca,3688006
Caicedonia,Colombia,Valle del Cauca,3688071
Buga,Colombia,Valle del Cauca,3688256
Buenaventura,Colombia,Valle del Cauca,3688451
Buenaventura,Colombia,Valle del Cauca,3688452
Bucaramanga,Colombia,Santander,3688465
BogotÃ¡,Colombia,Bogota D.C.,3688689
Bello,Colombia,Antioquia,3688928
BelÃ©n de UmbrÃ­a,Colombia,Risaralda,3688989
Barranquilla,Colombia,AtlÃ¡ntico,3689147
Barrancas,Colombia,La Guajira,3689162
Barrancabermeja,Colombia,Santander,3689169
Barbosa,Colombia,Antioquia,3689205
Barbosa,Colombia,Santander,3689206
Baranoa,Colombia,AtlÃ¡ntico,3689235
Ayapel,Colombia,CÃ³rdoba,3689381
Armenia,Colombia,QuindÃ­o,3689560
Arjona,Colombia,BolÃ­var,3689570
AriguanÃ­,Colombia,Cesar,3689589
Arauca,Colombia,Arauca,3689718
Aracataca,Colombia,Magdalena,3689759
ApartadÃ³,Colombia,Antioquia,3689798
Anserma,Colombia,Risaralda,3689833
Andes,Colombia,Antioquia,3689899
AndalucÃ­a,Colombia,Valle del Cauca,3689905
Aguazul,Colombia,Casanare,3690316
Aguadas,Colombia,Caldas,3690431
Aguachica,Colombia,Cesar,3690465
AcacÃ­as,Colombia,Meta,3690577
Morales,Colombia,Cauca,3770718
Carepa,Colombia,Antioquia,3792375
Ciudad BolÃ­var,Colombia,Antioquia,3792376
AgustÃ­n Codazzi,Colombia,Cesar,3792383
Plato,Colombia,Magdalena,3792392
San JosÃ© del Guaviare,Colombia,Guaviare,3828545
Turrialba,Costa Rica,Cartago,3621184
Tejar,Costa Rica,San JosÃ©,3621335
Siquirres,Costa Rica,LimÃ³n,3621440
San Vicente,Costa Rica,San JosÃ©,3621505
San Rafael Arriba,Costa Rica,San JosÃ©,3621655
San Rafael Abajo,Costa Rica,San JosÃ©,3621659
San Rafael,Costa Rica,Alajuela,3621687
San Rafael,Costa Rica,San JosÃ©,3621689
San Pedro,Costa Rica,San JosÃ©,3621717
San Pablo,Costa Rica,Heredia,3621729
San Miguel,Costa Rica,San JosÃ©,3621753
San Juan de Dios,Costa Rica,San JosÃ©,3621804
San Juan,Costa Rica,San JosÃ©,3621819
San JosÃ©,Costa Rica,Alajuela,3621841
San JosÃ©,Costa Rica,San JosÃ©,3621849
San Isidro,Costa Rica,San JosÃ©,3621889
San Francisco,Costa Rica,Heredia,3621911
San Felipe,Costa Rica,San JosÃ©,3621922
San Diego,Costa Rica,Cartago,3621926
Quesada,Costa Rica,Alajuela,3622190
Purral,Costa Rica,San JosÃ©,3622217
Puntarenas,Costa Rica,Puntarenas,3622228
LimÃ³n,Costa Rica,LimÃ³n,3622247
PatarrÃ¡,Costa Rica,San JosÃ©,3622507
ParaÃ­so,Costa Rica,Cartago,3622547
Nicoya,Costa Rica,Guanacaste,3622716
Mercedes,Costa Rica,Heredia,3622881
Liberia,Costa Rica,Guanacaste,3623076
IpÃ­s,Costa Rica,San JosÃ©,3623394
Heredia,Costa Rica,Heredia,3623486
GuÃ¡piles,Costa Rica,LimÃ³n,3623580
Guadalupe,Costa Rica,San JosÃ©,3623593
Esparza,Costa Rica,Puntarenas,3623781
Curridabat,Costa Rica,San JosÃ©,3623977
Colima,Costa Rica,San JosÃ©,3624174
Chacarita,Costa Rica,Puntarenas,3624288
Cartago,Costa Rica,Cartago,3624370
CaÃ±as,Costa Rica,Guanacaste,3624468
Calle Blancos,Costa Rica,San JosÃ©,3624509
AserrÃ­,Costa Rica,San JosÃ©,3624848
Alajuela,Costa Rica,Alajuela,3624955
San Vicente de Moravia,Costa Rica,San JosÃ©,6612154
Yara,Cuba,Granma,3533753
Yaguajay,Cuba,Sancti SpÃ­ritus,3533826
ViÃ±ales,Cuba,Pinar del RÃ­o,3534094
Vertientes,Cuba,CamagÃ¼ey,3534363
Venezuela,Cuba,Ciego de Ãvila,3534432
Varadero,Cuba,Matanzas,3534632
San GermÃ¡n,Cuba,HolguÃ­n,3534749
UniÃ³n de Reyes,Cuba,Matanzas,3534761
Trinidad,Cuba,Sancti SpÃ­ritus,3534915
SibanicÃº,Cuba,CamagÃ¼ey,3536259
Santo Domingo,Cuba,Villa Clara,3536640
Santiago de las Vegas,Cuba,La Habana,3536724
Santiago de Cuba,Cuba,Santiago de Cuba,3536729
Santa Cruz del Sur,Cuba,CamagÃ¼ey,3537840
Santa Cruz del Norte,Cuba,Mayabeque,3537845
Santa Clara,Cuba,Villa Clara,3537906
San Miguel del PadrÃ³n,Cuba,La Habana,3538803
San Luis,Cuba,Santiago de Cuba,3539093
San JosÃ© de las Lajas,Cuba,Mayabeque,3539560
Sancti SpÃ­ritus,Cuba,Sancti SpÃ­ritus,3540667
San Cristobal,Cuba,Artemisa,3540680
San Antonio de los BaÃ±os,Cuba,Artemisa,3540885
Sagua la Grande,Cuba,Villa Clara,3541440
Sagua de TÃ¡namo,Cuba,HolguÃ­n,3541446
Rodas,Cuba,Cienfuegos,3541999
RÃ­o Guayabal de Yateras,Cuba,GuantÃ¡namo,3542137
RÃ­o Cauto,Cuba,Granma,3542167
Remedios,Cuba,Villa Clara,3542455
Regla,Cuba,La Habana,3542502
Ranchuelo,Cuba,Villa Clara,3542744
Puerto Padre,Cuba,Las Tunas,3543299
Primero de Enero,Cuba,Ciego de Ãvila,3543498
Placetas,Cuba,Villa Clara,3543961
Pinar del RÃ­o,Cuba,Pinar del RÃ­o,3544091
Perico,Cuba,Matanzas,3544393
Pedro Betancourt,Cuba,Matanzas,3544607
Palmira,Cuba,Cienfuegos,3545040
Palma Soriano,Cuba,Santiago de Cuba,3545064
Nuevitas,Cuba,CamagÃ¼ey,3545841
Nueva Gerona,Cuba,Isla de la Juventud,3545867
Niquero,Cuba,Granma,3545981
MorÃ³n,Cuba,Ciego de Ãvila,3546434
Moa,Cuba,HolguÃ­n,3546791
Minas de Matahambre,Cuba,Pinar del RÃ­o,3546882
Minas,Cuba,CamagÃ¼ey,3546894
Media Luna,Cuba,Granma,3547260
Matanzas,Cuba,Matanzas,3547398
Mariel,Cuba,Artemisa,3547600
Manzanillo,Cuba,Granma,3547867
Manicaragua,Cuba,Villa Clara,3547976
MaisÃ­,Cuba,GuantÃ¡namo,3548441
Madruga,Cuba,Mayabeque,3548529
Los Palacios,Cuba,Pinar del RÃ­o,3548993
Las Tunas,Cuba,Las Tunas,3550598
La Sierpe,Cuba,Sancti SpÃ­ritus,3551184
La Salud,Cuba,Mayabeque,3551608
Havana,Cuba,La Habana,3553478
Jovellanos,Cuba,Matanzas,3555907
Jobabo,Cuba,HolguÃ­n,3556077
Jobabo,Cuba,Las Tunas,3556078
JiguanÃ­,Cuba,Granma,3556168
JesÃºs MenÃ©ndez,Cuba,Las Tunas,3556268
Jatibonico,Cuba,Sancti SpÃ­ritus,3556334
Jaruco,Cuba,Mayabeque,3556351
JagÃ¼ey Grande,Cuba,Matanzas,3556437
HolguÃ­n,Cuba,HolguÃ­n,3556969
Guisa,Cuba,Granma,3557332
GÃ¼ira de Melena,Cuba,Artemisa,3557347
GÃ¼ines,Cuba,Mayabeque,3557378
GuantÃ¡namo,Cuba,GuantÃ¡namo,3557689
Guane,Cuba,Pinar del RÃ­o,3557758
Guanajay,Cuba,Artemisa,3557801
Guanabacoa,Cuba,La Habana,3557846
GuÃ¡imaro,Cuba,CamagÃ¼ey,3557923
Gibara,Cuba,HolguÃ­n,3558315
Fomento,Cuba,Sancti SpÃ­ritus,3558744
Florida,Cuba,CamagÃ¼ey,3558771
Florencia,Cuba,Ciego de Ãvila,3558792
Esmeralda,Cuba,CamagÃ¼ey,3559318
Encrucijada,Cuba,Villa Clara,3559416
Cumanayagua,Cuba,Cienfuegos,3562827
Cueto,Cuba,HolguÃ­n,3562895
Cruces,Cuba,Cienfuegos,3563145
Corralillo,Cuba,Villa Clara,3563317
Contramaestre,Cuba,Santiago de Cuba,3563504
ConsolaciÃ³n del Sur,Cuba,Pinar del RÃ­o,3563559
Condado,Cuba,Sancti SpÃ­ritus,3563609
ColÃ³n,Cuba,Matanzas,3563843
Colombia,Cuba,Las Tunas,3563856
Ciro Redondo,Cuba,Ciego de Ãvila,3564084
Cifuentes,Cuba,Villa Clara,3564114
Cienfuegos,Cuba,Cienfuegos,3564124
Ciego de Ãvila,Cuba,Ciego de Ãvila,3564178
Chambas,Cuba,Ciego de Ãvila,3564394
Cerro,Cuba,La Habana,3564436
Cauto Cristo,Cuba,Granma,3564885
CÃ¡rdenas,Cuba,Matanzas,3565432
Campechuela,Cuba,Granma,3565951
CamajuanÃ­,Cuba,Villa Clara,3566054
CamagÃ¼ey,Cuba,CamagÃ¼ey,3566067
Calimete,Cuba,Matanzas,3566134
CaibariÃ©n,Cuba,Villa Clara,3566356
Cacocum,Cuba,HolguÃ­n,3566429
CabaiguÃ¡n,Cuba,Sancti SpÃ­ritus,3566603
Bejucal,Cuba,Mayabeque,3567546
Bayamo,Cuba,Granma,3567597
Bauta,Cuba,Artemisa,3567612
BartolomÃ© MasÃ³,Cuba,Granma,3567669
BaraguÃ¡,Cuba,Ciego de Ãvila,3567823
Baracoa,Cuba,GuantÃ¡namo,3567834
Banes,Cuba,HolguÃ­n,3567869
BahÃ­a Honda,Cuba,Artemisa,3567995
Artemisa,Cuba,Artemisa,3568312
Arroyo Naranjo,Cuba,La Habana,3568342
Amancio,Cuba,Las Tunas,3569024
AlquÃ­zar,Cuba,Artemisa,3569136
Alamar,Cuba,La Habana,3569370
Aguada de Pasajeros,Cuba,Cienfuegos,3569546
Abreus,Cuba,Cienfuegos,3569741
Habana del Este,Cuba,La Habana,3746181
Centro Habana,Cuba,La Habana,3746183
La Habana Vieja,Cuba,La Habana,3746184
BÃ¡guanos,Cuba,HolguÃ­n,3746938
JimaguayÃº,Cuba,CamagÃ¼ey,3754915
Arroyo Naranjo,Cuba,La Habana,6956646
Boyeros,Cuba,La Habana,6956647
Diez de Octubre,Cuba,La Habana,6956648
Santa Maria,Cape Verde,Sal,3374218
Praia,Cape Verde,Praia,3374333
Mindelo,Cape Verde,SÃ£o Vicente,3374462
Cova Figueira,Cape Verde,Santa Catarina do Fogo,3374707
Willemstad,Curacao,N/A,3513090
Flying Fish Cove,Christmas Island,N/A,2078127
Protaras,Cyprus,Ammochostos,18918
Paphos,Cyprus,Pafos,146214
Nicosia,Cyprus,Lefkosia,146268
Limassol,Cyprus,Limassol,146384
Larnaca,Cyprus,Larnaka,146400
Kyrenia,Cyprus,Keryneia,146412
Famagusta,Cyprus,Ammochostos,146617
DvÅ¯r KrÃ¡lovÃ© nad Labem,Czech Republic,KrÃ¡lovÃ©hradeckÃ½,3061284
Znojmo,Czech Republic,South Moravian,3061344
ZlÃ­n,Czech Republic,ZlÃ­n,3061370
Å½ÄÃ¡r nad SÃ¡zavou Druhy,Czech Republic,VysoÄina,3061692
Å½ÄÃ¡r nad SÃ¡zavou,Czech Republic,VysoÄina,3061695
Å½atec,Czech Republic,ÃšsteckÃ½,3061822
VyÅ¡kov,Czech Republic,South Moravian,3062283
VsetÃ­n,Czech Republic,ZlÃ­n,3062339
Varnsdorf,Czech Republic,ÃšsteckÃ½,3063375
ValaÅ¡skÃ© MeziÅ™Ã­ÄÃ­,Czech Republic,ZlÃ­n,3063447
ÃšstÃ­ nad OrlicÃ­,Czech Republic,PardubickÃ½,3063546
ÃšstÃ­ nad Labem,Czech Republic,ÃšsteckÃ½,3063548
UherskÃ½ Brod,Czech Republic,ZlÃ­n,3063736
UherskÃ© HradiÅ¡tÄ›,Czech Republic,ZlÃ­n,3063739
Trutnov,Czech Republic,KrÃ¡lovÃ©hradeckÃ½,3063907
TÅ™inec,Czech Republic,MoravskoslezskÃ½,3064000
TÅ™ebÃ­Ä,Czech Republic,VysoÄina,3064104
Teplice,Czech Republic,ÃšsteckÃ½,3064288
TÃ¡bor,Czech Republic,JihoÄeskÃ½,3064379
Svitavy,Czech Republic,PardubickÃ½,3064454
Å umperk,Czech Republic,OlomouckÃ½,3064673
Strakonice,Czech Republic,JihoÄeskÃ½,3065067
StarÃ½ BohumÃ­n,Czech Republic,MoravskoslezskÃ½,3065281
Sokolov,Czech Republic,KarlovarskÃ½,3065617
SlanÃ½,Czech Republic,Central Bohemia,3065903
RoÅ¾nov pod RadhoÅ¡tÄ›m,Czech Republic,ZlÃ­n,3066651
RakovnÃ­k,Czech Republic,Central Bohemia,3067051
ProstÄ›jov,Czech Republic,OlomouckÃ½,3067421
Prosek,Czech Republic,Praha,3067433
PÅ™Ã­bram,Czech Republic,Central Bohemia,3067542
PÅ™erov,Czech Republic,OlomouckÃ½,3067580
Prague,Czech Republic,Praha,3067696
Pilsen,Czech Republic,PlzeÅˆskÃ½,3068160
PÃ­sek,Czech Republic,JihoÄeskÃ½,3068293
PelhÅ™imov,Czech Republic,VysoÄina,3068445
Pardubice,Czech Republic,PardubickÃ½,3068582
Otrokovice,Czech Republic,ZlÃ­n,3068689
Otrokovice,Czech Republic,ZlÃ­n,3068690
Ostrov,Czech Republic,KarlovarskÃ½,3068766
Ostrava,Czech Republic,MoravskoslezskÃ½,3068799
OrlovÃ¡,Czech Republic,MoravskoslezskÃ½,3068873
Opava,Czech Republic,MoravskoslezskÃ½,3068927
Olomouc,Czech Republic,OlomouckÃ½,3069011
NovÃ½ JiÄÃ­n,Czech Republic,MoravskoslezskÃ½,3069305
Neratovice,Czech Republic,Central Bohemia,3069844
NÃ¡chod,Czech Republic,KrÃ¡lovÃ©hradeckÃ½,3070122
Most,Czech Republic,ÃšsteckÃ½,3070291
ModÅ™any,Czech Republic,Praha,3070420
MladÃ¡ Boleslav,Czech Republic,Central Bohemia,3070544
MÄ›lnÃ­k,Czech Republic,Central Bohemia,3070862
Louny,Czech Republic,ÃšsteckÃ½,3071507
LitvÃ­nov,Czech Republic,ÃšsteckÃ½,3071665
LitomÄ›Å™ice,Czech Republic,ÃšsteckÃ½,3071677
Liberec,Czech Republic,LibereckÃ½,3071961
LibeÅˆ,Czech Republic,Praha,3071966
LetÅˆany,Czech Republic,Praha,3072137
KutnÃ¡ Hora,Czech Republic,Central Bohemia,3072463
KromÄ›Å™Ã­Å¾,Czech Republic,ZlÃ­n,3072649
Krnov,Czech Republic,MoravskoslezskÃ½,3072656
Kralupy nad Vltavou,Czech Republic,Central Bohemia,3072929
KopÅ™ivnice,Czech Republic,MoravskoslezskÃ½,3073254
KolÃ­n,Czech Republic,Central Bohemia,3073371
Klatovy,Czech Republic,PlzeÅˆskÃ½,3073660
KlÃ¡Å¡terec nad OhÅ™Ã­,Czech Republic,ÃšsteckÃ½,3073668
Kladno,Czech Republic,Central Bohemia,3073699
KarvinÃ¡,Czech Republic,MoravskoslezskÃ½,3073789
Karlovy Vary,Czech Republic,KarlovarskÃ½,3073803
KadaÅˆ,Czech Republic,ÃšsteckÃ½,3074020
KadaÅˆ,Czech Republic,ÃšsteckÃ½,3074039
Jirkov,Czech Republic,ÃšsteckÃ½,3074110
JindÅ™ichÅ¯v Hradec,Czech Republic,JihoÄeskÃ½,3074149
Jihlava,Czech Republic,VysoÄina,3074199
JiÄÃ­n,Czech Republic,KrÃ¡lovÃ©hradeckÃ½,3074204
Jablonec nad Nisou,Czech Republic,LibereckÃ½,3074603
Hranice,Czech Republic,OlomouckÃ½,3074893
Hradec KrÃ¡lovÃ©,Czech Republic,KrÃ¡lovÃ©hradeckÃ½,3074967
HodonÃ­n,Czech Republic,South Moravian,3075654
HavlÃ­ÄkÅ¯v Brod,Czech Republic,VysoÄina,3075919
HavÃ­Å™ov,Czech Republic,MoravskoslezskÃ½,3075921
FrÃ½dek-MÃ­stek,Czech Republic,MoravskoslezskÃ½,3076127
DÄ›ÄÃ­n,Czech Republic,ÃšsteckÃ½,3077244
Chrudim,Czech Republic,PardubickÃ½,3077539
Chomutov,Czech Republic,ÃšsteckÃ½,3077685
Cheb,Czech Republic,KarlovarskÃ½,3077835
ÄŒeskÃ½ TÄ›Å¡Ã­n,Czech Republic,MoravskoslezskÃ½,3077882
ÄŒeskÃ© BudÄ›jovice,Czech Republic,JihoÄeskÃ½,3077916
ÄŒeskÃ¡ TÅ™ebovÃ¡,Czech Republic,PardubickÃ½,3077920
ÄŒeskÃ¡ LÃ­pa,Czech Republic,LibereckÃ½,3077929
BruntÃ¡l,Czech Republic,MoravskoslezskÃ½,3078545
Brno,Czech Republic,South Moravian,3078610
BÅ™eclav,Czech Republic,South Moravian,3078773
BranÃ­k,Czech Republic,Praha,3078833
BrandÃ½s nad Labem-StarÃ¡ Boleslav,Czech Republic,Central Bohemia,3078837
BohumÃ­n,Czech Republic,MoravskoslezskÃ½,3079129
Blansko,Czech Republic,South Moravian,3079273
BÃ­lina Kyselka,Czech Republic,ÃšsteckÃ½,3079346
BÃ­lina,Czech Republic,ÃšsteckÃ½,3079348
Beroun,Czech Republic,Central Bohemia,3079467
BeneÅ¡ov,Czech Republic,Central Bohemia,3079508
ÄŒernÃ½ Most,Czech Republic,Praha,6269470
Zwickau,Germany,Saxony,2803560
ZweibrÃ¼cken,Germany,Rheinland-Pfalz,2803620
Zulpich,Germany,North Rhine-Westphalia,2803723
Zossen,Germany,Brandenburg,2803870
Zittau,Germany,Saxony,2804008
Zirndorf,Germany,Bavaria,2804034
Zerbst,Germany,Saxony-Anhalt,2804748
Zeitz,Germany,Saxony-Anhalt,2804922
Zehlendorf,Germany,Berlin,2805059
Xanten,Germany,North Rhine-Westphalia,2805385
Wurzen,Germany,Saxony,2805597
WÃ¼rzburg,Germany,Bavaria,2805615
WÃ¼rselen,Germany,North Rhine-Westphalia,2805644
Wuppertal,Germany,North Rhine-Westphalia,2805753
Wunstorf,Germany,Lower Saxony,2805761
WÃ¼lfrath,Germany,North Rhine-Westphalia,2805910
WÃ¶rth am Rhein,Germany,Rheinland-Pfalz,2806081
Worms,Germany,Rheinland-Pfalz,2806142
Wolfsburg,Germany,Lower Saxony,2806654
Wolfratshausen,Germany,Bavaria,2806768
WolfenbÃ¼ttel,Germany,Lower Saxony,2806914
Wolfen,Germany,Saxony-Anhalt,2806919
Witzenhausen,Germany,Hesse,2807184
Wittstock,Germany,Brandenburg,2807201
Wittmund,Germany,Lower Saxony,2807218
Wittlich,Germany,Rheinland-Pfalz,2807240
Wittenberge,Germany,Brandenburg,2807344
Wittenau,Germany,Berlin,2807360
Witten,Germany,North Rhine-Westphalia,2807363
Wismar,Germany,Mecklenburg-Vorpommern,2807465
WipperfÃ¼rth,Germany,North Rhine-Westphalia,2807594
Winterhude,Germany,Hamburg,2807748
Winsen,Germany,Lower Saxony,2807845
Winnenden,Germany,Baden-WÃ¼rttemberg,2807872
Wilnsdorf,Germany,North Rhine-Westphalia,2808461
Wilmersdorf,Germany,Berlin,2808473
Willich,Germany,North Rhine-Westphalia,2808559
Wilhelmstadt,Germany,Berlin,2808662
Wilhelmshaven,Germany,Lower Saxony,2808720
Wildeshausen,Germany,Lower Saxony,2808893
Wiesloch,Germany,Baden-WÃ¼rttemberg,2809138
Wiesbaden,Germany,Hesse,2809346
Wiehl,Germany,North Rhine-Westphalia,2809517
Wetzlar,Germany,Hesse,2809889
Wetter (Ruhr),Germany,North Rhine-Westphalia,2809984
Westerstede,Germany,Lower Saxony,2810188
Westend,Germany,Berlin,2810538
Wesseling,Germany,North Rhine-Westphalia,2810612
Wesel,Germany,North Rhine-Westphalia,2810678
Wertheim,Germany,Baden-WÃ¼rttemberg,2810716
Wernigerode,Germany,Saxony-Anhalt,2810808
Werne,Germany,North Rhine-Westphalia,2810833
Wermelskirchen,Germany,North Rhine-Westphalia,2810855
Werl,Germany,North Rhine-Westphalia,2810878
Werdohl,Germany,North Rhine-Westphalia,2810919
Werder,Germany,Brandenburg,2810945
Werdau,Germany,Saxony,2810969
Wendlingen am Neckar,Germany,Baden-WÃ¼rttemberg,2811204
Wenden,Germany,North Rhine-Westphalia,2811278
Wendelstein,Germany,Bavaria,2811292
Weiterstadt,Germany,Hesse,2811644
WeiÃŸwasser,Germany,Saxony,2811698
WeiÃŸenfels,Germany,Saxony-Anhalt,2811899
WeiÃŸenburg in Bayern,Germany,Bavaria,2811909
Weinstadt-Endersbach,Germany,Baden-WÃ¼rttemberg,2812145
Weinheim,Germany,Baden-WÃ¼rttemberg,2812174
Weingarten,Germany,Baden-WÃ¼rttemberg,2812204
Weimar,Germany,Thuringia,2812482
Weilheim,Germany,Bavaria,2812515
Weilerswist,Germany,North Rhine-Westphalia,2812522
Weil der Stadt,Germany,Baden-WÃ¼rttemberg,2812625
Weil am Rhein,Germany,Baden-WÃ¼rttemberg,2812636
Weiden,Germany,Bavaria,2813040
WeiÃŸensee,Germany,Berlin,2813187
Wegberg,Germany,North Rhine-Westphalia,2813390
Weener,Germany,Lower Saxony,2813433
Wedel,Germany,Schleswig-Holstein,2813464
Wedding,Germany,Berlin,2813472
Wassenberg,Germany,North Rhine-Westphalia,2813786
Warstein,Germany,North Rhine-Westphalia,2814005
Warendorf,Germany,North Rhine-Westphalia,2814127
Waren,Germany,Mecklenburg-Vorpommern,2814131
Wardenburg,Germany,Lower Saxony,2814146
Warburg,Germany,North Rhine-Westphalia,2814153
Wangen im AllgÃ¤u,Germany,Baden-WÃ¼rttemberg,2814270
Wandlitz,Germany,Brandenburg,2814305
Waltrop,Germany,North Rhine-Westphalia,2814362
Walsrode,Germany,Lower Saxony,2814462
Wallenhorst,Germany,Lower Saxony,2814632
Waldshut-Tiengen,Germany,Baden-WÃ¼rttemberg,2814791
Waldkraiburg,Germany,Bavaria,2814874
Waldkirch,Germany,Baden-WÃ¼rttemberg,2814883
WaldbrÃ¶l,Germany,North Rhine-Westphalia,2815137
Waiblingen,Germany,Baden-WÃ¼rttemberg,2815330
WaghÃ¤usel,Germany,Baden-WÃ¼rttemberg,2815487
Wadgassen,Germany,Saarland,2815559
Wadern,Germany,Saarland,2815565
Wachtberg,Germany,North Rhine-Westphalia,2815678
Vreden,Germany,North Rhine-Westphalia,2815824
VÃ¶lklingen,Germany,Saarland,2816630
Voerde,Germany,North Rhine-Westphalia,2817065
Vlotho,Germany,North Rhine-Westphalia,2817105
Vilshofen,Germany,Bavaria,2817202
Villingen-Schwenningen,Germany,Baden-WÃ¼rttemberg,2817220
Viersen,Germany,North Rhine-Westphalia,2817311
Viernheim,Germany,Hesse,2817324
Versmold,Germany,North Rhine-Westphalia,2817537
Verl,Germany,North Rhine-Westphalia,2817576
Verden,Germany,Lower Saxony,2817599
Velbert,Germany,North Rhine-Westphalia,2817724
Vechta,Germany,Lower Saxony,2817812
Vechelde,Germany,Lower Saxony,2817813
Vaterstetten,Germany,Bavaria,2817818
Varel,Germany,Lower Saxony,2817873
Vaihingen an der Enz,Germany,Baden-WÃ¼rttemberg,2817927
Uetersen,Germany,Schleswig-Holstein,2818067
Uslar,Germany,Lower Saxony,2818094
UnterschleiÃŸheim,Germany,Bavaria,2818766
Unterhaching,Germany,Bavaria,2819465
Unterkrozingen,Germany,Baden-WÃ¼rttemberg,2819974
Unna,Germany,North Rhine-Westphalia,2820087
Ulm,Germany,Baden-WÃ¼rttemberg,2820256
Uelzen,Germany,Lower Saxony,2820456
Ãœberlingen,Germany,Baden-WÃ¼rttemberg,2820577
Ãœbach-Palenberg,Germany,North Rhine-Westphalia,2820621
Tuttlingen,Germany,Baden-WÃ¼rttemberg,2820693
TÃ¼bingen,Germany,Baden-WÃ¼rttemberg,2820860
Trossingen,Germany,Baden-WÃ¼rttemberg,2820973
Troisdorf,Germany,North Rhine-Westphalia,2821029
Trier,Germany,Rheinland-Pfalz,2821164
Traunstein,Germany,Bavaria,2821515
Traunreut,Germany,Bavaria,2821517
Torgau,Germany,Saxony,2821807
TÃ¶nisvorst,Germany,North Rhine-Westphalia,2821899
Tettnang,Germany,Baden-WÃ¼rttemberg,2823368
Templin,Germany,Brandenburg,2823533
Tempelhof,Germany,Berlin,2823538
Teltow,Germany,Brandenburg,2823567
Telgte,Germany,North Rhine-Westphalia,2823590
Tegel,Germany,Berlin,2823708
Taunusstein,Germany,Hesse,2823799
Taufkirchen,Germany,Bavaria,2823812
Syke,Germany,Lower Saxony,2824461
Sundern,Germany,North Rhine-Westphalia,2824655
Sulzbach-Rosenberg,Germany,Bavaria,2824801
Sulzbach,Germany,Saarland,2824841
Suhl,Germany,Thuringia,2824948
Stuttgart,Germany,Baden-WÃ¼rttemberg,2825297
Stuhr,Germany,Lower Saxony,2825422
Strausberg,Germany,Brandenburg,2826082
Straubing,Germany,Bavaria,2826099
Stralsund,Germany,Mecklenburg-Vorpommern,2826287
Straelen,Germany,North Rhine-Westphalia,2826304
Stolberg,Germany,North Rhine-Westphalia,2826595
Stockelsdorf,Germany,Schleswig-Holstein,2826861
Stockach,Germany,Baden-WÃ¼rttemberg,2826909
Stendal,Germany,Saxony-Anhalt,2827479
Stellingen,Germany,Hamburg,2827552
Steinhagen,Germany,North Rhine-Westphalia,2828050
Steinfurt,Germany,North Rhine-Westphalia,2828105
Steilshoop,Germany,Hamburg,2828994
Steglitz,Germany,Berlin,2829109
StaÃŸfurt,Germany,Saxony-Anhalt,2829422
Starnberg,Germany,Bavaria,2829457
Stadtlohn,Germany,North Rhine-Westphalia,2829758
Stadthagen,Germany,Lower Saxony,2829777
Stadtallendorf,Germany,Hesse,2829804
Stade,Germany,Lower Saxony,2829901
Staaken,Germany,Berlin,2829962
SprockhÃ¶vel,Germany,North Rhine-Westphalia,2829998
Springe,Germany,Lower Saxony,2830035
Speyer,Germany,Rheinland-Pfalz,2830582
Spenge,Germany,North Rhine-Westphalia,2830637
Sonthofen,Germany,Bavaria,2831088
Sonneberg,Germany,Thuringia,2831250
Sondershausen,Germany,Thuringia,2831276
SÃ¶mmerda,Germany,Thuringia,2831403
Soltau,Germany,Lower Saxony,2831486
Solingen,Germany,North Rhine-Westphalia,2831580
Soest,Germany,North Rhine-Westphalia,2831708
Sinzig,Germany,Rheinland-Pfalz,2831852
Sinsheim,Germany,Baden-WÃ¼rttemberg,2831872
Singen,Germany,Baden-WÃ¼rttemberg,2831924
Sindelfingen,Germany,Baden-WÃ¼rttemberg,2831948
Simmerath,Germany,North Rhine-Westphalia,2832023
Sigmaringen,Germany,Baden-WÃ¼rttemberg,2832232
Siegen,Germany,North Rhine-Westphalia,2832495
Siegburg,Germany,North Rhine-Westphalia,2832521
Senftenberg,Germany,Brandenburg,2833073
Senden,Germany,North Rhine-Westphalia,2833079
Senden,Germany,Bavaria,2833080
Selm,Germany,North Rhine-Westphalia,2833170
Seligenstadt,Germany,Hesse,2833242
Selb,Germany,Bavaria,2833296
Sehnde,Germany,Lower Saxony,2833475
Seevetal,Germany,Lower Saxony,2833564
Seesen,Germany,Lower Saxony,2833592
Seelze,Germany,Lower Saxony,2833641
Schwetzingen,Germany,Baden-WÃ¼rttemberg,2834240
Schwerte,Germany,North Rhine-Westphalia,2834265
Schwerin,Germany,Mecklenburg-Vorpommern,2834282
Schwelm,Germany,North Rhine-Westphalia,2834372
Schweinfurt,Germany,Bavaria,2834498
Schwedt (Oder),Germany,Brandenburg,2834629
Schwarzenberg,Germany,Saxony,2834978
Schwanewede,Germany,Lower Saxony,2835260
Schwandorf in Bayern,Germany,Bavaria,2835297
Schwalmtal,Germany,North Rhine-Westphalia,2835342
Schwalmstadt,Germany,Hesse,2835345
Schwalbach,Germany,Saarland,2835382
SchwÃ¤bisch Hall,Germany,Baden-WÃ¼rttemberg,2835481
SchwÃ¤bisch GmÃ¼nd,Germany,Baden-WÃ¼rttemberg,2835482
Schwabach,Germany,Bavaria,2835537
Schrobenhausen,Germany,Bavaria,2836084
Schramberg,Germany,Baden-WÃ¼rttemberg,2836203
Schortens,Germany,Lower Saxony,2836282
Schorndorf,Germany,Baden-WÃ¼rttemberg,2836320
Schopfheim,Germany,Baden-WÃ¼rttemberg,2836413
SchÃ¶neberg,Germany,Berlin,2836788
SchÃ¶nebeck,Germany,Saxony-Anhalt,2836809
Schneverdingen,Germany,Lower Saxony,2837291
Schneeberg,Germany,Saxony,2837470
Schmelz,Germany,Saarland,2837954
Schmargendorf,Germany,Berlin,2838009
Schmallenberg,Germany,North Rhine-Westphalia,2838053
Schmalkalden,Germany,Thuringia,2838059
SchlÃ¼chtern,Germany,Hesse,2838201
Schleswig,Germany,Schleswig-Holstein,2838634
Schkeuditz,Germany,Saxony,2839050
Schiffweiler,Germany,Saarland,2839316
Schifferstadt,Germany,Rheinland-Pfalz,2839335
Saulgau,Germany,Baden-WÃ¼rttemberg,2841125
Sasel,Germany,Hamburg,2841374
Sarstedt,Germany,Lower Saxony,2841386
Sankt Wendel,Germany,Saarland,2841463
Sankt Ingbert,Germany,Saarland,2841590
Sankt Augustin,Germany,North Rhine-Westphalia,2841648
Sangerhausen,Germany,Saxony-Anhalt,2841693
Salzwedel,Germany,Saxony-Anhalt,2842112
Salzkotten,Germany,North Rhine-Westphalia,2842131
Saarlouis,Germany,Saarland,2842632
SaarbrÃ¼cken,Germany,Saarland,2842647
Saalfeld,Germany,Thuringia,2842688
RÃ¼sselsheim,Germany,Hesse,2842884
Rummelsburg,Germany,Berlin,2843106
Rudow,Germany,Berlin,2843350
Rudolstadt,Germany,Thuringia,2843355
Rottweil,Germany,Baden-WÃ¼rttemberg,2843636
Rottenburg,Germany,Baden-WÃ¼rttemberg,2843729
Roth,Germany,Bavaria,2844265
Rotenburg,Germany,Lower Saxony,2844437
Rostock,Germany,Mecklenburg-Vorpommern,2844588
RÃ¶srath,Germany,North Rhine-Westphalia,2844862
Rosenheim,Germany,Bavaria,2844988
Ronnenberg,Germany,Lower Saxony,2845222
Rinteln,Germany,Lower Saxony,2846523
Rietberg,Germany,North Rhine-Westphalia,2846843
Riesa,Germany,Saxony,2846939
Riegelsberg,Germany,Saarland,2847033
Ribnitz-Damgarten,Germany,Mecklenburg-Vorpommern,2847524
Rheinfelden (Baden),Germany,Baden-WÃ¼rttemberg,2847639
Rheine,Germany,North Rhine-Westphalia,2847645
Rheinberg,Germany,North Rhine-Westphalia,2847662
Rheinbach,Germany,North Rhine-Westphalia,2847666
Rhede,Germany,North Rhine-Westphalia,2847689
Rheda-WiedenbrÃ¼ck,Germany,North Rhine-Westphalia,2847690
Reutlingen,Germany,Baden-WÃ¼rttemberg,2847736
Renningen,Germany,Baden-WÃ¼rttemberg,2848175
Rendsburg,Germany,Schleswig-Holstein,2848245
Remscheid,Germany,North Rhine-Westphalia,2848273
Remagen,Germany,Rheinland-Pfalz,2848335
Reinickendorf,Germany,Berlin,2848756
Reinheim,Germany,Hesse,2848762
Reinbek,Germany,Schleswig-Holstein,2848845
Reichenbach/Vogtland,Germany,Saxony,2849156
Regensburg,Germany,Bavaria,2849483
Rees,Germany,North Rhine-Westphalia,2849548
Recklinghausen,Germany,North Rhine-Westphalia,2849647
Ravensburg,Germany,Baden-WÃ¼rttemberg,2849802
Ratingen,Germany,North Rhine-Westphalia,2850174
Rathenow,Germany,Brandenburg,2850213
Ratekau,Germany,Schleswig-Holstein,2850235
Rastede,Germany,Lower Saxony,2850253
Rastatt,Germany,Baden-WÃ¼rttemberg,2850257
Rahden,Germany,North Rhine-Westphalia,2850887
Radolfzell am Bodensee,Germany,Baden-WÃ¼rttemberg,2850954
Radevormwald,Germany,North Rhine-Westphalia,2850995
Radebeul,Germany,Saxony,2851077
Radeberg,Germany,Saxony,2851079
Quickborn,Germany,Schleswig-Holstein,2851343
Quedlinburg,Germany,Saxony-Anhalt,2851465
PÃ¼ttlingen,Germany,Saarland,2851584
Pulheim,Germany,North Rhine-Westphalia,2851746
Puchheim,Germany,Bavaria,2851782
Prenzlauer Berg,Germany,Berlin,2852217
Prenzlau,Germany,Brandenburg,2852218
Preetz,Germany,Schleswig-Holstein,2852280
Potsdam,Germany,Brandenburg,2852458
Porta Westfalica,Germany,North Rhine-Westphalia,2852577
PoppenbÃ¼ttel,Germany,Hamburg,2852673
Plettenberg,Germany,North Rhine-Westphalia,2853209
Plauen,Germany,Saxony,2853292
Pirna,Germany,Saxony,2853572
Pirmasens,Germany,Rheinland-Pfalz,2853574
Pinneberg,Germany,Schleswig-Holstein,2853658
Pfungstadt,Germany,Hesse,2853924
Pfullingen,Germany,Baden-WÃ¼rttemberg,2853928
Pforzheim,Germany,Baden-WÃ¼rttemberg,2853969
Pfaffenhofen an der Ilm,Germany,Bavaria,2854386
Petershagen,Germany,North Rhine-Westphalia,2854655
Penzberg,Germany,Bavaria,2854923
Peine,Germany,Lower Saxony,2855047
Passau,Germany,Bavaria,2855328
Pasing,Germany,Bavaria,2855334
Parchim,Germany,Mecklenburg-Vorpommern,2855441
Papenburg,Germany,Lower Saxony,2855525
Pankow,Germany,Berlin,2855598
Paderborn,Germany,North Rhine-Westphalia,2855745
Oyten,Germany,Lower Saxony,2855794
Overath,Germany,North Rhine-Westphalia,2855859
Ottweiler,Germany,Saarland,2855917
Ottobrunn,Germany,Bavaria,2855935
Osterholz-Scharmbeck,Germany,Lower Saxony,2856500
OsnabrÃ¼ck,Germany,Lower Saxony,2856883
Oschersleben,Germany,Saxony-Anhalt,2856930
Oschatz,Germany,Saxony,2856944
Oranienburg,Germany,Brandenburg,2857129
Opladen,Germany,North Rhine-Westphalia,2857185
Olsberg,Germany,North Rhine-Westphalia,2857291
Olpe,Germany,North Rhine-Westphalia,2857306
Oldenburg,Germany,Lower Saxony,2857458
Olching,Germany,Bavaria,2857472
Ã–hringen,Germany,Baden-WÃ¼rttemberg,2857565
Offenburg,Germany,Baden-WÃ¼rttemberg,2857798
Offenbach,Germany,Hesse,2857807
Oerlinghausen,Germany,North Rhine-Westphalia,2857900
Oer-Erkenschwick,Germany,North Rhine-Westphalia,2857904
Oelde,Germany,North Rhine-Westphalia,2857943
Odenthal,Germany,North Rhine-Westphalia,2858103
Ochtrup,Germany,North Rhine-Westphalia,2858245
Oberursel,Germany,Hesse,2858738
Obertshausen,Germany,Hesse,2858763
OberschÃ¶neweide,Germany,Berlin,2859103
Ober-Ramstadt,Germany,Hesse,2859380
Oberkirch,Germany,Baden-WÃ¼rttemberg,2860080
Oberhausen,Germany,North Rhine-Westphalia,2860410
Oberasbach,Germany,Bavaria,2861402
NÃ¼rtingen,Germany,Baden-WÃ¼rttemberg,2861632
NÃ¼rnberg,Germany,Bavaria,2861650
NÃ¼mbrecht,Germany,North Rhine-Westphalia,2861677
Nottuln,Germany,North Rhine-Westphalia,2861733
Northeim,Germany,Lower Saxony,2861814
NÃ¶rdlingen,Germany,Bavaria,2861914
Nordhorn,Germany,Lower Saxony,2861934
Nordhausen,Germany,Thuringia,2861982
Norderstedt,Germany,Schleswig-Holstein,2862026
Nordenham,Germany,Lower Saxony,2862104
Norden,Germany,Lower Saxony,2862118
Nippes,Germany,North Rhine-Westphalia,2862375
Nikolassee,Germany,Berlin,2862423
Nienburg,Germany,Lower Saxony,2862620
NiederschÃ¶nhausen,Germany,Berlin,2862888
NiederkrÃ¼chten,Germany,North Rhine-Westphalia,2863199
Niederkassel,Germany,North Rhine-Westphalia,2863223
Nieder-Ingelheim,Germany,Rheinland-Pfalz,2863240
Nidderau,Germany,Hesse,2863712
Nidda,Germany,Hesse,2863716
Neu Wulmstorf,Germany,Lower Saxony,2863795
Neuwied,Germany,Rheinland-Pfalz,2863840
Neu-Ulm,Germany,Bavaria,2863941
Neustrelitz,Germany,Mecklenburg-Vorpommern,2864005
Neustadt in Holstein,Germany,Schleswig-Holstein,2864034
Neustadt bei Coburg,Germany,Bavaria,2864053
Neustadt,Germany,Rheinland-Pfalz,2864054
Neustadt am RÃ¼benberge,Germany,Lower Saxony,2864058
Neue Neustadt,Germany,Saxony-Anhalt,2864072
Neuss,Germany,North Rhine-Westphalia,2864118
Neuruppin,Germany,Brandenburg,2864276
Neunkirchen,Germany,Saarland,2864435
NeumÃ¼nster,Germany,Schleswig-Holstein,2864475
Neumarkt in der Oberpfalz,Germany,Bavaria,2864549
Neu Isenburg,Germany,Hesse,2864820
Neufahrn bei Freising,Germany,Bavaria,2865376
Neuenhagen,Germany,Brandenburg,2865716
Neuburg an der Donau,Germany,Bavaria,2866070
NeubrÃ¼ck,Germany,North Rhine-Westphalia,2866110
Neubrandenburg,Germany,Mecklenburg-Vorpommern,2866135
Neu-Anspach,Germany,Hesse,2866280
Nettetal,Germany,North Rhine-Westphalia,2866333
Netphen,Germany,North Rhine-Westphalia,2866375
Neckarsulm,Germany,Baden-WÃ¼rttemberg,2866758
Naumburg,Germany,Saxony-Anhalt,2866906
Nauen,Germany,Brandenburg,2866930
Nagold,Germany,Baden-WÃ¼rttemberg,2867164
Munster,Germany,Lower Saxony,2867542
MÃ¼nster,Germany,North Rhine-Westphalia,2867543
Hannoversch MÃ¼nden,Germany,Lower Saxony,2867613
Munich,Germany,Bavaria,2867714
MÃ¼llheim,Germany,Baden-WÃ¼rttemberg,2867770
MÃ¼lheim (Ruhr),Germany,North Rhine-Westphalia,2867838
MÃ¼hlheim am Main,Germany,Hesse,2867985
Stuttgart MÃ¼hlhausen,Germany,Baden-WÃ¼rttemberg,2867993
MÃ¼hlhausen,Germany,Thuringia,2867996
MÃ¼hldorf,Germany,Bavaria,2868506
MÃ¼hlacker,Germany,Baden-WÃ¼rttemberg,2868788
Much,Germany,North Rhine-Westphalia,2868936
MÃ¶ssingen,Germany,Baden-WÃ¼rttemberg,2869019
Mosbach,Germany,Baden-WÃ¼rttemberg,2869120
Moosburg,Germany,Bavaria,2869449
Monheim am Rhein,Germany,North Rhine-Westphalia,2869791
MÃ¶nchengladbach,Germany,North Rhine-Westphalia,2869894
MÃ¶lln,Germany,Schleswig-Holstein,2869994
Moers,Germany,North Rhine-Westphalia,2870221
Moabit,Germany,Berlin,2870310
Mittweida,Germany,Saxony,2870318
Minden,Germany,North Rhine-Westphalia,2871039
Michelstadt,Germany,Hesse,2871284
Metzingen,Germany,Baden-WÃ¼rttemberg,2871486
Mettmann,Germany,North Rhine-Westphalia,2871535
Meschede,Germany,North Rhine-Westphalia,2871668
Merzig,Germany,Saarland,2871675
Merseburg,Germany,Saxony-Anhalt,2871736
Meppen,Germany,Lower Saxony,2871845
Menden,Germany,North Rhine-Westphalia,2871983
Memmingen,Germany,Bavaria,2871992
Melle,Germany,Lower Saxony,2872079
Meissen,Germany,Saxony,2872155
Meiningen,Germany,Thuringia,2872225
Meinerzhagen,Germany,North Rhine-Westphalia,2872237
Meiderich,Germany,North Rhine-Westphalia,2872347
Meerbusch,Germany,North Rhine-Westphalia,2872504
Meerane,Germany,Saxony,2872519
Meckenheim,Germany,North Rhine-Westphalia,2872582
Mechernich,Germany,North Rhine-Westphalia,2872611
Mayen,Germany,Rheinland-Pfalz,2872649
Marzahn,Germany,Berlin,2873074
Marsberg,Germany,North Rhine-Westphalia,2873211
Marl,Germany,North Rhine-Westphalia,2873263
Marktredwitz,Germany,Bavaria,2873289
Marktoberdorf,Germany,Bavaria,2873291
Markkleeberg,Germany,Saxony,2873352
MÃ¤rkisches Viertel,Germany,Berlin,2873356
Marienfelde,Germany,Berlin,2873589
Mariendorf,Germany,Berlin,2873606
Marburg an der Lahn,Germany,Hesse,2873759
Marbach am Neckar,Germany,Baden-WÃ¼rttemberg,2873776
Mannheim,Germany,Baden-WÃ¼rttemberg,2873891
Mainz,Germany,Rheinland-Pfalz,2874225
Maintal,Germany,Hesse,2874230
Mahlsdorf,Germany,Berlin,2874455
Magdeburg,Germany,Saxony-Anhalt,2874545
LÃ¼nen,Germany,North Rhine-Westphalia,2875107
LÃ¼neburg,Germany,Lower Saxony,2875115
Ludwigshafen am Rhein,Germany,Rheinland-Pfalz,2875376
Ludwigsfelde,Germany,Brandenburg,2875379
Ludwigsburg,Germany,Baden-WÃ¼rttemberg,2875392
LÃ¼dinghausen,Germany,North Rhine-Westphalia,2875417
LÃ¼denscheid,Germany,North Rhine-Westphalia,2875457
Luckenwalde,Germany,Brandenburg,2875484
LÃ¼beck,Germany,Schleswig-Holstein,2875601
LÃ¼bbenau,Germany,Brandenburg,2875623
LÃ¼bbecke,Germany,North Rhine-Westphalia,2875626
Loxstedt,Germany,Lower Saxony,2875645
Losheim,Germany,Saarland,2875831
LÃ¶rrach,Germany,Baden-WÃ¼rttemberg,2875881
Lohr am Main,Germany,Bavaria,2876147
Lohne,Germany,Lower Saxony,2876185
LÃ¶hne,Germany,North Rhine-Westphalia,2876187
Lohmar,Germany,North Rhine-Westphalia,2876218
LÃ¶bau,Germany,Saxony,2876755
Lippstadt,Germany,North Rhine-Westphalia,2876865
Lingen,Germany,Lower Saxony,2877088
Lindlar,Germany,North Rhine-Westphalia,2877142
Lindau,Germany,Bavaria,2877550
Limburg an der Lahn,Germany,Hesse,2877648
Limbach-Oberfrohna,Germany,Saxony,2877673
Lilienthal,Germany,Lower Saxony,2877709
Lichterfelde,Germany,Berlin,2878018
Lichtenrade,Germany,Berlin,2878044
Lichtenfels,Germany,Bavaria,2878074
Lichtenberg,Germany,Berlin,2878102
Leverkusen,Germany,North Rhine-Westphalia,2878234
Leutkirch im AllgÃ¤u,Germany,Baden-WÃ¼rttemberg,2878270
LeopoldshÃ¶he,Germany,North Rhine-Westphalia,2878673
Leonberg,Germany,Baden-WÃ¼rttemberg,2878695
Lennestadt,Germany,North Rhine-Westphalia,2878784
Lengerich,Germany,North Rhine-Westphalia,2878840
Lemgo,Germany,North Rhine-Westphalia,2878943
Leipzig,Germany,Saxony,2879139
Leinfelden-Echterdingen,Germany,Baden-WÃ¼rttemberg,2879185
Leimen,Germany,Baden-WÃ¼rttemberg,2879241
Leichlingen,Germany,North Rhine-Westphalia,2879315
Lehrte,Germany,Lower Saxony,2879367
Leer,Germany,Lower Saxony,2879697
Lebach,Germany,Saarland,2879832
Laupheim,Germany,Baden-WÃ¼rttemberg,2880077
Lauf an der Pegnitz,Germany,Bavaria,2880144
Lauchhammer,Germany,Brandenburg,2880221
Lankwitz,Germany,Berlin,2880498
Langenhorn,Germany,Hamburg,2881018
Langenhagen,Germany,Lower Saxony,2881062
Langenfeld,Germany,North Rhine-Westphalia,2881085
Langen,Germany,Lower Saxony,2881276
Langen,Germany,Hesse,2881279
Landshut,Germany,Bavaria,2881485
Landsberg am Lech,Germany,Bavaria,2881509
Landau in der Pfalz,Germany,Rheinland-Pfalz,2881646
Lampertheim,Germany,Hesse,2881695
Lahr,Germany,Baden-WÃ¼rttemberg,2881885
Lahnstein,Germany,Rheinland-Pfalz,2881889
Lage,Germany,North Rhine-Westphalia,2881956
Laatzen,Germany,Lower Saxony,2882087
Bad Laasphe,Germany,North Rhine-Westphalia,2882091
KÃ¼rten,Germany,North Rhine-Westphalia,2882318
KÃ¼nzelsau,Germany,Baden-WÃ¼rttemberg,2882439
KÃ¼nzell,Germany,Hesse,2882440
Kulmbach,Germany,Bavaria,2882588
Kronberg,Germany,Hesse,2883754
Kronach,Germany,Bavaria,2883784
Kreuztal,Germany,North Rhine-Westphalia,2884050
Kreuzberg,Germany,Berlin,2884161
Kreuzau,Germany,North Rhine-Westphalia,2884245
Krefeld,Germany,North Rhine-Westphalia,2884509
KÃ¶then,Germany,Saxony-Anhalt,2885237
Korschenbroich,Germany,North Rhine-Westphalia,2885397
Kornwestheim,Germany,Baden-WÃ¼rttemberg,2885408
Korntal,Germany,Baden-WÃ¼rttemberg,2885412
Korbach,Germany,Hesse,2885536
KÃ¶penick,Germany,Berlin,2885656
Berlin KÃ¶penick,Germany,Berlin,2885657
Konz,Germany,Rheinland-Pfalz,2885672
Konstanz,Germany,Baden-WÃ¼rttemberg,2885679
KÃ¶nigs Wusterhausen,Germany,Brandenburg,2885732
KÃ¶nigswinter,Germany,North Rhine-Westphalia,2885734
KÃ¶nigstein im Taunus,Germany,Hesse,2885760
KÃ¶nigslutter am Elm,Germany,Lower Saxony,2885800
KÃ¶nigsbrunn,Germany,Bavaria,2885908
KÃ¶ln,Germany,North Rhine-Westphalia,2886242
Kolbermoor,Germany,Bavaria,2886446
Koblenz,Germany,Rheinland-Pfalz,2886946
Kleve,Germany,North Rhine-Westphalia,2887835
Kleinmachnow,Germany,Brandenburg,2888523
Kitzingen,Germany,Bavaria,2890158
Kirchlengern,Germany,North Rhine-Westphalia,2890425
Kirchheim unter Teck,Germany,Baden-WÃ¼rttemberg,2890473
Kirchhain,Germany,Hesse,2890504
Kierspe,Germany,North Rhine-Westphalia,2891014
Kiel,Germany,Schleswig-Holstein,2891122
Kevelaer,Germany,North Rhine-Westphalia,2891258
Kerpen,Germany,North Rhine-Westphalia,2891524
Kempten (AllgÃ¤u),Germany,Bavaria,2891621
Kempen,Germany,North Rhine-Westphalia,2891643
Kelkheim (Taunus),Germany,Hesse,2891832
Kelheim,Germany,Bavaria,2891834
Kehl,Germany,Baden-WÃ¼rttemberg,2891951
Kaulsdorf,Germany,Berlin,2892051
Kaufbeuren,Germany,Bavaria,2892080
Kassel,Germany,Hesse,2892518
Karow,Germany,Berlin,2892705
Karlstadt,Germany,Bavaria,2892786
Karlsruhe,Germany,Baden-WÃ¼rttemberg,2892794
Karlshorst,Germany,Berlin,2892811
Karlsfeld,Germany,Bavaria,2892874
Karben,Germany,Hesse,2892980
Kamp-Lintfort,Germany,North Rhine-Westphalia,2893264
Kamenz,Germany,Saxony,2893437
Kamen,Germany,North Rhine-Westphalia,2893438
Kaltenkirchen,Germany,Schleswig-Holstein,2893544
Kaiserslautern,Germany,Rheinland-Pfalz,2894003
Kaarst,Germany,North Rhine-Westphalia,2894375
JÃ¼lich,Germany,North Rhine-Westphalia,2894553
JÃ¼chen,Germany,North Rhine-Westphalia,2894637
Johannisthal,Germany,Berlin,2894755
Jena,Germany,Thuringia,2895044
Itzehoe,Germany,Schleswig-Holstein,2895569
Isernhagen Farster Bauerschaft,Germany,Lower Saxony,2895664
Iserlohn,Germany,North Rhine-Westphalia,2895669
Ingolstadt,Germany,Bavaria,2895992
Ilmenau,Germany,Thuringia,2896514
Illingen,Germany,Saarland,2896538
Illertissen,Germany,Bavaria,2896546
Idstein,Germany,Hesse,2896736
Idar-Oberstein,Germany,Rheinland-Pfalz,2896753
IbbenbÃ¼ren,Germany,North Rhine-Westphalia,2896817
Husum,Germany,Schleswig-Holstein,2897132
HÃ¼rth,Germany,North Rhine-Westphalia,2897216
HÃ¼nfeld,Germany,Hesse,2897436
HummelsbÃ¼ttel,Germany,Hamburg,2897674
Humboldtkolonie,Germany,North Rhine-Westphalia,2897732
Hude,Germany,Lower Saxony,2898079
HÃ¼ckeswagen,Germany,North Rhine-Westphalia,2898098
HÃ¼ckelhoven,Germany,North Rhine-Westphalia,2898111
Hoyerswerda,Germany,Saxony,2898304
HÃ¶xter,Germany,North Rhine-Westphalia,2898321
HÃ¶velhof,Germany,North Rhine-Westphalia,2898364
HÃ¶rstel,Germany,North Rhine-Westphalia,2898603
Horb am Neckar,Germany,Baden-WÃ¼rttemberg,2899101
Homburg,Germany,Saarland,2899449
Holzwickede,Germany,North Rhine-Westphalia,2899538
Holzminden,Germany,Lower Saxony,2899601
Holzkirchen,Germany,Bavaria,2899676
Hohenstein-Ernstthal,Germany,Saxony,2901420
Hohen Neuendorf,Germany,Brandenburg,2901588
Hofheim am Taunus,Germany,Hesse,2902533
Hofgeismar,Germany,Hesse,2902559
Hof,Germany,Bavaria,2902768
Hockenheim,Germany,Baden-WÃ¼rttemberg,2902852
Hochheim am Main,Germany,Hesse,2903175
Hochfeld,Germany,North Rhine-Westphalia,2903237
Hille,Germany,North Rhine-Westphalia,2904725
Hildesheim,Germany,Lower Saxony,2904789
Hilden,Germany,North Rhine-Westphalia,2904795
Hilchenbach,Germany,North Rhine-Westphalia,2904808
Hiddenhausen,Germany,North Rhine-Westphalia,2904886
Heusweiler,Germany,Saarland,2904985
Heusenstamm,Germany,Hesse,2904992
Hettstedt,Germany,Saxony-Anhalt,2905206
Hessisch Oldendorf,Germany,Lower Saxony,2905290
Herzogenrath,Germany,North Rhine-Westphalia,2905455
Herzogenaurach,Germany,Bavaria,2905457
Herten,Germany,North Rhine-Westphalia,2905560
Herrenberg,Germany,Baden-WÃ¼rttemberg,2905826
Herne,Germany,North Rhine-Westphalia,2905891
Hermsdorf,Germany,Berlin,2905904
Herford,Germany,North Rhine-Westphalia,2906121
Herdecke,Germany,North Rhine-Westphalia,2906152
Herborn,Germany,Hesse,2906199
Heppenheim an der Bergstrasse,Germany,Hesse,2906268
Hennigsdorf,Germany,Brandenburg,2906331
Hennef,Germany,North Rhine-Westphalia,2906376
Hemmingen,Germany,Lower Saxony,2906530
Hemer,Germany,North Rhine-Westphalia,2906595
Helmstedt,Germany,Lower Saxony,2906676
Hellersdorf,Germany,Berlin,2906809
Heinsberg,Germany,North Rhine-Westphalia,2907201
Heilbad Heiligenstadt,Germany,Thuringia,2907545
Heiligensee,Germany,Berlin,2907551
Heiligenhaus,Germany,North Rhine-Westphalia,2907585
Heilbronn,Germany,Baden-WÃ¼rttemberg,2907669
Heidenheim an der Brenz,Germany,Baden-WÃ¼rttemberg,2907851
Heidenau,Germany,Saxony,2907887
Heidelberg,Germany,Baden-WÃ¼rttemberg,2907911
Heide,Germany,Schleswig-Holstein,2908032
Hechingen,Germany,Baden-WÃ¼rttemberg,2908495
Hattingen,Germany,North Rhine-Westphalia,2909230
Hattersheim,Germany,Hesse,2909240
HaÃŸloch,Germany,Rheinland-Pfalz,2909313
Harsewinkel,Germany,North Rhine-Westphalia,2910278
Haren,Germany,Lower Saxony,2910514
Harburg,Germany,Hamburg,2910685
Hannover,Germany,Lower Saxony,2910831
Hanau am Main,Germany,Hesse,2911007
Hamminkeln,Germany,North Rhine-Westphalia,2911051
Hamm,Germany,North Rhine-Westphalia,2911240
Hameln,Germany,Lower Saxony,2911271
Wandsbek,Germany,Hamburg,2911285
Marienthal,Germany,Hamburg,2911287
Hamburg-Mitte,Germany,Hamburg,2911288
EimsbÃ¼ttel,Germany,Hamburg,2911293
Altona,Germany,Hamburg,2911296
Hamburg,Germany,Hamburg,2911298
Halver,Germany,North Rhine-Westphalia,2911384
Haltern,Germany,North Rhine-Westphalia,2911395
Halstenbek,Germany,Schleswig-Holstein,2911408
Halle,Germany,North Rhine-Westphalia,2911520
Halle (Saale),Germany,Saxony-Anhalt,2911522
Haldensleben I,Germany,Saxony-Anhalt,2911584
Halberstadt,Germany,Saxony-Anhalt,2911665
Hakenfelde,Germany,Berlin,2911710
Haiger,Germany,Hesse,2911964
Hagen,Germany,North Rhine-Westphalia,2912621
Haar,Germany,Bavaria,2913192
Haan,Germany,North Rhine-Westphalia,2913195
GÃ¼tersloh,Germany,North Rhine-Westphalia,2913366
GÃ¼strow,Germany,Mecklenburg-Vorpommern,2913433
Gunzenhausen,Germany,Bavaria,2913537
GÃ¼nzburg,Germany,Bavaria,2913555
Gummersbach,Germany,North Rhine-Westphalia,2913761
Guben,Germany,Brandenburg,2913922
GroÃŸ-Umstadt,Germany,Hesse,2914929
GroÃŸostheim,Germany,Bavaria,2915196
GroÃŸ-Gerau,Germany,Hesse,2915613
GroÃŸenhain,Germany,Saxony,2916630
Gronau,Germany,North Rhine-Westphalia,2917138
GrÃ¶benzell,Germany,Bavaria,2917221
Grimma,Germany,Saxony,2917325
Griesheim,Germany,Hesse,2917412
Grevenbroich,Germany,North Rhine-Westphalia,2917540
Greven,Germany,North Rhine-Westphalia,2917544
Greiz,Germany,Thuringia,2917737
Greifswald,Germany,Mecklenburg-Vorpommern,2917788
Grefrath,Germany,North Rhine-Westphalia,2917816
GÃ¶ttingen,Germany,Lower Saxony,2918632
Gotha,Germany,Thuringia,2918752
Goslar,Germany,Lower Saxony,2918840
GÃ¶rlitz,Germany,Saxony,2918987
GÃ¶ppingen,Germany,Baden-WÃ¼rttemberg,2919054
Goch,Germany,North Rhine-Westphalia,2919625
Glinde,Germany,Schleswig-Holstein,2919880
Glauchau,Germany,Saxony,2920020
Gladbeck,Germany,North Rhine-Westphalia,2920236
Ginsheim-Gustavsburg,Germany,Hesse,2920329
Gilching,Germany,Bavaria,2920433
Gifhorn,Germany,Lower Saxony,2920478
GieÃŸen,Germany,Hesse,2920512
Giengen an der Brenz,Germany,Baden-WÃ¼rttemberg,2920620
Gevelsberg,Germany,North Rhine-Westphalia,2920757
Gesundbrunnen,Germany,Berlin,2920789
Geseke,Germany,North Rhine-Westphalia,2920834
Gescher,Germany,North Rhine-Westphalia,2920842
Gersthofen,Germany,Bavaria,2920891
Germersheim,Germany,Rheinland-Pfalz,2921034
Germering,Germany,Bavaria,2921039
Gerlingen,Germany,Baden-WÃ¼rttemberg,2921061
Geretsried,Germany,Bavaria,2921139
Gera,Germany,Thuringia,2921232
GeorgsmarienhÃ¼tte,Germany,Lower Saxony,2921242
Gelsenkirchen,Germany,North Rhine-Westphalia,2921466
Gelnhausen,Germany,Hesse,2921473
Geldern,Germany,North Rhine-Westphalia,2921528
Geislingen an der Steige,Germany,Baden-WÃ¼rttemberg,2921653
Geilenkirchen,Germany,North Rhine-Westphalia,2921837
Geesthacht,Germany,Schleswig-Holstein,2922102
Gauting,Germany,Bavaria,2922230
Garmisch-Partenkirchen,Germany,Bavaria,2922530
Garching bei MÃ¼nchen,Germany,Bavaria,2922582
Garbsen,Germany,Lower Saxony,2922586
Ganderkesee,Germany,Lower Saxony,2922731
Gaggenau,Germany,Baden-WÃ¼rttemberg,2923362
FÃ¼rth,Germany,Bavaria,2923544
FÃ¼rstenwalde,Germany,Brandenburg,2923588
FÃ¼rstenfeldbruck,Germany,Bavaria,2923625
Fulda,Germany,Hesse,2923822
FrÃ¶ndenberg,Germany,North Rhine-Westphalia,2924206
Frohnau,Germany,Berlin,2924302
Friesoythe,Germany,Lower Saxony,2924360
Friedrichshain,Germany,Berlin,2924573
Friedrichshagen,Germany,Berlin,2924577
Friedrichshafen,Germany,Baden-WÃ¼rttemberg,2924585
Friedrichsfelde,Germany,Berlin,2924599
Friedrichsdorf,Germany,Hesse,2924625
Friedenau,Germany,Berlin,2924770
Friedberg,Germany,Hesse,2924802
Friedberg,Germany,Bavaria,2924803
Freudenstadt,Germany,Baden-WÃ¼rttemberg,2924894
Freudenberg,Germany,North Rhine-Westphalia,2924915
Freital,Germany,Saxony,2925017
Freising,Germany,Bavaria,2925034
Freilassing,Germany,Bavaria,2925080
Freiburg,Germany,Baden-WÃ¼rttemberg,2925177
Freiberg am Neckar,Germany,Baden-WÃ¼rttemberg,2925189
Freiberg,Germany,Saxony,2925192
Frechen,Germany,North Rhine-Westphalia,2925259
Frankfurt am Main,Germany,Hesse,2925533
Frankfurt (Oder),Germany,Brandenburg,2925535
Frankenthal,Germany,Rheinland-Pfalz,2925550
Frankenberg,Germany,Hesse,2925629
Frankenberg,Germany,Saxony,2925630
Forst,Germany,Brandenburg,2925832
Forchheim,Germany,Bavaria,2925910
FlÃ¶rsheim,Germany,Hesse,2926120
Flensburg,Germany,Schleswig-Holstein,2926271
Finsterwalde,Germany,Brandenburg,2926670
Finnentrop,Germany,North Rhine-Westphalia,2926716
Stuttgart Feuerbach,Germany,Baden-WÃ¼rttemberg,2927043
Fellbach,Germany,Baden-WÃ¼rttemberg,2927268
Falkensee,Germany,Brandenburg,2927930
Eutin,Germany,Schleswig-Holstein,2928381
Euskirchen,Germany,North Rhine-Westphalia,2928396
Ettlingen,Germany,Baden-WÃ¼rttemberg,2928615
Esslingen,Germany,Baden-WÃ¼rttemberg,2928751
Essen,Germany,North Rhine-Westphalia,2928810
Espelkamp,Germany,North Rhine-Westphalia,2928874
Eschweiler,Germany,North Rhine-Westphalia,2928963
Eschwege,Germany,Hesse,2928967
Eschborn,Germany,Hesse,2929134
Erwitte,Germany,North Rhine-Westphalia,2929247
Erlangen,Germany,Bavaria,2929567
Erkrath,Germany,North Rhine-Westphalia,2929600
Erkelenz,Germany,North Rhine-Westphalia,2929622
Erfurt,Germany,Thuringia,2929670
Erftstadt,Germany,North Rhine-Westphalia,2929671
Erding,Germany,Bavaria,2929715
Eppingen,Germany,Baden-WÃ¼rttemberg,2929831
Eppelborn,Germany,Saarland,2929865
Ennigerloh,Germany,North Rhine-Westphalia,2930030
Ennepetal,Germany,North Rhine-Westphalia,2930043
Enger,Germany,North Rhine-Westphalia,2930182
Engelskirchen,Germany,North Rhine-Westphalia,2930216
Emsdetten,Germany,North Rhine-Westphalia,2930449
Emmerich,Germany,North Rhine-Westphalia,2930509
Emmendingen,Germany,Baden-WÃ¼rttemberg,2930523
Emden,Germany,Lower Saxony,2930596
Eltville,Germany,Hesse,2930646
Elsdorf,Germany,North Rhine-Westphalia,2930778
Elmshorn,Germany,Schleswig-Holstein,2930821
Ellwangen,Germany,Baden-WÃ¼rttemberg,2930889
Eitorf,Germany,North Rhine-Westphalia,2931361
Eislingen,Germany,Baden-WÃ¼rttemberg,2931414
EisenhÃ¼ttenstadt,Germany,Brandenburg,2931481
Eisenach,Germany,Thuringia,2931574
Einbeck,Germany,Lower Saxony,2931804
Eilenburg,Germany,Saxony,2931871
Ehingen,Germany,Baden-WÃ¼rttemberg,2932924
Eggenstein-Leopoldshafen,Germany,Baden-WÃ¼rttemberg,2933101
Edewecht,Germany,Lower Saxony,2933364
EckernfÃ¶rde,Germany,Schleswig-Holstein,2933627
Eberswalde,Germany,Brandenburg,2933882
Ebersbach an der Fils,Germany,Baden-WÃ¼rttemberg,2933959
Eberbach,Germany,Baden-WÃ¼rttemberg,2934020
DÃ¼sseldorf,Germany,North Rhine-Westphalia,2934246
DÃ¼ren,Germany,North Rhine-Westphalia,2934486
DÃ¼lmen,Germany,North Rhine-Westphalia,2934662
Duisburg,Germany,North Rhine-Westphalia,2934691
Duderstadt,Germany,Lower Saxony,2934728
Dresden,Germany,Saxony,2935022
Drensteinfurt,Germany,North Rhine-Westphalia,2935042
Dreieich,Germany,Hesse,2935220
Dortmund,Germany,North Rhine-Westphalia,2935517
Dorsten,Germany,North Rhine-Westphalia,2935530
Dormagen,Germany,North Rhine-Westphalia,2935825
DonauwÃ¶rth,Germany,Bavaria,2936253
Donaueschingen,Germany,Baden-WÃ¼rttemberg,2936267
DÃ¶beln,Germany,Saxony,2936658
Ditzingen,Germany,Baden-WÃ¼rttemberg,2936705
Dinslaken,Germany,North Rhine-Westphalia,2936871
Dingolfing,Germany,Bavaria,2936909
Dillingen an der Donau,Germany,Bavaria,2936974
Dillingen,Germany,Saarland,2936977
Dillenburg,Germany,Hesse,2936985
Dietzenbach,Germany,Hesse,2937040
Diepholz,Germany,Lower Saxony,2937317
Dieburg,Germany,Hesse,2937591
Deutz,Germany,North Rhine-Westphalia,2937790
Detmold,Germany,North Rhine-Westphalia,2937936
Dessau,Germany,Saxony-Anhalt,2937959
Delmenhorst,Germany,Lower Saxony,2938323
Delitzsch,Germany,Saxony,2938376
DelbrÃ¼ck,Germany,North Rhine-Westphalia,2938389
Deggendorf,Germany,Bavaria,2938540
Datteln,Germany,North Rhine-Westphalia,2938784
Darmstadt,Germany,Hesse,2938913
Damme,Germany,Lower Saxony,2939167
Dahlem,Germany,Berlin,2939440
Dachau,Germany,Bavaria,2939623
Cuxhaven,Germany,Lower Saxony,2939658
Crimmitschau,Germany,Saxony,2939747
Crailsheim,Germany,Baden-WÃ¼rttemberg,2939797
Cottbus,Germany,Brandenburg,2939811
Coswig,Germany,Saxony,2939820
Coesfeld,Germany,North Rhine-Westphalia,2939945
Coburg,Germany,Bavaria,2939951
Cloppenburg,Germany,Lower Saxony,2939969
Clausthal-Zellerfeld,Germany,Lower Saxony,2939995
Chemnitz,Germany,Saxony,2940132
Charlottenburg,Germany,Berlin,2940187
Cham,Germany,Bavaria,2940204
Celle,Germany,Lower Saxony,2940213
Castrop-Rauxel,Germany,North Rhine-Westphalia,2940231
Calw,Germany,Baden-WÃ¼rttemberg,2940383
Buxtehude,Germany,Lower Saxony,2940451
Butzbach,Germany,Hesse,2940512
BÃ¼rstadt,Germany,Hesse,2940938
Burscheid,Germany,North Rhine-Westphalia,2940942
Burghausen,Germany,Bavaria,2941279
Burgdorf,Germany,Lower Saxony,2941405
Burg bei Magdeburg,Germany,Saxony-Anhalt,2941501
BÃ¼ren,Germany,North Rhine-Westphalia,2941570
BÃ¼nde,Germany,North Rhine-Westphalia,2941694
BÃ¼hl,Germany,Baden-WÃ¼rttemberg,2941976
BÃ¼dingen,Germany,Hesse,2942073
Buckow,Germany,Berlin,2942122
BÃ¼ckeburg,Germany,Lower Saxony,2942159
Buchholz in der Nordheide,Germany,Lower Saxony,2942323
FranzÃ¶sisch Buchholz,Germany,Berlin,2942341
Buchen,Germany,Baden-WÃ¼rttemberg,2942634
BrÃ¼hl,Germany,North Rhine-Westphalia,2943320
BrÃ¼ggen,Germany,North Rhine-Westphalia,2943336
BruckmÃ¼hl,Germany,Bavaria,2943408
Bruchsal,Germany,Baden-WÃ¼rttemberg,2943560
BruchkÃ¶bel,Germany,Hesse,2943573
Britz,Germany,Berlin,2944027
Brilon,Germany,North Rhine-Westphalia,2944079
Bretten,Germany,Baden-WÃ¼rttemberg,2944200
BremervÃ¶rde,Germany,Lower Saxony,2944354
Bremerhaven,Germany,Bremen,2944368
Bremen,Germany,Bremen,2944388
Braunschweig,Germany,Lower Saxony,2945024
Brandenburg an der Havel,Germany,Brandenburg,2945358
Bramsche,Germany,Lower Saxony,2945474
Brakel,Germany,North Rhine-Westphalia,2945542
Brake (Unterweser),Germany,Lower Saxony,2945545
Brackenheim,Germany,Baden-WÃ¼rttemberg,2945591
Bottrop,Germany,North Rhine-Westphalia,2945756
Bornheim,Germany,North Rhine-Westphalia,2946111
Borna,Germany,Saxony,2946172
Borken,Germany,North Rhine-Westphalia,2946228
Boppard,Germany,Rheinland-Pfalz,2946366
Bonn,Germany,North Rhine-Westphalia,2946447
BÃ¶nen,Germany,North Rhine-Westphalia,2946478
Bogenhausen,Germany,Bavaria,2947022
Bochum,Germany,North Rhine-Westphalia,2947416
Bocholt,Germany,North Rhine-Westphalia,2947421
BÃ¶blingen,Germany,Baden-WÃ¼rttemberg,2947444
Bobingen,Germany,Bavaria,2947449
Blomberg,Germany,North Rhine-Westphalia,2947641
Blieskastel,Germany,Saarland,2947739
Blankenburg,Germany,Saxony-Anhalt,2948071
Bitterfeld-Wolfen,Germany,Saxony,2948164
Bingen am Rhein,Germany,Rheinland-Pfalz,2948825
Bietigheim-Bissingen,Germany,Baden-WÃ¼rttemberg,2949012
Biesdorf,Germany,Berlin,2949073
Bielefeld,Germany,North Rhine-Westphalia,2949186
Biberach an der RiÃŸ,Germany,Baden-WÃ¼rttemberg,2949423
Bexbach,Germany,Saarland,2949470
Beverungen,Germany,North Rhine-Westphalia,2949475
Bernburg,Germany,Saxony-Anhalt,2950073
Bernau bei Berlin,Germany,Brandenburg,2950096
Berlin,Germany,Berlin,2950159
Bergneustadt,Germany,North Rhine-Westphalia,2950294
Bergkamen,Germany,North Rhine-Westphalia,2950344
Bergisch Gladbach,Germany,North Rhine-Westphalia,2950349
Bergheim,Germany,North Rhine-Westphalia,2950438
Bensheim,Germany,Hesse,2950978
Bendorf,Germany,Rheinland-Pfalz,2951111
Bedburg,Germany,North Rhine-Westphalia,2951648
Beckum,Germany,North Rhine-Westphalia,2951654
Beckingen,Germany,Saarland,2951679
Bayreuth,Germany,Bavaria,2951825
Bautzen,Germany,Saxony,2951881
Baunatal,Germany,Hesse,2951923
Baumschulenweg,Germany,Berlin,2951935
Bassum,Germany,Lower Saxony,2952252
Bamberg,Germany,Bavaria,2952984
Balingen,Germany,Baden-WÃ¼rttemberg,2953089
Baiersbronn,Germany,Baden-WÃ¼rttemberg,2953197
Baesweiler,Germany,North Rhine-Westphalia,2953302
Bad Zwischenahn,Germany,Lower Saxony,2953310
Bad Wildungen,Germany,Hesse,2953317
Bad Waldsee,Germany,Baden-WÃ¼rttemberg,2953320
Bad Vilbel,Germany,Hesse,2953321
Bad TÃ¶lz,Germany,Bavaria,2953324
Bad Soden am Taunus,Germany,Hesse,2953339
Bad Segeberg,Germany,Schleswig-Holstein,2953341
Bad Schwartau,Germany,Schleswig-Holstein,2953347
Bad Salzungen,Germany,Thuringia,2953357
Bad Salzuflen,Germany,North Rhine-Westphalia,2953358
Bad SÃ¤ckingen,Germany,Baden-WÃ¼rttemberg,2953363
Bad Reichenhall,Germany,Bavaria,2953371
Bad Rappenau,Germany,Baden-WÃ¼rttemberg,2953374
Bad Pyrmont,Germany,Lower Saxony,2953379
Bad Oldesloe,Germany,Schleswig-Holstein,2953385
Bad Oeynhausen,Germany,North Rhine-Westphalia,2953386
Bad Neustadt an der Saale,Germany,Bavaria,2953389
Bad Neuenahr-Ahrweiler,Germany,Rheinland-Pfalz,2953391
Bad Nauheim,Germany,Hesse,2953395
Bad MÃ¼nstereifel,Germany,North Rhine-Westphalia,2953398
Bad MÃ¼nder am Deister,Germany,Lower Saxony,2953400
Bad Mergentheim,Germany,Baden-WÃ¼rttemberg,2953402
Bad Lippspringe,Germany,North Rhine-Westphalia,2953405
Bad Langensalza,Germany,Thuringia,2953413
Bad Kreuznach,Germany,Rheinland-Pfalz,2953416
Bad Kissingen,Germany,Bavaria,2953424
Bad Honnef,Germany,North Rhine-Westphalia,2953435
Bad Homburg vor der HÃ¶he,Germany,Hesse,2953436
Bad Hersfeld,Germany,Hesse,2953439
Bad Harzburg,Germany,Lower Saxony,2953449
Bad Essen,Germany,Lower Saxony,2953464
Baden-Baden,Germany,Baden-WÃ¼rttemberg,2953504
Bad DÃ¼rkheim,Germany,Rheinland-Pfalz,2953522
Bad Driburg,Germany,North Rhine-Westphalia,2953525
Bad Berleburg,Germany,North Rhine-Westphalia,2953545
Bad Bentheim,Germany,Lower Saxony,2953552
Bad Aibling,Germany,Bavaria,2953558
Backnang,Germany,Baden-WÃ¼rttemberg,2953568
Babenhausen,Germany,Hesse,2953770
Aurich,Germany,Lower Saxony,2954006
Augsburg,Germany,Bavaria,2954172
Auerbach,Germany,Saxony,2954602
Aue,Germany,Saxony,2954695
Attendorn,Germany,North Rhine-Westphalia,2954932
Aschersleben,Germany,Saxony-Anhalt,2955168
Ascheberg,Germany,North Rhine-Westphalia,2955224
Aschaffenburg,Germany,Bavaria,2955272
Bad Arolsen,Germany,Hesse,2955421
Arnstadt,Germany,Thuringia,2955439
Arnsberg,Germany,North Rhine-Westphalia,2955471
Apolda,Germany,Thuringia,2955770
Ansbach,Germany,Bavaria,2955936
Annaberg-Buchholz,Germany,Saxony,2956005
AngermÃ¼nde,Germany,Brandenburg,2956093
Andernach,Germany,Rheinland-Pfalz,2956206
Amberg,Germany,Bavaria,2956656
Alzey,Germany,Rheinland-Pfalz,2956710
Alzenau in Unterfranken,Germany,Bavaria,2956715
Altglienicke,Germany,Berlin,2957185
Altenburg,Germany,Thuringia,2957773
Altena,Germany,North Rhine-Westphalia,2957886
Altdorf,Germany,Bavaria,2958024
Alsfeld,Germany,Hesse,2958128
Alsdorf,Germany,North Rhine-Westphalia,2958141
Alfter,Germany,North Rhine-Westphalia,2958516
Alfeld,Germany,Lower Saxony,2958533
Albstadt,Germany,Baden-WÃ¼rttemberg,2958595
Aichach,Germany,Bavaria,2958975
Ahrensburg,Germany,Schleswig-Holstein,2959083
Ahlen,Germany,North Rhine-Westphalia,2959223
Ahaus,Germany,North Rhine-Westphalia,2959279
Adlershof,Germany,Berlin,2959441
Achim,Germany,Lower Saxony,2959681
Achern,Germany,Baden-WÃ¼rttemberg,2959686
Aalen,Germany,Baden-WÃ¼rttemberg,2959927
Vellmar,Germany,Hesse,3207197
Henstedt-Ulzburg,Germany,Schleswig-Holstein,3209083
Aachen,Germany,North Rhine-Westphalia,3247449
MÃ¶rfelden-Walldorf,Germany,Hesse,3272460
Riedstadt,Germany,Hesse,3272941
Lauda-KÃ¶nigshofen,Germany,Baden-WÃ¼rttemberg,3274966
Filderstadt,Germany,Baden-WÃ¼rttemberg,3336891
Ostfildern,Germany,Baden-WÃ¼rttemberg,3336892
Rodgau,Germany,Hesse,3336893
Gropiusstadt,Germany,Berlin,3337408
Seeheim-Jugenheim,Germany,Hesse,3337504
Charlottenburg-Nord,Germany,Berlin,6545288
Mitte,Germany,Berlin,6545310
Spremberg,Germany,Brandenburg,6550659
Rheinstetten,Germany,Baden-WÃ¼rttemberg,6558039
Altstadt Sud,Germany,North Rhine-Westphalia,6691072
Altstadt Nord,Germany,North Rhine-Westphalia,6691073
Neuehrenfeld,Germany,North Rhine-Westphalia,6691076
Bilderstoeckchen,Germany,North Rhine-Westphalia,6691078
Stuttgart-Ost,Germany,Baden-WÃ¼rttemberg,6930414
Bochum-Hordel,Germany,North Rhine-Westphalia,6941055
St. Pauli,Germany,Hamburg,6944296
Eidelstedt,Germany,Hamburg,7274677
Halle Neustadt,Germany,Saxony-Anhalt,7289614
Bergedorf,Germany,Hamburg,7290243
Spandau,Germany,Berlin,7290252
Berlin SchÃ¶neberg,Germany,Berlin,7290254
Berlin Treptow,Germany,Berlin,7290255
Niederrad,Germany,Hesse,7290401
Haselbachtal,Germany,Saxony,7302786
Barmbek-Nord,Germany,Hamburg,7932342
Farmsen-Berne,Germany,Hamburg,7932386
Falkenhagener Feld,Germany,Berlin,8334621
Neu-HohenschÃ¶nhausen,Germany,Berlin,8334622
Alt-HohenschÃ¶nhausen,Germany,Berlin,8334624
Fennpfuhl,Germany,Berlin,8334625
Hamburg-Nord,Germany,Hamburg,8354626
Burg Unter-Falkenstein,Germany,Bavaria,8378906
Neustadt/Nord,Germany,North Rhine-Westphalia,8593855
Neustadt/SÃ¼d,Germany,North Rhine-Westphalia,8593856
Kalk,Germany,North Rhine-Westphalia,8593861
MÃ¼lheim,Germany,North Rhine-Westphalia,8593865
Gartenstadt,Germany,Rheinland-Pfalz,8642860
Tadjoura,Djibouti,Tadjourah,220782
Obock,Djibouti,Obock,221527
Djibouti,Djibouti,Djibouti,223817
á¸ŽÃ¢nan,Djibouti,Ali Sabieh,224152
'Ali Sabieh,Djibouti,Ali Sabieh,225284
Viborg,Denmark,Central Jutland,2610319
Vejle,Denmark,South Denmark,2610613
VanlÃ¸se,Denmark,Capital Region,2610734
Taastrup,Denmark,Capital Region,2611828
Svendborg,Denmark,South Denmark,2612045
StenlÃ¸se,Denmark,Capital Region,2612629
SÃ¸nderborg,Denmark,South Denmark,2613102
Slagelse,Denmark,Zealand,2613460
Skive,Denmark,Central Jutland,2613731
Silkeborg,Denmark,Central Jutland,2614030
Roskilde,Denmark,Zealand,2614481
RÃ¸dovre,Denmark,Capital Region,2614600
Ringsted,Denmark,Zealand,2614764
Randers,Denmark,Central Jutland,2615006
Odense,Denmark,South Denmark,2615876
NykÃ¸bing Falster,Denmark,Zealand,2615961
Nyborg,Denmark,South Denmark,2616015
NÃ¦stved,Denmark,Zealand,2616038
NÃ¸rresundby,Denmark,North Denmark,2616235
LillerÃ¸d,Denmark,Capital Region,2617658
KorsÃ¸r,Denmark,Zealand,2618361
KÃ¸ge,Denmark,Zealand,2618415
Copenhagen,Denmark,Capital Region,2618425
Kolding,Denmark,South Denmark,2618528
Kalundborg,Denmark,Zealand,2619154
IshÃ¸j,Denmark,Capital Region,2619377
Hvidovre,Denmark,Capital Region,2619528
Horsens,Denmark,Central Jutland,2619771
HÃ¸rsholm,Denmark,Capital Region,2619856
Holstebro,Denmark,Central Jutland,2620046
HolbÃ¦k,Denmark,Zealand,2620147
HjÃ¸rring,Denmark,North Denmark,2620214
HillerÃ¸d,Denmark,Capital Region,2620320
Herning,Denmark,Central Jutland,2620425
HelsingÃ¸r,Denmark,Capital Region,2620473
Haderslev,Denmark,South Denmark,2620964
Greve,Denmark,Zealand,2621215
Glostrup,Denmark,Capital Region,2621356
Frederikshavn,Denmark,North Denmark,2621927
Frederiksberg,Denmark,Capital Region,2621942
Fredericia,Denmark,South Denmark,2621951
Farum,Denmark,Capital Region,2622306
Esbjerg,Denmark,South Denmark,2622447
Charlottenlund,Denmark,Capital Region,2623188
BirkerÃ¸d,Denmark,Capital Region,2624112
Ballerup,Denmark,Capital Region,2624341
Ã…rhus,Denmark,Central Jutland,2624652
Aalborg,Denmark,North Denmark,2624886
Albertslund,Denmark,Capital Region,2624906
Aabenraa,Denmark,South Denmark,2625070
Roseau,Dominica,Saint George,3575635
Villa Francisca,Dominican Republic,Nacional,3491941
Villa Consuelo,Dominican Republic,Nacional,3491946
Villa BisonÃ³,Dominican Republic,Santiago,3491948
Villa Altagracia,Dominican Republic,San CristÃ³bal,3491952
Tamboril,Dominican Republic,Santiago,3492517
Santo Domingo,Dominican Republic,Nacional,3492908
Santiago de los Caballeros,Dominican Republic,Santiago,3492914
Santa Cruz de El Seibo,Dominican Republic,El SeÃ­bo,3492984
Santa Cruz de Barahona,Dominican Republic,Barahona,3492985
San Pedro de MacorÃ­s,Dominican Republic,San Pedro de MacorÃ­s,3493032
San Juan de la Maguana,Dominican Republic,San Juan,3493081
San JosÃ© de Ocoa,Dominican Republic,San JosÃ© de Ocoa,3493100
San Francisco de MacorÃ­s,Dominican Republic,Duarte,3493146
San Fernando de Monte Cristi,Dominican Republic,Monte Cristi,3493174
Puerto Plata,Dominican Republic,Puerto Plata,3493175
SalvaleÃ³n de HigÃ¼ey,Dominican Republic,La Altagracia,3493240
Salcedo,Dominican Republic,Hermanas Mirabal,3493283
Sabaneta,Dominican Republic,Santiago RodrÃ­guez,3493383
Sabana Grande de BoyÃ¡,Dominican Republic,Monte Plata,3493482
RÃ­o Grande,Dominican Republic,Puerto Plata,3493769
Quisqueya,Dominican Republic,San Pedro de MacorÃ­s,3494121
Punta Cana,Dominican Republic,La Altagracia,3494242
Neiba,Dominican Republic,Baoruco,3495857
Nagua,Dominican Republic,MarÃ­a Trinidad SÃ¡nchez,3496021
Monte Plata,Dominican Republic,Monte Plata,3496134
Moca,Dominican Republic,Espaillat,3496331
Mao,Dominican Republic,Valverde,3496831
Las Matas de FarfÃ¡n,Dominican Republic,San Juan,3500370
La Romana,Dominican Republic,La Romana,3500957
Jarabacoa,Dominican Republic,La Vega,3504158
Hato Mayor del Rey,Dominican Republic,Hato Mayor,3504765
Esperanza,Dominican Republic,Valverde,3505855
DajabÃ³n,Dominican Republic,DajabÃ³n,3508952
CotuÃ­,Dominican Republic,SÃ¡nchez RamÃ­rez,3509207
Constanza,Dominican Republic,La Vega,3509363
ConcepciÃ³n de La Vega,Dominican Republic,La Vega,3509382
Ciudad Nueva,Dominican Republic,Nacional,3509578
Bonao,Dominican Republic,MonseÃ±or Nouel,3511233
Boca Chica,Dominican Republic,Santo Domingo,3511336
San CristÃ³bal,Dominican Republic,San CristÃ³bal,3511540
Bella Vista,Dominican Republic,Nacional,3511550
Bayaguana,Dominican Republic,Monte Plata,3511626
BanÃ­,Dominican Republic,Peravia,3512067
Bajos de Haina,Dominican Republic,San CristÃ³bal,3512128
Azua,Dominican Republic,Azua,3512208
Santo Domingo Oeste,Dominican Republic,Santo Domingo,7874116
Boumerdas,Algeria,Boumerdes,2474141
Zeribet el Oued,Algeria,Biskra,2474506
Zeralda,Algeria,Tipaza,2474583
Zemoura,Algeria,Relizane,2474638
Touggourt,Algeria,Ouargla,2475475
Tolga,Algeria,Biskra,2475612
Tlemcen,Algeria,Tlemcen,2475687
Tizi Rached,Algeria,Tizi Ouzou,2475740
Tizi Ouzou,Algeria,Tizi Ouzou,2475744
Tizi-n-Tleta,Algeria,Tizi Ouzou,2475752
Tizi Gheniff,Algeria,Boumerdes,2475764
Tissemsilt,Algeria,Tissemsilt,2475860
Tirmitine,Algeria,Tizi Ouzou,2475921
Tipasa,Algeria,Tipaza,2476028
Tindouf,Algeria,Tindouf,2476301
Timizart,Algeria,Tizi Ouzou,2476396
Timimoun,Algeria,Adrar,2476403
el hed,Algeria,BejaÃ¯a,2476412
Tiaret,Algeria,Tiaret,2476897
Theniet el Had,Algeria,AÃ¯n Defla,2476915
Thenia,Algeria,Boumerdes,2476917
Telerghma,Algeria,Mila,2477255
TÃ©bessa,Algeria,TÃ©bessa,2477461
Tebesbest,Algeria,Ouargla,2477462
Tazoult-Lambese,Algeria,Batna,2477528
Tamanrasset,Algeria,Tamanghasset,2478216
Tamalous,Algeria,Skikda,2478226
TadmaÃ¯t,Algeria,Boumerdes,2478831
Sour el Ghozlane,Algeria,Bouira,2479161
Souma,Algeria,Blida,2479183
Lardjem,Algeria,Tissemsilt,2479203
Souk Ahras,Algeria,Souk Ahras,2479215
Sougueur,Algeria,Tiaret,2479247
Skikda,Algeria,Skikda,2479536
Sig,Algeria,Mascara,2479609
Sidi Okba,Algeria,Biskra,2479916
Sidi Moussa,Algeria,Blida,2479966
Sidi MÃ©rouane,Algeria,Mila,2480198
Sidi Khaled,Algeria,Biskra,2480368
Sidi ech Chahmi,Algeria,Oran,2480618
Sidi Bel AbbÃ¨s,Algeria,Sidi Bel AbbÃ¨s,2481007
Sidi Amrane,Algeria,Ouargla,2481058
Sidi Akkacha,Algeria,Chlef,2481207
Sidi AÃ¯ssa,Algeria,MÊ¼sila,2481246
Sidi Abdelli,Algeria,Tlemcen,2481389
Sfizef,Algeria,Sidi Bel AbbÃ¨s,2481639
SÃ©tif,Algeria,SÃ©tif,2481700
Sedrata,Algeria,Souk Ahras,2482090
Seddouk,Algeria,BejaÃ¯a,2482159
Sebdou,Algeria,Tlemcen,2482211
Saoula,Algeria,Tipaza,2482390
Salah Bey,Algeria,SÃ©tif,2482447
SaÃ¯da,Algeria,SaÃ¯da,2482572
Rouissat,Algeria,Ouargla,2482886
Rouiba,Algeria,Alger,2482908
Rouached,Algeria,Mila,2482939
Robbah,Algeria,El Oued,2483000
Remchi,Algeria,Tlemcen,2483649
Relizane,Algeria,Relizane,2483668
Reguiba,Algeria,El Oued,2483746
ReghaÃ¯a,Algeria,Boumerdes,2483757
Reggane,Algeria,Adrar,2483761
RÃ¢s el Oued,Algeria,Bordj Bou ArrÃ©ridj,2483936
RÃ¢s el AÃ¯oun,Algeria,Batna,2483968
Oum el Bouaghi,Algeria,Oum el Bouaghi,2484620
Ouled Mimoun,Algeria,Tlemcen,2484846
Oued Sly,Algeria,Chlef,2485572
Oued Rhiou,Algeria,Relizane,2485582
Oued Fodda,Algeria,Chlef,2485618
Oued el Alleug,Algeria,Tipaza,2485633
Oued el Abtal,Algeria,Mascara,2485636
Ouargla,Algeria,Ouargla,2485801
Oran,Algeria,Oran,2485926
Nedroma,Algeria,Tlemcen,2486284
Naciria,Algeria,Boumerdes,2486505
Mâ€™Sila,Algeria,MÊ¼sila,2486690
MouzaÃ¯a,Algeria,Tipaza,2486825
Mostaganem,Algeria,Mostaganem,2487134
Mila,Algeria,Mila,2487452
Metlili Chaamba,Algeria,GhardaÃ¯a,2487620
Messaad,Algeria,Djelfa,2487772
Meskiana,Algeria,Oum el Bouaghi,2487805
Mers el Kebir,Algeria,Oran,2487852
Merouana,Algeria,Batna,2487882
Melouza,Algeria,Bordj Bou ArrÃ©ridj,2488202
Mekla,Algeria,Tizi Ouzou,2488500
Mehdia,Algeria,Tiaret,2488616
Megarine,Algeria,Ouargla,2488716
Meftah,Algeria,Blida,2488722
MÃ©dÃ©a,Algeria,MÃ©dÃ©a,2488835
Mazouna,Algeria,Relizane,2489987
Mascara,Algeria,Mascara,2490098
Mansourah,Algeria,Bordj Bou ArrÃ©ridj,2490180
MansoÃ»ra,Algeria,Tlemcen,2490183
Makouda,Algeria,Boumerdes,2490297
Lâ€™Arbaa NaÃ¯t Irathen,Algeria,Tizi Ouzou,2491042
LarbaÃ¢,Algeria,Batna,2491050
Lakhdaria,Algeria,Bouira,2491134
Laghouat,Algeria,Laghouat,2491191
Ksar el Boukhari,Algeria,MÃ©dÃ©a,2491323
Ksar Chellala,Algeria,Tiaret,2491335
Kolea,Algeria,Tipaza,2491578
Khenchela,Algeria,Khenchela,2491889
Khemis Miliana,Algeria,AÃ¯n Defla,2491911
Khemis el Khechna,Algeria,Boumerdes,2491913
Kerkera,Algeria,Skikda,2492345
Jijel,Algeria,Jijel,2492913
Djidiouia,Algeria,Relizane,2492920
Isser,Algeria,Boumerdes,2492991
I-n-Salah,Algeria,Tamanghasset,2493222
Ighram,Algeria,Tizi Ouzou,2493605
Hennaya,Algeria,Tlemcen,2493918
HÃ©liopolis,Algeria,Guelma,2493956
Hassi Messaoud,Algeria,Ouargla,2494029
Hammamet,Algeria,TÃ©bessa,2494548
Hammam Bou Hadjar,Algeria,AÃ¯n Temouchent,2494554
Hamma Bouziane,Algeria,Constantine,2494610
Hadjout,Algeria,Tipaza,2494962
Guelma,Algeria,Guelma,2495662
GhardaÃ¯a,Algeria,GhardaÃ¯a,2496049
Frenda,Algeria,Tiaret,2496232
Freha,Algeria,Tizi Ouzou,2496241
Feraoun,Algeria,BejaÃ¯a,2496573
Es Senia,Algeria,Oran,2497060
El Tarf,Algeria,El Tarf,2497323
El Oued,Algeria,El Oued,2497411
El Malah,Algeria,AÃ¯n Temouchent,2497714
El Kseur,Algeria,BejaÃ¯a,2497796
El Khroub,Algeria,Constantine,2497849
El Kala,Algeria,El Tarf,2497988
El Idrissia,Algeria,Djelfa,2498000
El Hadjira,Algeria,Ouargla,2498172
El Hadjar,Algeria,Annaba,2498183
El Eulma,Algeria,SÃ©tif,2498392
El Bayadh,Algeria,El Bayadh,2498543
El Attaf,Algeria,AÃ¯n Defla,2498590
Chlef,Algeria,Chlef,2498611
El Aouinet,Algeria,Oum el Bouaghi,2498667
El Amria,Algeria,AÃ¯n Temouchent,2498704
El Affroun,Algeria,Tipaza,2498752
El Achir,Algeria,Bordj Bou ArrÃ©ridj,2498766
El Abiodh Sidi Cheikh,Algeria,El Bayadh,2498775
El Abadia,Algeria,AÃ¯n Defla,2498782
Ech Chettia,Algeria,Chlef,2498954
Drean,Algeria,Annaba,2499055
Draa el Mizan,Algeria,Bouira,2499104
Draa Ben Khedda,Algeria,Boumerdes,2499116
Douera,Algeria,Tipaza,2499193
Djelfa,Algeria,Djelfa,2500017
Djamaa,Algeria,Ouargla,2500282
Didouche Mourad,Algeria,Constantine,2500401
Dellys,Algeria,Boumerdes,2500583
Debila,Algeria,El Oued,2500737
Dar el BeÃ¯da,Algeria,Alger,2500889
Dar Chioukh,Algeria,Djelfa,2500904
Constantine,Algeria,Constantine,2501152
Chorfa,Algeria,Bouira,2501289
Chiffa,Algeria,Blida,2501323
Chetouane,Algeria,Tlemcen,2501362
Cheria,Algeria,TÃ©bessa,2501404
Cheraga,Algeria,Tipaza,2501465
Chemini,Algeria,Tizi Ouzou,2501508
Chelghoum el AÃ¯d,Algeria,Mila,2501541
Chebli,Algeria,Blida,2501680
Charef,Algeria,Djelfa,2501767
Chabet el Ameur,Algeria,Boumerdes,2501873
Brezina,Algeria,El Bayadh,2502034
Bou Tlelis,Algeria,Oran,2502239
Boumahra Ahmed,Algeria,Guelma,2502686
Boukadir,Algeria,Chlef,2502924
Bou IsmaÃ¯l,Algeria,Tipaza,2502939
BouÃ¯ra,Algeria,Bouira,2502958
Bouinan,Algeria,Blida,2502962
Bou Hanifia el Hamamat,Algeria,Mascara,2503033
Bougara,Algeria,Blida,2503147
Bougaa,Algeria,SÃ©tif,2503156
Boufarik,Algeria,Blida,2503181
Boudouaou,Algeria,Boumerdes,2503229
Boudjima,Algeria,Tizi Ouzou,2503237
BoÃ» Arfa,Algeria,Blida,2503468
Bordj Zemoura,Algeria,Bordj Bou ArrÃ©ridj,2503620
Bordj Ghdir,Algeria,Bordj Bou ArrÃ©ridj,2503654
Bordj el Kiffan,Algeria,Alger,2503661
Bordj Bou Arreridj,Algeria,Bordj Bou ArrÃ©ridj,2503701
Boghni,Algeria,Tizi Ouzou,2503755
Blida,Algeria,Blida,2503769
Biskra,Algeria,Biskra,2503826
Birkhadem,Algeria,Alger,2503847
Birine,Algeria,Djelfa,2503852
Bir el Djir,Algeria,Oran,2503874
Bir el Ater,Algeria,TÃ©bessa,2503878
Besbes,Algeria,El Tarf,2504072
Berrouaghia,Algeria,MÃ©dÃ©a,2504099
Berriane,Algeria,GhardaÃ¯a,2504110
Berrahal,Algeria,Annaba,2504136
Bensekrane,Algeria,Tlemcen,2504385
Ben Mehidi,Algeria,El Tarf,2504486
Beni Saf,Algeria,AÃ¯n Temouchent,2504581
Beni Mester,Algeria,Tlemcen,2504616
Beni Mered,Algeria,Blida,2504622
Beni Douala,Algeria,Tizi Ouzou,2504703
Beni Amrane,Algeria,Boumerdes,2504739
BejaÃ¯a,Algeria,BejaÃ¯a,2505329
BÃ©char,Algeria,BÃ©char,2505530
Batna,Algeria,Batna,2505572
Barika,Algeria,Batna,2505629
Barbacha,Algeria,BejaÃ¯a,2505651
Baraki,Algeria,Tipaza,2505653
Bab Ezzouar,Algeria,Alger,2505854
Azzaba,Algeria,Skikda,2505915
Azazga,Algeria,Tizi Ouzou,2506043
Arris,Algeria,Batna,2506404
Arhribs,Algeria,Tizi Ouzou,2506519
Arbatache,Algeria,Boumerdes,2506623
Aoulef,Algeria,Adrar,2506795
Annaba,Algeria,Annaba,2506999
Ammi Moussa,Algeria,Relizane,2507155
Amizour,Algeria,BejaÃ¯a,2507169
Algiers,Algeria,Alger,2507480
Akbou,Algeria,BejaÃ¯a,2507646
AÃ¯n Touta,Algeria,Batna,2507877
AÃ¯n Temouchent,Algeria,AÃ¯n Temouchent,2507901
AÃ¯n Taya,Algeria,Alger,2507912
AÃ¯n Smara,Algeria,Constantine,2507926
AÃ¯n Sefra,Algeria,Naama Ø§Ù„Ù†Ø¹Ø§Ù…Ø©,2507943
AÃ¯n Oussera,Algeria,Djelfa,2507972
â€™AÃ¯n Merane,Algeria,Relizane,2508010
AÃ¯n Kercha,Algeria,Oum el Bouaghi,2508059
AÃ¯n Fakroun,Algeria,Oum el Bouaghi,2508102
â€™AÃ¯n el Turk,Algeria,Oran,2508119
â€™AÃ¯n el Melh,Algeria,MÊ¼sila,2508130
â€™AÃ¯n el Hammam,Algeria,Tizi Ouzou,2508152
â€˜AÃ¯n el Hadjel,Algeria,MÊ¼sila,2508157
AÃ¯n el Bya,Algeria,Oran,2508174
â€™AÃ¯n el Berd,Algeria,Sidi Bel AbbÃ¨s,2508180
â€™AÃ¯n el Bell,Algeria,Djelfa,2508184
â€™AÃ¯n Deheb,Algeria,Tiaret,2508225
AÃ¯n Defla,Algeria,AÃ¯n Defla,2508228
AÃ¯n Bessem,Algeria,Bouira,2508268
â€™AÃ¯n Benian,Algeria,Tipaza,2508275
AÃ¯n BeÃ¯da,Algeria,Oum el Bouaghi,2508287
AÃ¯n Arnat,Algeria,SÃ©tif,2508297
â€™AÃ¯n Abid,Algeria,Constantine,2508309
Aflou,Algeria,Laghouat,2508737
Adrar,Algeria,Adrar,2508813
Abou el Hassan,Algeria,Chlef,2509031
BABOR - VILLE,Algeria,SÃ©tif,6698360
Zamora,Ecuador,Zamora-Chinchipe,3649959
Yaguachi Nuevo,Ecuador,Guayas,3650121
Vinces,Ecuador,Los RÃ­os,3650186
Ventanas,Ecuador,Los RÃ­os,3650267
Velasco Ibarra,Ecuador,Guayas,3650273
TulcÃ¡n,Ecuador,Carchi,3650472
Tena,Ecuador,Napo,3650721
Sucre,Ecuador,ManabÃ­,3650960
Santo Domingo de los Colorados,Ecuador,Santo Domingo de los TsÃ¡chilas,3651297
Santa Rosa,Ecuador,El Oro,3651356
Santa Elena,Ecuador,Santa Elena,3651438
San Lorenzo de Esmeraldas,Ecuador,Esmeraldas,3651694
San Gabriel,Ecuador,Carchi,3651868
SamborondÃ³n,Ecuador,Guayas,3652065
Salinas,Ecuador,Santa Elena,3652100
Rosa Zarate,Ecuador,Esmeraldas,3652257
Riobamba,Ecuador,Chimborazo,3652350
Quito,Ecuador,Pichincha,3652462
Quevedo,Ecuador,Los RÃ­os,3652567
Puyo,Ecuador,Pastaza,3652584
PujilÃ­,Ecuador,Cotopaxi,3652684
Puerto Francisco de Orellana,Ecuador,Orellana,3652743
Portoviejo,Ecuador,ManabÃ­,3652941
Playas,Ecuador,Guayas,3653015
PiÃ±as,Ecuador,El Oro,3653130
Pelileo,Ecuador,Tungurahua,3653287
Pedro Carbo,Ecuador,Guayas,3653295
Pasaje,Ecuador,El Oro,3653403
Otavalo,Ecuador,Imbabura,3653693
Naranjito,Ecuador,Guayas,3653873
Naranjal,Ecuador,Guayas,3653882
Montecristi,Ecuador,ManabÃ­,3654055
Montalvo,Ecuador,Los RÃ­os,3654064
Manta,Ecuador,ManabÃ­,3654410
Machala,Ecuador,El Oro,3654533
Machachi,Ecuador,Pichincha,3654536
Macas,Ecuador,Morona-Santiago,3654541
Loja,Ecuador,Loja,3654667
La Troncal,Ecuador,CaÃ±ar,3654853
Latacunga,Ecuador,Cotopaxi,3654870
La ManÃ¡,Ecuador,Cotopaxi,3655117
La Libertad,Ecuador,Guayas,3655131
Nueva Loja,Ecuador,Sucumbios,3655185
Jipijapa,Ecuador,ManabÃ­,3655446
Ibarra,Ecuador,Imbabura,3655673
Huaquillas,Ecuador,El Oro,3655720
Guayaquil,Ecuador,Guayas,3657509
Guaranda,Ecuador,BolÃ­var,3657571
Gualaceo,Ecuador,Azuay,3657670
Esmeraldas,Ecuador,Esmeraldas,3657990
El Triunfo,Ecuador,Guayas,3658053
Eloy Alfaro,Ecuador,Guayas,3658192
Cuenca,Ecuador,Azuay,3658666
Chone,Ecuador,ManabÃ­,3659139
Cayambe,Ecuador,Pichincha,3659578
Catamayo,Ecuador,Loja,3659599
Cariamanga,Ecuador,Loja,3659711
Calceta,Ecuador,ManabÃ­,3659926
Boca Suno,Ecuador,Orellana,3660152
Balzar,Ecuador,Guayas,3660361
BahÃ­a de CarÃ¡quez,Ecuador,ManabÃ­,3660401
Babahoyo,Ecuador,Los RÃ­os,3660418
Azogues,Ecuador,CaÃ±ar,3660434
Atuntaqui,Ecuador,Imbabura,3660478
Ambato,Ecuador,Tungurahua,3660689
Tutamandahostel,Ecuador,Pichincha,10277901
Viljandi,Estonia,Viljandimaa,587577
Tartu,Estonia,Tartu,588335
Tallinn,Estonia,Harjumaa,588409
SillamÃ¤e,Estonia,Ida-Virumaa,588686
Rakvere,Estonia,LÃ¤Ã¤ne-Virumaa,589165
PÃ¤rnu,Estonia,PÃ¤rnumaa,589580
Narva,Estonia,Ida-Virumaa,590031
Maardu,Estonia,Harjumaa,590447
Kohtla-JÃ¤rve,Estonia,Ida-Virumaa,591260
ZiftÃ¡,Egypt,Muá¸©ÄfazÌ§at al GharbÄ«yah,346030
Toukh,Egypt,Muá¸©ÄfazÌ§at al QalyÅ«bÄ«yah,347236
Tanda,Egypt,Muá¸©ÄfazÌ§at al GharbÄ«yah,347497
Å¢Ämiyah,Egypt,Muá¸©ÄfazÌ§at al FayyÅ«m,347542
Å¢alkhÄ,Egypt,Muá¸©ÄfazÌ§at ad DaqahlÄ«yah,347591
TalÄ,Egypt,Muá¸©ÄfazÌ§at al MinÅ«fÄ«yah,347612
Å¢ahÅ£Ä,Egypt,SÅ«hÄj,347634
SumusÅ£Ä as SulÅ£ÄnÄ«,Egypt,Muá¸©ÄfazÌ§at BanÄ« Suwayf,347749
Sohag,Egypt,SÅ«hÄj,347796
SÄ«dÄ« SÄlim,Egypt,Kafr ash Shaykh,348112
ShirbÄ«n,Egypt,Muá¸©ÄfazÌ§at ad DaqahlÄ«yah,349114
ShibÄ«n al QanÄÅ£ir,Egypt,Muá¸©ÄfazÌ§at al QalyÅ«bÄ«yah,349156
ShibÄ«n al Kawm,Egypt,Muá¸©ÄfazÌ§at al MinÅ«fÄ«yah,349158
SamannÅ«d,Egypt,Muá¸©ÄfazÌ§at al GharbÄ«yah,349715
SamÄlÅ«Å£,Egypt,Al MinyÄ,349717
Rosetta,Egypt,Al Buá¸©ayrah,350203
Ras Gharib,Egypt,Red Sea,350207
QuwaysinÄ,Egypt,Muá¸©ÄfazÌ§at al MinÅ«fÄ«yah,350370
QuÅ£Å«r,Egypt,Muá¸©ÄfazÌ§at al GharbÄ«yah,350376
Kousa,Egypt,QinÄ,350422
QinÄ,Egypt,QinÄ,350550
QalyÅ«b,Egypt,Muá¸©ÄfazÌ§at al QalyÅ«bÄ«yah,350789
Najâ€˜ á¸¨ammÄdÄ«,Egypt,QinÄ,351434
Minyat an NaÅŸr,Egypt,Muá¸©ÄfazÌ§at ad DaqahlÄ«yah,352344
MinÅ«f,Egypt,Muá¸©ÄfazÌ§at al MinÅ«fÄ«yah,352354
MaÅ£Äy,Egypt,Al MinyÄ,352628
MashtÅ«l as SÅ«q,Egypt,Eastern Province,352679
Mersa Matruh,Egypt,Muá¸©ÄfazÌ§at MaÅ£rÅ«á¸©,352733
ManfalÅ«Å£,Egypt,AsyÅ«Å£,352913
MallawÄ«,Egypt,Al MinyÄ,352951
MadÄ«nat Sittah UktÅ«bar,Egypt,Al JÄ«zah,353219
Kawm UmbÅ«,Egypt,AswÄn,353802
Kawm á¸¨amÄdah,Egypt,Al Buá¸©ayrah,353828
Kafr Åžaqr,Egypt,Eastern Province,354105
Kafr az ZayyÄt,Egypt,Muá¸©ÄfazÌ§at al GharbÄ«yah,354365
Kafr ash Shaykh,Egypt,Kafr ash Shaykh,354502
Kafr ad DawwÄr,Egypt,Al Buá¸©ayrah,354775
Juhaynah,Egypt,SÅ«hÄj,354981
JirjÄ,Egypt,SÅ«hÄj,355026
â€˜Izbat al Burj,Egypt,Muá¸©ÄfazÌ§at ad DaqahlÄ«yah,355392
IÅ£sÄ,Egypt,Muá¸©ÄfazÌ§at al FayyÅ«m,355420
IsnÄ,Egypt,QinÄ,355449
IdkÅ«,Egypt,Al Buá¸©ayrah,355628
IdfÅ«,Egypt,AswÄn,355635
IbshawÄy,Egypt,Muá¸©ÄfazÌ§at al FayyÅ«m,355648
á¸¨alwÄn,Egypt,Cairo Governorate,355795
HihyÄ,Egypt,Eastern Province,355939
á¸¨awsh â€˜ÄªsÃ¡,Egypt,Al Buá¸©ayrah,356000
Fuwwah,Egypt,Kafr ash Shaykh,356806
FarshÅ«Å£,Egypt,QinÄ,356933
FÄraskÅ«r,Egypt,DumyÄÅ£,356945
FÄqÅ«s,Egypt,Eastern Province,356989
Damietta,Egypt,DumyÄÅ£,358048
Diyarb Najm,Egypt,Eastern Province,358095
DisÅ«q,Egypt,Kafr ash Shaykh,358108
DishnÄ,Egypt,QinÄ,358115
Dikirnis,Egypt,Muá¸©ÄfazÌ§at ad DaqahlÄ«yah,358172
DayrÅ«Å£,Egypt,AsyÅ«Å£,358269
Dayr MawÄs,Egypt,Al MinyÄ,358274
DamanhÅ«r,Egypt,Al Buá¸©ayrah,358448
BÅ«sh,Egypt,Muá¸©ÄfazÌ§at BanÄ« Suwayf,358600
Port Said,Egypt,Muá¸©ÄfazÌ§at BÅ«r Saâ€˜Ä«d,358619
BÅ«r SafÄjah,Egypt,Red Sea,358620
BilqÄs,Egypt,Muá¸©ÄfazÌ§at ad DaqahlÄ«yah,358821
Bilbays,Egypt,Eastern Province,358840
BasyÅ«n,Egypt,Muá¸©ÄfazÌ§at al GharbÄ«yah,358970
BanÄ« Suwayf,Egypt,Muá¸©ÄfazÌ§at BanÄ« Suwayf,359173
BanÄ« MazÄr,Egypt,Al MinyÄ,359212
BanhÄ,Egypt,Muá¸©ÄfazÌ§at al QalyÅ«bÄ«yah,359280
Zagazig,Egypt,Eastern Province,359493
AwsÄ«m,Egypt,Al JÄ«zah,359576
At Tall al KabÄ«r,Egypt,Al IsmÄâ€˜Ä«lÄ«yah,359710
AsyÅ«Å£,Egypt,AsyÅ«Å£,359783
Aswan,Egypt,AswÄn,359792
Suez,Egypt,As Suways,359796
AÅŸ Åžaff,Egypt,Al JÄ«zah,359900
Ash ShuhadÄâ€™,Egypt,Muá¸©ÄfazÌ§at al MinÅ«fÄ«yah,359953
AshmÅ«n,Egypt,Muá¸©ÄfazÌ§at al MinÅ«fÄ«yah,360048
Al WÄsiÅ£ah,Egypt,Muá¸©ÄfazÌ§at al FayyÅ«m,360464
Luxor,Egypt,Luxor,360502
Al QÅ«ÅŸÄ«yah,Egypt,AsyÅ«Å£,360526
Al QuÅŸayr,Egypt,Red Sea,360531
Al Qurayn,Egypt,Eastern Province,360542
Al QanÄyÄt,Egypt,Eastern Province,360612
Al QanÄÅ£ir al KhayrÄ«yah,Egypt,Muá¸©ÄfazÌ§at al QalyÅ«bÄ«yah,360615
Cairo,Egypt,Cairo Governorate,360630
Al MinyÄ,Egypt,Al MinyÄ,360686
Al MaÅ£arÄ«yah,Egypt,Muá¸©ÄfazÌ§at ad DaqahlÄ«yah,360716
Al Manzilah,Egypt,Muá¸©ÄfazÌ§at ad DaqahlÄ«yah,360754
Al ManÅŸÅ«rah,Egypt,Muá¸©ÄfazÌ§at ad DaqahlÄ«yah,360761
Al ManshÄh,Egypt,SÅ«hÄj,360773
Al Maá¸©allah al KubrÃ¡,Egypt,Muá¸©ÄfazÌ§at al GharbÄ«yah,360829
Al KhÄrijah,Egypt,Muá¸©ÄfazÌ§at al WÄdÄ« al JadÄ«d,360923
Al KhÄnkah,Egypt,Muá¸©ÄfazÌ§at al QalyÅ«bÄ«yah,360928
Al JÄ«zah,Egypt,Al JÄ«zah,360995
Al JamÄlÄ«yah,Egypt,Muá¸©ÄfazÌ§at ad DaqahlÄ«yah,361029
Ismailia,Egypt,Al IsmÄâ€˜Ä«lÄ«yah,361055
Alexandria,Egypt,Alexandria,361058
Al IbrÄhÄ«mÄ«yah,Egypt,Eastern Province,361103
Al á¸¨awÄmidÄ«yah,Egypt,Al JÄ«zah,361179
Al á¸¨ÄmÅ«l,Egypt,Kafr ash Shaykh,361213
Hurghada,Egypt,Red Sea,361291
Al FayyÅ«m,Egypt,Muá¸©ÄfazÌ§at al FayyÅ«m,361320
Al Fashn,Egypt,Muá¸©ÄfazÌ§at BanÄ« Suwayf,361329
Al BawÄ«Å£Ä«,Egypt,Al JÄ«zah,361394
Al BalyanÄ,Egypt,SÅ«hÄj,361435
Al BÄjÅ«r,Egypt,Muá¸©ÄfazÌ§at al MinÅ«fÄ«yah,361457
Al BadÄrÄ«,Egypt,AsyÅ«Å£,361478
Al â€˜AyyÄÅ£,Egypt,Al JÄ«zah,361495
Arish,Egypt,ShamÄl SÄ«nÄÊ¼,361546
AkhmÄ«m,Egypt,SÅ«hÄj,361661
AjÄ,Egypt,Muá¸©ÄfazÌ§at ad DaqahlÄ«yah,361702
Ad DilinjÄt,Egypt,Al Buá¸©ayrah,361827
AbÅ« TÄ«j,Egypt,AsyÅ«Å£,362004
AbÅ« QurqÄÅŸ,Egypt,Al MinyÄ,362277
AbÅ« KabÄ«r,Egypt,Eastern Province,362485
AbÅ« al MaÅ£ÄmÄ«r,Egypt,Al Buá¸©ayrah,362882
AbnÅ«b,Egypt,AsyÅ«Å£,362973
Az ZarqÄ,Egypt,DumyÄÅ£,419435
Ain Sukhna,Egypt,As Suways,7521348
Smara,Western Sahara,Oued Ed-Dahab-Lagouira,2461874
LaÃ¢youne / El AaiÃºn,Western Sahara,Oued Ed-Dahab-Lagouira,2462881
Dakhla,Western Sahara,Oued Ed-Dahab-Lagouira,2463447
Massawa,Eritrea,Northern Red Sea Region,330546
Keren,Eritrea,Ä€nseba,333287
Barentu,Eritrea,Gash Barka,342711
Asmara,Eritrea,MaÊ¼Äkel,343300
Assab,Eritrea,DebubawÄ« KÊ¼eyih BahrÄ«,343386
Mendefera,Eritrea,Debub,344901
Zubia,Spain,Andalusia,2509305
Zafra,Spain,Extremadura,2509377
Yecla,Spain,Murcia,2509402
Villena,Spain,Valencia,2509463
Villarrobledo,Spain,Castille-La Mancha,2509491
Vila-real,Spain,Valencia,2509509
Villanueva de la Serena,Spain,Extremadura,2509553
Villajoyosa,Spain,Valencia,2509588
VÃ­car,Spain,Andalusia,2509650
VÃ©lez-MÃ¡laga,Spain,Andalusia,2509769
Valencia,Spain,Valencia,2509954
ValdepeÃ±as,Spain,Castille-La Mancha,2509982
Utrera,Spain,Andalusia,2510073
Ubrique,Spain,Andalusia,2510112
Ãšbeda,Spain,Andalusia,2510116
Totana,Spain,Murcia,2510224
Torrox,Spain,Andalusia,2510245
Torrevieja,Spain,Valencia,2510253
Torre-Pacheco,Spain,Murcia,2510271
Torrent,Spain,Valencia,2510279
Torremolinos,Spain,Andalusia,2510281
Tomelloso,Spain,Castille-La Mancha,2510392
Tomares,Spain,Andalusia,2510394
Toledo,Spain,Castille-La Mancha,2510409
TÃ­as,Spain,Canary Islands,2510485
Telde,Spain,Canary Islands,2510542
Teguise,Spain,Canary Islands,2510573
Tarifa,Spain,Andalusia,2510599
Talavera de la Reina,Spain,Castille-La Mancha,2510693
Tacoronte,Spain,Canary Islands,2510725
Tavernes de la Valldigna,Spain,Valencia,2510743
Sueca,Spain,Valencia,2510764
Silla,Spain,Valencia,2510880
Sevilla,Spain,Andalusia,2510911
San Vicent del Raspeig,Spain,Valencia,2511032
Santomera,Spain,Murcia,2511050
Santa Pola,Spain,Valencia,2511102
Santa LucÃ­a,Spain,Canary Islands,2511150
SantafÃ©,Spain,Andalusia,2511160
Santa EulÃ ria des Riu,Spain,Balearic Islands,2511162
Santa Cruz de Tenerife,Spain,Canary Islands,2511174
Santa Cruz de la Palma,Spain,Canary Islands,2511180
Santa BrÃ­gida,Spain,Canary Islands,2511202
San Roque,Spain,Andalusia,2511239
San Pedro del Pinatar,Spain,Murcia,2511247
San Pedro de AlcÃ¡ntara,Spain,Andalusia,2511250
San Miguel De Abona,Spain,Canary Islands,2511287
SanlÃºcar de Barrameda,Spain,Andalusia,2511306
San Juan de Aznalfarache,Spain,Andalusia,2511329
San Juan de Alicante,Spain,Valencia,2511330
San Javier,Spain,Murcia,2511366
San Isidro,Spain,Canary Islands,2511371
San Fernando,Spain,Andalusia,2511388
La Laguna,Spain,Canary Islands,2511401
San BartolomÃ© de Tirajana,Spain,Canary Islands,2511440
San BartolomÃ©,Spain,Canary Islands,2511447
Sant Antoni de Portmany,Spain,Balearic Islands,2511448
Sagunto,Spain,Valencia,2511619
Rota,Spain,Andalusia,2511700
Roquetas de Mar,Spain,Andalusia,2511716
Ronda,Spain,Andalusia,2511730
Rojales,Spain,Valencia,2511752
RincÃ³n de la Victoria,Spain,Andalusia,2511852
Ribarroja,Spain,Valencia,2511880
Requena,Spain,Valencia,2511930
Realejo Alto,Spain,Canary Islands,2511994
PuÃ§ol,Spain,Valencia,2512127
Puerto Real,Spain,Andalusia,2512169
Puertollano,Spain,Castille-La Mancha,2512177
Puerto del Rosario,Spain,Canary Islands,2512186
Puerto de la Cruz,Spain,Canary Islands,2512196
Puente-Genil,Spain,Andalusia,2512232
La Pobla de Vallbona,Spain,Valencia,2512251
Priego de CÃ³rdoba,Spain,Andalusia,2512282
Pozoblanco,Spain,Andalusia,2512340
PollenÃ§a,Spain,Balearic Islands,2512432
Pilar de la Horadada,Spain,Valencia,2512581
Picassent,Spain,Valencia,2512620
Paterna,Spain,Valencia,2512862
Palma,Spain,Balearic Islands,2512989
Palma del RÃ­o,Spain,Andalusia,2512990
PÃ¡jara,Spain,Canary Islands,2513026
Paiporta,Spain,Valencia,2513029
Osuna,Spain,Andalusia,2513052
Orihuela,Spain,Valencia,2513076
Ontinyent,Spain,Valencia,2513106
Onda,Spain,Valencia,2513115
Oliva,Spain,Valencia,2513145
Novelda,Spain,Valencia,2513195
NÃ­jar,Spain,Andalusia,2513222
Nerja,Spain,Andalusia,2513240
Navalmoral de la Mata,Spain,Extremadura,2513324
Murcia,Spain,Murcia,2513416
Mula,Spain,Murcia,2513436
Muchamiel,Spain,Valencia,2513465
Motril,Spain,Andalusia,2513477
MorÃ³n de la Frontera,Spain,Andalusia,2513509
Montilla,Spain,Andalusia,2513601
Montijo,Spain,Extremadura,2513604
Moncada,Spain,Valencia,2513703
Molina de Segura,Spain,Murcia,2513759
Moguer,Spain,Andalusia,2513791
MogÃ¡n,Spain,Canary Islands,2513798
Mislata,Spain,Valencia,2513811
Mijas,Spain,Andalusia,2513882
MÃ©rida,Spain,Extremadura,2513917
Melilla,Spain,Melilla,2513947
MazarrÃ³n,Spain,Murcia,2513983
Maspalomas,Spain,Canary Islands,2514042
Massamagrell,Spain,Valencia,2514066
Martos,Spain,Andalusia,2514073
MarratxÃ­,Spain,Balearic Islands,2514097
Marchena,Spain,Andalusia,2514158
Marbella,Spain,Andalusia,2514169
Maracena,Spain,Andalusia,2514176
Manzanares,Spain,Castille-La Mancha,2514190
Manises,Spain,Valencia,2514197
Manacor,Spain,Balearic Islands,2514216
MÃ¡laga,Spain,Andalusia,2514256
Mairena del Aljarafe,Spain,Andalusia,2514287
Mairena del Alcor,Spain,Andalusia,2514288
MaÃ³,Spain,Balearic Islands,2514301
Lucena,Spain,Andalusia,2514392
Los Palacios y Villafranca,Spain,Andalusia,2514553
Los Llanos de Aridane,Spain,Canary Islands,2514651
Los Barrios,Spain,Andalusia,2514824
Los AlcÃ¡zares,Spain,Murcia,2514868
Lorca,Spain,Murcia,2514891
Lora del RÃ­o,Spain,Andalusia,2514893
Loja,Spain,Andalusia,2514946
Llucmajor,Spain,Balearic Islands,2514984
LlÃ­ria,Spain,Valencia,2515036
Linares,Spain,Andalusia,2515045
Lepe,Spain,Andalusia,2515072
Lebrija,Spain,Andalusia,2515096
La UniÃ³n,Spain,Murcia,2515151
Las Torres de Cotillas,Spain,Murcia,2515219
Las Palmas de Gran Canaria,Spain,Canary Islands,2515270
La Solana,Spain,Castille-La Mancha,2515284
Las Cabezas de San Juan,Spain,Andalusia,2515493
La Roda,Spain,Castille-La Mancha,2515555
La Rinconada,Spain,Andalusia,2515562
La Orotava,Spain,Canary Islands,2515692
La Oliva,Spain,Canary Islands,2515698
la Nucia,Spain,Valencia,2515701
La LÃ­nea de la ConcepciÃ³n,Spain,Andalusia,2515812
L'Eliana,Spain,Valencia,2516004
La Carolina,Spain,Andalusia,2516088
Jumilla,Spain,Murcia,2516255
Jerez de la Frontera,Spain,Andalusia,2516326
Javea,Spain,Valencia,2516336
XÃ tiva,Spain,Valencia,2516345
JaÃ©n,Spain,Andalusia,2516395
Isla Cristina,Spain,Andalusia,2516431
Ingenio,Spain,Canary Islands,2516443
Inca,Spain,Balearic Islands,2516452
Icod de los Vinos,Spain,Canary Islands,2516474
Ibiza,Spain,Balearic Islands,2516479
Ibi,Spain,Valencia,2516480
HuÃ©rcal-Overa,Spain,Andalusia,2516542
Huelva,Spain,Andalusia,2516548
HellÃ­n,Spain,Castille-La Mancha,2516797
GÃ¼imar,Spain,Canary Islands,2516852
GuÃ­a de Isora,Spain,Canary Islands,2516860
Guardamar del Segura,Spain,Valencia,2516902
Guadix,Spain,Andalusia,2516925
Granadilla de Abona,Spain,Canary Islands,2517111
Granada,Spain,Andalusia,2517117
Gandia,Spain,Valencia,2517367
GÃ¡ldar,Spain,Canary Islands,2517436
Fuengirola,Spain,Andalusia,2517595
Felanitx,Spain,Balearic Islands,2517750
Estepona,Spain,Andalusia,2517816
El Viso del Alcor,Spain,Andalusia,2518040
El Puerto de Santa MarÃ­a,Spain,Andalusia,2518207
El Ejido,Spain,Andalusia,2518494
Elda,Spain,Valencia,2518505
Elche,Spain,Valencia,2518559
El Arahal,Spain,Andalusia,2518729
Ã‰cija,Spain,Andalusia,2518770
Dos Hermanas,Spain,Andalusia,2518794
Don Benito,Spain,Extremadura,2518820
Denia,Spain,Valencia,2518878
Daimiel,Spain,Castille-La Mancha,2518924
Cullera,Spain,Valencia,2518949
Quart de Poblet,Spain,Valencia,2519068
Crevillente,Spain,Valencia,2519110
Coria del RÃ­o,Spain,Andalusia,2519233
CÃ³rdoba,Spain,Andalusia,2519240
Conil de la Frontera,Spain,Andalusia,2519289
CoÃ­n,Spain,Andalusia,2519367
Ciudad Real,Spain,Castille-La Mancha,2519402
Cieza,Spain,Murcia,2519425
Xirivella,Spain,Valencia,2519466
Chipiona,Spain,Andalusia,2519477
Chiclana de la Frontera,Spain,Andalusia,2519513
CehegÃ­n,Spain,Murcia,2519651
Catarroja,Spain,Valencia,2519690
Castilleja de la Cuesta,Spain,Andalusia,2519738
CastellÃ³ de la Plana,Spain,Valencia,2519752
Cartaya,Spain,Andalusia,2520052
CÃ¡rtama,Spain,Andalusia,2520055
Cartagena,Spain,Murcia,2520058
Carmona,Spain,Andalusia,2520118
Carlet,Spain,Valencia,2520121
Carcaixent,Spain,Valencia,2520150
Caravaca,Spain,Murcia,2520171
Candelaria,Spain,Canary Islands,2520283
Campo de Criptana,Spain,Castille-La Mancha,2520413
CampiÃ±a,Spain,Andalusia,2520425
el Campello,Spain,Valencia,2520447
Camas,Spain,Andalusia,2520477
CalviÃ ,Spain,Balearic Islands,2520493
Calp,Spain,Valencia,2520496
Callosa de Segura,Spain,Valencia,2520502
Cadiz,Spain,Andalusia,2520600
CÃ¡ceres,Spain,Extremadura,2520611
Cabra,Spain,Andalusia,2520645
Burriana,Spain,Valencia,2520709
Burjassot,Spain,Valencia,2520712
Bormujos,Spain,Andalusia,2520833
BÃ©tera,Spain,Valencia,2520968
Berja,Spain,Andalusia,2521016
Benidorm,Spain,Valencia,2521088
BenetÃºsser,Spain,Valencia,2521105
BenalmÃ¡dena,Spain,Andalusia,2521139
Baza,Spain,Andalusia,2521215
Barbate de Franco,Spain,Andalusia,2521335
BailÃ©n,Spain,Andalusia,2521410
Baeza,Spain,Andalusia,2521413
Baena,Spain,Andalusia,2521415
Badajoz,Spain,Extremadura,2521420
Ayamonte,Spain,Andalusia,2521456
Atarfe,Spain,Andalusia,2521485
AtamarÃ­a,Spain,Murcia,2521486
Aspe,Spain,Valencia,2521510
Arucas,Spain,Canary Islands,2521519
Arrecife,Spain,Canary Islands,2521570
Arona,Spain,Canary Islands,2521582
Armilla,Spain,Andalusia,2521590
Arcos de la Frontera,Spain,Andalusia,2521665
Archena,Spain,Murcia,2521676
Antequera,Spain,Andalusia,2521710
AndÃºjar,Spain,Andalusia,2521738
Altea,Spain,Valencia,2521804
AlmuÃ±Ã©car,Spain,Andalusia,2521847
AlmoradÃ­,Spain,Valencia,2521855
Almonte,Spain,Andalusia,2521857
AlmerÃ­a,Spain,Andalusia,2521886
Almendralejo,Spain,Extremadura,2521893
Almassora,Spain,Valencia,2521909
Almansa,Spain,Castille-La Mancha,2521923
Aljaraque,Spain,Andalusia,2521964
Alicante,Spain,Valencia,2521978
AlhaurÃ­n el Grande,Spain,Andalusia,2521985
AlhaurÃ­n de la Torre,Spain,Andalusia,2521986
Alhama de Murcia,Spain,Murcia,2521992
AlgemesÃ­,Spain,Valencia,2522012
Algeciras,Spain,Andalusia,2522013
Alfafar,Spain,Valencia,2522057
Aldaia,Spain,Valencia,2522077
AlcÃºdia,Spain,Balearic Islands,2522091
Alcoy,Spain,Valencia,2522098
Alzira,Spain,Valencia,2522129
AlcÃ¡zar de San Juan,Spain,Castille-La Mancha,2522131
Alcantarilla,Spain,Murcia,2522152
AlcalÃ¡ la Real,Spain,Andalusia,2522160
AlcalÃ¡ de Guadaira,Spain,Andalusia,2522165
Alboraya,Spain,Valencia,2522203
Albolote,Spain,Andalusia,2522208
Albal,Spain,Valencia,2522250
Albacete,Spain,Castille-La Mancha,2522258
AlaquÃ s,Spain,Valencia,2522297
AgÃ¼imes,Spain,Canary Islands,2522325
Ãguilas,Spain,Murcia,2522333
Adra,Spain,Andalusia,2522430
Adeje,Spain,Canary Islands,2522437
Groa de Murviedro,Spain,Valencia,2567529
Zarautz,Spain,Basque Country,3104316
Zaragoza,Spain,Aragon,3104324
Zamora,Spain,Castille and LeÃ³n,3104342
Viveiro,Spain,Galicia,3104475
Gasteiz / Vitoria,Spain,Basque Country,3104499
VinarÃ²s,Spain,Valencia,3104584
Villaviciosa de OdÃ³n,Spain,Madrid,3104703
Villaverde,Spain,Madrid,3104748
Villaquilambre,Spain,Castille and LeÃ³n,3105148
Vilanova i la GeltrÃº,Spain,Catalonia,3105184
Villanueva del Pardillo,Spain,Madrid,3105214
Villanueva de la CaÃ±ada,Spain,Madrid,3105247
Vilalba,Spain,Galicia,3105522
VilagarcÃ­a de Arousa,Spain,Galicia,3105575
Vilafranca del PenedÃ¨s,Spain,Catalonia,3105600
Vila-seca,Spain,Catalonia,3105803
Vilaseca,Spain,Catalonia,3105805
Viladecans,Spain,Catalonia,3105935
Vigo,Spain,Galicia,3105976
Vic,Spain,Catalonia,3106050
VicÃ¡lvaro,Spain,Madrid,3106054
El Vendrell,Spain,Catalonia,3106180
Valls,Spain,Catalonia,3106492
Valladolid,Spain,Castille and LeÃ³n,3106672
Valdemoro,Spain,Madrid,3106868
Rivas-Vaciamadrid,Spain,Madrid,3107112
Utebo,Spain,Aragon,3107139
Tui,Spain,Galicia,3107364
Tudela,Spain,Navarre,3107418
Tortosa,Spain,Catalonia,3107677
Torrelodones,Spain,Madrid,3107765
Torrelavega,Spain,Cantabria,3107775
TorrejÃ³n de Ardoz,Spain,Madrid,3107784
Torredembarra,Spain,Catalonia,3107807
Tordera,Spain,Catalonia,3107955
Tolosa,Spain,Basque Country,3108008
TetuÃ¡n de las Victorias,Spain,Madrid,3108118
Teruel,Spain,Aragon,3108126
Teo,Spain,Galicia,3108165
TÃ rrega,Spain,Catalonia,3108285
Terrassa,Spain,Catalonia,3108286
Tarragona,Spain,Catalonia,3108288
TarancÃ³n,Spain,Castille-La Mancha,3108317
Soria,Spain,Castille and LeÃ³n,3108681
Sitges,Spain,Catalonia,3108877
Sestao,Spain,Basque Country,3109041
SeseÃ±a,Spain,Castille-La Mancha,3109050
Segovia,Spain,Castille and LeÃ³n,3109256
Cerdanyola del VallÃ¨s,Spain,Catalonia,3109402
Sant VicenÃ§ dels Horts,Spain,Catalonia,3109442
Barakaldo,Spain,Basque Country,3109453
Santurtzi,Spain,Basque Country,3109481
Sant Just Desvern,Spain,Catalonia,3109546
Santiago de Compostela,Spain,Galicia,3109642
Santa PerpÃ¨tua de Mogoda,Spain,Catalonia,3109689
Santander,Spain,Cantabria,3109718
BarberÃ  del VallÃ¨s,Spain,Catalonia,3109804
Santa Coloma de Gramenet,Spain,Catalonia,3109981
San SebastiÃ¡n de los Reyes,Spain,Madrid,3110040
Donostia / San SebastiÃ¡n,Spain,Basque Country,3110044
Sant Quirze del VallÃ¨s,Spain,Catalonia,3110101
Sant Pere de Ribes,Spain,Catalonia,3110143
San MartÃ­n de la Vega,Spain,Madrid,3110360
San Lorenzo de El Escorial,Spain,Madrid,3110458
Vilassar de Mar,Spain,Catalonia,3110516
Sant Joan DespÃ­,Spain,Catalonia,3110519
Sanxenxo,Spain,Galicia,3110610
San Fernando de Henares,Spain,Madrid,3110627
Sant Feliu de Llobregat,Spain,Catalonia,3110642
Sant Feliu de GuÃ­xols,Spain,Catalonia,3110643
Sant Cugat del VallÃ¨s,Spain,Catalonia,3110718
Sant Celoni,Spain,Catalonia,3110813
Sant Carles de la RÃ pita,Spain,Catalonia,3110821
Sant Boi de Llobregat,Spain,Catalonia,3110834
Sant Andreu de Palomar,Spain,Catalonia,3110876
San AndrÃ©s del Rabanedo,Spain,Castille and LeÃ³n,3110880
Sant Andreu de la Barca,Spain,Catalonia,3110885
Sant AdriÃ  de BesÃ²s,Spain,Catalonia,3110921
Sama,Spain,Asturias,3110962
Salt,Spain,Catalonia,3110983
Salou,Spain,Catalonia,3110986
Salamanca,Spain,Castille and LeÃ³n,3111108
Sabadell,Spain,Catalonia,3111199
RubÃ­,Spain,Catalonia,3111294
Roses,Spain,Catalonia,3111348
Ripollet,Spain,Catalonia,3111605
Ribeira,Spain,Galicia,3111807
Reus,Spain,Catalonia,3111933
Errenteria,Spain,Basque Country,3112011
Redondela,Spain,Galicia,3112154
Puente de Vallecas,Spain,Madrid,3112737
Ponteareas,Spain,Galicia,3112761
PremiÃ  de Mar,Spain,Catalonia,3112866
Pozuelo de AlarcÃ³n,Spain,Madrid,3112989
Poio,Spain,Galicia,3113035
Portugalete,Spain,Basque Country,3113082
PorriÃ±o,Spain,Galicia,3113157
Pontevedra,Spain,Galicia,3113209
Ponferrada,Spain,Castille and LeÃ³n,3113236
Plasencia,Spain,Extremadura,3113331
Pinto,Spain,Madrid,3113415
Pineda de Mar,Spain,Catalonia,3113526
Parla,Spain,Madrid,3114256
Parets del VallÃ¨s,Spain,Catalonia,3114267
Pamplona,Spain,Navarre,3114472
Palencia,Spain,Castille and LeÃ³n,3114531
PalamÃ³s,Spain,Catalonia,3114566
Palafrugell,Spain,Catalonia,3114567
Oviedo,Spain,Asturias,3114711
Oria,Spain,Basque Country,3114957
Ourense,Spain,Galicia,3114965
Olot,Spain,Catalonia,3115093
Olesa de Montserrat,Spain,Catalonia,3115171
Oleiros,Spain,Galicia,3115177
NigrÃ¡n,Spain,Galicia,3115463
Navalcarnero,Spain,Madrid,3115659
NarÃ³n,Spain,Galicia,3115739
Mungia,Spain,Basque Country,3115907
MÃ³stoles,Spain,Madrid,3116025
Moratalaz,Spain,Madrid,3116156
MonzÃ³n,Spain,Aragon,3116224
MontornÃ¨s del VallÃ¨s,Spain,Catalonia,3116262
Monforte de Lemos,Spain,Galicia,3116478
Arrasate / MondragÃ³n,Spain,Basque Country,3116503
Montcada i Reixac,Spain,Catalonia,3116527
Mollet del VallÃ¨s,Spain,Catalonia,3116553
Molins de Rei,Spain,Catalonia,3116562
MoaÃ±a,Spain,Galicia,3116653
Miranda de Ebro,Spain,Castille and LeÃ³n,3116689
Mieres,Spain,Asturias,3116789
Mejorada del Campo,Spain,Madrid,3116963
Medina del Campo,Spain,Castille and LeÃ³n,3117010
MatarÃ³,Spain,Catalonia,3117164
El Masnou,Spain,Catalonia,3117232
Martorell,Spain,Catalonia,3117331
MarÃ­n,Spain,Galicia,3117409
Manresa,Spain,Catalonia,3117533
Manlleu,Spain,Catalonia,3117539
Malgrat de Mar,Spain,Catalonia,3117636
Majadahonda,Spain,Madrid,3117667
Madrid,Spain,Madrid,3117735
Lugo,Spain,Galicia,3117814
LogroÃ±o,Spain,La Rioja,3118150
Lloret de Mar,Spain,Catalonia,3118212
Laudio / Llodio,Spain,Basque Country,3118228
Lleida,Spain,Catalonia,3118514
LeÃ³n,Spain,Castille and LeÃ³n,3118532
Leioa,Spain,Basque Country,3118554
LeganÃ©s,Spain,Madrid,3118594
Las Rozas de Madrid,Spain,Madrid,3118848
Lasarte,Spain,Basque Country,3119027
La Pineda,Spain,Catalonia,3119231
LalÃ­n,Spain,Galicia,3119536
Laguna de Duero,Spain,Castille and LeÃ³n,3119631
A Estrada,Spain,Galicia,3119746
A CoruÃ±a,Spain,Galicia,3119841
Irun,Spain,Basque Country,3120304
Illescas,Spain,Castille-La Mancha,3120410
Igualada,Spain,Catalonia,3120431
Humanes de Madrid,Spain,Madrid,3120501
Huesca,Spain,Aragon,3120514
L'Hospitalet de Llobregat,Spain,Catalonia,3120619
Hortaleza,Spain,Madrid,3120635
Hernani,Spain,Basque Country,3120811
Gernika-Lumo,Spain,Basque Country,3120989
Getxo,Spain,Basque Country,3121007
Guadalajara,Spain,Castille-La Mancha,3121070
Granollers,Spain,Catalonia,3121145
GrÃ cia,Spain,Catalonia,3121245
GijÃ³n,Spain,Asturias,3121424
Getafe,Spain,Madrid,3121437
Girona,Spain,Catalonia,3121456
GavÃ ,Spain,Catalonia,3121519
Galdakao,Spain,Basque Country,3121751
Galapagar,Spain,Madrid,3121766
Hondarribia,Spain,Basque Country,3121881
Fuenlabrada,Spain,Madrid,3121960
Figueras,Spain,Asturias,3122452
Figueres,Spain,Catalonia,3122453
Esplugues de Llobregat,Spain,Catalonia,3122826
Esparreguera,Spain,Catalonia,3122912
Ermua,Spain,Basque Country,3123063
Erandio,Spain,Basque Country,3123104
El Prat de Llobregat,Spain,Catalonia,3123329
Ferrol,Spain,Galicia,3123493
El Astillero,Spain,Cantabria,3123667
Ejea de los Caballeros,Spain,Aragon,3123688
Eibar,Spain,Basque Country,3123709
Durango,Spain,Basque Country,3123773
Culleredo,Spain,Galicia,3124041
Cuenca,Spain,Castille-La Mancha,3124132
Coslada,Spain,Madrid,3124408
CornellÃ  de Llobregat,Spain,Catalonia,3124569
Colmenar Viejo,Spain,Madrid,3124765
Collado-Villalba,Spain,Madrid,3124794
Ciudad Lineal,Spain,Madrid,3124964
Ciutadella,Spain,Balearic Islands,3124967
Ciempozuelos,Spain,Madrid,3125082
ChamartÃ­n,Spain,Madrid,3125239
Castro-Urdiales,Spain,Cantabria,3125621
Castelldefels,Spain,Catalonia,3125897
Castellar del VallÃ¨s,Spain,Catalonia,3125915
Cardedeu,Spain,Catalonia,3126317
Carballo,Spain,Galicia,3126369
Canovelles,Spain,Catalonia,3126534
Cangas do Morrazo,Spain,Galicia,3126577
Cambrils,Spain,Catalonia,3126888
Cambre,Spain,Galicia,3126890
Camargo,Spain,Cantabria,3126917
Calella,Spain,Catalonia,3127007
Caldes de Montbui,Spain,Catalonia,3127035
Calatayud,Spain,Aragon,3127047
Calahorra,Spain,La Rioja,3127065
Calafell,Spain,Catalonia,3127066
Burlata,Spain,Navarre,3127451
Burgos,Spain,Castille and LeÃ³n,3127461
Boiro,Spain,Galicia,3127889
Boadilla del Monte,Spain,Madrid,3127958
Blanes,Spain,Catalonia,3127978
Bilbao,Spain,Basque Country,3128026
Bermeo,Spain,Basque Country,3128174
Berga,Spain,Catalonia,3128201
BenicÃ ssim,Spain,Valencia,3128272
BenicarlÃ³,Spain,Valencia,3128273
Benavente,Spain,Castille and LeÃ³n,3128291
BÃ©jar,Spain,Castille and LeÃ³n,3128382
Barcelona,Spain,Catalonia,3128760
Barbastro,Spain,Aragon,3128795
BaraÃ±Ã¡in,Spain,Navarre,3128824
Barajas de Madrid,Spain,Madrid,3128832
Banyoles,Spain,Catalonia,3128885
Balaguer,Spain,Catalonia,3128978
Badalona,Spain,Catalonia,3129028
Azuqueca de Henares,Spain,Castille-La Mancha,3129046
AvilÃ©s,Spain,Asturias,3129135
Ãvila,Spain,Castille and LeÃ³n,3129136
Arteixo,Spain,Galicia,3129329
Arganda,Spain,Madrid,3129636
Aranjuez,Spain,Madrid,3129857
Aranda de Duero,Spain,Castille and LeÃ³n,3129877
Amposta,Spain,Catalonia,3130131
Amorebieta,Spain,Basque Country,3130137
AmÃ©s,Spain,Galicia,3130155
Algorta,Spain,Basque Country,3130380
Algete,Spain,Madrid,3130383
AlcorcÃ³n,Spain,Madrid,3130564
Alcobendas,Spain,Madrid,3130583
AlcaÃ±iz,Spain,Aragon,3130606
AlcalÃ¡ de Henares,Spain,Madrid,3130616
Nou Barris,Spain,Catalonia,6252065
Pinar de ChamartÃ­n,Spain,Madrid,6324376
Playa del Ingles,Spain,Canary Islands,6354969
Puerto del Carmen,Spain,Canary Islands,6355013
Ceuta,Spain,Ceuta,6362987
Moncloa-Aravaca,Spain,Madrid,6544099
Eixample,Spain,Catalonia,6544100
les Corts,Spain,Catalonia,6544101
SarriÃ -Sant Gervasi,Spain,Catalonia,6544102
Horta-GuinardÃ³,Spain,Catalonia,6544103
Sants-MontjuÃ¯c,Spain,Catalonia,6544104
Sant MartÃ­,Spain,Catalonia,6544105
Ciutat Vella,Spain,Catalonia,6544106
Arganzuela,Spain,Madrid,6544487
San Blas,Spain,Madrid,6544488
Latina,Spain,Madrid,6544489
Usera,Spain,Madrid,6544490
Salamanca,Spain,Madrid,6544491
ChamberÃ­,Spain,Madrid,6544492
Carabanchel,Spain,Madrid,6544493
City Center,Spain,Madrid,6544494
Retiro,Spain,Madrid,6544495
l'AlfÃ s del Pi,Spain,Valencia,6559503
Las Gabias,Spain,Andalusia,6559641
Delicias,Spain,Aragon,6615440
Almozara,Spain,Aragon,6615442
Montecanal,Spain,Aragon,6615443
Oliver-Valdefierro,Spain,Aragon,6615444
Santutxu,Spain,Basque Country,6618856
Los Realejos,Spain,Canary Islands,6692471
Pasaia,Spain,Basque Country,6693088
Basauri,Spain,Basque Country,6697039
LlefiÃ ,Spain,Catalonia,6943537
Corvera de Asturias,Spain,Asturias,7115111
Tres Cantos,Spain,Madrid,7577022
Iturrama,Spain,Navarre,8050879
ErmitagaÃ±a,Spain,Navarre,8050880
Primer Ensanche,Spain,Navarre,8050888
Segundo Ensanche,Spain,Navarre,8050889
Fuencarral-El Pardo,Spain,Madrid,8285534
Villa de Vallecas,Spain,Madrid,8285535
Natahoyo,Spain,Asturias,8629192
Ziway,Ethiopia,Oromiya,325579
Yirga â€˜Alem,Ethiopia,"Southern Nations, Nationalities, and People's Region",325780
YabÄ“lo,Ethiopia,Oromiya,326036
Werota,Ethiopia,Amhara,326206
WenjÄ«,Ethiopia,Oromiya,326308
Tippi,Ethiopia,"Southern Nations, Nationalities, and People's Region",327694
ShashemenÄ“,Ethiopia,Oromiya,328689
Shambu,Ethiopia,Oromiya,328709
ShakÄ«so,Ethiopia,Oromiya,328716
Sebeta,Ethiopia,Oromiya,329114
RobÄ«t,Ethiopia,Amhara,329586
Nejo,Ethiopia,Oromiya,330120
NazrÄ“t,Ethiopia,Oromiya,330186
Mojo,Ethiopia,Oromiya,330491
Metu,Ethiopia,Oromiya,330764
MetahÄra,Ethiopia,Oromiya,330811
MendÄ«,Ethiopia,Oromiya,331038
Mekele,Ethiopia,Tigray,331180
Maychâ€™ew,Ethiopia,Tigray,331416
Korem,Ethiopia,Tigray,332746
Kâ€™olÄ«to,Ethiopia,"Southern Nations, Nationalities, and People's Region",332880
Kibre Mengist,Ethiopia,Oromiya,333103
KemisÄ“,Ethiopia,Amhara,333356
Kombolcha,Ethiopia,Amhara,333373
Jinka,Ethiopia,"Southern Nations, Nationalities, and People's Region",333750
JÄ«ma,Ethiopia,Oromiya,333772
Jijiga,Ethiopia,Somali,333795
Inda SilasÄ“,Ethiopia,Tigray,334227
Harar,Ethiopia,Harari,335035
HÄgere Hiywet,Ethiopia,Oromiya,335288
Gondar,Ethiopia,Amhara,336014
Goba,Ethiopia,Oromiya,336350
Waliso,Ethiopia,Oromiya,336372
Ginir,Ethiopia,Oromiya,336454
Gimbi,Ethiopia,Oromiya,336496
Genet,Ethiopia,Oromiya,336931
Gelemso,Ethiopia,Oromiya,337010
Gebre Guracha,Ethiopia,Oromiya,337152
GambÄ“la,Ethiopia,Gambela,337405
Finote Selam,Ethiopia,Amhara,337712
FichÄ“,Ethiopia,Oromiya,337771
Felege Neway,Ethiopia,"Southern Nations, Nationalities, and People's Region",337853
Dubti,Ethiopia,Ä€far,338554
Dodola,Ethiopia,Oromiya,338726
Dire Dawa,Ethiopia,Dire Dawa,338832
DÄ«la,Ethiopia,"Southern Nations, Nationalities, and People's Region",338998
DesÄ“,Ethiopia,Amhara,339219
DembÄ« Dolo,Ethiopia,Oromiya,339448
Bishoftu,Ethiopia,Oromiya,339666
Debre Tabor,Ethiopia,Amhara,339686
Debre Markâ€™os,Ethiopia,Amhara,339708
Debre Birhan,Ethiopia,Amhara,339734
Debarkâ€™,Ethiopia,Amhara,339823
ButajÄ«ra,Ethiopia,"Southern Nations, Nationalities, and People's Region",341297
BurÄ“,Ethiopia,Amhara,341397
Bonga,Ethiopia,"Southern Nations, Nationalities, and People's Region",341742
BodÄ«tÄ«,Ethiopia,"Southern Nations, Nationalities, and People's Region",341877
Bichena,Ethiopia,Amhara,342190
BedÄ“sa,Ethiopia,Oromiya,342559
BedelÄ“,Ethiopia,Oromiya,342567
BatÄ«,Ethiopia,Amhara,342641
Bako,Ethiopia,"Southern Nations, Nationalities, and People's Region",342856
Bahir Dar,Ethiopia,Amhara,342884
Hawassa,Ethiopia,"Southern Nations, Nationalities, and People's Region",343137
Ä€sosa,Ethiopia,BÄ«nshangul Gumuz,343292
Ä€sbe TeferÄ«,Ethiopia,Oromiya,343402
Asaita,Ethiopia,Ä€far,343409
Ä€sasa,Ethiopia,Oromiya,343413
Ä€reka,Ethiopia,"Southern Nations, Nationalities, and People's Region",343593
Ä€rba Minchâ€™,Ethiopia,"Southern Nations, Nationalities, and People's Region",343663
Axum,Ethiopia,Tigray,344420
Hagere Maryam,Ethiopia,Oromiya,344620
Ä€garo,Ethiopia,Oromiya,344661
Ä€dÄ«s Zemen,Ethiopia,Amhara,344923
Addis Ababa,Ethiopia,Ä€dÄ«s Ä€beba,344979
Ä€dÄ«grat,Ethiopia,Tigray,345149
Addiet Canna,Ethiopia,Amhara,345353
Abomsa,Ethiopia,Amhara,345704
YlÃ¶jÃ¤rvi,Finland,Pirkanmaa,630752
Vihti,Finland,Uusimaa,631707
Varkaus,Finland,Northern Savo,632370
Vantaa,Finland,Uusimaa,632453
Valkeakoski,Finland,Pirkanmaa,632672
Vaasa,Finland,Ostrobothnia,632978
Uusikaupunki,Finland,Southwest Finland,633221
Tuusula,Finland,Uusimaa,633591
Turku,Finland,Southwest Finland,633679
Tornio,Finland,Lapland,634093
Tampere,Finland,Pirkanmaa,634963
SiilinjÃ¤rvi,Finland,Northern Savo,636947
Sibbo,Finland,Uusimaa,637067
SeinÃ¤joki,Finland,Southern Ostrobothnia,637219
Savonlinna,Finland,Southern Savonia,637292
Salo,Finland,Southwest Finland,637948
Rovaniemi,Finland,Lapland,638936
RiihimÃ¤ki,Finland,HÃ¤me,639406
Rauma,Finland,Satakunta,639734
Raisio,Finland,Southwest Finland,640124
Raahe,Finland,Northern Ostrobothnia,640276
Pori,Finland,Satakunta,640999
Pirkkala,Finland,Pirkanmaa,641489
Oulu,Finland,Northern Ostrobothnia,643492
NurmijÃ¤rvi,Finland,Uusimaa,644171
Nokia,Finland,Pirkanmaa,644450
Mikkeli,Finland,Southern Savonia,646005
MÃ¤ntsÃ¤lÃ¤,Finland,Uusimaa,646723
Lovisa,Finland,Uusimaa,647571
Lohja,Finland,Uusimaa,647751
Lieto,Finland,Southwest Finland,648056
LempÃ¤Ã¤lÃ¤,Finland,Pirkanmaa,648366
Laukaa,Finland,Central Finland,648738
Lappeenranta,Finland,South Karelia,648900
Lahti,Finland,PÃ¤ijÃ¤nne Tavastia,649360
Kirkkonummi,Finland,Uusimaa,649630
Kuusamo,Finland,Northern Ostrobothnia,649924
Kuopio,Finland,Northern Savo,650224
Kouvola,Finland,Kymenlaakso,650859
Kotka,Finland,Kymenlaakso,650946
Korsholm,Finland,Ostrobothnia,651299
Kokkola,Finland,Central Ostrobothnia,651943
Kerava,Finland,Uusimaa,653185
Kemi,Finland,Lapland,653281
Karhula,Finland,Kymenlaakso,654137
Kangasala,Finland,Pirkanmaa,654440
Kajaani,Finland,Kainuu,654899
Kaarina,Finland,Southwest Finland,655130
JyvÃ¤skylÃ¤,Finland,Central Finland,655194
Joensuu,Finland,North Karelia,655808
JÃ¤rvenpÃ¤Ã¤,Finland,Uusimaa,655958
Janakkala,Finland,HÃ¤me,656073
JÃ¤msÃ¤,Finland,Central Finland,656083
Jakobstad,Finland,Ostrobothnia,656130
Imatra,Finland,South Karelia,656688
Iisalmi,Finland,Northern Savo,656820
Hyvinge,Finland,Uusimaa,656913
Hollola,Finland,PÃ¤ijÃ¤nne Tavastia,657530
Helsinki,Finland,Uusimaa,658225
Heinola,Finland,PÃ¤ijÃ¤nne Tavastia,658288
Haukipudas,Finland,Northern Ostrobothnia,658629
Hamina,Finland,Kymenlaakso,659169
HÃ¤meenlinna,Finland,HÃ¤me,659180
Forssa,Finland,HÃ¤me,659935
Espoo,Finland,Uusimaa,660158
Porvoo,Finland,Uusimaa,660561
Anjala,Finland,Kymenlaakso,661164
LÃ¤nsi-Turunmaa,Finland,Southwest Finland,7911309
Suva,Fiji,Central,2198148
Nadi,Fiji,Western,2202064
Lautoka,Fiji,Western,2204506
Labasa,Fiji,Northern,2204582
Stanley,Falkland Islands,N/A,3426691
Palikir - National Government Center,Micronesia,Pohnpei,2081986
TÃ³rshavn,Faroe Islands,Streymoy,2611396
Yerres,France,ÃŽle-de-France,2967245
Wittenheim,France,Alsace-Champagne-Ardenne-Lorraine,2967318
Wattrelos,France,Nord-Pas-de-Calais-Picardie,2967421
Wasquehal,France,Nord-Pas-de-Calais-Picardie,2967438
Voiron,France,Auvergne-RhÃ´ne-Alpes,2967758
Vitry-sur-Seine,France,ÃŽle-de-France,2967849
Vitry-le-FranÃ§ois,France,Alsace-Champagne-Ardenne-Lorraine,2967856
Vitrolles,France,Provence-Alpes-CÃ´te d'Azur,2967870
VitrÃ©,France,Brittany,2967879
Viry-ChÃ¢tillon,France,ÃŽle-de-France,2967917
Viroflay,France,ÃŽle-de-France,2967934
Vincennes,France,ÃŽle-de-France,2968054
Villiers-sur-Marne,France,ÃŽle-de-France,2968142
Villiers-le-Bel,France,ÃŽle-de-France,2968176
Villeurbanne,France,Auvergne-RhÃ´ne-Alpes,2968254
Villers-lÃ¨s-Nancy,France,Alsace-Champagne-Ardenne-Lorraine,2968368
Villepinte,France,ÃŽle-de-France,2968482
Villeparisis,France,ÃŽle-de-France,2968496
Villeneuve-sur-Lot,France,Aquitaine-Limousin-Poitou-Charentes,2968515
Villeneuve-Saint-Georges,France,ÃŽle-de-France,2968529
Villeneuve-le-Roi,France,ÃŽle-de-France,2968546
Villeneuve-la-Garenne,France,ÃŽle-de-France,2968555
Villenave-dâ€™Ornon,France,Aquitaine-Limousin-Poitou-Charentes,2968620
Villemomble,France,ÃŽle-de-France,2968653
Villejuif,France,ÃŽle-de-France,2968705
Villefranche-sur-SaÃ´ne,France,Auvergne-RhÃ´ne-Alpes,2968748
Villefontaine,France,Auvergne-RhÃ´ne-Alpes,2968771
Vigneux-sur-Seine,France,ÃŽle-de-France,2969109
Vierzon,France,Centre,2969257
Vienne,France,Auvergne-RhÃ´ne-Alpes,2969284
Vichy,France,Auvergne-RhÃ´ne-Alpes,2969392
Vesoul,France,Bourgogne-Franche-ComtÃ©,2969562
Vertou,France,Pays de la Loire,2969612
Versailles,France,ÃŽle-de-France,2969679
VerriÃ¨res-le-Buisson,France,ÃŽle-de-France,2969692
Vernon,France,Normandy,2969766
Verneuil-sur-Seine,France,ÃŽle-de-France,2969796
Verdun,France,Alsace-Champagne-Ardenne-Lorraine,2969958
VÃ©nissieux,France,Auvergne-RhÃ´ne-Alpes,2970072
VendÃ´me,France,Centre,2970110
Vence,France,Provence-Alpes-CÃ´te d'Azur,2970148
VÃ©lizy-Villacoublay,France,ÃŽle-de-France,2970203
VaurÃ©al,France,ÃŽle-de-France,2970432
Vaulx-en-Velin,France,Auvergne-RhÃ´ne-Alpes,2970456
Vanves,France,ÃŽle-de-France,2970761
Vannes,France,Brittany,2970777
VandÅ“uvre-lÃ¨s-Nancy,France,Alsace-Champagne-Ardenne-Lorraine,2970797
Vallauris,France,Provence-Alpes-CÃ´te d'Azur,2970962
Valenciennes,France,Nord-Pas-de-Calais-Picardie,2971041
Valence,France,Auvergne-RhÃ´ne-Alpes,2971053
Tulle,France,Aquitaine-Limousin-Poitou-Charentes,2971482
Troyes,France,Alsace-Champagne-Ardenne-Lorraine,2971549
Tremblay-en-France,France,ÃŽle-de-France,2971874
Trappes,France,ÃŽle-de-France,2972049
Tours,France,Centre,2972191
Tournefeuille,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,2972237
Tourlaville,France,Normandy,2972270
Tourcoing,France,Nord-Pas-de-Calais-Picardie,2972284
Toulouse,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,2972315
Toulon,France,Provence-Alpes-CÃ´te d'Azur,2972328
Toul,France,Alsace-Champagne-Ardenne-Lorraine,2972350
Torcy,France,ÃŽle-de-France,2972444
Thonon-les-Bains,France,Auvergne-RhÃ´ne-Alpes,2972742
Thionville,France,Alsace-Champagne-Ardenne-Lorraine,2972811
Thiais,France,ÃŽle-de-France,2972893
Tergnier,France,Nord-Pas-de-Calais-Picardie,2973146
Taverny,France,ÃŽle-de-France,2973258
Tassin-la-Demi-Lune,France,Auvergne-RhÃ´ne-Alpes,2973317
Tarbes,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,2973385
Talence,France,Aquitaine-Limousin-Poitou-Charentes,2973495
Suresnes,France,ÃŽle-de-France,2973675
Sucy-en-Brie,France,ÃŽle-de-France,2973745
Strasbourg,France,Alsace-Champagne-Ardenne-Lorraine,2973783
Stains,France,ÃŽle-de-France,2973841
Sotteville-lÃ¨s-Rouen,France,Normandy,2974153
Sorgues,France,Provence-Alpes-CÃ´te d'Azur,2974188
Soisy-sous-Montmorency,France,ÃŽle-de-France,2974385
Soissons,France,Nord-Pas-de-Calais-Picardie,2974389
Six-Fours-les-Plages,France,Provence-Alpes-CÃ´te d'Azur,2974427
Sin-le-Noble,France,Nord-Pas-de-Calais-Picardie,2974494
Seynod,France,Auvergne-RhÃ´ne-Alpes,2974655
SÃ¨vres,France,ÃŽle-de-France,2974678
Sevran,France,ÃŽle-de-France,2974681
SÃ¨te,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,2974733
Sens,France,Bourgogne-Franche-ComtÃ©,2975050
Senlis,France,Nord-Pas-de-Calais-Picardie,2975088
SÃ©lestat,France,Alsace-Champagne-Ardenne-Lorraine,2975233
Sedan,France,Alsace-Champagne-Ardenne-Lorraine,2975349
Schiltigheim,France,Alsace-Champagne-Ardenne-Lorraine,2975446
Sceaux,France,ÃŽle-de-France,2975469
Savigny-sur-Orge,France,ÃŽle-de-France,2975525
Savigny-le-Temple,France,ÃŽle-de-France,2975536
Saumur,France,Pays de la Loire,2975758
Sartrouville,France,ÃŽle-de-France,2975921
Sarreguemines,France,Alsace-Champagne-Ardenne-Lorraine,2975964
Sarcelles,France,ÃŽle-de-France,2976043
Saran,France,Centre,2976050
Sannois,France,ÃŽle-de-France,2976179
Sanary-sur-Mer,France,Provence-Alpes-CÃ´te d'Azur,2976258
Salon-de-Provence,France,Provence-Alpes-CÃ´te d'Azur,2976341
Sallanches,France,Auvergne-RhÃ´ne-Alpes,2976406
Saint-SÃ©bastien-sur-Loire,France,Pays de la Loire,2976984
Saint-RaphaÃ«l,France,Provence-Alpes-CÃ´te d'Azur,2977246
Saint-Quentin,France,Nord-Pas-de-Calais-Picardie,2977295
Saint-Priest,France,Auvergne-RhÃ´ne-Alpes,2977356
Saint-Pol-sur-Mer,France,Nord-Pas-de-Calais-Picardie,2977388
Saint-Pierre-des-Corps,France,Centre,2977491
Saint-Ouen-lâ€™AumÃ´ne,France,ÃŽle-de-France,2977800
Saint-Ouen,France,ÃŽle-de-France,2977824
Saint-Omer,France,Nord-Pas-de-Calais-Picardie,2977845
Saint-Nazaire,France,Pays de la Loire,2977921
Saint-Michel-sur-Orge,France,ÃŽle-de-France,2977952
Saint-MÃ©dard-en-Jalles,France,Aquitaine-Limousin-Poitou-Charentes,2978072
Saint-Maximin-la-Sainte-Baume,France,Provence-Alpes-CÃ´te d'Azur,2978100
Saint-Maur-des-FossÃ©s,France,ÃŽle-de-France,2978179
Saint-Martin-dâ€™HÃ¨res,France,Auvergne-RhÃ´ne-Alpes,2978317
Saint-MandÃ©,France,ÃŽle-de-France,2978621
Saint-Malo,France,Brittany,2978640
Saint-Louis,France,Alsace-Champagne-Ardenne-Lorraine,2978742
Saint-LÃ´,France,Normandy,2978758
Saint-Leu-la-ForÃªt,France,ÃŽle-de-France,2978768
Saint-Leu,France,Bourgogne-Franche-ComtÃ©,2978771
Saint-Laurent-du-Var,France,Provence-Alpes-CÃ´te d'Azur,2978891
Saint-Jean-de-la-Ruelle,France,Centre,2979316
Saint-Jean-de-Braye,France,Centre,2979341
Saint-Herblain,France,Pays de la Loire,2979590
Saint-Gratien,France,ÃŽle-de-France,2979627
Saint-Germain-en-Laye,France,ÃŽle-de-France,2979783
Saint-Genis-Laval,France,Auvergne-RhÃ´ne-Alpes,2979985
Saint-Fons,France,Auvergne-RhÃ´ne-Alpes,2980097
Saint-Ã‰tienne-du-Rouvray,France,Normandy,2980236
Saint-Ã‰tienne,France,Auvergne-RhÃ´ne-Alpes,2980291
Saintes,France,Aquitaine-Limousin-Poitou-Charentes,2980340
Sainte-GeneviÃ¨ve-des-Bois,France,ÃŽle-de-France,2980558
Sainte-Foy-lÃ¨s-Lyon,France,Auvergne-RhÃ´ne-Alpes,2980586
Saint-Ã‰grÃ¨ve,France,Auvergne-RhÃ´ne-Alpes,2980636
Saint-Dizier,France,Alsace-Champagne-Ardenne-Lorraine,2980816
Saint-DiÃ©-des-Vosges,France,Alsace-Champagne-Ardenne-Lorraine,2980827
Saint-Denis,France,ÃŽle-de-France,2980916
Saint-Cyr-sur-Loire,France,Centre,2980935
Saint-Cyr-lâ€™Ã‰cole,France,ÃŽle-de-France,2980942
Saint-Cloud,France,ÃŽle-de-France,2981041
Saint-Chamond,France,Auvergne-RhÃ´ne-Alpes,2981206
Saint-Brieuc,France,Brittany,2981280
Saint-Avold,France,Alsace-Champagne-Ardenne-Lorraine,2981492
Saint-Avertin,France,Centre,2981512
Saint-Amand-les-Eaux,France,Nord-Pas-de-Calais-Picardie,2981839
Rueil-Malmaison,France,ÃŽle-de-France,2982235
Royan,France,Aquitaine-Limousin-Poitou-Charentes,2982343
Rouen,France,Normandy,2982652
Roubaix,France,Nord-Pas-de-Calais-Picardie,2982681
Rosny-sous-Bois,France,ÃŽle-de-France,2982757
Ronchin,France,Nord-Pas-de-Calais-Picardie,2982944
Romorantin-Lanthenay,France,Centre,2982967
Romans-sur-IsÃ¨re,France,Auvergne-RhÃ´ne-Alpes,2983011
Romainville,France,ÃŽle-de-France,2983026
Roissy-en-Brie,France,ÃŽle-de-France,2983074
Rodez,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,2983154
Rochefort,France,Aquitaine-Limousin-Poitou-Charentes,2983276
Roanne,France,Auvergne-RhÃ´ne-Alpes,2983362
Ris-Orangis,France,ÃŽle-de-France,2983440
Riom,France,Auvergne-RhÃ´ne-Alpes,2983489
Rillieux-la-Pape,France,Auvergne-RhÃ´ne-Alpes,2983536
RezÃ©,France,Pays de la Loire,2983770
Rennes,France,Brittany,2983990
Reims,France,Alsace-Champagne-Ardenne-Lorraine,2984114
Rambouillet,France,ÃŽle-de-France,2984513
Quimper,France,Brittany,2984701
Puteaux,France,ÃŽle-de-France,2985034
Port-de-Bouc,France,Provence-Alpes-CÃ´te d'Azur,2986025
Pontoise,France,ÃŽle-de-France,2986140
Pontivy,France,Brittany,2986160
Pontarlier,France,Bourgogne-Franche-ComtÃ©,2986302
Pont-Ã -Mousson,France,Alsace-Champagne-Ardenne-Lorraine,2986306
Poitiers,France,Aquitaine-Limousin-Poitou-Charentes,2986495
Poissy,France,ÃŽle-de-France,2986501
Ploemeur,France,Brittany,2986732
Plaisir,France,ÃŽle-de-France,2986930
Plaisance-du-Touch,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,2986933
Pierrefitte-sur-Seine,France,ÃŽle-de-France,2987271
Pessac,France,Aquitaine-Limousin-Poitou-Charentes,2987805
Pertuis,France,Provence-Alpes-CÃ´te d'Azur,2987825
Perpignan,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,2987914
PÃ©rigueux,France,Aquitaine-Limousin-Poitou-Charentes,2987967
Pau,France,Aquitaine-Limousin-Poitou-Charentes,2988358
Paris,France,ÃŽle-de-France,2988507
Pantin,France,ÃŽle-de-France,2988621
Pamiers,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,2988670
Palaiseau,France,ÃŽle-de-France,2988758
Ozoir-la-FerriÃ¨re,France,ÃŽle-de-France,2988867
Oyonnax,France,Auvergne-RhÃ´ne-Alpes,2988888
Outreau,France,Nord-Pas-de-Calais-Picardie,2988936
Oullins,France,Auvergne-RhÃ´ne-Alpes,2988998
Osny,France,ÃŽle-de-France,2989130
Orvault,France,Pays de la Loire,2989170
Orsay,France,ÃŽle-de-France,2989204
Orly,France,ÃŽle-de-France,2989297
OrlÃ©ans,France,Centre,2989317
Orange,France,Provence-Alpes-CÃ´te d'Azur,2989460
Olivet,France,Centre,2989611
Octeville,France,Normandy,2989755
Noyon,France,Nord-Pas-de-Calais-Picardie,2989877
Noisy-le-Sec,France,ÃŽle-de-France,2990187
Noisy-le-Grand,France,ÃŽle-de-France,2990189
Noisiel,France,ÃŽle-de-France,2990192
Nogent-sur-Oise,France,Nord-Pas-de-Calais-Picardie,2990264
Nogent-sur-Marne,France,ÃŽle-de-France,2990265
Niort,France,Aquitaine-Limousin-Poitou-Charentes,2990355
NÃ®mes,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,2990363
Nice,France,Provence-Alpes-CÃ´te d'Azur,2990440
Nevers,France,Bourgogne-Franche-ComtÃ©,2990474
Neuilly-sur-Seine,France,ÃŽle-de-France,2990611
Neuilly-sur-Marne,France,ÃŽle-de-France,2990612
Neuilly-Plaisance,France,ÃŽle-de-France,2990616
Narbonne,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,2990919
Nantes,France,Pays de la Loire,2990969
Nanterre,France,ÃŽle-de-France,2990970
Nancy,France,Alsace-Champagne-Ardenne-Lorraine,2990999
Muret,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,2991153
Mulhouse,France,Alsace-Champagne-Ardenne-Lorraine,2991214
Moulins,France,Auvergne-RhÃ´ne-Alpes,2991481
Mougins,France,Provence-Alpes-CÃ´te d'Azur,2991551
Morsang-sur-Orge,France,ÃŽle-de-France,2991719
Morlaix,France,Brittany,2991772
Mont-Saint-Aignan,France,Normandy,2992003
Montrouge,France,ÃŽle-de-France,2992017
Montreuil,France,ÃŽle-de-France,2992090
Montpellier,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,2992166
Montmorency,France,ÃŽle-de-France,2992229
MontluÃ§on,France,Auvergne-RhÃ´ne-Alpes,2992292
Montivilliers,France,Normandy,2992367
Montigny-lÃ¨s-Metz,France,Alsace-Champagne-Ardenne-Lorraine,2992402
Montigny-lÃ¨s-Cormeilles,France,ÃŽle-de-France,2992404
Montigny-le-Bretonneux,France,ÃŽle-de-France,2992415
Montgeron,France,ÃŽle-de-France,2992536
Montfermeil,France,ÃŽle-de-France,2992616
Montesson,France,ÃŽle-de-France,2992650
Montereau-Fault-Yonne,France,ÃŽle-de-France,2992671
MontÃ©limar,France,Auvergne-RhÃ´ne-Alpes,2992703
Mont-de-Marsan,France,Aquitaine-Limousin-Poitou-Charentes,2992771
Montceau-les-Mines,France,Bourgogne-Franche-ComtÃ©,2992863
Montbrison,France,Auvergne-RhÃ´ne-Alpes,2992890
MontbÃ©liard,France,Bourgogne-Franche-ComtÃ©,2992938
Montauban,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,2993002
Montargis,France,Centre,2993024
Mons-en-BarÅ“ul,France,Nord-Pas-de-Calais-Picardie,2993207
Moissy-Cramayel,France,ÃŽle-de-France,2993572
Mitry-Mory,France,ÃŽle-de-France,2993679
Miramas,France,Provence-Alpes-CÃ´te d'Azur,2993760
Millau,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,2993875
Meyzieu,France,Auvergne-RhÃ´ne-Alpes,2994048
Meylan,France,Auvergne-RhÃ´ne-Alpes,2994087
Meudon,France,ÃŽle-de-France,2994144
Metz,France,Alsace-Champagne-Ardenne-Lorraine,2994160
MÃ©rignac,France,Aquitaine-Limousin-Poitou-Charentes,2994393
Menton,France,Provence-Alpes-CÃ´te d'Azur,2994497
Melun,France,ÃŽle-de-France,2994651
Meaux,France,ÃŽle-de-France,2994798
Mayenne,France,Pays de la Loire,2994935
Maurepas,France,ÃŽle-de-France,2995041
Mauguio,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,2995121
Maubeuge,France,Nord-Pas-de-Calais-Picardie,2995150
Massy,France,ÃŽle-de-France,2995206
Martigues,France,Provence-Alpes-CÃ´te d'Azur,2995387
Marseille,France,Provence-Alpes-CÃ´te d'Azur,2995469
Marmande,France,Aquitaine-Limousin-Poitou-Charentes,2995642
Marly-le-Roi,France,ÃŽle-de-France,2995652
Marignane,France,Provence-Alpes-CÃ´te d'Azur,2995750
Marcq-en-BarÅ“ul,France,Nord-Pas-de-Calais-Picardie,2995908
Mantes-la-Ville,France,ÃŽle-de-France,2996146
Mantes-la-Jolie,France,ÃŽle-de-France,2996148
Manosque,France,Provence-Alpes-CÃ´te d'Azur,2996180
Mandelieu-la-Napoule,France,Provence-Alpes-CÃ´te d'Azur,2996255
Malakoff,France,ÃŽle-de-France,2996514
Maisons-Laffitte,France,ÃŽle-de-France,2996564
Maisons-Alfort,France,ÃŽle-de-France,2996568
MÃ¢con,France,Bourgogne-Franche-ComtÃ©,2996882
Lyon,France,Auvergne-RhÃ´ne-Alpes,2996944
LunÃ©ville,France,Alsace-Champagne-Ardenne-Lorraine,2997110
Lunel,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,2997116
LucÃ©,France,Centre,2997246
Louviers,France,Normandy,2997336
Lourdes,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,2997395
Lormont,France,Aquitaine-Limousin-Poitou-Charentes,2997556
Lorient,France,Brittany,2997577
Loos,France,Nord-Pas-de-Calais-Picardie,2997620
Lons-le-Saunier,France,Bourgogne-Franche-ComtÃ©,2997626
Longjumeau,France,ÃŽle-de-France,2997712
Lomme,France,Nord-Pas-de-Calais-Picardie,2997803
Lognes,France,ÃŽle-de-France,2997904
Livry-Gargan,France,ÃŽle-de-France,2998056
Lâ€™Isle-sur-la-Sorgue,France,Provence-Alpes-CÃ´te d'Azur,2998127
Lisieux,France,Normandy,2998150
Lingolsheim,France,Alsace-Champagne-Ardenne-Lorraine,2998224
Limoges,France,Aquitaine-Limousin-Poitou-Charentes,2998286
Limeil-BrÃ©vannes,France,ÃŽle-de-France,2998305
Limay,France,ÃŽle-de-France,2998311
Lille,France,Nord-Pas-de-Calais-Picardie,2998324
LiÃ©vin,France,Nord-Pas-de-Calais-Picardie,2998431
Libourne,France,Aquitaine-Limousin-Poitou-Charentes,2998517
L'HaÃ¿-les-Roses,France,ÃŽle-de-France,2998632
Le VÃ©sinet,France,ÃŽle-de-France,2998854
Levallois-Perret,France,ÃŽle-de-France,2998975
Les Sables-d'Olonne,France,Pays de la Loire,2999683
Les Pennes-Mirabeau,France,Provence-Alpes-CÃ´te d'Azur,3000047
Les Pavillons-sous-Bois,France,ÃŽle-de-France,3000060
Les Mureaux,France,ÃŽle-de-France,3000192
Les Lilas,France,ÃŽle-de-France,3000491
Les Herbiers,France,Pays de la Loire,3000648
Les Clayes-sous-Bois,France,ÃŽle-de-France,3001402
Le Puy-en-Velay,France,Auvergne-RhÃ´ne-Alpes,3002465
Le PrÃ©-Saint-Gervais,France,ÃŽle-de-France,3002499
Le Pontet,France,Provence-Alpes-CÃ´te d'Azur,3002570
Le Plessis-TrÃ©vise,France,ÃŽle-de-France,3002647
Le Plessis-Robinson,France,ÃŽle-de-France,3002650
Le Petit-Quevilly,France,Normandy,3002880
Le Perreux-sur-Marne,France,ÃŽle-de-France,3002965
Le Pecq,France,ÃŽle-de-France,3002984
Lens,France,Nord-Pas-de-Calais-Picardie,3003093
Le MÃ©e-sur-Seine,France,ÃŽle-de-France,3003481
Le Mans,France,Pays de la Loire,3003603
Le Kremlin-BicÃªtre,France,ÃŽle-de-France,3003737
Le Havre,France,Normandy,3003796
Le Grand-Quevilly,France,Normandy,3003952
Le Creusot,France,Bourgogne-Franche-ComtÃ©,3004427
Le Chesnay,France,ÃŽle-de-France,3004630
Le Cannet,France,Provence-Alpes-CÃ´te d'Azur,3004871
Le Bouscat,France,Aquitaine-Limousin-Poitou-Charentes,3005066
Le Blanc-Mesnil,France,ÃŽle-de-France,3005269
Laxou,France,Alsace-Champagne-Ardenne-Lorraine,3005417
La Valette-du-Var,France,Provence-Alpes-CÃ´te d'Azur,3005825
Laval,France,Pays de la Loire,3005866
Lattes,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,3006121
La Teste-de-Buch,France,Aquitaine-Limousin-Poitou-Charentes,3006283
La Seyne-sur-Mer,France,Provence-Alpes-CÃ´te d'Azur,3006414
La Roche-sur-Yon,France,Pays de la Loire,3006767
La Rochelle,France,Aquitaine-Limousin-Poitou-Charentes,3006787
Laon,France,Nord-Pas-de-Calais-Picardie,3007477
Lannion,France,Brittany,3007609
Lanester,France,Brittany,3007794
Landerneau,France,Brittany,3007874
Lambersart,France,Nord-Pas-de-Calais-Picardie,3008218
La Madeleine,France,Nord-Pas-de-Calais-Picardie,3008379
Lagny-sur-Marne,France,ÃŽle-de-France,3009071
La Garenne-Colombes,France,ÃŽle-de-France,3009169
La Garde,France,Provence-Alpes-CÃ´te d'Azur,3009223
La FlÃ¨che,France,Pays de la Loire,3009443
La Crau,France,Provence-Alpes-CÃ´te d'Azur,3009791
La Courneuve,France,ÃŽle-de-France,3009824
La Ciotat,France,Provence-Alpes-CÃ´te d'Azur,3010025
La Chapelle-sur-Erdre,France,Pays de la Loire,3010237
La Celle-Saint-Cloud,France,ÃŽle-de-France,3010529
Jouy-le-Moutier,France,ÃŽle-de-France,3012162
JouÃ©-lÃ©s-Tours,France,Centre,3012219
Joinville-le-Pont,France,ÃŽle-de-France,3012313
Ivry-sur-Seine,France,ÃŽle-de-France,3012621
Istres,France,Provence-Alpes-CÃ´te d'Azur,3012647
Issy-les-Moulineaux,France,ÃŽle-de-France,3012649
Issoire,France,Auvergne-RhÃ´ne-Alpes,3012664
Illzach,France,Alsace-Champagne-Ardenne-Lorraine,3012829
Illkirch-Graffenstaden,France,Alsace-Champagne-Ardenne-Lorraine,3012834
HyÃ¨res,France,Provence-Alpes-CÃ´te d'Azur,3012937
Houilles,France,ÃŽle-de-France,3013097
HÃ©rouville-Saint-Clair,France,Normandy,3013403
Herblay,France,ÃŽle-de-France,3013477
HÃ©nin-Beaumont,France,Nord-Pas-de-Calais-Picardie,3013525
Hem,France,Nord-Pas-de-Calais-Picardie,3013549
Hazebrouck,France,Nord-Pas-de-Calais-Picardie,3013619
Hayange,France,Alsace-Champagne-Ardenne-Lorraine,3013627
Hautmont,France,Nord-Pas-de-Calais-Picardie,3013681
Yutz,France,Alsace-Champagne-Ardenne-Lorraine,3013701
Haubourdin,France,Nord-Pas-de-Calais-Picardie,3013862
Halluin,France,Nord-Pas-de-Calais-Picardie,3014034
Haguenau,France,Alsace-Champagne-Ardenne-Lorraine,3014078
Guyancourt,France,ÃŽle-de-France,3014143
Gujan-Mestras,France,Aquitaine-Limousin-Poitou-Charentes,3014175
GuÃ©ret,France,Aquitaine-Limousin-Poitou-Charentes,3014383
GuÃ©rande,France,Pays de la Loire,3014392
Grigny,France,ÃŽle-de-France,3014646
Grenoble,France,Auvergne-RhÃ´ne-Alpes,3014728
Grasse,France,Provence-Alpes-CÃ´te d'Azur,3014856
Grande-Synthe,France,Nord-Pas-de-Calais-Picardie,3015160
Gradignan,France,Aquitaine-Limousin-Poitou-Charentes,3015419
Goussainville,France,ÃŽle-de-France,3015490
Gonesse,France,ÃŽle-de-France,3015689
Givors,France,Auvergne-RhÃ´ne-Alpes,3015902
Gif-sur-Yvette,France,ÃŽle-de-France,3016078
Gien,France,Centre,3016097
Gentilly,France,ÃŽle-de-France,3016292
Gennevilliers,France,ÃŽle-de-France,3016321
Garges-lÃ¨s-Gonesse,France,ÃŽle-de-France,3016621
Gardanne,France,Provence-Alpes-CÃ´te d'Azur,3016667
Garches,France,ÃŽle-de-France,3016675
Gap,France,Provence-Alpes-CÃ´te d'Azur,3016702
Gagny,France,ÃŽle-de-France,3016830
Frontignan,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,3016956
Fresnes,France,ÃŽle-de-France,3017178
FrÃ©jus,France,Provence-Alpes-CÃ´te d'Azur,3017253
Franconville,France,ÃŽle-de-France,3017341
FougÃ¨res,France,Brittany,3017609
Fos-sur-Mer,France,Provence-Alpes-CÃ´te d'Azur,3017651
Forbach,France,Alsace-Champagne-Ardenne-Lorraine,3017805
Fontenay-sous-Bois,France,ÃŽle-de-France,3017910
Fontenay-le-Comte,France,Pays de la Loire,3017921
Fontenay-aux-Roses,France,ÃŽle-de-France,3017924
Fontainebleau,France,ÃŽle-de-France,3018074
Fontaine,France,Auvergne-RhÃ´ne-Alpes,3018095
Floirac,France,Aquitaine-Limousin-Poitou-Charentes,3018246
Fleury-les-Aubrais,France,Centre,3018280
Flers,France,Normandy,3018339
Firminy,France,Auvergne-RhÃ´ne-Alpes,3018455
FÃ©camp,France,Normandy,3018794
Faches-Thumesnil,France,Nord-Pas-de-Calais-Picardie,3019153
Eysines,France,Aquitaine-Limousin-Poitou-Charentes,3019193
Ã‰vry,France,ÃŽle-de-France,3019256
Ã‰vreux,France,Normandy,3019265
Ã‰tampes,France,ÃŽle-de-France,3019459
La Baule-Escoublac,France,Pays de la Loire,3019766
Ermont,France,ÃŽle-de-France,3019897
Ã‰ragny,France,ÃŽle-de-France,3019952
Ã‰queurdreville-Hainneville,France,Normandy,3019960
Ã‰pinay-sur-Seine,France,ÃŽle-de-France,3020020
Ã‰pinal,France,Alsace-Champagne-Ardenne-Lorraine,3020035
Ã‰pernay,France,Alsace-Champagne-Ardenne-Lorraine,3020062
Elbeuf,France,Normandy,3020307
Ã‰lancourt,France,ÃŽle-de-France,3020310
Ã‰cully,France,Auvergne-RhÃ´ne-Alpes,3020392
Ã‰chirolles,France,Auvergne-RhÃ´ne-Alpes,3020495
Eaubonne,France,ÃŽle-de-France,3020601
Dunkerque,France,Nord-Pas-de-Calais-Picardie,3020686
Dreux,France,Centre,3020810
Draveil,France,ÃŽle-de-France,3020832
Drancy,France,ÃŽle-de-France,3020839
Draguignan,France,Provence-Alpes-CÃ´te d'Azur,3020850
Douarnenez,France,Brittany,3020996
Douai,France,Nord-Pas-de-Calais-Picardie,3021000
Domont,France,ÃŽle-de-France,3021150
Dole,France,Bourgogne-Franche-ComtÃ©,3021263
Dijon,France,Bourgogne-Franche-ComtÃ©,3021372
Digne-les-Bains,France,Provence-Alpes-CÃ´te d'Azur,3021382
Dieppe,France,Normandy,3021411
Deuil-la-Barre,France,ÃŽle-de-France,3021516
Denain,France,Nord-Pas-de-Calais-Picardie,3021605
DÃ©cines-Charpieu,France,Auvergne-RhÃ´ne-Alpes,3021662
Dax,France,Aquitaine-Limousin-Poitou-Charentes,3021670
Dammarie-les-Lys,France,ÃŽle-de-France,3021852
Cugnaux,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,3022151
Croix,France,Nord-Pas-de-Calais-Picardie,3022376
CrÃ©teil,France,ÃŽle-de-France,3022530
CrÃ©py-en-Valois,France,Nord-Pas-de-Calais-Picardie,3022569
Creil,France,Nord-Pas-de-Calais-Picardie,3022610
Cran-Gevrier,France,Auvergne-RhÃ´ne-Alpes,3022700
Cournon-dâ€™Auvergne,France,Auvergne-RhÃ´ne-Alpes,3022988
Courbevoie,France,ÃŽle-de-France,3023141
Coulommiers,France,ÃŽle-de-France,3023240
CouÃ«ron,France,Pays de la Loire,3023324
Coudekerque-Branche,France,Nord-Pas-de-Calais-Picardie,3023356
Cormeilles-en-Parisis,France,ÃŽle-de-France,3023645
Corbeil-Essonnes,France,ÃŽle-de-France,3023763
Conflans-Sainte-Honorine,France,ÃŽle-de-France,3023924
Concarneau,France,Brittany,3024035
CompiÃ¨gne,France,Nord-Pas-de-Calais-Picardie,3024066
Combs-la-Ville,France,ÃŽle-de-France,3024107
Pontault-Combault,France,ÃŽle-de-France,3024195
Colomiers,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,3024223
Colombes,France,ÃŽle-de-France,3024266
Colmar,France,Alsace-Champagne-Ardenne-Lorraine,3024297
Cognac,France,Aquitaine-Limousin-Poitou-Charentes,3024440
Cluses,France,Auvergne-RhÃ´ne-Alpes,3024532
Clichy-sous-Bois,France,ÃŽle-de-France,3024596
Clichy,France,ÃŽle-de-France,3024597
Clermont-Ferrand,France,Auvergne-RhÃ´ne-Alpes,3024635
Clamart,France,ÃŽle-de-France,3024783
Cholet,France,Pays de la Loire,3025053
Choisy-le-Roi,France,ÃŽle-de-France,3025055
Chilly-Mazarin,France,ÃŽle-de-France,3025144
Chevilly-Larue,France,ÃŽle-de-France,3025314
Cherbourg-Octeville,France,Normandy,3025466
ChenÃ´ve,France,Bourgogne-Franche-ComtÃ©,3025496
ChenneviÃ¨res-sur-Marne,France,ÃŽle-de-France,3025509
Chelles,France,ÃŽle-de-France,3025622
Chaville,France,ÃŽle-de-France,3025715
Chaumont,France,Alsace-Champagne-Ardenne-Lorraine,3025892
Chatou,France,ÃŽle-de-France,3026033
ChÃ¢tillon,France,ÃŽle-de-France,3026083
ChÃ¢tenay-Malabry,France,ÃŽle-de-France,3026108
ChÃ¢tellerault,France,Aquitaine-Limousin-Poitou-Charentes,3026141
ChÃ¢teau-Thierry,France,Nord-Pas-de-Calais-Picardie,3026194
ChÃ¢teauroux,France,Centre,3026204
ChÃ¢teaudun,France,Centre,3026285
Chartres,France,Centre,3026467
Charleville-MÃ©ziÃ¨res,France,Alsace-Champagne-Ardenne-Lorraine,3026613
Charenton-le-Pont,France,ÃŽle-de-France,3026637
Champs-sur-Marne,France,ÃŽle-de-France,3027014
Champigny-sur-Marne,France,ÃŽle-de-France,3027105
ChambÃ©ry,France,Auvergne-RhÃ´ne-Alpes,3027422
ChamaliÃ¨res,France,Auvergne-RhÃ´ne-Alpes,3027453
Chalon-sur-SaÃ´ne,France,Bourgogne-Franche-ComtÃ©,3027484
ChÃ¢lons-en-Champagne,France,Alsace-Champagne-Ardenne-Lorraine,3027487
Challans,France,Pays de la Loire,3027513
Cestas,France,Aquitaine-Limousin-Poitou-Charentes,3027763
Cesson-SÃ©vignÃ©,France,Brittany,3027767
Cergy,France,ÃŽle-de-France,3027883
Cenon,France,Aquitaine-Limousin-Poitou-Charentes,3027950
Cavaillon,France,Provence-Alpes-CÃ´te d'Azur,3028134
Castres,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,3028263
Castelnau-le-Lez,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,3028337
Carvin,France,Nord-Pas-de-Calais-Picardie,3028486
CarriÃ¨res-sous-Poissy,France,ÃŽle-de-France,3028521
Carquefou,France,Pays de la Loire,3028535
Carpentras,France,Provence-Alpes-CÃ´te d'Azur,3028542
Carcassonne,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,3028641
Canteleu,France,Normandy,3028779
Cannes,France,Provence-Alpes-CÃ´te d'Azur,3028808
Cambrai,France,Nord-Pas-de-Calais-Picardie,3029030
Caluire-et-Cuire,France,Auvergne-RhÃ´ne-Alpes,3029096
Calais,France,Nord-Pas-de-Calais-Picardie,3029162
Cahors,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,3029213
Cagnes-sur-Mer,France,Provence-Alpes-CÃ´te d'Azur,3029227
Caen,France,Normandy,3029241
Cachan,France,ÃŽle-de-France,3029276
Bry-sur-Marne,France,ÃŽle-de-France,3029706
Brunoy,France,ÃŽle-de-France,3029748
Bruay-la-BuissiÃ¨re,France,Nord-Pas-de-Calais-Picardie,3029825
Bron,France,Auvergne-RhÃ´ne-Alpes,3029931
Brive-la-Gaillarde,France,Aquitaine-Limousin-Poitou-Charentes,3029974
Brignoles,France,Provence-Alpes-CÃ´te d'Azur,3030057
Brie-Comte-Robert,France,ÃŽle-de-France,3030101
BrÃ©tigny-sur-Orge,France,ÃŽle-de-France,3030257
Brest,France,Brittany,3030300
Bressuire,France,Aquitaine-Limousin-Poitou-Charentes,3030303
Bourgoin,France,Auvergne-RhÃ´ne-Alpes,3030960
Bourg-lÃ¨s-Valence,France,Auvergne-RhÃ´ne-Alpes,3030985
Bourg-la-Reine,France,ÃŽle-de-France,3030990
Bourges,France,Centre,3031005
Bourg-en-Bresse,France,Auvergne-RhÃ´ne-Alpes,3031009
Boulogne-sur-Mer,France,Nord-Pas-de-Calais-Picardie,3031133
Boulogne-Billancourt,France,ÃŽle-de-France,3031137
Bouguenais,France,Pays de la Loire,3031268
Bordeaux,France,Aquitaine-Limousin-Poitou-Charentes,3031582
Bonneuil-sur-Marne,France,ÃŽle-de-France,3031709
Bondy,France,ÃŽle-de-France,3031815
Boissy-Saint-LÃ©ger,France,ÃŽle-de-France,3031898
Bois-Colombes,France,ÃŽle-de-France,3032070
Bobigny,France,ÃŽle-de-France,3032179
Blois,France,Centre,3032213
Blanquefort,France,Aquitaine-Limousin-Poitou-Charentes,3032340
Blagnac,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,3032469
Bischheim,France,Alsace-Champagne-Ardenne-Lorraine,3032551
Biarritz,France,Aquitaine-Limousin-Poitou-Charentes,3032797
Bezons,France,ÃŽle-de-France,3032824
BÃ©ziers,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,3032833
BÃ©thune,France,Nord-Pas-de-Calais-Picardie,3033002
BesanÃ§on,France,Bourgogne-Franche-ComtÃ©,3033123
Bergerac,France,Aquitaine-Limousin-Poitou-Charentes,3033391
Berck,France,Nord-Pas-de-Calais-Picardie,3033415
Berck-Plage,France,Nord-Pas-de-Calais-Picardie,3033416
Belfort,France,Bourgogne-Franche-ComtÃ©,3033791
BÃ¨gles,France,Aquitaine-Limousin-Poitou-Charentes,3033881
Beauvais,France,Nord-Pas-de-Calais-Picardie,3034006
Beaune,France,Bourgogne-Franche-ComtÃ©,3034126
Bayonne,France,Aquitaine-Limousin-Poitou-Charentes,3034475
Bayeux,France,Normandy,3034483
Bastia,France,Corsica,3034640
Bar-le-Duc,France,Alsace-Champagne-Ardenne-Lorraine,3034911
Balma,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,3035204
Bagnols-sur-CÃ¨ze,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,3035396
Bagnolet,France,ÃŽle-de-France,3035403
Bagneux,France,ÃŽle-de-France,3035409
Avon,France,ÃŽle-de-France,3035654
Avion,France,Nord-Pas-de-Calais-Picardie,3035667
Avignon,France,Provence-Alpes-CÃ´te d'Azur,3035681
Auxerre,France,Bourgogne-Franche-ComtÃ©,3035843
Autun,France,Bourgogne-Franche-ComtÃ©,3035883
Aurillac,France,Auvergne-RhÃ´ne-Alpes,3036016
Aulnay-sous-Bois,France,ÃŽle-de-France,3036145
Audincourt,France,Bourgogne-Franche-ComtÃ©,3036240
Auch,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,3036281
Aubervilliers,France,ÃŽle-de-France,3036386
Aubagne,France,Provence-Alpes-CÃ´te d'Azur,3036433
Athis-Mons,France,ÃŽle-de-France,3036460
AsniÃ¨res-sur-Seine,France,ÃŽle-de-France,3036572
Arras,France,Nord-Pas-de-Calais-Picardie,3036784
ArmentiÃ¨res,France,Nord-Pas-de-Calais-Picardie,3036903
Arles,France,Provence-Alpes-CÃ´te d'Azur,3036938
Argenteuil,France,ÃŽle-de-France,3037044
Argentan,France,Normandy,3037051
Arcueil,France,ÃŽle-de-France,3037157
Antony,France,ÃŽle-de-France,3037423
Antibes,France,Provence-Alpes-CÃ´te d'Azur,3037456
Annonay,France,Auvergne-RhÃ´ne-Alpes,3037514
Annemasse,France,Auvergne-RhÃ´ne-Alpes,3037538
Annecy-le-Vieux,France,Auvergne-RhÃ´ne-Alpes,3037540
Annecy,France,Auvergne-RhÃ´ne-Alpes,3037543
AngoulÃªme,France,Aquitaine-Limousin-Poitou-Charentes,3037598
Anglet,France,Aquitaine-Limousin-Poitou-Charentes,3037612
Angers,France,Pays de la Loire,3037656
Amiens,France,Nord-Pas-de-Calais-Picardie,3037854
Allauch,France,Provence-Alpes-CÃ´te d'Azur,3038159
Alfortville,France,ÃŽle-de-France,3038213
AlÃ¨s,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,3038224
AlenÃ§on,France,Normandy,3038230
Albi,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,3038261
Albertville,France,Auvergne-RhÃ´ne-Alpes,3038266
Ajaccio,France,Corsica,3038334
Aix-les-Bains,France,Auvergne-RhÃ´ne-Alpes,3038350
Aix-en-Provence,France,Provence-Alpes-CÃ´te d'Azur,3038354
Agen,France,Aquitaine-Limousin-Poitou-Charentes,3038634
Agde,France,Languedoc-Roussillon-Midi-PyrÃ©nÃ©es,3038638
AchÃ¨res,France,ÃŽle-de-France,3038712
Abbeville,France,Nord-Pas-de-Calais-Picardie,3038789
Villeneuve-d'Ascq,France,Nord-Pas-de-Calais-Picardie,6543862
Les Ulis,France,ÃŽle-de-France,6615536
Bourgoin-Jallieu,France,Auvergne-RhÃ´ne-Alpes,6615539
Marseille 01,France,Provence-Alpes-CÃ´te d'Azur,7284882
Marseille 02,France,Provence-Alpes-CÃ´te d'Azur,7284883
Marseille 03,France,Provence-Alpes-CÃ´te d'Azur,7284884
Marseille 04,France,Provence-Alpes-CÃ´te d'Azur,7284885
Marseille 05,France,Provence-Alpes-CÃ´te d'Azur,7284886
Marseille 06,France,Provence-Alpes-CÃ´te d'Azur,7284887
Marseille 07,France,Provence-Alpes-CÃ´te d'Azur,7284888
Marseille 08,France,Provence-Alpes-CÃ´te d'Azur,7284889
Marseille 10,France,Provence-Alpes-CÃ´te d'Azur,7284890
Marseille 09,France,Provence-Alpes-CÃ´te d'Azur,7284891
Marseille 11,France,Provence-Alpes-CÃ´te d'Azur,7284892
Marseille 12,France,Provence-Alpes-CÃ´te d'Azur,7284893
Marseille 13,France,Provence-Alpes-CÃ´te d'Azur,7284894
Marseille 14,France,Provence-Alpes-CÃ´te d'Azur,7284895
Marseille 15,France,Provence-Alpes-CÃ´te d'Azur,7284896
Marseille 16,France,Provence-Alpes-CÃ´te d'Azur,7284897
La Defense,France,ÃŽle-de-France,8504417
Saint-Quentin-en-Yvelines,France,ÃŽle-de-France,8533870
Cergy-Pontoise,France,ÃŽle-de-France,8555643
Tchibanga,Gabon,Nyanga,2396253
Port-Gentil,Gabon,OgoouÃ©-Maritime,2396518
Oyem,Gabon,Woleu-Ntem,2396646
Mouila,Gabon,NgouniÃ©,2398073
Moanda,Gabon,Haut-OgoouÃ©,2398269
Libreville,Gabon,Estuaire,2399697
LambarÃ©nÃ©,Gabon,Moyen-OgoouÃ©,2399888
Koulamoutou,Gabon,OgoouÃ©-Lolo,2399959
Franceville,Gabon,Haut-OgoouÃ©,2400555
York,United Kingdom,England,2633352
Yeovil,United Kingdom,England,2633373
Yeadon,United Kingdom,England,2633397
Yate,United Kingdom,England,2633406
Wrexham,United Kingdom,Wales,2633485
Worthing,United Kingdom,England,2633521
Worksop,United Kingdom,England,2633551
Workington,United Kingdom,England,2633553
Worcester,United Kingdom,England,2633563
Woodford Green,United Kingdom,England,2633655
Wombwell,United Kingdom,England,2633681
Wolverhampton,United Kingdom,England,2633691
Wokingham,United Kingdom,England,2633708
Woking,United Kingdom,England,2633709
Witney,United Kingdom,England,2633729
Witham,United Kingdom,England,2633749
Wishaw,United Kingdom,Scotland,2633765
Wisbech,United Kingdom,England,2633771
Winsford,United Kingdom,England,2633810
Windsor,United Kingdom,England,2633842
Winchester,United Kingdom,England,2633858
Wilmslow,United Kingdom,England,2633883
Willenhall,United Kingdom,England,2633912
Wigston Magna,United Kingdom,England,2633936
Wigan,United Kingdom,England,2633948
Widnes,United Kingdom,England,2633954
Wickford,United Kingdom,England,2633976
Whitstable,United Kingdom,England,2634021
Whitley Bay,United Kingdom,England,2634032
Whitehaven,United Kingdom,England,2634096
Whitefield,United Kingdom,England,2634103
Whickham,United Kingdom,England,2634155
Weymouth,United Kingdom,England,2634202
Weybridge,United Kingdom,England,2634204
Weston-super-Mare,United Kingdom,England,2634308
West Molesey,United Kingdom,England,2634340
Westhoughton,United Kingdom,England,2634387
West Bromwich,United Kingdom,England,2634491
West Bridgford,United Kingdom,England,2634493
Welwyn Garden City,United Kingdom,England,2634552
Wellington,United Kingdom,England,2634573
Wellingborough,United Kingdom,England,2634578
Welling,United Kingdom,England,2634579
Wednesfield,United Kingdom,England,2634616
Wednesbury,United Kingdom,England,2634617
Wath upon Dearne,United Kingdom,England,2634672
Watford,United Kingdom,England,2634677
Waterlooville,United Kingdom,England,2634686
Washington,United Kingdom,England,2634715
Warwick,United Kingdom,England,2634725
Warrington,United Kingdom,England,2634739
Warminster,United Kingdom,England,2634755
Ware,United Kingdom,England,2634777
Walton-on-Thames,United Kingdom,England,2634825
Waltham Abbey,United Kingdom,England,2634843
Walsall,United Kingdom,England,2634853
Wallsend,United Kingdom,England,2634864
Wallasey,United Kingdom,England,2634873
Walkden,United Kingdom,England,2634887
Wakefield,United Kingdom,England,2634910
Urmston,United Kingdom,England,2635062
Uckfield,United Kingdom,England,2635243
Stowmarket,United Kingdom,England,2636749
Stourport-on-Severn,United Kingdom,England,2636767
Stourbridge,United Kingdom,England,2636769
Stoke-on-Trent,United Kingdom,England,2636841
Stockton-on-Tees,United Kingdom,England,2636876
Stockport,United Kingdom,England,2636882
Stirling,United Kingdom,Scotland,2636910
Stevenage,United Kingdom,England,2636940
Staveley,United Kingdom,England,2636995
Stamford,United Kingdom,England,2637104
Stalybridge,United Kingdom,England,2637106
Staines,United Kingdom,England,2637126
Stafford,United Kingdom,England,2637142
Spennymoor,United Kingdom,England,2637235
Spalding,United Kingdom,England,2637265
South Shields,United Kingdom,England,2637329
Southsea,United Kingdom,England,2637330
Southport,United Kingdom,England,2637343
South Ockendon,United Kingdom,England,2637355
Southend-on-Sea,United Kingdom,England,2637433
South Elmsall,United Kingdom,England,2637435
South Benfleet,United Kingdom,England,2637476
Southampton,United Kingdom,England,2637487
Southall,United Kingdom,England,2637490
Solihull,United Kingdom,England,2637546
Slough,United Kingdom,England,2637627
Sleaford,United Kingdom,England,2637659
Skelmersdale,United Kingdom,England,2637752
Skegness,United Kingdom,England,2637762
Sittingbourne,United Kingdom,England,2637802
Shrewsbury,United Kingdom,England,2637891
Shoreham-by-Sea,United Kingdom,England,2637916
Shoreham,United Kingdom,England,2637917
Shipley,United Kingdom,England,2637958
Sheffield,United Kingdom,England,2638077
Sevenoaks,United Kingdom,England,2638187
Selby,United Kingdom,England,2638235
Seaham,United Kingdom,England,2638302
Seaford,United Kingdom,England,2638311
Scunthorpe,United Kingdom,England,2638324
Scarborough,United Kingdom,England,2638419
Sandown,United Kingdom,England,2638568
Sandbach,United Kingdom,England,2638600
Salisbury,United Kingdom,England,2638664
Salford,United Kingdom,England,2638671
Sale,United Kingdom,England,2638678
Saint Neots,United Kingdom,England,2638717
St Helens,United Kingdom,England,2638785
St Austell,United Kingdom,England,2638853
Saint Andrews,United Kingdom,Scotland,2638864
St Albans,United Kingdom,England,2638867
Ryton,United Kingdom,England,2638894
Ryde,United Kingdom,England,2638911
Rutherglen,United Kingdom,Scotland,2638926
Rushden,United Kingdom,England,2638946
Runcorn,United Kingdom,England,2638960
Ruislip,United Kingdom,England,2638976
Rugeley,United Kingdom,England,2638977
Rugby,United Kingdom,England,2638978
Royton,United Kingdom,England,2639015
Royal Tunbridge Wells,United Kingdom,England,2639022
Rottingdean,United Kingdom,England,2639069
Rotherham,United Kingdom,England,2639093
Romsey,United Kingdom,England,2639189
Rochford,United Kingdom,England,2639265
Rochester,United Kingdom,England,2639268
Rochdale,United Kingdom,England,2639272
Risca,United Kingdom,Wales,2639317
Ripon,United Kingdom,England,2639323
Ripley,United Kingdom,England,2639325
Rhyl,United Kingdom,Wales,2639409
Rhondda,United Kingdom,Wales,2639447
Renfrew,United Kingdom,Scotland,2639495
Reigate,United Kingdom,England,2639506
Redhill,United Kingdom,England,2639545
Redditch,United Kingdom,England,2639557
Redcar,United Kingdom,England,2639563
Reading,United Kingdom,England,2639577
Rayleigh,United Kingdom,England,2639583
Rawtenstall,United Kingdom,England,2639586
Rawmarsh,United Kingdom,England,2639588
Ramsgate,United Kingdom,England,2639660
Ramsbottom,United Kingdom,England,2639668
Purley,United Kingdom,England,2639842
Pudsey,United Kingdom,England,2639866
Prestwick,United Kingdom,Scotland,2639896
Prestwich,United Kingdom,England,2639897
Preston,United Kingdom,England,2639912
Prestatyn,United Kingdom,Wales,2639926
Prescot,United Kingdom,England,2639928
Poulton le Fylde,United Kingdom,England,2639958
Potters Bar,United Kingdom,England,2639970
Portsmouth,United Kingdom,England,2639996
Portslade,United Kingdom,England,2639998
Portishead,United Kingdom,England,2640037
Porthcawl,United Kingdom,Wales,2640054
Port Glasgow,United Kingdom,Scotland,2640060
Portadown,United Kingdom,Northern Ireland,2640085
Poole,United Kingdom,England,2640101
Pontypridd,United Kingdom,Wales,2640104
Pontypool,United Kingdom,Wales,2640106
Pontefract,United Kingdom,England,2640132
Polmont,United Kingdom,Scotland,2640155
Plymstock,United Kingdom,England,2640190
Plymouth,United Kingdom,England,2640194
Pitsea,United Kingdom,England,2640246
Pinner,United Kingdom,England,2640275
Peterlee,United Kingdom,England,2640349
Peterhead,United Kingdom,Scotland,2640351
Peterborough,United Kingdom,England,2640354
Perth,United Kingdom,Scotland,2640358
Penzance,United Kingdom,England,2640377
Penicuik,United Kingdom,Scotland,2640465
Penarth,United Kingdom,Wales,2640496
Paisley,United Kingdom,Scotland,2640677
Paignton,United Kingdom,England,2640681
Oxford,United Kingdom,England,2640729
Oswestry,United Kingdom,England,2640861
Ossett,United Kingdom,England,2640869
Orpington,United Kingdom,England,2640894
Ormskirk,United Kingdom,England,2640908
Omagh,United Kingdom,Northern Ireland,2640967
Oldham,United Kingdom,England,2641022
Oadby,United Kingdom,England,2641134
Nuneaton,United Kingdom,England,2641157
Nottingham,United Kingdom,England,2641170
Norwich,United Kingdom,England,2641181
Northwich,United Kingdom,England,2641224
North Shields,United Kingdom,England,2641267
Northolt,United Kingdom,England,2641290
Lancing,United Kingdom,England,2641319
Northampton,United Kingdom,England,2641430
Northallerton,United Kingdom,England,2641435
Newtownards,United Kingdom,Northern Ireland,2641519
Newtownabbey,United Kingdom,Northern Ireland,2641520
Newton Mearns,United Kingdom,Scotland,2641544
Newton-le-Willows,United Kingdom,England,2641546
Newton Aycliffe,United Kingdom,England,2641555
Newton Abbot,United Kingdom,England,2641557
Newry,United Kingdom,Northern Ireland,2641581
Newquay,United Kingdom,England,2641589
Newport Pagnell,United Kingdom,England,2641591
Newport,United Kingdom,Wales,2641598
Newport,United Kingdom,England,2641599
New Milton,United Kingdom,England,2641609
Newmarket,United Kingdom,England,2641616
New Malden,United Kingdom,England,2641617
Newcastle upon Tyne,United Kingdom,England,2641673
Newcastle under Lyme,United Kingdom,England,2641674
Newbury,United Kingdom,England,2641689
Newburn,United Kingdom,England,2641690
Newark on Trent,United Kingdom,England,2641731
Nelson,United Kingdom,England,2641810
Neath,United Kingdom,Wales,2641843
Nailsea,United Kingdom,England,2641913
Musselburgh,United Kingdom,Scotland,2641942
Motherwell,United Kingdom,Scotland,2642135
Morley,United Kingdom,England,2642189
Moreton,United Kingdom,England,2642204
Morecambe,United Kingdom,England,2642214
Mitcham,United Kingdom,England,2642414
Mirfield,United Kingdom,England,2642423
Milton Keynes,United Kingdom,England,2642465
Middleton,United Kingdom,England,2642593
Middlesbrough,United Kingdom,England,2642607
Mexborough,United Kingdom,England,2642683
Merthyr Tydfil,United Kingdom,Wales,2642705
Melton Mowbray,United Kingdom,England,2642763
Marple,United Kingdom,England,2642999
Marlow,United Kingdom,England,2643003
Market Harborough,United Kingdom,England,2643027
Margate,United Kingdom,England,2643044
March,United Kingdom,England,2643071
Mansfield Woodhouse,United Kingdom,England,2643096
Mansfield,United Kingdom,England,2643097
Mangotsfield,United Kingdom,England,2643116
Manchester,United Kingdom,England,2643123
Maltby,United Kingdom,England,2643144
Maldon,United Kingdom,England,2643160
Maidstone,United Kingdom,England,2643179
Maidenhead,United Kingdom,England,2643186
Maghull,United Kingdom,England,2643198
Maesteg,United Kingdom,Wales,2643218
Macclesfield,United Kingdom,England,2643266
Luton,United Kingdom,England,2643339
Lowestoft,United Kingdom,England,2643490
Louth,United Kingdom,England,2643553
Loughborough,United Kingdom,England,2643567
Longfield,United Kingdom,England,2643696
Long Eaton,United Kingdom,England,2643697
Londonderry County Borough,United Kingdom,Northern Ireland,2643734
Derry,United Kingdom,Northern Ireland,2643736
City of London,United Kingdom,England,2643741
London,United Kingdom,England,2643743
Lofthouse,United Kingdom,England,2643776
Llanelli,United Kingdom,Wales,2644100
Llandudno,United Kingdom,Wales,2644120
Livingston,United Kingdom,Scotland,2644204
Liverpool,United Kingdom,England,2644210
Littlehampton,United Kingdom,England,2644319
Litherland,United Kingdom,England,2644386
Lisburn,United Kingdom,Northern Ireland,2644411
Lincoln,United Kingdom,England,2644487
Lichfield,United Kingdom,England,2644531
Leyland,United Kingdom,England,2644547
Lewes,United Kingdom,England,2644559
Letchworth,United Kingdom,England,2644597
Leighton Buzzard,United Kingdom,England,2644652
Leigh,United Kingdom,England,2644660
Leicester,United Kingdom,England,2644668
Leek,United Kingdom,England,2644684
Leeds,United Kingdom,England,2644688
Leatherhead,United Kingdom,England,2644726
Royal Leamington Spa,United Kingdom,England,2644737
Larne,United Kingdom,Northern Ireland,2644849
Larkhall,United Kingdom,Scotland,2644853
Lancaster,United Kingdom,England,2644972
Kirkintilloch,United Kingdom,Scotland,2645261
Kirkcaldy,United Kingdom,Scotland,2645298
Kirkby in Ashfield,United Kingdom,England,2645309
Kirkby,United Kingdom,England,2645313
Kingswood,United Kingdom,England,2645418
Kingswinford,United Kingdom,England,2645420
Hull,United Kingdom,England,2645425
King's Lynn,United Kingdom,England,2645456
Kilwinning,United Kingdom,Scotland,2645541
Kilmarnock,United Kingdom,Scotland,2645605
Kidsgrove,United Kingdom,England,2645721
Kidlington,United Kingdom,England,2645722
Kidderminster,United Kingdom,England,2645724
Keynsham,United Kingdom,England,2645733
Kettering,United Kingdom,England,2645753
Kenilworth,United Kingdom,England,2645822
Kendal,United Kingdom,England,2645826
Kempston,United Kingdom,England,2645831
Keighley,United Kingdom,England,2645889
Johnstone,United Kingdom,Scotland,2645951
Jarrow,United Kingdom,England,2645972
Islington,United Kingdom,England,2646003
Isleworth,United Kingdom,England,2646004
Irvine,United Kingdom,England,2646032
Coity,United Kingdom,Wales,2652622
Cobham,United Kingdom,England,2652689
Coatbridge,United Kingdom,Scotland,2652696
Coalville,United Kingdom,England,2652698
Clydebank,United Kingdom,Scotland,2652730
Clydach,United Kingdom,Wales,2652734
Clitheroe,United Kingdom,England,2652819
Clevedon,United Kingdom,England,2652861
Cleethorpes,United Kingdom,England,2652885
Cleckheaton,United Kingdom,England,2652890
Clacton-on-Sea,United Kingdom,England,2652974
Cirencester,United Kingdom,England,2652995
Christchurch,United Kingdom,England,2653075
Chorley,United Kingdom,England,2653086
Chislehurst,United Kingdom,England,2653123
Chipping Sodbury,United Kingdom,England,2653137
Chippenham,United Kingdom,England,2653144
Chichester,United Kingdom,England,2653192
Chester-le-Street,United Kingdom,England,2653224
Chesterfield,United Kingdom,England,2653225
Chester,United Kingdom,England,2653228
Chessington,United Kingdom,England,2653229
Cheshunt,United Kingdom,England,2653232
Chesham,United Kingdom,England,2653235
Cheltenham,United Kingdom,England,2653261
Chelsea,United Kingdom,England,2653265
Chelmsford,United Kingdom,England,2653266
Cheadle Hulme,United Kingdom,England,2653290
Chatham,United Kingdom,England,2653305
Chapletown,United Kingdom,England,2653353
Chalfont Saint Peter,United Kingdom,England,2653393
Caterham,United Kingdom,England,2653520
Castlereagh,United Kingdom,Northern Ireland,2653558
Castleford,United Kingdom,England,2653584
Carshalton,United Kingdom,England,2653646
Carrickfergus,United Kingdom,Northern Ireland,2653680
Carmarthen,United Kingdom,Wales,2653755
Carlisle,United Kingdom,England,2653775
Cardiff,United Kingdom,Wales,2653822
Canterbury,United Kingdom,England,2653877
Cannock,United Kingdom,England,2653883
Cambridge,United Kingdom,England,2653941
Camborne,United Kingdom,England,2653945
Camberley,United Kingdom,England,2653947
Caerphilly,United Kingdom,Wales,2654089
Buxton,United Kingdom,England,2654141
Bushey,United Kingdom,England,2654179
Bury St Edmunds,United Kingdom,England,2654186
Bury,United Kingdom,England,2654187
Burton upon Trent,United Kingdom,England,2654200
Burntwood,United Kingdom,England,2654252
Burnley,United Kingdom,England,2654264
Burnham-on-Sea,United Kingdom,England,2654269
Burgess Hill,United Kingdom,England,2654308
Buckley,United Kingdom,Wales,2654394
Buckhaven,United Kingdom,Scotland,2654415
Brymbo,United Kingdom,Wales,2654450
Brownhills,United Kingdom,England,2654490
Bromsgrove,United Kingdom,England,2654579
Broadstairs,United Kingdom,England,2654635
Brixham,United Kingdom,England,2654663
Briton Ferry,United Kingdom,Wales,2654668
Bristol,United Kingdom,England,2654675
Brighton,United Kingdom,England,2654710
Brighouse,United Kingdom,England,2654715
Brierley Hill,United Kingdom,England,2654724
Bridlington,United Kingdom,England,2654728
Bridgwater,United Kingdom,England,2654730
Bridgend,United Kingdom,Wales,2654755
Brentwood,United Kingdom,England,2654782
Bredbury,United Kingdom,England,2654814
Bramhall,United Kingdom,England,2654927
Braintree,United Kingdom,England,2654938
Bradford,United Kingdom,England,2654993
Bracknell,United Kingdom,England,2655009
Bournemouth,United Kingdom,England,2655095
Boston,United Kingdom,England,2655138
Borehamwood,United Kingdom,England,2655186
Bootle,United Kingdom,England,2655198
Bolton,United Kingdom,England,2655237
Bognor Regis,United Kingdom,England,2655262
Blyth,United Kingdom,England,2655315
Bloxwich,United Kingdom,England,2655329
Bletchley,United Kingdom,England,2655351
Blackpool,United Kingdom,England,2655459
Blackburn,United Kingdom,England,2655524
Bishopstoke,United Kingdom,England,2655557
Bishops Stortford,United Kingdom,England,2655562
Bishopbriggs,United Kingdom,Scotland,2655582
Bishop Auckland,United Kingdom,England,2655583
Birmingham,United Kingdom,England,2655603
Birkenhead,United Kingdom,England,2655613
Bingley,United Kingdom,England,2655642
Billingham,United Kingdom,England,2655664
Billericay,United Kingdom,England,2655672
Biggleswade,United Kingdom,England,2655689
Bideford,United Kingdom,England,2655707
Biddulph,United Kingdom,England,2655708
Bicester,United Kingdom,England,2655729
Bexley,United Kingdom,England,2655775
Bexhill-on-Sea,United Kingdom,England,2655777
Beverley,United Kingdom,England,2655785
Berwick-Upon-Tweed,United Kingdom,England,2655819
Berkhamsted,United Kingdom,England,2655858
Bentley,United Kingdom,England,2655882
Belper,United Kingdom,England,2655942
Bellshill,United Kingdom,Scotland,2655952
Belfast,United Kingdom,Northern Ireland,2655984
Bedworth,United Kingdom,England,2656031
Bedlington,United Kingdom,England,2656039
Bedford,United Kingdom,England,2656046
Beckenham,United Kingdom,England,2656065
Bebington,United Kingdom,England,2656070
Bearsden,United Kingdom,Scotland,2656086
Batley,United Kingdom,England,2656168
Bathgate,United Kingdom,Scotland,2656169
Bath,United Kingdom,England,2656173
Basingstoke,United Kingdom,England,2656192
Basildon,United Kingdom,England,2656194
Barry,United Kingdom,Wales,2656235
Barrow in Furness,United Kingdom,England,2656241
Barrhead,United Kingdom,Scotland,2656258
Barnstaple,United Kingdom,England,2656281
Barnsley,United Kingdom,England,2656284
Barnet,United Kingdom,England,2656295
Barking,United Kingdom,England,2656333
Banstead,United Kingdom,England,2656379
Bangor,United Kingdom,Northern Ireland,2656396
Bangor,United Kingdom,Wales,2656397
Banbury,United Kingdom,England,2656406
Banbridge,United Kingdom,Northern Ireland,2656407
Ballymena,United Kingdom,Northern Ireland,2656490
Baildon,United Kingdom,England,2656627
Ayr,United Kingdom,Scotland,2656708
Aylesbury,United Kingdom,England,2656719
Atherton,United Kingdom,England,2656847
Ashton-under-Lyne,United Kingdom,England,2656915
Ashton in Makerfield,United Kingdom,England,2656918
Ashford,United Kingdom,England,2656955
Ascot,United Kingdom,England,2656992
Arnold,United Kingdom,England,2657030
Arbroath,United Kingdom,Scotland,2657215
Antrim,United Kingdom,Northern Ireland,2657255
Andover,United Kingdom,England,2657324
Amersham,United Kingdom,England,2657356
Altrincham,United Kingdom,England,2657402
Alton,United Kingdom,England,2657408
Alloa,United Kingdom,Scotland,2657471
Alfreton,United Kingdom,England,2657508
Aldridge,United Kingdom,England,2657528
Aldershot,United Kingdom,England,2657540
Airdrie,United Kingdom,Scotland,2657613
Acton,United Kingdom,England,2657697
Acocks Green,United Kingdom,England,2657703
Accrington,United Kingdom,England,2657770
Abingdon,United Kingdom,England,2657780
Aberystwyth,United Kingdom,Wales,2657782
Abergele,United Kingdom,Wales,2657812
Aberdeen,United Kingdom,Scotland,2657832
Aberdare,United Kingdom,Wales,2657835
Crosby,United Kingdom,England,3209584
Blackwood,United Kingdom,Wales,3345317
Neston,United Kingdom,England,3345432
Camden Town,United Kingdom,England,3345437
Telford,United Kingdom,England,3345439
Craigavon,United Kingdom,Northern Ireland,3345440
Bayswater,United Kingdom,England,6545243
Yateley,United Kingdom,England,6620293
Bowthorpe,United Kingdom,England,6620355
Hedge End,United Kingdom,England,6620360
Erskine,United Kingdom,Scotland,6639623
Hale,United Kingdom,England,6640028
Amersham on the Hill,United Kingdom,England,6690592
Battersea,United Kingdom,England,6690602
South Croydon,United Kingdom,England,6690862
Hornchurch,United Kingdom,England,6690863
Surbiton,United Kingdom,England,6690866
Ewell,United Kingdom,England,6690867
Becontree,United Kingdom,England,6690870
Brixton,United Kingdom,England,6690877
Bethnal Green,United Kingdom,England,6690989
Failsworth,United Kingdom,England,6691219
Radcliffe,United Kingdom,England,6691227
Heywood,United Kingdom,England,6691235
Longsight,United Kingdom,England,6691766
Heavitree,United Kingdom,England,6691884
Ferndown,United Kingdom,England,6691927
Canary Wharf,United Kingdom,England,6692280
Lytham St Annes,United Kingdom,England,6693470
Hadley Wood,United Kingdom,England,6693771
Chapel Allerton,United Kingdom,England,6695247
Blackheath,United Kingdom,England,6947041
Kempston Hardwick,United Kingdom,England,6947168
Mendip,United Kingdom,England,6947756
Lower Earley,United Kingdom,England,7290015
Bartley Green,United Kingdom,England,7302130
Earlsfield,United Kingdom,England,8063096
Letchworth Garden City,United Kingdom,England,8224216
Shirley,United Kingdom,England,8224782
Stanley,United Kingdom,England,8224783
Rossendale,United Kingdom,England,8299614
Thornton-Cleveleys,United Kingdom,England,8299615
Deeside,United Kingdom,Wales,8299616
High Peak,United Kingdom,England,8299617
Hayling Island,United Kingdom,England,8299619
Isle of Lewis,United Kingdom,Scotland,8299620
Shetland,United Kingdom,Scotland,8299621
Orkney,United Kingdom,Scotland,8299623
Holloway,United Kingdom,England,8315400
Harringay,United Kingdom,England,8581595
Saint George's,Grenada,Saint George,3579925
Zugdidi,Georgia,Samegrelo and Zemo Svaneti,610824
Zestapâ€™oni,Georgia,Imereti,610864
Tsâ€™khinvali,Georgia,Shida Kartli,611403
Tqvarch'eli,Georgia,Abkhazia,611583
Telavi,Georgia,Kakheti,611694
Tbilisi,Georgia,T'bilisi,611717
Sokhumi,Georgia,Abkhazia,611847
Senakâ€™i,Georgia,Samegrelo and Zemo Svaneti,612053
Samtredia,Georgia,Imereti,612126
Rustâ€™avi,Georgia,Kvemo Kartli,612287
Pâ€™otâ€™i,Georgia,Samegrelo and Zemo Svaneti,612366
Ozurgeti,Georgia,Guria,612536
Ochâ€™amchâ€™ire,Georgia,Abkhazia,612652
Marneuli,Georgia,Kvemo Kartli,613074
Kutaisi,Georgia,Imereti,613607
Kobuleti,Georgia,Ajaria,613762
Khashuri,Georgia,Shida Kartli,613988
Gori,Georgia,Shida Kartli,614455
Batumi,Georgia,Ajaria,615532
Akhaltsikhe,Georgia,Samtskhe-Javakheti,615860
Stantsiya Novyy Afon,Georgia,Abkhazia,615912
Tsqaltubo,Georgia,Imereti,824288
Saint-Laurent-du-Maroni,French Guiana,Guyane,3380387
RÃ©mire-Montjoly,French Guiana,Guyane,3380892
Matoury,French Guiana,Guyane,3380965
Kourou,French Guiana,Guyane,3381303
Cayenne,French Guiana,Guyane,3382160
Saint Peter Port,Guernsey,St Peter Port,3042287
Yendi,Ghana,Northern,2293801
Winneba,Ghana,Central,2294034
Wenchi,Ghana,Brong-Ahafo,2294086
Wa,Ghana,Upper West,2294206
Teshi Old Town,Ghana,Greater Accra,2294665
Tema,Ghana,Greater Accra,2294700
Techiman,Ghana,Brong-Ahafo,2294727
Tarkwa,Ghana,Western,2294768
Tamale,Ghana,Northern,2294877
Takoradi,Ghana,Western,2294915
Tafo,Ghana,Ashanti,2294938
Swedru,Ghana,Central,2294962
Sunyani,Ghana,Brong-Ahafo,2295021
Suhum,Ghana,Eastern,2295065
Shama Junction,Ghana,Western,2295385
Sekondi-Takoradi,Ghana,Western,2295458
Savelugu,Ghana,Northern,2295517
Saltpond,Ghana,Central,2295672
Salaga,Ghana,Northern,2295684
Prestea,Ghana,Western,2295840
Kasoa,Ghana,Central,2296458
Akim Oda,Ghana,Eastern,2296564
Obuasi,Ghana,Ashanti,2296606
Nungua,Ghana,Greater Accra,2296969
Nsawam,Ghana,Eastern,2297141
Nkawkaw,Ghana,Eastern,2297313
Navrongo,Ghana,Upper East,2297505
Mampong,Ghana,Ashanti,2298264
Medina Estates,Ghana,Greater Accra,2298330
Kumasi,Ghana,Ashanti,2298890
Kpandu,Ghana,Volta,2299233
Konongo,Ghana,Ashanti,2299349
Koforidua,Ghana,Eastern,2299522
Kintampo,Ghana,Brong-Ahafo,2299625
Keta,Ghana,Volta,2299645
Hohoe,Ghana,Volta,2300372
Ho,Ghana,Volta,2300379
Gbawe,Ghana,Greater Accra,2300721
Foso,Ghana,Central,2300883
Elmina,Ghana,Central,2301190
Ejura,Ghana,Ashanti,2301217
Dunkwa,Ghana,Central,2301400
Dome,Ghana,Greater Accra,2301639
Cape Coast,Ghana,Central,2302357
Bolgatanga,Ghana,Upper East,2302821
Bibiani,Ghana,Western,2303060
Berekum,Ghana,Brong-Ahafo,2303125
Begoro,Ghana,Eastern,2303236
Bawku,Ghana,Upper East,2303287
Axim,Ghana,Western,2303611
Asamankese,Ghana,Eastern,2304220
Apam,Ghana,Central,2304389
Anloga,Ghana,Volta,2304548
Akwatia,Ghana,Eastern,2304931
Agogo,Ghana,Ashanti,2305537
Achiaman,Ghana,Greater Accra,2306079
Accra,Ghana,Greater Accra,2306104
Aburi,Ghana,Eastern,2306119
Gibraltar,Gibraltar,N/A,2411585
Nuuk,Greenland,Sermersooq,3421319
Sukuta,Gambia,Western,2411880
Lamin,Gambia,North Bank,2412749
Farafenni,Gambia,North Bank,2413515
Brikama,Gambia,Western,2413753
Banjul,Gambia,Banjul,2413876
Bakau,Gambia,Banjul,2413920
TouguÃ©,Guinea,Labe,2414545
TÃ©limÃ©lÃ©,Guinea,Kindia,2414926
Siguiri,Guinea,Kankan,2415703
Pita,Guinea,Mamou,2416443
NzÃ©rÃ©korÃ©,Guinea,Nzerekore,2416969
Mamou,Guinea,Mamou,2417833
Macenta,Guinea,Nzerekore,2417988
LabÃ©,Guinea,Labe,2418362
Kissidougou,Guinea,Faranah,2419472
Kindia,Guinea,Kindia,2419533
Kankan,Guinea,Kankan,2419992
Kamsar,Guinea,Boke,2420056
Gueckedou,Guinea,Nzerekore,2420562
Fria,Guinea,Boke,2420884
Coyah,Guinea,Kindia,2422457
Conakry,Guinea,Conakry,2422465
Camayenne,Guinea,Conakry,2422488
BokÃ©,Guinea,Boke,2422924
Sainte-Rose,Guadeloupe,Guadeloupe,3578447
Sainte-Anne,Guadeloupe,Guadeloupe,3578466
Pointe-Ã -Pitre,Guadeloupe,Guadeloupe,3578599
Petit-Bourg,Guadeloupe,Guadeloupe,3578682
Les Abymes,Guadeloupe,Guadeloupe,3578959
Le Moule,Guadeloupe,Guadeloupe,3578967
Le Gosier,Guadeloupe,Guadeloupe,3578978
Capesterre-Belle-Eau,Guadeloupe,Guadeloupe,3579585
Basse-Terre,Guadeloupe,Guadeloupe,3579732
Baie-Mahault,Guadeloupe,Guadeloupe,3579767
Ebebiyin,Equatorial Guinea,KiÃ©-Ntem,2309332
Malabo,Equatorial Guinea,Bioko Norte,2309527
Bata,Equatorial Guinea,Litoral,2310046
VoÃºla,Greece,Attica,251780
VÃ³los,Greece,Thessaly,251833
VÃ½ronas,Greece,Attica,251948
VÃ¡ri,Greece,Attica,252270
TrÃ­poli,Greece,Peloponnese,252601
TrÃ­kala,Greece,Thessaly,252664
ThÃ­vai,Greece,Central Greece,252910
SpÃ¡rti,Greece,Peloponnese,253394
SalamÃ­na,Greece,Attica,254144
Rethymno,Greece,Crete,254352
PrÃ©veza,Greece,Epirus,254698
PÃ½rgos,Greece,West Greece,255229
Piraeus,Greece,Attica,255274
PetroÃºpolis,Greece,Attica,255377
PeristÃ©ri,Greece,Attica,255524
PÃ©rama,Greece,Attica,255588
PÃ¡tra,Greece,West Greece,255683
PalaiÃ³ FÃ¡liro,Greece,Attica,256075
NÃ­kaia,Greece,Attica,256429
NÃ©a SmÃ½rni,Greece,Attica,256575
NÃ©a MÃ¡kri,Greece,Attica,256598
Ãlion,Greece,Attica,256601
NÃ©a IonÃ­a,Greece,Attica,256614
NÃ©a FiladÃ©lfeia,Greece,Attica,256621
NÃ©a ErythraÃ­a,Greece,Attica,256622
MoskhÃ¡ton,Greece,Attica,256750
MytilÃ­ni,Greece,North Aegean,256866
MelÃ­ssia,Greece,Attica,257302
MÃ©gara,Greece,Attica,257365
ArtÃ©mida,Greece,Attica,258038
LivadeiÃ¡,Greece,Central Greece,258463
LÃ¡risa,Greece,Thessaly,258576
LamÃ­a,Greece,Central Greece,258620
MetamÃ³rfosi,Greece,Attica,259128
Kos,Greece,South Aegean,259245
KoropÃ­,Greece,Attica,259251
KÃ³rinthos,Greece,Peloponnese,259289
KifisiÃ¡,Greece,Attica,259824
CholargÃ³s,Greece,Attica,259949
Chios,Greece,North Aegean,259973
ChaniÃ¡,Greece,Crete,260114
ChalkÃ­da,Greece,Central Greece,260133
KhalÃ¡ndrion,Greece,Attica,260172
ChaÃ¯dÃ¡ri,Greece,Attica,260183
KeratsÃ­ni,Greece,Attica,260204
KardÃ­tsa,Greece,Thessaly,260989
KamaterÃ³n,Greece,Attica,261249
KallithÃ©a,Greece,Attica,261414
KalamÃ¡ta,Greece,Peloponnese,261604
Ãlimos,Greece,Attica,261614
KaisarianÃ­,Greece,Attica,261678
IrÃ¡kleio,Greece,Attica,261743
IrÃ¡kleion,Greece,Crete,261745
IoÃ¡nnina,Greece,Epirus,261779
GlyfÃ¡da,Greece,Attica,262036
GalÃ¡tsi,Greece,Attica,262135
EllinikÃ³,Greece,Attica,262719
ElefsÃ­na,Greece,Attica,262752
DhafnÃ­,Greece,Attica,263312
Agios Dimitrios,Greece,Attica,263986
AgÃ­a VarvÃ¡ra,Greece,Attica,264111
AgÃ­a ParaskevÃ­,Greece,Attica,264194
Athens,Greece,Attica,264371
AsprÃ³pyrgos,Greece,Attica,264445
ArgyroÃºpoli,Greece,Attica,264516
Ãrta,Greece,Epirus,264559
Ãrgos,Greece,Peloponnese,264670
Ãno LiÃ³sia,Greece,Attica,264888
MaroÃºsi,Greece,Attica,265243
AmaliÃ¡da,Greece,West Greece,265252
AcharnÃ©s,Greece,Attica,265488
AÃ­gio,Greece,West Greece,265500
AigÃ¡leo,Greece,Attica,265533
AgrÃ­nio,Greece,West Greece,265560
RÃ³dos,Greece,South Aegean,400666
GiannitsÃ¡,Greece,Central Macedonia,733776
XÃ¡nthi,Greece,East Macedonia and Thrace,733840
VÃ©roia,Greece,Central Macedonia,733905
ThessalonÃ­ki,Greece,Central Macedonia,734077
SykiÃ©s,Greece,Central Macedonia,734301
SÃ©rres,Greece,Central Macedonia,734330
Ptolemaá¸¯da,Greece,West Macedonia,734426
PolÃ­chni,Greece,Central Macedonia,734538
PylaÃ­a,Greece,Central Macedonia,734643
PeraÃ­a,Greece,Central Macedonia,734712
PanÃ³rama,Greece,Central Macedonia,734771
OrestiÃ¡da,Greece,East Macedonia and Thrace,734880
OraiÃ³kastro,Greece,Central Macedonia,734883
NÃ¡ousa,Greece,Central Macedonia,735030
MenemÃ©ni,Greece,Central Macedonia,735215
KozÃ¡ni,Greece,West Macedonia,735563
KomotinÃ­,Greece,East Macedonia and Thrace,735640
KilkÃ­s,Greece,Central Macedonia,735736
KavÃ¡la,Greece,East Macedonia and Thrace,735861
KaterÃ­ni,Greece,Central Macedonia,735914
KalamariÃ¡,Greece,Central Macedonia,736083
FlÃ³rina,Greece,West Macedonia,736229
Ã‰dessa,Greece,Central Macedonia,736357
DrÃ¡ma,Greece,East Macedonia and Thrace,736364
AlexandroÃºpoli,Greece,East Macedonia and Thrace,736928
Corfu,Greece,Ionian Islands,2463679
Vrilissia,Greece,Attica,6324534
GÃ©rakas,Greece,Attica,8201845
IlioÃºpoli,Greece,Attica,8310138
KorydallÃ³s,Greece,Attica,8310183
ZogrÃ¡fos,Greece,Attica,8358544
PÃ©fki,Greece,Attica,8358562
Ãgioi AnÃ¡rgyroi,Greece,Attica,8358563
Agios Ioannis Rentis,Greece,Attica,8478257
NÃ©a IonÃ­a,Greece,Thessaly,9034728
Grytviken,South Georgia and the South Sandwich Islands,N/A,3426466
Zacapa,Guatemala,Zacapa,3587587
Villa Nueva,Guatemala,Guatemala,3587902
Villa Canales,Guatemala,Guatemala,3587923
TotonicapÃ¡n,Guatemala,TotonicapÃ¡n,3588258
TecpÃ¡n Guatemala,Guatemala,Chimaltenango,3588476
Sumpango,Guatemala,SacatepÃ©quez,3588653
SololÃ¡,Guatemala,SololÃ¡,3588698
Santiago SacatepÃ©quez,Guatemala,SacatepÃ©quez,3589101
Santiago AtitlÃ¡n,Guatemala,SololÃ¡,3589105
Santa MarÃ­a de JesÃºs,Guatemala,SacatepÃ©quez,3589253
Santa LucÃ­a Cotzumalguapa,Guatemala,Escuintla,3589289
Santa Cruz del QuichÃ©,Guatemala,QuichÃ©,3589404
Santa Catarina Pinula,Guatemala,Guatemala,3589452
San Pedro SacatepÃ©quez,Guatemala,San Marcos,3589626
San Pedro Ayampuc,Guatemala,Guatemala,3589646
San Pablo Jocopilas,Guatemala,Suchitepeque,3589671
San Marcos,Guatemala,San Marcos,3589805
San Lucas SacatepÃ©quez,Guatemala,SacatepÃ©quez,3589852
San Juan SacatepÃ©quez,Guatemala,Guatemala,3589885
San JosÃ© Pinula,Guatemala,Guatemala,3589977
San Francisco El Alto,Guatemala,TotonicapÃ¡n,3590219
San CristÃ³bal Verapaz,Guatemala,Alta Verapaz,3590316
San Benito,Guatemala,PetÃ©n,3590389
Sanarate,Guatemala,El Progreso,3590406
San AndrÃ©s Itzapa,Guatemala,Chimaltenango,3590529
SalamÃ¡,Guatemala,Baja Verapaz,3590616
Retalhuleu,Guatemala,Retalhuleu,3590858
Quetzaltenango,Guatemala,Quetzaltenango,3590979
Puerto San JosÃ©,Guatemala,Escuintla,3591060
Puerto Barrios,Guatemala,Izabal,3591062
Tiquisate,Guatemala,Escuintla,3591093
PoptÃºn,Guatemala,PetÃ©n,3591181
Petapa,Guatemala,Guatemala,3591415
PatzÃºn,Guatemala,Chimaltenango,3591512
PatzicÃ­a,Guatemala,Chimaltenango,3591523
PanzÃ³s,Guatemala,Alta Verapaz,3591676
PalÃ­n,Guatemala,Escuintla,3591833
Palencia,Guatemala,Guatemala,3591851
Ostuncalco,Guatemala,Quetzaltenango,3591997
Nuevo San Carlos,Guatemala,Retalhuleu,3592105
Nebaj,Guatemala,QuichÃ©,3592237
NahualÃ¡,Guatemala,SololÃ¡,3592286
Morales,Guatemala,Izabal,3592362
Momostenango,Guatemala,TotonicapÃ¡n,3592483
Mixco,Guatemala,Guatemala,3592519
Mazatenango,Guatemala,Suchitepeque,3592609
La Gomera,Guatemala,Escuintla,3594575
La Esperanza,Guatemala,Quetzaltenango,3594703
Jutiapa,Guatemala,Jutiapa,3595069
Jocotenango,Guatemala,SacatepÃ©quez,3595171
Jalapa,Guatemala,Jalapa,3595237
Jacaltenango,Guatemala,Huehuetenango,3595248
Huehuetenango,Guatemala,Huehuetenango,3595416
GualÃ¡n,Guatemala,Zacapa,3595560
Fraijanes,Guatemala,Guatemala,3595714
Flores,Guatemala,PetÃ©n,3595725
Esquipulas,Guatemala,Chiquimula,3595783
Escuintla,Guatemala,Escuintla,3595803
El Tejar,Guatemala,Chimaltenango,3596041
El Palmar,Guatemala,Quetzaltenango,3596644
El Estor,Guatemala,Izabal,3597078
Cuilapa,Guatemala,Santa Rosa,3597804
Comitancillo,Guatemala,San Marcos,3598025
Comalapa,Guatemala,Chimaltenango,3598034
Colomba,Guatemala,Quetzaltenango,3598073
CobÃ¡n,Guatemala,Alta Verapaz,3598119
Coatepeque,Guatemala,Quetzaltenango,3598122
Ciudad Vieja,Guatemala,SacatepÃ©quez,3598128
Guatemala City,Guatemala,Guatemala,3598132
Chisec,Guatemala,Alta Verapaz,3598415
Chiquimula,Guatemala,Chiquimula,3598465
Chinautla,Guatemala,Guatemala,3598529
Chimaltenango,Guatemala,Chimaltenango,3598572
Chichicastenango,Guatemala,QuichÃ©,3598655
Chicacao,Guatemala,Suchitepeque,3598678
Cantel,Guatemala,Quetzaltenango,3599069
Barberena,Guatemala,Santa Rosa,3599582
AsunciÃ³n Mita,Guatemala,Jutiapa,3599639
Antigua Guatemala,Guatemala,SacatepÃ©quez,3599699
AmatitlÃ¡n,Guatemala,Guatemala,3599735
Alotenango,Guatemala,SacatepÃ©quez,3599788
Tamuning-Tumon-Harmon Village,Guam,Tamuning,4038659
Yigo Village,Guam,Yigo,4038794
Guam Government House,Guam,Hagatna,4043547
Dededo Village,Guam,Dededo,4043909
HagÃ¥tÃ±a,Guam,Hagatna,4044012
Mangilao Village,Guam,Mangilao,7268049
Bissau,Guinea-Bissau,Bissau,2374775
BafatÃ¡,Guinea-Bissau,BafatÃ¡,2375254
New Amsterdam,Guyana,East Berbice-Corentyne,3376762
Linden,Guyana,Upper Demerara-Berbice,3377408
Georgetown,Guyana,Demerara-Mahaica,3378644
Tsuen Wan,Hong Kong,Tsuen Wan,1818209
Yuen Long Kau Hui,Hong Kong,Yuen Long,1818223
Tuen Mun,Hong Kong,Tuen Mun,1818446
Tai Po,Hong Kong,Tai Po,1818673
Sha Tin,Hong Kong,Sha Tin,1818920
Kowloon,Hong Kong,Kowloon City,1819609
Hong Kong,Hong Kong,Central and Western,1819729
Puerto Cortez,Honduras,CortÃ©s,3600026
Yoro,Honduras,Yoro,3600195
Villanueva,Honduras,CortÃ©s,3600327
Tocoa,Honduras,ColÃ³n,3600704
Tela,Honduras,AtlÃ¡ntida,3600931
Tegucigalpa,Honduras,Francisco MorazÃ¡n,3600949
Siguatepeque,Honduras,Comayagua,3601311
Santa Rosa de CopÃ¡n,Honduras,CopÃ¡n,3601494
Santa BÃ¡rbara,Honduras,Santa BÃ¡rbara,3601691
San Pedro Sula,Honduras,CortÃ©s,3601782
San Lorenzo,Honduras,Valle,3601977
Potrerillos,Honduras,CortÃ©s,3603330
Olanchito,Honduras,Yoro,3604251
La Paz,Honduras,La Paz,3607254
La Lima,Honduras,CortÃ©s,3607511
La Ceiba,Honduras,AtlÃ¡ntida,3608248
Juticalpa,Honduras,Olancho,3608503
El Progreso,Honduras,Yoro,3610613
El ParaÃ­so,Honduras,El ParaÃ­so,3610965
DanlÃ­,Honduras,El ParaÃ­so,3612907
Comayagua,Honduras,Comayagua,3613321
CofradÃ­a,Honduras,CortÃ©s,3613394
Ciudad Choluteca,Honduras,Choluteca,3613528
Choloma,Honduras,CortÃ©s,3613533
ZapreÅ¡iÄ‡,Croatia,ZagrebaÄka,3186781
Zagreb,Croatia,Grad Zagreb,3186886
Zadar,Croatia,Zadarska,3186952
Vukovar,Croatia,Vukovarsko-Srijemska,3187047
Virovitica,Croatia,VirovitiÄk-Podravska,3187694
Vinkovci,Croatia,Vukovarsko-Srijemska,3187719
Velika Gorica,Croatia,ZagrebaÄka,3188244
VaraÅ¾din,Croatia,VaraÅ¾dinska,3188383
Split,Croatia,Splitsko-Dalmatinska,3190261
Solin,Croatia,Splitsko-Dalmatinska,3190359
Slavonski Brod,Croatia,Brodsko-Posavska,3190586
PoÅ¾ega,Croatia,PoÅ¾eÅ¡ko-Slavonska,3190589
Sisak,Croatia,SisaÄko-MoslavaÄka,3190813
Å ibenik,Croatia,Å ibensko-Kniniska,3190941
Sesvete,Croatia,Grad Zagreb,3190966
Samobor,Croatia,ZagrebaÄka,3191316
Rijeka,Croatia,Primorsko-Goranska,3191648
Pula,Croatia,Istarska,3192224
Osijek,Croatia,OsjeÄko-Baranjska,3193935
Koprivnica,Croatia,KoprivniÄko-KriÅ¾evaÄka,3197728
Karlovac,Croatia,KarlovaÄka,3198259
Dubrovnik,Croatia,DubrovaÄko-Neretvanska,3201047
ÄŒakovec,Croatia,MeÄ‘imurska,3202888
Bjelovar,Croatia,Bjelovarsko-Bilogorska,3203982
Zagreb- Stenjevec,Croatia,Grad Zagreb,3209380
Zagreb - Centar,Croatia,Grad Zagreb,6618983
Verrettes,Haiti,Artibonite,3716044
Thomazeau,Haiti,Ouest,3716667
Saint-RaphaÃ«l,Haiti,Nord,3717546
Saint-Marc,Haiti,Artibonite,3717588
Port-de-Paix,Haiti,Nord-Ouest,3718420
Port-au-Prince,Haiti,Ouest,3718426
Tigwav,Haiti,Ouest,3718962
PÃ©tionville,Haiti,Ouest,3719028
MiragoÃ¢ne,Haiti,Nippes,3720824
Lenbe,Haiti,Nord,3722124
LÃ©ogÃ¢ne,Haiti,Ouest,3722286
Kenscoff,Haiti,Ouest,3723440
JÃ©rÃ©mie,Haiti,GrandÊ¼Anse,3723593
Jacmel,Haiti,Sud-Est,3723779
Hinche,Haiti,Centre,3723841
Gressier,Haiti,Ouest,3724233
Grangwav,Haiti,Ouest,3724337
Gonayiv,Haiti,Artibonite,3724696
Fond Parisien,Haiti,Ouest,3725276
DÃ©sarmes,Haiti,Artibonite,3726674
Delmas 73,Haiti,Ouest,3726786
Croix des Bouquets,Haiti,Ouest,3727135
Les Cayes,Haiti,Sud,3728097
Carrefour,Haiti,Ouest,3728338
Okap,Haiti,Nord,3728474
Ti Port-de-Paix,Haiti,Nord-Ouest,3740016
TÃ¶rÃ¶kszentmiklÃ³s,Hungary,JÃ¡sz-Nagykun-Szolnok,714581
TiszaÃºjvÃ¡ros,Hungary,Borsod-AbaÃºj-ZemplÃ©n,714697
Szolnok,Hungary,JÃ¡sz-Nagykun-Szolnok,715126
Szentes,Hungary,CsongrÃ¡d,715338
Szeged,Hungary,CsongrÃ¡d,715429
Szarvas,Hungary,Bekes,715466
SÃ¡toraljaÃºjhely,Hungary,Borsod-AbaÃºj-ZemplÃ©n,715839
PÃ¼spÃ¶kladÃ¡ny,Hungary,HajdÃº-Bihar,716301
Ã“zd,Hungary,Borsod-AbaÃºj-ZemplÃ©n,716671
OroshÃ¡za,Hungary,Bekes,716736
NyÃ­regyhÃ¡za,Hungary,Szabolcs-SzatmÃ¡r-Bereg,716935
Miskolc,Hungary,Borsod-AbaÃºj-ZemplÃ©n,717582
MezÅ‘tÃºr,Hungary,JÃ¡sz-Nagykun-Szolnok,717635
MezÅ‘kÃ¶vesd,Hungary,Borsod-AbaÃºj-ZemplÃ©n,717652
MÃ¡tÃ©szalka,Hungary,Szabolcs-SzatmÃ¡r-Bereg,717771
MakÃ³,Hungary,CsongrÃ¡d,717902
KisvÃ¡rda,Hungary,Szabolcs-SzatmÃ¡r-Bereg,718739
Kazincbarcika,Hungary,Borsod-AbaÃºj-ZemplÃ©n,719311
Karcag,Hungary,JÃ¡sz-Nagykun-Szolnok,719404
HÃ³dmezÅ‘vÃ¡sÃ¡rhely,Hungary,CsongrÃ¡d,719965
HajdÃºszoboszlÃ³,Hungary,HajdÃº-Bihar,720276
HajdÃºnÃ¡nÃ¡s,Hungary,HajdÃº-Bihar,720284
HajdÃºbÃ¶szÃ¶rmÃ©ny,Hungary,HajdÃº-Bihar,720292
Gyula,Hungary,Bekes,720334
GyomaendrÅ‘d,Hungary,Bekes,720364
Eger,Hungary,Heves,721239
Debrecen,Hungary,HajdÃº-Bihar,721472
CsongrÃ¡d,Hungary,CsongrÃ¡d,721592
BerettyÃ³Ãºjfalu,Hungary,HajdÃº-Bihar,722324
BÃ©kÃ©scsaba,Hungary,Bekes,722437
BÃ©kÃ©s,Hungary,Bekes,722439
BalmazÃºjvÃ¡ros,Hungary,HajdÃº-Bihar,722636
Abony,Hungary,Pest,723030
Zalaegerszeg,Hungary,Zala,3042638
VeszprÃ©m,Hungary,VeszprÃ©m,3042929
VecsÃ©s,Hungary,Pest,3043019
VÃ¡rpalota,Hungary,VeszprÃ©m,3043095
VÃ¡c,Hungary,Pest,3043293
TatabÃ¡nya,Hungary,KomÃ¡rom-Esztergom,3044082
Tata,Hungary,KomÃ¡rom-Esztergom,3044083
Tapolca,Hungary,VeszprÃ©m,3044141
Szombathely,Hungary,Vas,3044310
SzigetszentmiklÃ³s,Hungary,Pest,3044475
Szentendre,Hungary,Pest,3044681
SzekszÃ¡rd,Hungary,Tolna,3044760
SzÃ©kesfehÃ©rvÃ¡r,Hungary,FejÃ©r,3044774
SzÃ¡zhalombatta,Hungary,Pest,3044821
Sopron,Hungary,GyÅ‘r-Moson-Sopron,3045190
SiÃ³fok,Hungary,Somogy,3045332
SÃ¡rvÃ¡r,Hungary,Vas,3045487
SalgÃ³tarjÃ¡n,Hungary,NÃ³grÃ¡d,3045643
PÃ©cs,Hungary,Baranya,3046526
ParÃ¡dsasvÃ¡r,Hungary,Heves,3046619
PÃ¡pa,Hungary,VeszprÃ©m,3046686
Paks,Hungary,Tolna,3046768
OroszlÃ¡ny,Hungary,KomÃ¡rom-Esztergom,3046888
NagykÅ‘rÃ¶s,Hungary,Pest,3047651
Nagykanizsa,Hungary,Zala,3047679
MosonmagyarÃ³vÃ¡r,Hungary,GyÅ‘r-Moson-Sopron,3047896
Monor,Hungary,Pest,3047942
MohÃ¡cs,Hungary,Baranya,3047967
KomlÃ³,Hungary,Baranya,3049512
KomÃ¡rom,Hungary,KomÃ¡rom-Esztergom,3049519
Kiskunhalas,Hungary,BÃ¡cs-Kiskun,3049880
KiskunfÃ©legyhÃ¡za,Hungary,BÃ¡cs-Kiskun,3049885
KiskÅ‘rÃ¶s,Hungary,BÃ¡cs-Kiskun,3049896
Keszthely,Hungary,Zala,3050212
KecskemÃ©t,Hungary,BÃ¡cs-Kiskun,3050434
KaposvÃ¡r,Hungary,Somogy,3050616
Kalocsa,Hungary,BÃ¡cs-Kiskun,3050719
JÃ¡szberÃ©ny,Hungary,JÃ¡sz-Nagykun-Szolnok,3050907
Hatvan,Hungary,Heves,3051621
GyÅ‘r,Hungary,GyÅ‘r-Moson-Sopron,3052009
GyÃ¶ngyÃ¶s,Hungary,Heves,3052040
GyÃ¡l,Hungary,Pest,3052101
GÃ¶dÃ¶llÅ‘,Hungary,Pest,3052236
GÃ¶d,Hungary,Pest,3052241
FÃ³t,Hungary,Pest,3052542
Esztergom,Hungary,KomÃ¡rom-Esztergom,3053163
Ã‰rd,Hungary,Pest,3053281
DunaÃºjvÃ¡ros,Hungary,FejÃ©r,3053438
Dunakeszi,Hungary,Pest,3053476
Dunaharaszti,Hungary,Pest,3053485
DombÃ³vÃ¡r,Hungary,Tolna,3053590
Dabas,Hungary,Pest,3053836
CeglÃ©d,Hungary,Pest,3054543
Budapest,Hungary,Budapest,3054643
BudaÃ¶rs,Hungary,Pest,3054646
Balassagyarmat,Hungary,NÃ³grÃ¡d,3055601
Baja,Hungary,BÃ¡cs-Kiskun,3055685
Ajka,Hungary,VeszprÃ©m,3056357
Budapest XII. kerÃ¼let,Hungary,Budapest,7284823
Budapest XI. kerÃ¼let,Hungary,Budapest,7284824
Budapest IX. kerÃ¼let,Hungary,Budapest,7284825
Budapest VIII. kerÃ¼let,Hungary,Budapest,7284826
Budapest VII. kerÃ¼let,Hungary,Budapest,7284827
Budapest VI. kerÃ¼let,Hungary,Budapest,7284828
Budapest XIV. kerÃ¼let,Hungary,Budapest,7284829
Budapest XIII. kerÃ¼let,Hungary,Budapest,7284830
Budapest IV. kerÃ¼let,Hungary,Budapest,7284831
Budapest XV. kerÃ¼let,Hungary,Budapest,7284832
Budapest XVI. kerÃ¼let,Hungary,Budapest,7284833
Budapest X. kerÃ¼let,Hungary,Budapest,7284834
Budapest XIX. kerÃ¼let,Hungary,Budapest,7284835
Budapest XVIII. kerÃ¼let,Hungary,Budapest,7284836
Budapest XXIII. kerÃ¼let,Hungary,Budapest,7284837
Budapest XXII. kerÃ¼let,Hungary,Budapest,7284838
Budapest XXI. kerÃ¼let,Hungary,Budapest,7284839
Budapest XX. kerÃ¼let,Hungary,Budapest,7284840
Budapest XVII. kerÃ¼let,Hungary,Budapest,7284841
Budapest III. kerÃ¼let,Hungary,Budapest,7284842
Budapest II. kerÃ¼let,Hungary,Budapest,7284843
Budapest I. kerÃ¼let,Hungary,Budapest,7284844
Tongging,Indonesia,North Sumatra,1213442
Teluk Nibung,Indonesia,North Sumatra,1213493
Tebingtinggi,Indonesia,North Sumatra,1213500
Tanjungtiram,Indonesia,North Sumatra,1213530
Tanjungbalai,Indonesia,North Sumatra,1213547
Sunggal,Indonesia,North Sumatra,1213614
Stabat,Indonesia,North Sumatra,1213655
Singkil,Indonesia,Aceh,1213713
Sigli,Indonesia,Aceh,1213821
Sibolga,Indonesia,North Sumatra,1213855
Sabang,Indonesia,Aceh,1214026
Reuleuet,Indonesia,Aceh,1214055
Rantauprapat,Indonesia,North Sumatra,1214073
Percut,Indonesia,North Sumatra,1214189
Perbaungan,Indonesia,North Sumatra,1214191
Pematangsiantar,Indonesia,North Sumatra,1214204
Pangkalan Brandan,Indonesia,North Sumatra,1214302
Padangsidempuan,Indonesia,North Sumatra,1214369
Meulaboh,Indonesia,Aceh,1214488
Medan,Indonesia,North Sumatra,1214520
Lhokseumawe,Indonesia,Aceh,1214658
Langsa,Indonesia,Aceh,1214724
Labuhan Deli,Indonesia,North Sumatra,1214800
Kisaran,Indonesia,North Sumatra,1214882
Kabanjahe,Indonesia,North Sumatra,1214965
Deli Tua,Indonesia,North Sumatra,1215199
Bireun,Indonesia,Aceh,1215350
Binjai,Indonesia,North Sumatra,1215355
Berastagi,Indonesia,North Sumatra,1215395
Belawan,Indonesia,North Sumatra,1215412
Bandar,Indonesia,North Sumatra,1215498
Banda Aceh,Indonesia,Aceh,1215502
Yogyakarta,Indonesia,Daerah Istimewa Yogyakarta,1621177
Wonosobo,Indonesia,Central Java,1621395
Wonopringgo,Indonesia,Central Java,1621416
Wongsorejo,Indonesia,East Java,1621439
Wiradesa,Indonesia,Central Java,1621520
Weru,Indonesia,West Java,1621613
Weleri,Indonesia,Central Java,1621655
Welahan,Indonesia,Central Java,1621659
Wedi,Indonesia,Central Java,1621678
Watampone,Indonesia,South Sulawesi,1621884
Wangon,Indonesia,Central Java,1622090
Wanaraja,Indonesia,West Java,1622138
Waingapu,Indonesia,East Nusa Tenggara,1622318
Ungaran,Indonesia,Central Java,1622636
Makassar,Indonesia,South Sulawesi,1622786
Ubud,Indonesia,Bali,1622846
Tulungagung,Indonesia,East Java,1623080
Tulangan Utara,Indonesia,East Java,1623096
Tuban,Indonesia,East Java,1623180
Tual,Indonesia,Maluku,1623197
Trucuk,Indonesia,Central Java,1623223
Trenggalek,Indonesia,East Java,1623251
Tondano,Indonesia,North Sulawesi,1623424
Tomohon,Indonesia,North Sulawesi,1623446
Ternate,Indonesia,Maluku Utara,1624041
Terbanggi Besar,Indonesia,Lampung,1624058
Tegal,Indonesia,Central Java,1624494
Tayu,Indonesia,Central Java,1624545
Tasikmalaya,Indonesia,West Java,1624647
Tarub,Indonesia,Central Java,1624668
Tarakan,Indonesia,North Kalimantan,1624725
Tanjungpinang,Indonesia,Riau Islands,1624863
Tanjung Pandan,Indonesia,Bangkaâ€“Belitung Islands,1624877
Bandar Lampung,Indonesia,Lampung,1624917
Tanjungagung,Indonesia,South Sumatra,1624987
Tanggulangin,Indonesia,East Java,1625067
Tangerang,Indonesia,Banten,1625084
Tabanan,Indonesia,Bali,1625708
Surakarta,Indonesia,Central Java,1625812
Surabaya,Indonesia,East Java,1625822
Sungai Raya,Indonesia,West Kalimantan,1625908
Sungai Penuh,Indonesia,Jambi,1625929
Sungailiat,Indonesia,Bangkaâ€“Belitung Islands,1625958
Sumenep,Indonesia,East Java,1626099
Sumedang Utara,Indonesia,N/A,1626100
Sumberpucung,Indonesia,East Java,1626134
Sumber,Indonesia,West Java,1626183
Sumbawa Besar,Indonesia,West Nusa Tenggara,1626185
Sokaraja,Indonesia,Central Java,1626312
Sukabumi,Indonesia,West Java,1626381
Srono,Indonesia,East Java,1626486
Srandakan,Indonesia,Daerah Istimewa Yogyakarta,1626493
Sragen,Indonesia,Central Java,1626498
Sorong,Indonesia,West Papua,1626542
Soreang,Indonesia,West Java,1626560
Solok,Indonesia,West Sumatra,1626649
Soko,Indonesia,East Java,1626673
Sofifi,Indonesia,Maluku Utara,1626698
Soe,Indonesia,East Nusa Tenggara,1626703
Sleman,Indonesia,Daerah Istimewa Yogyakarta,1626754
Slawi,Indonesia,Central Java,1626758
Situbondo,Indonesia,East Java,1626801
Sinjai,Indonesia,South Sulawesi,1626895
Singosari,Indonesia,East Java,1626899
Singojuruh,Indonesia,East Java,1626903
Singkawang,Indonesia,West Kalimantan,1626916
Sengkang,Indonesia,South Sulawesi,1626921
Singaraja,Indonesia,Bali,1626932
Singaparna,Indonesia,West Java,1626936
Simpang,Indonesia,Jambi,1627035
Sijunjung,Indonesia,West Sumatra,1627185
Sidoarjo,Indonesia,East Java,1627253
Sidareja,Indonesia,Central Java,1627267
Sewon,Indonesia,Daerah Istimewa Yogyakarta,1627357
Serpong,Indonesia,West Java,1627459
Serang,Indonesia,Banten,1627549
Sepatan,Indonesia,West Java,1627610
Semarang,Indonesia,Central Java,1627896
Selogiri,Indonesia,Central Java,1627969
Sawangan,Indonesia,West Java,1628453
Sampit,Indonesia,Central Kalimantan,1628884
Sampang,Indonesia,East Java,1628899
Samarinda,Indonesia,East Kalimantan,1629001
Salatiga,Indonesia,Central Java,1629131
Ruteng,Indonesia,East Nusa Tenggara,1629380
Rengasdengklok,Indonesia,West Java,1629710
Rembangan,Indonesia,Central Java,1629749
Rantepao,Indonesia,South Sulawesi,1629974
Rangkasbitung,Indonesia,Banten,1630058
Randudongkal,Indonesia,Central Java,1630088
Rajapolah,Indonesia,West Java,1630200
Purwokerto,Indonesia,Central Java,1630328
Purwodadi,Indonesia,Central Java,1630333
Purwakarta,Indonesia,West Java,1630341
Purbalingga,Indonesia,Central Java,1630366
Pundong,Indonesia,Daerah Istimewa Yogyakarta,1630416
Probolinggo,Indonesia,East Java,1630634
Prigen,Indonesia,East Java,1630649
Praya,Indonesia,West Nusa Tenggara,1630662
Candi Prambanan,Indonesia,Central Java,1630681
Poso,Indonesia,Central Sulawesi,1630723
Pontianak,Indonesia,West Kalimantan,1630789
Ponorogo,Indonesia,East Java,1630798
Polewali,Indonesia,Sulawesi Barat,1630935
Plumbon,Indonesia,West Java,1630997
Petarukan,Indonesia,Central Java,1631271
Prabumulih,Indonesia,South Sumatra,1631393
Pemangkat,Indonesia,West Kalimantan,1631637
Pemalang,Indonesia,Central Java,1631648
Pelabuhanratu,Indonesia,West Java,1631733
Pekanbaru,Indonesia,Riau,1631761
Pekalongan,Indonesia,Central Java,1631766
Pecangaan,Indonesia,Central Java,1631851
Payakumbuh,Indonesia,West Sumatra,1631905
Pati,Indonesia,Central Java,1631992
Pasuruan,Indonesia,East Java,1632033
Paseh,Indonesia,West Java,1632197
Pasarkemis,Indonesia,West Java,1632228
Parung,Indonesia,West Java,1632276
Pariaman,Indonesia,West Sumatra,1632334
Parepare,Indonesia,South Sulawesi,1632353
Pare,Indonesia,East Java,1632358
Panji,Indonesia,East Java,1632566
Pangkalpinang,Indonesia,Bangkaâ€“Belitung Islands,1632654
Pangkalanbuun,Indonesia,Central Kalimantan,1632694
Pandeglang,Indonesia,Banten,1632823
Pandaan,Indonesia,East Java,1632859
Pandak,Indonesia,Daerah Istimewa Yogyakarta,1632861
Panarukan,Indonesia,East Java,1632903
Pamulang,Indonesia,West Java,1632937
Pameungpeuk,Indonesia,West Java,1632974
Pamekasan,Indonesia,East Java,1632978
Pamanukan,Indonesia,West Java,1632998
Palu,Indonesia,Central Sulawesi,1633034
Palopo,Indonesia,South Sulawesi,1633037
Palimanan,Indonesia,West Java,1633056
Palembang,Indonesia,South Sumatra,1633070
Palangkaraya,Indonesia,Central Kalimantan,1633118
Pakisaji,Indonesia,East Java,1633182
Pageralam,Indonesia,South Sumatra,1633308
Padang,Indonesia,West Sumatra,1633419
Paciran,Indonesia,East Java,1633442
Ngunut,Indonesia,East Java,1633986
Ngoro,Indonesia,East Java,1634010
Ngawi,Indonesia,West Java,1634098
Nganjuk,Indonesia,East Java,1634131
Negara,Indonesia,Bali,1634266
Nabire,Indonesia,Papua,1634614
Muntok,Indonesia,Bangkaâ€“Belitung Islands,1634678
Muntilan,Indonesia,Central Java,1634680
Muncar,Indonesia,East Java,1634718
Mranggen,Indonesia,Central Java,1634954
Mojokerto,Indonesia,East Java,1635111
Mojoagung,Indonesia,East Java,1635116
Mlonggo,Indonesia,Central Java,1635164
Metro,Indonesia,Lampung,1635283
Mertoyudan,Indonesia,Central Java,1635342
Melati,Indonesia,Daerah Istimewa Yogyakarta,1635660
Maumere,Indonesia,East Nusa Tenggara,1635815
Mataram,Indonesia,West Nusa Tenggara,1635882
Martapura,Indonesia,South Kalimantan,1636022
Margasari,Indonesia,Central Java,1636121
Margahayukencana,Indonesia,West Java,1636125
Manokwari,Indonesia,West Papua,1636308
Manismata,Indonesia,West Kalimantan,1636322
Manggar,Indonesia,Bangkaâ€“Belitung Islands,1636426
Mendaha,Indonesia,Jambi,1636507
Manado,Indonesia,North Sulawesi,1636544
Malang,Indonesia,East Java,1636722
Majene,Indonesia,Sulawesi Barat,1636806
Majenang,Indonesia,Central Java,1636808
Majalengka,Indonesia,West Java,1636816
Magelang,Indonesia,Central Java,1636884
Madiun,Indonesia,East Java,1636930
Luwuk,Indonesia,Central Sulawesi,1637001
Lumajang,Indonesia,East Java,1637090
Lubuklinggau,Indonesia,South Sumatra,1637158
Loa Janan,Indonesia,East Kalimantan,1637510
Lembang,Indonesia,West Java,1638063
Lebaksiu,Indonesia,Central Java,1638217
Lawang,Indonesia,East Java,1638284
Lasem,Indonesia,Central Java,1638352
Lamongan,Indonesia,East Java,1638562
Lahat,Indonesia,South Sumatra,1638775
Labuan Bajo,Indonesia,East Nusa Tenggara,1638868
Labuan,Indonesia,Banten,1638870
Kutoarjo,Indonesia,Central Java,1638981
Kuta,Indonesia,Bali,1639002
Kuningan,Indonesia,West Java,1639094
Kudus,Indonesia,Central Java,1639215
Kuala Tungkal,Indonesia,Jambi,1639286
Kualakapuas,Indonesia,Central Kalimantan,1639304
Kroya,Indonesia,Central Java,1639337
Krian,Indonesia,East Java,1639356
Kresek,Indonesia,West Java,1639362
Kraksaan,Indonesia,East Java,1639431
Kotabumi,Indonesia,Lampung,1639524
Klungkung,Indonesia,Bali,1639850
Klaten,Indonesia,Central Java,1639900
Klangenan,Indonesia,West Java,1639925
Kijang,Indonesia,Riau Islands,1640044
Ketanggungan,Indonesia,Central Java,1640138
Kertosono,Indonesia,East Java,1640185
Kepanjen,Indonesia,East Java,1640296
Kendari,Indonesia,Sulawesi Tenggara,1640344
Kencong,Indonesia,East Java,1640354
Kefamenanu,Indonesia,East Nusa Tenggara,1640576
Kedungwuni,Indonesia,Central Java,1640581
Kedungwaru,Indonesia,East Java,1640585
Kediri,Indonesia,East Java,1640660
Kebonarun,Indonesia,Central Java,1640755
Kebomas,Indonesia,East Java,1640765
Kawalu,Indonesia,West Java,1640902
Katabu,Indonesia,Sulawesi Tenggara,1640972
Karangsembung,Indonesia,West Java,1641184
Karangasem,Indonesia,Bali,1641301
Karanganom,Indonesia,Central Java,1641333
Karangampel,Indonesia,West Java,1641342
Kamal,Indonesia,East Java,1641792
Kalianget,Indonesia,East Java,1641977
Juwana,Indonesia,Central Java,1642317
Jombang,Indonesia,East Java,1642414
Jogonalan,Indonesia,Central Java,1642437
Jember,Indonesia,East Java,1642588
Jekulo,Indonesia,Central Java,1642628
Jatiwangi,Indonesia,West Java,1642684
Jatiroto,Indonesia,Central Java,1642692
Jatibarang,Indonesia,West Java,1642726
Jaten,Indonesia,Central Java,1642754
Jambi City,Indonesia,Jambi,1642858
Jakarta,Indonesia,Jakarta Raya,1642911
Indramayu,Indonesia,West Java,1643078
Grogol,Indonesia,Central Java,1643761
Gresik,Indonesia,East Java,1643776
Gorontalo,Indonesia,Gorontalo,1643837
Gongdanglegi Kulon,Indonesia,East Java,1643898
Gombong,Indonesia,Central Java,1643920
Godean,Indonesia,Daerah Istimewa Yogyakarta,1643981
Genteng,Indonesia,East Java,1644178
Gedangan,Indonesia,East Java,1644349
Gebog,Indonesia,Central Java,1644360
Gampengrejo,Indonesia,East Java,1644522
Gambiran Satu,Indonesia,East Java,1644557
Galesong,Indonesia,South Sulawesi,1644605
Ende,Indonesia,East Nusa Tenggara,1644932
Dumai,Indonesia,Riau,1645133
Dukuhturi,Indonesia,Central Java,1645154
Driyorejo,Indonesia,East Java,1645220
Dompu,Indonesia,West Nusa Tenggara,1645343
Diwek,Indonesia,East Java,1645428
Depok,Indonesia,Daerah Istimewa Yogyakarta,1645518
Depok,Indonesia,West Java,1645524
Denpasar,Indonesia,Bali,1645528
Demak,Indonesia,Central Java,1645559
Delanggu,Indonesia,Central Java,1645565
Dampit,Indonesia,East Java,1645749
Curup,Indonesia,Bengkulu,1645875
Curug,Indonesia,Banten,1645895
Comal,Indonesia,Central Java,1645976
Colomadu,Indonesia,Central Java,1645978
Citeureup,Indonesia,West Java,1646034
Cirebon,Indonesia,West Java,1646170
Ciputat,Indonesia,West Java,1646194
Cimahi,Indonesia,West Java,1646448
Cileunyi,Indonesia,West Java,1646492
Cileungsir,Indonesia,West Java,1646494
Cikarang,Indonesia,West Java,1646678
Cikampek,Indonesia,West Java,1646698
Cicurug,Indonesia,West Java,1646893
Cibinong,Indonesia,West Java,1647003
Ciamis,Indonesia,West Java,1647149
Cepu,Indonesia,Central Java,1647179
Ceper,Indonesia,Central Java,1647187
Caringin,Indonesia,West Java,1647298
Ciampea,Indonesia,West Java,1647383
Bulakamba,Indonesia,Central Java,1647834
Bukittinggi,Indonesia,West Sumatra,1647866
Buduran,Indonesia,East Java,1647936
Buaran,Indonesia,Central Java,1647991
Boyolangu,Indonesia,East Java,1648082
Boyolali,Indonesia,Central Java,1648084
Bontang,Indonesia,East Kalimantan,1648186
Bondowoso,Indonesia,East Java,1648266
Bojonegoro,Indonesia,East Java,1648451
Bogor,Indonesia,West Java,1648473
Blora,Indonesia,Central Java,1648568
Blitar,Indonesia,East Java,1648580
Bitung,Indonesia,North Sulawesi,1648636
Bima,Indonesia,West Nusa Tenggara,1648759
Besuki,Indonesia,East Java,1648918
Bengkulu,Indonesia,Bengkulu,1649150
Bekasi,Indonesia,West Java,1649378
Baturaja,Indonesia,South Sumatra,1649593
Baturaden,Indonesia,Central Java,1649595
Batu,Indonesia,East Java,1649824
Batang,Indonesia,Central Java,1649881
Barabai,Indonesia,South Kalimantan,1650064
Banyuwangi,Indonesia,East Java,1650077
Banyumas,Indonesia,Central Java,1650095
Bantul,Indonesia,Daerah Istimewa Yogyakarta,1650119
Banjarmasin,Indonesia,South Kalimantan,1650213
Banjaran,Indonesia,West Java,1650227
Banjar,Indonesia,Bali,1650232
Banjar,Indonesia,West Java,1650234
Bangkalan,Indonesia,East Java,1650298
Bangil,Indonesia,East Java,1650319
Bandung,Indonesia,West Java,1650357
Bambanglipuro,Indonesia,Daerah Istimewa Yogyakarta,1650434
Balung,Indonesia,East Java,1650460
Balikpapan,Indonesia,East Kalimantan,1650527
Balapulang,Indonesia,Central Java,1650572
Balaipungut,Indonesia,Riau,1650600
Baki,Indonesia,Central Java,1650670
Baekrajan,Indonesia,Central Java,1650815
Babat,Indonesia,East Java,1650888
Atambua,Indonesia,East Nusa Tenggara,1651103
Astanajapura,Indonesia,West Java,1651112
Arjawinangun,Indonesia,West Java,1651226
Amuntai,Indonesia,South Kalimantan,1651461
Ambon,Indonesia,Maluku,1651531
Ambarawa,Indonesia,Central Java,1651555
Amahai,Indonesia,Maluku,1651591
Adiwerna,Indonesia,Central Java,1651887
Padalarang,Indonesia,West Java,1963770
Ciranjang-hilir,Indonesia,West Java,1964032
Cikupa,Indonesia,West Java,1985663
Teluknaga,Indonesia,West Java,1990589
Wonosari,Indonesia,Daerah Istimewa Yogyakarta,2002872
Gamping Lor,Indonesia,Daerah Istimewa Yogyakarta,2005057
Kasihan,Indonesia,Daerah Istimewa Yogyakarta,2005237
Ngemplak,Indonesia,Central Java,2010971
Kartasura,Indonesia,Central Java,2010985
Gatak,Indonesia,Central Java,2011457
Kupang,Indonesia,East Nusa Tenggara,2057087
Jayapura,Indonesia,Papua,2082600
Abepura,Indonesia,Papua,2082727
Seririt,Indonesia,Bali,7084521
City of Balikpapan,Indonesia,East Kalimantan,8224624
Pekan Bahapal,Indonesia,North Sumatra,8449493
South Tangerang,Indonesia,Banten,8581443
Loch Garman,Ireland,Leinster,2960964
Waterford,Ireland,Munster,2960992
Tralee,Ireland,Munster,2961123
Tallaght,Ireland,Leinster,2961284
Swords,Ireland,Leinster,2961297
Sligo,Ireland,Connaught,2961423
Droichead Nua,Ireland,Leinster,2962290
Navan,Ireland,Leinster,2962308
Naas,Ireland,Leinster,2962334
An Muileann gCearr,Ireland,Leinster,2962361
Malahide,Ireland,Leinster,2962725
Lucan,Ireland,Leinster,2962785
Luimneach,Ireland,Munster,2962943
Letterkenny,Ireland,Ulster,2962961
Leixlip,Ireland,Leinster,2962974
Kilkenny,Ireland,Leinster,2963398
Gaillimh,Ireland,Connaught,2964180
Finglas,Ireland,Leinster,2964303
Ennis,Ireland,Munster,2964405
DÃºn Laoghaire,Ireland,Leinster,2964506
Dundalk,Ireland,Leinster,2964540
Dublin,Ireland,Leinster,2964574
Drogheda,Ireland,Leinster,2964661
Cork,Ireland,Munster,2965140
Cluain Meala,Ireland,Munster,2965353
Celbridge,Ireland,Leinster,2965529
Carlow,Ireland,Leinster,2965768
Blanchardstown,Ireland,Leinster,2966110
Balbriggan,Ireland,Leinster,2966794
Athlone,Ireland,Leinster,2966839
Sandyford,Ireland,Leinster,3315278
Donaghmede,Ireland,Leinster,6691033
Jerusalem,Israel,Jerusalem,281184
Safed,Israel,Northern District,293100
Yehud,Israel,Central District,293207
YavnÃ©,Israel,Central District,293222
Yafo,Israel,Tel Aviv,293253
Umm el Faá¸¥m,Israel,Haifa,293286
Tirat Karmel,Israel,Haifa,293308
Tiberias,Israel,Northern District,293322
Tel Aviv,Israel,Tel Aviv,293397
maalot TarshÄ«hÄ,Israel,Northern District,293420
Tamra,Israel,Northern District,293426
Sederot,Israel,Southern District,293619
SakhnÄ«n,Israel,Northern District,293655
Rosh Haâ€˜Ayin,Israel,Central District,293690
Rishon Leáº”iyyon,Israel,Central District,293703
Ramla,Israel,Central District,293768
Ramat HaSharon,Israel,Tel Aviv,293783
Ramat Gan,Israel,Tel Aviv,293788
Ra'anana,Israel,Central District,293807
Qiryat Yam,Israel,Haifa,293822
Qiryat Shemona,Israel,Northern District,293825
Qiryat Moáº•qin,Israel,Haifa,293831
Qiryat Gat,Israel,Southern District,293842
Qiryat Bialik,Israel,Haifa,293844
Qiryat Ata,Israel,Haifa,293845
Qalansuwa,Israel,Central District,293896
Petaáº– Tiqwa,Israel,Central District,293918
Or Yehuda,Israel,Tel Aviv,293962
Ofaqim,Israel,Southern District,293992
Netivot,Israel,Southern District,294068
Netanya,Israel,Central District,294071
Ness Ziona,Israel,Central District,294074
Nesher,Israel,Haifa,294078
Nazareth,Israel,Northern District,294098
Nahariya,Israel,Northern District,294117
Migdal Haâ€˜Emeq,Israel,Northern District,294210
Mevo Betar,Israel,Jerusalem,294244
MaghÄr,Israel,Northern District,294387
Lod,Israel,Central District,294421
Kfar Saba,Israel,Central District,294514
Karmiâ€™el,Israel,Northern District,294577
Kafr QÄsim,Israel,Central District,294604
Kafr MandÄ,Israel,Northern District,294608
Kafr KannÄ,Israel,Northern District,294610
Judeida Makr,Israel,Northern District,294622
HÌ±olon,Israel,Tel Aviv,294751
Hod HaSharon,Israel,Central District,294760
Herzliyya,Israel,Tel Aviv,294778
Haifa,Israel,Haifa,294801
HÌ±adera,Israel,Haifa,294946
Givâ€˜at Shemuâ€™Ã©l,Israel,Tel Aviv,294981
Givâ€˜atayim,Israel,Tel Aviv,294999
Tirah,Israel,Central District,295127
Eá¹­ á¹¬aiyiba,Israel,Central District,295130
Er Reina,Israel,Northern District,295174
Eilat,Israel,Southern District,295277
Dimona,Israel,Southern District,295328
DÄliyat el Karmil,Israel,Haifa,295365
Bet Shemesh,Israel,Jerusalem,295432
Bet Sheâ€™an,Israel,Northern District,295435
BenÃ© Beraq,Israel,Tel Aviv,295514
Beersheba,Israel,Southern District,295530
Bat Yam,Israel,Tel Aviv,295548
Ashqelon,Israel,Southern District,295620
Ashdod,Israel,Southern District,295629
â€˜Arad,Israel,Southern District,295657
â€˜Akko,Israel,Northern District,295721
â€˜Afula â€˜Illit,Israel,Northern District,295739
Modiin,Israel,Central District,6693679
West Jerusalem,Israel,Jerusalem,7498240
Modiin Ilit,Israel,Jerusalem,8199378
Ariel,Israel,Jerusalem,8199394
Douglas,Isle of Man,Douglas,3042237
PÅ«nch,India,Kashmir,1167718
Keelakarai,India,Tamil Nadu,1252646
Zunheboto,India,Nagaland,1252653
ZamÄnia,India,Uttar Pradesh,1252692
Zaidpur,India,Uttar Pradesh,1252698
ZahirÄbÄd,India,Telangana,1252699
Yeola,India,Maharashtra,1252738
YellÄpur,India,Karnataka,1252744
Yellandu,India,Telangana,1252745
Yelahanka,India,Karnataka,1252758
YavatmÄl,India,Maharashtra,1252770
YÄval,India,Maharashtra,1252773
Yanam,India,Andhra Pradesh,1252795
YamunÄnagar,India,Haryana,1252797
YÄdgÄ«r,India,Karnataka,1252822
Wokha,India,Nagaland,1252840
Wer,India,Rajasthan,1252885
Wellington,India,Tamil Nadu,1252887
WazÄ«rganj,India,Uttar Pradesh,1252892
WÄshÄ«m,India,Maharashtra,1252908
Warud,India,Maharashtra,1252919
Warora,India,Maharashtra,1252925
WÄris AlÄ«ganj,India,Bihar,1252930
Wardha,India,Maharashtra,1252942
WÄrÄseonÄ«,India,Madhya Pradesh,1252946
Warangal,India,Telangana,1252948
Wanparti,India,Telangana,1252956
WÄnkÄner,India,Gujarat,1252958
Wani,India,Maharashtra,1252960
Walajapet,India,Tamil Nadu,1252997
Wai,India,Maharashtra,1253013
WÄdi,India,Karnataka,1253041
VyÄra,India,Gujarat,1253074
VuyyÅ«ru,India,Andhra Pradesh,1253077
VrindÄvan,India,Uttar Pradesh,1253079
VriddhÄchalam,India,Tamil Nadu,1253080
Vizianagaram,India,Andhra Pradesh,1253084
Vite,India,Maharashtra,1253091
Visnagar,India,Gujarat,1253095
Visakhapatnam,India,Andhra Pradesh,1253102
VÄ«sÄvadar,India,Gujarat,1253105
Virudunagar,India,Tamil Nadu,1253113
ViravanallÅ«r,India,Tamil Nadu,1253127
VÄ«rarÄjendrapet,India,Karnataka,1253132
VirÄr,India,Maharashtra,1253133
Vinukonda,India,Andhra Pradesh,1253150
Villupuram,India,Tamil Nadu,1253166
VikÄrÄbÄd,India,Telangana,1253182
Vijayawada,India,Andhra Pradesh,1253184
VijÄpur,India,Gujarat,1253193
Vidisha,India,Madhya Pradesh,1253200
VettÅ«r,India,Kerala,1253216
Vettaikkaranpudur,India,Tamil Nadu,1253219
VetapÄlem,India,Andhra Pradesh,1253220
VerÄval,India,Gujarat,1253237
Vepagunta,India,Andhra Pradesh,1253242
Venkatagiri,India,Andhra Pradesh,1253251
VemalwÄda,India,Telangana,1253275
Velur,India,Tamil Nadu,1253278
Vellore,India,Tamil Nadu,1253286
Vejalpur,India,Gujarat,1253315
Vedaraniyam,India,Tamil Nadu,1253330
VayalÄr,India,Kerala,1253340
Vattalkundu,India,Tamil Nadu,1253352
VÄsudevanallÅ«r,India,Tamil Nadu,1253357
Vasind,India,Maharashtra,1253363
VÄsco Da GÄma,India,Goa,1253367
Vasa,India,Gujarat,1253374
Varkala,India,Kerala,1253392
Varangaon,India,Maharashtra,1253403
Varanasi,India,Uttar Pradesh,1253405
Vaniyambadi,India,Tamil Nadu,1253437
VandavÄsi,India,Tamil Nadu,1253452
ValsÄd,India,Gujarat,1253468
Valparai,India,Tamil Nadu,1253472
Vallabh Vidyanagar,India,Gujarat,1253482
ValabhÄ«pur,India,Gujarat,1253512
Vaikam,India,Kerala,1253544
VaijÄpur,India,Maharashtra,1253545
Vadodara,India,Gujarat,1253573
Vadnagar,India,Gujarat,1253577
VadlapÅ«di,India,Andhra Pradesh,1253578
VÄdippatti,India,Tamil Nadu,1253579
Vadamadurai,India,Tamil Nadu,1253595
Vadakku ValliyÅ«r,India,Tamil Nadu,1253605
VÄda,India,Maharashtra,1253610
UttiramerÅ«r,India,Tamil Nadu,1253623
UttarkÄshi,India,Uttarakhand,1253628
UttamapÄlaiyam,India,Tamil Nadu,1253635
Utraula,India,Uttar Pradesh,1253638
Usilampatti,India,Tamil Nadu,1253671
Usehat,India,Uttar Pradesh,1253673
Uravakonda,India,Andhra Pradesh,1253698
Uran,India,Maharashtra,1253702
Upleta,India,Gujarat,1253736
Uppal Kalan,India,Telangana,1253744
UnnÄo,India,Uttar Pradesh,1253747
Unjha,India,Gujarat,1253750
Unhel,India,Madhya Pradesh,1253754
Una,India,Himachal Pradesh,1253782
Una,India,Gujarat,1253783
Åªn,India,Uttar Pradesh,1253785
Un,India,Gujarat,1253786
Umreth,India,Gujarat,1253805
Umred,India,Maharashtra,1253807
Umarkot,India,Chhattisgarh,1253860
Umarkhed,India,Maharashtra,1253861
Umaria,India,Madhya Pradesh,1253863
Umarga,India,Maharashtra,1253870
Ullal,India,Karnataka,1253888
Ulhasnagar,India,Maharashtra,1253894
Ujjain,India,Madhya Pradesh,1253914
UjhÄni,India,Uttar Pradesh,1253918
Udumalaippettai,India,Tamil Nadu,1253944
Udipi,India,Karnataka,1253952
Udhampur,India,Kashmir,1253956
UdgÄ«r,India,Maharashtra,1253958
Udankudi,India,Tamil Nadu,1253972
Udalguri,India,Assam,1253977
Udaipura,India,Madhya Pradesh,1253984
Udaipur,India,Rajasthan,1253985
Udaipur,India,Rajasthan,1253986
Udaipur,India,Tripura,1253987
Ooty,India,Tamil Nadu,1253993
Bara UchÄna,India,Haryana,1254000
TuraiyÅ«r,India,Tamil Nadu,1254043
Tura,India,Meghalaya,1254046
Tuni,India,Andhra Pradesh,1254054
TÅ«ndla,India,Uttar Pradesh,1254069
Tumsar,India,Maharashtra,1254080
TumkÅ«r,India,Karnataka,1254089
TulsÄ«pur,India,Uttar Pradesh,1254102
TuljÄpur,India,Maharashtra,1254111
TufÄnganj,India,West Bengal,1254131
Tuensang,India,Nagaland,1254133
Thiruvananthapuram,India,Kerala,1254163
TrichÅ«r,India,Kerala,1254187
Tonk,India,Rajasthan,1254241
Tondi,India,Tamil Nadu,1254249
TohÄna,India,Haryana,1254274
Todaraisingh,India,Rajasthan,1254282
Todabhim,India,Rajasthan,1254283
TitlÄgarh,India,Odisha,1254304
TitÄgarh,India,West Bengal,1254309
Tisaiyanvilai,India,Tamil Nadu,1254317
TiruvottiyÅ«r,India,Tamil Nadu,1254320
Cheyyar,India,Tamil Nadu,1254322
TiruvannÄmalai,India,Tamil Nadu,1254327
Tiruvallur,India,Tamil Nadu,1254331
Tiruvalla,India,Kerala,1254335
Thiruthani,India,Tamil Nadu,1254342
Tiruttangal,India,Tamil Nadu,1254343
Tirur,India,Kerala,1254346
Tiruppuvanam,India,Tamil Nadu,1254347
Tiruppur,India,Tamil Nadu,1254348
Tirupparangunram,India,Tamil Nadu,1254356
Tirupati,India,Andhra Pradesh,1254360
Tirunelveli,India,Tamil Nadu,1254361
Tirumala,India,Andhra Pradesh,1254373
Tirukkoyilur,India,Tamil Nadu,1254377
Tiruchengode,India,Tamil Nadu,1254385
Tiruchirappalli,India,Tamil Nadu,1254388
Tiruchchendur,India,Tamil Nadu,1254390
TÄ«rthahalli,India,Karnataka,1254396
TiptÅ«r,India,Karnataka,1254420
Tinsukia,India,Assam,1254432
TinnanÅ«r,India,Tamil Nadu,1254436
Tindivanam,India,Tamil Nadu,1254444
Tilhar,India,Uttar Pradesh,1254481
TÄ«kamgarh,India,Madhya Pradesh,1254534
TijÄra,India,Rajasthan,1254538
ThoubÄl,India,Manipur,1254570
Thiruvarur,India,Tamil Nadu,1254589
ThÄsra,India,Gujarat,1254624
TharÄd,India,Gujarat,1254638
ThanjÄvÅ«r,India,Tamil Nadu,1254649
ThÄnesar,India,Haryana,1254657
ThÄne,India,Maharashtra,1254661
ThÄna Bhawan,India,Uttar Pradesh,1254673
ThÄn,India,Gujarat,1254675
ThÄkurganj,India,Bihar,1254694
Thakurdwara,India,Uttar Pradesh,1254695
Tezpur,India,Assam,1254710
TerdÄl,India,Karnataka,1254727
Teonthar,India,Madhya Pradesh,1254732
Thenkasi,India,Tamil Nadu,1254744
Teni,India,Tamil Nadu,1254745
Tellicherry,India,Kerala,1254780
TelhÄra,India,Maharashtra,1254787
Tekkali,India,Andhra Pradesh,1254794
Tekkalakote,India,Karnataka,1254795
TekÄri,India,Bihar,1254797
Tehri,India,Uttarakhand,1254808
Teghra,India,Bihar,1254813
TÄsgaon,India,Maharashtra,1254858
Tarn TÄran,India,Punjab,1254868
Tarikere,India,Karnataka,1254880
Tharangambadi,India,Tamil Nadu,1254904
TÄrÄnagar,India,Rajasthan,1254908
TarÄna,India,Madhya Pradesh,1254909
TÄramangalam,India,Tamil Nadu,1254910
Tarakeswar,India,West Bengal,1254912
TÄoru,India,Haryana,1254948
Tanuku,India,Andhra Pradesh,1254953
TÄndÅ«r,India,Telangana,1255004
TÄnda,India,Uttar Pradesh,1255023
TÄndÄ,India,Uttar Pradesh,1255024
Tanakpur,India,Uttarakhand,1255027
TamlÅ«k,India,West Bengal,1255046
TalwÄra,India,Punjab,1255076
Talwandi Bhai,India,Punjab,1255082
Taloda,India,Maharashtra,1255104
Talipparamba,India,Kerala,1255121
TÄlÄ«kota,India,Karnataka,1255122
Taleigao,India,Goa,1255131
Talegaon DÄbhÄde,India,Maharashtra,1255134
TÄlcher,India,Odisha,1255143
TalÄja,India,Gujarat,1255175
TÄki,India,West Bengal,1255211
Takhatpur,India,Chhattisgarh,1255212
Takhatgarh,India,Rajasthan,1255213
TÄjpur,India,Uttar Pradesh,1255224
TÄdpatri,India,Andhra Pradesh,1255254
TÄdepallegÅ«dem,India,Andhra Pradesh,1255264
TÄdepalle,India,Andhra Pradesh,1255265
SuriÄpet,India,Telangana,1255344
SuriÄnwÄn,India,Uttar Pradesh,1255346
Surendranagar,India,Gujarat,1255349
SÅ«ratgarh,India,Rajasthan,1255361
SÅ«rat,India,Gujarat,1255364
SÅ«randai,India,Tamil Nadu,1255372
SÅ«rajgarh,India,Rajasthan,1255383
Supaul,India,Bihar,1255396
Sunel,India,Rajasthan,1255425
Sundarnagar,India,Himachal Pradesh,1255434
Sundargarh,India,Odisha,1255437
SunÄm,India,Punjab,1255449
Sulya,India,Karnataka,1255482
SÅ«lÅ«ru,India,Andhra Pradesh,1255483
Sulur,India,Tamil Nadu,1255484
Sultanpur,India,Punjab,1255488
SultÄnpur,India,Uttar Pradesh,1255491
Suket,India,Rajasthan,1255551
SÅ«jÄngarh,India,Rajasthan,1255560
SuÄr,India,Uttar Pradesh,1255597
Srivilliputhur,India,Tamil Nadu,1255616
SrÄ«vardhan,India,Maharashtra,1255619
Srivaikuntam,India,Tamil Nadu,1255620
SrÄ«sailain,India,Andhra Pradesh,1255621
SrÄ«rÄmnagar,India,Telangana,1255625
SrÄ«perumbÅ«dÅ«r,India,Tamil Nadu,1255630
SrÄ«nivÄspur,India,Karnataka,1255631
Srinagar,India,Kashmir,1255634
SrÄ«nagar,India,Uttarakhand,1255635
Sri MÄdhopur,India,Rajasthan,1255643
Karanpur,India,Rajasthan,1255646
Chicacole,India,Andhra Pradesh,1255647
Sri DÅ«ngargarh,India,Rajasthan,1255654
Soygaon,India,Maharashtra,1255667
Soron,India,Uttar Pradesh,1255704
Soro,India,Odisha,1255705
Sorada,India,Odisha,1255712
Sopur,India,Kashmir,1255714
SonÄ«pat,India,Haryana,1255744
Songadh,India,Gujarat,1255762
Sonepur,India,Odisha,1255763
SonÄri,India,Assam,1255788
SonÄmukhi,India,West Bengal,1255792
Sompeta,India,Andhra Pradesh,1255816
Someshwar,India,Karnataka,1255823
Solan,India,Himachal Pradesh,1255850
SojÄ«tra,India,Gujarat,1255858
Sojat,India,Rajasthan,1255860
Sohna,India,Haryana,1255870
SohÄgpur,India,Madhya Pradesh,1255884
SiwÄna,India,Rajasthan,1255925
SiwÄn,India,Bihar,1255927
Sivakasi,India,Tamil Nadu,1255947
Sivagiri,India,Tamil Nadu,1255950
Sivagiri,India,Tamil Nadu,1255951
Sivaganga,India,Tamil Nadu,1255953
Siuri,India,West Bengal,1255955
SitÄrganj,India,Uttarakhand,1255963
SÄ«tÄpur,India,Uttar Pradesh,1255969
SÄ«tÄmarhi,India,Bihar,1255983
SiswÄ BÄzÄr,India,Uttar Pradesh,1255995
Sisauli,India,Uttar Pradesh,1256003
SirÅ«r,India,Maharashtra,1256025
Sirumugai,India,Tamil Nadu,1256027
Siruguppa,India,Karnataka,1256029
Sirsilla,India,Telangana,1256039
Sirsi,India,Uttar Pradesh,1256040
Sirsi,India,Karnataka,1256047
SirsÄganj,India,Uttar Pradesh,1256050
Sirsa,India,Haryana,1256052
Sironj,India,Madhya Pradesh,1256064
Sirohi,India,Rajasthan,1256067
SÄ«rkÄzhi,India,Tamil Nadu,1256075
Sirhind,India,Punjab,1256087
SÄ«ra,India,Karnataka,1256104
Sinnar,India,Maharashtra,1256119
Singur,India,West Bengal,1256124
SingarÄyakonda,India,Andhra Pradesh,1256176
SingÄnallÅ«r,India,Tamil Nadu,1256184
SindhnÅ«r,India,Karnataka,1256207
Sindgi,India,Karnataka,1256214
Shimla,India,Himachal Pradesh,1256237
Simdega,India,Jharkhand,1256246
Silvassa,India,Dadra and Nagar Haveli,1256259
Sillod,India,Maharashtra,1256269
Silchar,India,Assam,1256287
Silao,India,Bihar,1256295
SÄ«kar,India,Rajasthan,1256320
Sikandra Rao,India,Uttar Pradesh,1256322
Sikandarpur,India,Uttar Pradesh,1256328
SikandarÄbÄd,India,Uttar Pradesh,1256329
Sikka,India,Gujarat,1256333
Sijua,India,Jharkhand,1256335
SihorÄ,India,Madhya Pradesh,1256340
Sihor,India,Gujarat,1256343
Sidlaghatta,India,Karnataka,1256363
Sidhi,India,Madhya Pradesh,1256369
SidhaulÄ«,India,Uttar Pradesh,1256372
Siddipet,India,Telangana,1256377
Siddhapur,India,Gujarat,1256382
SibsÄgar,India,Assam,1256388
Shyamnagar,India,West Bengal,1256409
ShujÄlpur,India,Madhya Pradesh,1256418
ShrÄ«rangapattana,India,Karnataka,1256421
ShrÄ«rÄmpur,India,West Bengal,1256422
ShrÄ«gonda,India,Maharashtra,1256426
ShorÄpur,India,Karnataka,1256431
ShoranÅ«r,India,Kerala,1256432
Sholinghur,India,Tamil Nadu,1256435
SolÄpur,India,Maharashtra,1256436
Shivpuri,India,Madhya Pradesh,1256451
ShÄ«shgarh,India,Uttar Pradesh,1256468
Shirpur,India,Maharashtra,1256475
Shirhatti,India,Karnataka,1256483
Shirdi,India,Maharashtra,1256489
Shimoga,India,Karnataka,1256515
Shillong,India,Meghalaya,1256523
Shiliguri,India,West Bengal,1256525
ShikohÄbÄd,India,Uttar Pradesh,1256529
ShikÄrpÅ«r,India,Uttar Pradesh,1256532
ShikÄrpur,India,Karnataka,1256537
Shiggaon,India,Karnataka,1256539
Shertallai,India,Kerala,1256558
Sherkot,India,Uttar Pradesh,1256569
SherghÄti,India,Bihar,1256572
Sheopur,India,Madhya Pradesh,1256593
Sheohar,India,Bihar,1256597
Sheoganj,India,Rajasthan,1256598
Shegaon,India,Maharashtra,1256620
ShÄntipur,India,West Bengal,1256639
ShamsÄbÄd,India,Uttar Pradesh,1256659
ShamsÄbÄd,India,Uttar Pradesh,1256660
ShÄmli,India,Uttar Pradesh,1256671
ShÄmgarh,India,Madhya Pradesh,1256673
ShÄjÄpur,India,Madhya Pradesh,1256693
Sheikhpura,India,Bihar,1256698
ShÄhpura,India,Rajasthan,1256705
ShÄhpura,India,Rajasthan,1256706
ShÄhpur,India,Uttar Pradesh,1256713
ShÄhpur,India,Bihar,1256715
ShÄhpur,India,Madhya Pradesh,1256720
ShÄhpur,India,Karnataka,1256722
ShÄhjÄnpur,India,Uttar Pradesh,1256728
ShÄhi,India,Uttar Pradesh,1256731
ShÄhganj,India,Uttar Pradesh,1256735
Shahdol,India,Madhya Pradesh,1256739
ShÄhÄda,India,Maharashtra,1256750
ShÄhÄbÄd,India,Haryana,1256752
ShÄhÄbÄd,India,Uttar Pradesh,1256753
ShÄhÄbÄd,India,Uttar Pradesh,1256755
ShÄhÄbÄd,India,Karnataka,1256759
SerchhÄ«p,India,Mizoram,1256812
Seram,India,Karnataka,1256814
Seoni MÄlwa,India,Madhya Pradesh,1256823
Seoni,India,Madhya Pradesh,1256826
Seondha,India,Madhya Pradesh,1256828
SeohÄra,India,Uttar Pradesh,1256832
Sendhwa,India,Madhya Pradesh,1256854
Sehore,India,Madhya Pradesh,1256913
Secunderabad,India,Telangana,1256922
SÄyla,India,Gujarat,1256929
SawÄi MÄdhopur,India,Rajasthan,1256949
SÄvda,India,Maharashtra,1256959
SavanÅ«r,India,Karnataka,1256967
SÄvantvÄdi,India,Maharashtra,1256968
Sausar,India,Madhya Pradesh,1256974
Saundatti,India,Karnataka,1256983
Sathyamangalam,India,Tamil Nadu,1256989
Sattur,India,Tamil Nadu,1256995
Sattenapalle,India,Andhra Pradesh,1257001
Satna,India,Madhya Pradesh,1257022
SÄtÄra,India,Maharashtra,1257055
SatÄnÄ,India,Maharashtra,1257060
SÄsvad,India,Maharashtra,1257066
SarwÄr,India,Rajasthan,1257093
Sarkhej,India,Gujarat,1257149
Sardulgarh,India,Punjab,1257191
Sardhana,India,Uttar Pradesh,1257196
SardÄrshahr,India,Rajasthan,1257198
Sarauli,India,Uttar Pradesh,1257219
SÄrangpur,India,Madhya Pradesh,1257237
Saraipali,India,Chhattisgarh,1257259
SarÄi MÄ«r,India,Uttar Pradesh,1257260
SarÄi Ä€kil,India,Uttar Pradesh,1257268
Saoner,India,Maharashtra,1257307
SÄnkrÄil,India,West Bengal,1257354
Sankeshwar,India,Karnataka,1257369
SangrÅ«r,India,Punjab,1257402
SÄngola,India,Maharashtra,1257409
Sangod,India,Rajasthan,1257410
SÄngli,India,Maharashtra,1257416
SangariÄ,India,Rajasthan,1257429
SangÄreddi,India,Telangana,1257431
Sangamner,India,Maharashtra,1257436
SandÅ«r,India,Karnataka,1257456
SandÄ«la,India,Uttar Pradesh,1257459
SÄndi,India,Uttar Pradesh,1257461
Sancoale,India,Goa,1257476
SÄnchor,India,Rajasthan,1257477
SanÄwad,India,Madhya Pradesh,1257481
Sanaur,India,Punjab,1257482
SÄnand,India,Gujarat,1257486
Samthar,India,Uttar Pradesh,1257498
SamrÄla,India,Punjab,1257503
Samdari,India,Rajasthan,1257528
SÄmbhar,India,Rajasthan,1257539
Sambhal,India,Uttar Pradesh,1257540
Sambalpur,India,Odisha,1257542
SÄmba,India,Kashmir,1257545
SamÄstipur,India,Bihar,1257551
SÄmalkot,India,Andhra Pradesh,1257565
SamÄlkha,India,Haryana,1257566
SÄlÅ«r,India,Andhra Pradesh,1257587
SÄlÅ«mbar,India,Rajasthan,1257588
Salem,India,Tamil Nadu,1257629
SalÄya,India,Gujarat,1257638
SaktÄ«,India,Chhattisgarh,1257673
Sakleshpur,India,Karnataka,1257698
Saint Thomas Mount,India,Tamil Nadu,1257749
Sainthia,India,West Bengal,1257751
Selu,India,Maharashtra,1257762
Saiha,India,Mizoram,1257771
Saidpur,India,Uttar Pradesh,1257776
SÄhibganj,India,Jharkhand,1257794
SahÄwar,India,Uttar Pradesh,1257799
SahaswÄn,India,Uttar Pradesh,1257800
Sahaspur,India,Uttar Pradesh,1257802
Saharsa,India,Bihar,1257804
SahÄranpur,India,Uttar Pradesh,1257806
Sagauli,India,Bihar,1257830
Saugor,India,Madhya Pradesh,1257845
SÄgar,India,Karnataka,1257851
SafÄ«pur,India,Uttar Pradesh,1257854
Safidon,India,Haryana,1257855
SÄdri,India,Rajasthan,1257865
SadÄseopet,India,Telangana,1257890
Sadalgi,India,Karnataka,1257895
SadÄbÄd,India,Uttar Pradesh,1257896
Sabalgarh,India,Madhya Pradesh,1257928
Rusera,India,Bihar,1257936
Rura,India,Uttar Pradesh,1257940
Ropar,India,Punjab,1257951
RÅ«darpur,India,Uttar Pradesh,1258012
Roorkee,India,Uttarakhand,1258044
Ron,India,Karnataka,1258061
Rohtak,India,Haryana,1258076
Roha,India,Maharashtra,1258099
Robertsonpet,India,Karnataka,1258109
Robertsganj,India,Uttar Pradesh,1258111
Risod,India,Maharashtra,1258124
Rishra,India,West Bengal,1258126
RishÄ«kesh,India,Uttarakhand,1258128
RÄ«ngas,India,Rajasthan,1258140
Richha,India,Uttar Pradesh,1258164
RewÄri,India,Haryana,1258178
Rewa,India,Madhya Pradesh,1258182
Revelganj,India,Bihar,1258186
Repalle,India,Andhra Pradesh,1258201
Reoti,India,Uttar Pradesh,1258203
RenukÅ«t,India,Uttar Pradesh,1258207
Renigunta,India,Andhra Pradesh,1258213
Remuna,India,Odisha,1258229
Rehli,India,Madhya Pradesh,1258247
RÄzÄm,India,Andhra Pradesh,1258270
RÄybÄg,India,Karnataka,1258278
RÄyadrug,India,Andhra Pradesh,1258290
RÄyachoti,India,Andhra Pradesh,1258291
RÄya,India,Uttar Pradesh,1258292
Raxaul,India,Bihar,1258294
RÄwatsÄr,India,Rajasthan,1258295
RÄwatbhÄta,India,Rajasthan,1258297
RÄver,India,Maharashtra,1258307
Ratnagiri,India,Maharashtra,1258338
RatlÄm,India,Madhya Pradesh,1258342
Ratia,India,Haryana,1258347
RÄth,India,Uttar Pradesh,1258352
Ratanpur,India,Chhattisgarh,1258362
Ratangarh,India,Rajasthan,1258366
RasrÄ,India,Uttar Pradesh,1258380
Rasipuram,India,Tamil Nadu,1258386
RÄpar,India,Gujarat,1258406
RÄnÄ«pur,India,Uttar Pradesh,1258449
RÄnikhet,India,Uttarakhand,1258455
RÄnÄ«ganj,India,West Bengal,1258470
RÄnÄ«bennur,India,Karnataka,1258474
RÄnia,India,Haryana,1258477
Rangia,India,Assam,1258492
RangÄpÄra,India,Assam,1258501
Ranchi,India,Jharkhand,1258526
RÄnÄvÄv,India,Gujarat,1258534
RÄnÄghÄt,India,West Bengal,1258546
RÄmtek,India,Maharashtra,1258553
Rampur Hat,India,West Bengal,1258581
RÄmpura,India,Punjab,1258584
RÄmpura,India,Madhya Pradesh,1258592
RÄmpur,India,Uttar Pradesh,1258598
RÄmpur,India,Uttar Pradesh,1258599
RÄmnagar,India,Uttarakhand,1258637
RÄmnagar,India,Bihar,1258639
RÄmnagar,India,Uttar Pradesh,1258642
RÄmjÄ«banpur,India,West Bengal,1258658
RÄmgundam,India,Telangana,1258662
RÄmgarh,India,Rajasthan,1258677
RÄmgarh,India,Jharkhand,1258686
RÄmganj Mandi,India,Rajasthan,1258692
Rameswaram,India,Tamil Nadu,1258698
RÄmÄpuram,India,Andhra Pradesh,1258726
Ramanathapuram,India,Tamil Nadu,1258740
RÄmanagaram,India,Karnataka,1258744
RÄmachandrapuram,India,Andhra Pradesh,1258756
RÄjÅ«ra,India,Maharashtra,1258786
RÄjula,India,Gujarat,1258795
RÄjsamand,India,Rajasthan,1258797
RÄjpura,India,Punjab,1258803
Rajpur,India,Madhya Pradesh,1258815
Rajpur,India,Madhya Pradesh,1258816
RÄjpÄ«pla,India,Gujarat,1258819
RÄj-NÄndgaon,India,Chhattisgarh,1258831
RÄjmahal,India,West Bengal,1258843
RÄjkot,India,Gujarat,1258847
RÄjgurunagar,India,Maharashtra,1258859
RÄjgÄ«r,India,Bihar,1258864
RÄjgarh,India,Rajasthan,1258868
RÄjgarh,India,Rajasthan,1258869
RÄjgarh,India,Madhya Pradesh,1258875
RÄjgarh,India,Madhya Pradesh,1258876
Rajaori,India,Kashmir,1258891
Rajapalaiyam,India,Tamil Nadu,1258916
RÄjampet,India,Andhra Pradesh,1258922
RÄjaldesar,India,Rajasthan,1258928
RÄjÄkhera,India,Rajasthan,1258930
RÄjahmundry,India,Andhra Pradesh,1258932
RÄisinghnagar,India,Rajasthan,1258950
Raisen,India,Madhya Pradesh,1258952
RÄipur,India,Uttarakhand,1258967
Raipur,India,Rajasthan,1258972
Raipur,India,Chhattisgarh,1258980
RÄikot,India,Punjab,1258993
Raigarh,India,Chhattisgarh,1259005
RÄiganj,India,West Bengal,1259009
RÄichÅ«r,India,Karnataka,1259012
RÄhuri,India,Maharashtra,1259019
Rahimatpur,India,Maharashtra,1259026
RÄhatgarh,India,Madhya Pradesh,1259034
Raghunathpur,India,West Bengal,1259049
RÄghogarh,India,Madhya Pradesh,1259056
Rafiganj,India,Bihar,1259060
Raebareli,India,Uttar Pradesh,1259064
RÄdhanpur,India,Gujarat,1259069
Rabkavi,India,Karnataka,1259083
Kollam,India,Kerala,1259091
Kasba,India,Bihar,1259108
QÄdiÄn,India,Punjab,1259110
PuttÅ«r,India,Andhra Pradesh,1259123
PuttÅ«r,India,Karnataka,1259124
Pushkar,India,Rajasthan,1259148
Pusad,India,Maharashtra,1259154
PurwÄ,India,Uttar Pradesh,1259157
Puruliya,India,West Bengal,1259163
Purnia,India,Bihar,1259166
PÅ«rna,India,Maharashtra,1259177
Puri,India,Odisha,1259184
PÅ«ranpur,India,Uttar Pradesh,1259190
Pupri,India,Bihar,1259210
Punjai Puliyampatti,India,Tamil Nadu,1259222
PunganÅ«ru,India,Andhra Pradesh,1259228
Pune,India,Maharashtra,1259229
PÅ«ndri,India,Haryana,1259231
PunÄsa,India,Madhya Pradesh,1259239
PunalÅ«r,India,Kerala,1259243
PÅ«nÄhÄna,India,Haryana,1259244
Pulwama,India,Kashmir,1259251
Puliyangudi,India,Tamil Nadu,1259263
Pulivendla,India,Andhra Pradesh,1259264
Pulgaon,India,Maharashtra,1259272
PukhrÄyÄn,India,Uttar Pradesh,1259283
Pudukkottai,India,Tamil Nadu,1259297
ProddatÅ«r,India,Andhra Pradesh,1259312
PratÄpgarh,India,Rajasthan,1259338
Port Blair,India,Andaman and Nicobar Islands,1259385
Porsa,India,Madhya Pradesh,1259388
Porbandar,India,Gujarat,1259395
Poonamalle,India,Tamil Nadu,1259400
PonnÅ«ru,India,Andhra Pradesh,1259408
Ponneri,India,Tamil Nadu,1259409
PonnÄni,India,Kerala,1259411
Puducherry,India,Pondicherry,1259425
Ponda,India,Goa,1259429
PolÅ«r,India,Tamil Nadu,1259434
Pollachi,India,Tamil Nadu,1259440
Polavaram,India,Andhra Pradesh,1259444
Polasara,India,Odisha,1259446
Pokaran,India,Rajasthan,1259460
PithorÄgarh,India,Uttarakhand,1259503
PithÄpuram,India,Andhra Pradesh,1259508
Piro,India,Bihar,1259530
PiriyÄpatna,India,Karnataka,1259535
Piravam,India,Kerala,1259541
PÄ«pri,India,Maharashtra,1259552
Pipraich,India,Uttar Pradesh,1259554
Pipili,India,Odisha,1259592
PÄ«pÄr,India,Rajasthan,1259608
Pinjaur,India,Haryana,1259630
PindwÄra,India,Rajasthan,1259638
PinÄhat,India,Uttar Pradesh,1259647
Pimpri,India,Maharashtra,1259652
Pilkhua,India,Uttar Pradesh,1259680
PÄ«libhÄ«t,India,Uttar Pradesh,1259686
Pilibangan,India,Rajasthan,1259688
PilÄni,India,Rajasthan,1259693
PihÄnÄ«,India,Uttar Pradesh,1259701
Phulpur,India,Uttar Pradesh,1259735
Phulera,India,Rajasthan,1259744
PhulabÄni,India,Odisha,1259756
Phirangipuram,India,Andhra Pradesh,1259773
Phillaur,India,Punjab,1259775
Phek,India,Manipur,1259784
PhaphÅ«nd,India,Uttar Pradesh,1259801
Phaltan,India,Maharashtra,1259811
Phalodi,India,Rajasthan,1259813
Phalauda,India,Uttar Pradesh,1259818
PhagwÄra,India,Punjab,1259827
PetlÄd,India,Gujarat,1259841
Perundurai,India,Tamil Nadu,1259855
PerumpÄvÅ«r,India,Kerala,1259857
Periyanayakkanpalaiyam,India,Tamil Nadu,1259878
Periyakulam,India,Tamil Nadu,1259879
Peravurani,India,Tamil Nadu,1259890
PeranÄmpattu,India,Tamil Nadu,1259892
Perambalur,India,Tamil Nadu,1259896
Penukonda,India,Andhra Pradesh,1259905
Penugonda,India,Andhra Pradesh,1259907
PennÄgaram,India,Tamil Nadu,1259916
PennÄdam,India,Tamil Nadu,1259917
Pen,India,Maharashtra,1259931
Pehowa,India,Haryana,1259939
PeddÄpuram,India,Andhra Pradesh,1259954
Peddapalli,India,Telangana,1259961
Pedana,India,Andhra Pradesh,1259986
PayyannÅ«r,India,Kerala,1259994
PawÄyan,India,Uttar Pradesh,1260003
PÄvugada,India,Karnataka,1260014
Pauri,India,Uttarakhand,1260016
Pawni,India,Maharashtra,1260022
PÄtÅ«r,India,Maharashtra,1260035
Pattukkottai,India,Tamil Nadu,1260040
Patti,India,Punjab,1260045
PatnÄgarh,India,Odisha,1260082
Patna,India,Bihar,1260086
PatiÄla,India,Punjab,1260107
PÄthri,India,Maharashtra,1260120
Patharia,India,Madhya Pradesh,1260129
PÄthardih,India,Jharkhand,1260134
PÄthardi,India,Maharashtra,1260135
PathÄnkot,India,Punjab,1260137
PathanÄmthitta,India,Kerala,1260138
Pathalgaon,India,Chhattisgarh,1260141
Pataudi,India,Haryana,1260156
Patancheru,India,Telangana,1260168
PÄtan,India,Gujarat,1260173
PatÄmundai,India,Odisha,1260178
PÄsighÄt,India,Arunachal Pradesh,1260206
PasÄn,India,Chhattisgarh,1260210
Parvatsar,India,Rajasthan,1260221
PÄrvatipuram,India,Andhra Pradesh,1260222
PartÅ«r,India,Maharashtra,1260228
Parola,India,Maharashtra,1260274
Parli VaijnÄth,India,Maharashtra,1260290
ParlÄkimidi,India,Andhra Pradesh,1260296
PariyÄpuram,India,Kerala,1260304
ParÄ«chhatgarh,India,Uttar Pradesh,1260313
PÄrdi,India,Gujarat,1260335
Parbhani,India,Maharashtra,1260341
ParavÅ«r,India,Kerala,1260354
ParÄsia,India,Madhya Pradesh,1260368
Paramagudi,India,Tamil Nadu,1260387
ParÄdÄ«p Garh,India,Odisha,1260393
PÄppinisshÄ“ri,India,Kerala,1260406
Papanasam,India,Tamil Nadu,1260417
PÄonta SÄhib,India,Himachal Pradesh,1260421
Panvel,India,Maharashtra,1260434
Panruti,India,Tamil Nadu,1260448
Panna,India,Madhya Pradesh,1260454
Panmana,India,Kerala,1260456
PÄnÄ«pat,India,Haryana,1260476
PÄnihÄti,India,West Bengal,1260482
Pandua,India,West Bengal,1260527
PÄndhurnÄ,India,Madhya Pradesh,1260543
Pandharpur,India,Maharashtra,1260546
French Rocks,India,Karnataka,1260553
Panaji,India,Goa,1260607
PanÄgar,India,Madhya Pradesh,1260612
Palwal,India,Haryana,1260637
PÄloncha,India,Telangana,1260667
Palani,India,Tamil Nadu,1260671
Palmaner,India,Andhra Pradesh,1260674
Pallippatti,India,Tamil Nadu,1260681
Pallikondai,India,Tamil Nadu,1260685
PallÄvaram,India,Tamil Nadu,1260692
Pallappatti,India,Tamil Nadu,1260694
Palladam,India,Tamil Nadu,1260697
PÄlkonda,India,Andhra Pradesh,1260702
PÄlitÄna,India,Gujarat,1260707
PaliÄ KalÄn,India,Uttar Pradesh,1260713
PÄli,India,Rajasthan,1260716
PÄli,India,Madhya Pradesh,1260718
Palakkad,India,Kerala,1260728
PÄlghar,India,Maharashtra,1260730
Palera,India,Madhya Pradesh,1260734
PalÄsa,India,Andhra Pradesh,1260771
PÄlanpur,India,Gujarat,1260777
PÄlakollu,India,Andhra Pradesh,1260792
PÄlakkodu,India,Tamil Nadu,1260793
PÄkaur,India,Jharkhand,1260824
PÄkÄla,India,Andhra Pradesh,1260830
Paithan,India,Maharashtra,1260833
PahÄsu,India,Uttar Pradesh,1260868
Padrauna,India,Uttar Pradesh,1260909
Padra,India,Gujarat,1260911
PadmanÄbhapuram,India,Tamil Nadu,1260918
Padampur,India,Rajasthan,1260938
Padampur,India,Odisha,1260940
Padam,India,Kashmir,1260942
Pachperwa,India,Uttar Pradesh,1260954
PÄchora,India,Maharashtra,1260959
OttappÄlam,India,Kerala,1261008
Osmanabad,India,Maharashtra,1261012
Orai,India,Uttar Pradesh,1261039
Ongole,India,Andhra Pradesh,1261045
Okha,India,Gujarat,1261066
Ozar,India,Maharashtra,1261068
Obra,India,Uttar Pradesh,1261086
NÅ«zvÄ«d,India,Andhra Pradesh,1261110
NÅ«rpur,India,Uttar Pradesh,1261122
Nowrangapur,India,Odisha,1261162
North Lakhimpur,India,Assam,1261181
North GuwÄhÄti,India,Assam,1261186
Nongstoin,India,Meghalaya,1261205
Nokha,India,Rajasthan,1261227
Nohar,India,Rajasthan,1261234
NoÄmundi,India,Jharkhand,1261242
NizÄmÄbÄd,India,Telangana,1261258
NirmÄli,India,Bihar,1261285
Nirmal,India,Telangana,1261288
NipÄni,India,Maharashtra,1261309
Neem ka Thana,India,Rajasthan,1261342
NÄ«mbÄhera,India,Rajasthan,1261369
NimÄparha,India,Odisha,1261375
NÄ«mÄj,India,Rajasthan,1261378
NÄ«lokheri,India,Haryana,1261382
NÄ«lÄ“shwar,India,Kerala,1261394
Nilanga,India,Maharashtra,1261396
Nilakottai,India,Tamil Nadu,1261401
NÄ«lgiri,India,Odisha,1261402
Nihtaur,India,Uttar Pradesh,1261415
Nidadavole,India,Andhra Pradesh,1261446
Nichlaul,India,Uttar Pradesh,1261451
NeyyÄttinkara,India,Kerala,1261470
New Delhi,India,NCT,1261481
Neral,India,Maharashtra,1261512
NepÄnagar,India,Madhya Pradesh,1261517
Nellore,India,Andhra Pradesh,1261529
Nellikkuppam,India,Tamil Nadu,1261532
Nelamangala,India,Karnataka,1261539
NedumangÄd,India,Kerala,1261553
NÄyudupeta,India,Andhra Pradesh,1261567
NayÄgarh,India,Odisha,1261580
NawÄshahr,India,Punjab,1261598
Nawalgarh,India,Rajasthan,1261613
Niwai,India,Rajasthan,1261614
NawÄda,India,Bihar,1261631
NawÄbganj,India,Uttar Pradesh,1261639
NawÄbganj,India,Uttar Pradesh,1261641
NawÄbganj,India,Uttar Pradesh,1261642
NÄwa,India,Rajasthan,1261647
Navalgund,India,Karnataka,1261667
NavadwÄ«p,India,West Bengal,1261669
Nautanwa,India,Uttar Pradesh,1261672
Naugachhia,India,Bihar,1261696
Nattam,India,Tamil Nadu,1261705
NÄthdwÄra,India,Rajasthan,1261711
NasrullÄhganj,India,Madhya Pradesh,1261721
NÄsriganj,India,Bihar,1261722
NÄspur,India,Telangana,1261726
NasÄ«rÄbÄd,India,Rajasthan,1261727
Nashik,India,Maharashtra,1261731
Narwar,India,Madhya Pradesh,1261736
NarwÄna,India,Haryana,1261739
NarsÄ«patnam,India,Andhra Pradesh,1261748
Narsinghgarh,India,Madhya Pradesh,1261752
Narsimhapur,India,Madhya Pradesh,1261754
NÄrnaund,India,Haryana,1261771
NÄrnaul,India,Haryana,1261772
Nargund,India,Karnataka,1261800
Naregal,India,Karnataka,1261810
NÄrÄyanpet,India,Telangana,1261823
NarÄyangarh,India,Haryana,1261828
NÄravÄrikuppam,India,Tamil Nadu,1261835
Naraura,India,Uttar Pradesh,1261837
Narauli,India,Uttar Pradesh,1261839
Narasaraopet,India,Andhra Pradesh,1261848
Narasapur,India,Andhra Pradesh,1261852
Narasannapeta,India,Andhra Pradesh,1261853
Naraini,India,Madhya Pradesh,1261871
Naraina,India,Rajasthan,1261872
NapÄsar,India,Rajasthan,1261882
NÄnpÄra,India,Uttar Pradesh,1261901
NanjangÅ«d,India,Karnataka,1261910
NÄngloi JÄt,India,NCT,1261913
NÄngal Township,India,Punjab,1261922
NandyÄl,India,Andhra Pradesh,1261927
Nandurbar,India,Maharashtra,1261931
NÄndÅ«ra Buzurg,India,Maharashtra,1261932
NandikotkÅ«r,India,Andhra Pradesh,1261957
NandigÄma,India,Andhra Pradesh,1261960
NÄndgaon,India,Maharashtra,1261971
Nanded,India,Maharashtra,1261977
Nanauta,India,Uttar Pradesh,1261998
NÄmrup,India,Assam,1262013
NambiyÅ«r,India,Tamil Nadu,1262034
NÄmakkal,India,Tamil Nadu,1262039
NÄmagiripettai,India,Tamil Nadu,1262040
NalhÄti,India,West Bengal,1262065
Nalgonda,India,Telangana,1262067
Naldurg,India,Maharashtra,1262073
NakÅ«r,India,Uttar Pradesh,1262089
NaksalbÄri,India,West Bengal,1262092
Nakodar,India,Punjab,1262097
NajÄ«bÄbÄd,India,Uttar Pradesh,1262109
Nainwa,India,Rajasthan,1262115
Nainpur,India,Madhya Pradesh,1262116
Naini TÄl,India,Uttarakhand,1262117
NaihÄti,India,West Bengal,1262131
Nahorkatiya,India,Assam,1262140
NÄhan,India,Himachal Pradesh,1262151
Nagpur,India,Maharashtra,1262180
NÄgod,India,Madhya Pradesh,1262187
NagÄ«na,India,Uttar Pradesh,1262200
NÄgercoil,India,Tamil Nadu,1262204
Nagda,India,Madhya Pradesh,1262209
NÄgaur,India,Rajasthan,1262216
NÄgar KarnÅ«l,India,Telangana,1262230
Nagari,India,Andhra Pradesh,1262240
Nagar,India,Rajasthan,1262253
NÄgappattinam,India,Tamil Nadu,1262260
NÄgamangala,India,Karnataka,1262266
NaduvannÅ«r,India,Kerala,1262285
NadiÄd,India,Gujarat,1262292
NÄdbai,India,Rajasthan,1262296
NÄdÄpuram,India,Kerala,1262302
NabÄ«nagar,India,Bihar,1262318
NÄbha,India,Punjab,1262319
Mysore,India,Karnataka,1262321
Muzaffarpur,India,Bihar,1262330
Muzaffarnagar,India,Uttar Pradesh,1262332
MÅ«vattupula,India,Kerala,1262338
Muttupet,India,Tamil Nadu,1262346
Mussoorie,India,Uttarakhand,1262374
Musiri,India,Tamil Nadu,1262380
MushÄbani,India,Jharkhand,1262382
MurwÄra,India,Madhya Pradesh,1262395
MurtajÄpur,India,Maharashtra,1262410
MurshidÄbÄd,India,West Bengal,1262412
MurlÄ«ganj,India,Bihar,1262419
Morinda,India,Punjab,1262426
MurbÄd,India,Maharashtra,1262444
MurÄdnagar,India,Uttar Pradesh,1262453
Munnar,India,Kerala,1262463
Monghyr,India,Bihar,1262482
Mungeli,India,Chhattisgarh,1262484
Mungaoli,India,Madhya Pradesh,1262485
MÅ«ndwa,India,Rajasthan,1262491
Mundra,India,Gujarat,1262497
Mundgod,India,Karnataka,1262510
Mundargi,India,Karnataka,1262516
Multai,India,Madhya Pradesh,1262534
MÅ«lki,India,Karnataka,1262546
Mulgund,India,Karnataka,1262553
MulbÄgal,India,Karnataka,1262562
Muluppilagadu,India,Kerala,1262566
MÅ«l,India,Maharashtra,1262574
Muktsar,India,Punjab,1262578
Mukher,India,Maharashtra,1262591
MukeriÄn,India,Punjab,1262596
MuhammadÄbÄd,India,Uttar Pradesh,1262624
MuhammadÄbÄd,India,Uttar Pradesh,1262625
MuhammadÄbÄd,India,Uttar Pradesh,1262626
Mughal SarÄi,India,Uttar Pradesh,1262634
Mudkhed,India,Maharashtra,1262651
Mudhol,India,Karnataka,1262663
Mudgal,India,Karnataka,1262664
MuddebihÄl,India,Karnataka,1262669
MÅ«dbidri,India,Karnataka,1262672
MubÄrakpur,India,Uttar Pradesh,1262678
MothÄ«hÄri,India,Bihar,1262710
Morwa,India,Gujarat,1262734
Morsi,India,Maharashtra,1262740
Morena,India,Madhya Pradesh,1262771
Morbi,India,Gujarat,1262775
MorÄr,India,Madhya Pradesh,1262783
Moram,India,Maharashtra,1262794
MorÄdÄbÄd,India,Uttar Pradesh,1262801
Mon,India,Nagaland,1262824
MokokchÅ«ng,India,Nagaland,1262843
Mokameh,India,Bihar,1262852
MoirÄng,India,Manipur,1262863
Moga,India,Punjab,1262951
ModÄsa,India,Gujarat,1262958
Misrikh,India,Uttar Pradesh,1262988
MirzÄpur,India,Uttar Pradesh,1262995
MiriÄlgÅ«da,India,Telangana,1263012
MÄ«rganj,India,Uttar Pradesh,1263015
MÄ«rÄnpur Katra,India,Uttar Pradesh,1263021
MÄ«rÄnpur,India,Uttar Pradesh,1263022
MÄ«njÅ«r,India,Tamil Nadu,1263034
Milak,India,Uttar Pradesh,1263051
Mihona,India,Madhya Pradesh,1263057
MhÄsvÄd,India,Maharashtra,1263083
Mettur,India,Tamil Nadu,1263101
Mettupalayam,India,Tamil Nadu,1263103
Merta,India,Rajasthan,1263120
Mendarda,India,Gujarat,1263142
MemÄri,India,West Bengal,1263148
Melur,India,Tamil Nadu,1263151
MehndÄwal,India,Uttar Pradesh,1263185
Mehekar,India,Maharashtra,1263195
Meerut,India,Uttar Pradesh,1263214
MedinÄ«pur,India,West Bengal,1263220
Medak,India,Telangana,1263230
Mayiladuthurai,India,Tamil Nadu,1263247
MayÄng ImphÄl,India,Manipur,1263255
MawÄna,India,Uttar Pradesh,1263275
Mavoor,India,Kerala,1263280
MÄvelikara,India,Kerala,1263285
Maur,India,Punjab,1263293
Mauganj,India,Madhya Pradesh,1263300
Maudaha,India,Uttar Pradesh,1263303
Mau Aimma,India,Uttar Pradesh,1263306
Mau,India,Madhya Pradesh,1263309
Mau,India,Uttar Pradesh,1263311
MattanÅ«r,India,Kerala,1263331
Mathura,India,Uttar Pradesh,1263364
MÄtÄbhÄnga,India,West Bengal,1263395
Masaurhi Buzurg,India,Bihar,1263427
Marmagao,India,Goa,1263494
MÄrkÄpur,India,Andhra Pradesh,1263504
MariÄni,India,Assam,1263522
MariÄhu,India,Uttar Pradesh,1263523
Marhaura,India,Bihar,1263528
Margherita,India,Arunachal Pradesh,1263532
Marakkanam,India,Tamil Nadu,1263564
MÄrahra,India,Uttar Pradesh,1263567
MÄpuca,India,Goa,1263580
MÄnwat,India,Maharashtra,1263591
MÄnvi,India,Karnataka,1263594
Manthani,India,Telangana,1263610
MÄnsa,India,Punjab,1263622
MÄnsa,India,Gujarat,1263623
Manoharpur,India,Rajasthan,1263649
Mannargudi,India,Tamil Nadu,1263659
MannÄrakkÄt,India,Kerala,1263661
ManmÄd,India,Maharashtra,1263664
MankÄchar,India,Meghalaya,1263678
MÄjalgaon,India,Maharashtra,1263684
Manjhanpur,India,Uttar Pradesh,1263691
Manjeri,India,Kerala,1263694
ManihÄri,India,Bihar,1263723
Maniar,India,Uttar Pradesh,1263730
MangrÅ«l PÄ«r,India,Maharashtra,1263744
MÄngrol,India,Rajasthan,1263751
MÄngrol,India,Gujarat,1263752
Manglaur,India,Uttarakhand,1263761
Mangalore,India,Karnataka,1263780
Mangaldai,India,Assam,1263787
Mangalagiri,India,Andhra Pradesh,1263797
Maner,India,Bihar,1263807
Mandya,India,Karnataka,1263814
MÄndvi,India,Gujarat,1263824
MÄndvi,India,Gujarat,1263826
MÄndu,India,Madhya Pradesh,1263833
Mandsaur,India,Madhya Pradesh,1263834
MandlÄ,India,Madhya Pradesh,1263852
Mandi,India,Himachal Pradesh,1263862
MandÄwar,India,Uttar Pradesh,1263879
Mandapeta,India,Andhra Pradesh,1263898
Mandapam,India,Tamil Nadu,1263900
MÄndalgarh,India,Rajasthan,1263911
MÄndal,India,Rajasthan,1263917
MancherÄl,India,Telangana,1263936
ManÄwar,India,Madhya Pradesh,1263940
MÄnÄvadar,India,Gujarat,1263943
ManÄsa,India,Madhya Pradesh,1263949
Manapparai,India,Tamil Nadu,1263952
Manamadurai,India,Tamil Nadu,1263965
Manali,India,Tamil Nadu,1263968
MÄlvan,India,Maharashtra,1264007
MÄlÅ«r,India,Karnataka,1264010
MÄlpura,India,Rajasthan,1264032
Malpe,India,Karnataka,1264037
Mallasamudram,India,Tamil Nadu,1264047
MalkÄpur,India,Maharashtra,1264071
Malakanagiri,India,Odisha,1264075
MalÄ«hÄbÄd,India,Uttar Pradesh,1264085
MÄler Kotla,India,Punjab,1264111
MÄlegaon,India,Maharashtra,1264115
Malavalli,India,Karnataka,1264136
Malaut,India,Punjab,1264138
Malappuram,India,Kerala,1264154
MÄkum,India,Assam,1264196
Maksi,India,Madhya Pradesh,1264198
MakrÄna,India,Rajasthan,1264206
Mairwa,India,Bihar,1264282
Mainpuri,India,Uttar Pradesh,1264292
MainÄguri,India,West Bengal,1264301
Maihar,India,Madhya Pradesh,1264317
Mahwah,India,Rajasthan,1264323
Mahudha,India,Gujarat,1264344
Maholi,India,Uttar Pradesh,1264356
MahobÄ,India,Uttar Pradesh,1264359
MahmudÄbÄd,India,Uttar Pradesh,1264363
MahÄ«shÄdal,India,West Bengal,1264368
MahgawÄn,India,Madhya Pradesh,1264383
Maheshwar,India,Madhya Pradesh,1264385
Mahendragarh,India,Haryana,1264395
MahemdÄvÄd,India,Gujarat,1264398
MahÄ“,India,Kerala,1264403
MahbÅ«bnagar,India,Telangana,1264407
MahbÅ«bÄbÄd,India,Telangana,1264409
MahÄsamund,India,Chhattisgarh,1264414
MahÄrÄganj,India,Uttar Pradesh,1264433
MahÄrÄjgani,India,Bihar,1264436
Maham,India,Haryana,1264455
MahÄlingpur,India,Karnataka,1264457
MahÄd,India,Maharashtra,1264489
Maghar,India,Uttar Pradesh,1264504
MÄgadi,India,Karnataka,1264514
MadurÄntakam,India,Tamil Nadu,1264520
Madurai,India,Tamil Nadu,1264521
MadukkÅ«r,India,Tamil Nadu,1264523
Madukkarai,India,Tamil Nadu,1264524
Chennai,India,Tamil Nadu,1264527
Madikeri,India,Karnataka,1264540
Madhyamgram,India,West Bengal,1264543
Madhupur,India,Jharkhand,1264551
Maddagiri,India,Karnataka,1264553
Madhubani,India,Bihar,1264555
Madhipura,India,Bihar,1264570
Madgaon,India,Goa,1264588
MaddÅ«r,India,Karnataka,1264592
Madanapalle,India,Andhra Pradesh,1264621
MachilÄ«patnam,India,Andhra Pradesh,1264637
MachhlÄ«shahr,India,Uttar Pradesh,1264643
MÄchhÄ«wÄra,India,Punjab,1264644
MÄcherla,India,Andhra Pradesh,1264647
Lunglei,India,Mizoram,1264688
LÅ«nÄvÄda,India,Gujarat,1264700
LudhiÄna,India,Punjab,1264728
Lucknow,India,Uttar Pradesh,1264733
Luckeesarai,India,Bihar,1264735
Losal,India,Rajasthan,1264756
Loni,India,Uttar Pradesh,1264773
Lonavla,India,Maharashtra,1264793
LonÄr,India,Maharashtra,1264794
LohÄrdaga,India,Jharkhand,1264839
LingsugÅ«r,India,Karnataka,1264890
Limbdi,India,Gujarat,1264912
Leteri,India,Madhya Pradesh,1264949
Leh,India,Kashmir,1264976
LÄwar KhÄs,India,Uttar Pradesh,1264989
LaungowÄl,India,Punjab,1265007
Latur,India,Maharashtra,1265014
LÄthi,India,Gujarat,1265022
LÄtehÄr,India,Jharkhand,1265025
Lar,India,Uttar Pradesh,1265053
LÄlsot,India,Rajasthan,1265143
LÄlpur,India,Gujarat,1265150
Lalitpur,India,Uttar Pradesh,1265157
Lalgudi,India,Tamil Nadu,1265163
LÄlgola,India,West Bengal,1265166
LÄlganj,India,Uttar Pradesh,1265169
LÄlganj,India,Bihar,1265170
Lakshmeshwar,India,Karnataka,1265201
Laksar,India,Uttarakhand,1265208
Lakhyabad,India,West Bengal,1265220
LakhnÄdon,India,Madhya Pradesh,1265233
LakhÄ«mpur,India,Uttar Pradesh,1265242
LÄkheri,India,Rajasthan,1265246
LÄharpur,India,Uttar Pradesh,1265310
LahÄr,India,Madhya Pradesh,1265311
LÄdwa,India,Haryana,1265323
LÄdnÅ«n,India,Rajasthan,1265331
Lachhmangarh SÄ«kar,India,Rajasthan,1265354
Kuzhithurai,India,Tamil Nadu,1265387
Koothanallur,India,Tamil Nadu,1265400
Kuttampuzha,India,Kerala,1265401
KutiyÄna,India,Gujarat,1265415
Kutiatodu,India,Kerala,1265418
Kushtagi,India,Karnataka,1265446
KurinjippÄdi,India,Tamil Nadu,1265504
KurduvÄdi,India,Maharashtra,1265521
KurandvÄd,India,Maharashtra,1265539
Kuppam,India,Andhra Pradesh,1265555
Kunnamkulam,India,Kerala,1265579
Kunnamangalam,India,Kerala,1265580
Kunigal,India,Karnataka,1265591
Kundla,India,Gujarat,1265605
Kundgol,India,Karnataka,1265607
Kundarkhi,India,Uttar Pradesh,1265613
Kunda,India,Uttar Pradesh,1265632
Kumta,India,Karnataka,1265645
KÅ«mher,India,Rajasthan,1265655
KumhÄri,India,Chhattisgarh,1265660
KumbhrÄj,India,Madhya Pradesh,1265670
Kumbakonam,India,Tamil Nadu,1265683
Kulu,India,Himachal Pradesh,1265709
Kulti,India,West Bengal,1265711
KulpahÄr,India,Uttar Pradesh,1265716
Kulittalai,India,Tamil Nadu,1265723
Kulgam,India,Kashmir,1265734
Kukshi,India,Madhya Pradesh,1265752
KÅ«katpalli,India,Telangana,1265767
Kuju,India,Jharkhand,1265773
KÅ«dligi,India,Karnataka,1265795
Kudachi,India,Karnataka,1265811
Kuchera,India,Rajasthan,1265821
KuchÄman,India,Rajasthan,1265828
Kuchaiburi,India,Odisha,1265830
KrishnarÄjpet,India,Karnataka,1265852
Krishnanagar,India,West Bengal,1265859
Krishnagiri,India,Tamil Nadu,1265863
Kozhikode,India,Kerala,1265873
Koynanagar,India,Maharashtra,1265881
KovvÅ«r,India,Andhra Pradesh,1265886
KovÅ«r,India,Andhra Pradesh,1265888
Kovilpatti,India,Tamil Nadu,1265891
KottÅ«ru,India,Karnataka,1265905
Kottayam,India,Kerala,1265911
KottagÅ«dem,India,Telangana,1265938
Kotputli,India,Rajasthan,1265961
Kotma,India,Madhya Pradesh,1265964
KotdwÄra,India,Uttarakhand,1266014
KotapÄrh,India,Chhattisgarh,1266029
Kotamangalam,India,Kerala,1266031
Kotagiri,India,Tamil Nadu,1266038
Kota,India,Rajasthan,1266049
KotÄ,India,Chhattisgarh,1266051
Kosigi,India,Andhra Pradesh,1266070
Kosi,India,Uttar Pradesh,1266073
Kosamba,India,Gujarat,1266087
Korwai,India,Madhya Pradesh,1266092
Koregaon,India,Maharashtra,1266116
Korba,India,Chhattisgarh,1266122
Koratla,India,Telangana,1266124
KorÄput,India,Odisha,1266128
Koppal,India,Karnataka,1266154
Kopargaon,India,Maharashtra,1266162
KopÄganj,India,Uttar Pradesh,1266164
KonnÅ«r,India,Karnataka,1266178
Konnagar,India,West Bengal,1266179
Kondapalle,India,Andhra Pradesh,1266209
Kondagaon,India,Chhattisgarh,1266216
Konch,India,Uttar Pradesh,1266217
KonÄrka,India,Odisha,1266220
Kolasib,India,Mizoram,1266258
KollegÄl,India,Karnataka,1266267
KolhÄpur,India,Maharashtra,1266285
KolÄras,India,Madhya Pradesh,1266302
KolÄr,India,Karnataka,1266305
Colachel,India,Tamil Nadu,1266322
Kokrajhar,India,Assam,1266330
Kohima,India,Nagaland,1266366
KoelwÄr,India,Bihar,1266372
KodungallÅ«r,India,Kerala,1266385
Kodoli,India,Maharashtra,1266390
KodÄ«nar,India,Gujarat,1266397
KodarmÄ,India,Jharkhand,1266414
KodÄr,India,Telangana,1266416
KodaikÄnÄl,India,Tamil Nadu,1266425
Koch BihÄr,India,West Bengal,1266436
KoÄth,India,Bihar,1266448
Kizhake ChÄlakudi,India,Kerala,1266452
Kithor,India,Uttar Pradesh,1266461
KishtwÄr,India,Kashmir,1266475
Kishangarh,India,Rajasthan,1266486
Kishanganj,India,Bihar,1266489
KÄ«ratpur,India,Uttar Pradesh,1266509
Kiraoli,India,Uttar Pradesh,1266510
Kinwat,India,Maharashtra,1266518
Kichha,India,Uttarakhand,1266575
KhÅ«tÄr,India,Uttar Pradesh,1266596
Khurja,India,Uttar Pradesh,1266607
Khurda,India,Odisha,1266616
Khurai,India,Madhya Pradesh,1266620
Khunti,India,Jharkhand,1266622
KhuldÄbÄd,India,Maharashtra,1266631
Khowai,India,Tripura,1266649
Khopoli,India,Maharashtra,1266666
KhirkiyÄn,India,Madhya Pradesh,1266710
Khilchipur,India,Madhya Pradesh,1266731
Khetri,India,Rajasthan,1266744
Khetia,India,Maharashtra,1266746
Kheri,India,Uttar Pradesh,1266762
KherÄlu,India,Gujarat,1266774
Khekra,India,Uttar Pradesh,1266794
Khed Brahma,India,Gujarat,1266806
Kheda,India,Gujarat,1266809
KhÄtra,India,West Bengal,1266838
KhatÄ«ma,India,Uttarakhand,1266843
KhÄtegaon,India,Madhya Pradesh,1266847
Khatauli,India,Uttar Pradesh,1266849
KhÄrupatia,India,Assam,1266862
Kharsia,India,Chhattisgarh,1266872
Kharkhauda,India,Haryana,1266891
Khargone,India,Madhya Pradesh,1266928
Khardah,India,West Bengal,1266945
Kharar,India,Punjab,1266960
Kharakvasla,India,Maharashtra,1266966
Kharagpur,India,Bihar,1266975
Kharagpur,India,West Bengal,1266976
KhÄpa,India,Maharashtra,1267006
Khanna,India,Punjab,1267016
Khandwa,India,Madhya Pradesh,1267031
Khandela,India,Rajasthan,1267044
KhÄnÄpur,India,Karnataka,1267065
Khammam,India,Telangana,1267076
KhÄmgaon,India,Maharashtra,1267084
KhambhÄt,India,Gujarat,1267090
KhambhÄliya,India,Gujarat,1267091
Khamaria,India,Madhya Pradesh,1267097
KhalÄ«lÄbÄd,India,Uttar Pradesh,1267115
KhajurÄho,India,Madhya Pradesh,1267154
KhairÄgarh,India,Chhattisgarh,1267173
KhairÄgarh,India,Chhattisgarh,1267174
KhairÄbÄd,India,Uttar Pradesh,1267175
Khair,India,Uttar Pradesh,1267182
Khagaul,India,Bihar,1267187
Khagaria,India,Bihar,1267189
Khadki,India,Maharashtra,1267195
Khada,India,Uttar Pradesh,1267202
KhÄchrod,India,Madhya Pradesh,1267203
Kesinga,India,Odisha,1267222
Keshorai PÄtan,India,Rajasthan,1267226
Keshod,India,Gujarat,1267227
KerÅ«r,India,Karnataka,1267239
KendrÄparha,India,Odisha,1267283
Kenda,India,West Bengal,1267290
KemrÄ«,India,Uttar Pradesh,1267297
Kekri,India,Rajasthan,1267336
KÄyankulam,India,Kerala,1267360
Kayalpattinam,India,Tamil Nadu,1267361
Kawardha,India,Chhattisgarh,1267369
KÄvali,India,Andhra Pradesh,1267394
KattivÄkkam,India,Tamil Nadu,1267433
Kattanam,India,Kerala,1267435
KÄtrÄs,India,Jharkhand,1267439
KÄtpÄdi,India,Tamil Nadu,1267456
KÄtoya,India,West Bengal,1267457
KÄtol,India,Maharashtra,1267461
Katihar,India,Bihar,1267480
Kathua,India,Kashmir,1267486
KÄthor,India,Gujarat,1267492
Katghora,India,Chhattisgarh,1267517
Katangi,India,Madhya Pradesh,1267537
Katangi,India,Madhya Pradesh,1267538
KasrÄwad,India,Madhya Pradesh,1267558
Kashipur,India,Uttarakhand,1267579
KÄsganj,India,Uttar Pradesh,1267588
KÄsaragod,India,Kerala,1267616
Karwar,India,Karnataka,1267635
Karur,India,Tamil Nadu,1267648
KartÄrpur,India,Punjab,1267669
KÄrsiyÄng,India,West Bengal,1267675
Karol BÄgh,India,NCT,1267696
KarnÄl,India,Haryana,1267708
KarmÄla,India,Maharashtra,1267716
KÄrkala,India,Karnataka,1267739
Karjat,India,Maharashtra,1267742
KarÄ«mnagar,India,Telangana,1267755
KarÄ«mganj,India,Assam,1267758
Karhal,India,Uttar Pradesh,1267772
Karera,India,Madhya Pradesh,1267786
Kareli,India,Madhya Pradesh,1267794
Karauli,India,Rajasthan,1267819
KÄranja,India,Maharashtra,1267853
Karamsad,India,Gujarat,1267862
KÄramadai,India,Tamil Nadu,1267869
KÄraikkudi,India,Tamil Nadu,1267885
KÄraikÄl,India,Pondicherry,1267887
KarÄd,India,Maharashtra,1267904
KapÅ«rthala,India,Punjab,1267911
KÄpren,India,Rajasthan,1267923
Kapadvanj,India,Gujarat,1267939
KÄnth,India,Uttar Pradesh,1267972
KantÄbÄnji,India,Odisha,1267978
KÄnt,India,Uttar Pradesh,1267979
Kanpur,India,Uttar Pradesh,1267995
Kannod,India,Madhya Pradesh,1268007
KanniyÄkumÄri,India,Tamil Nadu,1268008
Kannauj,India,Uttar Pradesh,1268011
KÄnnangÄd,India,Kerala,1268015
Kannad,India,Maharashtra,1268020
KÄnker,India,Chhattisgarh,1268031
KÄnke,India,Jharkhand,1268032
Kankauli,India,Maharashtra,1268035
Kanigiri,India,Andhra Pradesh,1268059
Kangayam,India,Tamil Nadu,1268095
KandukÅ«r,India,Andhra Pradesh,1268111
KÄndla,India,Gujarat,1268124
KÄndi,India,West Bengal,1268135
KÄndhla,India,Uttar Pradesh,1268138
KÄnchipuram,India,Tamil Nadu,1268159
Kanakapura,India,Karnataka,1268189
KÄmthi,India,Maharashtra,1268205
Kampli,India,Karnataka,1268214
Cumbum,India,Tamil Nadu,1268246
KÄmÄrhÄti,India,West Bengal,1268257
KÄmÄreddi,India,Telangana,1268259
KÄman,India,Rajasthan,1268266
Kamalganj,India,Uttar Pradesh,1268276
KÄmÄkhyÄnagar,India,Odisha,1268279
Kalyani,India,West Bengal,1268293
KalyÄn,India,Maharashtra,1268295
Kalugumalai,India,Tamil Nadu,1268310
KÄlpi,India,Uttar Pradesh,1268325
Kalpetta,India,Kerala,1268327
KÄlol,India,Gujarat,1268339
KÄlna,India,West Bengal,1268341
Kalmeshwar,India,Maharashtra,1268344
Kallidaikurichchi,India,Tamil Nadu,1268360
Kallakkurichchi,India,Tamil Nadu,1268376
KÄlka,India,Himachal Pradesh,1268381
KÄliyÄganj,India,West Bengal,1268383
KÄlimpong,India,West Bengal,1268403
Kalghatgi,India,Karnataka,1268434
KÄlÄvad,India,Gujarat,1268450
KÄlÄnwÄli,India,Haryana,1268469
KalÄnaur,India,Haryana,1268476
KalamnÅ«ri,India,Maharashtra,1268480
Kalamb,India,Maharashtra,1268484
KalakkÄdu,India,Tamil Nadu,1268495
KakrÄla,India,Uttar Pradesh,1268540
KÄkori,India,Uttar Pradesh,1268545
KÄkinÄda,India,Andhra Pradesh,1268561
Kakching,India,Manipur,1268567
Kaithal,India,Haryana,1268593
KairÄna,India,Uttar Pradesh,1268601
Kaimori,India,Madhya Pradesh,1268615
Kaimganj,India,Uttar Pradesh,1268616
KailÄshahar,India,Tripura,1268622
KailÄras,India,Madhya Pradesh,1268624
KaikalÅ«r,India,Andhra Pradesh,1268627
KÄgal,India,Maharashtra,1268651
KadÅ«r,India,Karnataka,1268662
Kadod,India,Gujarat,1268667
Kadiri,India,Andhra Pradesh,1268673
Kadi,India,Gujarat,1268680
Kadayanallur,India,Tamil Nadu,1268707
KÄnchrÄpÄra,India,West Bengal,1268715
Kachhwa,India,Uttar Pradesh,1268722
KabrÄi,India,Uttar Pradesh,1268739
Junnar,India,Maharashtra,1268761
JÅ«nÄgarh,India,Chhattisgarh,1268772
JÅ«nÄgadh,India,Gujarat,1268773
Jumri TilaiyÄ,India,Jharkhand,1268775
Jalandhar,India,Punjab,1268782
JugsÄlai,India,Jharkhand,1268799
JorhÄt,India,Assam,1268820
Jora,India,Madhya Pradesh,1268823
JolÄrpettai,India,Tamil Nadu,1268834
Jogbani,India,Bihar,1268855
Jodiya Bandar,India,Gujarat,1268863
Jodhpur,India,Rajasthan,1268865
Jodhpur,India,Gujarat,1268866
JintÅ«r,India,Maharashtra,1268896
JÄ«nd,India,Haryana,1268907
JhÅ«si,India,Uttar Pradesh,1268929
JhunjhunÅ«n,India,Rajasthan,1268936
JhinjhÄna,India,Uttar Pradesh,1268961
JhÄ«njhak,India,Uttar Pradesh,1268962
JhÄrsuguda,India,Odisha,1268977
Jharia,India,Jharkhand,1268988
JhÄrgrÄm,India,West Bengal,1268990
JhÄnsi,India,Uttar Pradesh,1269006
JhanjhÄrpur,India,Bihar,1269012
JhÄlu,India,Uttar Pradesh,1269019
JhÄlrapÄtan,India,Rajasthan,1269020
Jhalida,India,West Bengal,1269026
JhÄlÄwÄr,India,Rajasthan,1269027
Jhajjar,India,Haryana,1269042
JhÄ JhÄ,India,Bihar,1269046
JhÄbua,India,Madhya Pradesh,1269053
Jewar,India,Uttar Pradesh,1269056
Jevargi,India,Karnataka,1269057
Jetpur,India,Gujarat,1269065
Jeypore,India,Odisha,1269092
Jaynagar,India,Bihar,1269093
Jaynagar-Majilpur,India,West Bengal,1269094
Jayamkondacholapuram,India,Tamil Nadu,1269102
JÄwad,India,Madhya Pradesh,1269126
Jaunpur,India,Uttar Pradesh,1269135
JatÄra,India,Madhya Pradesh,1269153
Jatani,India,Odisha,1269154
Jaswantnagar,India,Uttar Pradesh,1269158
Jaspur,India,Uttarakhand,1269168
Jasidih,India,Jharkhand,1269175
Jashpurnagar,India,Chhattisgarh,1269177
Jasdan,India,Gujarat,1269179
Jarwal,India,Uttar Pradesh,1269183
JaorÄ,India,Madhya Pradesh,1269217
JÄnsath,India,Uttar Pradesh,1269227
JÄnjgÄ«r,India,Chhattisgarh,1269239
Jangipur,India,West Bengal,1269247
Jangaon,India,Telangana,1269256
JandiÄla,India,Punjab,1269269
JÄmuria,India,West Bengal,1269280
JamÅ«Ä«,India,Bihar,1269291
JÄmtÄra,India,Jharkhand,1269298
Jamshedpur,India,Jharkhand,1269300
JÄmnagar,India,Gujarat,1269317
Jammu,India,Kashmir,1269321
Jammalamadugu,India,Andhra Pradesh,1269323
Jamkhandi,India,Karnataka,1269328
Jambusar,India,Gujarat,1269350
JamÄlpur,India,Bihar,1269374
JÄmai,India,Madhya Pradesh,1269377
JÄmadoba,India,Jharkhand,1269379
JalpÄiguri,India,West Bengal,1269388
Jalor,India,Rajasthan,1269392
JÄlna,India,Maharashtra,1269395
Jalgaon Jamod,India,Maharashtra,1269406
Jalgaon,India,Maharashtra,1269407
Jaleshwar,India,Odisha,1269413
Jalesar,India,Uttar Pradesh,1269415
JÄlaun,India,Uttar Pradesh,1269422
JalÄlpur,India,Uttar Pradesh,1269435
JalÄlpur,India,Gujarat,1269439
JalÄlÄ«,India,Uttar Pradesh,1269441
JalÄlÄbÄd,India,Punjab,1269445
JalÄlÄbad,India,Uttar Pradesh,1269446
JalÄlÄbÄd,India,Uttar Pradesh,1269447
JÄjpur,India,Odisha,1269477
Jaito,India,Punjab,1269488
JaitÄran,India,Rajasthan,1269498
Jaisingpur,India,Maharashtra,1269502
Jaisalmer,India,Rajasthan,1269507
Jais,India,Uttar Pradesh,1269509
Jaipur,India,Rajasthan,1269515
JahÄzpur,India,Rajasthan,1269545
JahÄngÄ«rÄbÄd,India,Uttar Pradesh,1269551
JahÄnÄbÄd,India,Bihar,1269557
JagtiÄl,India,Telangana,1269562
Jagraon,India,Punjab,1269564
Jaggayyapeta,India,Andhra Pradesh,1269570
JagdÄ«spur,India,Bihar,1269573
JagdÄ«shpur,India,Uttar Pradesh,1269574
Jagdalpur,India,Chhattisgarh,1269578
Jagatsinghapur,India,Odisha,1269581
JagalÅ«r,India,Karnataka,1269602
JagÄdhri,India,Haryana,1269605
Jabalpur,India,Madhya Pradesh,1269633
ItimÄdpur,India,Uttar Pradesh,1269646
ItÄrsi,India,Madhya Pradesh,1269653
ItÄnagar,India,Arunachal Pradesh,1269655
IslÄmpur,India,West Bengal,1269665
IslÄmpur,India,Bihar,1269666
IslÄmnagar,India,Uttar Pradesh,1269670
IrugÅ«r,India,Tamil Nadu,1269690
IrinjÄlakuda,India,Kerala,1269693
Iringal,India,Kerala,1269694
IngrÄj BÄzÄr,India,West Bengal,1269723
Indri,India,Haryana,1269731
Indore,India,Madhya Pradesh,1269743
Indi,India,Karnataka,1269751
Indergarh,India,Uttar Pradesh,1269752
IndÄpur,India,Maharashtra,1269761
Imphal,India,Manipur,1269771
Ilkal,India,Karnataka,1269784
Igatpuri,India,Maharashtra,1269810
Idappadi,India,Tamil Nadu,1269819
IchchÄpuram,India,Andhra Pradesh,1269827
Ichalkaranji,India,Maharashtra,1269834
Hyderabad,India,Telangana,1269843
Hadagalli,India,Karnataka,1269849
HusainÄbÄd,India,Jharkhand,1269862
HunsÅ«r,India,Karnataka,1269873
Hungund,India,Karnataka,1269876
Hukeri,India,Karnataka,1269908
Hugli,India,West Bengal,1269910
Hubli,India,Karnataka,1269920
Howli,India,Assam,1269927
HosÅ«r,India,Tamil Nadu,1269934
Hospet,India,Karnataka,1269935
Hoskote,India,Karnataka,1269936
HoshangÄbÄd,India,Madhya Pradesh,1269939
Hosdurga,India,Karnataka,1269943
HonnÄli,India,Karnataka,1269970
HonÄvar,India,Karnataka,1269976
HomnÄbÄd,India,Karnataka,1269979
Hole Narsipur,India,Karnataka,1269985
Holalkere,India,Karnataka,1269990
HojÄi,India,Assam,1269993
Hodal,India,Haryana,1270000
HisuÄ,India,Bihar,1270021
Hisar,India,Haryana,1270022
HiriyÅ«r,India,Karnataka,1270032
HirekerÅ«r,India,Karnataka,1270036
HÄ«rÄkud,India,Odisha,1270059
Hinjilikatu,India,Odisha,1270066
Hingoli,India,Maharashtra,1270072
HinganghÄt,India,Maharashtra,1270077
Hindupur,India,Andhra Pradesh,1270079
Hindoria,India,Madhya Pradesh,1270082
Hindaun,India,Rajasthan,1270090
Himatnagar,India,Gujarat,1270099
Hilsa,India,Bihar,1270102
HazÄrÄ«bÄg,India,Jharkhand,1270164
HÄveri,India,Karnataka,1270171
Hatta,India,Madhya Pradesh,1270185
HÄthras,India,Uttar Pradesh,1270216
HastinÄpur,India,Uttar Pradesh,1270237
Hassan,India,Karnataka,1270239
HÄsimÄra,India,West Bengal,1270245
Hasanpur,India,Uttar Pradesh,1270251
HarÅ«r,India,Tamil Nadu,1270265
HarsÅ«d,India,Madhya Pradesh,1270271
Harpanahalli,India,Karnataka,1270287
HarpÄlpur,India,Madhya Pradesh,1270291
HÄrij,India,Gujarat,1270343
Harihar,India,Karnataka,1270349
Haridwar,India,Uttarakhand,1270351
HardoÄ«,India,Uttar Pradesh,1270370
Harda KhÄs,India,Madhya Pradesh,1270375
HÄpur,India,Uttar Pradesh,1270393
HÄora,India,West Bengal,1270396
HanumÄngarh,India,Rajasthan,1270407
HÄnsi,India,Haryana,1270417
HÄngal,India,Karnataka,1270435
HandiÄ,India,Uttar Pradesh,1270437
HamÄ«rpur,India,Himachal Pradesh,1270454
HamÄ«rpur,India,Uttar Pradesh,1270455
Halvad,India,Gujarat,1270466
HÄlol,India,Gujarat,1270474
Haliyal,India,Karnataka,1270482
HÄlÄ«sahar,India,West Bengal,1270484
Haldwani,India,Uttarakhand,1270498
Haldaur,India,Uttar Pradesh,1270509
HÄjo,India,Assam,1270522
HÄjÄ«pur,India,Bihar,1270525
HailÄkÄndi,India,Assam,1270530
HÄflong,India,Assam,1270543
HadgÄon,India,Maharashtra,1270554
HÄbra,India,West Bengal,1270568
Gwalior,India,Madhya Pradesh,1270583
Guskhara,India,West Bengal,1270598
GuruvÄyÅ«r,India,Kerala,1270603
Guru Har SahÄi,India,Punjab,1270612
GursarÄi,India,Uttar Pradesh,1270618
GursahÄiganj,India,Uttar Pradesh,1270619
GurmatkÄl,India,Karnataka,1270627
Gurgaon,India,Haryana,1270642
Gunupur,India,Odisha,1270667
GuntÅ«r,India,Andhra Pradesh,1270668
Guntakal Junction,India,Andhra Pradesh,1270670
Gunnaur,India,Uttar Pradesh,1270674
Gundlupet,India,Karnataka,1270686
Guna,India,Madhya Pradesh,1270711
Gummidipundi,India,Tamil Nadu,1270718
Gumla,India,Chhattisgarh,1270722
Gumia,India,Jharkhand,1270723
Guledagudda,India,Karnataka,1270750
Gulbarga,India,Karnataka,1270752
GulÄothi,India,Uttar Pradesh,1270759
GulÄbpura,India,Rajasthan,1270763
GÅ«duvÄncheri,India,Tamil Nadu,1270787
GÅ«dÅ«r,India,Andhra Pradesh,1270791
Gudiyatham,India,Tamil Nadu,1270800
GudivÄda,India,Andhra Pradesh,1270801
Gudalur,India,Tamil Nadu,1270820
Gubbi,India,Karnataka,1270824
GoyerkÄta,India,West Bengal,1270845
Govardhan,India,Uttar Pradesh,1270863
GosÄba,India,West Bengal,1270896
Gorakhpur,India,Haryana,1270926
Gorakhpur,India,Uttar Pradesh,1270927
Gobichettipalayam,India,Tamil Nadu,1270947
GopÄlganj,India,Bihar,1270965
GondiÄ,India,Maharashtra,1270990
Gondal,India,Gujarat,1270994
GondÄ City,India,Uttar Pradesh,1270996
Gomoh,India,Jharkhand,1271005
Gola GokarannÄth,India,Uttar Pradesh,1271049
GolÄghÄt,India,Assam,1271050
Gokarna,India,Karnataka,1271064
Gokak,India,Karnataka,1271067
GohÄna,India,Haryana,1271079
Gohadi,India,Madhya Pradesh,1271083
Godhra,India,Gujarat,1271107
Godda,India,Jharkhand,1271113
Gobindpur,India,Jharkhand,1271131
GobÄrdÄnga,India,West Bengal,1271142
GoÄlpÄra,India,Assam,1271151
GirÄ«dÄ«h,India,Jharkhand,1271175
Gingee,India,Tamil Nadu,1271199
GiddarbÄha,India,Punjab,1271212
GiddalÅ«r,India,Andhra Pradesh,1271213
Ghugus,India,Maharashtra,1271244
Ghoti Budrukh,India,Maharashtra,1271250
GhosÄ«,India,Uttar Pradesh,1271259
GhazÄ«pur,India,Uttar Pradesh,1271306
GhÄziÄbÄd,India,Uttar Pradesh,1271308
GhÄtsÄ«la,India,Jharkhand,1271319
GhÄtanji,India,Maharashtra,1271343
GhÄtampur,India,Uttar Pradesh,1271345
GhÄtÄl,India,West Bengal,1271346
Gharaunda,India,Haryana,1271363
Gevrai,India,Maharashtra,1271413
Gaya,India,Bihar,1271439
Gauripur,India,Assam,1271453
GoribidnÅ«r,India,Karnataka,1271459
Guwahati,India,Assam,1271476
Garhwa,India,Jharkhand,1271493
Garui,India,West Bengal,1271495
Gariadhar,India,Gujarat,1271533
Garhshankar,India,Punjab,1271538
Garhmuktesar,India,Uttar Pradesh,1271543
GarhÄkota,India,Madhya Pradesh,1271563
Gannavaram,India,Andhra Pradesh,1271613
Gangtok,India,Sikkim,1271631
Gangolli,India,Karnataka,1271642
Gangoh,India,Uttar Pradesh,1271644
GangÄwati,India,Karnataka,1271662
GangÄrÄmpur,India,West Bengal,1271670
GangÄpur,India,Rajasthan,1271675
GangÄpur,India,Rajasthan,1271676
GangÄpur,India,Maharashtra,1271680
GangÄnagar,India,Rajasthan,1271685
GangÄkher,India,Maharashtra,1271688
Ghandinagar,India,Gujarat,1271715
GÄndhÄ«dhÄm,India,Gujarat,1271717
Gandevi,India,Gujarat,1271722
GÄndarbal,India,Kashmir,1271729
Gajraula,India,Uttar Pradesh,1271780
Gajendragarh,India,Karnataka,1271789
GadwÄl,India,Telangana,1271819
Gadhinglaj,India,Maharashtra,1271834
Gadhada,India,Gujarat,1271839
GÄdarwÄra,India,Madhya Pradesh,1271847
Gadag,India,Karnataka,1271850
Fort Gloster,India,West Bengal,1271871
Forbesganj,India,Bihar,1271874
FÄ«rozpur Jhirka,India,Haryana,1271881
Ferozepore,India,Punjab,1271883
FÄ«rozÄbÄd,India,Uttar Pradesh,1271885
Ferokh,India,Kerala,1271888
FÄzilka,India,Punjab,1271891
Fatwa,India,Bihar,1271892
Fatehpur SÄ«kri,India,Uttar Pradesh,1271900
Fatehpur,India,Rajasthan,1271910
Fatehpur,India,Uttar Pradesh,1271911
Fatehpur,India,Uttar Pradesh,1271912
Fatehgarh ChÅ«riÄn,India,Punjab,1271923
Fatehganj West,India,Uttar Pradesh,1271929
FatehÄbÄd,India,Haryana,1271934
FatehÄbÄd,India,Uttar Pradesh,1271936
Farrukhnagar,India,Telangana,1271940
FarrukhÄbÄd,India,Uttar Pradesh,1271942
FarÄ«dpur,India,Uttar Pradesh,1271947
FarÄ«dkot,India,Punjab,1271949
FarÄ«dÄbÄd,India,Haryana,1271951
Farakka,India,West Bengal,1271954
FÄlÄkÄta,India,West Bengal,1271965
Faizpur,India,Maharashtra,1271975
FyzÄbÄd,India,Uttar Pradesh,1271976
EtÄwah,India,Uttar Pradesh,1271987
Erraguntla,India,Andhra Pradesh,1272008
Erode,India,Tamil Nadu,1272013
ErÄttupetta,India,Kerala,1272022
Erandol,India,Maharashtra,1272025
EmmiganÅ«r,India,Andhra Pradesh,1272045
Ellore,India,Andhra Pradesh,1272051
ElÅ«r,India,Kerala,1272052
Ellenabad,India,Haryana,1272061
Elamanchili,India,Andhra Pradesh,1272084
Egra,India,West Bengal,1272101
DwÄrka,India,Gujarat,1272140
Durgapur,India,West Bengal,1272175
DurgÄpur,India,Maharashtra,1272177
Durg,India,Chhattisgarh,1272181
DÅ«ngarpur,India,Rajasthan,1272201
Ganj DundwÄra,India,Uttar Pradesh,1272207
Dumraon,India,Bihar,1272225
Dumra,India,Bihar,1272229
Dumka,India,Jharkhand,1272237
Dum Duma,India,Assam,1272242
Dam Dam,India,West Bengal,1272243
DuliÄgaon,India,Assam,1272259
Dugda,India,Jharkhand,1272277
DubrÄjpur,India,West Bengal,1272320
Dornakal,India,Telangana,1272367
DorÄha,India,Punjab,1272375
Dongargarh,India,Chhattisgarh,1272396
Dondaicha,India,Maharashtra,1272411
Dombivli,India,Maharashtra,1272423
Dod BallÄpur,India,Karnataka,1272473
Doda,India,Kashmir,1272476
Diu,India,Daman and Diu,1272502
DÄ«sa,India,Gujarat,1272513
Diphu,India,Assam,1272525
DÄ«nhÄta,India,West Bengal,1272532
Dindori,India,Madhya Pradesh,1272540
Dindigul,India,Tamil Nadu,1272543
DÄ«nÄnagar,India,Punjab,1272546
DimÄpur,India,Nagaland,1272552
Digras,India,Maharashtra,1272596
DÄ«glÅ«r,India,Maharashtra,1272606
DighwÄra,India,Bihar,1272610
Digboi,India,Assam,1272629
DÄ«g,India,Rajasthan,1272639
DÄ«dwÄna,India,Rajasthan,1272640
Dicholi,India,Goa,1272646
Dibrugarh,India,Assam,1272648
Dibai,India,Uttar Pradesh,1272653
Diamond Harbour,India,West Bengal,1272657
DhÅ«ri,India,Punjab,1272670
DhupgÄri,India,West Bengal,1272674
DhuliÄn,India,West Bengal,1272689
DhÅ«lia,India,Maharashtra,1272691
Dhuburi,India,Assam,1272694
Dhrol,India,Gujarat,1272699
DhrÄngadhra,India,Gujarat,1272701
DhorÄji,India,Gujarat,1272720
Dhone,India,Andhra Pradesh,1272722
Dholka,India,Gujarat,1272733
Dhing,India,Assam,1272768
DhenkÄnÄl,India,Odisha,1272780
Dhekiajuli,India,Assam,1272790
Dhaurahra,India,Uttar Pradesh,1272802
Dhaulpur,India,Rajasthan,1272805
DhÄrÅ«r,India,Maharashtra,1272819
DhÄruhera,India,Haryana,1272822
DharmsÄla,India,Himachal Pradesh,1272832
Dharmavaram,India,Andhra Pradesh,1272842
Dharmapuri,India,Tamil Nadu,1272847
Dharmanagar,India,Tripura,1272852
Dharmadam,India,Kerala,1272856
DharmÄbÄd,India,Maharashtra,1272857
DhÄriwÄl,India,Punjab,1272860
DhÄri,India,Gujarat,1272861
Dharapuram,India,Tamil Nadu,1272873
Dharangaon,India,Maharashtra,1272874
Dharampur,India,Gujarat,1272881
DhÄr,India,Madhya Pradesh,1272892
Dhanera,India,Gujarat,1272962
Dhandhuka,India,Gujarat,1272970
DhanbÄd,India,Jharkhand,1272979
Dhanaura,India,Uttar Pradesh,1272983
Dhanaula,India,Punjab,1272985
Dhamtari,India,Chhattisgarh,1272997
DhÄmpur,India,Uttar Pradesh,1273002
DhÄmnod,India,Madhya Pradesh,1273006
DhÄka,India,Bihar,1273043
Dewas,India,Madhya Pradesh,1273066
Deoli,India,Rajasthan,1273083
Devgarh,India,Rajasthan,1273098
Devgadh BÄriya,India,Gujarat,1273104
Devarkonda,India,Telangana,1273109
Devanhalli,India,Karnataka,1273123
Devakottai,India,Tamil Nadu,1273128
DeÅ«lgaon RÄja,India,Maharashtra,1273136
Deshnoke,India,Rajasthan,1273153
DepÄlpur,India,Madhya Pradesh,1273181
Deori KhÄs,India,Madhya Pradesh,1273191
Deoria,India,Uttar Pradesh,1273193
DeoraniÄn,India,Uttar Pradesh,1273206
Deoli,India,Maharashtra,1273228
DeolÄli,India,Maharashtra,1273232
Deogarh,India,Odisha,1273246
Deoband,India,Uttar Pradesh,1273265
Denkanikota,India,Tamil Nadu,1273272
Delhi,India,NCT,1273294
Dehri,India,Bihar,1273309
Dehra DÅ«n,India,Uttarakhand,1273313
Dausa,India,Rajasthan,1273369
Daund,India,Maharashtra,1273374
Daudnagar,India,Bihar,1273390
DattÄpur,India,Maharashtra,1273397
Datia,India,Madhya Pradesh,1273403
DÄtÄganj,India,Uttar Pradesh,1273409
DasÅ«ya,India,Punjab,1273410
DÄsna,India,Uttar Pradesh,1273416
DaryÄpur,India,Maharashtra,1273434
DÄrwha,India,Maharashtra,1273440
DÄrjiling,India,West Bengal,1273467
Darbhanga,India,Bihar,1273491
Dandeli,India,Karnataka,1273574
Dinapore,India,Bihar,1273581
Damoh,India,Madhya Pradesh,1273587
DÄmnagar,India,Gujarat,1273593
Daman,India,Daman and Diu,1273618
Daltonganj,India,Jharkhand,1273626
Dalsingh Sarai,India,Bihar,1273628
Dalkola,India,West Bengal,1273642
DÄkor,India,Gujarat,1273665
Dohad,India,Gujarat,1273687
DahegÄm,India,Gujarat,1273704
DÄhÄnu,India,Maharashtra,1273708
DÄdri,India,Uttar Pradesh,1273724
DabwÄli,India,Haryana,1273745
Dabra,India,Madhya Pradesh,1273751
Daboh,India,Madhya Pradesh,1273756
Dabhoi,India,Gujarat,1273766
Cuttack,India,Odisha,1273780
Curchorem,India,Goa,1273788
Cuncolim,India,Goa,1273793
Cumbum,India,Andhra Pradesh,1273795
Cuddapah,India,Andhra Pradesh,1273800
Cuddalore,India,Tamil Nadu,1273802
Coondapoor,India,Karnataka,1273834
Colonelganj,India,Uttar Pradesh,1273850
Colgong,India,Bihar,1273856
Calangute,India,Goa,1273858
Coimbatore,India,Tamil Nadu,1273865
Cochin,India,Kerala,1273874
Clement Town,India,Uttarakhand,1273880
ChÅ«ru,India,Rajasthan,1273892
ChurÄchÄndpur,India,Manipur,1273909
ChunÄr,India,Uttar Pradesh,1273923
Chotila,India,Gujarat,1273960
Chopda,India,Maharashtra,1273992
Chodavaram,India,Andhra Pradesh,1274020
Rampachodavaram,India,Andhra Pradesh,1274021
ChittÅ«r,India,Kerala,1274032
Chittaurgarh,India,Rajasthan,1274040
Chittaranjan,India,West Bengal,1274043
Chitradurga,India,Karnataka,1274056
ChÄ«tÄpur,India,Karnataka,1274077
Chidawa,India,Rajasthan,1274102
ChÄ«rÄla,India,Andhra Pradesh,1274106
ChÄ«purupalle,India,Andhra Pradesh,1274116
ChiplÅ«n,India,Maharashtra,1274119
ChintÄmani,India,Karnataka,1274129
Chinna Salem,India,Tamil Nadu,1274146
ChinnamanÅ«r,India,Tamil Nadu,1274151
Chincholi,India,Karnataka,1274169
ChillupÄr,India,Uttar Pradesh,1274195
ChilakalÅ«rupet,India,Andhra Pradesh,1274213
Chikodi,India,Karnataka,1274218
ChiknÄyakanhalli,India,Karnataka,1274219
ChikmagalÅ«r,India,Karnataka,1274220
Chikhli,India,Maharashtra,1274237
Chik BallÄpur,India,Karnataka,1274243
Chidambaram,India,Tamil Nadu,1274256
Chicholi,India,Maharashtra,1274265
Chhoti SÄdri,India,Rajasthan,1274284
Chhota Udepur,India,Gujarat,1274285
ChhindwÄra,India,Madhya Pradesh,1274304
ChhibrÄmau,India,Uttar Pradesh,1274315
Chhatarpur,India,Madhya Pradesh,1274337
ChhÄtÄpur,India,Bihar,1274342
ChhÄta,India,Uttar Pradesh,1274343
Chharra,India,Uttar Pradesh,1274346
Chhaprauli,India,Uttar Pradesh,1274351
ChÄpra,India,Bihar,1274353
ChhÄpar,India,Rajasthan,1274359
Chhala,India,Gujarat,1274369
Chhabra,India,Rajasthan,1274381
ChettipÄlaiyam,India,Tamil Nadu,1274389
Chetput,India,Tamil Nadu,1274394
Chennimalai,India,Tamil Nadu,1274422
ChengannÅ«r,India,Kerala,1274428
Chengam,India,Tamil Nadu,1274429
Chengalpattu,India,Tamil Nadu,1274430
ChÄvakkÄd,India,Kerala,1274468
Chaksu,India,Rajasthan,1274532
Chatrapur,India,Odisha,1274533
Chatra,India,Jharkhand,1274536
ChÄs,India,Jharkhand,1274553
CharthÄwal,India,Uttar Pradesh,1274560
Charkhi DÄdri,India,Haryana,1274571
CharkhÄri,India,Uttar Pradesh,1274574
ChÄpar,India,Assam,1274618
ChannarÄyapatna,India,Karnataka,1274640
Channapatna,India,Karnataka,1274641
Channagiri,India,Karnataka,1274642
ChanganÄcheri,India,Kerala,1274664
ChÄndor,India,Maharashtra,1274673
ChÄndÅ«r BÄzÄr,India,Maharashtra,1274674
ChÄndÅ«r,India,Maharashtra,1274675
ChÄndur,India,Maharashtra,1274676
ChÄnda,India,Maharashtra,1274693
Chandrakona,India,West Bengal,1274699
ChÄndpur,India,Uttar Pradesh,1274714
Chandigarh,India,Chandigarh,1274746
Chanderi,India,Madhya Pradesh,1274755
Chanduasi,India,Uttar Pradesh,1274767
Chandauli,India,Uttar Pradesh,1274770
Chandannagar,India,West Bengal,1274784
ChÄnasma,India,Gujarat,1274807
Chamrajnagar,India,Karnataka,1274821
ChÄmpa,India,Chhattisgarh,1274837
Chamba,India,Himachal Pradesh,1274848
Challapalle,India,Andhra Pradesh,1274861
Challakere,India,Karnataka,1274862
ChÄlisgaon,India,Maharashtra,1274868
ChalÄla,India,Gujarat,1274874
Chakradharpur,India,Jharkhand,1274890
ChaklÄsi,India,Gujarat,1274896
ChÄkia,India,Bihar,1274899
ChÄkan,India,Maharashtra,1274914
ChÄÄ«bÄsa,India,Jharkhand,1274928
Canning,India,West Bengal,1274984
Cannanore,India,Kerala,1274987
Kolkata,India,West Bengal,1275004
ByÄdgi,India,Karnataka,1275016
Buxar,India,Bihar,1275019
Burla,India,Odisha,1275050
Burhar,India,Madhya Pradesh,1275066
BurhÄnpur,India,Madhya Pradesh,1275068
BÅ«ndu,India,Jharkhand,1275097
BÅ«ndi,India,Rajasthan,1275103
BuldÄna,India,Maharashtra,1275117
Bulandshahr,India,Uttar Pradesh,1275120
BudhlÄda,India,Punjab,1275147
BudhÄna,India,Uttar Pradesh,1275152
Budaun,India,Uttar Pradesh,1275163
BrÄjarÄjnagar,India,Odisha,1275194
Brahmapur,India,Odisha,1275198
BotÄd,India,Gujarat,1275218
Borsad,India,Gujarat,1275230
Borivli,India,Maharashtra,1275248
Bongaigaon,India,Assam,1275321
Mumbai,India,Maharashtra,1275339
Bolpur,India,West Bengal,1275346
BokÄro,India,Jharkhand,1275362
BokajÄn,India,Assam,1275364
Boisar,India,Maharashtra,1275368
BodinÄyakkanÅ«r,India,Tamil Nadu,1275388
Buddh Gaya,India,Bihar,1275389
Bodhan,India,Telangana,1275391
Bobbili,India,Andhra Pradesh,1275406
BiswÄn,India,Uttar Pradesh,1275435
BissÄu,India,Rajasthan,1275441
Bishnupur,India,West Bengal,1275462
Bisauli,India,Uttar Pradesh,1275476
BÄ«salpur,India,Uttar Pradesh,1275481
BirÅ«r,India,Karnataka,1275488
BÄ«rpur,India,Bihar,1275499
Birmitrapur,India,Odisha,1275506
Binka,India,Odisha,1275558
Bindki,India,Uttar Pradesh,1275572
EtÄwa,India,Madhya Pradesh,1275582
Bilthra,India,Uttar Pradesh,1275589
Bilsi,India,Uttar Pradesh,1275590
Bilsanda,India,Uttar Pradesh,1275593
Bilimora,India,Gujarat,1275610
Bilhaur,India,Uttar Pradesh,1275614
BilgrÄm,India,Uttar Pradesh,1275618
Bilgi,India,Karnataka,1275619
BÄ«lÄspur,India,Uttar Pradesh,1275634
BilÄspur,India,Chhattisgarh,1275637
BilÄsipÄra,India,Assam,1275641
BilÄri,India,Uttar Pradesh,1275646
BilÄra,India,Rajasthan,1275647
Bikramganj,India,Bihar,1275655
BÄ«kaner,India,Rajasthan,1275665
Bijnor,India,Uttar Pradesh,1275679
BijbiÄra,India,Kashmir,1275692
BijÄwar,India,Madhya Pradesh,1275694
Bijapur,India,Karnataka,1275701
BihÄr,India,Bihar,1275716
BihÄrÄ«ganj,India,Bihar,1275719
BidhÅ«na,India,Uttar Pradesh,1275732
BÄ«dar,India,Karnataka,1275738
Biaora,India,Madhya Pradesh,1275762
Bhuvanagiri,India,Tamil Nadu,1275768
BhusÄval,India,Maharashtra,1275778
BhÅ«m,India,Maharashtra,1275804
Bhuj,India,Gujarat,1275812
Bhudgaon,India,Maharashtra,1275814
Bhubaneshwar,India,Odisha,1275817
Bhuban,India,Odisha,1275818
Bhor,India,Maharashtra,1275836
Bhopal,India,Madhya Pradesh,1275841
BhongÄ«r,India,Telangana,1275848
Bhongaon,India,Uttar Pradesh,1275849
Bhogpur,India,Punjab,1275882
BhiwÄni,India,Haryana,1275899
Bhiwandi,India,Maharashtra,1275901
BhitarwÄr,India,Madhya Pradesh,1275905
BhÄ«nmÄl,India,Rajasthan,1275920
Bhinga,India,Uttar Pradesh,1275921
BhindÄr,India,Rajasthan,1275925
Bhind,India,Madhya Pradesh,1275926
BhÄ«munipatnam,India,Andhra Pradesh,1275930
BhÄ«mavaram,India,Andhra Pradesh,1275947
BhÄ«lwÄra,India,Rajasthan,1275960
Bhilai,India,Chhattisgarh,1275971
BhÄ«khi,India,Punjab,1275977
Bhikangaon,India,Madhya Pradesh,1275978
BhÄyÄvadar,India,Gujarat,1276013
Bhayandar,India,Maharashtra,1276014
BhawÄnipatna,India,Odisha,1276023
BhawÄnÄ«garh,India,Punjab,1276026
BhawÄniganj,India,Madhya Pradesh,1276027
BhÄvnagar,India,Gujarat,1276032
BhavÄni,India,Tamil Nadu,1276037
Bhattiprolu,India,Andhra Pradesh,1276054
BhÄtpÄra,India,West Bengal,1276058
Bhatkal,India,Karnataka,1276067
Bhatinda,India,Punjab,1276070
BhÄtÄpÄra,India,Chhattisgarh,1276084
BhasÄwar,India,Rajasthan,1276092
BharwÄri,India,Uttar Pradesh,1276095
BharÅ«ch,India,Gujarat,1276100
Bharthana,India,Uttar Pradesh,1276103
Bharatpur,India,Rajasthan,1276128
BhÄnvad,India,Gujarat,1276147
BhÄnpurÄ«,India,Chhattisgarh,1276151
BhÄnpura,India,Madhya Pradesh,1276152
Bhanjanagar,India,Odisha,1276159
BhÄnder,India,Madhya Pradesh,1276178
BhandÄra,India,Maharashtra,1276191
BhÄlki,India,Karnataka,1276219
Bhaisa,India,Telangana,1276249
Bhainsdehi,India,Madhya Pradesh,1276265
BhÄgalpur,India,Bihar,1276300
Bhadreswar,India,West Bengal,1276320
BhadrÄvati,India,Karnataka,1276321
Bhadrakh,India,Odisha,1276325
BhadrÄchalam,India,Telangana,1276328
BhÄdra,India,Rajasthan,1276330
Bhadohi,India,Uttar Pradesh,1276335
Bhadaur,India,Punjab,1276353
BhÄdÄsar,India,Rajasthan,1276355
BhachÄu,India,Gujarat,1276370
Bhabhua,India,Bihar,1276371
Beypore,India,Kerala,1276378
Bewar,India,Uttar Pradesh,1276381
BetÅ«l,India,Madhya Pradesh,1276389
Bettiah,India,Bihar,1276393
Betamcherla,India,Andhra Pradesh,1276416
Beri KhÄs,India,Haryana,1276437
Berasia,India,Madhya Pradesh,1276449
BeohÄri,India,Madhya Pradesh,1276455
BemetÄra,India,Chhattisgarh,1276478
BelÅ«r,India,Karnataka,1276486
Belsand,India,Bihar,1276495
Belonia,India,Tripura,1276502
Bellary,India,Karnataka,1276509
Belgaum,India,Karnataka,1276533
BeldÄnga,India,West Bengal,1276548
Bela,India,Uttar Pradesh,1276574
Behror,India,Rajasthan,1276589
Behat,India,Uttar Pradesh,1276600
Begusarai,India,Bihar,1276609
BegÅ«n,India,Rajasthan,1276615
Begamganj,India,Madhya Pradesh,1276621
Bedi,India,Gujarat,1276627
BeÄwar,India,Rajasthan,1276634
BÄzpur,India,Uttarakhand,1276642
BayÄna,India,Rajasthan,1276652
BawÄna,India,NCT,1276663
Bauda,India,Odisha,1276686
BatÄla,India,Punjab,1276720
Baswa,India,Rajasthan,1276724
BÄsudebpur,India,Odisha,1276731
BastÄ«,India,Uttar Pradesh,1276736
BÄsoda,India,Madhya Pradesh,1276752
Basni,India,Rajasthan,1276754
Basmat,India,Maharashtra,1276757
Basi,India,Punjab,1276764
Basi,India,Punjab,1276765
Basi,India,Rajasthan,1276767
Basavana BÄgevÄdi,India,Karnataka,1276782
BasavakalyÄn,India,Karnataka,1276783
BarwÄni,India,Madhya Pradesh,1276810
BarwÄla,India,Haryana,1276815
BÄruni,India,Bihar,1276829
BÄruipur,India,West Bengal,1276832
BÄrsi,India,Maharashtra,1276856
Barpeta,India,Assam,1276867
BarpÄli,India,Odisha,1276870
BarnÄla,India,Punjab,1276895
BÄrmer,India,Rajasthan,1276901
Barki Saria,India,Jharkhand,1276919
Barka KÄna,India,Jharkhand,1276927
Barjala,India,Tripura,1276938
Bari SÄdri,India,Rajasthan,1276939
BÄri,India,Rajasthan,1276948
Barhiya,India,Bihar,1276954
BÄrh,India,Bihar,1276977
Bargi,India,Madhya Pradesh,1276982
Bargarh,India,Odisha,1276988
Bareilly,India,Uttar Pradesh,1277013
BÄrdoli,India,Gujarat,1277022
BarddhamÄn,India,West Bengal,1277029
Bar Bigha,India,Bihar,1277038
Baraut,India,Uttar Pradesh,1277044
Barauli,India,Bihar,1277053
BÄrÄsat,India,West Bengal,1277065
BÄrÄsat,India,West Bengal,1277066
Baranagar,India,West Bengal,1277082
BÄrÄn,India,Rajasthan,1277084
BÄramÅ«la,India,Kashmir,1277085
BÄrÄmati,India,Maharashtra,1277091
BÄrÄkpur,India,West Bengal,1277100
BÄpatla,India,Andhra Pradesh,1277183
BanÅ«r,India,Punjab,1277200
BantvÄl,India,Karnataka,1277201
BÄntva,India,Gujarat,1277202
BÄnswÄra,India,Rajasthan,1277214
BÄnswÄda,India,Telangana,1277216
BÄnsi,India,Uttar Pradesh,1277232
BÄnsdÄ«h,India,Uttar Pradesh,1277238
BÄnsbÄria,India,West Bengal,1277240
BannÅ«r,India,Karnataka,1277255
Banmankhi,India,Bihar,1277263
BÄnkura,India,West Bengal,1277264
BÄnki,India,Odisha,1277273
BÄnka,India,Bihar,1277289
BÄngarmau,India,Uttar Pradesh,1277318
BangÄrapet,India,Karnataka,1277320
Bangaon,India,Bihar,1277322
Bangaon,India,West Bengal,1277324
Banganapalle,India,Andhra Pradesh,1277330
Bengaluru,India,Karnataka,1277333
Banga,India,Punjab,1277338
Bandipura,India,Kashmir,1277358
BÄndÄ«kÅ«i,India,Rajasthan,1277362
BÄnda,India,Uttar Pradesh,1277397
Banda,India,Madhya Pradesh,1277398
Banat,India,Uttar Pradesh,1277409
BÄnapur,India,Odisha,1277426
BÄmor KalÄn,India,Madhya Pradesh,1277442
BÄlurghÄt,India,West Bengal,1277508
BÄlugaon,India,Odisha,1277514
BalrÄmpur,India,Uttar Pradesh,1277525
BÄlotra,India,Rajasthan,1277527
Baloda BÄzÄr,India,Chhattisgarh,1277530
Balod,India,Chhattisgarh,1277535
BÄli,India,West Bengal,1277539
BallÄlpur,India,Maharashtra,1277557
BÄli,India,Rajasthan,1277590
Balasore,India,Odisha,1277599
BalarÄmpur,India,West Bengal,1277634
BÄlÄpur,India,Maharashtra,1277636
BalÄngÄ«r,India,Odisha,1277643
BÄlÄghÄt,India,Madhya Pradesh,1277661
BÄlÄchor,India,Punjab,1277666
BakhtiyÄrpur,India,Bihar,1277684
Baj Baj,India,West Bengal,1277723
BairÄgnia,India,Bihar,1277748
Byndoor,India,Karnataka,1277759
Bail-Hongal,India,Karnataka,1277765
Baihar,India,Madhya Pradesh,1277776
BaidyabÄti,India,West Bengal,1277780
Bahraigh,India,Uttar Pradesh,1277799
Bahjoi,India,Uttar Pradesh,1277808
Baheri,India,Uttar Pradesh,1277814
Baharampur,India,West Bengal,1277820
BahÄdurgarh,India,Haryana,1277835
BahÄdurganj,India,Bihar,1277836
BÄh,India,Uttar Pradesh,1277841
BagulÄ,India,West Bengal,1277844
BÄghpat,India,Uttar Pradesh,1277882
BÄghdogra,India,West Bengal,1277897
BÄgha PurÄna,India,Punjab,1277902
BÄgepalli,India,Karnataka,1277909
Bagasra,India,Gujarat,1277924
Bagar,India,Rajasthan,1277930
Bagalkot,India,Karnataka,1277936
Bagaha,India,Bihar,1277939
Bagaha,India,Bihar,1277940
Badvel,India,Andhra Pradesh,1277949
BadÅ«ria,India,West Bengal,1277950
BadnÄwar,India,Madhya Pradesh,1277970
Badlapur,India,Maharashtra,1277976
BÄdÄmi,India,Karnataka,1278017
Badagara,India,Kerala,1278023
Bada BarabÄ«l,India,Odisha,1278026
Bachhraon,India,Uttar Pradesh,1278036
BabrÄla,India,Uttar Pradesh,1278052
BÄbra,India,Gujarat,1278054
BabÄ«na,India,Uttar Pradesh,1278058
Baberu,India,Uttar Pradesh,1278064
BÄbai,India,Madhya Pradesh,1278073
Azamgarh,India,Uttar Pradesh,1278083
Ajodhya,India,Uttar Pradesh,1278094
Ayakudi,India,Tamil Nadu,1278100
Avanigadda,India,Andhra Pradesh,1278122
Avinashi,India,Tamil Nadu,1278124
Ä€vadi,India,Tamil Nadu,1278130
Ausa,India,Maharashtra,1278139
AurangÄbÄd,India,Bihar,1278148
Aurangabad,India,Maharashtra,1278149
Auraiya,India,Uttar Pradesh,1278152
AurÄd,India,Karnataka,1278156
Attur,India,Tamil Nadu,1278173
Attingal,India,Kerala,1278176
Attili,India,Andhra Pradesh,1278178
AtraulÄ«,India,Uttar Pradesh,1278190
AtmakÅ«r,India,Andhra Pradesh,1278201
Adirampattinam,India,Tamil Nadu,1278204
Athni,India,Karnataka,1278208
Ä€thagarh,India,Odisha,1278216
Atarra,India,Uttar Pradesh,1278228
Ä€sind,India,Rajasthan,1278278
Ä€sika,India,Odisha,1278279
AsifÄbÄd,India,Telangana,1278282
Ashta,India,Madhya Pradesh,1278294
Ashta,India,Maharashtra,1278296
Ashoknagar,India,Madhya Pradesh,1278297
Ä€sansol,India,West Bengal,1278314
Ä€sandh,India,Haryana,1278320
Ä€rvi,India,Maharashtra,1278335
Aruppukkottai,India,Tamil Nadu,1278340
Arumuganeri,India,Tamil Nadu,1278343
Arukutti,India,Kerala,1278345
Arsikere,India,Karnataka,1278354
Ä€ron,India,Madhya Pradesh,1278365
ArkalgÅ«d,India,Karnataka,1278393
AriyalÅ«r,India,Tamil Nadu,1278405
Arcot,India,Tamil Nadu,1278432
ArÄria,India,Bihar,1278446
ArantÄngi,India,Tamil Nadu,1278448
Ä€rani,India,Tamil Nadu,1278454
Ä€rangaon,India,Maharashtra,1278455
Arang,India,Chhattisgarh,1278458
ArÄmbÄgh,India,West Bengal,1278466
Arakkonam,India,Tamil Nadu,1278471
Arrah,India,Bihar,1278483
Aonla,India,Uttar Pradesh,1278498
AnÅ«pshahr,India,Uttar Pradesh,1278507
AnÅ«ppur,India,Madhya Pradesh,1278508
AnÅ«pgarh,India,Rajasthan,1278510
Anta,India,Rajasthan,1278532
Anshing,India,Maharashtra,1278534
Annur,India,Tamil Nadu,1278539
Annigeri,India,Karnataka,1278540
Ankleshwar,India,Gujarat,1278553
AnjÄr,India,Gujarat,1278573
Anjangaon,India,Maharashtra,1278580
Anjad,India,Madhya Pradesh,1278588
Angul,India,Odisha,1278593
AngamÄli,India,Kerala,1278602
Anekal,India,Karnataka,1278609
Andol,India,Telangana,1278621
Anthiyur,India,Tamil Nadu,1278622
Ä€ndippatti,India,Tamil Nadu,1278625
Anantnag,India,Kashmir,1278667
Anantapur,India,Andhra Pradesh,1278672
Anandpur,India,Punjab,1278676
Ä€nand,India,Gujarat,1278685
AnakÄpalle,India,Andhra Pradesh,1278688
Anaimalai,India,Tamil Nadu,1278692
AmudÄlavalasa,India,Andhra Pradesh,1278698
Ä€mta,India,West Bengal,1278703
Amroli,India,Gujarat,1278707
Amroha,India,Uttar Pradesh,1278708
Amritsar,India,Punjab,1278710
Amreli,India,Gujarat,1278715
AmrÄvati,India,Maharashtra,1278718
Amod,India,Gujarat,1278742
Ä€mli,India,Dadra and Nagar Haveli,1278768
Ä€mlÄgora,India,West Bengal,1278774
Amla,India,Madhya Pradesh,1278775
Amet,India,Rajasthan,1278808
Ambur,India,Tamil Nadu,1278815
AmbikÄpur,India,Chhattisgarh,1278827
AmbattÅ«r,India,Tamil Nadu,1278840
Ambasamudram,India,Tamil Nadu,1278841
AmbÄla,India,Haryana,1278860
AmbÄjogÄi,India,Maharashtra,1278862
AmbÄh,India,Madhya Pradesh,1278868
Ambad,India,Maharashtra,1278871
Amarpur,India,Bihar,1278895
AmarpÄtan,India,Madhya Pradesh,1278899
AmarnÄth,India,Maharashtra,1278903
Amalner,India,Maharashtra,1278931
AmalÄpuram,India,Andhra Pradesh,1278935
Aluva,India,Kerala,1278941
Alwar,India,Rajasthan,1278946
Alot,India,Madhya Pradesh,1278964
Along,India,Arunachal Pradesh,1278969
AlnÄvar,India,Karnataka,1278973
Almora,India,Uttarakhand,1278974
Alleppey,India,Kerala,1278985
AllahÄbÄd,India,Uttar Pradesh,1278994
AlÄ«pur,India,NCT,1279005
AlÄ«garh,India,Uttar Pradesh,1279017
AlÄ«ganj,India,Uttar Pradesh,1279023
AlÄ«bÄg,India,Maharashtra,1279027
Ä€langulam,India,Tamil Nadu,1279058
Ä€langÄyam,India,Tamil Nadu,1279061
Alandur,India,Tamil Nadu,1279064
Alandi,India,Maharashtra,1279066
Aland,India,Karnataka,1279068
Akot,India,Maharashtra,1279094
Akola,India,Maharashtra,1279105
Aklera,India,Rajasthan,1279115
AkivÄ«du,India,Andhra Pradesh,1279123
Akbarpur,India,Uttar Pradesh,1279134
Akbarpur,India,Uttar Pradesh,1279135
Akaltara,India,Chhattisgarh,1279144
Akalkot,India,Maharashtra,1279147
Ajra,India,Maharashtra,1279154
AjnÄla,India,Punjab,1279158
Ajmer,India,Rajasthan,1279159
Aizawl,India,Mizoram,1279186
Ahraura,India,Uttar Pradesh,1279219
Ahmadpur,India,Maharashtra,1279227
Ahmadnagar,India,Maharashtra,1279228
Ahmedabad,India,Gujarat,1279233
Ä€gra,India,Uttar Pradesh,1279259
Agartala,India,Tripura,1279290
Agar,India,Madhya Pradesh,1279299
Afzalpur,India,Karnataka,1279306
Afzalgarh,India,Uttar Pradesh,1279307
AdÅ«r,India,Kerala,1279323
Adra,India,West Bengal,1279334
Ä€doni,India,Andhra Pradesh,1279335
Ä€dilÄbÄd,India,Telangana,1279344
Addanki,India,Andhra Pradesh,1279356
Achhnera,India,Uttar Pradesh,1279382
Achalpur,India,Maharashtra,1279390
Ä€bu Road,India,Rajasthan,1279394
Ä€bu,India,Rajasthan,1279396
Abohar,India,Punjab,1279403
AbhayÄpuri,India,Assam,1279407
Contai,India,West Bengal,1344069
Haldia,India,West Bengal,1344377
SrirÄmpur,India,West Bengal,1348562
Dumjor,India,West Bengal,1348739
Bankra,India,West Bengal,1348747
Chakapara,India,West Bengal,1348753
Mahiari,India,West Bengal,1348775
Dhulagari,India,West Bengal,1348780
PÄnchla,India,West Bengal,1348785
Nangi,India,West Bengal,1348818
Pujali,India,West Bengal,1348820
Monoharpur,India,West Bengal,1349041
NabagrÄm,India,West Bengal,1349357
SoyÄ«bug,India,Kashmir,1430991
SingÄpur,India,Telangana,1445156
Ghatkesar,India,Telangana,1445378
Vijayapura,India,Karnataka,1462711
Ä€dampur,India,Punjab,1462733
Porur,India,Tamil Nadu,1465622
Madipakkam,India,Tamil Nadu,1465825
Perungudi,India,Tamil Nadu,1465828
Madambakkam,India,Tamil Nadu,1465910
Powai,India,Maharashtra,6324621
Navi Mumbai,India,Maharashtra,6619347
Murudeshwara,India,Karnataka,6941937
Shivaji Nagar,India,Maharashtra,6943660
Greater Noida,India,Uttar Pradesh,6954929
Mohali,India,Punjab,6992326
Pithampur,India,Madhya Pradesh,7279595
Barbil,India,Odisha,7279597
Airoli,India,Maharashtra,7279599
Aluva,India,Kerala,7279600
Kotkapura,India,Punjab,7279734
Muvattupuzha,India,Kerala,7279735
Perumbavoor,India,Kerala,7279739
Vapi,India,Gujarat,7279741
Baddi,India,Himachal Pradesh,7279742
Noida,India,Uttar Pradesh,7279746
Bhiwadi,India,Rajasthan,7279747
Mandideep,India,Madhya Pradesh,7279752
Singrauli,India,Madhya Pradesh,7279754
Birpara,India,West Bengal,7284803
Jaigaon,India,West Bengal,7284820
Akkarampalle,India,Andhra Pradesh,7302805
Bellampalli,India,Telangana,7302806
Chemmumiahpet,India,Andhra Pradesh,7302808
Gaddi Annaram,India,Telangana,7302810
Dasnapur,India,Telangana,7302812
Kanuru,India,Andhra Pradesh,7302825
Lal Bahadur Nagar,India,Telangana,7302826
Malkajgiri,India,Telangana,7302828
Mandamarri,India,Telangana,7302829
Chinnachowk,India,Andhra Pradesh,7302830
Kyathampalle,India,Telangana,7302832
Gajuwaka,India,Andhra Pradesh,7302833
Manuguru,India,Telangana,7302836
Kalyandurg,India,Andhra Pradesh,7302838
Ponnur,India,Andhra Pradesh,7302844
Quthbullapur,India,Telangana,7302845
Ramanayyapeta,India,Andhra Pradesh,7302846
Palwancha,India,Telangana,7302847
Barpeta Road,India,Assam,7302849
Sathupalli,India,Telangana,7302851
Yanamalakuduru,India,Andhra Pradesh,7302853
Marigaon,India,Assam,7302854
Naharlagun,India,Arunachal Pradesh,7302855
Serilingampalle,India,Telangana,7302856
Silapathar,India,Assam,7302857
Lumding Railway Colony,India,Assam,7302859
Aistala,India,West Bengal,7302860
Ashoknagar Kalyangarh,India,West Bengal,7302861
Bahula,India,West Bengal,7302862
Bhawanipur,India,Bihar,7626554
Zira,India,Punjab,7645176
Ramagundam,India,Telangana,8347656
Cherpulassery,India,Kerala,8504418
Kirandul,India,Chhattisgarh,8581647
Shiraguppi,India,Maharashtra,8714565
V.S.K.Valasai (Dindigul-Dist.),India,Tamil Nadu,8948694
Neelankarai,India,Tamil Nadu,9212568
Injambakkam,India,Tamil Nadu,9212569
Kultali,India,West Bengal,9781227
Shahbazpur,India,Bihar,9794300
Kumbalam,India,Kerala,10627510
Aroor,India,Kerala,10628607
Kadakkavoor,India,Kerala,10628608
Kalavoor,India,Kerala,10629189
Kalamassery,India,Kerala,10630431
Cherthala,India,Kerala,10792588
Zaxo,Iraq,DahÅ«k,89570
Umm QaÅŸr,Iraq,Basra Governorate,89824
Tozkhurmato,Iraq,Salah ad Din Governorate,90026
TikrÄ«t,Iraq,Salah ad Din Governorate,90150
Tallkayf,Iraq,NÄ«nawÃ¡,90353
SÄ«nah,Iraq,DahÅ«k,90708
SÄmarrÄâ€™,Iraq,Salah ad Din Governorate,91597
NÄá¸©Ä«yat Saddat al HindÄ«yah,Iraq,BÄbil,91812
RuwÄndiz,Iraq,ArbÄ«l,92002
RÄwah,Iraq,Anbar,92004
Al-Hamdaniya,Iraq,NÄ«nawÃ¡,92430
MandalÄ«,Iraq,DiyÄlÃ¡,93709
Koysinceq,Iraq,ArbÄ«l,94220
KifrÄ«,Iraq,DiyÄlÃ¡,94298
Kirkuk,Iraq,At TaÊ¼mÄ«m,94787
Karbala,Iraq,KarbalÄÊ¼,94824
Erbil,Iraq,ArbÄ«l,95446
HÄ«t,Iraq,Anbar,95788
á¸¨alabjah,Iraq,As SulaymÄnÄ«yah,96205
á¸¨adÄ«thah,Iraq,Anbar,96309
Dihok,Iraq,DahÅ«k,96994
JamjamÄl,Iraq,As SulaymÄnÄ«yah,97417
BayjÄ«,Iraq,Salah ad Din Governorate,97783
Baqubah,Iraq,DiyÄlÃ¡,97990
Baynjiwayn,Iraq,As SulaymÄnÄ«yah,98012
Balad,Iraq,Salah ad Din Governorate,98112
Baghdad,Iraq,Mayorality of Baghdad,98182
Az Zubayr,Iraq,Basra Governorate,98245
AÅŸ Åžuwayrah,Iraq,WÄsiÅ£,98459
As SulaymÄnÄ«yah,Iraq,As SulaymÄnÄ«yah,98463
As Samawah,Iraq,Al MuthannÃ¡,98530
NÄá¸©iyat ash ShinÄfÄ«yah,Iraq,Al QÄdisÄ«yah,98589
Ash ShaÅ£rah,Iraq,Dhi Qar,98622
Ash ShÄmÄ«yah,Iraq,Al QÄdisÄ«yah,98629
Ar RuÅ£bah,Iraq,Anbar,98677
Ar Rumaythah,Iraq,Al MuthannÃ¡,98685
Ramadi,Iraq,Anbar,98717
â€˜Aqrah,Iraq,NÄ«nawÃ¡,98822
An NÄÅŸirÄ«yah,Iraq,Dhi Qar,98854
Najaf,Iraq,An Najaf,98860
â€˜Anat al QadÄ«mah,Iraq,Anbar,98885
Imam Qasim,Iraq,BÄbil,99010
Al Musayyib,Iraq,BÄbil,99039
Al MishkhÄb,Iraq,An Najaf,99060
Al MiqdÄdÄ«yah,Iraq,DiyÄlÃ¡,99062
Al MawÅŸil al JadÄ«dah,Iraq,NÄ«nawÃ¡,99071
Mosul,Iraq,NÄ«nawÃ¡,99072
Al KÅ«t,Iraq,WÄsiÅ£,99131
Kufa,Iraq,An Najaf,99135
KhÄliÅŸ,Iraq,DiyÄlÃ¡,99169
â€˜AlÄ« al GharbÄ«,Iraq,Maysan,99306
Al HindÄ«yah,Iraq,KarbalÄÊ¼,99344
Al á¸¨illah,Iraq,BÄbil,99347
Al á¸¨ayy,Iraq,WÄsiÅ£,99350
Al HÄrithah,Iraq,Basra Governorate,99369
Nahiyat Ghammas,Iraq,Al QÄdisÄ«yah,99434
NÄá¸©iyat al FuhÅ«d,Iraq,Dhi Qar,99439
Al FÄw,Iraq,Basra Governorate,99446
Al FallÅ«jah,Iraq,Anbar,99454
Basrah,Iraq,Basra Governorate,99532
Al â€˜AzÄ«zÄ«yah,Iraq,WÄsiÅ£,99548
Al â€˜AmÄrah,Iraq,Maysan,99608
â€˜Afak,Iraq,Al QÄdisÄ«yah,99738
Ad Dujayl,Iraq,Salah ad Din Governorate,99759
Ad DÄ«wÄnÄ«yah,Iraq,Al QÄdisÄ«yah,99762
AbÅ« Ghurayb,Iraq,Mayorality of Baghdad,100077
Al BaÅŸrah al QadÄ«mah,Iraq,Basra Governorate,388349
SinjÄr,Iraq,NÄ«nawÃ¡,448149
Ä€zÄdshahr,Iran,HamadÄn,14256
KahrÄ«z,Iran,KermÄnshÄh,23814
NÅ«rÄbÄd,Iran,LorestÄn,24851
ÄªstgÄh-e RÄh Ä€han-e GarmsÄr,Iran,SemnÄn,32723
Qarchak,Iran,TehrÄn,32767
Shahre Jadide Andisheh,Iran,TehrÄn,32909
Khorramdarreh,Iran,Zanjan,41210
Yasuj,Iran,KohgÄ«lÅ«yeh va BÅ«yer Aá¸©mad,66093
Ä€zÄdshahr,Iran,GolestÄn,110831
Zarand,Iran,Kerman,111421
ZanjÄn,Iran,Zanjan,111453
Yazd,Iran,Yazd,111822
VarÄmÄ«n,Iran,TehrÄn,112214
Torbat-e á¸¨eydarÄ«yeh,Iran,Razavi Khorasan,112646
TonekÄbon,Iran,MÄzandarÄn,112656
Tehran,Iran,TehrÄn,112931
Hashtpar,Iran,GÄ«lÄn,113343
TÄkestÄn,Iran,QazvÄ«n,113491
TakÄb,Iran,Ä€zÌ„ÄrbÄyjÄn-e GharbÄ«,113508
Taft,Iran,Yazd,113632
Tabriz,Iran,East Azerbaijan,113646
Tabas,Iran,Yazd,113659
Sonqor,Iran,KermÄnshÄh,114049
Sirjan,Iran,Kerman,114259
ShÅ«shtar,Iran,Khuzestan,114584
ShÅ«sh,Iran,Khuzestan,114593
ShÄ«rvÄn,Iran,KhorÄsÄn-e ShomÄlÄ«,114930
Shiraz,Iran,Fars,115019
Shahr-e Kord,Iran,ChahÄr Maá¸©Äll va BakhtÄ«ÄrÄ«,115770
Shahr-e BÄbak,Iran,Kerman,115781
ShÄdegÄn,Iran,Khuzestan,116102
SemnÄn,Iran,SemnÄn,116402
SemÄ«rom,Iran,Isfahan,116406
SÄveh,Iran,Markazi,116667
Sari,Iran,MÄzandarÄn,116996
Saqqez,Iran,KordestÄn,117392
Sanandaj,Iran,KordestÄn,117574
SalmÄs,Iran,Ä€zÌ„ÄrbÄyjÄn-e GharbÄ«,117656
ShÄhÄ«n Dezh,Iran,Ä€zÌ„ÄrbÄyjÄn-e GharbÄ«,117793
Sabzevar,Iran,Razavi Khorasan,118063
RÅ«dsar,Iran,GÄ«lÄn,118191
RobÄÅ£ KarÄ«m,Iran,TehrÄn,118367
RÄvar,Iran,Kerman,118704
Rasht,Iran,GÄ«lÄn,118743
RÄmshÄ«r,Iran,Khuzestan,118805
RÄmhormoz,Iran,Khuzestan,118826
RafsanjÄn,Iran,Kerman,118994
QÅ«chÄn,Iran,Razavi Khorasan,119115
Qorveh,Iran,KordestÄn,119161
Qom,Iran,Qom,119208
Qeshm,Iran,Hormozgan,119374
Qazvin,Iran,QazvÄ«n,119505
Qarah áº”Ä«Äâ€™ od DÄ«n,Iran,Ä€zÌ„ÄrbÄyjÄn-e GharbÄ«,119730
Farrokh Shahr,Iran,ChahÄr Maá¸©Äll va BakhtÄ«ÄrÄ«,120678
QÄâ€™en,Iran,KhorÄsÄn-e JonÅ«bÄ«,120694
Sarpol-e ZÌ„ahÄb,Iran,KermÄnshÄh,120931
PÄ«shvÄ,Iran,TehrÄn,120972
Piranshahr,Iran,Ä€zÌ„ÄrbÄyjÄn-e GharbÄ«,121110
PÄveh,Iran,KermÄnshÄh,121240
PÄrsÄbÄd,Iran,ArdabÄ«l,121380
OshnavÄ«yeh,Iran,Ä€zÌ„ÄrbÄyjÄn-e GharbÄ«,121795
OrÅ«mÄ«yeh,Iran,Ä€zÌ„ÄrbÄyjÄn-e GharbÄ«,121801
OmÄ«dÄ«yeh,Iran,Khuzestan,121861
NÅ«rÄbÄd,Iran,Fars,121925
Nowshahr,Iran,MÄzandarÄn,121959
NÄ«shÄbÅ«r,Iran,Razavi Khorasan,122285
NeyrÄ«z,Iran,Fars,122289
NekÄ,Iran,MÄzandarÄn,122397
NazÌ§arÄbÄd,Iran,Alborz,122438
Naqadeh,Iran,Ä€zÌ„ÄrbÄyjÄn-e GharbÄ«,122698
NahÄvand,Iran,HamadÄn,122915
MÄ«nÄb,Iran,Hormozgan,123941
MÄ«ÄndoÄb,Iran,Ä€zÌ„ÄrbÄyjÄn-e GharbÄ«,124085
Meybod,Iran,Yazd,124193
MahrÄ«z,Iran,Yazd,124274
Masjed SoleymÄn,Iran,Khuzestan,124620
BardsÄ«r,Iran,Kerman,124647
Mashhad,Iran,Razavi Khorasan,124665
Marand,Iran,East Azerbaijan,124862
MalÄyer,Iran,HamadÄn,125185
MalÄrd,Iran,TehrÄn,125188
MahÄbÄd,Iran,Ä€zÌ„ÄrbÄyjÄn-e GharbÄ«,125446
LangarÅ«d,Iran,GÄ«lÄn,125897
KÅ«hdasht,Iran,LorestÄn,126409
KÄ«sh,Iran,Hormozgan,126914
Khvoy,Iran,Ä€zÌ„ÄrbÄyjÄn-e GharbÄ«,126972
KhvÄnsÄr,Iran,Isfahan,127033
Khorramshahr,Iran,Khuzestan,127319
Khorramabad,Iran,LorestÄn,127349
Khomeyn,Iran,Markazi,127403
KhalkhÄl,Iran,ArdabÄ«l,128008
KermÄnshÄh,Iran,KermÄnshÄh,128226
Kerman,Iran,Kerman,128234
KÄzerÅ«n,Iran,Fars,128321
KÄshmar,Iran,Razavi Khorasan,128447
KÄshÄn,Iran,Isfahan,128477
Karaj,Iran,Alborz,128747
KangÄvar,Iran,KermÄnshÄh,128831
KÄmyÄrÄn,Iran,KordestÄn,128905
KalÄleh,Iran,GolestÄn,129512
JÅ«ybÄr,Iran,MÄzandarÄn,129933
JavÄnrÅ«d,Iran,KermÄnshÄh,130245
ÄªlÄm,Iran,ÄªlÄm,130802
HarsÄ«n,Iran,KermÄnshÄh,131962
HamadÄn,Iran,HamadÄn,132144
GorgÄn,Iran,GolestÄn,132892
Gonbad-e KÄvÅ«s,Iran,GolestÄn,132938
GonÄbÄd,Iran,Razavi Khorasan,132961
GolpÄyegÄn,Iran,Isfahan,133037
GerÄsh,Iran,Fars,133595
Bandar-e GanÄveh,Iran,Bushehr,134217
FÅ«man,Iran,GÄ«lÄn,134441
FÄ«rÅ«zÄbÄd,Iran,Fars,134518
FereydÅ«nkenÄr,Iran,MÄzandarÄn,134602
FasÄ,Iran,Fars,134721
FÄrsÄn,Iran,ChahÄr Maá¸©Äll va BakhtÄ«ÄrÄ«,134762
EsfarÄyen,Iran,KhorÄsÄn-e ShomÄlÄ«,135298
Shahrud,Iran,SemnÄn,135423
Dogonbadan,Iran,KohgÄ«lÅ«yeh va BÅ«yer Aá¸©mad,136014
DelÄ«jÄn,Iran,Markazi,136399
DehlorÄn,Iran,ÄªlÄm,136702
Dehdasht,Iran,KohgÄ«lÅ«yeh va BÅ«yer Aá¸©mad,136987
SÅ«sangerd,Iran,Khuzestan,137268
Darreh Shahr,Iran,ÄªlÄm,137436
DÄrÄb,Iran,Fars,137956
DÄmghÄn,Iran,SemnÄn,138025
DamÄvand,Iran,TehrÄn,138042
ChenÄrÄn,Iran,Razavi Khorasan,138742
ChÄlÅ«s,Iran,MÄzandarÄn,139223
Bandar-e BÅ«shehr,Iran,Bushehr,139817
BÅ«kÄn,Iran,Ä€zÌ„ÄrbÄyjÄn-e GharbÄ«,139889
BorÅ«jerd,Iran,LorestÄn,140044
BorÅ«jen,Iran,ChahÄr Maá¸©Äll va BakhtÄ«ÄrÄ«,140046
BorÄzjÄn,Iran,Bushehr,140097
BojnÅ«rd,Iran,KhorÄsÄn-e ShomÄlÄ«,140380
BÄ«rjand,Iran,KhorÄsÄn-e JonÅ«bÄ«,140463
BÄ«jÄr,Iran,KordestÄn,140521
BonÄb,Iran,East Azerbaijan,140889
Behshahr,Iran,MÄzandarÄn,140918
BehbahÄn,Iran,Khuzestan,140951
BÄneh,Iran,KordestÄn,141584
Bandar-e Lengeh,Iran,Hormozgan,141665
Bandar-e AnzalÄ«,Iran,GÄ«lÄn,141679
Bandar â€˜AbbÄs,Iran,Hormozgan,141681
Bam,Iran,Kerman,141736
BahÄr,Iran,HamadÄn,142000
BÄfq,Iran,Yazd,142255
BÄbolsar,Iran,MÄzandarÄn,142358
BÄbol,Iran,MÄzandarÄn,142363
AznÄ,Iran,LorestÄn,142496
HashtrÅ«d,Iran,East Azerbaijan,142554
Ä€stÄrÄ,Iran,GÄ«lÄn,142676
Ä€stÄneh-ye AshrafÄ«yeh,Iran,GÄ«lÄn,142679
AsadÄbÄd,Iran,HamadÄn,142872
ArdestÄn,Iran,Isfahan,143052
ArdakÄn,Iran,Yazd,143073
ArdabÄ«l,Iran,ArdabÄ«l,143083
ArÄk,Iran,Markazi,143127
Ä€mol,Iran,MÄzandarÄn,143534
Alvand,Iran,Zanjan,143748
ShahrÄ«Är,Iran,TehrÄn,143860
AlÄ«gÅ«darz,Iran,LorestÄn,143921
Aleshtar,Iran,LorestÄn,144269
AkbarÄbÄd,Iran,Fars,144410
â€˜Ajab ShÄ«r,Iran,East Azerbaijan,144443
Ahvaz,Iran,Khuzestan,144448
Ahar,Iran,East Azerbaijan,144616
Aghajari,Iran,Khuzestan,144696
Ä€byek,Iran,Markazi,144794
Abhar,Iran,Zanjan,145034
Ä€bdÄnÄn,Iran,ÄªlÄm,145233
Ä€bÄdeh,Iran,Fars,145449
Abadan,Iran,Khuzestan,145459
EqbÄlÄ«yeh,Iran,TehrÄn,406993
ShÄhreáº•Ä,Iran,Isfahan,417594
RehnÄn,Iran,Isfahan,418521
QahderÄ«jÄn,Iran,Isfahan,418571
NajafÄbÄd,Iran,Isfahan,418606
KhomeynÄ« Shahr,Iran,Isfahan,418710
KelÄ«shÄd va SÅ«darjÄn,Iran,Isfahan,418723
FalÄvarjÄn,Iran,Isfahan,418851
Isfahan,Iran,Isfahan,418863
DowlatÄbÄd,Iran,Isfahan,418868
Dorcheh PÄ«Äz,Iran,Isfahan,418896
ZÄbol,Iran,Sistan and Baluchestan,1113217
Zahedan,Iran,Sistan and Baluchestan,1159301
Torbat-e JÄm,Iran,Razavi Khorasan,1159362
TÄybÄd,Iran,Razavi Khorasan,1159384
Sarakhs,Iran,Razavi Khorasan,1159716
QaÅŸr-e Qand,Iran,Sistan and Baluchestan,1159877
KhÄsh,Iran,Sistan and Baluchestan,1160571
ÄªrÄnshahr,Iran,Sistan and Baluchestan,1160939
Chabahar,Iran,Sistan and Baluchestan,1161724
Mahdishahr,Iran,SemnÄn,7100777
Pasragad Branch,Iran,HamadÄn,10630176
Akureyri,Iceland,Northeast,2633274
ReykjavÃ­k,Iceland,Capital Region,3413829
KÃ³pavogur,Iceland,Capital Region,3415212
HafnarfjÃ¶rÃ°ur,Iceland,Capital Region,3416706
Vittoria,Italy,Sicily,2522713
Villabate,Italy,Sicily,2522767
Vibo Valentia,Italy,Calabria,2522776
Trapani,Italy,Sicily,2522876
Termini Imerese,Italy,Sicily,2522960
Siracusa,Italy,Sicily,2523083
Sinnai,Italy,Sardinia,2523087
Siderno,Italy,Calabria,2523113
Sestu,Italy,Sardinia,2523136
Selargius,Italy,Sardinia,2523166
Scordia,Italy,Sicily,2523180
Scicli,Italy,Sicily,2523192
Sciacca,Italy,Sicily,2523194
San Giovanni la Punta,Italy,Sicily,2523460
San Giovanni in Fiore,Italy,Calabria,2523461
San Cataldo,Italy,Sicily,2523513
Rossano Stazione,Italy,Calabria,2523577
Rosolini,Italy,Sicily,2523581
Ribera,Italy,Sicily,2523619
Reggio Calabria,Italy,Calabria,2523630
Ragusa,Italy,Sicily,2523650
Quattromiglia,Italy,Calabria,2523664
Quartu Sant'Elena,Italy,Sardinia,2523665
Pozzallo,Italy,Sicily,2523693
Porto Empedocle,Italy,Sicily,2523705
Piazza Armerina,Italy,Sicily,2523796
PaternÃ²,Italy,Sicily,2523866
Partinico,Italy,Sicily,2523871
Palmi,Italy,Calabria,2523902
Palma di Montechiaro,Italy,Sicily,2523908
Palermo,Italy,Sicily,2523920
Palagonia,Italy,Sicily,2523927
Pachino,Italy,Sicily,2523938
Oristano,Italy,Sardinia,2523964
Noto,Italy,Sicily,2523998
Niscemi,Italy,Sicily,2524006
Nicastro-Sambiase,Italy,Calabria,2524013
Monserrato,Italy,Sardinia,2524084
Monreale,Italy,Sicily,2524085
Modica,Italy,Sicily,2524119
Misterbianco,Italy,Sicily,2524123
Misilmeri,Italy,Sicily,2524126
Milazzo,Italy,Sicily,2524155
Messina,Italy,Sicily,2524170
Mazara del Vallo,Italy,Sicily,2524205
Mascalucia,Italy,Sicily,2524236
Marsala,Italy,Sicily,2524245
Licata,Italy,Sicily,2524393
Lentini,Italy,Sicily,2524410
Iglesias,Italy,Sardinia,2524533
Gioia Tauro,Italy,Calabria,2524606
Giarre,Italy,Sicily,2524618
Gela,Italy,Sicily,2524653
Floridia,Italy,Sicily,2524734
Favara,Italy,Sicily,2524786
Enna,Italy,Sicily,2524819
Crotone,Italy,Calabria,2524881
Cosenza,Italy,Calabria,2524907
Comiso,Italy,Sicily,2524955
Catanzaro,Italy,Calabria,2525059
Catania,Italy,Sicily,2525068
Castrovillari,Italy,Calabria,2525070
Castelvetrano,Italy,Sicily,2525083
Casarano,Italy,Apulia,2525207
Carini,Italy,Sicily,2525350
Carbonia,Italy,Sardinia,2525362
CanicattÃ¬,Italy,Sicily,2525405
Caltanissetta,Italy,Sicily,2525448
Caltagirone,Italy,Sicily,2525450
Cagliari,Italy,Sardinia,2525473
Bronte,Italy,Sicily,2525498
Biancavilla,Italy,Sicily,2525560
Belpasso,Italy,Sicily,2525571
Barcellona Pozzo di Gotto,Italy,Sicily,2525597
Bagheria,Italy,Sicily,2525628
Avola,Italy,Sicily,2525643
Augusta,Italy,Sicily,2525646
Assemini,Italy,Sardinia,2525655
Amato,Italy,Calabria,2525725
Alcamo,Italy,Sicily,2525755
Agrigento,Italy,Sicily,2525764
Adrano,Italy,Sicily,2525769
Acireale,Italy,Sicily,2525790
Aci Catena,Italy,Sicily,2525791
Aci Castello,Italy,Sicily,2525792
Zola Predosa,Italy,Emilia-Romagna,3163853
Voghera,Italy,Lombardy,3163995
Vittorio Veneto,Italy,Veneto,3164028
Viterbo,Italy,Latium,3164039
Vimodrone,Italy,Lombardy,3164080
Vimercate,Italy,Lombardy,3164083
Lancenigo-Villorba,Italy,Veneto,3164090
Villaricca,Italy,Campania,3164153
Villafranca di Verona,Italy,Veneto,3164241
Vignola,Italy,Emilia-Romagna,3164342
Vigevano,Italy,Lombardy,3164376
Vicenza,Italy,Veneto,3164419
Viareggio,Italy,Tuscany,3164433
Verona,Italy,Veneto,3164527
Vercelli,Italy,Piedmont,3164565
Ventimiglia,Italy,Liguria,3164582
Venice,Italy,Veneto,3164603
Venaria Reale,Italy,Piedmont,3164617
Velletri,Italy,Latium,3164630
Vasto,Italy,Abruzzo,3164672
Varese,Italy,Lombardy,3164699
Valenzano,Italy,Apulia,3164919
Valenza,Italy,Piedmont,3164920
Valdagno,Italy,Veneto,3164954
Udine,Italy,Friuli Venezia Giulia,3165072
Triggiano,Italy,Apulia,3165178
Trieste,Italy,Friuli Venezia Giulia,3165185
Trezzano sul Naviglio,Italy,Lombardy,3165198
Treviso,Italy,Veneto,3165201
Treviglio,Italy,Lombardy,3165207
Trentola-Ducenta,Italy,Campania,3165240
Trento,Italy,Trentino-Alto Adige,3165243
Trecate,Italy,Piedmont,3165275
Trani,Italy,Apulia,3165322
Tradate,Italy,Lombardy,3165340
Tortona,Italy,Piedmont,3165370
Torremaggiore,Italy,Apulia,3165435
Torre del Greco,Italy,Campania,3165456
Torre Annunziata,Italy,Campania,3165475
Turin,Italy,Piedmont,3165524
Tolentino,Italy,The Marches,3165595
Tivoli,Italy,Latium,3165624
Thiene,Italy,Veneto,3165698
Terzigno,Italy,Campania,3165737
Terracina,Italy,Latium,3165762
Terni,Italy,Umbria,3165771
Termoli,Italy,Molise,3165773
Terlizzi,Italy,Apulia,3165788
Teramo,Italy,Abruzzo,3165803
Taranto,Italy,Apulia,3165926
Suzzara,Italy,Lombardy,3166006
Sulmona,Italy,Abruzzo,3166034
Spoleto,Italy,Umbria,3166236
Sora,Italy,Latium,3166387
Sondrio,Italy,Lombardy,3166397
Somma Vesuviana,Italy,Campania,3166404
Siena,Italy,Tuscany,3166548
Sezze,Italy,Latium,3166571
Seveso,Italy,Lombardy,3166574
Settimo Torinese,Italy,Piedmont,3166576
Sestri Levante,Italy,Liguria,3166595
Sesto San Giovanni,Italy,Lombardy,3166598
Sesto Fiorentino,Italy,Tuscany,3166601
Seriate,Italy,Lombardy,3166706
Seregno,Italy,Lombardy,3166711
Senigallia,Italy,The Marches,3166740
Senago,Italy,Lombardy,3166753
Segrate,Italy,Lombardy,3166808
Schio,Italy,Veneto,3166917
Scandicci,Italy,Tuscany,3166988
Scafati,Italy,Campania,3167010
Savona,Italy,Liguria,3167022
Savigliano,Italy,Piedmont,3167034
Sava,Italy,Apulia,3167044
Sassuolo,Italy,Emilia-Romagna,3167053
Sassari,Italy,Sardinia,3167096
Sarzana,Italy,Liguria,3167104
Saronno,Italy,Lombardy,3167113
Sarno,Italy,Campania,3167116
San Vito dei Normanni,Italy,Apulia,3167184
Santeramo in Colle,Italy,Apulia,3167327
Sant'Antonio Abate,Italy,Campania,3167393
Sant'Antimo,Italy,Campania,3167419
Sant'Anastasia,Italy,Campania,3167509
Santa Maria Capua Vetere,Italy,Campania,3167561
San Severo,Italy,Apulia,3167731
San Sebastiano,Italy,Lombardy,3167744
San Salvo,Italy,Abruzzo,3167751
San Remo,Italy,Liguria,3167777
Sannicandro Garganico,Italy,Apulia,3167940
San Miniato,Italy,Tuscany,3167953
San Miniato Basso,Italy,Tuscany,3167954
San Mauro Torinese,Italy,Piedmont,3167978
San Lazzaro,Italy,Emilia-Romagna,3168175
San Giuseppe Vesuviano,Italy,Campania,3168209
San Giuliano Milanese,Italy,Lombardy,3168222
San Giovanni Valdarno,Italy,Tuscany,3168231
San Giovanni Rotondo,Italy,Apulia,3168234
San Giovanni Lupatoto,Italy,Veneto,3168236
San Giovanni in Persiceto,Italy,Emilia-Romagna,3168239
San Giorgio a Cremano,Italy,Campania,3168309
San Donato Milanese,Italy,Lombardy,3168414
San DonÃ  di Piave,Italy,Veneto,3168429
San Bonifacio,Italy,Veneto,3168514
San Benedetto del Tronto,Italy,The Marches,3168550
Salsomaggiore Terme,Italy,Emilia-Romagna,3168627
Salerno,Italy,Campania,3168673
Sacile,Italy,Friuli Venezia Giulia,3168730
Ruvo di Puglia,Italy,Apulia,3168770
Rutigliano,Italy,Apulia,3168775
Rozzano,Italy,Lombardy,3168837
Rovigo,Italy,Veneto,3168843
Rovereto,Italy,Trentino-Alto Adige,3168854
Rosignano Solvay-Castiglioncello,Italy,Tuscany,3168930
Roseto degli Abruzzi,Italy,Abruzzo,3168936
Romano di Lombardia,Italy,Lombardy,3169056
Rome,Italy,Latium,3169070
Rocca di Papa,Italy,Latium,3169181
Rivoli,Italy,Piedmont,3169231
Rimini,Italy,Emilia-Romagna,3169361
Rieti,Italy,Latium,3169412
Riccione,Italy,Emilia-Romagna,3169424
Rho,Italy,Lombardy,3169447
Reggio nell'Emilia,Italy,Emilia-Romagna,3169522
Ravenna,Italy,Emilia-Romagna,3169561
Rapallo,Italy,Liguria,3169602
Qualiano,Italy,Campania,3169724
Putignano,Italy,Apulia,3169742
Prato,Italy,Tuscany,3169921
Pozzuoli,Italy,Campania,3169984
Potenza,Italy,Basilicate,3170027
Porto Torres,Italy,Sardinia,3170069
Porto Sant'Elpidio,Italy,The Marches,3170072
Porto San Giorgio,Italy,The Marches,3170073
Portogruaro,Italy,Veneto,3170086
Civitanova Marche,Italy,The Marches,3170102
Portici,Italy,Campania,3170116
Pordenone,Italy,Friuli Venezia Giulia,3170147
Pontedera,Italy,Tuscany,3170272
Pompei,Italy,Campania,3170335
Pomigliano d'Arco,Italy,Campania,3170341
Pomezia,Italy,Latium,3170342
Poggiomarino,Italy,Campania,3170457
Poggibonsi,Italy,Tuscany,3170504
Pistoia,Italy,Tuscany,3170621
Pisa,Italy,Tuscany,3170647
Piossasco,Italy,Piedmont,3170659
Piombino,Italy,Tuscany,3170674
Pioltello,Italy,Lombardy,3170676
Pinerolo,Italy,Piedmont,3170694
Pietrasanta,Italy,Tuscany,3170778
Piacenza,Italy,Emilia-Romagna,3171058
Pescara,Italy,Abruzzo,3171168
Pesaro,Italy,The Marches,3171173
Perugia,Italy,Umbria,3171180
Pavia,Italy,Lombardy,3171366
Parma,Italy,Emilia-Romagna,3171457
Parabiago,Italy,Lombardy,3171484
Palo del Colle,Italy,Apulia,3171562
Palazzolo sull'Oglio,Italy,Lombardy,3171586
Palagiano,Italy,Apulia,3171664
Pagani,Italy,Campania,3171703
Padova,Italy,Veneto,3171728
Paderno Dugnano,Italy,Lombardy,3171737
Ottaviano,Italy,Campania,3171778
Ostuni,Italy,Apulia,3171786
Osimo,Italy,The Marches,3171848
Orta Nova,Italy,Apulia,3171900
Orbassano,Italy,Piedmont,3171986
Olbia,Italy,Sardinia,3172087
Oderzo,Italy,Veneto,3172116
Nuoro,Italy,Sardinia,3172154
Novi Ligure,Italy,Piedmont,3172170
Novate Milanese,Italy,Lombardy,3172184
Novara,Italy,Piedmont,3172189
Nova Milanese,Italy,Lombardy,3172191
Nola,Italy,Campania,3172227
Noicattaro,Italy,Apulia,3172228
Noci,Italy,Apulia,3172240
Nocera Superiore,Italy,Campania,3172243
Nocera Inferiore,Italy,Campania,3172244
Nichelino,Italy,Piedmont,3172269
Nettuno,Italy,Latium,3172287
Nerviano,Italy,Lombardy,3172297
NardÃ²,Italy,Apulia,3172379
Napoli,Italy,Campania,3172394
Mugnano di Napoli,Italy,Campania,3172472
MuggiÃ²,Italy,Lombardy,3172479
Monza,Italy,Lombardy,3172629
Montichiari,Italy,Lombardy,3172681
Montevarchi,Italy,Tuscany,3172718
Montesilvano Marina,Italy,Abruzzo,3172729
Monterotondo,Italy,Latium,3172768
Montemurlo,Italy,Tuscany,3172828
Montecchio Maggiore-Alte Ceccato,Italy,Veneto,3172979
Montecatini-Terme,Italy,Tuscany,3172996
Montebelluna,Italy,Veneto,3173029
Monopoli,Italy,Apulia,3173131
Monfalcone,Italy,Friuli Venezia Giulia,3173153
Mondragone,Italy,Campania,3173160
MondovÃ¬,Italy,Piedmont,3173162
Moncalieri,Italy,Piedmont,3173180
Molfetta,Italy,Apulia,3173287
Mola di Bari,Italy,Apulia,3173302
Mogliano Veneto,Italy,Veneto,3173314
Modugno,Italy,Apulia,3173326
Modena,Italy,Emilia-Romagna,3173331
Mirano,Italy,Veneto,3173369
Mirandola,Italy,Emilia-Romagna,3173370
Mira Taglio,Italy,Veneto,3173385
Minturno,Italy,Latium,3173391
Milano,Italy,Lombardy,3173435
Mestre,Italy,Veneto,3173529
Mesagne,Italy,Apulia,3173537
Merano,Italy,Trentino-Alto Adige,3173577
Mentana,Italy,Latium,3173582
Melzo,Italy,Lombardy,3173599
Melito di Napoli,Italy,Campania,3173614
Melegnano,Italy,Lombardy,3173631
Meda,Italy,Lombardy,3173671
Matera,Italy,Basilicate,3173721
Massafra,Italy,Apulia,3173762
Massa,Italy,Tuscany,3173775
Martina Franca,Italy,Apulia,3173841
Marino,Italy,Latium,3173914
Marina di Carrara,Italy,Tuscany,3173935
Marigliano,Italy,Campania,3173945
Mariano Comense,Italy,Lombardy,3173949
Marcianise,Italy,Campania,3173995
Marano di Napoli,Italy,Campania,3174021
Mantova,Italy,Lombardy,3174051
Manfredonia,Italy,Apulia,3174092
Manduria,Italy,Apulia,3174096
Malnate,Italy,Lombardy,3174141
Magenta,Italy,Lombardy,3174295
Maddaloni,Italy,Campania,3174358
Macerata,Italy,The Marches,3174380
Lugo,Italy,Emilia-Romagna,3174494
Lucera,Italy,Apulia,3174526
Lucca,Italy,Tuscany,3174530
Lodi,Italy,Lombardy,3174638
Livorno,Italy,Tuscany,3174659
Lissone,Italy,Lombardy,3174679
Limbiate,Italy,Lombardy,3174719
Lido di Ostia,Italy,Latium,3174741
Lido,Italy,Veneto,3174748
Legnano,Italy,Lombardy,3174921
Legnago,Italy,Veneto,3174922
Lecco,Italy,Lombardy,3174945
Lecce,Italy,Apulia,3174953
Latina,Italy,Latium,3175058
La Spezia,Italy,Liguria,3175081
L'Aquila,Italy,Abruzzo,3175121
Lanciano,Italy,Abruzzo,3175173
Lainate,Italy,Lombardy,3175238
Ladispoli,Italy,Latium,3175298
Ivrea,Italy,Piedmont,3175384
Isernia,Italy,Molise,3175445
Ischia Porto,Italy,Campania,3175453
Ischia,Italy,Campania,3175458
Pallanza-Intra-Suna,Italy,Piedmont,3175500
Imperia,Italy,Liguria,3175532
Imola,Italy,Emilia-Romagna,3175537
Jesi,Italy,The Marches,3175628
Guidonia,Italy,Latium,3175678
Grumo Nevano,Italy,Campania,3175743
Grugliasco,Italy,Piedmont,3175755
Grottaglie,Italy,Apulia,3175773
Grottaferrata,Italy,Latium,3175775
Grosseto,Italy,Tuscany,3175786
Gravina in Puglia,Italy,Apulia,3175860
Gragnano,Italy,Campania,3175952
Gorizia,Italy,Friuli Venezia Giulia,3175986
Gorgonzola,Italy,Lombardy,3175990
Giussano,Italy,Lombardy,3176041
Giulianova,Italy,Abruzzo,3176053
Giugliano in Campania,Italy,Campania,3176059
Giovinazzo,Italy,Apulia,3176072
Gioia del Colle,Italy,Apulia,3176090
Ginosa,Italy,Apulia,3176097
Ghedi,Italy,Lombardy,3176177
Genzano di Roma,Italy,Latium,3176203
Genoa,Italy,Liguria,3176219
Garbagnate Milanese,Italy,Lombardy,3176322
Gallipoli,Italy,Apulia,3176366
Gallarate,Italy,Lombardy,3176391
Galatina,Italy,Apulia,3176407
Gaeta,Italy,Latium,3176438
Frosinone,Italy,Latium,3176515
Frattaminore,Italy,Campania,3176560
Frattamaggiore,Italy,Campania,3176561
Frascati,Italy,Latium,3176589
Francavilla Fontana,Italy,Apulia,3176603
Francavilla al Mare,Italy,Abruzzo,3176605
Fossano,Italy,Piedmont,3176639
Fornacelle,Italy,Tuscany,3176722
Formigine,Italy,Emilia-Romagna,3176733
Formia,Italy,Latium,3176738
ForlÃ¬,Italy,Emilia-Romagna,3176746
Forio,Italy,Campania,3176748
Fondi,Italy,Latium,3176843
Follonica,Italy,Tuscany,3176849
Foligno,Italy,Umbria,3176854
Foggia,Italy,Apulia,3176885
Fiumicino-Isola Sacra,Italy,Latium,3176923
Florence,Italy,Tuscany,3176959
Fiorano,Italy,Emilia-Romagna,3176970
Fidenza,Italy,Emilia-Romagna,3177029
Ferrara,Italy,Emilia-Romagna,3177090
Fermo,Italy,The Marches,3177099
Fasano,Italy,Apulia,3177171
Fano,Italy,The Marches,3177219
Falconara Marittima,Italy,The Marches,3177250
Faenza,Italy,Emilia-Romagna,3177300
Fabriano,Italy,The Marches,3177315
Ercolano,Italy,Campania,3177363
Erba,Italy,Lombardy,3177372
Empoli,Italy,Tuscany,3177400
Eboli,Italy,Campania,3177438
Domodossola,Italy,Piedmont,3177532
Desio,Italy,Lombardy,3177608
Desenzano del Garda,Italy,Lombardy,3177610
Dalmine,Italy,Lombardy,3177650
Cusano Milanino,Italy,Lombardy,3177664
Cuneo,Italy,Piedmont,3177700
Cremona,Italy,Lombardy,3177838
Crema,Italy,Lombardy,3177841
Corsico,Italy,Lombardy,3178004
Correggio,Italy,Emilia-Romagna,3178019
Cornaredo,Italy,Lombardy,3178074
Cormano,Italy,Lombardy,3178087
Cordenons,Italy,Friuli Venezia Giulia,3178112
Corato,Italy,Apulia,3178131
Copertino,Italy,Apulia,3178141
Conversano,Italy,Apulia,3178147
Conegliano,Italy,Veneto,3178197
Como,Italy,Lombardy,3178229
Cologno Monzese,Italy,Lombardy,3178283
Collegno,Italy,Piedmont,3178388
Colleferro,Italy,Latium,3178398
Colle di Val d'Elsa,Italy,Tuscany,3178402
Civitavecchia,Italy,Latium,3178587
CittÃ  di Castello,Italy,Umbria,3178619
Cisterna di Latina,Italy,Latium,3178631
CiriÃ¨,Italy,Piedmont,3178650
Cinisello Balsamo,Italy,Lombardy,3178671
Ciampino,Italy,Latium,3178738
Chivasso,Italy,Piedmont,3178745
Chioggia,Italy,Veneto,3178784
Chieti,Italy,Abruzzo,3178796
Chieri,Italy,Piedmont,3178818
Chiavari,Italy,Liguria,3178832
Chiari,Italy,Lombardy,3178850
Cesenatico,Italy,Emilia-Romagna,3178956
Cesena,Italy,Emilia-Romagna,3178957
Cesano Maderno,Italy,Lombardy,3178972
Cervia,Italy,Emilia-Romagna,3178998
Cerveteri,Italy,Latium,3178999
Cernusco sul Naviglio,Italy,Lombardy,3179066
Cerignola,Italy,Apulia,3179075
Cercola,Italy,Campania,3179109
Cento,Italy,Emilia-Romagna,3179162
Ceglie Messapica,Italy,Apulia,3179218
Cecina,Italy,Tuscany,3179235
Cava DÃ¨ Tirreni,Italy,Campania,3179337
Cattolica,Italy,Emilia-Romagna,3179347
Castiglione delle Stiviere,Italy,Lombardy,3179415
Castel Volturno,Italy,Campania,3179443
Castel Maggiore,Italy,Emilia-Romagna,3179560
Castellammare di Stabia,Italy,Campania,3179661
Castelfranco Veneto,Italy,Veneto,3179684
Castelfranco Emilia,Italy,Emilia-Romagna,3179686
Cassino,Italy,Latium,3179781
Cassano d'Adda,Italy,Lombardy,3179795
Casoria,Italy,Campania,3179806
Caserta,Italy,Campania,3179866
Cascina,Italy,Tuscany,3179977
Casamassima,Italy,Apulia,3180133
Casalnuovo di Napoli,Italy,Campania,3180172
Casale Monferrato,Italy,Piedmont,3180208
Casalecchio di Reno,Italy,Emilia-Romagna,3180224
Casal di Principe,Italy,Campania,3180240
Carrara,Italy,Tuscany,3180423
Carpi Centro,Italy,Emilia-Romagna,3180445
Carmagnola,Italy,Piedmont,3180496
Cardito,Italy,Campania,3180541
Carate Brianza,Italy,Lombardy,3180581
Capua,Italy,Campania,3180601
Capannori,Italy,Tuscany,3180733
CantÃ¹,Italy,Lombardy,3180758
Canosa di Puglia,Italy,Apulia,3180792
Campobasso,Italy,Molise,3180991
Campi Bisenzio,Italy,Tuscany,3181018
Camaiore,Italy,Tuscany,3181125
Caivano,Italy,Campania,3181258
Busto Arsizio,Italy,Lombardy,3181355
Bussolengo,Italy,Veneto,3181359
Brusciano,Italy,Campania,3181471
Brugherio,Italy,Lombardy,3181495
Brindisi,Italy,Apulia,3181528
Bresso,Italy,Lombardy,3181548
Bressanone,Italy,Trentino-Alto Adige,3181550
Brescia,Italy,Lombardy,3181554
Bra,Italy,Piedmont,3181631
Bovisio-Masciago,Italy,Lombardy,3181641
Boscoreale,Italy,Campania,3181683
Borgomanero,Italy,Piedmont,3181790
Bolzano,Italy,Trentino-Alto Adige,3181913
Bologna,Italy,Emilia-Romagna,3181928
Bollate,Italy,Lombardy,3181931
Bitonto,Italy,Apulia,3181995
Bisceglie,Italy,Apulia,3182007
Biella,Italy,Piedmont,3182043
Bergamo,Italy,Lombardy,3182164
Benevento,Italy,Campania,3182179
Belluno,Italy,Veneto,3182210
Battipaglia,Italy,Campania,3182272
Bastia umbra,Italy,Umbria,3182289
Bassano del Grappa,Italy,Veneto,3182297
Barletta,Italy,Apulia,3182340
Bari,Italy,Apulia,3182351
Bareggio,Italy,Lombardy,3182361
Bagnoli,Italy,Campania,3182518
Bacoli,Italy,Campania,3182599
Avezzano,Italy,Abruzzo,3182636
Aversa,Italy,Campania,3182640
Avellino,Italy,Campania,3182650
Asti,Italy,Piedmont,3182714
Ascoli Piceno,Italy,The Marches,3182749
Arzignano,Italy,Veneto,3182757
Arzano,Italy,Campania,3182765
Ariccia,Italy,Latium,3182851
Arezzo,Italy,Tuscany,3182884
Arese,Italy,Lombardy,3182886
Ardea,Italy,Latium,3182897
Arcore,Italy,Lombardy,3182904
Aprilia,Italy,Latium,3182957
Aosta,Italy,Aosta Valley,3182997
Anzio,Italy,Latium,3183005
Angri,Italy,Campania,3183063
Andria,Italy,Apulia,3183072
Ancona,Italy,The Marches,3183089
Altamura,Italy,Apulia,3183178
Alpignano,Italy,Piedmont,3183187
Alghero,Italy,Sardinia,3183284
Alessandria,Italy,Piedmont,3183299
Albignasego,Italy,Veneto,3183319
Albenga,Italy,Liguria,3183343
Albano Laziale,Italy,Latium,3183356
Alba,Italy,Piedmont,3183364
Agropoli,Italy,Campania,3183412
Afragola,Italy,Campania,3183455
Adelfia,Italy,Apulia,3183472
Acqui Terme,Italy,Piedmont,3183490
Acquaviva delle Fonti,Italy,Apulia,3183494
Acilia-Castel Fusano-Ostia Antica,Italy,Latium,3183539
Acerra,Italy,Campania,3183541
Abbiategrasso,Italy,Lombardy,3183573
Abano Terme,Italy,Veneto,3183587
Spinea-Orgnano,Italy,Veneto,3219114
Verbania,Italy,Piedmont,6457398
Lumezzane,Italy,Lombardy,6534216
Guidonia Montecelio,Italy,Latium,6534228
Lamezia Terme,Italy,Calabria,6534232
Caronno Pertusella,Italy,Lombardy,6534234
Cassano Magnago,Italy,Lombardy,6534235
San Felice A Cancello,Italy,Campania,6534252
San Nicola la Strada,Italy,Campania,6534253
Quarto,Italy,Campania,6534256
Orta di Atella,Italy,Campania,6534264
Casavatore,Italy,Campania,6534267
Volla,Italy,Campania,6534268
Gravina di Catania,Italy,Sicily,6534275
Cesano Boscone,Italy,Lombardy,6534280
Tor Lupara,Italy,Latium,6534284
Torvaianica,Italy,Latium,6620312
Bellaria-Igea Marina,Italy,Emilia-Romagna,8224092
Villanova,Italy,Latium,8378910
Marina di Ardea-Tor San Lorenzo,Italy,Latium,8394392
San Paolo,Italy,Apulia,8948703
Monterusciello,Italy,Campania,8948704
Romano Banco,Italy,Lombardy,8948705
Casa Santa,Italy,Sicily,8948706
Arpino,Italy,Campania,8948708
Paolo VI,Italy,Apulia,8948709
Corigliano Scalo,Italy,Calabria,9003711
Saint Helier,Jersey,St Helier,3042091
Spanish Town,Jamaica,Saint Catherine,3488465
Savanna-la-Mar,Jamaica,Westmoreland,3488613
Portmore,Jamaica,Saint Catherine,3488981
Old Harbour,Jamaica,Saint Catherine,3489227
New Kingston,Jamaica,Saint Andrew,3489297
Montego Bay,Jamaica,Saint James,3489460
May Pen,Jamaica,Clarendon,3489523
Mandeville,Jamaica,Manchester,3489577
Linstead,Jamaica,Saint Catherine,3489760
Kingston,Jamaica,Kingston,3489854
Half Way Tree,Jamaica,Saint Andrew,3490165
WÄdÄ« as SÄ«r,Jordan,Amman,246013
Umm as SummÄq,Jordan,Amman,246314
Saá¸©Äb,Jordan,Amman,247105
MÄdabÄ,Jordan,Madaba,248370
Ma'an,Jordan,Maâ€™an,248382
Kurayyimah,Jordan,Irbid,248414
Judita,Jordan,Irbid,248803
Jarash,Jordan,Jerash,248875
â€˜IzrÄ,Jordan,Karak,248923
Irbid,Jordan,Irbid,248946
Zarqa,Jordan,Zarqa,250090
AydÅ«n,Jordan,Irbid,250152
AÅ£ Å¢afÄ«lah,Jordan,Tafielah,250198
As SalÅ£,Jordan,Balqa,250258
Safi,Jordan,Karak,250267
Ar RamthÄ,Jordan,Irbid,250336
â€˜Anjarah,Jordan,Ajlun,250420
Amman,Jordan,Amman,250441
Al Quwaysimah,Jordan,Amman,250461
Mafraq,Jordan,Mafraq,250582
QÄ«r MoÄv,Jordan,Maâ€™an,250624
Al Jubayhah,Jordan,Amman,250637
Aqaba,Jordan,Aqaba,250774
â€˜AjlÅ«n,Jordan,Ajlun,250799
Karak City,Jordan,Karak,6946409
Russeifa,Jordan,Zarqa,7838895
ShingÅ«,Japan,Wakayama,1847947
Atsugi,Japan,Kanagawa,1847963
Akashi,Japan,HyÅgo,1847966
Zushi,Japan,Kanagawa,1847968
Zama,Japan,Kanagawa,1848004
Yuza,Japan,Yamagata,1848016
Gero,Japan,Gifu,1848055
Yukuhashi,Japan,Fukuoka,1848087
YÅ«ki,Japan,Ibaraki,1848096
Yugawara,Japan,Kanagawa,1848113
Yoshikawa,Japan,Saitama,1848188
Yoshii,Japan,Gunma,1848194
Yoshida-kasugachÅ,Japan,Niigata,1848210
Yorii,Japan,Saitama,1848243
Yono,Japan,Saitama,1848254
Yonago,Japan,Tottori,1848277
Yokosuka,Japan,Kanagawa,1848313
Yokohama,Japan,Kanagawa,1848354
Yokkaichi,Japan,Mie,1848373
Youkaichi,Japan,Shiga Prefecture,1848382
Yawata,Japan,Kyoto,1848439
Yatsushiro,Japan,Kumamoto,1848445
Yatsuomachi-higashikumisaka,Japan,Toyama,1848447
YasugichÅ,Japan,Shimane,1848482
Yashiro,Japan,HyÅgo,1848498
Yashio-shi,Japan,Saitama,1848499
Yao,Japan,ÅŒsaka,1848522
Yanai,Japan,Yamaguchi,1848550
Yanagawa,Japan,Fukuoka,1848573
YamazakichÅ-nakabirose,Japan,HyÅgo,1848633
Yamaguchi,Japan,Yamaguchi,1848689
Yamaga,Japan,Kumamoto,1848705
Yaizu,Japan,Shizuoka,1848774
Yaita,Japan,Tochigi,1848776
Wakimachi,Japan,Tokushima,1848933
Utsunomiya,Japan,Tochigi,1849053
Uto,Japan,Kumamoto,1849069
Usuki,Japan,Oita,1849094
Ushibuka,Japan,Kumamoto,1849154
Ureshinomachi-shimojuku,Japan,Saga Prefecture,1849183
Urayasu,Japan,Tokyo,1849186
Uozu,Japan,Toyama,1849237
Umi,Japan,Fukuoka,1849299
Ujiie,Japan,Tochigi,1849367
Uji,Japan,Kyoto,1849372
Uenohara,Japan,Yamanashi,1849407
Ueno-ebisumachi,Japan,Mie,1849414
Ueki,Japan,Kumamoto,1849424
Ueda,Japan,Nagano,1849429
Ube,Japan,Yamaguchi,1849498
Tsuyama,Japan,Okayama,1849519
Tsushima,Japan,Aichi,1849539
Tsurusaki,Japan,Oita,1849561
Tsuruoka,Japan,Yamagata,1849563
Tsurugi-asahimachi,Japan,Ishikawa,1849584
Tsuruga,Japan,Fukui,1849592
Tsuma,Japan,Miyazaki,1849647
Tsukumiura,Japan,Oita,1849661
Tsukawaki,Japan,Oita,1849706
Tsubata,Japan,Ishikawa,1849782
Tsubame,Japan,Niigata,1849788
Tsu,Japan,Mie,1849796
Toyota,Japan,Aichi,1849814
Toyoshina,Japan,Nagano,1849817
Toyooka,Japan,HyÅgo,1849831
Toyonaka,Japan,ÅŒsaka,1849837
Toyokawa,Japan,Aichi,1849845
Toyohashi,Japan,Aichi,1849846
Toyohama,Japan,Aichi,1849850
Toyama,Japan,Toyama,1849876
Tottori,Japan,Tottori,1849892
Tosu,Japan,Saga Prefecture,1849904
TonoshÅ,Japan,Kagawa,1850004
TondabayashichÅ,Japan,ÅŒsaka,1850034
Tomioka,Japan,Gunma,1850091
Tomigusuku,Japan,Okinawa,1850108
Tokyo,Japan,Tokyo,1850147
Tokuyama,Japan,Yamaguchi,1850152
Tokushima,Japan,Tokushima,1850158
Tokorozawa,Japan,Saitama,1850181
Tokoname,Japan,Aichi,1850185
Toki,Japan,Gifu,1850207
TÅkamachi,Japan,Niigata,1850217
Togitsu,Japan,Nagasaki,1850269
Tochio-honchÅ,Japan,Niigata,1850307
Tochigi,Japan,Tochigi,1850311
Toba,Japan,Mie,1850345
Tenri,Japan,Nara,1850396
TennÅ,Japan,Akita,1850405
Tawaramoto,Japan,Nara,1850472
Tatsuno,Japan,Nagano,1850498
TatsunochÅ-tominaga,Japan,HyÅgo,1850499
Tateyama,Japan,Chiba,1850523
Tatebayashi,Japan,Gunma,1850559
Tarumizu,Japan,Kagoshima,1850589
Tarui,Japan,Gifu,1850600
Tanushimarumachi-toyoki,Japan,Fukuoka,1850627
Tanuma,Japan,Tochigi,1850630
Nishi-Tokyo-shi,Japan,Tokyo,1850692
TanashichÅ,Japan,Tokyo,1850693
Tanabe,Japan,Kyoto,1850707
Tanabe,Japan,Wakayama,1850708
Tamano,Japan,Okayama,1850742
Tamana,Japan,Kumamoto,1850745
Tamamura,Japan,Gunma,1850746
Taketoyo,Japan,Aichi,1850818
TakeochÅ-takeo,Japan,Saga Prefecture,1850834
Takehara,Japan,Hiroshima,1850860
Takefu,Japan,Fukui,1850872
Takedamachi,Japan,Oita,1850878
Takayama,Japan,Gifu,1850892
Takatsuki,Japan,ÅŒsaka,1850910
Takasaki,Japan,Gunma,1851002
Takarazuka,Japan,HyÅgo,1851012
Takaoka,Japan,Toyama,1851032
Takanabe,Japan,Miyazaki,1851068
Takamatsu,Japan,Kagawa,1851100
Takaishi,Japan,ÅŒsaka,1851125
Takahashi,Japan,Okayama,1851137
Takahama,Japan,Aichi,1851155
Bungo-Takada-shi,Japan,Oita,1851170
Tajimi,Japan,Gifu,1851193
Tahara,Japan,Aichi,1851259
Tagawa,Japan,Fukuoka,1851273
Tadotsu,Japan,Kagawa,1851282
Suzuka,Japan,Mie,1851348
Suzaka,Japan,Nagano,1851357
Suwa,Japan,Nagano,1851368
Susaki,Japan,Kochi,1851390
Sumoto,Japan,HyÅgo,1851426
Sukumo,Japan,Kochi,1851462
Suita,Japan,ÅŒsaka,1851483
Suibara,Japan,Niigata,1851494
Sugito,Japan,Saitama,1851504
SueyoshichÅ-ninokata,Japan,Kagoshima,1851542
SÅka,Japan,Saitama,1851604
SÅja,Japan,Okayama,1851606
Sobue,Japan,Aichi,1851622
ShÅbu,Japan,Saitama,1851711
ShÅbara,Japan,Hiroshima,1851713
Shizuoka,Japan,Shizuoka,1851717
Shirone,Japan,Niigata,1851813
Shiraoka,Japan,Saitama,1851883
ShirahamachÅ-usazakiminami,Japan,HyÅgo,1851935
Shiozawa,Japan,Niigata,1851952
Shiojiri,Japan,Nagano,1852003
Shinshiro,Japan,Aichi,1852046
Shinâ€™ichi,Japan,Hiroshima,1852102
ShingÅ«,Japan,Fukuoka,1852109
Shimonoseki,Japan,Yamaguchi,1852225
Shimodate,Japan,Ibaraki,1852347
Shimoda,Japan,Shizuoka,1852357
Minato,Japan,Wakayama,1852383
Nishishinminato,Japan,Toyama,1852385
Shimada,Japan,Shizuoka,1852472
Shimabara,Japan,Nagasaki,1852479
Shiki,Japan,Saitama,1852502
Shido,Japan,Kagawa,1852561
Shibushi,Japan,Kagoshima,1852588
Shibukawa,Japan,Gunma,1852595
Shibata,Japan,Niigata,1852607
Seto,Japan,Aichi,1852663
Setakamachi-takayanagi,Japan,Fukuoka,1852673
Satsumasendai,Japan,Kagoshima,1852736
Satte,Japan,Saitama,1852849
Sasebo,Japan,Nagasaki,1852899
Sasayama,Japan,HyÅgo,1852901
Sasaguri,Japan,Fukuoka,1852915
Sano,Japan,Tochigi,1852964
SanjÅ,Japan,Niigata,1852984
SandachÅ,Japan,HyÅgo,1853008
Sakurai,Japan,Nara,1853066
Saku,Japan,Nagano,1853081
Sakata,Japan,Yamagata,1853140
Sakaiminato,Japan,Shimane,1853174
SakaidechÅ,Japan,Kagawa,1853190
Sakai-nakajima,Japan,Gunma,1853192
Sakai,Japan,Ibaraki,1853193
Sakai,Japan,ÅŒsaka,1853195
Sakado,Japan,Saitama,1853209
Saiki,Japan,Oita,1853237
Sagara,Japan,Shizuoka,1853280
Saga,Japan,Saga Prefecture,1853303
Sabae,Japan,Fukui,1853338
RyÅ«Å,Japan,Yamanashi,1853354
RyÅtsu-minato,Japan,Niigata,1853371
ÅŒzu,Japan,Kumamoto,1853433
Oyama,Japan,Tochigi,1853483
ÅŒyama,Japan,Shizuoka,1853486
Owase,Japan,Mie,1853514
ÅŒtsuki,Japan,Yamanashi,1853564
ÅŒtsu,Japan,Shiga Prefecture,1853574
ÅŒtake,Japan,Yamaguchi,1853662
ÅŒta,Japan,Gunma,1853677
Osaka,Japan,ÅŒsaka,1853909
Onomichi,Japan,Hiroshima,1853992
Onoda,Japan,Yamaguchi,1854018
Ono,Japan,Fukui,1854022
Ono,Japan,HyÅgo,1854026
ÅŒno-hara,Japan,Hiroshima,1854028
ÅŒmuta,Japan,Fukuoka,1854083
ÅŒmura,Japan,Nagasaki,1854093
ÅŒme,Japan,Tokyo,1854162
ÅŒmamachÅ-Åmama,Japan,Gunma,1854177
ÅŒmachi,Japan,Nagano,1854186
ÅŒkuchi-shinohara,Japan,Kagoshima,1854246
Okegawa,Japan,Saitama,1854371
Okazaki,Japan,Aichi,1854376
Okayama,Japan,Okayama,1854383
Okaya,Japan,Nagano,1854384
ÅŒkawa,Japan,Saga Prefecture,1854405
Ojiya,Japan,Niigata,1854444
ÅŒita,Japan,Oita,1854487
ÅŒiso,Japan,Kanagawa,1854492
ÅŒi,Japan,Saitama,1854530
OgÅri-shimogÅ,Japan,Yamaguchi,1854629
Ogawa,Japan,Saitama,1854665
ÅŒgaki,Japan,Gifu,1854703
Odawara,Japan,Kanagawa,1854747
ÅŒdachÅ-Åda,Japan,Shimane,1854774
ÅŒbu,Japan,Aichi,1854803
Obita,Japan,Nagasaki,1854807
Obama,Japan,Fukui,1854849
NyÅ«zen,Japan,Toyama,1854868
Numazu,Japan,Shizuoka,1854902
Numata,Japan,Gunma,1854905
Nonoichi,Japan,Ishikawa,1854979
NÅgata,Japan,Fukuoka,1855066
Noda,Japan,Chiba,1855078
Nobeoka,Japan,Miyazaki,1855095
Nishiwaki,Japan,HyÅgo,1855134
Nishio,Japan,Aichi,1855189
Nishinoomote,Japan,Kagoshima,1855203
Nishinomiya-hama,Japan,HyÅgo,1855207
Nirasaki,Japan,Yamanashi,1855363
Ninomiya,Japan,Kanagawa,1855380
NikkÅ,Japan,Tochigi,1855395
Niitsu-honchÅ,Japan,Niigata,1855410
Niimi,Japan,Okayama,1855416
Niihama,Japan,Ehime,1855425
Niigata,Japan,Niigata,1855431
Nichinan,Japan,Miyazaki,1855476
Naze,Japan,Kagoshima,1855540
NarutochÅ-mitsuishi,Japan,Tokushima,1855580
Nara-shi,Japan,Nara,1855612
Nanao,Japan,Ishikawa,1855670
Namerikawa,Japan,Toyama,1855694
Nakatsugawa,Japan,Gifu,1855753
Nakatsu,Japan,Fukuoka,1855757
NakanojÅmachi,Japan,Gunma,1855852
Nakano,Japan,Nagano,1855863
Nakamura,Japan,Kochi,1855891
Nakama,Japan,Fukuoka,1855907
Naha,Japan,Okinawa,1856035
Nagoya,Japan,Aichi,1856057
Nago,Japan,Okinawa,1856068
Nagasaki,Japan,Nagasaki,1856177
Nagareyama,Japan,Chiba,1856184
Nagaoka,Japan,Niigata,1856199
Nagano,Japan,Nagano,1856215
Nagahama,Japan,Shiga Prefecture,1856243
Nabari,Japan,Mie,1856293
Musashino,Japan,Tokyo,1856367
Muroto-misakicho,Japan,Kochi,1856392
Muramatsu,Japan,Niigata,1856426
Murakami,Japan,Niigata,1856434
MukÅ,Japan,Kyoto,1856456
Muikamachi,Japan,Niigata,1856476
MorohongÅ,Japan,Saitama,1856560
Moriyama,Japan,Shiga Prefecture,1856569
Moriguchi,Japan,ÅŒsaka,1856584
Mori,Japan,Shizuoka,1856586
Mizunami,Japan,Gifu,1856667
Miyoshi,Japan,Hiroshima,1856698
Miyazu,Japan,Kyoto,1856703
Miyazaki,Japan,Miyazaki,1856717
MiyakonojÅ,Japan,Miyazaki,1856775
Miyata,Japan,Fukuoka,1856828
Mitsuke,Japan,Niigata,1856878
MitsukaidÅ,Japan,Ibaraki,1856881
Mitake,Japan,Gifu,1856938
Mitaka-shi,Japan,Tokyo,1856942
Mishima,Japan,Shizuoka,1856977
Mino,Japan,ÅŒsaka,1857046
Mino,Japan,Gifu,1857062
Minamirinkan,Japan,Kanagawa,1857144
Minamata,Japan,Kumamoto,1857208
MinakuchichÅ-matoba,Japan,Shiga Prefecture,1857209
Mikuni,Japan,Fukui,1857260
Miki,Japan,HyÅgo,1857276
Mihara,Japan,Hiroshima,1857334
Mibu,Japan,Tochigi,1857379
Menuma,Japan,Saitama,1857403
MatsutÅ,Japan,Ishikawa,1857470
Matsumoto,Japan,Nagano,1857519
Matsue,Japan,Shimane,1857550
Matsudo,Japan,Chiba,1857553
Matsubase,Japan,Kumamoto,1857560
Matsubara,Japan,ÅŒsaka,1857568
Masuda,Japan,Shimane,1857594
Maruoka,Japan,Fukui,1857651
Kamimaruko,Japan,Nagano,1857659
Marugame,Japan,Kagawa,1857665
Makurazaki,Japan,Kagoshima,1857712
Maki,Japan,Niigata,1857751
Maizuru,Japan,Kyoto,1857766
Maebashi,Japan,Gunma,1857843
Maebaru-chÅ«Å,Japan,Fukuoka,1857844
Machida,Japan,Tokyo,1857871
Kyoto,Japan,Kyoto,1857910
Kushikino,Japan,Kagoshima,1858041
Kusatsu,Japan,Shiga Prefecture,1858067
Kurume,Japan,Fukuoka,1858088
Kuroda,Japan,Aichi,1858249
Kurihashi,Japan,Saitama,1858283
Kure,Japan,Hiroshima,1858296
Kurayoshi,Japan,Tottori,1858301
Kurashiki,Japan,Okayama,1858311
Kumamoto,Japan,Kumamoto,1858421
Kumagaya,Japan,Saitama,1858428
KukichÅ«Å,Japan,Saitama,1858445
Kudamatsu,Japan,Yamaguchi,1858498
Kozakai-chÅ,Japan,Aichi,1858591
Koshigaya,Japan,Saitama,1858729
Kosai-shi,Japan,Shizuoka,1858756
KÅnosu,Japan,Saitama,1858794
KÅnan,Japan,Aichi,1858836
Komoro,Japan,Nagano,1858858
Komono,Japan,Mie,1858866
KomatsushimachÅ,Japan,Tokushima,1858902
Komatsu,Japan,Ishikawa,1858910
Komaki,Japan,Aichi,1858926
Kokubunji,Japan,Tokyo,1858964
Kokubu-matsuki,Japan,Kagoshima,1858972
Koga,Japan,Ibaraki,1859093
Koga,Japan,Fukuoka,1859094
KÅfu,Japan,Yamanashi,1859100
KodamachÅ-kodamaminami,Japan,Saitama,1859113
Kochi,Japan,Kochi,1859146
Kobe,Japan,HyÅgo,1859171
Kobayashi,Japan,Miyazaki,1859175
Kitsuki,Japan,Oita,1859234
Kitakyushu,Japan,Fukuoka,1859307
Kitakata,Japan,Fukushima,1859319
Kitahama,Japan,Shiga Prefecture,1859335
Kishiwada,Japan,ÅŒsaka,1859383
Kisarazu,Japan,Chiba,1859393
Kisai,Japan,Saitama,1859400
KiryÅ«,Japan,Gunma,1859405
Kikuchi,Japan,Kumamoto,1859492
Kazo,Japan,Saitama,1859586
Kawasaki,Japan,Kanagawa,1859642
Kawasaki,Japan,Fukuoka,1859647
Kawanishi,Japan,HyÅgo,1859675
Kawaguchi,Japan,Saitama,1859730
Kawagoe,Japan,Saitama,1859740
Katsuyama,Japan,Fukui,1859765
Kasukabe,Japan,Saitama,1859884
Kasugai,Japan,Aichi,1859891
Kashiwazaki,Japan,Niigata,1859908
Kashiwa,Japan,Chiba,1859924
Kashima,Japan,Saga Prefecture,1859941
Kashihara-shi,Japan,Nara,1859951
Kashihara,Japan,ÅŒsaka,1859952
Kaseda-shirakame,Japan,Kagoshima,1859964
Kasaoka,Japan,Okayama,1859990
KasamatsuchÅ,Japan,Gifu,1859998
Kariya,Japan,Aichi,1860034
Karatsu,Japan,Saga Prefecture,1860063
Kanzakimachi-kanzaki,Japan,Saga Prefecture,1860095
Kanuma,Japan,Tochigi,1860098
Kanoya,Japan,Kagoshima,1860112
Kanâ€™onjichÅ,Japan,Kagawa,1860122
KannabechÅ-yahiro,Japan,Hiroshima,1860176
Kanie,Japan,Aichi,1860191
Kanekomachi,Japan,Gunma,1860211
Kanda,Japan,Fukuoka,1860234
Kanazawa,Japan,Ishikawa,1860243
Kanaya,Japan,Shizuoka,1860256
KamojimachÅ-jÅgejima,Japan,Tokushima,1860321
KamogatachÅ-kamogata,Japan,Okayama,1860335
Kamo,Japan,Niigata,1860341
Kamirenjaku,Japan,Tokyo,1860437
Kaminokawa,Japan,Tochigi,1860458
Kamiichi,Japan,Toyama,1860563
Kameyama,Japan,Mie,1860626
Kameoka,Japan,Kyoto,1860635
Kameda-honchÅ,Japan,Niigata,1860648
Kamakura,Japan,Kanagawa,1860672
KakogawachÅ-honmachi,Japan,HyÅgo,1860704
Kakegawa,Japan,Shizuoka,1860728
Kakamigahara,Japan,Gifu,1860735
Kashima-shi,Japan,Ibaraki,1860748
Kajiki,Japan,Kagoshima,1860750
Kaizuka,Japan,ÅŒsaka,1860765
Kainan,Japan,Wakayama,1860785
Kagoshima,Japan,Kagoshima,1860827
Kadoma,Japan,ÅŒsaka,1860871
Izumo,Japan,Shimane,1861084
IzumiÅtsu,Japan,ÅŒsaka,1861095
Izumi,Japan,ÅŒsaka,1861107
Izumi,Japan,Kagoshima,1861108
Iwatsuki,Japan,Saitama,1861164
Iwata,Japan,Shizuoka,1861171
Iwakura,Japan,Aichi,1861207
Iwakuni,Japan,Yamaguchi,1861212
Iwai,Japan,Ibaraki,1861223
Iwade,Japan,Wakayama,1861244
Itsukaichi,Japan,Tokyo,1861261
Itoman,Japan,Okinawa,1861280
Itoigawa,Japan,Niigata,1861285
ItÅ,Japan,Shizuoka,1861290
Itami,Japan,HyÅgo,1861310
Ishiki,Japan,Aichi,1861383
Ishikawa,Japan,Okinawa,1861393
Ishii,Japan,Tokushima,1861400
Ishige,Japan,Ibaraki,1861406
Ishigaki,Japan,Okinawa,1861416
Isesaki,Japan,Gunma,1861436
Isehara,Japan,Kanagawa,1861449
Ise,Japan,Mie,1861450
Isawa,Japan,Yamanashi,1861454
Isahaya,Japan,Nagasaki,1861464
Inuyama,Japan,Gifu,1861528
Ino,Japan,Kochi,1861584
Innoshima,Japan,Hiroshima,1861586
Inazawa,Japan,Aichi,1861602
Ina,Japan,Nagano,1861641
ImarichÅ-kÅ,Japan,Saga Prefecture,1861677
Imaichi,Japan,Tochigi,1861699
Ikoma,Japan,Nara,1861749
Ikeda,Japan,ÅŒsaka,1861795
IkedachÅ,Japan,Tokushima,1861799
IjÅ«in,Japan,Kagoshima,1861825
Iizuka,Japan,Fukuoka,1861835
Iiyama,Japan,Nagano,1861838
Iida,Japan,Nagano,1861864
Ichinomiya,Japan,Aichi,1861949
Ibusuki,Japan,Kagoshima,1862010
Ibaraki,Japan,ÅŒsaka,1862033
Ibara,Japan,Okayama,1862034
Hotaka,Japan,Nagano,1862098
HonjÅ,Japan,Saitama,1862198
Hondo,Japan,Kumamoto,1862230
HÅfu,Japan,Yamaguchi,1862302
Hitoyoshi,Japan,Kumamoto,1862352
Hita,Japan,Oita,1862373
Hisai-motomachi,Japan,Mie,1862389
Hiroshima,Japan,Hiroshima,1862415
Hiratsuka,Japan,Kanagawa,1862462
HiratachÅ,Japan,Shimane,1862471
Hirara,Japan,Okinawa,1862505
Hirakata,Japan,ÅŒsaka,1862540
Hirado,Japan,Nagasaki,1862555
Hino,Japan,Tokyo,1862599
Hino,Japan,Shiga Prefecture,1862601
Himimachi,Japan,Toyama,1862612
Himeji,Japan,HyÅgo,1862627
Hikone,Japan,Shiga Prefecture,1862636
Hiji,Japan,Oita,1862689
Hekinan,Japan,Aichi,1862912
Hayama,Japan,Kanagawa,1862992
Hatsukaichi,Japan,Hiroshima,1863018
Hatogaya-honchÅ,Japan,Saitama,1863023
Hashimoto,Japan,Wakayama,1863082
HanyÅ«,Japan,Saitama,1863173
HannÅ,Japan,Saitama,1863183
Handa,Japan,Aichi,1863209
Hamanoichi,Japan,Kagoshima,1863279
Hamamatsu,Japan,Shizuoka,1863289
Hamakita,Japan,Shizuoka,1863293
Hamada,Japan,Shimane,1863310
Hakui,Japan,Ishikawa,1863341
Haibara-akanedai,Japan,Nara,1863398
Hagi,Japan,Yamaguchi,1863418
Katsuren-haebaru,Japan,Okinawa,1863426
Hadano,Japan,Kanagawa,1863431
HachiÅji,Japan,Tokyo,1863440
ÅŒmihachiman,Japan,Shiga Prefecture,1863451
GyÅda,Japan,Saitama,1863482
Gushikawa,Japan,Okinawa,1863495
GÅtsuchÅ,Japan,Shimane,1863521
Gotenba,Japan,Shizuoka,1863528
Gosen,Japan,Niigata,1863540
Gose,Japan,Nara,1863541
GojÅ,Japan,Nara,1863592
GÅdo,Japan,Gifu,1863611
GobÅ,Japan,Wakayama,1863614
Ginowan,Japan,Okinawa,1863627
Gifu-shi,Japan,Gifu,1863641
GamagÅri,Japan,Aichi,1863693
Futtsu,Japan,Chiba,1863713
HonchÅ,Japan,Chiba,1863905
Fukuyama,Japan,Hiroshima,1863917
Fukuroi,Japan,Shizuoka,1863945
Fukura,Japan,HyÅgo,1863953
Fukuoka,Japan,Fukuoka,1863967
Fukumitsu,Japan,Toyama,1863973
Nishifukuma,Japan,Fukuoka,1863978
Fukui-shi,Japan,Fukui,1863985
FukuechÅ,Japan,Nagasaki,1863997
Fukuchiyama,Japan,Kyoto,1864009
Fukiage-fujimi,Japan,Saitama,1864025
FukayachÅ,Japan,Saitama,1864031
Fujisawa,Japan,Kanagawa,1864092
Fujioka,Japan,Tochigi,1864098
Fujioka,Japan,Gunma,1864099
Fujinomiya,Japan,Shizuoka,1864105
Fujieda,Japan,Shizuoka,1864132
Fuji,Japan,Shizuoka,1864134
FuchÅ«chÅ,Japan,Hiroshima,1864155
Enzan,Japan,Yamanashi,1864180
DaitÅchÅ,Japan,ÅŒsaka,1864416
ChÅfugaoka,Japan,Tokyo,1864518
ChiryÅ«,Japan,Aichi,1864549
Chino,Japan,Nagano,1864557
Chikushino-shi,Japan,Fukuoka,1864572
Chigasaki,Japan,Kanagawa,1864624
Chichibu,Japan,Saitama,1864637
Chatan,Japan,Okinawa,1864652
Beppu,Japan,Oita,1864750
Ayabe,Japan,Kyoto,1864873
Atami,Japan,Shizuoka,1864945
Ashiya,Japan,HyÅgo,1864985
Ashikaga,Japan,Tochigi,1865005
Arai,Japan,Niigata,1865207
Annaka,Japan,Gunma,1865290
AnjÅ,Japan,Aichi,1865294
Anan,Japan,Tokushima,1865309
Amagi,Japan,Fukuoka,1865375
Amagasaki,Japan,HyÅgo,1865387
Akune,Japan,Kagoshima,1865401
Kariya,Japan,HyÅgo,1865412
Aki,Japan,Kochi,1865449
Aioi,Japan,HyÅgo,1865661
Ageoshimo,Japan,Saitama,1865714
Okinawa,Japan,Okinawa,1894616
Kushima,Japan,Miyazaki,1895695
Hikari,Japan,Yamaguchi,1896348
Nagato,Japan,Yamaguchi,1899102
Hasuda,Japan,Saitama,1907123
Kamifukuoka,Japan,Saitama,1907125
Sayama,Japan,Saitama,1907146
Fussa,Japan,Tokyo,1907148
Asaka,Japan,Saitama,1907299
Wako,Japan,Saitama,1907300
Shimotoda,Japan,Saitama,1907301
Kimitsu,Japan,Chiba,1907307
Miura,Japan,Kanagawa,1907309
Wakayama,Japan,Wakayama,1926004
Iyo,Japan,Ehime,1926006
Uwajima,Japan,Ehime,1926020
SaijÅ,Japan,Ehime,1926054
ÅŒzu,Japan,Ehime,1926055
Matsuyama,Japan,Ehime,1926099
Masaki-chÅ,Japan,Ehime,1926101
KawanoechÅ,Japan,Ehime,1926116
HÅjÅ,Japan,Ehime,1926142
Yuzawa,Japan,Akita,2110460
YotsukaidÅ,Japan,Chiba,2110480
Yonezawa,Japan,Yamagata,2110498
Yokotemachi,Japan,Akita,2110506
YÅkaichiba,Japan,Chiba,2110518
Yanagawamachi-saiwaichÅ,Japan,Fukushima,2110538
Yamoto,Japan,Miyagi,2110541
Yamagata,Japan,Yamagata,2110556
Yamada,Japan,Iwate,2110560
Yachimata,Japan,Chiba,2110579
Watari,Japan,Miyagi,2110586
Wakuya,Japan,Miyagi,2110596
Ushiku,Japan,Ibaraki,2110629
Tsukuba,Japan,Ibaraki,2110683
Toride,Japan,Ibaraki,2110729
TÅno,Japan,Iwate,2110735
Tomobe,Japan,Ibaraki,2110743
Tomiya,Japan,Miyagi,2110744
TÅgane,Japan,Chiba,2110774
TendÅ,Japan,Yamagata,2110793
Takahata,Japan,Yamagata,2110891
Takahagi,Japan,Ibaraki,2110893
Sukagawa,Japan,Fukushima,2110959
Shizukuishi,Japan,Iwate,2110994
Shisui,Japan,Chiba,2111008
Shiroishi,Japan,Miyagi,2111016
Shiroi,Japan,Chiba,2111018
Shiogama,Japan,Miyagi,2111049
ShinjÅ,Japan,Yamagata,2111065
Sendai,Japan,Miyagi,2111149
Sawara,Japan,Chiba,2111173
Sakura,Japan,Chiba,2111220
Sagae,Japan,Yamagata,2111248
RyÅ«gasaki,Japan,Ibaraki,2111258
Rifu,Japan,Miyagi,2111277
ÅŒtsuchi,Japan,Iwate,2111310
ÅŒtawara,Japan,Tochigi,2111325
ÅŒmiya,Japan,Ibaraki,2111425
Omigawa,Japan,Chiba,2111429
ÅŒmagari,Japan,Akita,2111435
Okunoya,Japan,Ibaraki,2111441
ÅŒkawara,Japan,Miyagi,2111461
ÅŒhara,Japan,Chiba,2111495
ÅŒfunato,Japan,Iwate,2111530
Obanazawa,Japan,Yamagata,2111559
ÅŒarai,Japan,Ibaraki,2111567
ÅŒami,Japan,Chiba,2111568
Nihommatsu,Japan,Fukushima,2111656
NarutÅ,Japan,Chiba,2111677
Narita,Japan,Chiba,2111684
Namie,Japan,Fukushima,2111704
Naka,Japan,Ibaraki,2111749
Nagai,Japan,Yamagata,2111781
Motomiya,Japan,Fukushima,2111824
Motegi,Japan,Tochigi,2111827
Moriya,Japan,Ibaraki,2111831
Morioka,Japan,Iwate,2111834
Mooka,Japan,Tochigi,2111836
Mobara,Japan,Chiba,2111855
Mizusawa,Japan,Iwate,2111859
Miyako,Japan,Iwate,2111884
Mito,Japan,Ibaraki,2111901
Miharu,Japan,Fukushima,2111943
Matsushima,Japan,Miyagi,2111964
Mashiko,Japan,Tochigi,2111999
Marumori,Japan,Miyagi,2112008
Makabe,Japan,Ibaraki,2112019
Kuroiso,Japan,Tochigi,2112077
KÅriyama,Japan,Fukushima,2112141
Kogota,Japan,Miyagi,2112182
Kitakami,Japan,Iwate,2112227
Kitaibaraki,Japan,Ibaraki,2112232
Kamogawa,Japan,Chiba,2112297
Katsuura,Japan,Chiba,2112309
Katsuta,Japan,Ibaraki,2112312
Katori-shi,Japan,Chiba,2112319
Kasama,Japan,Ibaraki,2112343
Karasuyama,Japan,Tochigi,2112354
Kaminoyama,Japan,Yamagata,2112409
Kamaishi,Japan,Iwate,2112444
Kakuda,Japan,Miyagi,2112455
Iwase,Japan,Ibaraki,2112521
Iwanuma,Japan,Miyagi,2112527
Iwaki,Japan,Fukushima,2112539
Itako,Japan,Ibaraki,2112555
Ishioka,Japan,Ibaraki,2112571
Ishinomaki,Japan,Miyagi,2112576
Ishikawa,Japan,Fukushima,2112583
Inawashiro,Japan,Fukushima,2112615
Ichinoseki,Japan,Iwate,2112656
Ichihara,Japan,Chiba,2112664
Hobaramachi,Japan,Fukushima,2112692
Hitachi,Japan,Ibaraki,2112708
Higashine,Japan,Yamagata,2112758
Hasaki,Japan,Chiba,2112802
Hanamaki,Japan,Iwate,2112823
Furukawa,Japan,Miyagi,2112899
Funehikimachi-funehiki,Japan,Fukushima,2112903
Funaishikawa,Japan,Ibaraki,2112913
Fukushima,Japan,Fukushima,2112923
Fujishiro,Japan,Ibaraki,2112940
Edosaki,Japan,Ibaraki,2112963
Daigo,Japan,Ibaraki,2112989
Chiba,Japan,Chiba,2113015
Asahi,Japan,Chiba,2113077
Ami,Japan,Ibaraki,2113115
Akita,Japan,Akita,2113126
Abiko,Japan,Chiba,2113164
Akitashi,Japan,Akita,2113719
Bihoro,Japan,Hokkaido,2127383
Wakkanai,Japan,Hokkaido,2127515
Tomakomai,Japan,Hokkaido,2127733
TÅbetsu,Japan,Hokkaido,2127802
Mutsu,Japan,Aomori,2127878
Takikawa,Japan,Hokkaido,2127896
Takanosu,Japan,Akita,2127910
Sunagawa,Japan,Hokkaido,2127955
Shizunai-furukawachÅ,Japan,Hokkaido,2128025
Shiraoi,Japan,Hokkaido,2128072
Shimo-furano,Japan,Hokkaido,2128147
Shibetsu,Japan,Hokkaido,2128206
Sapporo,Japan,Hokkaido,2128295
Rumoi,Japan,Hokkaido,2128382
Otofuke,Japan,Hokkaido,2128558
Otaru,Japan,Hokkaido,2128574
ÅŒdate,Japan,Akita,2128787
Obihiro,Japan,Hokkaido,2128815
Noshiro,Japan,Akita,2128867
Nemuro,Japan,Hokkaido,2128975
Nayoro,Japan,Hokkaido,2128983
Nanae,Japan,Hokkaido,2129003
Namioka,Japan,Aomori,2129005
Muroran,Japan,Hokkaido,2129101
Mombetsu,Japan,Hokkaido,2129163
Misawa,Japan,Aomori,2129211
Yoichi,Japan,Hokkaido,2129218
Makubetsu,Japan,Hokkaido,2129324
Kushiro,Japan,Hokkaido,2129376
Kuroishi,Japan,Aomori,2129395
Shimokizukuri,Japan,Aomori,2129513
Kitami,Japan,Hokkaido,2129537
Kamiiso,Japan,Hokkaido,2129766
Iwanai,Japan,Hokkaido,2129868
Iwamizawa,Japan,Hokkaido,2129870
Ishikari,Japan,Hokkaido,2129909
Ichinohe,Japan,Iwate,2129961
Kitahiroshima,Japan,Hokkaido,2130054
Hirosaki,Japan,Aomori,2130057
Hanawa,Japan,Akita,2130146
Hakodate,Japan,Hokkaido,2130188
Hachinohe,Japan,Aomori,2130203
Fukagawa,Japan,Hokkaido,2130332
Ebetsu,Japan,Hokkaido,2130404
Date,Japan,Hokkaido,2130421
Chitose,Japan,Hokkaido,2130452
Bibai,Japan,Hokkaido,2130534
Ashibetsu,Japan,Hokkaido,2130612
Asahikawa,Japan,Hokkaido,2130629
Aomorishi,Japan,Aomori,2130658
Abashiri,Japan,Hokkaido,2130741
Goshogawara,Japan,Aomori,2131612
Aso,Japan,Kumamoto,6324583
Nanto-shi,Japan,Toyama,6694821
Kawage,Japan,Mie,6696932
Neyagawa,Japan,ÅŒsaka,6697563
Hitachi-Naka,Japan,Ibaraki,6822096
Inashiki,Japan,Ibaraki,6822108
ÅŒnojÅ,Japan,Fukuoka,6822146
Minokamo,Japan,Gifu,6822217
GujÅ,Japan,Gifu,6822219
JÅetsu,Japan,Niigata,6825489
Saitama,Japan,Saitama,6940394
Higashimurayama-shi,Japan,Tokyo,7279570
Fujikawaguchiko,Japan,Yamanashi,7281819
Dazaifu,Japan,Fukuoka,7422816
KamigyÅ-ku,Japan,Kyoto,8125829
Buzen,Japan,Fukuoka,8198709
Sendai,Japan,Miyagi,8555918
Webuye,Kenya,Bungoma,178202
Wajir,Kenya,Wajir,178443
Voi,Kenya,Taita Taveta,178522
Thika,Kenya,Nairobi Area,179330
Rongai,Kenya,Nakuru,181135
Pumwani,Kenya,Nairobi Area,181501
Nyeri,Kenya,Nyeri,182701
Nyahururu,Kenya,Laikipia,183027
Narok,Kenya,Narok,184379
Nanyuki,Kenya,Laikipia,184433
Nakuru,Kenya,Nakuru,184622
Naivasha,Kenya,Nakuru,184707
Nairobi,Kenya,Nairobi Area,184745
Mumias,Kenya,Kakamega,185702
Muhoroni,Kenya,Kisumu,185939
Moyale,Kenya,Marsabit,186180
Mombasa,Kenya,Mombasa,186301
Molo,Kenya,Nakuru,186315
Migori,Kenya,Migori,186731
Meru,Kenya,Meru,186827
Mbale,Kenya,Vihiga,187110
Marsabit,Kenya,Marsabit,187585
Maralal,Kenya,Samburu,187725
Mandera,Kenya,Mandera,187896
Malindi,Kenya,Kilifi,187968
Makueni,Kenya,Makueni,188080
Machakos,Kenya,Machakos,188492
Lugulu,Kenya,Busia,188657
Lodwar,Kenya,Turkana,189280
Lamu,Kenya,Lamu,189741
Kitui,Kenya,Kitui,191038
Kitale,Kenya,Trans Nzoia,191220
Kisumu,Kenya,Kisumu,191245
Kisii,Kenya,Kisii,191299
Kilifi,Kenya,Kilifi,192067
Kiambu,Kenya,Kiambu,192710
Keruguya,Kenya,Kirinyaga,192859
Kericho,Kenya,Kericho,192900
Karuri,Kenya,Murang'A,193627
Kapenguria,Kenya,West Pokot,194160
Kakamega,Kenya,Kakamega,195272
Kabarnet,Kenya,Baringo,195821
Isiolo,Kenya,Isiolo,196231
Homa Bay,Kenya,Homa Bay,196742
Garissa,Kenya,Garissa,197745
Embu,Kenya,Embu,198476
Eldoret,Kenya,Uasin Gishu,198629
Busia,Kenya,Busia,199989
Bungoma,Kenya,Bungoma,200067
Athi River,Kenya,Machakos,200787
Siaya,Kenya,Siaya,383388
Ol Kalou,Kenya,Nyandarua,7931933
Suluktu,Kyrgyzstan,Batken,1222562
Isfana,Kyrgyzstan,Batken,1222662
Balykchy,Kyrgyzstan,Ysyk-KÃ¶l,1527004
Tokmok,Kyrgyzstan,ChÃ¼y,1527199
Tash-Kumyr,Kyrgyzstan,Jalal-Abad,1527260
Talas,Kyrgyzstan,Talas,1527299
Kyzyl-Suu,Kyrgyzstan,Ysyk-KÃ¶l,1527497
Uzgen,Kyrgyzstan,Osh,1527513
Osh,Kyrgyzstan,Osh,1527534
Naryn,Kyrgyzstan,Naryn,1527592
Kyzyl-Kyya,Kyrgyzstan,Batken,1527719
Kara Suu,Kyrgyzstan,Osh,1528091
Karakol,Kyrgyzstan,Ysyk-KÃ¶l,1528121
Kara-Balta,Kyrgyzstan,ChÃ¼y,1528182
Kant,Kyrgyzstan,ChÃ¼y,1528193
Jalal-Abad,Kyrgyzstan,Jalal-Abad,1528249
Iradan,Kyrgyzstan,Batken,1528283
Cholpon-Ata,Kyrgyzstan,Ysyk-KÃ¶l,1528512
Bishkek,Kyrgyzstan,Bishkek,1528675
Bazar-Korgon,Kyrgyzstan,Jalal-Abad,1528717
At-Bashi,Kyrgyzstan,Naryn,1528796
Toktogul,Kyrgyzstan,Jalal-Abad,1538648
Osh City,Kyrgyzstan,Osh City,11054823
Phnom Penh,Cambodia,Phnom Penh,1821306
Ta Khmau,Cambodia,Kandal,1821935
Takeo,Cambodia,Takeo,1821940
Svay Rieng,Cambodia,Svay Rieng,1821993
Stung Treng,Cambodia,Stung Treng,1822029
SisÅphÅn,Cambodia,Banteay Meanchey,1822207
Siem Reap,Cambodia,Siem Reap,1822214
Prey Veng,Cambodia,Prey Veng,1822610
Pursat,Cambodia,Pursat,1822768
PhumÄ­ VÃ©al SrÃª,Cambodia,Takeo,1822906
SÃ¢mraÃ´ng,Cambodia,ÅŽtÃ¢r MÃ©anchey,1825093
TbÃªng MÃ©anchey,Cambodia,Preah Vihear,1830098
PaÃ´y PÃªt,Cambodia,Banteay Meanchey,1830194
Pailin,Cambodia,Pailin,1830205
LumphÄƒt,Cambodia,Ratanakiri,1830377
Koh Kong,Cambodia,Koh Kong,1830468
KratiÃ©,Cambodia,Kratie,1830564
Kampot,Cambodia,Kampot,1831112
Kampong Thom,Cambodia,Kampong Thom,1831125
Kampong Speu,Cambodia,Kampong Speu,1831133
Sihanoukville,Cambodia,Preah Sihanouk,1831142
Kampong Chhnang,Cambodia,Kampong Chhnang,1831167
Kampong Cham,Cambodia,Kampong Cham,1831173
Ban LÅ­ng,Cambodia,Ratanakiri,1831732
Battambang,Cambodia,Battambang,1831797
Smach Mean Chey,Cambodia,Koh Kong,8740221
Tarawa,Kiribati,Gilbert Islands,2110257
Moutsamoudou,Comoros,Anjouan,921753
Moroni,Comoros,Grande Comore,921772
Basseterre,Saint Kitts and Nevis,Saint George Basseterre,3575551
YÅnan-Å­p,North Korea,Hwanghae-namdo,1866569
WÅnsan,North Korea,KangwÅn-do,1866923
Tâ€™ongchâ€™Ån-Å­p,North Korea,KangwÅn-do,1867927
SÅ­ngho 1-tong,North Korea,Pyongyang,1868998
Sunan,North Korea,Pyongyang,1869021
Songnim,North Korea,Hwanghae-bukto,1869446
Sil-li,North Korea,P'yÅngan-namdo,1870413
Sinmak,North Korea,Hwanghae-bukto,1870434
Sinanju,North Korea,P'yÅngan-namdo,1870742
SariwÅn,North Korea,Hwanghae-bukto,1870883
Samho-rodongjagu,North Korea,HamgyÅng-namdo,1871484
Pyongyang,North Korea,Pyongyang,1871859
Pâ€™yÅngsÅng,North Korea,P'yÅngan-namdo,1871871
Ongjin,North Korea,Hwanghae-namdo,1873172
Nampâ€™o,North Korea,P'yÅngan-namdo,1873757
KusÅng,North Korea,P'yÅngan-bukto,1875107
Kujang-Å­p,North Korea,P'yÅngan-bukto,1875506
KowÅn-Å­p,North Korea,HamgyÅng-namdo,1875588
Kosan,North Korea,KangwÅn-do,1875632
Kangdong-Å­p,North Korea,Pyongyang,1876153
KaesÅng,North Korea,Hwanghae-namdo,1876373
Hwangju-Å­p,North Korea,Hwanghae-bukto,1876873
HÅ­ngnam,North Korea,HamgyÅng-namdo,1877030
HÅ­kkyo-ri,North Korea,Hwanghae-bukto,1877046
Hoeyang,North Korea,KangwÅn-do,1877148
HamhÅ­ng,North Korea,HamgyÅng-namdo,1877449
Haeju,North Korea,Hwanghae-namdo,1877615
Chunghwa,North Korea,Pyongyang,1877872
ChÅngju,North Korea,P'yÅngan-bukto,1878389
ChangyÅn,North Korea,Hwanghae-namdo,1879029
ChaeryÅng-Å­p,North Korea,Hwanghae-namdo,1879487
Ayang-ni,North Korea,Hwanghae-namdo,1879544
Anju,North Korea,P'yÅngan-namdo,1879613
AnbyÅn-Å­p,North Korea,KangwÅn-do,1879672
Anak,North Korea,Hwanghae-bukto,1879682
Yuktae-dong,North Korea,HamgyÅng-namdo,2038854
Å¬iju,North Korea,P'yÅngan-bukto,2039623
SÅnbong,North Korea,Rason,2040674
SinÅ­iju,North Korea,P'yÅngan-bukto,2040893
Sakchu-Å­p,North Korea,P'yÅngan-bukto,2041533
YÅnggwang-Å­p,North Korea,HamgyÅng-namdo,2042249
OnsÅng,North Korea,HamgyÅng-bukto,2042267
Nanam,North Korea,HamgyÅng-bukto,2042498
Namyang-dong,North Korea,HamgyÅng-bukto,2042503
Najin,North Korea,Rason,2042645
Musan-Å­p,North Korea,HamgyÅng-bukto,2042738
KyÅngsÅng,North Korea,HamgyÅng-bukto,2042987
Kilju,North Korea,HamgyÅng-bukto,2043484
Kapsan-Å­p,North Korea,Yanggang-do,2043531
Kanggye-si,North Korea,Chagang-do,2043572
IwÅn-Å­p,North Korea,HamgyÅng-namdo,2043677
Hyesan-dong,North Korea,Yanggang-do,2043835
Hyesan-si,North Korea,Yanggang-do,2043837
HongwÅn,North Korea,HamgyÅng-namdo,2044050
HoeryÅng,North Korea,HamgyÅng-bukto,2044091
Chongjin,North Korea,HamgyÅng-bukto,2044757
Aoji-ri,North Korea,HamgyÅng-bukto,2045311
Heung-hai,South Korea,Gyeongsangbuk-do,1832015
Enjitsu,South Korea,Gyeongsangbuk-do,1832215
Neietsu,South Korea,Gangwon-do,1832257
Eisen,South Korea,Gyeongsangbuk-do,1832384
Reiko,South Korea,Jeollanam-do,1832501
YÅng-dong,South Korea,Chungcheongbuk-do,1832566
Eisen,South Korea,Gyeongsangbuk-do,1832617
Yeoju,South Korea,Gyeonggi-do,1832743
Yesan,South Korea,Chungcheongnam-do,1832771
Yangsan,South Korea,Gyeongsangnam-do,1832828
Yangp'yÅng,South Korea,Gyeonggi-do,1832830
Yangju,South Korea,Gyeonggi-do,1832847
Yanggu,South Korea,Gangwon-do,1832909
WÅnju,South Korea,Gangwon-do,1833105
Wanju,South Korea,Jeollabuk-do,1833466
Waegwan,South Korea,Gyeongsangbuk-do,1833514
Ulsan,South Korea,Ulsan,1833747
Uijeongbu-si,South Korea,Gyeonggi-do,1833788
Tangjin,South Korea,Chungcheongnam-do,1834885
Taesal-li,South Korea,Chungcheongnam-do,1835096
Daejeon,South Korea,Daejeon,1835235
Daegu,South Korea,Daegu,1835329
Taisen-ri,South Korea,Chungcheongnam-do,1835447
Tâ€™aebaek,South Korea,Gangwon-do,1835515
Suwon-si,South Korea,Gyeonggi-do,1835553
Suncheon,South Korea,Jeollanam-do,1835648
Seoul,South Korea,Seoul,1835848
Suisan,South Korea,Chungcheongnam-do,1835895
Jenzan,South Korea,Gyeongsangbuk-do,1835967
Seonghwan,South Korea,Chungcheongnam-do,1836208
Sokcho,South Korea,Gangwon-do,1836553
Sangju,South Korea,Gyeongsangbuk-do,1837706
Santyoku,South Korea,Gangwon-do,1838069
Fuyo,South Korea,Chungcheongnam-do,1838508
Busan,South Korea,Busan,1838524
Bucheon-si,South Korea,Gyeonggi-do,1838716
Puan,South Korea,Jeollabuk-do,1838722
Beolgyo,South Korea,Jeollanam-do,1839011
Pohang,South Korea,Gyeongsangbuk-do,1839071
Osan,South Korea,Gyeonggi-do,1839652
Asan,South Korea,Chungcheongnam-do,1839726
Okcheon,South Korea,Chungcheongbuk-do,1839873
Kosong,South Korea,Gangwon-do,1840179
Nonsan,South Korea,Chungcheongnam-do,1840211
Nangen,South Korea,Jeollabuk-do,1840379
Naju,South Korea,Jeollanam-do,1840536
Munsan,South Korea,Gyeonggi-do,1840862
Mungyeong,South Korea,Gyeongsangbuk-do,1840886
Muan,South Korea,Jeollanam-do,1840982
Moppo,South Korea,Jeollanam-do,1841066
Miryang,South Korea,Gyeongsangnam-do,1841149
Gyeongsan-si,South Korea,Gyeongsangbuk-do,1841598
Kyonju,South Korea,Gyeongsangbuk-do,1841603
Kwangyang,South Korea,Jeollanam-do,1841775
Gwangju,South Korea,Gyeonggi-do,1841810
Gwangju,South Korea,Gwangju,1841811
Kurye,South Korea,Jeollanam-do,1841976
Guri-si,South Korea,Gyeonggi-do,1841988
Kunwi,South Korea,Gyeongsangbuk-do,1842016
Kunsan,South Korea,Jeollabuk-do,1842025
Kinzan,South Korea,Chungcheongnam-do,1842153
Gumi,South Korea,Gyeongsangbuk-do,1842225
Goyang-si,South Korea,Gyeonggi-do,1842485
Goseong,South Korea,Gyeongsangnam-do,1842518
Gongju,South Korea,Chungcheongnam-do,1842616
Kyosai,South Korea,Gyeongsangnam-do,1842754
Koesan,South Korea,Chungcheongbuk-do,1842800
Koch'ang,South Korea,Jeollabuk-do,1842859
Kimje,South Korea,Jeollabuk-do,1842939
Kimhae,South Korea,Gyeongsangnam-do,1842943
Gimcheon,South Korea,Gyeongsangbuk-do,1842944
Gijang,South Korea,Busan,1842966
Gapyeong,South Korea,Gyeonggi-do,1843082
Kang-neung,South Korea,Gangwon-do,1843137
Ganghwa-gun,South Korea,Incheon,1843163
Iksan,South Korea,Jeollabuk-do,1843491
Incheon,South Korea,Incheon,1843564
Imsil,South Korea,Jeollabuk-do,1843585
Icheon-si,South Korea,Gyeonggi-do,1843702
Hwasun,South Korea,Jeollanam-do,1843841
Hwaseong-si,South Korea,Gyeonggi-do,1843847
Hwacheon,South Korea,Gangwon-do,1844045
Hongsung,South Korea,Chungcheongnam-do,1844174
Hongchâ€™Ån,South Korea,Gangwon-do,1844191
Hayang,South Korea,Gyeongsangbuk-do,1844308
Haenam,South Korea,Jeollanam-do,1844751
Chuncheon,South Korea,Gangwon-do,1845136
Jeonju,South Korea,Jeollabuk-do,1845457
Cheongsong gun,South Korea,Gyeongsangbuk-do,1845519
Cheongju-si,South Korea,Chungcheongbuk-do,1845604
Cheonan,South Korea,Chungcheongnam-do,1845759
Chinju,South Korea,Gyeongsangnam-do,1846052
Chinch'Ån,South Korea,Chungcheongbuk-do,1846095
Jinan-gun,South Korea,Jeollabuk-do,1846114
Jeju City,South Korea,Jeju-do,1846266
Changwon,South Korea,Gyeongsangnam-do,1846326
Changsu,South Korea,Jeollabuk-do,1846355
Anyang-si,South Korea,Gyeonggi-do,1846898
Anseong,South Korea,Gyeonggi-do,1846912
Ansan-si,South Korea,Gyeonggi-do,1846918
Andong,South Korea,Gyeongsangbuk-do,1846986
Gaigeturi,South Korea,Jeju-do,1847050
Sinhyeon,South Korea,Gyeongsangnam-do,1882056
Yeosu,South Korea,Jeollanam-do,1884138
YÅnmu,South Korea,Chungcheongnam-do,1886598
Tonghae,South Korea,Gangwon-do,1892823
Pubal,South Korea,Gyeonggi-do,1896953
Seongnam-si,South Korea,Gyeonggi-do,1897000
Hanam,South Korea,Gyeonggi-do,1897007
Hwado,South Korea,Gyeonggi-do,1897118
Namyangju,South Korea,Gyeonggi-do,1897122
Ungsang,South Korea,Gyeongsangnam-do,1912205
Wabu,South Korea,Gyeonggi-do,1912209
NaesÅ,South Korea,Gyeongsangnam-do,1925936
HwawÅn,South Korea,Daegu,1925943
KwangmyÅng,South Korea,Gyeonggi-do,1948005
Sinan,South Korea,Jeollanam-do,6395804
Seogwipo,South Korea,Jeju-do,6621166
Changnyeong,South Korea,Gyeongsangnam-do,6903078
JanÅ«b as Surrah,Kuwait,Al Farwaniyah,285603
á¸¨awallÄ«,Kuwait,Muá¸©ÄfazÌ§at á¸¨awallÄ«,285629
BayÄn,Kuwait,N/A,285663
As SÄlimÄ«yah,Kuwait,Muá¸©ÄfazÌ§at á¸¨awallÄ«,285704
Ar RumaythÄ«yah,Kuwait,Muá¸©ÄfazÌ§at á¸¨awallÄ«,285726
Ar Riqqah,Kuwait,Al Aá¸©madÄ«,285728
Al Manqaf,Kuwait,Al Aá¸©madÄ«,285778
Al MahbÅ«lah,Kuwait,Al Aá¸©madÄ«,285782
Kuwait City,Kuwait,Al Asimah,285787
Al JahrÄâ€™,Kuwait,Al JahrÄÊ¼,285799
Al Faá¸©Äá¸©Ä«l,Kuwait,Al Aá¸©madÄ«,285811
Al FinÅ£Äs,Kuwait,Al Aá¸©madÄ«,285812
Al FarwÄnÄ«yah,Kuwait,Al Farwaniyah,285815
Al Aá¸©madÄ«,Kuwait,Al Aá¸©madÄ«,285839
Ad Dasmah,Kuwait,Al Asimah,285856
SalwÃ¡,Kuwait,Muá¸©ÄfazÌ§at á¸¨awallÄ«,387958
Ar RÄbiyah,Kuwait,Al Asimah,388065
ÅžabÄá¸© as SÄlim,Kuwait,MubÄrak al KabÄ«r,412800
George Town,Cayman Islands,George Town,3580661
Zhanaozen,Kazakhstan,MangghystaÅ«,607610
Shalqar,Kazakhstan,AqtÃ¶be,608359
Shalkar,Kazakhstan,AtyraÅ«,608362
Oral,Kazakhstan,Batys Qazaqstan,608668
Kandyagash,Kazakhstan,AqtÃ¶be,608679
Qulsary,Kazakhstan,AtyraÅ«,609123
Khromtau,Kazakhstan,AqtÃ¶be,609404
Karagandy,Kazakhstan,Qaraghandy,609655
Embi,Kazakhstan,AqtÃ¶be,609924
Balyqshy,Kazakhstan,AtyraÅ«,610445
Atyrau,Kazakhstan,AtyraÅ«,610529
AqtÃ¶be,Kazakhstan,AqtÃ¶be,610611
Aktau,Kazakhstan,MangghystaÅ«,610612
Aqsay,Kazakhstan,Batys Qazaqstan,610613
Zyryanovsk,Kazakhstan,East Kazakhstan,1516438
Zhosaly,Kazakhstan,Qyzylorda,1516519
Zhezqazghan,Kazakhstan,Qaraghandy,1516589
Dzhetygara,Kazakhstan,Qostanay,1516601
Zhangatas,Kazakhstan,Zhambyl,1516788
Ayteke Bi,Kazakhstan,Qyzylorda,1516789
Taraz,Kazakhstan,Zhambyl,1516905
Zaysan,Kazakhstan,East Kazakhstan,1517060
Yanykurgan,Kazakhstan,Qyzylorda,1517323
Vannovka,Kazakhstan,OngtÃ¼stik Qazaqstan,1517501
Ush-Tyube,Kazakhstan,Almaty Oblysy,1517637
Turkestan,Kazakhstan,OngtÃ¼stik Qazaqstan,1517945
Temirtau,Kazakhstan,Qaraghandy,1518262
Tekeli,Kazakhstan,Almaty Oblysy,1518296
TasbÃ¶get,Kazakhstan,Qyzylorda,1518431
Talghar,Kazakhstan,Almaty Oblysy,1518518
Taldykorgan,Kazakhstan,Almaty Oblysy,1518542
Taldyqorghan,Kazakhstan,Almaty Oblysy,1518543
Shymkent,Kazakhstan,OngtÃ¼stik Qazaqstan,1518980
Chu,Kazakhstan,Zhambyl,1519030
ShemonaÄ«kha,Kazakhstan,East Kazakhstan,1519226
ShchÅ«chÄ«nsk,Kazakhstan,SoltÃ¼stik Qazaqstan,1519244
Semey,Kazakhstan,East Kazakhstan,1519422
Saryaghash,Kazakhstan,OngtÃ¼stik Qazaqstan,1519673
Sarkand,Kazakhstan,Almaty Oblysy,1519691
Sorang,Kazakhstan,Qaraghandy,1519725
Rudnyy,Kazakhstan,Qostanay,1519843
Kyzylorda,Kazakhstan,Qyzylorda,1519922
Kostanay,Kazakhstan,Qostanay,1519928
Karatau,Kazakhstan,Zhambyl,1519938
Kapshagay,Kazakhstan,Almaty Oblysy,1519948
Petropavl,Kazakhstan,SoltÃ¼stik Qazaqstan,1520172
Pavlodar,Kazakhstan,Pavlodar,1520240
Zharkent,Kazakhstan,Almaty Oblysy,1520253
Ust-Kamenogorsk,Kazakhstan,East Kazakhstan,1520316
Sarykemer,Kazakhstan,Zhambyl,1520947
Merke,Kazakhstan,Zhambyl,1520969
MakÄ«nsk,Kazakhstan,Aqmola,1521230
Lisakovsk,Kazakhstan,Qostanay,1521315
Baykonyr,Kazakhstan,Bayqongyr Qalasy,1521368
Ridder,Kazakhstan,East Kazakhstan,1521370
Lenger,Kazakhstan,OngtÃ¼stik Qazaqstan,1521379
Kokshetau,Kazakhstan,Aqmola,1522203
Kentau,Kazakhstan,OngtÃ¼stik Qazaqstan,1522751
Esik,Kazakhstan,Almaty Oblysy,1523741
GeorgÄ«evka,Kazakhstan,East Kazakhstan,1524245
Aksu,Kazakhstan,Pavlodar,1524298
Otegen Batyra,Kazakhstan,Almaty Oblysy,1524308
Ekibastuz,Kazakhstan,Pavlodar,1524325
ShÄ«eli,Kazakhstan,Qyzylorda,1524801
Shardara,Kazakhstan,OngtÃ¼stik Qazaqstan,1524889
Burunday,Kazakhstan,Almaty Oblysy,1524958
Aksu,Kazakhstan,OngtÃ¼stik Qazaqstan,1525462
Balqash,Kazakhstan,Qaraghandy,1525798
Ayagoz,Kazakhstan,East Kazakhstan,1525988
Atbasar,Kazakhstan,Aqmola,1526038
Arys,Kazakhstan,OngtÃ¼stik Qazaqstan,1526168
Arkalyk,Kazakhstan,Qostanay,1526193
Aral,Kazakhstan,Qyzylorda,1526265
Astana,Kazakhstan,Astana Qalasy,1526273
Almaty,Kazakhstan,Almaty Qalasy,1526384
Akkolâ€™,Kazakhstan,Aqmola,1526797
Abay,Kazakhstan,Qaraghandy,1526970
Stepnogorsk,Kazakhstan,Aqmola,1537939
Kyzyl-Orda,Kazakhstan,Qyzylorda,9862222
Vientiane,Laos,Vientiane,1651944
Xam Nua,Laos,Houaphan,1652203
SavannakhÃ©t,Laos,SavannahkhÃ©t,1653316
PakxÃ©,Laos,Champasak,1654379
Muang Xay,Laos,OudÃ´mxai,1655078
Vangviang,Laos,Vientiane Province,1655087
Muang PhÃ´nsavan,Laos,Xiangkhoang,1655123
Muang Pakxan,Laos,Bolikhamsai Province,1655140
ThakhÃ¨k,Laos,Khammouan,1655199
Luang Prabang,Laos,Louangphabang,1655559
Ban Houakhoua,Laos,Bokeo Province,1904391
Phonsavan,Laos,Xiangkhoang,1952156
ZahlÃ©,Lebanon,BÃ©qaa,266045
Tripoli,Lebanon,Liban-Nord,266826
Tyre,Lebanon,Liban-Sud,267008
Sidon,Lebanon,Liban-Sud,268064
Raâ€™s BayrÅ«t,Lebanon,Beyrouth,268743
Djounie,Lebanon,Mont-Liban,273140
JbaÃ¯l,Lebanon,Mont-Liban,273203
HabboÃ»ch,Lebanon,NabatÃ®yÃ©,274874
BcharrÃ©,Lebanon,Liban-Nord,276359
Beirut,Lebanon,Beyrouth,276781
Baalbek,Lebanon,Baalbek-Hermel,277130
En NÃ¢qoÃ»ra,Lebanon,Liban-Sud,278832
NabatÃ®yÃ© et Tahta,Lebanon,NabatÃ®yÃ©,278913
Castries,Saint Lucia,Castries Quarter,3576812
Vaduz,Liechtenstein,Vaduz,3042030
Welisara,Sri Lanka,Western,1223648
Weligama,Sri Lanka,Southern,1223738
Wattala,Sri Lanka,Western,1224085
Vavuniya,Sri Lanka,Northern Province,1225018
Valvedditturai,Sri Lanka,Northern Province,1225142
Trincomalee,Sri Lanka,Eastern Province,1226260
Ratnapura,Sri Lanka,Sabaragamuwa,1228730
Puttalam,Sri Lanka,North Western,1229293
Point Pedro,Sri Lanka,Northern Province,1229989
Pita Kotte,Sri Lanka,Western,1230089
Peliyagoda,Sri Lanka,Western,1230613
Panadura,Sri Lanka,Western,1231410
Nuwara Eliya,Sri Lanka,Central,1232783
Negombo,Sri Lanka,Western,1233369
Mulleriyawa,Sri Lanka,Western,1234378
Dehiwala-Mount Lavinia,Sri Lanka,Western,1234569
Moratuwa,Sri Lanka,Western,1234633
Matara,Sri Lanka,Southern,1235846
Maharagama,Sri Lanka,Western,1236854
Kurunegala,Sri Lanka,North Western,1237980
Sri Jayewardenepura Kotte,Sri Lanka,Western,1238992
Kotikawatta,Sri Lanka,Western,1239047
Kolonnawa,Sri Lanka,Western,1239593
Kelaniya,Sri Lanka,Western,1240622
Katunayaka,Sri Lanka,Western,1240935
Kandy,Sri Lanka,Central,1241622
Kandana,Sri Lanka,Western,1241750
Kalutara,Sri Lanka,Western,1241964
Kalmunai,Sri Lanka,Eastern Province,1242110
Jaffna,Sri Lanka,Northern Province,1242833
Ja Ela,Sri Lanka,Western,1242835
Homagama,Sri Lanka,Western,1243936
Hendala,Sri Lanka,Western,1244397
Hatton,Sri Lanka,Central,1244596
Hanwella Ihala,Sri Lanka,Western,1244773
Gampola,Sri Lanka,Central,1246000
Galle,Sri Lanka,Southern,1246294
Galkissa,Sri Lanka,Western,1246321
Eravur Town,Sri Lanka,Eastern Province,1246924
Dambulla,Sri Lanka,Central,1248749
Colombo,Sri Lanka,Western,1248991
Chilaw,Sri Lanka,North Western,1249145
Beruwala,Sri Lanka,Western,1249931
Bentota,Sri Lanka,Southern,1249978
Batticaloa,Sri Lanka,Eastern Province,1250161
Battaramulla South,Sri Lanka,Western,1250164
Badulla,Sri Lanka,Uva,1250615
Anuradhapura,Sri Lanka,North Central,1251081
Ampara,Sri Lanka,Eastern Province,1251459
Ambalangoda,Sri Lanka,Southern,1251574
Shanjeev Home,Sri Lanka,Eastern Province,8260318
Mount Lavinia,Sri Lanka,Western,9259456
Zwedru,Liberia,Grand Gedeh,2272491
New Yekepa,Liberia,Nimba,2272790
Voinjama,Liberia,Lofa,2273312
Monrovia,Liberia,Montserrado,2274895
Kakata,Liberia,Margibi,2276086
Harper,Liberia,Maryland,2276492
Greenville,Liberia,Sinoe,2276600
Gbarnga,Liberia,Bong,2277060
Buchanan,Liberia,Grand Bassa,2278158
Bensonville,Liberia,Montserrado,2278682
Quthing,Lesotho,Quthing,932183
Qachaâ€™s Nek,Lesotho,QachaÊ¼s Nek,932218
Mohaleâ€™s Hoek,Lesotho,MohaleÊ¼s Hoek,932438
Maseru,Lesotho,Maseru,932505
Maputsoe,Lesotho,Leribe,932521
Mafeteng,Lesotho,Mafeteng,932614
Leribe,Lesotho,Leribe,932698
Butha-Buthe,Lesotho,Butha-Buthe,932886
Visaginas,Lithuania,Utenos apskritis,593063
Vilnius,Lithuania,Vilnius County,593116
Utena,Lithuania,Utenos apskritis,593672
Ukmerge,Lithuania,Vilnius County,593733
Telsiai,Lithuania,TelÅ¡iÅ³ apskritis,593926
Taurage,Lithuania,TauragÄ—s apskritis,593959
Silute,Lithuania,KlaipÄ—dos apskritis,594656
Å iauliai,Lithuania,Å iauliÅ³ apskritis,594739
RokiÅ¡kis,Lithuania,PanevÄ—Å¾ys,595213
Radviliskis,Lithuania,Å iauliÅ³ apskritis,595449
Plunge,Lithuania,TelÅ¡iÅ³ apskritis,595689
PanevÄ—Å¾ys,Lithuania,PanevÄ—Å¾ys,596128
Palanga,Lithuania,KlaipÄ—dos apskritis,596238
FabijoniÅ¡kÄ—s,Lithuania,Vilnius County,596479
Mazeikiai,Lithuania,TelÅ¡iÅ³ apskritis,597188
MarijampolÄ—,Lithuania,MarijampolÄ—s apskritis,597231
Kretinga,Lithuania,KlaipÄ—dos apskritis,597989
KlaipÄ—da,Lithuania,KlaipÄ—dos apskritis,598098
KÄ—dainiai,Lithuania,Kauno apskritis,598272
Kaunas,Lithuania,Kauno apskritis,598316
Jonava,Lithuania,Kauno apskritis,598818
GargÅ¾dai,Lithuania,KlaipÄ—dos apskritis,599506
Druskininkai,Lithuania,Alytaus apskritis,599757
Alytus,Lithuania,Alytaus apskritis,601084
Aleksotas,Lithuania,Kauno apskritis,601138
Dainava (Kaunas),Lithuania,Kauno apskritis,6618486
Å ilainiai,Lithuania,Kauno apskritis,9610004
Eiguliai,Lithuania,Kauno apskritis,9610008
PaÅ¡ilaiÄiai,Lithuania,Vilnius County,10062599
PilaitÄ—,Lithuania,Vilnius County,10062600
JustiniÅ¡kÄ—s,Lithuania,Vilnius County,10062601
Å eÅ¡kinÄ—,Lithuania,Vilnius County,10062602
Lazdynai,Lithuania,Vilnius County,10062605
VilkpÄ—dÄ—,Lithuania,Vilnius County,10062606
Naujamiestis,Lithuania,Vilnius County,10062607
Luxembourg,Luxembourg,Luxembourg,2960316
Esch-sur-Alzette,Luxembourg,Luxembourg,2960596
Dudelange,Luxembourg,Luxembourg,2960634
Valmiera,Latvia,Valmieras Rajons,453754
Ventspils,Latvia,Ventspils,454310
Vec-LiepÄja,Latvia,LiepÄja,454432
Tukums,Latvia,Tukuma Rajons,454768
Salaspils,Latvia,Salaspils,455898
Riga,Latvia,Riga,456172
RÄ“zekne,Latvia,RÄ“zekne,456202
Ogre,Latvia,Ogre,457065
LiepÄja,Latvia,LiepÄja,457954
JÅ«rmala,Latvia,JÅ«rmala,459201
Jelgava,Latvia,Jelgava,459279
JÄ“kabpils,Latvia,JÄ“kabpils Municipality,459283
Daugavpils,Latvia,Daugavpils municipality,460413
CÄ“sis,Latvia,CÄ“su Rajons,460570
Tobruk,Libya,Shaâ€˜bÄ«yat al BuÅ£nÄn,81302
SulÅ«q,Libya,BanghÄzÄ«,81604
Darnah,Libya,Darnah,87205
Benghazi,Libya,BanghÄzÄ«,88319
Az ZuwaytÄ«nah,Libya,Shaâ€˜bÄ«yat al WÄá¸©Ät,88380
At TÄj,Libya,Al Kufrah,88562
TÅ«krah,Libya,Al Marj,88834
Al Qubbah,Libya,Darnah,88835
Al Marj,Libya,Al Marj,88903
Al Jawf,Libya,Al Kufrah,88962
Al Bayá¸‘Äâ€™,Libya,Al Jabal al Akhá¸‘ar,89055
Al AbyÄr,Libya,Al Marj,89087
Ajdabiya,Libya,Shaâ€˜bÄ«yat al WÄá¸©Ät,89113
ZuwÄrah,Libya,An NuqÄÅ£ al Khams,2208425
Zliten,Libya,MiÅŸrÄtah,2208485
ZalÅ£an,Libya,An NuqÄÅ£ al Khams,2208655
Yafran,Libya,Shaâ€˜bÄ«yat al Jabal al GharbÄ«,2208791
WaddÄn,Libya,Al Jufrah,2209055
Tarhuna,Libya,Al Marqab,2210221
Tripoli,Libya,Tripoli,2210247
Tagiura,Libya,Tripoli,2210394
Sirte,Libya,Surt,2210554
ÅžurmÄn,Libya,Az ZÄwiyah,2210560
ÅžabrÄtah,Libya,Az ZÄwiyah,2212771
SabhÄ,Libya,SabhÄ,2212775
NÄlÅ«t,Libya,Shaâ€˜bÄ«yat NÄlÅ«t,2214433
Murzuq,Libya,Murzuq,2214603
Mizdah,Libya,Shaâ€˜bÄ«yat al Jabal al GharbÄ«,2214827
MiÅŸrÄtah,Libya,MiÅŸrÄtah,2214846
MasallÄtah,Libya,Al Marqab,2215163
HÅ«n,Libya,Al Jufrah,2216645
Zawiya,Libya,Az ZÄwiyah,2216885
Ghat,Libya,Shaâ€˜bÄ«yat GhÄt,2217351
Gharyan,Libya,Shaâ€˜bÄ«yat al Jabal al GharbÄ«,2217362
Brak,Libya,Ash ShÄÅ£iÊ¼,2218478
BanÄ« WalÄ«d,Libya,MiÅŸrÄtah,2218840
Az ZintÄn,Libya,Shaâ€˜bÄ«yat al Jabal al GharbÄ«,2218963
Az ZÄwÄ«yah,Libya,Az ZÄwiyah,2218970
AwbÄrÄ«,Libya,Shaâ€˜bÄ«yat WÄdÄ« al á¸¨ayÄt,2219235
Al Khums,Libya,Al Marqab,2219905
Al JadÄ«d,Libya,SabhÄ,2219960
ZaÃ¯o,Morocco,Oriental,2526435
Zagora,Morocco,Souss-Massa-DrÃ¢a,2526452
Youssoufia,Morocco,Doukkala-Abda,2526488
Tiznit,Morocco,Souss-Massa-DrÃ¢a,2527089
TirhanimÃ®ne,Morocco,Taza-Al Hoceima-Taounate,2527645
Tinghir,Morocco,Souss-Massa-DrÃ¢a,2527915
Tiflet,Morocco,Rabat-SalÃ©-Zemmour-ZaÃ«r,2528659
TÃ©touan,Morocco,Tanger-TÃ©touan,2528910
Taza,Morocco,Taza-Al Hoceima-Taounate,2529317
Taroudant,Morocco,Souss-Massa-DrÃ¢a,2529649
Taourirt,Morocco,Oriental,2530048
Taounate,Morocco,Taza-Al Hoceima-Taounate,2530155
Tan-Tan,Morocco,Guelmim-Es Smara,2530241
Tangier,Morocco,Tanger-TÃ©touan,2530335
Tahla,Morocco,Taza-Al Hoceima-Taounate,2531480
Souq Larbâ€™a al Gharb,Morocco,Gharb-Chrarda-Beni Hssen,2532394
Sidi Yahia El Gharb,Morocco,Gharb-Chrarda-Beni Hssen,2532822
Sidi Slimane,Morocco,Gharb-Chrarda-Beni Hssen,2532945
Sidi Qacem,Morocco,Gharb-Chrarda-Beni Hssen,2533191
Sidi Ifni,Morocco,Souss-Massa-DrÃ¢a,2534515
Sidi Bennour,Morocco,Doukkala-Abda,2536074
Settat,Morocco,Chaouia-Ouardigha,2537406
Sefrou,Morocco,FÃ¨s-Boulemane,2537545
Sale,Morocco,Rabat-SalÃ©-Zemmour-ZaÃ«r,2537763
Safi,Morocco,Doukkala-Abda,2537881
Rabat,Morocco,Rabat-SalÃ©-Zemmour-ZaÃ«r,2538475
Oulad TeÃ¯ma,Morocco,Souss-Massa-DrÃ¢a,2539134
Oujda,Morocco,Oriental,2540483
Oued Zem,Morocco,Chaouia-Ouardigha,2540689
Ouezzane,Morocco,Gharb-Chrarda-Beni Hssen,2540810
Ouarzazat,Morocco,Souss-Massa-DrÃ¢a,2540850
Nador,Morocco,Oriental,2541479
Mohammedia,Morocco,Grand Casablanca,2542051
Midelt,Morocco,MeknÃ¨s-Tafilalet,2542227
MeknÃ¨s,Morocco,MeknÃ¨s-Tafilalet,2542715
Mechraa Bel Ksiri,Morocco,Gharb-Chrarda-Beni Hssen,2542866
Martil,Morocco,Tanger-TÃ©touan,2542987
Marrakesh,Morocco,Marrakech-Tensift-Al Haouz,2542997
Larache,Morocco,Tanger-TÃ©touan,2543549
Ksar El Kebir,Morocco,Tanger-TÃ©touan,2544001
Khouribga,Morocco,Chaouia-Ouardigha,2544248
Khenifra,Morocco,MeknÃ¨s-Tafilalet,2544333
Kenitra,Morocco,Gharb-Chrarda-Beni Hssen,2544571
Kasba Tadla,Morocco,Tadla-Azilal,2544720
Jerada,Morocco,Oriental,2545017
ImzoÃ»rene,Morocco,Taza-Al Hoceima-Taounate,2545985
Guercif,Morocco,Taza-Al Hoceima-Taounate,2548489
Guelmim,Morocco,Guelmim-Es Smara,2548526
Fkih Ben Salah,Morocco,Tadla-Azilal,2548830
FÃ¨s al Bali,Morocco,FÃ¨s-Boulemane,2548880
Fes,Morocco,FÃ¨s-Boulemane,2548885
Essaouira,Morocco,Marrakech-Tensift-Al Haouz,2549263
El Jadida,Morocco,Doukkala-Abda,2550078
El Hajeb,Morocco,MeknÃ¨s-Tafilalet,2550252
El AÃ¯oun,Morocco,Oriental,2550806
Chefchaouene,Morocco,Tanger-TÃ©touan,2553455
Casablanca,Morocco,Grand Casablanca,2553604
Bouznika,Morocco,Chaouia-Ouardigha,2553751
Berkane,Morocco,Oriental,2555467
Beni Mellal,Morocco,Tadla-Azilal,2555745
Berrechid,Morocco,Chaouia-Ouardigha,2556272
Azrou,Morocco,MeknÃ¨s-Tafilalet,2556464
Azemmour,Morocco,Doukkala-Abda,2556657
Asilah,Morocco,Tanger-TÃ©touan,2557055
Khemisset,Morocco,Rabat-SalÃ©-Zemmour-ZaÃ«r,2558470
Al HoceÃ¯ma,Morocco,Taza-Al Hoceima-Taounate,2558545
Ahfir,Morocco,Oriental,2561124
Agadir,Morocco,Souss-Massa-DrÃ¢a,2561668
Skhirate,Morocco,Rabat-SalÃ©-Zemmour-ZaÃ«r,2562055
Boujniba,Morocco,Chaouia-Ouardigha,6546693
Dakhla,Morocco,Oued ed Dahab-Lagouira,8542188
Monte-Carlo,Monaco,,2992741
Monaco,Monaco,,2993458
EdineÅ£,Moldova,Raionul EdineÅ£,617076
Ungheni,Moldova,Ungheni,617180
Tiraspolul,Moldova,StÃ®nga Nistrului,617239
StraÅŸeni,Moldova,StrÄƒÈ™eni,617302
Bilicenii Vechi,Moldova,SÃ®ngerei,617345
Soroca,Moldova,Raionul Soroca,617367
Slobozia,Moldova,StÃ®nga Nistrului,617381
RÃ®bniÅ£a,Moldova,StÃ®nga Nistrului,617486
Orhei,Moldova,Orhei,617638
HÃ®nceÅŸti,Moldova,HÃ®nceÅŸti,617993
CÄƒuÅŸeni,Moldova,CÄƒuÅŸeni,618120
FloreÅŸti,Moldova,FloreÅŸti,618329
DubÄƒsari,Moldova,TeleneÅŸti,618365
Drochia,Moldova,Drochia,618370
Comrat,Moldova,GÄƒgÄƒuzia,618405
ChiÅŸinÄƒu,Moldova,ChiÅŸinÄƒu,618426
CeadÃ®r-Lunga,Moldova,GÄƒgÄƒuzia,618450
Cahul,Moldova,Cahul,618456
Bender,Moldova,Bender,618577
BÄƒlÅ£i,Moldova,BÄƒlÅ£i,618605
Podgorica,Montenegro,Podgorica,3193044
Pljevlja,Montenegro,Pljevlja,3193161
NikÅ¡iÄ‡,Montenegro,OpÅ¡tina NikÅ¡iÄ‡,3194494
Herceg-Novi,Montenegro,Herceg Novi,3199394
Cetinje,Montenegro,Cetinje,3202641
Budva,Montenegro,Budva,3203106
Bijelo Polje,Montenegro,Bijelo Polje,3204176
Bar,Montenegro,Bar,3204509
Marigot,Saint Martin,N/A,3578851
Toamasina,Madagascar,Atsinanana,1053384
Vondrozo,Madagascar,Atsimo-Atsinanana,1053507
Vohipaho,Madagascar,Atsimo-Atsinanana,1053778
Vohibinany,Madagascar,Atsinanana,1054035
Vavatenina,Madagascar,Analanjirofo,1054192
Vangaindrano,Madagascar,Atsimo-Atsinanana,1054329
Tsiroanomandidy,Madagascar,Bongolava,1054463
Tsiombe,Madagascar,Androy,1054500
Tsaratanana,Madagascar,Betsiboka,1055059
Toliara,Madagascar,Atsimo-Andrefana,1055429
Fort Dauphin,Madagascar,Anosy,1055433
Soavinandriana,Madagascar,Itasy,1056151
Soanindrariny,Madagascar,Vakinankaratra,1056381
Soanierana Ivongo,Madagascar,Analanjirofo,1056386
Sitampiky,Madagascar,Boeny,1056531
Sambava,Madagascar,Sava,1056899
Sakaraha,Madagascar,Atsimo-Andrefana,1057095
Sahavato,Madagascar,Vatovavy Fitovinany,1057277
Sadabe,Madagascar,Analamanga,1057688
Nosy Varika,Madagascar,Vatovavy Fitovinany,1058080
Morondava,Madagascar,Menabe,1058381
Moramanga,Madagascar,Alaotra Mangoro,1058532
Miandrivazo,Madagascar,Menabe,1059051
Miandrarivo,Madagascar,Vakinankaratra,1059059
Marovoay,Madagascar,Boeny,1059507
Marolambo,Madagascar,Atsinanana,1060007
Maroantsetra,Madagascar,Analanjirofo,1060283
Manjakandriana,Madagascar,Analamanga,1060673
Mananjary,Madagascar,Vatovavy Fitovinany,1061335
Mananara,Madagascar,Analanjirofo,1061412
Manakara,Madagascar,Vatovavy Fitovinany,1061605
Maintirano,Madagascar,Melaky,1061912
Mahanoro,Madagascar,Atsinanana,1062553
Mahajanga,Madagascar,Boeny,1062663
Maevatanana,Madagascar,Betsiboka,1062842
Ikongo,Madagascar,Vatovavy Fitovinany,1064234
Ikalamavony,Madagascar,Upper Matsiatra,1064258
Ihosy,Madagascar,Ihorombe,1064275
Ifanadiana,Madagascar,Vatovavy Fitovinany,1064366
Fianarantsoa,Madagascar,Upper Matsiatra,1064890
Fenoarivo Be,Madagascar,Bongolava,1064978
Fenoarivo Atsinanana,Madagascar,Analanjirofo,1064980
Faratsiho,Madagascar,Vakinankaratra,1065140
Farafangana,Madagascar,Atsimo-Atsinanana,1065158
Fandriana,Madagascar,Amoron'i Mania,1065222
Betioky,Madagascar,Atsimo-Andrefana,1066310
Betafo,Madagascar,Vakinankaratra,1066514
Beroroha,Madagascar,Atsimo-Andrefana,1066831
Belo sur Tsiribihina,Madagascar,Menabe,1067531
Beloha,Madagascar,Androy,1067565
Bealanana,Madagascar,Sofia,1068670
Arivonimamo,Madagascar,Itasy,1068865
Antsohimbondrona,Madagascar,Diana,1068955
Antsohihy,Madagascar,Sofia,1068971
Antsiranana,Madagascar,Diana,1069129
Antsirabe,Madagascar,Vakinankaratra,1069166
Antanifotsy,Madagascar,Vakinankaratra,1070661
Antananarivo,Madagascar,Analamanga,1070940
Antalaha,Madagascar,Sava,1071296
Ankazondandy,Madagascar,Analamanga,1072711
Ankazobe,Madagascar,Analamanga,1072849
Ankazoabo,Madagascar,Atsimo-Andrefana,1072879
Anjozorobe,Madagascar,Analamanga,1073482
Hell-Ville,Madagascar,Diana,1076105
Andilamena,Madagascar,Alaotra Mangoro,1076194
Andapa,Madagascar,Sava,1076454
Ampasimanolotra,Madagascar,Atsinanana,1078171
Amparafaravola,Madagascar,Alaotra Mangoro,1078446
Ampanihy,Madagascar,Atsimo-Andrefana,1078553
Ampahana,Madagascar,Sava,1078966
Ambovombe,Madagascar,Androy,1079048
Ambositra,Madagascar,Amoron'i Mania,1079088
Ambohitrolomahitsy,Madagascar,Analamanga,1079777
Amboasary,Madagascar,Anosy,1081790
Amboanjo,Madagascar,Vatovavy Fitovinany,1081863
Ambilobe,Madagascar,Diana,1082243
Ambatondrazaka,Madagascar,Alaotra Mangoro,1082639
Ambatolampy,Madagascar,Vakinankaratra,1082992
Ambatofinandrahana,Madagascar,Amoron'i Mania,1083239
Ambato Boeny,Madagascar,Boeny,1083257
Ambarakaraka,Madagascar,Diana,1083676
Ambanja,Madagascar,Diana,1083724
Ambalavao,Madagascar,Upper Matsiatra,1083968
Alarobia,Madagascar,Analamanga,1084740
Majuro,Marshall Islands,Majuro Atoll,2113779
RMI Capitol,Marshall Islands,Majuro Atoll,7874852
Ð–ÐµÐ»Ð¸Ð½Ð¾,Macedonia,Å½elino,783926
Vinica,Macedonia,Vinica,784424
Veles,Macedonia,Veles,785058
Tetovo,Macedonia,Tetovo,785082
Ð¢ÐµÐ°Ñ€Ñ†Ðµ,Macedonia,Tearce,785113
Ð¡Ñ‚ÑƒÐ´ÐµÐ½Ð¸Ñ‡Ð°Ð½Ð¸,Macedonia,StudeniÄani,785345
Strumica,Macedonia,Strumica,785380
Struga,Macedonia,Struga,785387
Shtip,Macedonia,Å tip,785482
Skopje,Macedonia,KarpoÅ¡,785842
Ð¡Ð°Ñ€Ð°Ñ˜,Macedonia,Saraj,786093
Ð ÐµÑÐµÐ½,Macedonia,Resen,786341
Ð Ð°Ð´Ð¾Ð²Ð¸Ñˆ,Macedonia,RadoviÅ¡,786565
Prilep,Macedonia,Prilep,786735
Ohrid,Macedonia,Ohrid,787487
ÐÐµÐ³Ð¾Ñ‚Ð¸Ð½Ð¾,Macedonia,VrapÄiÅ¡te,787715
Negotino,Macedonia,Negotino,787716
Ð›Ð¸Ð¿ÐºÐ¾Ð²Ð¾,Macedonia,Opstina Lipkovo,788654
Kumanovo,Macedonia,Kumanovo,788886
ÐšÑ€Ð¸Ð²Ð° ÐŸÐ°Ð»Ð°Ð½ÐºÐ°,Macedonia,Kriva Palanka,789045
Kochani,Macedonia,KoÄani,789403
KiÄevo,Macedonia,KiÄevo,789527
Kavadarci,Macedonia,Kavadarci,789541
Kamenjane,Macedonia,Bogovinje,789611
Gostivar,Macedonia,Gostivar,790295
Gevgelija,Macedonia,Gevgelija,790744
Delcevo,Macedonia,DelÄevo,791559
Debar,Macedonia,Debar,791606
Brvenica,Macedonia,Brvenica,792227
Bogovinje,Macedonia,Bogovinje,792501
Bitola,Macedonia,Bitola,792578
Å uto Orizare,Macedonia,Å uto Orizari,833258
Butel,Macedonia,Butel,833260
ÄŒair,Macedonia,ÄŒair,833262
Ilinden,Macedonia,Ilinden,833357
Kisela Voda,Macedonia,Kisela Voda,863675
Centar Å½upa,Macedonia,Centar Å½upa,7886881
Yorosso,Mali,Sikasso,2448442
Timbuktu,Mali,Tombouctou,2449067
Sikasso,Mali,Sikasso,2451185
SÃ©gou,Mali,SÃ©gou,2451478
San,Mali,SÃ©gou,2451778
Sagalo,Mali,Kayes,2451935
Mopti,Mali,Mopti,2453348
Markala,Mali,SÃ©gou,2453662
Koutiala,Mali,Sikasso,2454268
Koulikoro,Mali,Koulikoro,2454530
Kolokani,Mali,Koulikoro,2454955
Kayes,Mali,Kayes,2455518
Kati,Mali,Koulikoro,2455558
Kangaba,Mali,Koulikoro,2455735
Gao,Mali,Gao,2457163
DjÃ©nnÃ©,Mali,Mopti,2458589
Bougouni,Mali,Sikasso,2459775
Banamba,Mali,Koulikoro,2460546
Bamako,Mali,Bamako,2460596
BafoulabÃ©,Mali,Kayes,2460755
Yenangyaung,Myanmar,Magway,1285173
Nyaungdon,Myanmar,Ayeyarwady,1285871
Yamethin,Myanmar,Mandalay,1285899
Wakema,Myanmar,Ayeyarwady,1289828
Twante,Myanmar,Yangon,1290374
Taungoo,Myanmar,Bago,1290596
Thongwa,Myanmar,Yangon,1291193
Thayetmyo,Myanmar,Magway,1292037
Thaton,Myanmar,Mon,1292288
Tharyarwady,Myanmar,Bago,1292313
Thanatpin,Myanmar,Bago,1292579
Thanatpin,Myanmar,Bago,1292580
Dawei,Myanmar,Tanintharyi,1293625
Taunggyi,Myanmar,Shan,1293960
Taungdwingyi,Myanmar,Magway,1294041
Syriam,Myanmar,Yangon,1295395
Sittwe,Myanmar,Rakhine,1295765
Shwebo,Myanmar,Sagain,1296736
Sagaing,Myanmar,Sagain,1298482
Yangon,Myanmar,Yangon,1298824
Pyu,Myanmar,Bago,1298911
Pyinmana,Myanmar,Mandalay,1298987
Pyay,Myanmar,Bago,1299154
Pyapon,Myanmar,Ayeyarwady,1299237
Bago,Myanmar,Bago,1300466
Paungde,Myanmar,Bago,1300969
Pakokku,Myanmar,Magway,1302439
Hpa-an,Myanmar,Kayin,1302849
Nyaunglebin,Myanmar,Bago,1303406
Myitkyina,Myanmar,Kachin,1307741
Myingyan,Myanmar,Mandalay,1307835
Myawadi,Myanmar,Kayin,1308052
Myanaung,Myanmar,Ayeyarwady,1308204
Mudon,Myanmar,Mon,1308415
Mawlamyinegyunn,Myanmar,Ayeyarwady,1308464
Mawlamyine,Myanmar,Mon,1308465
Monywa,Myanmar,Sagain,1308522
Mogok,Myanmar,Mandalay,1308937
Minbu,Myanmar,Magway,1309289
Myeik,Myanmar,Tanintharyi,1309611
Meiktila,Myanmar,Mandalay,1309793
Pyin Oo Lwin,Myanmar,Mandalay,1309937
Mawlaik,Myanmar,Sagain,1310120
Maubin,Myanmar,Ayeyarwady,1310362
Martaban,Myanmar,Mon,1310460
Mandalay,Myanmar,Mandalay,1311874
Magway,Myanmar,Magway,1312609
Loikaw,Myanmar,Kayah,1313479
Letpandan,Myanmar,Bago,1314042
Lashio,Myanmar,Shan,1314759
Kyaukse,Myanmar,Mandalay,1316703
Kyaikto,Myanmar,Mon,1317375
Kyaiklat,Myanmar,Ayeyarwady,1317397
Kyaikkami,Myanmar,Mon,1317402
Kayan,Myanmar,Yangon,1319533
Kanbe,Myanmar,Yangon,1320944
Hinthada,Myanmar,Ayeyarwady,1325211
Hakha,Myanmar,Chin,1325443
Chauk,Myanmar,Magway,1327659
Bogale,Myanmar,Ayeyarwady,1328121
Bhamo,Myanmar,Kachin,1328218
Pathein,Myanmar,Ayeyarwady,1328421
Myaydo,Myanmar,Magway,1329239
Nay Pyi Taw,Myanmar,Mandalay,6611854
Uliastay,Mongolia,Dzabkhan,1515007
Ulaangom,Mongolia,Uvs,1515029
Ã–lgiy,Mongolia,Bayan-Ã–lgiy,1515436
Khovd,Mongolia,Hovd,1516048
Altai,Mongolia,GovÄ­-Altay,1516393
Ulan Bator,Mongolia,Ulaanbaatar,2028462
SÃ¼hbaatar,Mongolia,Selenge,2029156
Murun-kuren,Mongolia,HÃ¶vsgÃ¶l,2029945
Mandalgovi,Mongolia,Middle GovÄ­,2030065
Hovd,Mongolia,Ã–vÃ¶rhangay,2030474
Erdenet,Mongolia,Orhon,2031405
DzÃ¼Ã¼nharaa,Mongolia,Selenge,2031533
Darhan,Mongolia,Darhan Uul,2031964
Dalandzadgad,Mongolia,Ã–mnÃ¶govÄ­,2032007
Saynshand,Mongolia,East Gobi Aymag,2032081
Bulgan,Mongolia,Bulgan,2032201
Bayanhongor,Mongolia,Bayanhongor,2032532
Bayanhongor,Mongolia,Bayanhongor,2032533
Baruun-Urt,Mongolia,SÃ¼hbaatar,2032614
Arvayheer,Mongolia,Ã–vÃ¶rhangay,2032814
Ð—ÑƒÑƒÐ½Ð¼Ð¾Ð´,Mongolia,Central Aimak,7648817
Macau,Macao,Macau,1821274
Saipan,Northern Mariana Islands,Saipan,7828758
Saint-Joseph,Martinique,Martinique,3569915
Sainte-Marie,Martinique,Martinique,3569926
Petite RiviÃ¨re SalÃ©e,Martinique,Martinique,3570166
Le Robert,Martinique,Martinique,3570412
Le Lamentin,Martinique,Martinique,3570428
Le FranÃ§ois,Martinique,Martinique,3570429
La TrinitÃ©,Martinique,Martinique,3570446
Fort-de-France,Martinique,Martinique,3570675
Ducos,Martinique,Martinique,3570785
Zouerate,Mauritania,Tiris Zemmour,2375558
TÃ©kane,Mauritania,Trarza,2376189
SÃ©libaby,Mauritania,Guidimaka,2376719
Rosso,Mauritania,Trarza,2376898
Nouakchott,Mauritania,Nouakchott,2377450
NouÃ¢dhibou,Mauritania,Dakhlet Nouadhibou,2377457
NÃ©ma,Mauritania,Hodh ech Chargui,2377539
Kiffa,Mauritania,Assaba,2378538
KaÃ©di,Mauritania,Gorgol,2378736
Atar,Mauritania,Adrar,2381334
Aleg,Mauritania,Brakna,2381659
Plymouth,Montserrat,Saint Anthony,3578069
Brades,Montserrat,Saint Peter,7266440
Å»abbar,Malta,Ä¦aÅ¼-Å»abbar,2562266
Valletta,Malta,Il-Belt Valletta,2562305
Qormi,Malta,Qormi,2562629
Mosta,Malta,Il-Mosta,2562704
Birkirkara,Malta,Birkirkara,2563191
Vacoas,Mauritius,Plaines Wilhems,933945
Triolet,Mauritius,Pamplemousses,933959
Saint Pierre,Mauritius,Moka,934032
Quatre Bornes,Mauritius,Plaines Wilhems,934131
Port Louis,Mauritius,Port Louis,934154
MahÃ©bourg,Mauritius,Grand Port,934322
Goodlands,Mauritius,RiviÃ¨re du Rempart,934488
Curepipe,Mauritius,Plaines Wilhems,934570
Centre de Flacq,Mauritius,Flacq,934631
Bel Air RiviÃ¨re SÃ¨che,Mauritius,Flacq,934750
Le Hochet,Mauritius,Pamplemousses,1106809
Male,Maldives,Kaafu Atoll,1282027
Karonga,Malawi,Northern Region,235715
Zomba,Malawi,Southern Region,923295
Salima,Malawi,Central Region,924055
Rumphi,Malawi,Northern Region,924102
Nsanje,Malawi,Southern Region,924572
Nkhotakota,Malawi,Central Region,924705
Mzuzu,Malawi,Northern Region,925475
Mzimba,Malawi,Northern Region,925498
Mulanje,Malawi,Southern Region,925789
Mchinji,Malawi,Central Region,926747
Mangochi,Malawi,Southern Region,927246
Liwonde,Malawi,Southern Region,927834
Lilongwe,Malawi,Central Region,927967
Kasungu,Malawi,Central Region,928534
Dedza,Malawi,Central Region,930025
Blantyre,Malawi,Southern Region,931755
Balaka,Malawi,Southern Region,931865
Gustavo A. Madero,Mexico,Tamaulipas,3482969
San Fernando,Mexico,Tamaulipas,3483197
Zumpango,Mexico,MÃ©xico,3513966
Zumpango del RÃ­o,Mexico,Guerrero,3513967
ZacualtipÃ¡n,Mexico,Hidalgo,3514134
ZacatlÃ¡n,Mexico,Puebla,3514148
Zacatepec,Mexico,Morelos,3514163
Yecapixtla,Mexico,Morelos,3514278
Yautepec,Mexico,Morelos,3514321
Xoxocotla,Mexico,Morelos,3514398
XonacatlÃ¡n,Mexico,Morelos,3514409
Xochitepec,Mexico,Morelos,3514437
Xochimilco,Mexico,Mexico City,3514450
Xicotepec de JuÃ¡rez,Mexico,Puebla,3514510
Xico,Mexico,Veracruz,3514518
San Miguel Xico Viejo,Mexico,MÃ©xico,3514519
Ãlvaro ObregÃ³n,Mexico,Mexico City,3514663
Villahermosa,Mexico,Tabasco,3514670
Gustavo A. Madero,Mexico,Mexico City,3514674
Villa CuauhtÃ©moc Otzolotepec,Mexico,MÃ©xico,3514683
Veracruz,Mexico,Veracruz,3514783
Venustiano Carranza,Mexico,Chiapas,3514785
Valle Hermoso,Mexico,Tamaulipas,3514868
Valladolid,Mexico,YucatÃ¡n,3514876
Uman,Mexico,YucatÃ¡n,3514929
Tuxtla GutiÃ©rrez,Mexico,Chiapas,3515001
Tuxpan de RodrÃ­guez Cano,Mexico,Veracruz,3515011
TultitlÃ¡n,Mexico,MÃ©xico,3515042
Tultepec,Mexico,MÃ©xico,3515044
Tulancingo,Mexico,Hidalgo,3515062
Tula de Allende,Mexico,Hidalgo,3515064
Toluca,Mexico,MÃ©xico,3515302
Tlazcalancingo,Mexico,Puebla,3515358
Tlaquiltenango,Mexico,Morelos,3515373
Tlapa de Comonfort,Mexico,Guerrero,3515384
Tlapacoyan,Mexico,Veracruz,3515386
Tlalpan,Mexico,Mexico City,3515428
Tlalnepantla,Mexico,MÃ©xico,3515431
Tlahuac,Mexico,Mexico City,3515463
TizimÃ­n,Mexico,YucatÃ¡n,3515504
Tizayuca,Mexico,Morelos,3515505
Tixtla de Guerrero,Mexico,Guerrero,3515510
Ticul,Mexico,YucatÃ¡n,3515665
Santiago TÃ­anguistenco,Mexico,MÃ©xico,3515679
Tezontepec de Aldama,Mexico,Hidalgo,3515690
Teziutlan,Mexico,Puebla,3515696
Texcoco de Mora,Mexico,MÃ©xico,3515715
Tequixquiac,Mexico,MÃ©xico,3515794
Tequisquiapan,Mexico,QuerÃ©taro,3515796
CuautitlÃ¡n Izcalli,Mexico,MÃ©xico,3515807
TepoztlÃ¡n,Mexico,Morelos,3515811
TepotzotlÃ¡n,Mexico,MÃ©xico,3515827
Tepeji de Ocampo,Mexico,Hidalgo,3515887
Tepeaca,Mexico,Puebla,3515904
Tepatlaxco de Hidalgo,Mexico,Puebla,3515906
Teoloyucan,Mexico,MÃ©xico,3515942
Tenosique de Pino SuÃ¡rez,Mexico,Tabasco,3515956
Tenango de Arista,Mexico,Morelos,3515993
Temixco,Mexico,Morelos,3516035
Temapache,Mexico,Veracruz,3516053
Teloloapan,Mexico,Guerrero,3516060
Tecax,Mexico,YucatÃ¡n,3516076
TehuacÃ¡n,Mexico,Puebla,3516109
Tecamachalco,Mexico,Puebla,3516188
Teapa,Mexico,Tabasco,3516210
Taxco de AlarcÃ³n,Mexico,Guerrero,3516225
Tapachula,Mexico,Chiapas,3516266
Tantoyuca,Mexico,Veracruz,3516271
Tampico,Mexico,Tamaulipas,3516355
Tamazunchale,Mexico,San Luis PotosÃ­,3516385
Santo Domingo Tehuantepec,Mexico,Oaxaca,3516843
Santiago Tuxtla,Mexico,Veracruz,3516912
Santiago Pinotepa Nacional,Mexico,Oaxaca,3516926
Santiago Tulantepec,Mexico,Hidalgo,3516982
Moyotzingo,Mexico,Puebla,3517231
Santa MarÃ­a ChimalhuacÃ¡n,Mexico,MÃ©xico,3517270
Santa Cruz XoxocotlÃ¡n,Mexico,Oaxaca,3517517
Tecamac de Felipe Villanueva,Mexico,Morelos,3517524
Chiautempan,Mexico,Tlaxcala,3517742
San Salvador El Seco,Mexico,Puebla,3517831
San Salvador Atenco,Mexico,MÃ©xico,3517832
San Pablo de las Salinas,Mexico,MÃ©xico,3518135
San Pablo Autopan,Mexico,Morelos,3518138
San Miguel Zinacantepec,Mexico,MÃ©xico,3518221
CoatlinchÃ¡n,Mexico,MÃ©xico,3518277
San Mateo Atenco,Mexico,Morelos,3518387
San Martin Texmelucan de Labastida,Mexico,Puebla,3518407
Teolocholco,Mexico,Tlaxcala,3518475
TeotihuacÃ¡n de Arista,Mexico,Morelos,3518618
San Juan del RÃ­o,Mexico,QuerÃ©taro,3518692
Tuxtepec,Mexico,Oaxaca,3518723
San Francisco Acuautla,Mexico,MÃ©xico,3519290
Sanctorum,Mexico,Puebla,3519531
San CristÃ³bal de las Casas,Mexico,Chiapas,3519537
San Andres Tuxtla,Mexico,Veracruz,3519907
Salina Cruz,Mexico,Oaxaca,3520064
RÃ­o Verde,Mexico,San Luis PotosÃ­,3520235
RÃ­o Bravo,Mexico,Tamaulipas,3520271
RÃ­o Blanco,Mexico,Veracruz,3520274
Reynosa,Mexico,Tamaulipas,3520339
Puerto Escondido,Mexico,Oaxaca,3520994
Puente de Ixtla,Mexico,Morelos,3521051
Puebla,Mexico,Puebla,3521081
Progreso de Alvaro Obregon,Mexico,Hidalgo,3521103
Progreso de Castro,Mexico,YucatÃ¡n,3521108
Poza Rica de Hidalgo,Mexico,Veracruz,3521168
Polanco,Mexico,Mexico City,3521305
Playa del Carmen,Mexico,Quintana Roo,3521342
Pijijiapan,Mexico,Chiapas,3521476
Peto,Mexico,YucatÃ¡n,3521596
Perote,Mexico,Veracruz,3521628
Paraiso,Mexico,Tabasco,3521912
Papantla de Olarte,Mexico,Veracruz,3521922
PÃ¡nuco,Mexico,Veracruz,3521941
Palmarito TochapÃ¡n,Mexico,Puebla,3522118
Palenque,Mexico,Chiapas,3522164
Pachuca de Soto,Mexico,Hidalgo,3522210
Ozumba de Alzate,Mexico,MÃ©xico,3522232
Oxkutzkab,Mexico,YucatÃ¡n,3522251
Orizaba,Mexico,Veracruz,3522307
Ometepec,Mexico,Guerrero,3522343
Ocozocoautla de Espinosa,Mexico,Chiapas,3522444
Ocoyoacac,Mexico,Morelos,3522445
Ocosingo,Mexico,Chiapas,3522484
Oaxaca de JuÃ¡rez,Mexico,Oaxaca,3522507
Nuevo Laredo,Mexico,Tamaulipas,3522551
Nogales,Mexico,Veracruz,3522696
NicolÃ¡s Romero,Mexico,MÃ©xico,3522732
Naucalpan de JuÃ¡rez,Mexico,MÃ©xico,3522790
Naranjos,Mexico,Veracruz,3522804
Villa Nanchital,Mexico,Veracruz,3522845
Motul,Mexico,YucatÃ¡n,3522924
Motozintla,Mexico,Chiapas,3522926
Montemorelos,Mexico,Nuevo LeÃ³n,3523011
Santiago Momoxpan,Mexico,Puebla,3523061
Mixquiahuala de Juarez,Mexico,Hidalgo,3523127
Misantla,Mexico,Veracruz,3523141
Miramar,Mexico,Tamaulipas,3523149
Minatitlan,Mexico,Veracruz,3523183
Milpa Alta,Mexico,Mexico City,3523202
MiahuatlÃ¡n de Porfirio DÃ­az,Mexico,Oaxaca,3523240
Metepec,Mexico,Morelos,3523303
MÃ©rida,Mexico,YucatÃ¡n,3523349
MatÃ­as Romero,Mexico,Oaxaca,3523450
Heroica Matamoros,Mexico,Tamaulipas,3523466
MartÃ­nez de la Torre,Mexico,Veracruz,3523513
Mapastepec,Mexico,Chiapas,3523590
Malinaltepec,Mexico,Guerrero,3523683
Magdalena Contreras,Mexico,Mexico City,3523760
Macuspana,Mexico,Tabasco,3523791
Reyes Acozac,Mexico,Morelos,3523900
Los Reyes La Paz,Mexico,MÃ©xico,3523908
Linares,Mexico,Nuevo LeÃ³n,3524348
Lerma de Villada,Mexico,Morelos,3524389
Lerdo de Tejada,Mexico,Veracruz,3524391
Las Margaritas,Mexico,Chiapas,3524744
Las Choapas,Mexico,Veracruz,3524903
La Isla,Mexico,Veracruz,3525596
KanasÃ­n,Mexico,YucatÃ¡n,3526323
JuchitÃ¡n de Zaragoza,Mexico,Oaxaca,3526357
Jojutla,Mexico,Morelos,3526467
Jiutepec,Mexico,Morelos,3526485
Jalpa de MÃ©ndez,Mexico,Tabasco,3526603
Xalapa de EnrÃ­quez,Mexico,Veracruz,3526617
IzÃºcar de Matamoros,Mexico,Puebla,3526657
San JerÃ³nimo Ixtepec,Mexico,Oaxaca,3526674
Ixtapan de la Sal,Mexico,MÃ©xico,3526681
Ixtapaluca,Mexico,MÃ©xico,3526682
Iztapalapa,Mexico,Mexico City,3526683
Ixtac ZoquitlÃ¡n,Mexico,Veracruz,3526696
Iztacalco,Mexico,Mexico City,3526700
Ixmiquilpan,Mexico,Hidalgo,3526708
Iguala de la Independencia,Mexico,Guerrero,3526798
HunucmÃ¡,Mexico,YucatÃ¡n,3526838
Huixtla,Mexico,Chiapas,3526855
Huitzuco de los Figueroa,Mexico,Guerrero,3526864
Huimanguillo,Mexico,Tabasco,3526908
Huejutla de Reyes,Mexico,Hidalgo,3526952
Huejotzingo,Mexico,Puebla,3526953
Huauchinango,Mexico,Puebla,3526992
Huatusco de Chicuellar,Mexico,Veracruz,3526993
Ciudad de Huajuapan de LeÃ³n,Mexico,Oaxaca,3527023
Frontera Comalapa,Mexico,Chiapas,3527542
Frontera,Mexico,Tabasco,3527545
FortÃ­n de las Flores,Mexico,Veracruz,3527596
Felipe Carrillo Puerto,Mexico,Quintana Roo,3527639
EscÃ¡rcega,Mexico,Campeche,3527795
Emiliano Zapata,Mexico,Morelos,3527879
Emiliano Zapata,Mexico,Chiapas,3527880
Ciudad Mante,Mexico,Tamaulipas,3528756
Ecatepec,Mexico,MÃ©xico,3529612
CunduacÃ¡n,Mexico,Tabasco,3529886
Cuernavaca,Mexico,Morelos,3529947
Cuautlancingo,Mexico,Puebla,3529981
Cuautla Morelos,Mexico,Morelos,3529982
CuautitlÃ¡n,Mexico,MÃ©xico,3529986
Cuautepec de Hinojosa,Mexico,Hidalgo,3529989
Cuajimalpa,Mexico,Mexico City,3530049
San Miguel de Cozumel,Mexico,Quintana Roo,3530103
Coyotepec,Mexico,Morelos,3530123
CoyoacÃ¡n,Mexico,Mexico City,3530139
Cosoleacaque,Mexico,Veracruz,3530167
Cosamaloapan de Carpio,Mexico,Veracruz,3530177
CÃ³rdoba,Mexico,Veracruz,3530240
San Bernardino Contla,Mexico,Tlaxcala,3530276
ComitÃ¡n,Mexico,Chiapas,3530367
Comalcalco,Mexico,Tabasco,3530385
Coatzintla,Mexico,Veracruz,3530513
Coatzacoalcos,Mexico,Veracruz,3530517
Coatepec,Mexico,Veracruz,3530531
Coacalco,Mexico,MÃ©xico,3530569
Ciudad Victoria,Mexico,Tamaulipas,3530580
Ciudad Valles,Mexico,San Luis PotosÃ­,3530582
Ciudad SerdÃ¡n,Mexico,Puebla,3530584
Ciudad Sahagun,Mexico,Hidalgo,3530587
Ciudad Nezahualcoyotl,Mexico,MÃ©xico,3530589
Ciudad Miguel AlemÃ¡n,Mexico,Tamaulipas,3530590
Ciudad Mendoza,Mexico,Veracruz,3530592
Ciudad Madero,Mexico,Tamaulipas,3530594
Ciudad FernÃ¡ndez,Mexico,San Luis PotosÃ­,3530596
Mexico City,Mexico,Mexico City,3530597
Ciudad del Carmen,Mexico,Campeche,3530599
Cintalapa de Figueroa,Mexico,Chiapas,3530617
Cholula,Mexico,Puebla,3530757
Chilpancingo de los Bravos,Mexico,Guerrero,3530870
Chilapa de Alvarez,Mexico,Guerrero,3530886
Chignahuapan,Mexico,Puebla,3530908
Chiconcuac,Mexico,MÃ©xico,3530932
San Vicente Chicoloapan,Mexico,MÃ©xico,3530937
ChichÃ©n-ItzÃ¡,Mexico,YucatÃ¡n,3530978
Chiautla,Mexico,MÃ©xico,3531007
Chiapa de Corzo,Mexico,Chiapas,3531013
Chetumal,Mexico,Quintana Roo,3531023
ChampotÃ³n,Mexico,Campeche,3531177
Chalco de DÃ­az Covarrubias,Mexico,MÃ©xico,3531200
Cerro Azul,Mexico,Veracruz,3531321
Catemaco,Mexico,Veracruz,3531416
Carlos A. Carrillo,Mexico,Veracruz,3531556
Cardenas,Mexico,San Luis PotosÃ­,3531574
CÃ¡rdenas,Mexico,Tabasco,3531576
Capulhuac,Mexico,Morelos,3531598
CancÃºn,Mexico,Quintana Roo,3531673
Campeche,Mexico,Campeche,3531732
Calpulalpan,Mexico,Hidalgo,3531784
Cadereyta,Mexico,Nuevo LeÃ³n,3531865
BerriozÃ¡bal,Mexico,Chiapas,3532254
Banderilla,Mexico,Veracruz,3532414
Azcapotzalco,Mexico,Mexico City,3532497
Axochiapan,Mexico,Morelos,3532545
Atlixco,Mexico,Puebla,3532592
Atlacomulco,Mexico,MÃ©xico,3532617
Ciudad LÃ³pez Mateos,Mexico,MÃ©xico,3532624
Apizaco,Mexico,Tlaxcala,3532792
Apan,Mexico,Hidalgo,3532815
Amozoc de Mota,Mexico,Puebla,3532881
Amecameca,Mexico,MÃ©xico,3532899
Heroica Alvarado,Mexico,Veracruz,3532964
Altotonga,Mexico,Veracruz,3532969
Altepexi,Mexico,Puebla,3532989
Altamira,Mexico,Tamaulipas,3533005
Allende,Mexico,Veracruz,3533056
Ãlamo,Mexico,Veracruz,3533107
Ajalpan,Mexico,Puebla,3533126
Agua Dulce,Mexico,Veracruz,3533269
Actopan,Mexico,Hidalgo,3533389
Acayucan,Mexico,Veracruz,3533426
Acatzingo de Hidalgo,Mexico,Puebla,3533433
AcatlÃ¡n de Osorio,Mexico,Puebla,3533440
Acapulco de JuÃ¡rez,Mexico,Guerrero,3533462
Acajete,Mexico,Puebla,3533486
San Antonio de la Cal,Mexico,Oaxaca,3762770
Hidalgo,Mexico,Nuevo LeÃ³n,3792044
RÃ­o de Teapa,Mexico,Tabasco,3802739
Huamantla,Mexico,Tlaxcala,3815324
Zacatelco,Mexico,Tlaxcala,3815392
Tlaxcala de Xicohtencatl,Mexico,Tlaxcala,3815415
Papalotla,Mexico,Tlaxcala,3815447
Vicente Guerrero,Mexico,Tlaxcala,3815453
TonalÃ¡,Mexico,Chiapas,3816721
Arriaga,Mexico,Chiapas,3816739
San AndrÃ©s Cholula,Mexico,Puebla,3818742
Tampico,Mexico,Tamaulipas,3824166
Alto Lucero,Mexico,Veracruz,3824536
San Mateo Otzacatipan,Mexico,Morelos,3827254
Santa MarÃ­a Totoltepec,Mexico,MÃ©xico,3827256
San Lorenzo Acopilco,Mexico,Mexico City,3827403
Benito Juarez,Mexico,Mexico City,3827406
Venustiano Carranza,Mexico,Mexico City,3827407
Miguel Hidalgo,Mexico,Mexico City,3827408
CuauhtÃ©moc,Mexico,Mexico City,3827409
Huixquilucan,Mexico,MÃ©xico,3827414
Melchor Ocampo,Mexico,MÃ©xico,3827586
Huilango,Mexico,MÃ©xico,3827588
Santiago Teyahualco,Mexico,MÃ©xico,3827596
Ojo de Agua,Mexico,MÃ©xico,3827598
Buenavista,Mexico,MÃ©xico,3827606
Miguel AlemÃ¡n (La Doce),Mexico,Sonora,3970972
Leyva Solano,Mexico,Sinaloa,3976775
CihuatlÃ¡n,Mexico,Jalisco,3976999
Guadalupe Victoria,Mexico,Baja California,3979505
Ixtapa-Zihuatanejo,Mexico,Guerrero,3979673
Zapotlanejo,Mexico,Jalisco,3979717
Zapotiltic,Mexico,Jalisco,3979727
Zapopan,Mexico,Jalisco,3979770
Zamora,Mexico,MichoacÃ¡n,3979802
Zacoalco de Torres,Mexico,Jalisco,3979822
Zacatecas,Mexico,Zacatecas,3979844
ZacapÃº,Mexico,MichoacÃ¡n,3979846
Yuriria,Mexico,Guanajuato,3979855
YurÃ©cuaro,Mexico,MichoacÃ¡n,3979856
VillagrÃ¡n,Mexico,Guanajuato,3980174
Ciudad Frontera,Mexico,Coahuila,3980180
GarcÃ­a,Mexico,Nuevo LeÃ³n,3980190
Ciudad de Villa de Ãlvarez,Mexico,Colima,3980194
Valle de Santiago,Mexico,Guanajuato,3980605
Valle de Bravo,Mexico,MÃ©xico,3980621
Uruapan,Mexico,MichoacÃ¡n,3980760
Uriangato,Mexico,Guanajuato,3980777
Tuxpan,Mexico,Jalisco,3980844
Torreon,Mexico,Coahuila,3981254
TonalÃ¡,Mexico,Jalisco,3981369
Tlaquepaque,Mexico,Jalisco,3981461
Tlajomulco de ZÃºÃ±iga,Mexico,Jalisco,3981467
Tijuana,Mexico,Baja California,3981609
TesistÃ¡n,Mexico,Jalisco,3981791
Tequila,Mexico,Jalisco,3981885
Tepic,Mexico,Nayarit,3981941
TepatitlÃ¡n de Morelos,Mexico,Jalisco,3981984
Tepalcatepec,Mexico,MichoacÃ¡n,3982007
Teocaltiche,Mexico,Jalisco,3982034
Tejupilco de Hidalgo,Mexico,MÃ©xico,3982121
Tecoman,Mexico,Colima,3982213
Tecate,Mexico,Baja California,3982266
TangancÃ­cuaro de Arista,Mexico,MÃ©xico,3982545
Tamazula de Gordiano,Mexico,Jalisco,3982567
Tala,Mexico,Jalisco,3982616
TacÃ¡mbaro de Codallos,Mexico,MichoacÃ¡n,3982693
Sombrerete,Mexico,Zacatecas,3982887
Soledad DÃ­ez GutiÃ©rrez,Mexico,San Luis PotosÃ­,3982912
Silao,Mexico,Guanajuato,3983058
Sayula,Mexico,Jalisco,3983216
Santiago Papasquiaro,Mexico,Durango,3983631
Santiago Ixcuintla,Mexico,Nayarit,3983636
Santiago,Mexico,Nuevo LeÃ³n,3983671
Santa Rosa Jauregui,Mexico,QuerÃ©taro,3983820
Santa Catarina,Mexico,Nuevo LeÃ³n,3984583
Santa Anita,Mexico,Jalisco,3984680
San SebastiÃ¡n el Grande,Mexico,Jalisco,3984791
San Pedro,Mexico,Coahuila,3985129
San NicolÃ¡s de los Garza,Mexico,Nuevo LeÃ³n,3985241
San Miguel el Alto,Mexico,Jalisco,3985323
San Miguel de Papasquiaro,Mexico,Durango,3985327
San Miguel de Allende,Mexico,Guanajuato,3985344
San Luis RÃ­o Colorado,Mexico,Sonora,3985604
San Luis PotosÃ­,Mexico,San Luis PotosÃ­,3985606
San Luis de la Paz,Mexico,Guanajuato,3985620
San Luis de la Paz,Mexico,Guerrero,3985621
Cabo San Lucas,Mexico,Baja California Sur,3985710
San Juan de los Lagos,Mexico,Jalisco,3985865
San JosÃ© Iturbide,Mexico,Guanajuato,3986088
San JosÃ© del Cabo,Mexico,Baja California Sur,3986172
San Francisco del RincÃ³n,Mexico,Guanajuato,3986984
San Felipe,Mexico,Baja California,3987224
San Felipe,Mexico,Guanajuato,3987246
San Buenaventura,Mexico,Coahuila,3987500
NicolÃ¡s R Casillas,Mexico,Jalisco,3988025
Salvatierra,Mexico,Guanajuato,3988050
Saltillo,Mexico,Coahuila,3988086
Salamanca,Mexico,Guanajuato,3988214
Sahuayo de Morelos,Mexico,MichoacÃ¡n,3988258
Sabinas Hidalgo,Mexico,Nuevo LeÃ³n,3988327
Ciudad Sabinas,Mexico,Coahuila,3988333
Rosarito,Mexico,Baja California,3988392
Romita,Mexico,Guanajuato,3988462
RÃ­o Grande,Mexico,Zacatecas,3988594
RincÃ³n de Romos,Mexico,Aguascalientes,3988651
Ramos Arizpe,Mexico,Coahuila,3991043
Santiago de QuerÃ©taro,Mexico,QuerÃ©taro,3991164
PuruÃ¡ndiro,Mexico,MÃ©xico,3991219
Puerto Vallarta,Mexico,Jalisco,3991328
Puerto PeÃ±asco,Mexico,Sonora,3991347
Piedras Negras,Mexico,Coahuila,3992619
PetatlÃ¡n,Mexico,Guerrero,3992842
PÃ©njamo,Mexico,Guanajuato,3992986
PÃ¡tzcuaro,Mexico,MichoacÃ¡n,3993179
Parras de la Fuente,Mexico,Coahuila,3993335
Paracho de Verduzco,Mexico,MichoacÃ¡n,3993457
Palau,Mexico,Coahuila,3993893
Ojinaga,Mexico,Chihuahua,3994469
OcotlÃ¡n,Mexico,Jalisco,3994489
Nuevo MÃ©xico,Mexico,Jalisco,3994604
Nuevo Casas Grandes,Mexico,Chihuahua,3994616
Nueva Rosita,Mexico,Coahuila,3994667
Nueva Italia de Ruiz,Mexico,MichoacÃ¡n,3994674
NochistlÃ¡n,Mexico,Zacatecas,3994912
Navolato,Mexico,Sinaloa,3995017
Navojoa,Mexico,Sonora,3995019
Nava,Mexico,Coahuila,3995050
MoroleÃ³n,Mexico,Guanajuato,3995343
Morelia,Mexico,MichoacÃ¡n,3995402
Monterrey,Mexico,Nuevo LeÃ³n,3995465
Monclova,Mexico,Coahuila,3995523
Mexicali,Mexico,Baja California,3996069
Pedro Meoqui,Mexico,Chihuahua,3996234
Melchor MÃºzquiz,Mexico,Coahuila,3996271
Medina,Mexico,Guanajuato,3996299
MazatlÃ¡n,Mexico,Sinaloa,3996322
Matehuala,Mexico,San Luis PotosÃ­,3996387
Matamoros,Mexico,Coahuila,3996426
Marfil,Mexico,Guanajuato,3996595
MaravatÃ­o,Mexico,MichoacÃ¡n,3996626
Manzanillo,Mexico,Colima,3996663
Rodolfo SÃ¡nchez Taboada,Mexico,Baja California,3996737
Magdalena de Kino,Mexico,Sonora,3996893
San Pedro Madera,Mexico,Chihuahua,3996956
Los Mochis,Mexico,Sinaloa,3997479
Loreto,Mexico,Zacatecas,3998291
LeÃ³n,Mexico,Guanajuato,3998655
Las Pintas de Arriba,Mexico,Jalisco,3999325
La Piedad Cavadas,Mexico,MichoacÃ¡n,4000821
La Paz,Mexico,Baja California Sur,4000900
La Orilla,Mexico,MichoacÃ¡n,4001056
Lagos de Moreno,Mexico,Jalisco,4002224
La Cruz,Mexico,Sinaloa,4002745
La Barca,Mexico,Jalisco,4003526
Santa Cruz de Juventino Rosas,Mexico,Guanajuato,4003662
Jocotepec,Mexico,Jalisco,4003908
JiquÃ­lpan de JuÃ¡rez,Mexico,MÃ©xico,4003923
JimÃ©nez,Mexico,Chihuahua,4003938
JesÃºs MarÃ­a,Mexico,Aguascalientes,4003995
Jerez de GarcÃ­a Salinas,Mexico,Zacatecas,4004024
Jaral del Progreso,Mexico,Guanajuato,4004092
Jamay,Mexico,Jalisco,4004126
JalostotitlÃ¡n,Mexico,Jalisco,4004153
IxtlÃ¡n del RÃ­o,Mexico,Nayarit,4004267
Ixtapa,Mexico,Jalisco,4004293
Irapuato,Mexico,Guanajuato,4004330
Huetamo de NÃºÃ±ez,Mexico,MichoacÃ¡n,4004555
Huatabampo,Mexico,Sonora,4004647
Hidalgo del Parral,Mexico,Chihuahua,4004867
HerÃ³ica ZitÃ¡cuaro,Mexico,MichoacÃ¡n,4004885
Nogales,Mexico,Sonora,4004886
Heroica Caborca,Mexico,Sonora,4004887
Hermosillo,Mexico,Sonora,4004898
Heroica Guaymas,Mexico,Sonora,4005143
Guasave,Mexico,Sinaloa,4005219
Guanajuato,Mexico,Guanajuato,4005270
GuamÃºchil,Mexico,Sinaloa,4005297
Guadalupe,Mexico,Nuevo LeÃ³n,4005492
Guadalupe,Mexico,Zacatecas,4005509
Guadalajara,Mexico,Jalisco,4005539
Gomez Palacio,Mexico,Durango,4005775
Juan Jose Rios,Mexico,Sinaloa,4005864
General Escobedo,Mexico,Nuevo LeÃ³n,4005867
Garza GarcÃ­a,Mexico,Nuevo LeÃ³n,4005937
Fresnillo,Mexico,Zacatecas,4006163
Escuinapa de Hidalgo,Mexico,Sinaloa,4006622
Ensenada,Mexico,Baja California,4006702
EncarnaciÃ³n de DÃ­az,Mexico,Jalisco,4006783
Empalme,Mexico,Sonora,4006806
Pueblo Nuevo,Mexico,Durango,4007676
El Salto,Mexico,Jalisco,4007684
El Pueblito,Mexico,QuerÃ©taro,4008303
El Grullo,Mexico,Jalisco,4009697
Victoria de Durango,Mexico,Durango,4011743
CuliacÃ¡n,Mexico,Sinaloa,4012176
CuauhtÃ©moc,Mexico,Chihuahua,4012406
Villa de Costa Rica,Mexico,Sinaloa,4012693
Cortazar,Mexico,Guanajuato,4012721
Compostela,Mexico,Nayarit,4013085
Comonfort,Mexico,Guanajuato,4013094
Colima,Mexico,Colima,4013516
Ciudad ObregÃ³n,Mexico,Sonora,4013704
Ciudad Lerdo,Mexico,Coahuila,4013706
Ciudad JuÃ¡rez,Mexico,Chihuahua,4013708
Ciudad Hidalgo,Mexico,MichoacÃ¡n,4013712
Ciudad GuzmÃ¡n,Mexico,Jalisco,4013714
Ciudad Delicias,Mexico,Chihuahua,4013720
Ciudad ConstituciÃ³n,Mexico,Baja California Sur,4013723
Ciudad Camargo,Mexico,Chihuahua,4013724
Ciudad AnÃ¡huac,Mexico,Nuevo LeÃ³n,4013726
Ciudad Altamirano,Mexico,Guerrero,4013727
Ciudad AcuÃ±a,Mexico,Coahuila,4013728
Chihuahua,Mexico,Chihuahua,4014338
Chapala,Mexico,Jalisco,4014553
Celaya,Mexico,Guanajuato,4014875
CastaÃ±os,Mexico,Coahuila,4015022
Cananea,Mexico,Sonora,4015700
Villa JuÃ¡rez,Mexico,Sinaloa,4015938
Calvillo,Mexico,Aguascalientes,4016086
VÃ­ctor Rosales,Mexico,Zacatecas,4016132
AutlÃ¡n de Navarro,Mexico,Jalisco,4017957
Atoyac de Ãlvarez,Mexico,Guerrero,4017984
Atotonilco el Alto,Mexico,Jalisco,4017992
Armeria,Mexico,Colima,4018227
Arcelia,Mexico,Guerrero,4018320
Arandas,Mexico,Jalisco,4018348
Apodaca,Mexico,Nuevo LeÃ³n,4018390
ApatzingÃ¡n,Mexico,MichoacÃ¡n,4018400
Apaseo el Grande,Mexico,Guanajuato,4018403
Apaseo el Alto,Mexico,Guanajuato,4018404
Ameca,Mexico,Jalisco,4018582
Allende,Mexico,Coahuila,4018761
Allende,Mexico,Nuevo LeÃ³n,4018762
Aguascalientes,Mexico,Aguascalientes,4019233
Agua Prieta,Mexico,Sonora,4019260
Acaponeta,Mexico,Nayarit,4019819
AcÃ¡mbaro,Mexico,Guanajuato,4019827
Abasolo,Mexico,Guanajuato,4019869
AnÃ¡huac,Mexico,Nuevo LeÃ³n,4022908
Dolores Hidalgo Cuna de la Independencia Nacional,Mexico,Guanajuato,4023117
Guacamayas,Mexico,MichoacÃ¡n,4026075
Ciudad LÃ¡zaro CÃ¡rdenas,Mexico,MichoacÃ¡n,4026082
Colonia del Valle,Mexico,Mexico City,7280708
Colonia Lindavista,Mexico,MÃ©xico,7280711
Colonia Nativitas,Mexico,Mexico City,7280718
Las Delicias,Mexico,Baja California,8599061
San Pedro Garza Garcia,Mexico,Nuevo LeÃ³n,8617692
Soledad de Graciano SÃ¡nchez,Mexico,San Luis PotosÃ­,8858078
Manzanillo,Mexico,Colima,8858079
Naucalpan de JuÃ¡rez,Mexico,MÃ©xico,8858082
Hacienda Santa Fe,Mexico,Jalisco,8858085
Fuentes del Valle,Mexico,MÃ©xico,8858086
San Salvador Tizatlalli,Mexico,MÃ©xico,8858087
Jardines de la Silla (Jardines),Mexico,Nuevo LeÃ³n,8858088
San Buenaventura,Mexico,MÃ©xico,8858089
Colonia Santa Teresa,Mexico,MÃ©xico,8858090
San JerÃ³nimo Cuatro Vientos,Mexico,MÃ©xico,8858091
San MartÃ­n Azcatepec,Mexico,MÃ©xico,8858092
Fraccionamiento Real Palmas,Mexico,Nuevo LeÃ³n,8858093
PÃ³rticos de San Antonio,Mexico,Baja California,8858094
San Isidro,Mexico,MÃ©xico,8858095
Centro Familiar la Soledad,Mexico,Guanajuato,8858096
San JosÃ© Guadalupe Otzacatipan,Mexico,MÃ©xico,8858097
Las Pintitas,Mexico,Jalisco,8858098
Emiliano Zapata,Mexico,MÃ©xico,8858099
San Antonio TecÃ³mitl,Mexico,Mexico City,8858100
Licenciado Benito JuÃ¡rez (Campo Gobierno),Mexico,Sinaloa,8858101
TeotihuacÃ¡n de Arista,Mexico,MÃ©xico,8858102
JesÃºs del Monte,Mexico,MÃ©xico,8858103
San Jorge Pueblo Nuevo,Mexico,MÃ©xico,8858104
Manuel Ojinaga,Mexico,Chihuahua,8858105
Terrazas del Valle,Mexico,Baja California,8858106
La Ermita,Mexico,Guanajuato,8858107
Lomas del Sur,Mexico,Jalisco,8858108
Parque Industrial Ciudad Mitras,Mexico,Nuevo LeÃ³n,8858109
Mitras Poniente,Mexico,Nuevo LeÃ³n,8858110
Villa del Prado 2da SecciÃ³n,Mexico,Baja California,8858111
Tres de Mayo,Mexico,Morelos,8858112
Don Antonio,Mexico,Hidalgo,8858113
Heroica Ciudad de Tlaxiaco,Mexico,Oaxaca,8858114
Ciudad de Huitzuco,Mexico,Guerrero,8858115
Casa Blanca,Mexico,Puebla,8858116
La Providencia Siglo XXI,Mexico,Hidalgo,8858117
AmpliaciÃ³n San Mateo (Colonia Solidaridad),Mexico,MÃ©xico,8858118
Fraccionamiento Ciudad Olmeca,Mexico,Veracruz,8858119
San Rafael Tlanalapan,Mexico,Puebla,8858120
TecÃ¡mac de Felipe Villanueva,Mexico,MÃ©xico,8858121
Venceremos,Mexico,QuerÃ©taro,8858122
Alborada Jaltenco,Mexico,MÃ©xico,8858123
Crucecita,Mexico,Oaxaca,8858124
Padang Mat Sirat,Malaysia,Kedah,1222387
Kuah,Malaysia,Kedah,1222396
Jerantut,Malaysia,Pahang,1732602
Raub,Malaysia,Pahang,1732663
Batu Pahat,Malaysia,Johor,1732687
Parit Raja,Malaysia,Johor,1732698
Pekan Nenas,Malaysia,Johor,1732706
Pontian Kechil,Malaysia,Johor,1732711
Kampung Pasir Gudang Baru,Malaysia,Johor,1732721
Kota Tinggi,Malaysia,Johor,1732738
Taman Senai,Malaysia,Johor,1732741
Kulai,Malaysia,Johor,1732742
Skudai,Malaysia,Johor,1732745
Johor Bahru,Malaysia,Johor,1732752
Kluang,Malaysia,Johor,1732811
Yong Peng,Malaysia,Johor,1732814
Mersing,Malaysia,Johor,1732826
Segamat,Malaysia,Johor,1732846
Tangkak,Malaysia,Johor,1732857
Muar,Malaysia,Johor,1732869
Bakri,Malaysia,Johor,1732871
Labis,Malaysia,Johor,1732877
Kuala Selangor,Malaysia,Selangor,1732891
Batang Berjuntai,Malaysia,Selangor,1732892
Batu Arang,Malaysia,Selangor,1732893
Shah Alam,Malaysia,Selangor,1732903
Klang,Malaysia,Selangor,1732905
Cukai,Malaysia,Terengganu,1732945
Kuala Lipis,Malaysia,Pahang,1733023
Papar,Malaysia,Sabah,1733353
Kota Kinabalu,Malaysia,Sabah,1733432
Donggongon,Malaysia,Sabah,1733438
Putatan,Malaysia,Sabah,1733440
Kinarut,Malaysia,Sabah,1733449
Ranau,Malaysia,Sabah,1733502
Semporna,Malaysia,Sabah,1733697
Victoria,Malaysia,Labuan,1733782
Beaufort,Malaysia,Sabah,1733874
Lahad Datu,Malaysia,Sabah,1733953
Sandakan,Malaysia,Sabah,1734052
Keningau,Malaysia,Sabah,1734098
Tawau,Malaysia,Sabah,1734199
Paka,Malaysia,Terengganu,1734313
Kertih,Malaysia,Terengganu,1734316
Kulim,Malaysia,Kedah,1734393
Bagan Serai,Malaysia,Perak,1734409
Bedong,Malaysia,Kedah,1734439
Simpang Empat,Malaysia,Perak,1734576
Taiping,Malaysia,Perak,1734586
Kuala Kangsar,Malaysia,Perak,1734599
Ipoh,Malaysia,Perak,1734634
Gua Musang,Malaysia,Kelantan,1734651
Kuala Terengganu,Malaysia,Terengganu,1734705
Marang,Malaysia,Terengganu,1734715
Tampin,Malaysia,Negeri Sembilan,1734738
Alor Gajah,Malaysia,Melaka,1734745
Kampung Ayer Keroh,Malaysia,Melaka,1734753
Sungai Udang,Malaysia,Melaka,1734757
Malacca,Malaysia,Melaka,1734759
Banting,Malaysia,Selangor,1734781
Jenjarum,Malaysia,Selangor,1734793
Semenyih,Malaysia,Selangor,1734798
Seremban,Malaysia,Negeri Sembilan,1734810
Port Dickson,Malaysia,Negeri Sembilan,1734815
Sepang,Malaysia,Selangor,1734821
Bahau,Malaysia,Negeri Sembilan,1734839
Kuala Pilah,Malaysia,Negeri Sembilan,1734841
Pekan,Malaysia,Pahang,1734971
Mentekab,Malaysia,Pahang,1735018
Temerluh,Malaysia,Pahang,1735022
Butterworth,Malaysia,Penang,1735076
Perai,Malaysia,Penang,1735077
Bukit Mertajam,Malaysia,Penang,1735079
Nibong Tebal,Malaysia,Penang,1735086
Parit Buntar,Malaysia,Perak,1735089
Tasek Glugor,Malaysia,Penang,1735093
George Town,Malaysia,Penang,1735106
Serendah,Malaysia,Selangor,1735148
Rawang,Malaysia,Selangor,1735150
Petaling Jaya,Malaysia,Selangor,1735158
Kuala Lumpur,Malaysia,Kuala Lumpur,1735161
Sabak Bernam,Malaysia,Selangor,1735195
Sungai Besar,Malaysia,Selangor,1735199
Kuantan,Malaysia,Pahang,1735227
Batu Gajah,Malaysia,Perak,1735268
Kampar,Malaysia,Perak,1735274
Tapah Road,Malaysia,Perak,1735282
Bidur,Malaysia,Perak,1735287
Lumut,Malaysia,Perak,1735450
Teluk Intan,Malaysia,Perak,1735459
Gurun,Malaysia,Kedah,1735485
Sungai Petani,Malaysia,Kedah,1735498
Kepala Batas,Malaysia,Penang,1735506
Tanah Merah,Malaysia,Kelantan,1735553
Kuching,Malaysia,Sarawak,1735634
Simanggang,Malaysia,Sarawak,1735799
Sarikei,Malaysia,Sarawak,1735837
Sibu,Malaysia,Sarawak,1735902
Kangar,Malaysia,Perlis,1736278
Jitra,Malaysia,Kedah,1736302
Kuala Kedah,Malaysia,Kedah,1736305
Alor Setar,Malaysia,Kedah,1736309
Pasir Mas,Malaysia,Kelantan,1736372
Kota Bharu,Malaysia,Kelantan,1736376
Kudat,Malaysia,Sabah,1736458
Kapit,Malaysia,Sarawak,1737185
Bintulu,Malaysia,Sarawak,1737486
Limbang,Malaysia,Sarawak,1737714
Miri,Malaysia,Sarawak,1738050
Ulu Tiram,Malaysia,Johor,1738294
Tanjung Tokong,Malaysia,Penang,1741550
Tanjung Sepat,Malaysia,Selangor,1741562
Permatang Kuching,Malaysia,Penang,1750500
Peringat,Malaysia,Kelantan,1750582
Ladang Seri Kundang,Malaysia,Selangor,1750974
Pantai Remis,Malaysia,Perak,1752256
Kuang,Malaysia,Selangor,1759486
Klebang Besar,Malaysia,Melaka,1761242
Kampung Tanjung Karang,Malaysia,Selangor,1763412
Kampung Sungai Ara,Malaysia,Penang,1764160
Kampung Simpang Renggam,Malaysia,Johor,1764318
Kampong Pangkal Kalong,Malaysia,Kelantan,1766249
Kampong Masjid Tanah,Malaysia,Melaka,1767021
Kampong Kadok,Malaysia,Kelantan,1768664
Kampong Dungun,Malaysia,Perak,1769612
Kampung Bukit Baharu,Malaysia,Melaka,1770351
Kampung Baru Subang,Malaysia,Selangor,1771023
Kampung Baharu Nilai,Malaysia,Negeri Sembilan,1771287
Kampong Baharu Balakong,Malaysia,Selangor,1771304
Kampung Ayer Molek,Malaysia,Melaka,1771485
Bukit Rambai,Malaysia,Melaka,1778290
Bentong Town,Malaysia,Pahang,1779790
Batu Berendam,Malaysia,Melaka,1780890
Putrajaya,Malaysia,Putrajaya,6697380
Bandar Labuan,Malaysia,Sabah,7302815
Subang Jaya,Malaysia,Selangor,8504423
Putra Heights,Malaysia,Selangor,10792382
Pantai Cenang,Malaysia,Perlis,11002069
Xai-Xai,Mozambique,Gaza,1024552
Dondo,Mozambique,Sofala,1024696
Macia,Mozambique,Gaza,1024701
Tete,Mozambique,Tete,1026014
Ressano Garcia,Mozambique,Maputo,1028079
Quelimane,Mozambique,ZambÃ©zia,1028434
Pemba,Mozambique,Cabo Delgado,1028918
Nampula,Mozambique,Nampula,1033356
Nacala,Mozambique,Nampula,1035025
Montepuez,Mozambique,Cabo Delgado,1037125
MocÃ­mboa,Mozambique,Cabo Delgado,1037370
Ilha de MoÃ§ambique,Mozambique,Nampula,1037390
Maxixe,Mozambique,Inhambane,1039536
Matola,Mozambique,Maputo,1039854
Maputo,Mozambique,Maputo City,1040652
Manjacaze,Mozambique,Gaza,1040938
Lichinga,Mozambique,Niassa,1043893
Inhambane,Mozambique,Inhambane,1045114
Cuamba,Mozambique,Niassa,1047660
ChokwÃ©,Mozambique,Gaza,1048364
Chimoio,Mozambique,Manica,1049261
Chibuto,Mozambique,Gaza,1049861
Beira,Mozambique,Sofala,1052373
AntÃ³nio Enes,Mozambique,Nampula,1052944
MutuÃ¡li,Mozambique,Nampula,1088155
Katima Mulilo,Namibia,Zambezi,877178
Windhoek,Namibia,Khomas,3352136
Swakopmund,Namibia,Erongo,3352844
Rundu,Namibia,Kavango East,3353383
Rehoboth,Namibia,Hardap,3353540
Otjiwarongo,Namibia,Otjozondjupa,3353811
Oshakati,Namibia,Oshana,3354021
Okahandja,Namibia,Otjozondjupa,3354898
LÃ¼deritz,Namibia,Karas,3355672
Keetmanshoop,Namibia,Karas,3356264
Grootfontein,Namibia,Otjozondjupa,3357114
Gobabis,Namibia,Omaheke,3357247
Walvis Bay,Namibia,Erongo,3359638
NoumÃ©a,New Caledonia,South Province,2139521
Mont-Dore,New Caledonia,South Province,2140066
DumbÃ©a,New Caledonia,South Province,2141394
Birni N Konni,Niger,Tahoua,2437732
Zinder,Niger,Zinder,2437798
TillabÃ©ri,Niger,TillabÃ©ri,2438678
Tibiri,Niger,Maradi,2438774
Tessaoua,Niger,Maradi,2438823
TÃ©ra,Niger,TillabÃ©ri,2438855
Tanout,Niger,Zinder,2439155
Tahoua,Niger,Tahoua,2439376
Niamey,Niger,Niamey,2440485
Nguigmi,Niger,Diffa,2440495
Mirriah,Niger,Zinder,2440921
Mayahi,Niger,Maradi,2441194
Matamey,Niger,Zinder,2441217
Maradi,Niger,Maradi,2441291
Magaria,Niger,Zinder,2441482
Madaoua,Niger,Tahoua,2441530
IllÃ©la,Niger,Tahoua,2443304
Gaya,Niger,Dosso,2444489
Dosso,Niger,Dosso,2445488
Dogondoutchi,Niger,Dosso,2445553
Diffa,Niger,Diffa,2445704
Dakoro,Niger,Maradi,2446267
Ayorou,Niger,TillabÃ©ri,2447416
Alaghsas,Niger,Agadez,2447938
Agadez,Niger,Agadez,2448085
Kingston,Norfolk Island,N/A,2161314
Zuru,Nigeria,Kebbi,2317548
Zungeru,Nigeria,Niger,2317569
Zaria,Nigeria,Kaduna,2317765
Yola,Nigeria,Adamawa,2318044
Yenagoa,Nigeria,Bayelsa,2318123
Wukari,Nigeria,Taraba,2318921
Wudil,Nigeria,Kano,2318933
Warri,Nigeria,Delta,2319133
Wamba,Nigeria,Nassarawa,2319257
Uyo,Nigeria,Akwa Ibom,2319480
Uromi,Nigeria,Edo,2319668
Umuahia,Nigeria,Abia,2320576
Ughelli,Nigeria,Delta,2320829
Ugep,Nigeria,Cross River,2320831
Uga,Nigeria,Anambra,2320920
Ubiaja,Nigeria,Edo,2321031
Tegina,Nigeria,Niger,2322263
Tambuwal,Nigeria,Sokoto,2322495
Talata Mafara,Nigeria,Zamfara,2322529
Takum,Nigeria,Benue,2322552
Suleja,Nigeria,Niger,2322794
Sokoto,Nigeria,Sokoto,2322911
Soba,Nigeria,Kaduna,2322957
Saki,Nigeria,Oyo,2323390
Shagamu,Nigeria,Ogun,2323411
Sapele,Nigeria,Delta,2323675
Rijau,Nigeria,Niger,2324504
Rano,Nigeria,Kano,2324575
Potiskum,Nigeria,Yobe,2324767
Port Harcourt,Nigeria,Rivers,2324774
Pindiga,Nigeria,Gombe,2324857
Patigi,Nigeria,Kwara,2324960
Pankshin,Nigeria,Plateau,2325060
Ozubulu,Nigeria,Anambra,2325161
Oyo,Nigeria,Oyo,2325200
Oyan,Nigeria,Osun,2325249
Owo,Nigeria,Ondo,2325314
Owerri,Nigeria,Imo,2325330
Otukpa,Nigeria,Benue,2325437
Otan Ayegbaju,Nigeria,Osun,2325506
Osogbo,Nigeria,Osun,2325590
Orita Eruwa,Nigeria,Oyo,2325733
Onitsha,Nigeria,Anambra,2326016
Ondo,Nigeria,Ondo,2326171
Olupona,Nigeria,Osun,2326302
Okuta,Nigeria,Kwara,2326811
Okrika,Nigeria,Rivers,2326899
Okigwe,Nigeria,Imo,2327143
Okene,Nigeria,Kogi,2327220
Oke Mesi,Nigeria,Osun,2327223
Oke Ila,Nigeria,Ekiti,2327233
Ohafia-Ifigh,Nigeria,Abia,2327494
Ogwashi-Uku,Nigeria,Delta,2327513
Oguta,Nigeria,Imo,2327521
Ogoja,Nigeria,Cross River,2327650
Ogaminana,Nigeria,Kogi,2327827
Offa,Nigeria,Kwara,2327879
Ode,Nigeria,Ondo,2328090
Obudu,Nigeria,Cross River,2328151
Obonoma,Nigeria,Rivers,2328185
Numan,Nigeria,Adamawa,2328617
Nsukka,Nigeria,Enugu,2328684
Nnewi,Nigeria,Anambra,2328765
Nkwerre,Nigeria,Imo,2328790
Nkpor,Nigeria,Anambra,2328811
Nguru,Nigeria,Yobe,2328952
Nasarawa,Nigeria,Nassarawa,2329451
Nafada,Nigeria,Gombe,2329562
Mubi,Nigeria,Adamawa,2329821
Moriki,Nigeria,Zamfara,2329920
Monguno,Nigeria,Borno,2329946
Mokwa,Nigeria,Niger,2329981
Modakeke,Nigeria,Osun,2330028
Minna,Nigeria,Niger,2330100
Marte,Nigeria,Borno,2330719
Malumfashi,Nigeria,Katsina,2331005
Makurdi,Nigeria,Benue,2331140
Makoko,Nigeria,Lagos,2331158
Maiduguri,Nigeria,Borno,2331447
Magumeri,Nigeria,Borno,2331528
Lokoja,Nigeria,Kogi,2331939
Lere,Nigeria,Kaduna,2332079
Lapai,Nigeria,Niger,2332249
Lalupon,Nigeria,Oyo,2332357
Lagos,Nigeria,Lagos,2332459
Lafiagi,Nigeria,Kwara,2332504
Lafia,Nigeria,Nassarawa,2332515
Kwale,Nigeria,Delta,2332871
Kumo,Nigeria,Gombe,2333451
Kumagunnam,Nigeria,Yobe,2333490
Kukawa,Nigeria,Borno,2333563
Kuje,Nigeria,Abuja Federal Capital Territory,2333604
Kontagora,Nigeria,Niger,2334008
Kiyawa,Nigeria,Jigawa,2334306
Kisi,Nigeria,Oyo,2334327
Keffi,Nigeria,Nassarawa,2334652
Kaura Namoda,Nigeria,Zamfara,2334756
Katsina-Ala,Nigeria,Benue,2334801
Katsina,Nigeria,Katsina,2334802
Kari,Nigeria,Bauchi,2335015
Kano,Nigeria,Kano,2335204
Kamba,Nigeria,Kebbi,2335333
Kaiama,Nigeria,Kwara,2335596
Kagoro,Nigeria,Kaduna,2335614
Kafanchan,Nigeria,Kaduna,2335713
Kaduna,Nigeria,Kaduna,2335727
Kachia,Nigeria,Kaduna,2335798
Kabba,Nigeria,Kogi,2335843
Jos,Nigeria,Plateau,2335953
Jimeta,Nigeria,Adamawa,2336056
Jega,Nigeria,Kebbi,2336237
Jebba,Nigeria,Kwara,2336251
Jalingo,Nigeria,Taraba,2336589
Iwo,Nigeria,Osun,2336905
Itu,Nigeria,Akwa Ibom,2336985
Isieke,Nigeria,Ebonyi,2337148
Ise-Ekiti,Nigeria,Ekiti,2337207
Isanlu-Itedoijowa,Nigeria,Kogi,2337235
Ipoti,Nigeria,Ekiti,2337352
Iperu,Nigeria,Ogun,2337379
Inisa,Nigeria,Osun,2337490
Ilorin,Nigeria,Kwara,2337639
Ilobu,Nigeria,Osun,2337659
Illela,Nigeria,Sokoto,2337680
Ilesa,Nigeria,Osun,2337704
Ilaro,Nigeria,Ogun,2337759
Ila Orangun,Nigeria,Osun,2337765
Ikot Ekpene,Nigeria,Akwa Ibom,2338106
Ikom,Nigeria,Cross River,2338242
Ikirun,Nigeria,Osun,2338269
Ikire,Nigeria,Osun,2338273
Ikere-Ekiti,Nigeria,Ekiti,2338287
Ikeja,Nigeria,Lagos,2338313
Ijero-Ekiti,Nigeria,Ekiti,2338385
Ijebu-Ode,Nigeria,Ogun,2338400
Ijebu-Jesa,Nigeria,Osun,2338401
Ijebu-Igbo,Nigeria,Ogun,2338403
Ihiala,Nigeria,Anambra,2338497
Igede-Ekiti,Nigeria,Ekiti,2338630
Igbo-Ukwu,Nigeria,Anambra,2338640
Igbor,Nigeria,Benue,2338660
Igbo-Ora,Nigeria,Oyo,2338669
Igboho,Nigeria,Oyo,2338711
Igbeti,Nigeria,Oyo,2338772
Igbara-Odo,Nigeria,Ekiti,2338810
Ifo,Nigeria,Ogun,2338876
Idanre,Nigeria,Ondo,2339150
Idah,Nigeria,Kogi,2339156
Ibi,Nigeria,Taraba,2339287
Ibeto,Nigeria,Niger,2339293
Ibadan,Nigeria,Oyo,2339354
Hadejia,Nigeria,Jigawa,2339631
Gwoza,Nigeria,Borno,2339665
Gwarzo,Nigeria,Kano,2339756
Gwaram,Nigeria,Jigawa,2339786
Gwadabawa,Nigeria,Sokoto,2339892
Gusau,Nigeria,Zamfara,2339937
Gummi,Nigeria,Zamfara,2340086
Gumel,Nigeria,Jigawa,2340091
Gombi,Nigeria,Adamawa,2340446
Gombe,Nigeria,Gombe,2340451
Gembu,Nigeria,Taraba,2341275
Geidam,Nigeria,Yobe,2341294
Gbongan,Nigeria,Osun,2341355
Gaya,Nigeria,Kano,2341580
Gashua,Nigeria,Yobe,2341656
Garko,Nigeria,Gombe,2341758
Ganye,Nigeria,Adamawa,2341955
Gamboru,Nigeria,Borno,2342192
Funtua,Nigeria,Katsina,2342490
Fiditi,Nigeria,Oyo,2342628
Ezza-Ohu,Nigeria,Ebonyi,2342883
Esuk Oron,Nigeria,Akwa Ibom,2343093
Epe,Nigeria,Lagos,2343252
Enugu-Ukwu,Nigeria,Anambra,2343270
Enugu-Ezike,Nigeria,Enugu,2343273
Enugu,Nigeria,Enugu,2343279
Emure-Ekiti,Nigeria,Ekiti,2343299
Elele,Nigeria,Rivers,2343512
Ekpoma,Nigeria,Edo,2343641
Eket,Nigeria,Akwa Ibom,2343720
Ejigbo,Nigeria,Osun,2343784
Eha Amufu,Nigeria,Enugu,2343822
Egbe,Nigeria,Kogi,2343943
Effon Alaiye,Nigeria,Osun,2343983
Effium,Nigeria,Ebonyi,2343985
Ebute Ikorodu,Nigeria,Lagos,2344082
Dutsen Wai,Nigeria,Kaduna,2344229
Dutse,Nigeria,Jigawa,2344245
Dukku,Nigeria,Gombe,2344418
Doma,Nigeria,Nassarawa,2344600
Dikwa,Nigeria,Borno,2344854
Deba,Nigeria,Gombe,2345029
Daura,Nigeria,Katsina,2345094
Daura,Nigeria,Yobe,2345096
Darazo,Nigeria,Bauchi,2345152
Damboa,Nigeria,Borno,2345498
Damaturu,Nigeria,Yobe,2345521
Calabar,Nigeria,Cross River,2346229
Burutu,Nigeria,Delta,2346317
Bukuru,Nigeria,Plateau,2346561
Buguma,Nigeria,Rivers,2346615
Bonny,Nigeria,Rivers,2346812
Bode Saadu,Nigeria,Kwara,2346951
Biu,Nigeria,Borno,2346995
Birnin Kudu,Nigeria,Jigawa,2347057
Birnin Kebbi,Nigeria,Kebbi,2347059
Sofo-Birnin-Gwari,Nigeria,Kaduna,2347061
Billiri,Nigeria,Gombe,2347155
Bida,Nigeria,Niger,2347209
Benin City,Nigeria,Edo,2347283
Bende,Nigeria,Abia,2347303
Beli,Nigeria,Taraba,2347330
Bauchi,Nigeria,Bauchi,2347470
Baro,Nigeria,Niger,2347592
Bama,Nigeria,Borno,2347954
Badagry,Nigeria,Lagos,2348395
Babana,Nigeria,Niger,2348507
Azare,Nigeria,Bauchi,2348595
Awka,Nigeria,Anambra,2348773
Awgu,Nigeria,Enugu,2348783
Auchi,Nigeria,Edo,2348892
Asaba,Nigeria,Delta,2349276
Argungu,Nigeria,Kebbi,2349431
Aramoko-Ekiti,Nigeria,Ekiti,2349529
Apomu,Nigeria,Osun,2349558
Anchau,Nigeria,Kaduna,2349951
Amaigbo,Nigeria,Abia,2350249
Akwanga,Nigeria,Nassarawa,2350806
Akure,Nigeria,Ondo,2350841
Aku,Nigeria,Enugu,2350886
Ajaokuta,Nigeria,Kogi,2351470
Agulu,Nigeria,Anambra,2351740
Agbor,Nigeria,Delta,2351979
Afikpo,Nigeria,Ebonyi,2352250
Ado Odo,Nigeria,Ogun,2352356
Ado-Ekiti,Nigeria,Ekiti,2352379
Abuja,Nigeria,Abuja Federal Capital Territory,2352778
Abeokuta,Nigeria,Ogun,2352947
Abakaliki,Nigeria,Ebonyi,2353099
Aba,Nigeria,Abia,2353151
Degema Hulk,Nigeria,Rivers,2591159
Tipitapa,Nicaragua,Managua,3616035
Somoto,Nicaragua,Madriz,3616232
Somotillo,Nicaragua,Chinandega,3616234
Siuna,Nicaragua,AtlÃ¡ntico Norte (RAAN),3616253
San Rafael del Sur,Nicaragua,Managua,3616594
San Marcos,Nicaragua,Carazo,3616682
Rivas,Nicaragua,Rivas,3617052
RÃ­o Blanco,Nicaragua,Matagalpa,3617069
Rama,Nicaragua,AtlÃ¡ntico Sur,3617095
Puerto Cabezas,Nicaragua,AtlÃ¡ntico Norte (RAAN),3617154
Ocotal,Nicaragua,Nueva Segovia,3617448
Nueva Guinea,Nicaragua,AtlÃ¡ntico Sur,3617459
Nandaime,Nicaragua,Granada,3617513
Nagarote,Nicaragua,LeÃ³n,3617522
Matagalpa,Nicaragua,Matagalpa,3617708
Masaya,Nicaragua,Masaya,3617723
Masatepe,Nicaragua,Masaya,3617725
Managua,Nicaragua,Managua,3617763
LeÃ³n,Nicaragua,LeÃ³n,3618030
La Paz Centro,Nicaragua,LeÃ³n,3618411
Juigalpa,Nicaragua,Chontales,3618908
Jinotepe,Nicaragua,Carazo,3618926
Jinotega,Nicaragua,Jinotega,3618929
Jalapa,Nicaragua,Nueva Segovia,3618954
Granada,Nicaragua,Granada,3619136
EstelÃ­,Nicaragua,EstelÃ­,3619194
El Viejo,Nicaragua,Chinandega,3619267
El Crucero,Nicaragua,Managua,3619853
Diriamba,Nicaragua,Carazo,3620170
Corinto,Nicaragua,Chinandega,3620269
Chinandega,Nicaragua,Chinandega,3620381
Chichigalpa,Nicaragua,Chinandega,3620390
Camoapa,Nicaragua,Boaco,3620544
Boaco,Nicaragua,Boaco,3620674
Bluefields,Nicaragua,AtlÃ¡ntico Sur,3620680
Ciudad Sandino,Nicaragua,Managua,3828262
Zwolle,Netherlands,Overijssel,2743477
Zwijndrecht,Netherlands,South Holland,2743493
Zutphen,Netherlands,Gelderland,2743608
Zundert,Netherlands,North Brabant,2743619
Zoetermeer,Netherlands,South Holland,2743856
Zevenaar,Netherlands,Gelderland,2743949
Zeist,Netherlands,Utrecht,2743977
Zeewolde,Netherlands,Flevoland,2743997
Zandvoort,Netherlands,North Holland,2744042
Zaltbommel,Netherlands,Gelderland,2744102
Zaanstad,Netherlands,North Holland,2744114
Zaandam,Netherlands,North Holland,2744118
Wolvega,Netherlands,Friesland,2744194
Woerden,Netherlands,Utrecht,2744248
Woensdrecht,Netherlands,North Brabant,2744257
Wisch,Netherlands,Gelderland,2744324
Winterswijk,Netherlands,Gelderland,2744332
Winschoten,Netherlands,Groningen,2744344
Wijk bij Duurstede,Netherlands,Utrecht,2744483
Wijchen,Netherlands,Gelderland,2744514
Wierden,Netherlands,Overijssel,2744549
Westervoort,Netherlands,Gelderland,2744675
Werkendam,Netherlands,North Brabant,2744827
Weesp,Netherlands,North Holland,2744904
Weert,Netherlands,Limburg,2744911
Wassenaar,Netherlands,South Holland,2744991
Wageningen,Netherlands,Gelderland,2745088
Waddinxveen,Netherlands,South Holland,2745096
Waalwijk,Netherlands,North Brabant,2745123
Waalre,Netherlands,North Brabant,2745127
Vught,Netherlands,North Brabant,2745154
Voorst,Netherlands,Gelderland,2745297
Voorschoten,Netherlands,South Holland,2745301
Voorhout,Netherlands,South Holland,2745311
Voorburg,Netherlands,South Holland,2745321
Volendam,Netherlands,North Holland,2745340
Vlissingen,Netherlands,Zeeland,2745392
Vlagtwedde,Netherlands,Groningen,2745461
Vlaardingen,Netherlands,South Holland,2745467
Vianen,Netherlands,Utrecht,2745580
Venray,Netherlands,Limburg,2745634
Venlo,Netherlands,Limburg,2745641
Velsen-Zuid,Netherlands,North Holland,2745673
Velp,Netherlands,Gelderland,2745677
Veldhoven,Netherlands,North Brabant,2745706
Veghel,Netherlands,North Brabant,2745726
Veere,Netherlands,Zeeland,2745739
Veenendaal,Netherlands,Utrecht,2745774
Veendam,Netherlands,Groningen,2745783
Valkenswaard,Netherlands,North Brabant,2745860
Utrecht,Netherlands,Utrecht,2745912
Urk,Netherlands,Flevoland,2745932
Uithoorn,Netherlands,North Holland,2745973
Uden,Netherlands,North Brabant,2746005
Tubbergen,Netherlands,Overijssel,2746133
Tongelre,Netherlands,North Brabant,2746215
Tilburg,Netherlands,North Brabant,2746301
Tiel,Netherlands,Gelderland,2746331
Terneuzen,Netherlands,Zeeland,2746420
Tegelen,Netherlands,Limburg,2746504
Steenwijk,Netherlands,Overijssel,2746766
Steenbergen,Netherlands,North Brabant,2746804
Staphorst,Netherlands,Overijssel,2746839
Stadskanaal,Netherlands,Groningen,2746860
Spijkenisse,Netherlands,South Holland,2746932
Someren,Netherlands,North Brabant,2747021
Soest,Netherlands,Utrecht,2747034
Sneek,Netherlands,Friesland,2747063
Sliedrecht,Netherlands,South Holland,2747169
Sittard,Netherlands,Limburg,2747203
Sint-Oedenrode,Netherlands,North Brabant,2747227
's-Hertogenbosch,Netherlands,North Brabant,2747351
's-Gravenzande,Netherlands,South Holland,2747364
The Hague,Netherlands,South Holland,2747373
Schijndel,Netherlands,North Brabant,2747584
Schiedam,Netherlands,South Holland,2747596
Scheveningen,Netherlands,South Holland,2747599
Schagen,Netherlands,North Holland,2747720
Rucphen,Netherlands,North Brabant,2747858
Rotterdam,Netherlands,South Holland,2747891
Roosendaal,Netherlands,North Brabant,2747930
Roermond,Netherlands,Limburg,2748000
Rijswijk,Netherlands,South Holland,2748076
Ridderkerk,Netherlands,South Holland,2748172
Rhoon,Netherlands,South Holland,2748178
Rhenen,Netherlands,Utrecht,2748185
Raalte,Netherlands,Overijssel,2748371
Putten,Netherlands,Gelderland,2748392
Purmerend,Netherlands,North Holland,2748413
Pijnacker,Netherlands,South Holland,2748591
Papendrecht,Netherlands,South Holland,2748729
Oud-Beijerland,Netherlands,South Holland,2749182
Oss,Netherlands,North Brabant,2749234
Oosterhout,Netherlands,North Brabant,2749450
Oldenzaal,Netherlands,Overijssel,2749644
Oldebroek,Netherlands,Gelderland,2749668
Oisterwijk,Netherlands,North Brabant,2749680
Oegstgeest,Netherlands,South Holland,2749723
Nuth,Netherlands,Limburg,2749753
Nunspeet,Netherlands,Gelderland,2749756
Nuenen,Netherlands,North Brabant,2749780
Noordwijkerhout,Netherlands,South Holland,2749811
Noordwijk-Binnen,Netherlands,South Holland,2749812
Nijmegen,Netherlands,Gelderland,2750053
Nijkerk,Netherlands,Gelderland,2750065
Nieuwegein,Netherlands,Utrecht,2750325
Nederweert,Netherlands,Limburg,2750467
Naarden,Netherlands,North Holland,2750521
Naaldwijk,Netherlands,South Holland,2750523
Mijdrecht,Netherlands,Utrecht,2750815
Middelharnis,Netherlands,South Holland,2750884
Middelburg,Netherlands,Zeeland,2750896
Meppel,Netherlands,Drenthe,2750947
Meerssen,Netherlands,Limburg,2751037
Medemblik,Netherlands,North Holland,2751073
Maastricht,Netherlands,Limburg,2751283
Maassluis,Netherlands,South Holland,2751285
Maarssen,Netherlands,Utrecht,2751316
Losser,Netherlands,Overijssel,2751424
Loon op Zand,Netherlands,North Brabant,2751456
Lisse,Netherlands,South Holland,2751547
Lindenholt,Netherlands,Gelderland,2751582
Lichtenvoorde,Netherlands,Gelderland,2751651
Leusden,Netherlands,Utrecht,2751687
Lelystad,Netherlands,Flevoland,2751738
Leiderdorp,Netherlands,South Holland,2751771
Leiden,Netherlands,South Holland,2751773
Leeuwarden,Netherlands,Friesland,2751792
Leerdam,Netherlands,South Holland,2751808
Leek,Netherlands,Groningen,2751834
Krimpen aan den IJssel,Netherlands,South Holland,2752264
Korrewegwijk,Netherlands,Groningen,2752420
Kerkrade,Netherlands,Limburg,2752923
Katwijk aan Zee,Netherlands,South Holland,2753010
Kampen,Netherlands,Overijssel,2753106
IJsselstein,Netherlands,Utrecht,2753355
Huizen,Netherlands,North Holland,2753468
Houten,Netherlands,Utrecht,2753557
Horst,Netherlands,Gelderland,2753587
Hoorn,Netherlands,North Holland,2753638
Hoogezand,Netherlands,Groningen,2753706
Hoogeveen,Netherlands,Drenthe,2753719
Hoofddorp,Netherlands,North Holland,2753801
Hoge Vucht,Netherlands,North Brabant,2753955
Hoensbroek,Netherlands,Limburg,2753996
Hilversum,Netherlands,North Holland,2754064
Hilvarenbeek,Netherlands,North Brabant,2754066
Hillegom,Netherlands,South Holland,2754073
Heusden,Netherlands,North Brabant,2754135
Hengelo,Netherlands,Overijssel,2754394
Hendrik-Ido-Ambacht,Netherlands,South Holland,2754408
Helmond,Netherlands,North Brabant,2754447
Hellevoetsluis,Netherlands,South Holland,2754454
Heiloo,Netherlands,North Holland,2754516
Heesch,Netherlands,North Brabant,2754635
Heerlen,Netherlands,Limburg,2754652
Heerhugowaard,Netherlands,North Holland,2754659
Heerenveen,Netherlands,Friesland,2754669
Heerde,Netherlands,Gelderland,2754681
Heemstede,Netherlands,North Holland,2754692
Heemskerk,Netherlands,North Holland,2754697
Harlingen,Netherlands,Friesland,2754817
Harenkarspel,Netherlands,North Holland,2754837
Haren,Netherlands,Groningen,2754841
Harderwijk,Netherlands,Gelderland,2754848
Hardenberg,Netherlands,Overijssel,2754861
Haarlem,Netherlands,North Holland,2755003
Haaksbergen,Netherlands,Overijssel,2755030
Groningen,Netherlands,Groningen,2755251
Groesbeek,Netherlands,Gelderland,2755272
Gouda,Netherlands,South Holland,2755420
Gorinchem,Netherlands,South Holland,2755434
Goirle,Netherlands,North Brabant,2755464
Goes,Netherlands,Zeeland,2755476
Gennep,Netherlands,Limburg,2755584
Gendringen,Netherlands,Gelderland,2755599
Geldrop,Netherlands,North Brabant,2755619
Geldermalsen,Netherlands,Gelderland,2755633
Geertruidenberg,Netherlands,North Brabant,2755669
Ermelo,Netherlands,Gelderland,2756039
Epe,Netherlands,Gelderland,2756059
Enschede,Netherlands,Overijssel,2756071
Enkhuizen,Netherlands,North Holland,2756077
Emmen,Netherlands,Drenthe,2756136
Emmeloord,Netherlands,Flevoland,2756139
Elst,Netherlands,Gelderland,2756161
Elburg,Netherlands,Gelderland,2756232
Eindhoven,Netherlands,North Brabant,2756253
Eibergen,Netherlands,Gelderland,2756295
Eersel,Netherlands,North Brabant,2756342
Ede,Netherlands,Gelderland,2756429
Duiven,Netherlands,Gelderland,2756507
Druten,Netherlands,Gelderland,2756539
Dronten,Netherlands,Flevoland,2756559
Drimmelen,Netherlands,North Brabant,2756569
Driebergen-Rijsenburg,Netherlands,Utrecht,2756619
Drachten,Netherlands,Friesland,2756644
Dordrecht,Netherlands,South Holland,2756669
Dongen,Netherlands,North Brabant,2756723
Doetinchem,Netherlands,Gelderland,2756767
Diemen,Netherlands,North Holland,2756888
Deventer,Netherlands,Overijssel,2756987
Den Helder,Netherlands,North Holland,2757220
Delfzijl,Netherlands,Groningen,2757340
Delft,Netherlands,South Holland,2757345
Delfshaven,Netherlands,South Holland,2757347
De Bilt,Netherlands,Utrecht,2757783
Dalfsen,Netherlands,Overijssel,2757850
Culemborg,Netherlands,Gelderland,2757872
Cuijk,Netherlands,North Brabant,2757874
Cranendonck,Netherlands,North Brabant,2757890
Castricum,Netherlands,North Holland,2757991
Capelle aan den IJssel,Netherlands,South Holland,2758012
Bussum,Netherlands,North Holland,2758064
Bunschoten,Netherlands,Utrecht,2758104
Brunssum,Netherlands,Limburg,2758174
Brummen,Netherlands,Gelderland,2758177
Broek op Langedijk,Netherlands,North Holland,2758245
Broek in Waterland,Netherlands,North Holland,2758258
Breda,Netherlands,North Brabant,2758401
Boxtel,Netherlands,North Brabant,2758460
Boskoop,Netherlands,South Holland,2758547
Borssele,Netherlands,Zeeland,2758587
Borne,Netherlands,Overijssel,2758598
Born,Netherlands,Limburg,2758602
Borger,Netherlands,Drenthe,2758621
Bodegraven,Netherlands,South Holland,2758765
Bloemendaal,Netherlands,North Holland,2758804
Bladel,Netherlands,North Brabant,2758878
Beverwijk,Netherlands,North Holland,2758998
Beuningen,Netherlands,Gelderland,2759016
Best,Netherlands,North Brabant,2759040
Bergschenhoek,Netherlands,South Holland,2759113
Bergeijk,Netherlands,North Brabant,2759132
Bergen op Zoom,Netherlands,North Brabant,2759145
Benthuizen,Netherlands,South Holland,2759178
Beek,Netherlands,Limburg,2759350
Barneveld,Netherlands,Gelderland,2759407
Barendrecht,Netherlands,South Holland,2759426
Baarn,Netherlands,Utrecht,2759544
Asten,Netherlands,North Brabant,2759621
Assen,Netherlands,Drenthe,2759633
Arnhem,Netherlands,Gelderland,2759661
Apeldoorn,Netherlands,Gelderland,2759706
Anloo,Netherlands,Drenthe,2759746
Amsterdam,Netherlands,North Holland,2759794
Amstelveen,Netherlands,North Holland,2759798
Amersfoort,Netherlands,Utrecht,2759821
Alphen aan den Rijn,Netherlands,South Holland,2759875
Almere Stad,Netherlands,Flevoland,2759879
Almelo,Netherlands,Overijssel,2759887
Alkmaar,Netherlands,North Holland,2759899
Alblasserdam,Netherlands,South Holland,2759915
Aalten,Netherlands,Gelderland,2760123
Aalsmeer,Netherlands,North Holland,2760134
Amsterdam-Zuidoost,Netherlands,North Holland,6544881
Berkel en Rodenrijs,Netherlands,South Holland,6929992
Ypenburg,Netherlands,South Holland,6941548
Trondheim,Norway,SÃ¸r-TrÃ¸ndelag,3133880
TromsÃ¸,Norway,Troms,3133895
TÃ¸nsberg,Norway,Vestfold,3134331
Steinkjer,Norway,Nord-TrÃ¸ndelag,3136947
Stavanger,Norway,Rogaland,3137115
Skien,Norway,Telemark,3139075
Sarpsborg,Norway,Ã˜stfold,3140084
Sandnes,Norway,Rogaland,3140321
Sandefjord,Norway,Vestfold,3140390
Porsgrunn,Norway,Telemark,3142657
Oslo,Norway,Oslo,3143244
Moss,Norway,Ã˜stfold,3145375
Molde,Norway,MÃ¸re og Romsdal,3145580
Mo i Rana,Norway,Nordland,3145614
Lillehammer,Norway,Oppland,3147474
Larvik,Norway,Vestfold,3148129
Kristiansund,Norway,MÃ¸re og Romsdal,3149312
Kristiansand,Norway,Vest-Agder,3149318
Kongsberg,Norway,Buskerud,3149563
Horten,Norway,Vestfold,3151770
Haugesund,Norway,Rogaland,3153623
Harstad,Norway,Troms,3153823
Hamar,Norway,Hedmark,3154084
Halden,Norway,Ã˜stfold,3154209
GjÃ¸vik,Norway,Oppland,3155573
Fredrikstad,Norway,Ã˜stfold,3156529
Drammen,Norway,Buskerud,3159016
BodÃ¸,Norway,Nordland,3160881
Bergen,Norway,Hordaland,3161732
Arendal,Norway,Aust-Agder,3162955
Ã…lesund,Norway,MÃ¸re og Romsdal,3163392
AskÃ¸y,Norway,Hordaland,3336587
Ytrebygda,Norway,Hordaland,6697344
WÄling,Nepal,Western Region,1282616
TulsÄ«pur,Nepal,Mid Western,1282635
TÄ«kÄpur,Nepal,Far Western,1282666
TÄnsen,Nepal,Western Region,1282714
SirÄhÄ,Nepal,Eastern Region,1282770
RÄjbirÄj,Nepal,Eastern Region,1282884
Pokhara,Nepal,Western Region,1282898
PÄtan,Nepal,Central Region,1282931
PanautiÌ‡Ì„,Nepal,Central Region,1282950
Malangwa,Nepal,Central Region,1283082
Mahendranagar,Nepal,Far Western,1283095
LahÄn,Nepal,Eastern Region,1283161
Kirtipur,Nepal,Central Region,1283190
KhÄndbÄri,Nepal,Eastern Region,1283217
Kathmandu,Nepal,Central Region,1283240
Janakpur,Nepal,Central Region,1283318
Jaleswar,Nepal,Central Region,1283323
Ithari,Nepal,Eastern Region,1283329
IlÄm,Nepal,Eastern Region,1283333
Hetauda,Nepal,Central Region,1283339
GulariyÄ,Nepal,Mid Western,1283368
Gaur,Nepal,Central Region,1283401
DharÄn BÄzÄr,Nepal,Eastern Region,1283460
DhankutÄ,Nepal,Eastern Region,1283465
Dhangarhi,Nepal,Far Western,1283467
DÄrchulÄ,Nepal,Western Region,1283484
Dailekh,Nepal,Mid Western,1283496
DadeldhurÄ,Nepal,Far Western,1283499
ButwÄl,Nepal,Western Region,1283562
BÄ«rganj,Nepal,Central Region,1283581
BirÄtnagar,Nepal,Eastern Region,1283582
Bharatpur,Nepal,Central Region,1283613
BhairÄhawÄ,Nepal,Western Region,1283621
Bhadrapur,Nepal,Eastern Region,1283628
BanepÄ,Nepal,Central Region,1283679
BÄglung,Nepal,Western Region,1283711
Birendranagar,Nepal,Mid Western,6254843
Dipayal,Nepal,Far Western,6254845
Nepalgunj,Nepal,Mid Western,6941099
Yaren,Nauru,Yaren,7626461
Alofi,Niue,N/A,4036284
Wellington,New Zealand,Wellington,2179537
Wanganui,New Zealand,Manawatu-Wanganui,2179670
Timaru,New Zealand,Canterbury,2181133
Taupo,New Zealand,Waikato,2181742
Pukekohe East,New Zealand,Auckland,2184155
Porirua,New Zealand,Wellington,2184397
Paraparaumu,New Zealand,Wellington,2184904
Palmerston North,New Zealand,Manawatu-Wanganui,2185018
North Shore,New Zealand,Auckland,2185964
New Plymouth,New Zealand,Taranaki,2186239
Nelson,New Zealand,Nelson,2186280
Napier,New Zealand,Hawke's Bay,2186313
Manukau City,New Zealand,Auckland,2187404
Mangere,New Zealand,Auckland,2187454
Lower Hutt,New Zealand,Wellington,2188164
Invercargill,New Zealand,Southland,2189529
Hastings,New Zealand,Hawke's Bay,2190224
Hamilton,New Zealand,Waikato,2190324
Dunedin,New Zealand,Otago,2191562
Christchurch,New Zealand,Canterbury,2192362
Auckland,New Zealand,Auckland,2193733
Levin,New Zealand,Manawatu-Wanganui,2206371
Gisborne,New Zealand,Gisborne,2206854
Masterton,New Zealand,Wellington,2206890
Tauranga,New Zealand,Bay of Plenty,2208032
Papakura,New Zealand,Auckland,2208329
Whakatane,New Zealand,Bay of Plenty,2208330
Ashburton,New Zealand,Canterbury,6217081
Whangarei,New Zealand,Northland,6230919
Cambridge,New Zealand,Waikato,6240770
Rotorua,New Zealand,Bay of Plenty,6241325
Blenheim,New Zealand,Marlborough,6243926
Upper Hutt,New Zealand,Wellington,6244895
Taradale,New Zealand,Hawke's Bay,6246634
Waitakere,New Zealand,Auckland,7302484
Sur,Oman,Ash Sharqiyah South Governorate,286245
Sohar,Oman,Al Batinah North Governorate,286282
SufÄlat SamÄâ€™il,Oman,Muá¸©ÄfazÌ§at ad DÄkhilÄ«yah,286293
ShinÄÅŸ,Oman,Al Batinah North Governorate,286402
ÅžalÄlah,Oman,ZÌ§ufÄr,286621
Åžaá¸©am,Oman,Al Batinah North Governorate,286647
NizwÃ¡,Oman,Muá¸©ÄfazÌ§at ad DÄkhilÄ«yah,286987
Muscat,Oman,Muá¸©ÄfazÌ§at MasqaÅ£,287286
Khasab,Oman,Musandam,287614
IzkÄ«,Oman,Muá¸©ÄfazÌ§at ad DÄkhilÄ«yah,287814
â€˜IbrÄ«,Oman,AzÌ§ ZÌ§Ähirah,287830
IbrÄâ€™,Oman,Ash Sharqiyah North Governorate,287832
Bidbid,Oman,Muá¸©ÄfazÌ§at ad DÄkhilÄ«yah,288721
Bawshar,Oman,Muá¸©ÄfazÌ§at MasqaÅ£,288764
BarkÄâ€™,Oman,Al Batinah South Governorate,288789
BahlÄâ€™,Oman,Muá¸©ÄfazÌ§at ad DÄkhilÄ«yah,288899
BadÄ«yah,Oman,Ash Sharqiyah North Governorate,288902
As Suwayq,Oman,Al Batinah North Governorate,288955
Seeb,Oman,Muá¸©ÄfazÌ§at MasqaÅ£,288967
Rustaq,Oman,Al Batinah South Governorate,289011
Al LiwÄâ€™,Oman,Al Batinah North Governorate,289174
Al KhÄbÅ«rah,Oman,Al Batinah North Governorate,289199
Al BuraymÄ«,Oman,Al Buraimi,289317
Ä€dam,Oman,Muá¸©ÄfazÌ§at ad DÄkhilÄ«yah,289433
Yanqul,Oman,AzÌ§ ZÌ§Ähirah,411849
Vista Alegre,Panama,PanamÃ¡,3700038
Veracruz,Panama,PanamÃ¡,3700164
Tocumen,Panama,PanamÃ¡,3700563
Santiago de Veraguas,Panama,Veraguas,3701117
San Miguelito,Panama,PanamÃ¡,3701329
Puerto Armuelles,Panama,ChiriquÃ­,3702431
Pedregal,Panama,ChiriquÃ­,3703229
PanamÃ¡,Panama,PanamÃ¡,3703443
Pacora,Panama,PanamÃ¡,3703647
Nuevo ArraijÃ¡n,Panama,PanamÃ¡,3703833
Las Cumbres,Panama,PanamÃ¡,3706567
La ConcepciÃ³n,Panama,ChiriquÃ­,3707899
La Chorrera,Panama,PanamÃ¡,3707961
La Cabima,Panama,PanamÃ¡,3708066
David,Panama,ChiriquÃ­,3711668
ColÃ³n,Panama,ColÃ³n,3712076
ChitrÃ©,Panama,Herrera,3712384
Chilibre,Panama,PanamÃ¡,3712455
Chepo,Panama,PanamÃ¡,3712505
Changuinola,Panama,Bocas del Toro,3712560
CativÃ¡,Panama,ColÃ³n,3712884
ArraijÃ¡n,Panama,PanamÃ¡,3714637
Alcalde DÃ­az,Panama,PanamÃ¡,3714932
Aguadulce,Panama,CoclÃ©,3715042
Yurimaguas,Peru,Loreto,3690654
VirÃº,Peru,La Libertad,3690875
Uchiza,Peru,San MartÃ­n,3691094
Tumbes,Peru,Tumbes,3691148
Trujillo,Peru,La Libertad,3691175
Tocache,Peru,San MartÃ­n,3691324
Tingo MarÃ­a,Peru,Huanuco,3691348
Tambo Grande,Peru,Piura,3691530
Talara,Peru,Piura,3691582
Sullana,Peru,Piura,3691674
Sechura,Peru,Piura,3691954
Santiago de Cao,Peru,La Libertad,3692073
San Pedro de Lloc,Peru,La Libertad,3692310
SaÃ±a,Peru,Lambayeque,3692667
Rioja,Peru,San MartÃ­n,3692863
Querecotillo,Peru,Piura,3693057
Pucallpa,Peru,Ucayali,3693345
Piura,Peru,Piura,3693528
Pimentel,Peru,Lambayeque,3693584
Picsi,Peru,Lambayeque,3693645
Paita,Peru,Piura,3694112
PaijÃ¡n,Peru,La Libertad,3694119
Pacasmayo,Peru,La Libertad,3694178
Moyobamba,Peru,San MartÃ­n,3694564
MonsefÃº,Peru,Lambayeque,3694666
Moche,Peru,La Libertad,3694725
Marcavelica,Peru,Piura,3694939
La UniÃ³n,Peru,Piura,3695466
Laredo,Peru,La Libertad,3695617
La Peca,Peru,Amazonas,3695675
Lambayeque,Peru,Lambayeque,3695754
JuanjuÃ­,Peru,San MartÃ­n,3696057
JaÃ©n,Peru,Cajamarca,3696150
Iquitos,Peru,Loreto,3696183
Huaraz,Peru,Ancash,3696378
HuÃ¡nuco,Peru,Huanuco,3696417
Huamachuco,Peru,La Libertad,3696509
Guadalupe,Peru,La Libertad,3696847
FerreÃ±afe,Peru,Lambayeque,3697033
Coishco,Peru,Ancash,3697990
Chulucanas,Peru,Piura,3698105
Chongoyape,Peru,Lambayeque,3698176
Chocope,Peru,La Libertad,3698194
Chimbote,Peru,Ancash,3698304
Chiclayo,Peru,Lambayeque,3698350
ChepÃ©n,Peru,La Libertad,3698390
Chachapoyas,Peru,Amazonas,3698540
Catacaos,Peru,Piura,3698658
Cajamarca,Peru,Cajamarca,3699088
Bellavista,Peru,San MartÃ­n,3699364
Bagua Grande,Peru,Amazonas,3699484
La Breita,Peru,Piura,3814568
Zarumilla,Peru,Tumbes,3818398
Yunguyo,Peru,Puno,3925476
Yanacancha,Peru,Huanuco,3925863
Tarma,Peru,JunÃ­n,3927758
Tambopata,Peru,Madre de Dios,3927942
Tacna,Peru,Tacna,3928128
Santiago de Surco,Peru,Lima region,3928245
Sicuani,Peru,Cusco,3928679
Satipo,Peru,JunÃ­n,3928924
San Vicente de CaÃ±ete,Peru,Lima region,3928993
Santa Ana,Peru,Cusco,3929295
San Isidro,Peru,Lima region,3929631
San Clemente,Peru,Ica,3929768
Puno,Peru,Puno,3931276
Puerto Maldonado,Peru,Madre de Dios,3931470
Pisco,Peru,Ica,3932145
Paramonga,Peru,Lima region,3933024
Nuevo Imperial,Peru,Lima region,3934239
Nazca,Peru,Ica,3934356
Moquegua,Peru,Moquegua,3934608
Mollendo,Peru,Arequipa,3934707
Minas de Marcona,Peru,Ica,3935288
Mala,Peru,Lima region,3935572
Lima,Peru,Lima Province,3936456
La Oroya,Peru,JunÃ­n,3936952
JunÃ­n,Peru,JunÃ­n,3937486
Juliaca,Peru,Puno,3937513
Jauja,Peru,JunÃ­n,3937733
Imperial,Peru,Lima region,3938396
Ilo,Peru,Moquegua,3938415
Ilave,Peru,Puno,3938451
Ica,Peru,Ica,3938527
Huaura,Peru,Lima region,3939023
Huarmey,Peru,Ancash,3939168
Huaral,Peru,Lima region,3939285
Huanta,Peru,Ayacucho,3939386
Huancayo,Peru,JunÃ­n,3939459
Huancavelica,Peru,Huancavelica,3939470
Hualmay,Peru,Lima region,3939761
Huacho,Peru,Lima region,3940002
Cusco,Peru,Cusco,3941584
Chosica,Peru,Lima region,3943423
Chincha Alta,Peru,Ica,3943789
Chaupimarca,Peru,Pasco,3944179
Chancay,Peru,Lima region,3944399
Cerro de Pasco,Peru,Pasco,3944797
CamanÃ¡,Peru,Arequipa,3945985
Callao,Peru,Callao,3946083
Barranca,Peru,Lima region,3946820
Ayaviri,Peru,Puno,3946985
Ayacucho,Peru,Ayacucho,3947019
Arequipa,Peru,Arequipa,3947322
Andahuaylas,Peru,ApurÃ­mac,3947740
Abancay,Peru,ApurÃ­mac,3948642
La Rinconada,Peru,Puno,7626291
Punaauia,French Polynesia,ÃŽles du Vent,4033779
Papeete,French Polynesia,ÃŽles du Vent,4033936
Faaa,French Polynesia,ÃŽles du Vent,4034561
Wewak,Papua New Guinea,East Sepik,2083537
Port Moresby,Papua New Guinea,National Capital,2088122
Popondetta,Papua New Guinea,Northern Province,2088163
Mount Hagen,Papua New Guinea,Western Highlands,2090409
Mendi,Papua New Guinea,Southern Highlands,2090990
Madang,Papua New Guinea,Madang,2091996
Lae,Papua New Guinea,Morobe,2092740
Kokopo,Papua New Guinea,East New Britain,2093685
Kimbe,Papua New Guinea,West New Britain,2093967
Goroka,Papua New Guinea,Eastern Highlands,2096742
Daru,Papua New Guinea,Western Province,2098329
Bulolo,Papua New Guinea,Morobe,2098869
Arawa,Papua New Guinea,Bougainville,2100633
Zamboanga,Philippines,Zamboanga Peninsula,1679432
Wao,Philippines,Autonomous Region in Muslim Mindanao,1679678
Virac,Philippines,Bicol,1679802
Vigan,Philippines,Ilocos,1679980
Victorias,Philippines,Western Visayas,1680007
Victoria,Philippines,Calabarzon,1680018
Veruela,Philippines,Caraga,1680040
Valencia,Philippines,Northern Mindanao,1680116
Urdaneta,Philippines,Ilocos,1680197
Ualog,Philippines,Western Visayas,1680505
Tupi,Philippines,Davao,1680613
Tuguegarao City,Philippines,Cagayan Valley,1680932
Trento,Philippines,Caraga,1681333
Toledo,Philippines,Central Visayas,1681602
Tiwi,Philippines,Bicol,1681676
Ternate,Philippines,Calabarzon,1682472
Teresa,Philippines,Calabarzon,1682478
Telabastagan,Philippines,Central Luzon,1682537
Taytay,Philippines,Calabarzon,1682598
Tayabas,Philippines,Calabarzon,1682659
Tarlac City,Philippines,Central Luzon,1682812
Tanza,Philippines,Metro Manila,1683013
Tanjay,Philippines,Central Visayas,1683088
Tangub,Philippines,Northern Mindanao,1683116
Tandag,Philippines,Caraga,1683302
Tanay,Philippines,Calabarzon,1683319
Tanauan,Philippines,Calabarzon,1683340
Tanauan,Philippines,Eastern Visayas,1683342
Taloc,Philippines,Western Visayas,1683800
Talisay,Philippines,Calabarzon,1683860
Talisay,Philippines,Western Visayas,1683877
Talisay,Philippines,Central Visayas,1683881
Talavera,Philippines,Central Luzon,1684016
Talacogon,Philippines,Caraga,1684137
Tagum,Philippines,Davao,1684269
Taguig,Philippines,Calabarzon,1684308
Tagudin,Philippines,Ilocos,1684320
Tagoloan,Philippines,Northern Mindanao,1684379
Tagbilaran City,Philippines,Central Visayas,1684497
Tagas,Philippines,Bicol,1684577
Tacurong,Philippines,Soccsksargen,1684681
Tabuk,Philippines,Cordillera,1684803
Tabaco,Philippines,Bicol,1685117
Taal,Philippines,Calabarzon,1685146
Surigao,Philippines,Caraga,1685218
Surallah,Philippines,Soccsksargen,1685230
Subic,Philippines,Central Luzon,1685577
Suay,Philippines,Western Visayas,1685622
Sorsogon,Philippines,Bicol,1685755
Solano,Philippines,Cagayan Valley,1685875
Solana,Philippines,Cagayan Valley,1685880
Sitangkai,Philippines,Autonomous Region in Muslim Mindanao,1686004
Sipalay,Philippines,Western Visayas,1686102
Silang,Philippines,Calabarzon,1686547
Sibulan,Philippines,Central Visayas,1686728
Sexmoan,Philippines,Central Luzon,1686933
Sebu,Philippines,Soccsksargen,1687029
Sariaya,Philippines,Calabarzon,1687164
San Vicente,Philippines,Central Luzon,1687409
Santo Tomas,Philippines,Calabarzon,1687534
Santol,Philippines,Central Luzon,1687687
Santiago,Philippines,Cagayan Valley,1687801
Santa Rosa,Philippines,Calabarzon,1687894
Santa Maria,Philippines,Ilocos,1688017
Santa Maria,Philippines,Davao,1688058
Santa Cruz,Philippines,Central Luzon,1688232
Santa Cruz,Philippines,Central Luzon,1688248
Santa Cruz,Philippines,Calabarzon,1688253
Santa Catalina,Philippines,Central Visayas,1688363
Santa Barbara,Philippines,Ilocos,1688372
Santa Ana,Philippines,Central Luzon,1688398
San Simon,Philippines,Central Luzon,1688425
San Pedro,Philippines,Calabarzon,1688749
San Pascual,Philippines,Calabarzon,1688795
San Pablo,Philippines,Calabarzon,1688830
San Nicolas,Philippines,Ilocos,1688859
San Narciso,Philippines,Central Luzon,1688912
San Miguel,Philippines,Central Luzon,1688949
San Miguel,Philippines,Central Luzon,1688954
San Mateo,Philippines,Cagayan Valley,1689052
San Mateo,Philippines,Calabarzon,1689056
San Mariano,Philippines,Davao,1689087
San Marcelino,Philippines,Central Luzon,1689099
San Luis,Philippines,Central Luzon,1689129
San Leonardo,Philippines,Central Luzon,1689171
San Juan,Philippines,Metro Manila,1689286
San Jose del Monte,Philippines,Central Luzon,1689395
San Jose,Philippines,Bicol,1689498
San Jose,Philippines,Mimaropa,1689510
San Ildefonso,Philippines,Central Luzon,1689832
San Francisco,Philippines,Central Luzon,1689973
Aurora,Philippines,Calabarzon,1689994
San Francisco,Philippines,Caraga,1690019
San Fernando,Philippines,Ilocos,1690033
San Fernando,Philippines,Central Luzon,1690039
San Fernando,Philippines,Central Visayas,1690060
San Antonio,Philippines,Central Luzon,1690313
San Antonio,Philippines,Central Luzon,1690315
San Antonio,Philippines,Central Luzon,1690321
Sampaloc,Philippines,Calabarzon,1690570
Samal,Philippines,Central Luzon,1690664
Samal,Philippines,Davao,1690666
Sagay,Philippines,Western Visayas,1691150
Sablayan,Philippines,Mimaropa,1691280
Roxas,Philippines,Cagayan Valley,1691441
Roxas City,Philippines,Western Visayas,1691444
Roxas,Philippines,Mimaropa,1691446
Romblon,Philippines,Mimaropa,1691538
Rizal,Philippines,Central Luzon,1691606
Recodo,Philippines,Zamboanga Peninsula,1691804
Ramos,Philippines,Central Luzon,1691904
Ramon,Philippines,Cagayan Valley,1691911
Quiapo,Philippines,Metro Manila,1692184
Quezon City,Philippines,Metro Manila,1692192
Quezon,Philippines,Central Luzon,1692199
Quezon,Philippines,Northern Mindanao,1692214
Pulupandan,Philippines,Western Visayas,1692489
Pulong Santa Cruz,Philippines,Calabarzon,1692520
Pulilan,Philippines,Central Luzon,1692565
Puerto Princesa,Philippines,Mimaropa,1692685
Port Area,Philippines,Metro Manila,1692872
Porac,Philippines,Central Luzon,1692914
Polomolok,Philippines,Davao,1693077
Polangui,Philippines,Bicol,1693136
Plaridel,Philippines,Central Luzon,1693239
Pio,Philippines,Central Luzon,1693401
Pinamungahan,Philippines,Central Visayas,1693574
Pinamalayan,Philippines,Mimaropa,1693618
Pililla,Philippines,Calabarzon,1693778
Pilar,Philippines,Central Luzon,1693839
Pila,Philippines,Calabarzon,1693870
PeÃ±aranda,Philippines,Central Luzon,1694075
Patuto,Philippines,Calabarzon,1694290
Passi,Philippines,Western Visayas,1694498
Parang,Philippines,Autonomous Region in Muslim Mindanao,1694775
Paraiso,Philippines,Western Visayas,1694791
Papaya,Philippines,Central Luzon,1694826
Paombong,Philippines,Central Luzon,1694861
Pantubig,Philippines,Central Luzon,1694914
Paniqui,Philippines,Central Luzon,1695097
Pangil,Philippines,Calabarzon,1695283
Pandi,Philippines,Central Luzon,1695462
Pandacaqui,Philippines,Central Luzon,1695583
Panalanoy,Philippines,Eastern Visayas,1695743
Panabo,Philippines,Davao,1695804
Palo,Philippines,Eastern Visayas,1696041
Palayan City,Philippines,Central Luzon,1696165
Pagbilao,Philippines,Calabarzon,1696614
PagaluÃ±gan,Philippines,Autonomous Region in Muslim Mindanao,1696683
Pagadian,Philippines,Zamboanga Peninsula,1696710
Paete,Philippines,Calabarzon,1696718
Pacol,Philippines,Western Visayas,1696814
Ozamiz City,Philippines,Northern Mindanao,1696899
Oroquieta,Philippines,Northern Mindanao,1697006
Ormoc,Philippines,Eastern Visayas,1697018
Orion,Philippines,Central Luzon,1697023
Orani,Philippines,Central Luzon,1697046
Olongapo,Philippines,Central Luzon,1697175
Obando,Philippines,Central Luzon,1697376
Noveleta,Philippines,Calabarzon,1697486
Norzagaray,Philippines,Central Luzon,1697497
New Corella,Philippines,Davao,1697773
Nasugbu,Philippines,Calabarzon,1698030
Narra,Philippines,Mimaropa,1698103
Naic,Philippines,Calabarzon,1698548
Nagcarlan,Philippines,Calabarzon,1698740
Naga,Philippines,Bicol,1698829
Naga,Philippines,Central Visayas,1698839
Nabunturan,Philippines,Davao,1698887
Nabua,Philippines,Bicol,1698921
Muricay,Philippines,Zamboanga Peninsula,1699054
Murcia,Philippines,Western Visayas,1699060
MuÃ±oz,Philippines,Central Luzon,1699088
Morong,Philippines,Central Luzon,1699204
Morong,Philippines,Calabarzon,1699205
Rodriguez,Philippines,Calabarzon,1699296
Monkayo,Philippines,Davao,1699323
Molave,Philippines,Zamboanga Peninsula,1699388
Minglanilla,Philippines,Central Visayas,1699572
Midsayap,Philippines,Soccsksargen,1699755
Meycauayan,Philippines,Central Luzon,1699802
Mexico,Philippines,Central Luzon,1699805
Mercedes,Philippines,Bicol,1699833
Mendez-NuÃ±ez,Philippines,Calabarzon,1699858
Mauban,Philippines,Calabarzon,1700179
Mati,Philippines,Davao,1700360
Masinloc,Philippines,Central Luzon,1700665
Masbate,Philippines,Bicol,1700712
Masantol,Philippines,Central Luzon,1700753
Mariveles,Philippines,Central Luzon,1700868
Marilao,Philippines,Central Luzon,1700917
Mariano,Philippines,Northern Mindanao,1700980
Marawi City,Philippines,Autonomous Region in Muslim Mindanao,1701053
Maramag,Philippines,Northern Mindanao,1701124
Maragondon,Philippines,Calabarzon,1701149
Mantampay,Philippines,Northern Mindanao,1701472
Mansilingan,Philippines,Western Visayas,1701500
Mansalay,Philippines,Mimaropa,1701516
Manolo Fortich,Philippines,Northern Mindanao,1701537
Manila,Philippines,Metro Manila,1701668
Manibaug Pasig,Philippines,Central Luzon,1701692
Mangaldan,Philippines,Ilocos,1701872
Mandaue City,Philippines,Central Visayas,1701947
Mandaluyong City,Philippines,Metro Manila,1701966
Mankayan,Philippines,Cordillera,1702002
Manay,Philippines,Davao,1702032
Manapla,Philippines,Western Visayas,1702077
Manaoag,Philippines,Ilocos,1702096
Mamburao,Philippines,Mimaropa,1702263
Mamatid,Philippines,Calabarzon,1702372
Malvar,Philippines,Calabarzon,1702413
Maluso,Philippines,Autonomous Region in Muslim Mindanao,1702425
MaluÃ±gun,Philippines,Soccsksargen,1702442
Malolos,Philippines,Central Luzon,1702540
Malita,Philippines,Davao,1702649
Malilipot,Philippines,Bicol,1702763
Malaybalay,Philippines,Northern Mindanao,1702934
Malapatan,Philippines,Soccsksargen,1703051
Malanday,Philippines,Calabarzon,1703116
Malabanban Norte,Philippines,Calabarzon,1703355
Makati City,Philippines,Metro Manila,1703417
Mahayag,Philippines,Zamboanga Peninsula,1703598
Magsaysay,Philippines,Davao,1703773
Magarao,Philippines,Bicol,1704002
Maganoy,Philippines,Autonomous Region in Muslim Mindanao,1704021
Magalang,Philippines,Central Luzon,1704067
Mabalacat City,Philippines,Central Luzon,1704703
Maasin,Philippines,Eastern Visayas,1704758
Maao,Philippines,Western Visayas,1704781
Lupon,Philippines,Davao,1704968
Lumbang,Philippines,Calabarzon,1705190
Lucena,Philippines,Calabarzon,1705357
Lucban,Philippines,Calabarzon,1705367
Lubao,Philippines,Central Luzon,1705440
Los BaÃ±os,Philippines,Calabarzon,1705536
Lopez,Philippines,Calabarzon,1705572
Loma de Gato,Philippines,Central Luzon,1705771
Loboc,Philippines,Central Visayas,1705871
Lipa City,Philippines,Calabarzon,1706090
Lingayen,Philippines,Ilocos,1706188
Limay,Philippines,Central Luzon,1706361
Liloan,Philippines,Central Visayas,1706393
Lilio,Philippines,Calabarzon,1706402
Libon,Philippines,Bicol,1706609
Libertad,Philippines,Caraga,1706684
Legaspi,Philippines,Bicol,1706889
Laur,Philippines,Central Luzon,1707049
La Trinidad,Philippines,Cordillera,1707123
Lapu-Lapu City,Philippines,Central Visayas,1707267
La Paz,Philippines,Central Luzon,1707324
Laoang,Philippines,Eastern Visayas,1707398
Laoag,Philippines,Ilocos,1707404
Lala,Philippines,Northern Mindanao,1707944
Laguilayan,Philippines,Soccsksargen,1708056
La Castellana,Philippines,Western Visayas,1708217
La Carlota,Philippines,Western Visayas,1708226
Labo,Philippines,Bicol,1708291
Koronadal,Philippines,Soccsksargen,1708522
Kidapawan,Philippines,Soccsksargen,1708824
Kawit,Philippines,Calabarzon,1709003
Kalibo (poblacion),Philippines,Western Visayas,1709632
Kabankalan,Philippines,Western Visayas,1709968
Kabacan,Philippines,Soccsksargen,1710011
Jose PaÃ±ganiban,Philippines,Bicol,1710103
Jolo,Philippines,Autonomous Region in Muslim Mindanao,1710141
Jasaan,Philippines,Northern Mindanao,1710258
Jalajala,Philippines,Calabarzon,1710357
Jagna,Philippines,Central Visayas,1710378
Jaen,Philippines,Central Luzon,1710389
Itogon,Philippines,Cordillera,1710441
Isulan,Philippines,Soccsksargen,1710470
Isabela,Philippines,Western Visayas,1710518
City of Isabela,Philippines,Autonomous Region in Muslim Mindanao,1710519
Irosin,Philippines,Bicol,1710531
Iriga City,Philippines,Bicol,1710544
Ipil,Philippines,Zamboanga Peninsula,1710612
Indang,Philippines,Calabarzon,1710770
Imus,Philippines,Calabarzon,1710914
Iloilo,Philippines,Western Visayas,1711005
Iligan City,Philippines,Soccsksargen,1711082
Ilagan,Philippines,Cagayan Valley,1711146
Iba,Philippines,Central Luzon,1711437
Hinigaran,Philippines,Western Visayas,1711621
Himamaylan,Philippines,Western Visayas,1711718
Hermosa,Philippines,Central Luzon,1711829
Hagonoy,Philippines,Central Luzon,1711982
Guyong,Philippines,Central Luzon,1712051
Gumaca,Philippines,Calabarzon,1712162
Guiset East,Philippines,Ilocos,1712232
Guimba,Philippines,Central Luzon,1712488
GuihulÃ±gan,Philippines,Central Visayas,1712520
Guiguinto,Philippines,Central Luzon,1712531
Goa,Philippines,Bicol,1712808
Glan,Philippines,Soccsksargen,1712819
Gerona,Philippines,Central Luzon,1713004
General Trias,Philippines,Calabarzon,1713014
General Tinio,Philippines,Central Luzon,1713018
General Santos,Philippines,Soccsksargen,1713022
General Mamerto Natividad,Philippines,Central Luzon,1713027
Gapan,Philippines,Central Luzon,1713226
Escalante,Philippines,Western Visayas,1713818
Saravia,Philippines,Western Visayas,1713857
Dumaguete,Philippines,Central Visayas,1714201
Don Carlos,Philippines,Northern Mindanao,1714441
Domalanoan,Philippines,Ilocos,1714482
Dologon,Philippines,Northern Mindanao,1714519
Dipolog,Philippines,Zamboanga Peninsula,1714674
Dinalupihan,Philippines,Central Luzon,1714766
Digos,Philippines,Davao,1714956
Diadi,Philippines,Cagayan Valley,1715094
Del Pilar,Philippines,Central Luzon,1715169
Davao,Philippines,Davao,1715348
DasmariÃ±as,Philippines,Calabarzon,1715430
Dapitan,Philippines,Zamboanga Peninsula,1715542
Danao,Philippines,Central Visayas,1715804
Danao,Philippines,Central Visayas,1715812
Daet,Philippines,Bicol,1716287
Cuenca,Philippines,Calabarzon,1716618
Cotabato,Philippines,Autonomous Region in Muslim Mindanao,1716771
Cordova,Philippines,Central Visayas,1716858
Consolacion,Philippines,Central Visayas,1716924
Concepcion,Philippines,Central Luzon,1716995
Concepcion Ibaba,Philippines,Calabarzon,1717008
Compostela,Philippines,Central Visayas,1717051
Compostela,Philippines,Davao,1717053
Cebu City,Philippines,Central Visayas,1717512
Cavite City,Philippines,Calabarzon,1717641
Catbalogan,Philippines,Eastern Visayas,1717911
Catarman,Philippines,Eastern Visayas,1717926
Catanauan,Philippines,Calabarzon,1717960
Castillejos,Philippines,Central Luzon,1718078
Carmona,Philippines,Calabarzon,1718306
Cogan,Philippines,Central Visayas,1718328
Carigara,Philippines,Eastern Visayas,1718393
Cardona,Philippines,Calabarzon,1718426
Carcar,Philippines,Central Visayas,1718436
Capas,Philippines,Central Luzon,1718722
Canlaon,Philippines,Central Visayas,1719053
Candelaria,Philippines,Calabarzon,1719274
Candaba,Philippines,Central Luzon,1719329
Camiling,Philippines,Central Luzon,1719683
Calumpit,Philippines,Central Luzon,1720034
Calumpang,Philippines,Metro Manila,1720052
Calbayog City,Philippines,Eastern Visayas,1720402
Calauan,Philippines,Calabarzon,1720464
Calauag,Philippines,Calabarzon,1720472
Calatagan,Philippines,Calabarzon,1720499
Calasiao,Philippines,Ilocos,1720508
Calapan,Philippines,Mimaropa,1720561
Calamba,Philippines,Calabarzon,1720681
Calaca,Philippines,Calabarzon,1720751
Calabanga,Philippines,Bicol,1720793
Cainta,Philippines,Calabarzon,1720840
Cagayan de Oro,Philippines,Northern Mindanao,1721080
Cadiz,Philippines,Western Visayas,1721168
Cabiao,Philippines,Central Luzon,1721636
Cabayangan,Philippines,Davao,1721695
Cabanatuan City,Philippines,Central Luzon,1721906
Cabagan,Philippines,Cagayan Valley,1722005
Cabadbaran,Philippines,Caraga,1722032
Butuan,Philippines,Caraga,1722186
Bustos,Philippines,Central Luzon,1722267
Boroon,Philippines,Northern Mindanao,1722356
Burgos,Philippines,Central Luzon,1722433
Bunawan,Philippines,Caraga,1722731
Buluan,Philippines,Autonomous Region in Muslim Mindanao,1722818
Bulaon,Philippines,Central Luzon,1722930
Bulan,Philippines,Bicol,1722985
Bulacan,Philippines,Central Luzon,1723066
Buhi,Philippines,Bicol,1723166
Bugo,Philippines,Northern Mindanao,1723257
Buenavista,Philippines,Caraga,1723481
Budta,Philippines,Autonomous Region in Muslim Mindanao,1723510
Botolan,Philippines,Central Luzon,1723822
Borongan,Philippines,Eastern Visayas,1723893
Bongao,Philippines,Autonomous Region in Muslim Mindanao,1724088
Bongabon,Philippines,Central Luzon,1724106
Bogo,Philippines,Central Visayas,1724435
Bocaue,Philippines,Central Luzon,1724489
Bislig,Philippines,Caraga,1724767
Binonga,Philippines,Western Visayas,1724933
Binmaley,Philippines,Ilocos,1724956
Binangonan,Philippines,Calabarzon,1725094
Binalbagan,Philippines,Western Visayas,1725157
Bignay Uno,Philippines,Calabarzon,1725359
Bayugan,Philippines,Caraga,1725684
Bayombong,Philippines,Cagayan Valley,1725729
Baybay,Philippines,Eastern Visayas,1725799
Bayawan,Philippines,Central Visayas,1725804
Bayambang,Philippines,Ilocos,1725863
Bay,Philippines,Calabarzon,1725919
Bauang,Philippines,Ilocos,1725983
Bauan,Philippines,Calabarzon,1725991
Bato,Philippines,Bicol,1726156
Batangas,Philippines,Calabarzon,1726280
Batac City,Philippines,Ilocos,1726339
Baras,Philippines,Calabarzon,1726765
Bantayan,Philippines,Central Visayas,1727043
Bansalan,Philippines,Davao,1727080
BaÃ±ga,Philippines,Soccsksargen,1727400
Banaybanay,Philippines,Calabarzon,1727522
Bambang,Philippines,Cagayan Valley,1727663
Baliuag,Philippines,Central Luzon,1727995
Balayan,Philippines,Calabarzon,1728336
Balanga,Philippines,Central Luzon,1728523
Balamban,Philippines,Central Visayas,1728546
Balagtas,Philippines,Central Luzon,1728584
Bais,Philippines,Central Visayas,1728772
Bah-Bah,Philippines,Caraga,1728825
Baguio,Philippines,Cordillera,1728930
Bago City,Philippines,Western Visayas,1729085
Baggabag B,Philippines,Cagayan Valley,1729324
Bacoor,Philippines,Calabarzon,1729524
Bacolod City,Philippines,Western Visayas,1729564
Babo-Pangulo,Philippines,Central Luzon,1729734
Baao,Philippines,Bicol,1729814
Atimonan,Philippines,Calabarzon,1729987
Asia,Philippines,Western Visayas,1730097
Aringay,Philippines,Ilocos,1730171
Arayat,Philippines,Central Luzon,1730225
Aparri,Philippines,Cagayan Valley,1730398
Apalit,Philippines,Central Luzon,1730413
Antipolo,Philippines,Calabarzon,1730501
Angono,Philippines,Calabarzon,1730713
Angeles City,Philippines,Central Luzon,1730737
Angat,Philippines,Central Luzon,1730749
Amadeo,Philippines,Calabarzon,1731212
Alicia,Philippines,Cagayan Valley,1731486
Aliaga,Philippines,Central Luzon,1731528
Alaminos,Philippines,Calabarzon,1731686
Alabel,Philippines,Soccsksargen,1731744
Agoo,Philippines,Ilocos,1731959
Abuyog,Philippines,Eastern Visayas,1732312
Abucay,Philippines,Central Luzon,1732354
Bagong Pagasa,Philippines,Calabarzon,1966336
Malingao,Philippines,Soccsksargen,1978681
Pasig City,Philippines,Metro Manila,7290466
Pandan,Philippines,Western Visayas,8299649
Apas,Philippines,Central Visayas,10628881
Chuhar JamÄli,Pakistan,Sindh,1108161
RÄwala Kot,Pakistan,Azad Kashmir,1161983
PÄ«r jo Goth,Pakistan,Sindh,1161991
Khairpur,Pakistan,Sindh,1162004
Zhob,Pakistan,BalochistÄn,1162105
Zaida,Pakistan,Khyber Pakhtunkhwa,1162261
ZÄhir PÄ«r,Pakistan,Punjab,1162275
ZafarwÄl,Pakistan,Punjab,1162285
Yazman,Pakistan,Punjab,1162316
WazÄ«rÄbÄd,Pakistan,Punjab,1162456
Warburton,Pakistan,Punjab,1162572
WÄrÄh,Pakistan,Sindh,1162589
VihÄri,Pakistan,Punjab,1162813
UtmÄnzai,Pakistan,Khyber Pakhtunkhwa,1162855
Uthal,Pakistan,BalochistÄn,1162862
Usta Muhammad,Pakistan,BalochistÄn,1162868
Umarkot,Pakistan,Sindh,1162959
Ubauro,Pakistan,Sindh,1163021
Turbat,Pakistan,BalochistÄn,1163054
Topi,Pakistan,Khyber Pakhtunkhwa,1163224
Toba Tek Singh,Pakistan,Punjab,1163272
Thul,Pakistan,Sindh,1163414
Thatta,Pakistan,Sindh,1163582
ThÄru ShÄh,Pakistan,Sindh,1163595
Taunsa,Pakistan,Punjab,1163724
TÄnk,Pakistan,Khyber Pakhtunkhwa,1163905
Tangi,Pakistan,Khyber Pakhtunkhwa,1163927
Tando Muhammad KhÄn,Pakistan,Sindh,1163952
Tando JÄm,Pakistan,Sindh,1163958
Tando AllÄhyÄr,Pakistan,Sindh,1163965
Tando Ä€dam,Pakistan,Sindh,1163967
TÄndliÄnwÄla,Pakistan,Punjab,1163968
TalhÄr,Pakistan,Sindh,1164045
Talamba,Pakistan,Punjab,1164064
Talagang,Pakistan,Punjab,1164069
TÄl,Pakistan,Khyber Pakhtunkhwa,1164076
SwÄbi,Pakistan,Khyber Pakhtunkhwa,1164216
Surkhpur,Pakistan,Punjab,1164245
Sukkur,Pakistan,Sindh,1164408
Sukheke Mandi,Pakistan,Punjab,1164419
Sodhra,Pakistan,Punjab,1164679
SÄ«ta Road,Pakistan,Sindh,1164716
Sinjhoro,Pakistan,Sindh,1164776
SillÄnwÄli,Pakistan,Punjab,1164825
Sibi,Pakistan,BalochistÄn,1164896
Sialkot,Pakistan,Punjab,1164909
ShujÄÄbÄd,Pakistan,Punjab,1164970
Shorko,Pakistan,Khyber Pakhtunkhwa,1164987
ShikÄrpur,Pakistan,Sindh,1165108
Sheikhupura,Pakistan,Punjab,1165221
Sharqpur,Pakistan,Punjab,1165260
Shakargarr,Pakistan,Punjab,1165388
Shahr SultÄn,Pakistan,Punjab,1165486
ShÄhpur ChÄkar,Pakistan,Sindh,1165507
Shahkot,Pakistan,Punjab,1165569
ShÄhdÄdpur,Pakistan,Sindh,1165635
ShÄhdÄdkot,Pakistan,Sindh,1165638
Shabqadar,Pakistan,Khyber Pakhtunkhwa,1165744
SehwÄn,Pakistan,Sindh,1165789
Sargodha,Pakistan,Punjab,1166000
SarÄi Sidhu,Pakistan,Punjab,1166062
SarÄi Naurang,Pakistan,Khyber Pakhtunkhwa,1166066
SarÄi Ä€lamgÄ«r,Pakistan,Punjab,1166073
Sangla Hill,Pakistan,Punjab,1166146
SÄnghar,Pakistan,Sindh,1166164
SambriÄl,Pakistan,Punjab,1166265
Sakrand,Pakistan,Sindh,1166381
SÄhÄ«wÄl,Pakistan,Punjab,1166547
Sahiwal,Pakistan,Punjab,1166548
SÄdiqÄbÄd,Pakistan,Punjab,1166652
Rohri,Pakistan,Sindh,1166827
RenÄla Khurd,Pakistan,Punjab,1166933
Rawalpindi,Pakistan,Punjab,1166993
Ratodero,Pakistan,Sindh,1167031
RÄnÄ«pur,Pakistan,Sindh,1167142
RÄjanpur,Pakistan,Punjab,1167380
RÄja Jang,Pakistan,Punjab,1167386
RÄiwind,Pakistan,Punjab,1167398
RÄdhan,Pakistan,Sindh,1167501
RabwÄh,Pakistan,Punjab,1167507
Quetta,Pakistan,BalochistÄn,1167528
Kambar,Pakistan,Sindh,1167622
QÄdirpur RÄn,Pakistan,Punjab,1167648
Pishin,Pakistan,BalochistÄn,1167821
PÄ«r Mahal,Pakistan,Punjab,1167873
Pindi Gheb,Pakistan,Punjab,1168015
Pindi BhattiÄn,Pakistan,Punjab,1168021
Pind DÄdan KhÄn,Pakistan,Punjab,1168036
PhÄlia,Pakistan,Punjab,1168166
Peshawar,Pakistan,Khyber Pakhtunkhwa,1168197
Pattoki,Pakistan,Punjab,1168226
PasrÅ«r,Pakistan,Punjab,1168307
Pasni,Pakistan,BalochistÄn,1168312
PÄno Ä€qil,Pakistan,Sindh,1168412
PÄkpattan,Pakistan,Punjab,1168555
PahÄrpur,Pakistan,Khyber Pakhtunkhwa,1168633
Pad Äªdan,Pakistan,Sindh,1168652
Pabbi,Pakistan,Khyber Pakhtunkhwa,1168680
OkÄra,Pakistan,Punjab,1168718
Nushki,Pakistan,BalochistÄn,1168749
NawÄbshÄh,Pakistan,Sindh,1169116
Naushahro FÄ«roz,Pakistan,Sindh,1169143
Naushahra VirkÄn,Pakistan,Punjab,1169145
Naudero,Pakistan,Sindh,1169187
NasÄ«rÄbÄd,Pakistan,Sindh,1169254
NÄrowÄl,Pakistan,Punjab,1169278
NÄrang,Pakistan,Punjab,1169334
Naukot,Pakistan,Sindh,1169367
NankÄna SÄhib,Pakistan,Punjab,1169372
Muzaffargarh,Pakistan,Punjab,1169605
MuzaffarÄbÄd,Pakistan,Azad Kashmir,1169607
MustafÄbÄd,Pakistan,Punjab,1169620
Murree,Pakistan,Punjab,1169684
MurÄ«dke,Pakistan,Punjab,1169692
MultÄn,Pakistan,Punjab,1169825
Moro,Pakistan,Sindh,1170013
Mithi,Pakistan,Sindh,1170219
Mitha TiwÄna,Pakistan,Punjab,1170222
MÄ«rpur MÄthelo,Pakistan,Sindh,1170294
Mirpur Khas,Pakistan,Sindh,1170295
Mingora,Pakistan,Khyber Pakhtunkhwa,1170395
MinchinÄbÄd,Pakistan,Punjab,1170398
MiÄnwÄli,Pakistan,Punjab,1170425
MiÄn ChannÅ«n,Pakistan,Punjab,1170486
MehrÄbpur,Pakistan,BalochistÄn,1170564
Mehar,Pakistan,Sindh,1170584
MÄtli,Pakistan,Sindh,1170667
MatiÄri,Pakistan,Sindh,1170677
Mastung,Pakistan,BalochistÄn,1170706
Mardan,Pakistan,Khyber Pakhtunkhwa,1170880
MÄnsehra,Pakistan,Khyber Pakhtunkhwa,1170951
Mangla,Pakistan,Punjab,1171050
Mandi BahÄuddÄ«n,Pakistan,Punjab,1171123
MÄnÄnwÄla,Pakistan,Punjab,1171165
MÄmu KÄnjan,Pakistan,Punjab,1171198
Malir Cantonment,Pakistan,Sindh,1171305
MalakwÄl,Pakistan,Punjab,1171376
Mailsi,Pakistan,Punjab,1171502
Mach,Pakistan,BalochistÄn,1171757
Loralai,Pakistan,BalochistÄn,1171868
LodhrÄn,Pakistan,Punjab,1171965
Layyah,Pakistan,Punjab,1172035
LÄrkÄna,Pakistan,Sindh,1172128
LÄliÄn,Pakistan,Punjab,1172295
LÄla MÅ«sa,Pakistan,Punjab,1172318
Lakki Marwat,Pakistan,Khyber Pakhtunkhwa,1172339
Lahore,Pakistan,Punjab,1172451
LadhewÄla WarÄich,Pakistan,Punjab,1172488
LÄchi,Pakistan,Khyber Pakhtunkhwa,1172513
Kunri,Pakistan,Sindh,1172657
KunjÄh,Pakistan,Punjab,1172663
KundiÄn,Pakistan,Punjab,1172682
KulÄchi,Pakistan,Khyber Pakhtunkhwa,1172779
Kot SamÄba,Pakistan,Punjab,1172888
Kotri,Pakistan,Sindh,1172904
Kot RÄdha Kishan,Pakistan,Punjab,1172915
Kot MÅ«min,Pakistan,Punjab,1172964
Kot Malik,Pakistan,BalochistÄn,1172993
Kotli LohÄrÄn,Pakistan,Punjab,1173025
Kotli,Pakistan,Azad Kashmir,1173055
Kot GhulÄm Muhammad,Pakistan,Punjab,1173272
Kot Diji,Pakistan,Sindh,1173302
Kot Addu,Pakistan,Punjab,1173378
KohÄt,Pakistan,Khyber Pakhtunkhwa,1173491
KhushÄb,Pakistan,Punjab,1173687
KhurriÄnwÄla,Pakistan,Punjab,1173692
Khewra,Pakistan,Punjab,1173920
KhÄriÄn,Pakistan,Punjab,1174042
KhÄrÄn,Pakistan,BalochistÄn,1174062
KhÄnpur,Pakistan,Punjab,1174167
KhÄnpur,Pakistan,Sindh,1174171
KhÄngarh,Pakistan,Punjab,1174211
KhÄngÄh DogrÄn,Pakistan,Punjab,1174217
KhalÄbat,Pakistan,Khyber Pakhtunkhwa,1174301
Khairpur Nathan ShÄh,Pakistan,Sindh,1174344
Khairpur,Pakistan,Punjab,1174355
Khairpur,Pakistan,Sindh,1174357
KasÅ«r,Pakistan,Punjab,1174625
Kashmor,Pakistan,Sindh,1174653
Karor,Pakistan,Punjab,1174720
Karachi,Pakistan,Sindh,1174872
Kanganpur,Pakistan,Punjab,1174984
KandiÄro,Pakistan,Sindh,1175010
Kandhkot,Pakistan,Sindh,1175021
KÄmra,Pakistan,Punjab,1175082
Kamoke,Pakistan,Punjab,1175088
KamÄ«r,Pakistan,Punjab,1175098
Kamar MushÄni,Pakistan,Punjab,1175125
KamÄlia,Pakistan,Punjab,1175156
KalÅ«r Kot,Pakistan,Punjab,1175180
Kallar KahÄr,Pakistan,Punjab,1175232
KÄleke Mandi,Pakistan,Punjab,1175283
KalÄt,Pakistan,BalochistÄn,1175296
KÄlÄbÄgh,Pakistan,Punjab,1175365
KahÅ«ta,Pakistan,Punjab,1175436
Kohror Pakka,Pakistan,Punjab,1175446
KÄhna,Pakistan,Punjab,1175453
KabÄ«rwÄla,Pakistan,Punjab,1175560
Johi,Pakistan,Sindh,1175678
JÄ«wani,Pakistan,BalochistÄn,1175712
Jhumra,Pakistan,Punjab,1175748
Jhol,Pakistan,Sindh,1175762
Jhelum,Pakistan,Punjab,1175864
JhawÄriÄn,Pakistan,Punjab,1175870
Jhang Sadr,Pakistan,Punjab,1175892
JauharÄbÄd,Pakistan,Punjab,1176022
Jatoi ShimÄli,Pakistan,Punjab,1176035
JarÄnwÄla,Pakistan,Punjab,1176106
Jand,Pakistan,Punjab,1176218
JÄmpur,Pakistan,Punjab,1176241
JalÄlpur PÄ«rwÄla,Pakistan,Punjab,1176358
JalÄlpur,Pakistan,Punjab,1176368
JahÄniÄn ShÄh,Pakistan,Punjab,1176444
JacobÄbÄd,Pakistan,Sindh,1176515
Islamabad,Pakistan,IslÄmÄbÄd,1176615
Hyderabad,Pakistan,Sindh,1176734
Hujra,Pakistan,Punjab,1176800
Hingorja,Pakistan,Sindh,1176889
Hazro,Pakistan,Punjab,1176948
HaveliÄn,Pakistan,Khyber Pakhtunkhwa,1176995
Haveli,Pakistan,Punjab,1176997
HÄsilpur,Pakistan,Punjab,1177042
Hasan AbdÄl,Pakistan,Punjab,1177064
Haru Zbad,Pakistan,Punjab,1177073
Harnoli,Pakistan,Punjab,1177089
HarÄ«pur,Pakistan,Khyber Pakhtunkhwa,1177107
Hangu,Pakistan,Khyber Pakhtunkhwa,1177203
HÄla,Pakistan,Sindh,1177278
HÄfizÄbÄd,Pakistan,Punjab,1177384
HadÄli,Pakistan,Punjab,1177397
Gwadar,Pakistan,BalochistÄn,1177446
GujrÄt,Pakistan,Punjab,1177654
GujrÄnwÄla,Pakistan,Punjab,1177662
GÅ«jar KhÄn,Pakistan,Punjab,1177682
Gojra,Pakistan,Punjab,1178231
Ghotki,Pakistan,Sindh,1178456
Ghauspur,Pakistan,Sindh,1178560
GhÄro,Pakistan,Sindh,1178587
Garh MahÄrÄja,Pakistan,Punjab,1178841
Gambat,Pakistan,Sindh,1179061
Fort AbbÄs,Pakistan,Punjab,1179223
Fazalpur,Pakistan,Punjab,1179255
Chak Two Hundred Forty-Nine TDA,Pakistan,Punjab,1179305
Faruka,Pakistan,Punjab,1179346
FaqÄ«rwÄli,Pakistan,Punjab,1179377
FaisalÄbÄd,Pakistan,Punjab,1179400
EminÄbÄd,Pakistan,Punjab,1179406
DunyÄpur,Pakistan,Punjab,1179450
Dunga Bunga,Pakistan,Punjab,1179463
DullewÄla,Pakistan,Punjab,1179496
DÄ«r,Pakistan,Khyber Pakhtunkhwa,1179757
DÄ«pÄlpur,Pakistan,Punjab,1179760
Dinga,Pakistan,Punjab,1179790
Dijkot,Pakistan,Punjab,1179834
Digri,Pakistan,Sindh,1179837
Dhoro Naro,Pakistan,Sindh,1179902
Dhanot,Pakistan,Punjab,1180133
Dera IsmÄÄ«l KhÄn,Pakistan,Khyber Pakhtunkhwa,1180281
Dera Ghazi Khan,Pakistan,Punjab,1180289
Dera Bugti,Pakistan,BalochistÄn,1180295
Daur,Pakistan,Sindh,1180374
DÄÅ«d Khel,Pakistan,Punjab,1180419
Daska,Pakistan,Punjab,1180436
Darya KhÄn,Pakistan,Punjab,1180454
DÄjal,Pakistan,Punjab,1180752
Dadu,Pakistan,Sindh,1180809
DÄdhar,Pakistan,BalochistÄn,1180825
ChÅ«niÄn,Pakistan,Punjab,1180942
ChÅ«har KÄna,Pakistan,Punjab,1180983
Chor,Pakistan,Sindh,1181022
Choa SaidÄn ShÄh,Pakistan,Punjab,1181053
ChishtiÄn Mandi,Pakistan,Punjab,1181073
Chiniot,Pakistan,Punjab,1181096
ChÄ«chÄwatni,Pakistan,Punjab,1181163
Chawinda,Pakistan,Punjab,1181352
Charsadda,Pakistan,Khyber Pakhtunkhwa,1181439
Chaman,Pakistan,BalochistÄn,1181611
ChakwÄl,Pakistan,Punjab,1181636
Chak Ä€zam Saffo,Pakistan,Punjab,1181887
BÅ«rewÄla,Pakistan,Punjab,1182092
BhopÄlwÄla,Pakistan,Punjab,1182577
Bhit ShÄh,Pakistan,Sindh,1182607
Bhimbar,Pakistan,Azad Kashmir,1182637
Bhera,Pakistan,Punjab,1182665
BhawÄna,Pakistan,Punjab,1182682
BhÄn,Pakistan,Sindh,1182775
BhalwÄl,Pakistan,Punjab,1182787
Bhakkar,Pakistan,Punjab,1182815
BhÄi Pheru,Pakistan,Punjab,1182829
Bela,Pakistan,BalochistÄn,1182998
Bat Khela,Pakistan,Khyber Pakhtunkhwa,1183090
BasÄ«rpur,Pakistan,Punjab,1183224
Bannu,Pakistan,Khyber Pakhtunkhwa,1183460
BahÄwalpur,Pakistan,Punjab,1183880
BahÄwalnagar,Pakistan,Punjab,1183883
BadÄ«n,Pakistan,Sindh,1184055
Baddomalhi,Pakistan,Punjab,1184075
Attock City,Pakistan,Punjab,1184249
Ä€rifwÄla,Pakistan,Punjab,1184370
Amangarh,Pakistan,Khyber Pakhtunkhwa,1184569
AlÄ«pur,Pakistan,Punjab,1184655
Akora,Pakistan,Khyber Pakhtunkhwa,1184752
Ahmadpur East,Pakistan,Punjab,1184845
AbbottÄbÄd,Pakistan,Khyber Pakhtunkhwa,1185056
BahÄwalnagar,Pakistan,Punjab,1332083
Nowshera Cantonment,Pakistan,Khyber Pakhtunkhwa,1341204
Ahmadpur SiÄl,Pakistan,Punjab,1356491
New BÄdÄh,Pakistan,Sindh,1357699
Tando GhulÄm Ali,Pakistan,Sindh,1360491
SethÄrja Old,Pakistan,Sindh,1412008
RisÄlpur,Pakistan,Khyber Pakhtunkhwa,1448637
Malakwal City,Pakistan,Punjab,6457378
Å»yrardÃ³w,Poland,Masovian Voivodeship,752967
Å»oliborz,Poland,Masovian Voivodeship,753142
Zielonka,Poland,Masovian Voivodeship,753276
ZamoÅ›Ä‡,Poland,Lublin Voivodeship,753866
ZambrÃ³w,Poland,Podlasie,753895
ZÄ…bki,Poland,Masovian Voivodeship,754351
WyszkÃ³w,Poland,Masovian Voivodeship,754454
WoÅ‚omin,Poland,Masovian Voivodeship,754800
Wola,Poland,Masovian Voivodeship,755330
WÅ‚ochy,Poland,Masovian Voivodeship,755475
Wieliczka,Poland,Lesser Poland Voivodeship,755889
WesoÅ‚a,Poland,Masovian Voivodeship,756004
Wawer,Poland,Masovian Voivodeship,756092
Warsaw,Poland,Masovian Voivodeship,756135
Ursus,Poland,Masovian Voivodeship,756320
TomaszÃ³w Mazowiecki,Poland,ÅÃ³dÅº Voivodeship,756867
TomaszÃ³w Lubelski,Poland,Lublin Voivodeship,756868
TarnÃ³w,Poland,Lesser Poland Voivodeship,757026
Tarnobrzeg,Poland,Subcarpathian Voivodeship,757033
TargÃ³wek,Poland,Masovian Voivodeship,757065
Szczytno,Poland,Warmian-Masurian Voivodeship,757357
Åšwidnik,Poland,Lublin Voivodeship,757692
SuwaÅ‚ki,Poland,Podlasie,757718
SulejÃ³wek,Poland,Masovian Voivodeship,757809
StaszÃ³w,Poland,ÅšwiÄ™tokrzyskie,758252
Starachowice,Poland,ÅšwiÄ™tokrzyskie,758390
Stalowa Wola,Poland,Subcarpathian Voivodeship,758445
ÅšrÃ³dmieÅ›cie,Poland,Masovian Voivodeship,758470
SokoÅ‚Ã³w Podlaski,Poland,Masovian Voivodeship,758626
SokÃ³Å‚ka,Poland,Podlasie,758651
Sochaczew,Poland,Masovian Voivodeship,758682
Skierniewice,Poland,ÅÃ³dÅº Voivodeship,759123
SkarÅ¼ysko-Kamienna,Poland,ÅšwiÄ™tokrzyskie,759141
Siemiatycze,Poland,Podlasie,759320
Siedlce,Poland,Masovian Voivodeship,759412
Sanok,Poland,Subcarpathian Voivodeship,759591
Sandomierz,Poland,ÅšwiÄ™tokrzyskie,759603
RzeszÃ³w,Poland,Subcarpathian Voivodeship,759734
Ropczyce,Poland,Subcarpathian Voivodeship,760343
RembertÃ³w,Poland,Masovian Voivodeship,760503
Rawa Mazowiecka,Poland,ÅÃ³dÅº Voivodeship,760584
RadzyÅ„ Podlaski,Poland,Lublin Voivodeship,760680
Radom,Poland,Masovian Voivodeship,760778
PuÅ‚tusk,Poland,Masovian Voivodeship,760917
PuÅ‚awy,Poland,Lublin Voivodeship,760924
Przeworsk,Poland,Subcarpathian Voivodeship,761131
PrzemyÅ›l,Poland,Subcarpathian Voivodeship,761168
Przasnysz,Poland,Masovian Voivodeship,761218
PruszkÃ³w,Poland,Masovian Voivodeship,761228
PÅ‚oÅ„sk,Poland,Masovian Voivodeship,762021
Pisz,Poland,Warmian-Masurian Voivodeship,762120
Pionki,Poland,Masovian Voivodeship,762199
PiastÃ³w,Poland,Masovian Voivodeship,762381
Piaseczno,Poland,Masovian Voivodeship,762423
Otwock,Poland,Masovian Voivodeship,762788
OstrÃ³w Mazowiecka,Poland,Masovian Voivodeship,762850
Ostrowiec ÅšwiÄ™tokrzyski,Poland,ÅšwiÄ™tokrzyskie,762863
OstroÅ‚Ä™ka,Poland,Masovian Voivodeship,762909
Opoczno,Poland,ÅÃ³dÅº Voivodeship,763111
Olsztyn,Poland,Warmian-Masurian Voivodeship,763166
Olecko,Poland,Warmian-Masurian Voivodeship,763291
Ochota,Poland,Masovian Voivodeship,763442
Nowy Targ,Poland,Lesser Poland Voivodeship,763523
Nowy SÄ…cz,Poland,Lesser Poland Voivodeship,763534
Nowy DwÃ³r Mazowiecki,Poland,Masovian Voivodeship,763556
Nisko,Poland,Subcarpathian Voivodeship,763829
MrÄ…gowo,Poland,Warmian-Masurian Voivodeship,764312
MokotÃ³w,Poland,Masovian Voivodeship,764484
MÅ‚awa,Poland,Masovian Voivodeship,764634
MiÅ„sk Mazowiecki,Poland,Masovian Voivodeship,764679
MilanÃ³wek,Poland,Masovian Voivodeship,764749
Mielec,Poland,Subcarpathian Voivodeship,764849
MiÄ™dzyrzec Podlaski,Poland,Lublin Voivodeship,764862
Marki,Poland,Masovian Voivodeship,765191
ÅukÃ³w,Poland,Lublin Voivodeship,765749
Lublin,Poland,Lublin Voivodeship,765876
LubartÃ³w,Poland,Lublin Voivodeship,765927
ÅomÅ¼a,Poland,Podlasie,766027
Åomianki,Poland,Masovian Voivodeship,766042
Lidzbark WarmiÅ„ski,Poland,Warmian-Masurian Voivodeship,766307
Legionowo,Poland,Masovian Voivodeship,766555
ÅÄ™czna,Poland,Lublin Voivodeship,766583
Åapy,Poland,Podlasie,766783
ÅaÅ„cut,Poland,Subcarpathian Voivodeship,766810
Krosno,Poland,Subcarpathian Voivodeship,767470
Krasnystaw,Poland,Lublin Voivodeship,767605
KraÅ›nik,Poland,Lublin Voivodeship,767623
Kozienice,Poland,Masovian Voivodeship,767814
Konstancin-Jeziorna,Poland,Masovian Voivodeship,768216
KoÅ„skie,Poland,ÅšwiÄ™tokrzyskie,768218
KobyÅ‚ka,Poland,Masovian Voivodeship,768905
Kielce,Poland,ÅšwiÄ™tokrzyskie,769250
KÄ™trzyn,Poland,Warmian-Masurian Voivodeship,769274
Kabaty,Poland,Masovian Voivodeship,769893
JÃ³zefÃ³w,Poland,Masovian Voivodeship,769981
JÄ™drzejÃ³w,Poland,ÅšwiÄ™tokrzyskie,770157
JasÅ‚o,Poland,Subcarpathian Voivodeship,770293
JarosÅ‚aw,Poland,Subcarpathian Voivodeship,770380
HrubieszÃ³w,Poland,Lublin Voivodeship,770966
HajnÃ³wka,Poland,Podlasie,771158
Grodzisk Mazowiecki,Poland,Masovian Voivodeship,771401
Grajewo,Poland,Podlasie,771506
Gorlice,Poland,Lesser Poland Voivodeship,771804
GiÅ¼ycko,Poland,Warmian-Masurian Voivodeship,772195
GierÅ‚oÅ¼,Poland,Warmian-Masurian Voivodeship,772227
Garwolin,Poland,Masovian Voivodeship,772339
EÅ‚k,Poland,Warmian-Masurian Voivodeship,772621
DziaÅ‚dowo,Poland,Warmian-Masurian Voivodeship,772748
DÄ™blin,Poland,Lublin Voivodeship,773357
DÄ™bica,Poland,Subcarpathian Voivodeship,773380
CiechanÃ³w,Poland,Masovian Voivodeship,774208
CheÅ‚m,Poland,Lublin Voivodeship,774558
Busko-ZdrÃ³j,Poland,ÅšwiÄ™tokrzyskie,774747
Brzesko,Poland,Lesser Poland Voivodeship,775183
Bochnia,Poland,Lesser Poland Voivodeship,775758
BiÅ‚goraj,Poland,Lublin Voivodeship,775922
Bielsk Podlaski,Poland,Podlasie,775986
Bielany,Poland,Masovian Voivodeship,776029
BiaÅ‚ystok,Poland,Podlasie,776069
BiaÅ‚oÅ‚eka,Poland,Masovian Voivodeship,776103
BiaÅ‚a Podlaska,Poland,Lublin Voivodeship,776175
Bemowo,Poland,Masovian Voivodeship,776251
Bartoszyce,Poland,Warmian-Masurian Voivodeship,776337
AugustÃ³w,Poland,Podlasie,776597
Å»ywiec,Poland,Silesian Voivodeship,3079855
Å»ory,Poland,Silesian Voivodeship,3080004
ZÅ‚otÃ³w,Poland,Greater Poland Voivodeship,3080071
ZÅ‚otoryja,Poland,Lower Silesian Voivodeship,3080074
Zielona GÃ³ra,Poland,Lubusz,3080165
Zgorzelec,Poland,Lower Silesian Voivodeship,3080231
Zgierz,Poland,ÅÃ³dÅº Voivodeship,3080251
ZduÅ„ska Wola,Poland,ÅÃ³dÅº Voivodeship,3080414
Zawiercie,Poland,Silesian Voivodeship,3080526
Å»ary,Poland,Lubusz,3080644
Zakopane,Poland,Lesser Poland Voivodeship,3080866
Å»agaÅ„,Poland,Lubusz,3080944
Zabrze,Poland,Silesian Voivodeship,3080985
ZÄ…bkowice ÅšlÄ…skie,Poland,Lower Silesian Voivodeship,3081046
WrzeÅ›nia,Poland,Greater Poland Voivodeship,3081324
WrocÅ‚aw,Poland,Lower Silesian Voivodeship,3081368
WodzisÅ‚aw ÅšlÄ…ski,Poland,Silesian Voivodeship,3081677
WÅ‚ocÅ‚awek,Poland,Kujawsko-Pomorskie,3081741
WieluÅ„,Poland,ÅÃ³dÅº Voivodeship,3082197
Wejherowo,Poland,Pomeranian Voivodeship,3082473
WaÅ‚cz,Poland,West Pomeranian Voivodeship,3082704
WaÅ‚brzych,Poland,Lower Silesian Voivodeship,3082707
WÄ…growiec,Poland,Greater Poland Voivodeship,3082712
Wadowice,Poland,Lesser Poland Voivodeship,3082722
UstroÅ„,Poland,Silesian Voivodeship,3082751
Ustka,Poland,Pomeranian Voivodeship,3082756
Tychy,Poland,Silesian Voivodeship,3082914
Turek,Poland,Greater Poland Voivodeship,3082998
Trzebinia,Poland,Lesser Poland Voivodeship,3083111
Trzcianka,Poland,Greater Poland Voivodeship,3083185
ToruÅ„,Poland,Kujawsko-Pomorskie,3083271
Tczew,Poland,Pomeranian Voivodeship,3083426
Tarnowskie GÃ³ry,Poland,Silesian Voivodeship,3083440
Szczecinek,Poland,West Pomeranian Voivodeship,3083826
Szczecin,Poland,West Pomeranian Voivodeship,3083829
SzamotuÅ‚y,Poland,Greater Poland Voivodeship,3083878
ÅšwinoujÅ›cie,Poland,West Pomeranian Voivodeship,3083955
ÅšwiÄ™tochÅ‚owice,Poland,Silesian Voivodeship,3083988
Åšwiebodzin,Poland,Lubusz,3084062
Åšwiecie,Poland,Kujawsko-Pomorskie,3084074
Åšwiebodzice,Poland,Lower Silesian Voivodeship,3084084
Åšwidwin,Poland,West Pomeranian Voivodeship,3084085
Åšwidnica,Poland,Lower Silesian Voivodeship,3084093
SwarzÄ™dz,Poland,Greater Poland Voivodeship,3084130
SulechÃ³w,Poland,Lubusz,3084241
Strzelce Opolskie,Poland,Opole Voivodeship,3084415
Strzegom,Poland,Lower Silesian Voivodeship,3084440
Starogard GdaÅ„ski,Poland,Pomeranian Voivodeship,3084826
Stargard SzczeciÅ„ski,Poland,West Pomeranian Voivodeship,3084840
Åšroda Wielkopolska,Poland,Greater Poland Voivodeship,3085045
Åšrem,Poland,Greater Poland Voivodeship,3085056
Sosnowiec,Poland,Silesian Voivodeship,3085128
Sopot,Poland,Pomeranian Voivodeship,3085151
Solec Kujawski,Poland,Kujawsko-Pomorskie,3085172
SÅ‚upsk,Poland,Pomeranian Voivodeship,3085450
SÅ‚ubice,Poland,Lubusz,3085495
Skawina,Poland,Lesser Poland Voivodeship,3085807
Sierpc,Poland,Masovian Voivodeship,3085941
Sieradz,Poland,ÅÃ³dÅº Voivodeship,3085978
Siemianowice ÅšlÄ…skie,Poland,Silesian Voivodeship,3086024
Rypin,Poland,Kujawsko-Pomorskie,3086511
RyduÅ‚towy,Poland,Silesian Voivodeship,3086531
Rybnik,Poland,Silesian Voivodeship,3086586
Rumia,Poland,Pomeranian Voivodeship,3086706
Ruda ÅšlÄ…ska,Poland,Silesian Voivodeship,3086800
Reda,Poland,Pomeranian Voivodeship,3087281
Rawicz,Poland,Greater Poland Voivodeship,3087307
RadzionkÃ³w,Poland,Silesian Voivodeship,3087418
Radomsko,Poland,ÅÃ³dÅº Voivodeship,3087497
Radlin,Poland,Silesian Voivodeship,3087529
RacibÃ³rz,Poland,Silesian Voivodeship,3087584
Pyskowice,Poland,Silesian Voivodeship,3087628
Pszczyna,Poland,Silesian Voivodeship,3087705
Pruszcz GdaÅ„ski,Poland,Pomeranian Voivodeship,3088034
Prudnik,Poland,Opole Voivodeship,3088065
PoznaÅ„,Poland,Greater Poland Voivodeship,3088171
Polkowice,Poland,Lower Silesian Voivodeship,3088435
Police,Poland,West Pomeranian Voivodeship,3088461
PÅ‚ock,Poland,Masovian Voivodeship,3088825
Pleszew,Poland,Greater Poland Voivodeship,3088848
PiotrkÃ³w Trybunalski,Poland,ÅÃ³dÅº Voivodeship,3088972
PiÅ‚a,Poland,Greater Poland Voivodeship,3089033
Piekary ÅšlÄ…skie,Poland,Silesian Voivodeship,3089125
Pabianice,Poland,ÅÃ³dÅº Voivodeship,3089578
OzorkÃ³w,Poland,ÅÃ³dÅº Voivodeship,3089582
OÅ›wiÄ™cim,Poland,Lesser Poland Voivodeship,3089658
OstrÃ³w Wielkopolski,Poland,Greater Poland Voivodeship,3089684
OstrÃ³da,Poland,Warmian-Masurian Voivodeship,3089779
Orzesze,Poland,Silesian Voivodeship,3089965
Opole,Poland,Opole Voivodeship,3090048
Olkusz,Poland,Lesser Poland Voivodeship,3090146
OleÅ›nica,Poland,Lower Silesian Voivodeship,3090170
OÅ‚awa,Poland,Lower Silesian Voivodeship,3090205
Oborniki,Poland,Greater Poland Voivodeship,3090403
Nysa,Poland,Opole Voivodeship,3090436
Nowy TomyÅ›l,Poland,Greater Poland Voivodeship,3090452
Nowogard,Poland,West Pomeranian Voivodeship,3090558
Nowa SÃ³l,Poland,Lubusz,3090764
Nowa Ruda,Poland,Lower Silesian Voivodeship,3090768
NamysÅ‚Ã³w,Poland,Opole Voivodeship,3091141
NakÅ‚o nad NoteciÄ…,Poland,Kujawsko-Pomorskie,3091150
MyszkÃ³w,Poland,Silesian Voivodeship,3091217
MysÅ‚owice,Poland,Silesian Voivodeship,3091232
MyÅ›lenice,Poland,Lesser Poland Voivodeship,3091256
MikoÅ‚Ã³w,Poland,Silesian Voivodeship,3091831
MiÄ™dzyrzecz,Poland,Lubusz,3091969
Malbork,Poland,Pomeranian Voivodeship,3092472
LuboÅ„,Poland,Greater Poland Voivodeship,3092856
Lubliniec,Poland,Silesian Voivodeship,3092906
Lubin,Poland,Lower Silesian Voivodeship,3092931
LubaÅ„,Poland,Lower Silesian Voivodeship,3093040
Åowicz,Poland,ÅÃ³dÅº Voivodeship,3093066
ÅÃ³dÅº,Poland,ÅÃ³dÅº Voivodeship,3093133
LibiÄ…Å¼,Poland,Lesser Poland Voivodeship,3093457
Leszno,Poland,Greater Poland Voivodeship,3093524
Legnica,Poland,Lower Silesian Voivodeship,3093692
LÄ™dziny,Poland,Silesian Voivodeship,3093708
ÅÄ™czyca,Poland,ÅÃ³dÅº Voivodeship,3093726
LÄ™bork,Poland,Pomeranian Voivodeship,3093739
Åaziska GÃ³rne,Poland,Silesian Voivodeship,3093785
Åask,Poland,ÅÃ³dÅº Voivodeship,3093902
Kwidzyn,Poland,Pomeranian Voivodeship,3094086
Kutno,Poland,ÅÃ³dÅº Voivodeship,3094170
Krotoszyn,Poland,Greater Poland Voivodeship,3094625
Krapkowice,Poland,Opole Voivodeship,3094788
KrakÃ³w,Poland,Lesser Poland Voivodeship,3094802
Koszalin,Poland,West Pomeranian Voivodeship,3095049
Kostrzyn nad OdrÄ…,Poland,Lubusz,3095057
KoÅ›cierzyna,Poland,Pomeranian Voivodeship,3095126
KoÅ›cian,Poland,Greater Poland Voivodeship,3095151
KonstantynÃ³w ÅÃ³dzki,Poland,ÅÃ³dÅº Voivodeship,3095277
Konin,Poland,Greater Poland Voivodeship,3095321
KoÅ‚obrzeg,Poland,West Pomeranian Voivodeship,3095795
KoÅ‚o,Poland,Greater Poland Voivodeship,3095797
KnurÃ³w,Poland,Silesian Voivodeship,3095971
Kluczbork,Poland,Opole Voivodeship,3096003
KÅ‚odzko,Poland,Lower Silesian Voivodeship,3096053
KÄ™ty,Poland,Lesser Poland Voivodeship,3096328
KÄ™dzierzyn-KoÅºle,Poland,Opole Voivodeship,3096372
Katowice,Poland,Silesian Voivodeship,3096472
Kartuzy,Poland,Pomeranian Voivodeship,3096525
Kamienna GÃ³ra,Poland,Lower Silesian Voivodeship,3096779
Kalisz,Poland,Greater Poland Voivodeship,3096880
Jelenia GÃ³ra,Poland,Lower Silesian Voivodeship,3097257
Jelcz,Poland,Lower Silesian Voivodeship,3097271
Jaworzno,Poland,Silesian Voivodeship,3097333
Jawor,Poland,Lower Silesian Voivodeship,3097367
JastrzÄ™bie ZdrÃ³j,Poland,Silesian Voivodeship,3097391
Jarocin,Poland,Greater Poland Voivodeship,3097528
InowrocÅ‚aw,Poland,Kujawsko-Pomorskie,3097872
IÅ‚awa,Poland,Warmian-Masurian Voivodeship,3097902
Gubin,Poland,Lubusz,3098130
Gryfino,Poland,West Pomeranian Voivodeship,3098200
Gryfice,Poland,West Pomeranian Voivodeship,3098201
GrudziÄ…dz,Poland,Kujawsko-Pomorskie,3098218
Gostynin,Poland,Masovian Voivodeship,3098619
GostyÅ„,Poland,Greater Poland Voivodeship,3098625
GorzÃ³w Wielkopolski,Poland,Lubusz,3098722
GoleniÃ³w,Poland,West Pomeranian Voivodeship,3098966
Gniezno,Poland,Greater Poland Voivodeship,3099112
GÅ‚uchoÅ‚azy,Poland,Opole Voivodeship,3099169
GÅ‚owno,Poland,ÅÃ³dÅº Voivodeship,3099180
GÅ‚ogÃ³w,Poland,Lower Silesian Voivodeship,3099213
Gliwice,Poland,Silesian Voivodeship,3099230
Gdynia,Poland,Pomeranian Voivodeship,3099424
GdaÅ„sk,Poland,Pomeranian Voivodeship,3099434
Fordon,Poland,Kujawsko-Pomorskie,3099654
ElblÄ…g,Poland,Warmian-Masurian Voivodeship,3099759
DzierÅ¼oniÃ³w,Poland,Lower Silesian Voivodeship,3099828
DÄ…browa GÃ³rnicza,Poland,Silesian Voivodeship,3100796
CzÄ™stochowa,Poland,Silesian Voivodeship,3100946
Czerwionka-Leszczyny,Poland,Silesian Voivodeship,3100974
CzeladÅº,Poland,Silesian Voivodeship,3101057
Czechowice-Dziedzice,Poland,Silesian Voivodeship,3101076
Cieszyn,Poland,Silesian Voivodeship,3101321
ChrzanÃ³w,Poland,Lesser Poland Voivodeship,3101547
Choszczno,Poland,West Pomeranian Voivodeship,3101613
ChorzÃ³w,Poland,Silesian Voivodeship,3101619
Chojnice,Poland,Pomeranian Voivodeship,3101672
ChodzieÅ¼,Poland,Greater Poland Voivodeship,3101680
CheÅ‚mÅ¼a,Poland,Kujawsko-Pomorskie,3101787
CheÅ‚mno,Poland,Kujawsko-Pomorskie,3101795
BytÃ³w,Poland,Pomeranian Voivodeship,3101943
Bytom,Poland,Silesian Voivodeship,3101950
Bydgoszcz,Poland,Kujawsko-Pomorskie,3102014
Brzeg,Poland,Opole Voivodeship,3102459
Brodnica,Poland,Kujawsko-Pomorskie,3102627
Braniewo,Poland,Warmian-Masurian Voivodeship,3102677
BolesÅ‚awiec,Poland,Lower Silesian Voivodeship,3102987
BoguszÃ³w-Gorce,Poland,Lower Silesian Voivodeship,3103034
Bogatynia,Poland,Lower Silesian Voivodeship,3103096
BieruÅ„,Poland,Silesian Voivodeship,3103365
Bielsko-Biala,Poland,Silesian Voivodeship,3103402
Bielawa,Poland,Lower Silesian Voivodeship,3103476
BiaÅ‚ogard,Poland,West Pomeranian Voivodeship,3103556
BeÅ‚chatÃ³w,Poland,ÅÃ³dÅº Voivodeship,3103709
BÄ™dzin,Poland,Silesian Voivodeship,3103719
AndrychÃ³w,Poland,Lesser Poland Voivodeship,3104115
AleksandrÃ³w ÅÃ³dzki,Poland,ÅÃ³dÅº Voivodeship,3104132
UrsynÃ³w,Poland,Masovian Voivodeship,6545326
Praga PÃ³Å‚noc,Poland,Masovian Voivodeship,6545347
Praga PoÅ‚udnie,Poland,Masovian Voivodeship,6545348
Jelcz Laskowice,Poland,Lower Silesian Voivodeship,7303641
Saint-Pierre,Saint Pierre and Miquelon,Saint-Pierre,3424934
Adamstown,Pitcairn,N/A,4030723
Aguadilla,Puerto Rico,Aguadilla,4562506
Arecibo,Puerto Rico,Arecibo,4562635
Barceloneta,Puerto Rico,Barceloneta,4562768
BayamÃ³n,Puerto Rico,BayamÃ³n,4562831
Caguas,Puerto Rico,Caguas,4563008
Candelaria,Puerto Rico,Toa Baja,4563122
Carolina,Puerto Rico,Carolina,4563243
CataÃ±o,Puerto Rico,Catano,4563298
Cayey,Puerto Rico,Cayey,4563308
Fajardo,Puerto Rico,Fajardo,4564946
Guayama,Puerto Rico,Guayama,4565105
Guaynabo,Puerto Rico,Guaynabo,4565119
Humacao,Puerto Rico,Humacao,4565564
Levittown,Puerto Rico,Toa Baja,4566002
ManatÃ­,Puerto Rico,Manati,4566137
MayagÃ¼ez,Puerto Rico,Mayaguez,4566385
Ponce,Puerto Rico,Ponce,4566880
San Juan,Puerto Rico,San Juan,4568127
Trujillo Alto,Puerto Rico,Trujillo Alto,4568451
Vega Baja,Puerto Rico,Vega Baja,4568533
Yauco,Puerto Rico,Yauco,4568917
Rafaá¸©,Palestinian Territory,Gaza Strip,281102
An NuÅŸayrÄt,Palestinian Territory,Gaza Strip,281109
KhÄn YÅ«nis,Palestinian Territory,Gaza Strip,281124
JabÄlyÄ,Palestinian Territory,Gaza Strip,281129
Gaza,Palestinian Territory,Gaza Strip,281133
Dayr al Balaá¸©,Palestinian Territory,Gaza Strip,281141
Bayt LÄhyÄ,Palestinian Territory,Gaza Strip,281145
Bayt á¸¨ÄnÅ«n,Palestinian Territory,Gaza Strip,281146
BanÄ« SuhaylÄ,Palestinian Territory,Gaza Strip,281148
Al Burayj,Palestinian Territory,Gaza Strip,281161
â€˜AbasÄn al KabÄ«rah,Palestinian Territory,Gaza Strip,281165
Yuta,Palestinian Territory,West Bank,281292
Å¢Å«lkarm,Palestinian Territory,West Bank,281577
Å¢Å«bÄs,Palestinian Territory,West Bank,281581
Saâ€˜Ä«r,Palestinian Territory,West Bank,281793
Ramallah,Palestinian Territory,West Bank,282239
QalqÄ«lyah,Palestinian Territory,West Bank,282457
QabÄÅ£Ä«yah,Palestinian Territory,West Bank,282476
Nablus,Palestinian Territory,West Bank,282615
JanÄ«n,Palestinian Territory,West Bank,283506
IdhnÄ,Palestinian Territory,West Bank,283621
á¸¨alá¸©Å«l,Palestinian Territory,West Bank,283806
DÅ«rÄ,Palestinian Territory,West Bank,284011
Bethlehem,Palestinian Territory,West Bank,284315
Bayt JÄlÄ,Palestinian Territory,West Bank,284324
BanÄ« Naâ€˜Ä«m,Palestinian Territory,West Bank,284431
BalÄÅ£ah,Palestinian Territory,West Bank,284446
AzÌ§ ZÌ§ÄhirÄ«yah,Palestinian Territory,West Bank,284486
As SamÅ«â€˜,Palestinian Territory,West Bank,284583
Ar RÄm wa á¸Äá¸©iyat al BarÄ«d,Palestinian Territory,West Bank,284890
Jericho,Palestinian Territory,West Bank,284899
Al YÄmÅ«n,Palestinian Territory,West Bank,284999
Hebron,Palestinian Territory,West Bank,285066
Al BÄ«rah,Palestinian Territory,West Bank,285108
Al â€˜AyzarÄ«yah,Palestinian Territory,West Bank,285111
Old City,Palestinian Territory,West Bank,6945291
Al QarÄrah,Palestinian Territory,Gaza Strip,6967865
Az ZuwÄydah,Palestinian Territory,Gaza Strip,6967990
East Jerusalem,Palestinian Territory,West Bank,7303419
Vila Franca de Xira,Portugal,Lisbon,2261639
Vialonga,Portugal,Lisbon,2261697
Torres Vedras,Portugal,Lisbon,2262581
Tomar,Portugal,SantarÃ©m,2262644
Sintra,Portugal,Lisbon,2262912
Sesimbra,Portugal,SetÃºbal,2262957
SetÃºbal,Portugal,SetÃºbal,2262963
SÃ£o JoÃ£o da Talha,Portugal,Lisbon,2263326
SÃ£o Domingos de Rana,Portugal,Lisbon,2263352
SantarÃ©m,Portugal,SantarÃ©m,2263480
Santa Iria da AzÃ³ia,Portugal,Lisbon,2263523
SacavÃ©m,Portugal,Lisbon,2263667
Rio de Mouro,Portugal,Lisbon,2263827
Ramada,Portugal,Lisbon,2264087
Queluz,Portugal,Lisbon,2264268
Quarteira,Portugal,Faro,2264299
PÃ³voa de Santa Iria,Portugal,Lisbon,2264359
PortimÃ£o,Portugal,Faro,2264456
Portalegre,Portugal,Portalegre,2264508
Pontinha,Portugal,Lisbon,2264526
Pombal,Portugal,Leiria,2264575
Pinhal Novo,Portugal,SetÃºbal,2264718
Piedade,Portugal,SetÃºbal,2264736
Peniche,Portugal,Leiria,2264923
Parede,Portugal,Lisbon,2265169
Palmela,Portugal,SetÃºbal,2265223
PaÃ§o de Arcos,Portugal,Lisbon,2265326
OlhÃ£o,Portugal,Faro,2265447
Odivelas,Portugal,Lisbon,2265467
Montijo,Portugal,SetÃºbal,2265788
Monte Estoril,Portugal,Lisbon,2265927
Monsanto,Portugal,SantarÃ©m,2266249
Moita,Portugal,SetÃºbal,2266319
Marinha Grande,Portugal,Leiria,2266703
Loures,Portugal,Lisbon,2266977
LoulÃ©,Portugal,Faro,2266988
Lisbon,Portugal,Lisbon,2267057
Linda-a-Velha,Portugal,Lisbon,2267067
Leiria,Portugal,Leiria,2267095
Laranjeiro,Portugal,Faro,2267131
Lagos,Portugal,Faro,2267226
Funchal,Portugal,Madeira,2267827
Faro,Portugal,Faro,2268339
Ã‰vora,Portugal,Ã‰vora,2268406
Estoril,Portugal,Lisbon,2268436
Entroncamento,Portugal,SantarÃ©m,2268575
Corroios,Portugal,SetÃºbal,2269041
Charneca,Portugal,SetÃºbal,2269282
Castelo Branco,Portugal,Castelo Branco,2269514
Cascais,Portugal,Lisbon,2269594
Carnaxide,Portugal,Lisbon,2270157
Carcavelos,Portugal,Lisbon,2270184
Caparica,Portugal,SetÃºbal,2270229
Camarate,Portugal,Lisbon,2270377
CÃ¢mara de Lobos,Portugal,Madeira,2270380
Caldas da Rainha,Portugal,Leiria,2270437
CacÃ©m,Portugal,Lisbon,2270503
Belas,Portugal,Lisbon,2270981
Beja,Portugal,Beja,2270985
Barreiro,Portugal,SetÃºbal,2271071
Arrentela,Portugal,SetÃºbal,2271473
Amora,Portugal,SetÃºbal,2271680
Amadora,Portugal,Lisbon,2271772
Almada,Portugal,SetÃºbal,2271961
AlgÃ©s,Portugal,Lisbon,2271985
Alcabideche,Portugal,Lisbon,2272215
Albufeira,Portugal,Faro,2272222
Viseu,Portugal,Viseu,2732265
Vila Real,Portugal,Vila Real,2732438
Vilar de Andorinho,Portugal,Porto,2732475
Vila Nova de Gaia,Portugal,Porto,2732544
Vila do Conde,Portugal,Porto,2732649
Viana do Castelo,Portugal,Viana do Castelo,2732773
Valongo,Portugal,Porto,2732978
Sequeira,Portugal,Guarda,2734106
Senhora da Hora,Portugal,Porto,2734140
SÃ£o Pedro da Cova,Portugal,Porto,2734363
SÃ£o Mamede de Infesta,Portugal,Porto,2734434
SÃ£o JoÃ£o da Madeira,Portugal,Aveiro,2734484
Rio Tinto,Portugal,Porto,2735083
PÃ³voa de Varzim,Portugal,Porto,2735787
Porto,Portugal,Porto,2735943
Ponte de Lima,Portugal,Viana do Castelo,2736041
Pedroso,Portugal,Porto,2736521
Ovar,Portugal,Aveiro,2736930
Oliveira do Douro,Portugal,Porto,2737039
MonÃ§Ã£o,Portugal,Viana do Castelo,2737523
Matosinhos,Portugal,Porto,2737824
Maia,Portugal,Porto,2738014
LeÃ§a do Bailio,Portugal,Porto,2738347
LeÃ§a da Palmeira,Portugal,Porto,2738348
Ãlhavo,Portugal,Aveiro,2738707
GuimarÃ£es,Portugal,Braga,2738752
Guarda,Portugal,Guarda,2738785
Gondomar,Portugal,Porto,2738925
Feira,Portugal,Aveiro,2739723
FÃ¢nzeres,Portugal,Porto,2739756
Fafe,Portugal,Braga,2739788
Esposende,Portugal,Braga,2739848
Esposende,Portugal,Braga,2739849
Ermesinde,Portugal,Porto,2739997
Custoias,Portugal,Guarda,2740174
CovilhÃ£,Portugal,Castelo Branco,2740313
Coimbra,Portugal,Coimbra,2740637
Canidelo,Portugal,Porto,2741551
BraganÃ§a,Portugal,BraganÃ§a,2742027
Braga,Portugal,Braga,2742032
Bougado,Portugal,Porto,2742051
Barcelos,Portugal,Braga,2742416
Baguim do Monte,Portugal,Porto,2742506
Aveiro,Portugal,Aveiro,2742611
Ãguas Santas,Portugal,Porto,2743304
Ponta Delgada,Portugal,Azores,3372783
Melekeok,Palau,Melekeok,7303944
Villarrica,Paraguay,GuairÃ¡,3436714
Villa Hayes,Paraguay,Presidente Hayes,3436725
Villa Elisa,Paraguay,Central,3436728
San Lorenzo,Paraguay,Central,3437056
San Juan Bautista,Paraguay,Misiones,3437063
San Antonio,Paraguay,Central,3437127
Presidente Franco,Paraguay,Alto ParanÃ¡,3437444
Pilar,Paraguay,Ã‘eembucÃº,3437526
Pedro Juan Caballero,Paraguay,Amambay,3437547
Nemby,Paraguay,Central,3437665
Limpio,Paraguay,Central,3437842
LambarÃ©,Paraguay,Central,3437863
ItauguÃ¡,Paraguay,Central,3437918
ItÃ¡,Paraguay,Central,3437954
Fernando de la Mora,Paraguay,Central,3438115
EncarnaciÃ³n,Paraguay,ItapÃºa,3438735
Coronel Oviedo,Paraguay,CaaguazÃº,3438819
ConcepciÃ³n,Paraguay,ConcepciÃ³n,3438834
Colonia Mariano Roque Alonso,Paraguay,Central,3438995
Ciudad del Este,Paraguay,Alto ParanÃ¡,3439101
CapiatÃ¡,Paraguay,Central,3439214
CaazapÃ¡,Paraguay,CaazapÃ¡,3439297
CaaguazÃº,Paraguay,CaaguazÃº,3439317
CaacupÃ©,Paraguay,Cordillera,3439320
AsunciÃ³n,Paraguay,AsunciÃ³n,3439389
Umm ÅžalÄl Muá¸©ammad,Qatar,BaladÄ«yat Umm ÅžalÄl,289523
Ar RayyÄn,Qatar,BaladÄ«yat ar RayyÄn,289888
Al Wakrah,Qatar,Al Wakrah,289915
Al Khawr,Qatar,Al Khawr,289962
Doha,Qatar,BaladÄ«yat ad Dawá¸©ah,290030
Saint-Pierre,Reunion,RÃ©union,935214
Saint-Paul,Reunion,RÃ©union,935221
Saint-Louis,Reunion,RÃ©union,935223
Saint-Leu,Reunion,RÃ©union,935225
Saint-Joseph,Reunion,RÃ©union,935227
Sainte-Suzanne,Reunion,RÃ©union,935248
Sainte-Marie,Reunion,RÃ©union,935255
Saint-Denis,Reunion,RÃ©union,935264
Saint-BenoÃ®t,Reunion,RÃ©union,935267
Saint-AndrÃ©,Reunion,RÃ©union,935268
Le Tampon,Reunion,RÃ©union,935582
Le Port,Reunion,RÃ©union,935616
La Possession,Reunion,RÃ©union,935691
Piton Saint-Leu,Reunion,N/A,7932385
Zimnicea,Romania,Teleorman,662187
ZÄƒrneÈ™ti,Romania,BraÅŸov,662284
ZalÄƒu,Romania,SÄƒlaj,662334
Vulcan,Romania,Hunedoara,662432
Voluntari,Romania,Ilfov,662476
ViÅŸeu de Sus,Romania,MaramureÅŸ,662699
Vatra Dornei,Romania,Suceava,663100
Vaslui,Romania,Vaslui,663118
Urziceni,Romania,IalomiÅ£a,664074
Turnu MÄƒgurele,Romania,Teleorman,664437
Turda,Romania,Cluj,664460
Tulcea,Romania,Tulcea,664518
TÃ¢rnÄƒveni,Romania,MureÅŸ,664963
TÃ¢rgu Secuiesc,Romania,Covasna,665000
TÃ¢rgu NeamÅ£,Romania,NeamÅ£,665003
TÃ¢rgu-MureÅŸ,Romania,MureÅŸ,665004
TÃ¢rgu Jiu,Romania,Gorj,665010
TÃ¢rgoviÅŸte,Romania,DÃ¢mboviÅ£a,665024
TimiÅŸoara,Romania,TimiÅŸ,665087
Tecuci,Romania,GalaÅ£i,665355
Suceava,Romania,Suceava,665850
Slatina,Romania,Olt,666767
Åžimleu Silvaniei,Romania,SÄƒlaj,667101
Sighetu MarmaÅ£iei,Romania,MaramureÅŸ,667227
Sibiu,Romania,Sibiu,667268
SfÃ¢ntu-Gheorghe,Romania,Covasna,667303
SebeÅŸ,Romania,Alba,667526
Satu Mare,Romania,Satu Mare,667873
Salonta,Romania,Bihor,668129
SÄƒcele,Romania,BraÅŸov,668314
RoÈ™iorii de Vede,Romania,Teleorman,668605
Roman,Romania,NeamÅ£,668732
RÃ¢ÅŸnov,Romania,BraÅŸov,668828
RÃ¢mnicu VÃ¢lcea,Romania,VÃ¢lcea,668872
RÃ¢mnicu SÄƒrat,Romania,BuzÄƒu,668873
ReÅŸiÅ£a,Romania,CaraÅŸ-Severin,668954
Reghin-Sat,Romania,MureÅŸ,668995
RÄƒdÄƒuÈ›i,Romania,Suceava,669289
PopeÅŸti-Leordeni,Romania,Ilfov,669870
PloieÅŸti,Romania,Prahova,670474
PiteÅŸti,Romania,ArgeÅŸ,670609
Piatra NeamÅ£,Romania,NeamÅ£,670889
PetroÅŸani,Romania,Hunedoara,670938
Petrila,Romania,Hunedoara,670969
Pantelimon,Romania,Ilfov,671382
OrÄƒÅŸtie,Romania,Hunedoara,671757
Oradea,Romania,Bihor,671768
OlteniÅ£a,Romania,CÄƒlÄƒraÅŸi,671832
Odorheiu Secuiesc,Romania,Harghita,671964
Ocna MureÅŸ,Romania,Alba,672024
NÄƒvodari,Romania,ConstanÈ›a,672486
Motru,Romania,Gorj,672757
Moreni,Romania,DÃ¢mboviÅ£a,672862
MoineÅŸti,Romania,BacÄƒu,672926
Mizil,Romania,Prahova,673033
Miercurea-Ciuc,Romania,Harghita,673441
MediaÅŸ,Romania,Sibiu,673634
Medgidia,Romania,ConstanÈ›a,673636
Mangalia,Romania,ConstanÈ›a,673921
Lupeni,Romania,Hunedoara,674295
Lugoj,Romania,TimiÅŸ,674531
LuduÅŸ,Romania,MureÅŸ,674541
IaÅŸi,Romania,IaÅŸi,675810
HuÅŸi,Romania,Vaslui,675892
Hunedoara,Romania,Hunedoara,675918
Gura Humorului,Romania,Suceava,676527
Giurgiu,Romania,Giurgiu,677106
Gherla,Romania,Cluj,677429
Gheorgheni,Romania,Harghita,677458
GalaÅ£i,Romania,GalaÅ£i,677697
GÄƒeÅŸti,Romania,DÃ¢mboviÅ£a,677742
FocÈ™ani,Romania,Vrancea,678015
FiliaÅŸi,Romania,Dolj,678261
FeteÈ™ti-GarÄƒ,Romania,IalomiÅ£a,678301
FeteÅŸti,Romania,IalomiÅ£a,678306
FÄƒlticeni,Romania,Suceava,678459
FÄƒgÄƒraÈ™,Romania,BraÅŸov,678499
Drobeta-Turnu Severin,Romania,MehedinÅ£i,678817
DrÄƒgÄƒÅŸani,Romania,VÃ¢lcea,678978
Dorohoi,Romania,BotoÅŸani,679065
Deva,Romania,Hunedoara,679452
Dej,Romania,Cluj,679550
Curtea de ArgeÅŸ,Romania,ArgeÅŸ,679907
Cugir,Romania,Alba,679995
Craiova,Romania,Dolj,680332
Corabia,Romania,Olt,680897
ConstanÅ£a,Romania,ConstanÈ›a,680963
ComÄƒneÅŸti,Romania,BacÄƒu,681017
Codlea,Romania,BraÅŸov,681179
Cluj-Napoca,Romania,Cluj,681290
CisnÄƒdie,Romania,Sibiu,681502
CÃ¢mpulung Moldovenesc,Romania,Suceava,681845
CÃ¢mpina,Romania,Prahova,681862
CÃ¢mpia Turzii,Romania,Cluj,681865
CernavodÄƒ,Romania,ConstanÈ›a,682321
Carei,Romania,Satu Mare,682685
CaransebeÅŸ,Romania,CaraÅŸ-Severin,682729
Caracal,Romania,Olt,682747
Calafat,Romania,Dolj,683034
BuzÄƒu,Romania,BuzÄƒu,683123
BuhuÅŸi,Romania,BacÄƒu,683365
Buftea,Romania,Ilfov,683394
Bucharest,Romania,BucureÅŸti,683506
Breaza,Romania,Prahova,683760
BraÅŸov,Romania,BraÅŸov,683844
BrÄƒila,Romania,BrÄƒila,683902
Brad,Romania,Hunedoara,683974
BotoÅŸani,Romania,BotoÅŸani,684039
BorÅŸa,Romania,MaramureÅŸ,684156
BocÅŸa,Romania,CaraÅŸ-Severin,684490
Blaj,Romania,Alba,684612
BistriÅ£a,Romania,BistriÅ£a-NÄƒsÄƒud,684657
BÃ¢rlad,Romania,Vaslui,684802
BalÅŸ,Romania,Olt,685586
BÄƒileÅŸti,Romania,Dolj,685785
BÄƒicoi,Romania,Prahova,685811
Baia Sprie,Romania,MaramureÅŸ,685823
Baia Mare,Romania,MaramureÅŸ,685826
BacÄƒu,Romania,BacÄƒu,685948
Arad,Romania,Arad,686254
Alexandria,Romania,Teleorman,686502
Alba Iulia,Romania,Alba,686578
Aiud,Romania,Alba,686590
Adjud,Romania,Vrancea,686669
Baia Mare,Romania,Satu Mare,6697993
PaÅŸcani,Romania,IaÅŸi,6945426
Mioveni,Romania,ArgeÅŸ,7733099
SighiÈ™oara,Romania,MureÅŸ,8436351
Slobozia,Romania,IalomiÅ£a,8581467
Sector 1,Romania,BucureÅŸti,11048317
Sector 2,Romania,BucureÅŸti,11048318
Sector 3,Romania,BucureÅŸti,11048319
Sector 4,Romania,BucureÅŸti,11048320
Sector 5,Romania,BucureÅŸti,11048322
Sector 6,Romania,BucureÅŸti,11048323
Zrenjanin,Serbia,Vojvodina,783814
Zemun,Serbia,Central Serbia,783920
ZajeÄar,Serbia,Central Serbia,784024
VrÅ¡ac,Serbia,Vojvodina,784136
Vranje,Serbia,Central Serbia,784227
Trstenik,Serbia,Central Serbia,784873
Stara Pazova,Serbia,Vojvodina,785559
SremÄica,Serbia,Central Serbia,785615
Smederevska Palanka,Serbia,Central Serbia,785753
Smederevo,Serbia,Central Serbia,785756
Senta,Serbia,Vojvodina,785965
Prokuplje,Serbia,Central Serbia,786690
PoÅ¾arevac,Serbia,Central Serbia,786827
Pirot,Serbia,Central Serbia,787050
PanÄevo,Serbia,Vojvodina,787237
Obrenovac,Serbia,Central Serbia,787516
Novi Pazar,Serbia,Central Serbia,787595
Nova Pazova,Serbia,Vojvodina,787615
NiÅ¡,Serbia,Central Serbia,787657
Negotin,Serbia,Central Serbia,787718
Leskovac,Serbia,Central Serbia,788709
Lazarevac,Serbia,Central Serbia,788771
KruÅ¡evac,Serbia,Central Serbia,788975
Kraljevo,Serbia,Central Serbia,789107
Kragujevac,Serbia,Central Serbia,789128
Kikinda,Serbia,Vojvodina,789518
Jagodina,Serbia,Central Serbia,789923
InÄ‘ija,Serbia,Vojvodina,790015
Gornji Milanovac,Serbia,Central Serbia,790367
Ä†uprija,Serbia,Central Serbia,791678
ÄŒaÄak,Serbia,Central Serbia,792078
Bor,Serbia,Central Serbia,792456
Belgrade,Serbia,Central Serbia,792680
BeÄej,Serbia,Vojvodina,792814
AranÄ‘elovac,Serbia,Central Serbia,793111
Vrbas,Serbia,Vojvodina,3187297
Valjevo,Serbia,Central Serbia,3188402
UÅ¾ice,Serbia,Central Serbia,3188434
Subotica,Serbia,Vojvodina,3189595
Sremska Mitrovica,Serbia,Vojvodina,3190103
Sombor,Serbia,Vojvodina,3190342
Å abac,Serbia,Central Serbia,3191376
Ruma,Serbia,Vojvodina,3191429
Novi Sad,Serbia,Vojvodina,3194360
BaÄka Topola,Serbia,Vojvodina,3204672
BaÄka Palanka,Serbia,Vojvodina,3204674
Apatin,Serbia,Vojvodina,3204793
Knjazevac,Serbia,Central Serbia,6619277
Udomlya,Russia,Tverskaya,452949
Sosnovka,Russia,St.-Petersburg,461698
Sasovo,Russia,Rjazan,461699
Zyuzino,Russia,Moscow,461740
Zyablikovo,Russia,Moscow,461835
Zverevo,Russia,Rostov,461910
Zvenigorod,Russia,MO,461920
Zlatoust,Russia,Chelyabinsk,462444
Zimovniki,Russia,Rostov,462522
Zhulebino,Russia,Moscow,462745
Zhukovskiy,Russia,MO,462755
Zhukovka,Russia,Brjansk,462822
Zhirnovsk,Russia,Volgograd,462984
Zhigulevsk,Russia,Samara,463082
Zherdevka,Russia,Tambov,463217
Zheleznovodsk,Russia,Stavropol'skiy,463340
Zheleznogorsk,Russia,Kursk,463343
Zheleznodorozhnyy,Russia,MO,463355
Zernograd,Russia,Rostov,463637
Zelenokumsk,Russia,Stavropol'skiy,463824
Zelenograd,Russia,Moscow,463829
Zelenodolsk,Russia,Tatarstan,463835
Zelenchukskaya,Russia,Karachayevo-Cherkesiya,463885
Zavolzhâ€™ye,Russia,Nizjnij Novgorod,464101
Zarechnyy,Russia,Penza,464625
Zaraysk,Russia,MO,464687
Zapolyarnyy,Russia,Murmansk,464790
Zamoskvorechâ€™ye,Russia,Moscow,465057
Zainsk,Russia,Tatarstan,465543
Yurâ€™yev-Polâ€™skiy,Russia,Vladimir,466215
Yoshkar-Ola,Russia,Mariy-El,466806
Yeysk,Russia,Krasnodarskiy,466885
Yessentukskaya,Russia,Stavropol'skiy,466989
Yessentuki,Russia,Stavropol'skiy,466990
Yershov,Russia,Saratov,467120
Yemva,Russia,Komi Republic,467525
Yelizavetinskaya,Russia,Krasnodarskiy,467854
Yelets,Russia,Lipetsk,467978
Yelanâ€™,Russia,Volgograd,468063
Yelabuga,Russia,Tatarstan,468082
Yegorâ€™yevsk,Russia,MO,468250
Yegorlykskaya,Russia,Rostov,468307
Yefremov,Russia,Tula,468390
Yasnyy,Russia,Orenburg,468657
Yasnogorsk,Russia,Tula,468671
Yasenevo,Russia,Moscow,468809
Yartsevo,Russia,Smolensk,468866
Yaroslavl,Russia,Jaroslavl,468902
Yaransk,Russia,Kirov,469005
Yanaul,Russia,Bashkortostan,469178
Yagry,Russia,Arkhangelskaya,469707
Yablonovskiy,Russia,Adygeya,469844
Vyshniy VolochÃ«k,Russia,Tverskaya,470252
Vyselki,Russia,Krasnodarskiy,470338
Vyksa,Russia,Nizjnij Novgorod,470444
Vykhino-Zhulebino,Russia,Moscow,470451
Vyborg,Russia,Leningrad,470546
Vyazniki,Russia,Vladimir,470666
Vyazâ€™ma,Russia,Smolensk,470676
Vyatskiye Polyany,Russia,Kirov,470734
Vsevolozhsk,Russia,Leningrad,471101
Votkinsk,Russia,Udmurtiya,471430
Vostryakovo,Russia,MO,471456
Vostryakovo,Russia,MO,471457
Voskresensk,Russia,MO,471656
Voronezh,Russia,Voronezj,472045
Altufâ€™yevskiy,Russia,Moscow,472072
Vorobâ€™yovo,Russia,Moscow,472079
Volzhskiy,Russia,Volgograd,472231
Volzhsk,Russia,Mariy-El,472234
Volâ€™sk,Russia,Saratov,472278
Volokolamsk,Russia,MO,472433
Vologda,Russia,Vologda,472459
Volkhov,Russia,Leningrad,472722
Nagornyy,Russia,Moscow,472732
Volgorechensk,Russia,Kostroma,472750
Volgograd,Russia,Volgograd,472757
Volgodonsk,Russia,Rostov,472761
Vnukovo,Russia,Moscow,473021
Novovladykino,Russia,Moscow,473127
Vladimir,Russia,Vladimir,473247
Vladikavkaz,Russia,North Ossetia,473249
Vidnoye,Russia,MO,473778
Vichuga,Russia,Ivanovo,473788
Veshnyaki,Russia,Moscow,473972
Vereshchagino,Russia,Perm,475777
VenÃ«v,Russia,Tula,475881
Velâ€™sk,Russia,Arkhangelskaya,475938
Velikiy Ustyug,Russia,Vologda,476062
Velikiye Luki,Russia,Pskov,476077
Vatutino,Russia,Moscow,476368
Valuyki,Russia,Belgorod,477192
Valday,Russia,Novgorod,477301
Vagonoremont,Russia,Moscow,477377
Uzlovaya,Russia,Tula,477494
Uvarovo,Russia,Tambov,477626
Uva,Russia,Udmurtiya,477656
Ustâ€™-Labinsk,Russia,Krasnodarskiy,478044
Ustâ€™-Katav,Russia,Chelyabinsk,478071
Ustâ€™-Dzheguta,Russia,Karachayevo-Cherkesiya,478130
Usmanâ€™,Russia,Lipetsk,478317
Uryupinsk,Russia,Volgograd,478544
Urus-Martan,Russia,Chechnya,478581
Uritsk,Russia,St.-Petersburg,478724
Unecha,Russia,Brjansk,479028
Ulyanovsk,Russia,Ulyanovsk,479123
Ukhta,Russia,Komi Republic,479411
Uglich,Russia,Jaroslavl,479532
Ufa,Russia,Bashkortostan,479561
Uchkeken,Russia,Karachayevo-Cherkesiya,479687
Uchaly,Russia,Bashkortostan,479703
Uchaly,Russia,Bashkortostan,479704
Tyrnyauz,Russia,Kabardino-Balkariya,479933
Tver,Russia,Tverskaya,480060
Tuymazy,Russia,Bashkortostan,480089
Tutayev,Russia,Jaroslavl,480122
Tula,Russia,Tula,480562
Tuchkovo,Russia,MO,480685
Tuapse,Russia,Krasnodarskiy,480716
Tsimlyansk,Russia,Rostov,480876
Trubchevsk,Russia,Brjansk,481350
TroparÃ«vo,Russia,Moscow,481453
Troitskaya,Russia,Ingushetiya,481605
Troitsk,Russia,Moscow,481608
Tosno,Russia,Leningrad,481964
Torzhok,Russia,Tverskaya,481985
Tomilino,Russia,MO,482260
Tolâ€™yatti,Russia,Samara,482283
TimashÃ«vsk,Russia,Krasnodarskiy,482965
Tikhvin,Russia,Leningrad,483019
Tikhoretsk,Russia,Krasnodarskiy,483029
Teykovo,Russia,Ivanovo,483137
Terek,Russia,Kabardino-Balkariya,483495
Tyoply Stan,Russia,Moscow,483551
Temryuk,Russia,Krasnodarskiy,483661
Tekstilâ€™shchiki,Russia,Moscow,483826
Tbilisskaya,Russia,Krasnodarskiy,483883
Tambov,Russia,Tambov,484646
Agidelâ€™,Russia,Bashkortostan,484856
Taganrog,Russia,Rostov,484907
Taganskiy,Russia,Moscow,484912
Syzranâ€™,Russia,Samara,484972
Syktyvkar,Russia,Komi Republic,485239
Svobody,Russia,Stavropol'skiy,485432
Sviblovo,Russia,Moscow,485630
Svetogorsk,Russia,Leningrad,485639
Svetlyy,Russia,Kaliningrad,485660
Svetlograd,Russia,Stavropol'skiy,485698
Suvorovskaya,Russia,Stavropol'skiy,485871
Suvorov,Russia,Tula,485888
Surovikino,Russia,Volgograd,486071
Surkhakhi,Russia,Ingushetiya,486110
Sukhinichi,Russia,Kaluga,486665
Stupino,Russia,MO,486968
Strunino,Russia,Vladimir,487095
Stroitelâ€™,Russia,Belgorod,487147
Strogino,Russia,Moscow,487150
Sterlitamak,Russia,Bashkortostan,487495
Stavropolâ€™,Russia,Stavropol'skiy,487846
Staryy Oskol,Russia,Belgorod,487928
Staroshcherbinovskaya,Russia,Krasnodarskiy,488635
Starominskaya,Russia,Krasnodarskiy,488742
Starodub,Russia,Brjansk,488852
Staraya Russa,Russia,Novgorod,489088
Staraya Kupavna,Russia,MO,489162
Staraya Derevnya,Russia,St.-Petersburg,489226
Sovetsk,Russia,Kirov,490067
Sovetsk,Russia,Kaliningrad,490068
Sosnovyy Bor,Russia,Leningrad,490172
Sosnovaya Polyana,Russia,St.-Petersburg,490377
Sosnogorsk,Russia,Komi Republic,490391
Sortavala,Russia,Republic of Karelia,490466
Sorochinsk,Russia,Orenburg,490554
Solntsevo,Russia,Moscow,490971
Solnechnogorsk,Russia,MO,490996
Solâ€™-Iletsk,Russia,Orenburg,491019
Solikamsk,Russia,Perm,491023
Sokolâ€™niki,Russia,Moscow,491250
Sokol,Russia,Moscow,491280
Sokol,Russia,Vologda,491281
Sofrino,Russia,MO,491352
Sochi,Russia,Krasnodarskiy,491422
Sobinka,Russia,Vladimir,491480
Smolensk,Russia,Smolensk,491687
Slobodskoy,Russia,Kirov,491882
Slobodka,Russia,Moscow,491895
Slavyansk-na-Kubani,Russia,Krasnodarskiy,492094
Slantsy,Russia,Leningrad,492162
Skopin,Russia,Rjazan,492376
Skhodnya,Russia,MO,492448
Sim,Russia,Chelyabinsk,492944
Sibay,Russia,Bashkortostan,493160
Shuya,Russia,Ivanovo,493231
Shushary,Russia,St.-Petersburg,493316
Shumerlya,Russia,Chuvashia,493463
Mikhaylovsk,Russia,Stavropol'skiy,493702
Shilovo,Russia,Rjazan,494427
Sheksna,Russia,Vologda,495062
Shebekino,Russia,Belgorod,495112
Shchukino,Russia,Moscow,495136
Shchigry,Russia,Kursk,495206
Shcherbinka,Russia,Moscow,495260
Shchelkovo,Russia,MO,495344
ShchÃ«kino,Russia,Tula,495394
Shatura,Russia,MO,495518
Sharâ€™ya,Russia,Kostroma,495619
Shali,Russia,Chechnya,495957
Shakhunâ€™ya,Russia,Nizjnij Novgorod,496012
Shakhty,Russia,Rostov,496015
Severskaya,Russia,Krasnodarskiy,496267
Severo-Zadonsk,Russia,Tula,496269
Severouralâ€™sk,Russia,Sverdlovsk,496275
Severomorsk,Russia,Murmansk,496278
Severodvinsk,Russia,Arkhangelskaya,496285
Severnyy,Russia,Moscow,496348
Setunâ€™,Russia,Moscow,496456
Sestroretsk,Russia,St.-Petersburg,496478
Sertolovo,Russia,Leningrad,496519
Serpukhov,Russia,MO,496527
Sergiyev Posad,Russia,MO,496638
Sergach,Russia,Nizjnij Novgorod,496802
Serdobsk,Russia,Penza,496934
Semiluki,Russia,Voronezj,497206
Semikarakorsk,Russia,Rostov,497218
SemÃ«novskoye,Russia,MO,497271
SemÃ«nov,Russia,Nizjnij Novgorod,497450
Selâ€™tso,Russia,Brjansk,497610
Segezha,Russia,Republic of Karelia,497927
Satka,Russia,Chelyabinsk,498418
Sarov,Russia,Nizjnij Novgorod,498525
Saratov,Russia,Saratov,498677
Sarapul,Russia,Udmurtiya,498687
Saransk,Russia,Mordoviya,498698
Saraktash,Russia,Orenburg,498708
Saint Petersburg,Russia,St.-Petersburg,498817
Samara,Russia,Samara,499099
Salâ€™sk,Russia,Rostov,499161
Salavat,Russia,Bashkortostan,499292
Safonovo,Russia,Smolensk,499452
Rzhev,Russia,Tverskaya,499717
Rybnoye,Russia,Rjazan,499975
Rybinsk,Russia,Jaroslavl,500004
Rybatskoye,Russia,Leningrad,500019
Ryazhsk,Russia,Rjazan,500047
Ryazanâ€™,Russia,Rjazan,500096
Ruzayevka,Russia,Mordoviya,500299
RublÃ«vo,Russia,Moscow,500843
Rtishchevo,Russia,Saratov,500886
Rostov-na-Donu,Russia,Rostov,501175
Rostov,Russia,Jaroslavl,501183
Rostokino,Russia,Moscow,501187
Rossoshâ€™,Russia,Voronezj,501215
Rossoshâ€™,Russia,Voronezj,501231
Roslavlâ€™,Russia,Smolensk,501283
Roshalâ€™,Russia,MO,501320
Rodniki,Russia,Ivanovo,501730
Revda,Russia,Sverdlovsk,502011
Reutov,Russia,MO,502018
Razumnoye,Russia,Belgorod,502400
Rayevskiy,Russia,Bashkortostan,502540
Rasskazovo,Russia,Tambov,502793
Ramenki,Russia,Moscow,502971
Pyatigorsk,Russia,Stavropol'skiy,503550
Pushkino,Russia,MO,503977
Pushkin,Russia,St.-Petersburg,504003
Pushchino,Russia,MO,504042
Pugachev,Russia,Saratov,504250
Pskov,Russia,Pskov,504341
Protvino,Russia,MO,504576
Proletarsk,Russia,Rostov,504831
Prokhladnyy,Russia,Kabardino-Balkariya,504935
Priyutovo,Russia,Bashkortostan,505014
Privolzhskiy,Russia,Saratov,505057
Privolzhsk,Russia,Ivanovo,505060
PriozÃ«rsk,Russia,Leningrad,505230
Primorsko-Akhtarsk,Russia,Krasnodarskiy,505259
Pridonskoy,Russia,Voronezj,505421
Povorino,Russia,Voronezj,505806
Kotlovka,Russia,Moscow,506043
Annino,Russia,Moscow,506117
Polyarnyye Zori,Russia,Murmansk,506762
Polyarnyy,Russia,Murmansk,506763
Pokrovskoye-StreshnÃ«vo,Russia,Moscow,507338
Pokrov,Russia,Vladimir,507599
Pokhvistnevo,Russia,Samara,507624
Podporozhâ€™ye,Russia,Leningrad,508034
Podolâ€™sk,Russia,MO,508101
Pochep,Russia,Brjansk,508656
Ryazanskiy,Russia,Moscow,508751
Plavsk,Russia,Tula,509052
PikalÃ«vo,Russia,Leningrad,509598
Petushki,Russia,Vladimir,509697
Petrozavodsk,Russia,Republic of Karelia,509820
Petrovskaya,Russia,MO,509981
Petrovsk,Russia,Saratov,509987
Petrodvorets,Russia,St.-Petersburg,510225
Peterhof,Russia,St.-Petersburg,510291
Pestovo,Russia,Novgorod,510364
Pervouralâ€™sk,Russia,Sverdlovsk,510808
Perovo,Russia,Moscow,511153
Perm,Russia,Perm,511196
Pereslavlâ€™-Zalesskiy,Russia,Jaroslavl,511359
Novo-Peredelkino,Russia,Moscow,511510
Penza,Russia,Penza,511565
Pechora,Russia,Komi Republic,511794
Pavlovskiy Posad,Russia,MO,512023
Pavlovskaya,Russia,Krasnodarskiy,512051
Pavlovsk,Russia,St.-Petersburg,512052
Pavlovsk,Russia,Voronezj,512053
Pashkovskiy,Russia,Krasnodarskiy,512382
Pallasovka,Russia,Volgograd,513042
OzÃ«ry,Russia,MO,513378
Ozerki,Russia,St.-Petersburg,513471
Otradnyy,Russia,Samara,513883
Otradnoye,Russia,Moscow,513896
Otradnoye,Russia,Leningrad,513898
Otradnaya,Russia,Krasnodarskiy,513911
Ostrov,Russia,Pskov,514171
Ostrogozhsk,Russia,Voronezj,514198
Ostashkov,Russia,Tverskaya,514259
Ostankinskiy,Russia,Moscow,514284
Osa,Russia,Perm,514706
Orsk,Russia,Orenburg,514734
Orlovskiy,Russia,Rostov,514796
Orenburg,Russia,Orenburg,515003
OrÃ«l,Russia,Orjol,515012
Orekhovo-Zuyevo,Russia,MO,515024
Orekhovo-Borisovo Severnoye,Russia,Moscow,515027
Ordzhonikidzevskaya,Russia,Ingushetiya,515083
Onega,Russia,Arkhangelskaya,515246
Omutninsk,Russia,Kirov,515267
Olenegorsk,Russia,Murmansk,515698
Tsotsin-Yurt,Russia,Chechnya,515804
Oktyabrâ€™skiy,Russia,Bashkortostan,515879
Odintsovo,Russia,MO,516215
OchÃ«r,Russia,Perm,516256
Ochakovo-Matveyevskoye,Russia,Moscow,516264
Obninsk,Russia,Kaluga,516436
Nytva,Russia,Perm,516576
Nyandoma,Russia,Arkhangelskaya,516647
Nurlat,Russia,Tatarstan,516716
Novyy Oskol,Russia,Belgorod,516931
Novyye Kuzâ€™minki,Russia,Moscow,517121
Novyye CherÃ«mushki,Russia,Moscow,517161
Novozybkov,Russia,Brjansk,517269
Novovoronezh,Russia,Voronezj,517716
Novouzensk,Russia,Saratov,517739
Novoulâ€™yanovsk,Russia,Ulyanovsk,517766
Novotroitsk,Russia,Orenburg,517836
Novotitarovskaya,Russia,Krasnodarskiy,517842
Novoshakhtinsk,Russia,Rostov,517963
Novorossiysk,Russia,Krasnodarskiy,518255
Novopokrovskaya,Russia,Krasnodarskiy,518325
Novopavlovsk,Russia,Stavropol'skiy,518383
Novomoskovsk,Russia,Tula,518557
Novomichurinsk,Russia,Rjazan,518602
Novokuzâ€™minki,Russia,Moscow,518657
Novokuybyshevsk,Russia,Samara,518659
Novokubansk,Russia,Krasnodarskiy,518682
Novokhovrino,Russia,Moscow,518740
Novogireyevo,Russia,MO,518879
Novodvinsk,Russia,Arkhangelskaya,518909
Novocherkassk,Russia,Rostov,518970
Novocheboksarsk,Russia,Chuvashia,518976
Novoanninskiy,Russia,Volgograd,519062
Novoaleksandrovsk,Russia,Stavropol'skiy,519106
Velikiy Novgorod,Russia,Novgorod,519336
Novaya Usmanâ€™,Russia,Voronezj,519447
Novaya Derevnya,Russia,St.-Petersburg,519711
Noginsk,Russia,MO,520068
Nizhnyaya Tura,Russia,Sverdlovsk,520204
Nizhniy Tagil,Russia,Sverdlovsk,520494
Nizhniy Novgorod,Russia,Nizjnij Novgorod,520555
Nizhniy Lomov,Russia,Penza,520574
Nizhnekamsk,Russia,Tatarstan,521118
Nikulino,Russia,Moscow,521416
Nikolâ€™skoye,Russia,Moscow,521500
Nikolâ€™skoye,Russia,Leningrad,521509
Nikolâ€™sk,Russia,Penza,521776
Nikolayevsk,Russia,Volgograd,521874
Nikelâ€™,Russia,Murmansk,522260
Nezlobnaya,Russia,Stavropol'skiy,522301
Nevinnomyssk,Russia,Stavropol'skiy,522377
Nevelâ€™,Russia,Pskov,522410
Nesterovskaya,Russia,Ingushetiya,522470
Nerekhta,Russia,Kostroma,522594
Nelidovo,Russia,Tverskaya,522775
Neftekamsk,Russia,Bashkortostan,522942
Neftegorsk,Russia,Samara,522945
Nazranâ€™,Russia,Ingushetiya,523064
Navashino,Russia,Nizjnij Novgorod,523198
Nar'yan-Mar,Russia,Nenetskiy Avtonomnyy Okrug,523392
Nartkala,Russia,Kabardino-Balkariya,523405
Naro-Fominsk,Russia,MO,523426
Nalâ€™chik,Russia,Kabardino-Balkariya,523523
Nakhabino,Russia,MO,523553
Naberezhnyye Chelny,Russia,Tatarstan,523750
Mytishchi,Russia,MO,523812
Murom,Russia,Vladimir,524294
Murmansk,Russia,Murmansk,524305
Mtsensk,Russia,Orjol,524640
Mozhga,Russia,Udmurtiya,524699
Mozhaysk,Russia,MO,524712
Mozdok,Russia,North Ossetia,524736
Mostovskoy,Russia,Krasnodarskiy,524809
Moscow,Russia,Moscow,524901
Morshansk,Russia,Tambov,525138
Morozovsk,Russia,Rostov,525162
Monino,Russia,MO,525396
Monchegorsk,Russia,Murmansk,525404
Mirnyy,Russia,Arkhangelskaya,526346
Mineralnye Vody,Russia,Stavropol'skiy,526480
Millerovo,Russia,Rostov,526558
Mikhaylovka,Russia,Volgograd,527012
Mikhalkovo,Russia,Moscow,527057
Michurinsk,Russia,Tambov,527191
Metallostroy,Russia,St.-Petersburg,527361
Menzelinsk,Russia,Tatarstan,527529
Mendeleyevsk,Russia,Tatarstan,527579
Meleuz,Russia,Bashkortostan,527717
Melenki,Russia,Vladimir,527740
Medvezhâ€™yegorsk,Russia,Republic of Karelia,527888
Medvedovskaya,Russia,Krasnodarskiy,527968
Medvedevo,Russia,Mariy-El,528056
Mednogorsk,Russia,Orenburg,528109
Maykop,Russia,Adygeya,528293
Matveyevskoye,Russia,Moscow,528454
Marks,Russia,Saratov,529073
Marâ€™ino,Russia,Moscow,529237
Marâ€™ina Roshcha,Russia,Moscow,529334
Manturovo,Russia,Kostroma,529505
Yaroslavskiy,Russia,Moscow,530088
Maloyaroslavets,Russia,Kaluga,530849
Malgobek,Russia,Ingushetiya,531129
Malakhovka,Russia,MO,531820
Makhachkala,Russia,Dagestan,532096
Magnitogorsk,Russia,Chelyabinsk,532288
Lyudinovo,Russia,Kaluga,532459
Lyublino,Russia,Moscow,532535
Lyubertsy,Russia,MO,532615
Lytkarino,Russia,MO,532657
Lysâ€™va,Russia,Perm,532675
Lyskovo,Russia,Nizjnij Novgorod,532715
Luzhniki,Russia,Moscow,533067
Lukhovitsy,Russia,MO,533543
Luga,Russia,Leningrad,533690
Losino-Petrovskiy,Russia,MO,534015
Lomonosov,Russia,St.-Petersburg,534341
Lodeynoye Pole,Russia,Leningrad,534560
Lobnya,Russia,MO,534595
Livny,Russia,Orjol,534701
Liski,Russia,Voronezj,534838
Lipetsk,Russia,Lipetsk,535121
Likino-Dulevo,Russia,MO,535243
Likhobory,Russia,Moscow,535270
Lianozovo,Russia,Moscow,535330
Lâ€™govskiy,Russia,Kursk,535334
Levoberezhnaya,Russia,MO,535451
Komendantsky aerodrom,Russia,St.-Petersburg,535729
Lermontov,Russia,Stavropol'skiy,535886
Leonovo,Russia,Moscow,535966
Leninskiye Gory,Russia,MO,536098
Leninsk,Russia,Volgograd,536156
Leninogorsk,Russia,Tatarstan,536162
Tsaritsyno,Russia,Moscow,536164
Leningradskaya,Russia,Krasnodarskiy,536200
Yubileyny,Russia,MO,536206
Lefortovo,Russia,Moscow,536398
Lebedyanâ€™,Russia,Lipetsk,536518
Lazarevskoye,Russia,Krasnodarskiy,536625
Lakinsk,Russia,Vladimir,537107
Labinsk,Russia,Krasnodarskiy,537281
Dugulubgey,Russia,Kabardino-Balkariya,537345
Kuznetsk,Russia,Penza,537737
Kuzâ€™minki,Russia,Moscow,537832
Kuvandyk,Russia,Orenburg,538138
Kuskovo,Russia,MO,538321
Kushva,Russia,Sverdlovsk,538340
KushchÃ«vskaya,Russia,Krasnodarskiy,538416
Kusa,Russia,Chelyabinsk,538442
Kurâ€™yanovo,Russia,MO,538472
Kursk,Russia,Kursk,538560
Kurovskoye,Russia,MO,538601
Kurganinsk,Russia,Krasnodarskiy,538836
Kurchatov,Russia,Kursk,538908
Kurchaloy,Russia,Chechnya,538913
Kupchino,Russia,St.-Petersburg,539061
Kungur,Russia,Perm,539147
Kumertau,Russia,Bashkortostan,539283
Kulebaki,Russia,Nizjnij Novgorod,539555
Kukmor,Russia,Tatarstan,539689
Kudymkar,Russia,Perm,539817
Kudepsta,Russia,Krasnodarskiy,539907
Kubinka,Russia,MO,540030
Kstovo,Russia,Nizjnij Novgorod,540103
Krymsk,Russia,Krasnodarskiy,540251
Kropotkin,Russia,Krasnodarskiy,540761
Kronshtadt,Russia,St.-Petersburg,540771
Krasnyy Sulin,Russia,Rostov,541404
BiryulÃ«vo Zapadnoye,Russia,MO,541406
Krasnoye Selo,Russia,St.-Petersburg,542000
Krasnovishersk,Russia,Perm,542184
Krasnoufimsk,Russia,Sverdlovsk,542199
Krasnokamsk,Russia,Perm,542327
Krasnogvardeyskoye,Russia,Stavropol'skiy,542334
Krasnogorsk,Russia,MO,542374
Krasnodar,Russia,Krasnodarskiy,542420
Krasnoarmeyskaya,Russia,Krasnodarskiy,542461
Krasnoarmeysk,Russia,MO,542463
Krasnoarmeysk,Russia,Saratov,542464
Presnenskiy,Russia,MO,542634
Kozâ€™modemâ€™yansk,Russia,Mariy-El,543018
Kozhukhovo,Russia,MO,543254
Kozeyevo,Russia,Moscow,543344
Kozelâ€™sk,Russia,Kaluga,543348
Kovylkino,Russia,Mordoviya,543436
Kovrov,Russia,Vladimir,543460
Kovdor,Russia,Murmansk,543508
Kotovsk,Russia,Tambov,543605
Kotovo,Russia,Volgograd,543633
Kotlas,Russia,Arkhangelskaya,543704
Kotelâ€™nikovo,Russia,Volgograd,543728
Kotelâ€™niki,Russia,MO,543731
Kotelâ€™nich,Russia,Kirov,543737
Kostroma,Russia,Kostroma,543878
Kostomuksha,Russia,Republic of Karelia,543899
Kosaya Gora,Russia,Tula,544293
Koryazhma,Russia,Arkhangelskaya,544370
Korenovsk,Russia,Krasnodarskiy,544896
Konstantinovsk,Russia,Rostov,545277
Kondrovo,Russia,Kaluga,545575
Kondopoga,Russia,Republic of Karelia,545626
Konakovo,Russia,Tverskaya,545673
Kommunar,Russia,Leningrad,545788
Kolpino,Russia,St.-Petersburg,546105
Kolomyagi,Russia,St.-Petersburg,546225
Kolomna,Russia,MO,546230
Kolomenskoye,Russia,Moscow,546244
Kolâ€™chugino,Russia,Vladimir,546521
Kokhma,Russia,Ivanovo,546672
Klintsy,Russia,Brjansk,547475
Klin,Russia,MO,547523
Klimovsk,Russia,MO,547560
Kizlyar,Russia,Dagestan,547840
Kizilyurt,Russia,Dagestan,547849
Kizel,Russia,Perm,547875
Kislovodsk,Russia,Stavropol'skiy,548114
Kirzhach,Russia,Vladimir,548278
Kirsanov,Russia,Tambov,548330
Kirovsk,Russia,Murmansk,548391
Kirovsk,Russia,Leningrad,548392
Kirovo-Chepetsk,Russia,Kirov,548395
Kirov,Russia,Kirov,548408
Kirov,Russia,Kaluga,548410
Kirishi,Russia,Leningrad,548442
Kireyevsk,Russia,Tula,548506
Kingisepp,Russia,Leningrad,548602
Kineshma,Russia,Ivanovo,548605
Kinelâ€™-Cherkassy,Russia,Samara,548622
Kinelâ€™,Russia,Samara,548625
Kimry,Russia,Tverskaya,548652
Kimovsk,Russia,Tula,548658
Khot'kovo,Russia,MO,549373
Khosta,Russia,Krasnodarskiy,549424
KhoroshÃ«vo-Mnevniki,Russia,MO,549479
Kholmskiy,Russia,Krasnodarskiy,549741
Khimki,Russia,Moscow,550280
Khasavyurt,Russia,Dagestan,550478
Kharabali,Russia,Astrakhan,550671
Khadyzhensk,Russia,Krasnodarskiy,550846
Kazan,Russia,Tatarstan,551487
Katav-Ivanovsk,Russia,Chelyabinsk,551794
Kastanayevo,Russia,MO,551835
Kaspiysk,Russia,Dagestan,551847
Kasimov,Russia,Rjazan,551891
Kashira,Russia,MO,551964
Kashin,Russia,Tverskaya,551986
Karachev,Russia,Brjansk,552920
Karachayevsk,Russia,Karachayevo-Cherkesiya,552924
Karabulak,Russia,Ingushetiya,552951
Karabanovo,Russia,Vladimir,552977
Kapotnya,Russia,Moscow,553034
Kantyshevo,Russia,Ingushetiya,553092
Kanevskaya,Russia,Krasnodarskiy,553152
Kandalaksha,Russia,Murmansk,553190
Kanash,Russia,Chuvashia,553216
Kamyzyak,Russia,Astrakhan,553248
Kamyshin,Russia,Volgograd,553287
Kamensk-Shakhtinskiy,Russia,Rostov,553399
Kaluga,Russia,Kaluga,553915
Kalininsk,Russia,Saratov,554199
Korolev,Russia,MO,554233
Kaliningrad,Russia,Kaliningrad,554234
Kalach-na-Donu,Russia,Volgograd,554397
Kalach,Russia,Voronezj,554410
Kachkanar,Russia,Sverdlovsk,554599
Kabanovo,Russia,MO,554679
Izobilâ€™nyy,Russia,Stavropol'skiy,554770
Izmaylovo,Russia,MO,554787
Izhevsk,Russia,Udmurtiya,554840
Izberbash,Russia,Dagestan,554894
Ivanteyevka,Russia,MO,555111
Ivanovskoye,Russia,Moscow,555129
Ivanovo,Russia,Ivanovo,555312
Istra,Russia,MO,555746
Ishimbay,Russia,Bashkortostan,555980
Ipatovo,Russia,Stavropol'skiy,556230
Inza,Russia,Ulyanovsk,556283
Inozemtsevo,Russia,Stavropol'skiy,556320
Ilâ€™skiy,Russia,Krasnodarskiy,556951
Igra,Russia,Udmurtiya,557469
Gusâ€™-Khrustalâ€™nyy,Russia,Vladimir,557775
Gusev,Russia,Kaliningrad,557882
Gulâ€™kevichi,Russia,Krasnodarskiy,558066
Gukovo,Russia,Rostov,558082
Gudermes,Russia,Chechnya,558118
Gubkin,Russia,Belgorod,558146
Gubakha,Russia,Perm,558209
Gryazovets,Russia,Vologda,558236
Gryazi,Russia,Lipetsk,558312
Groznyy,Russia,Chechnya,558418
Gribanovskiy,Russia,Voronezj,558799
Grazhdanka,Russia,St.-Petersburg,559029
Goryachiy Klyuch,Russia,Krasnodarskiy,559317
Goryachevodskiy,Russia,Stavropol'skiy,559320
Gorodishche,Russia,Volgograd,559654
Gorodets,Russia,Nizjnij Novgorod,559678
Gorelovo,Russia,St.-Petersburg,560142
Golâ€™yanovo,Russia,Moscow,560465
Golitsyno,Russia,MO,560756
Glazov,Russia,Udmurtiya,561347
Giaginskaya,Russia,Adygeya,561515
Georgiyevsk,Russia,Stavropol'skiy,561627
Gelendzhik,Russia,Krasnodarskiy,561667
Gay,Russia,Orenburg,561731
Gavrilov-Yam,Russia,Jaroslavl,561762
Gatchina,Russia,Leningrad,561887
Galich,Russia,Kostroma,562161
Gagarin,Russia,Smolensk,562237
Furmanov,Russia,Ivanovo,562309
Fryazino,Russia,MO,562319
Fryazevo,Russia,MO,562321
Frolovo,Russia,Volgograd,562389
Fili,Russia,MO,562820
Ezhva,Russia,Komi Republic,563379
Engelâ€™s,Russia,Saratov,563464
Enem,Russia,Adygeya,563472
Elista,Russia,Kalmykiya,563514
Elektrougli,Russia,MO,563522
Elektrostalâ€™,Russia,MO,563523
Elektrogorsk,Russia,MO,563524
Ekazhevo,Russia,Ingushetiya,563551
Dzerzhinskiy,Russia,MO,563705
Dzerzhinsk,Russia,Nizjnij Novgorod,563708
Dyurtyuli,Russia,Bashkortostan,563719
Dyatâ€™kovo,Russia,Brjansk,563822
Dubovka,Russia,Volgograd,564654
Dubna,Russia,MO,564719
Dorogomilovo,Russia,MO,565197
Donskoye,Russia,Stavropol'skiy,565289
Donskoy,Russia,Tula,565290
Donetsk,Russia,Rostov,565348
Domodedovo,Russia,MO,565381
Dolgoprudnyy,Russia,MO,565614
Dobryanka,Russia,Perm,565778
Dmitrov,Russia,MO,565955
Divnoye,Russia,Stavropol'skiy,566155
Dinskaya,Russia,Krasnodarskiy,566181
Dimitrovgrad,Russia,Ulyanovsk,566199
Desnogorsk,Russia,Smolensk,566384
Derbent,Russia,Dagestan,566532
Zapadnoye Degunino,Russia,Moscow,566809
Dedovsk,Russia,MO,566854
Davydkovo,Russia,Moscow,566976
Davlekanovo,Russia,Bashkortostan,567006
Dankov,Russia,Lipetsk,567109
Danilov,Russia,Jaroslavl,567183
Dagestanskiye Ogni,Russia,Dagestan,567290
Dachnoye,Russia,St.-Petersburg,567311
Chusovoy,Russia,Perm,567434
Chudovo,Russia,Novgorod,567774
Chistopolâ€™,Russia,Tatarstan,567990
Chishmy,Russia,Bashkortostan,568012
Chernyanka,Russia,Belgorod,568587
Chernyakhovsk,Russia,Kaliningrad,568595
Chernushka,Russia,Perm,568608
Chernogolovka,Russia,MO,568808
Cherkessk,Russia,Karachayevo-Cherkesiya,569154
Cherepovets,Russia,Vologda,569223
CherÃ«mushki,Russia,MO,569273
Chekhov,Russia,MO,569591
Chegem,Russia,Kabardino-Balkariya,569639
Cheboksary,Russia,Chuvashia,569696
Chaykovskiy,Russia,Perm,569742
Chapayevsk,Russia,Samara,569955
Buzuluk,Russia,Orenburg,570427
Buynaksk,Russia,Dagestan,570479
Buy,Russia,Kostroma,570508
Buturlinovka,Russia,Voronezj,570563
Businovo,Russia,Moscow,570636
Buinsk,Russia,Tatarstan,571155
Buguruslan,Russia,Orenburg,571159
Bugulâ€™ma,Russia,Tatarstan,571170
BudÃ«nnovsk,Russia,Stavropol'skiy,571306
Bryukhovetskaya,Russia,Krasnodarskiy,571420
Bryansk,Russia,Brjansk,571476
Bronnitsy,Russia,MO,571557
Brateyevo,Russia,Moscow,571741
Borovichi,Russia,Novgorod,572154
Borisoglebsk,Russia,Voronezj,572525
Bor,Russia,Nizjnij Novgorod,572665
Bolâ€™shaya Setunâ€™,Russia,MO,574675
Bologoye,Russia,Tverskaya,575349
Boksitogorsk,Russia,Leningrad,575410
Boguchar,Russia,Voronezj,575457
Bogorodskoye,Russia,MO,575505
Bogorodsk,Russia,Nizjnij Novgorod,575560
Bogoroditsk,Russia,Tula,575591
Bobrov,Russia,Voronezj,575948
Blagoveshchensk,Russia,Bashkortostan,576116
Blagodarnyy,Russia,Stavropol'skiy,576172
BiryulÃ«vo,Russia,Moscow,576279
Birsk,Russia,Bashkortostan,576317
Bibirevo,Russia,Moscow,576432
Bezhetsk,Russia,Tverskaya,576566
Bezenchuk,Russia,Samara,576590
Beslan,Russia,North Ossetia,576697
Berezniki,Russia,Perm,577206
Beloretsk,Russia,Bashkortostan,577881
Belorechensk,Russia,Krasnodarskiy,577893
BeloozÃ«rskiy,Russia,MO,577901
Belgorod,Russia,Belgorod,578072
BelÃ«v,Russia,Tula,578091
Belebey,Russia,Bashkortostan,578120
Belaya Kalitva,Russia,Rostov,578155
Belaya Glina,Russia,Krasnodarskiy,578169
Baymak,Russia,Bashkortostan,578534
Bavly,Russia,Tatarstan,578638
Bataysk,Russia,Rostov,578740
Barysh,Russia,Ulyanovsk,578931
Balezino,Russia,Udmurtiya,579432
Balashov,Russia,Saratov,579460
Balashikha,Russia,MO,579464
Balakovo,Russia,Saratov,579492
Novaya Balakhna,Russia,Nizjnij Novgorod,579514
Balabanovo,Russia,Kaluga,579529
Baksan,Russia,Kabardino-Balkariya,579574
Bakal,Russia,Chelyabinsk,579738
Bagayevskaya,Russia,Rostov,579771
Babushkin,Russia,Moscow,579870
Azov,Russia,Rostov,580054
Avtury,Russia,Chechnya,580218
Avtovo,Russia,St.-Petersburg,580222
Atkarsk,Russia,Saratov,580420
Astrakhan,Russia,Astrakhan,580497
Asha,Russia,Chelyabinsk,580660
Arzgir,Russia,Stavropol'skiy,580716
Arzamas,Russia,Nizjnij Novgorod,580724
Arsk,Russia,Tatarstan,580850
Armavir,Russia,Krasnodarskiy,580922
Arkhangelâ€™sk,Russia,Arkhangelskaya,581049
Argun,Russia,Chechnya,581126
Ardon,Russia,North Ossetia,581179
Apsheronsk,Russia,Krasnodarskiy,581313
Aprelevka,Russia,MO,581321
Apatity,Russia,Murmansk,581357
Anna,Russia,Voronezj,581671
Andreyevskoye,Russia,MO,581928
Anapa,Russia,Krasnodarskiy,582182
Aminâ€™yevo,Russia,Moscow,582266
Alâ€™metâ€™yevsk,Russia,Tatarstan,582432
Aleksin,Russia,Tula,582750
Alekseyevka,Russia,MO,582846
Alekseyevka,Russia,Belgorod,582956
Aleksandrovskoye,Russia,Stavropol'skiy,582993
Aleksandrovsk,Russia,Perm,583041
Aleksandrov,Russia,Vladimir,583350
Alatyrâ€™,Russia,Chuvashia,583437
Levoberezhnyy,Russia,MO,583589
Aksay,Russia,Rostov,583673
Akhtyrskiy,Russia,Krasnodarskiy,583785
Akhtubinsk,Russia,Astrakhan,583798
Agryz,Russia,Tatarstan,583983
Afipskiy,Russia,Krasnodarskiy,584126
Adler,Russia,Krasnodarskiy,584243
Achkhoy-Martan,Russia,Chechnya,584298
Abinsk,Russia,Krasnodarskiy,584441
Abdulino,Russia,Orenburg,584471
Vasilâ€™yevo,Russia,Tatarstan,611182
Rylâ€™sk,Russia,Kursk,695019
Neftekumsk,Russia,Stavropol'skiy,797781
Alagir,Russia,North Ossetia,802078
Persianovka,Russia,Rostov,802714
Annino,Russia,MO,819552
Dagomys,Russia,Krasnodarskiy,823674
Pavlovo,Russia,Nizjnij Novgorod,827329
Belidzhi,Russia,Dagestan,828055
Lesnoy,Russia,Sverdlovsk,829005
TrÃ«khgornyy,Russia,Chelyabinsk,830844
Mirnyy,Russia,Arkhangelskaya,831129
Znamensk,Russia,Astrakhan,831130
Zarechnyy,Russia,Penza,831165
Kochubeyevskoye,Russia,Stavropol'skiy,841006
Vnukovo,Russia,MO,857689
Moskovskiy,Russia,Moscow,857690
Usinsk,Russia,Komi Republic,863061
Obukhovo,Russia,St.-Petersburg,873901
Staryy Malgobek,Russia,Ingushetiya,874045
Zavodoukovsk,Russia,Tjumen,1485357
Zarinsk,Russia,Altai Krai,1485439
Zarechnyy,Russia,Sverdlovsk,1485445
Yuzhnyy,Russia,Altai Krai,1485627
Yuzhnouralâ€™sk,Russia,Chelyabinsk,1485634
Yurga,Russia,Kemerovo,1485724
Yeniseysk,Russia,Krasnoyarskiy,1485997
Yemanzhelinsk,Russia,Chelyabinsk,1486039
Yekaterinburg,Russia,Sverdlovsk,1486209
Yashkino,Russia,Kemerovo,1486298
Yarovoye,Russia,Altai Krai,1486340
Yalutorovsk,Russia,Tjumen,1486468
Vorkuta,Russia,Komi Republic,1486910
Vorgashor,Russia,Komi Republic,1486913
Verkhnyaya Salda,Russia,Sverdlovsk,1487277
Verkhnyaya Pyshma,Russia,Sverdlovsk,1487281
Verkhniy Ufaley,Russia,Chelyabinsk,1487394
Uzhur,Russia,Krasnoyarskiy,1487882
Zelenogorsk,Russia,Krasnoyarskiy,1488253
Uray,Russia,Khanty-Mansiyskiy Avtonomnyy Okrug,1488429
Tyumen,Russia,Tjumen,1488754
Turinsk,Russia,Sverdlovsk,1488933
Troitsk,Russia,Chelyabinsk,1489246
Topki,Russia,Kemerovo,1489394
Tomsk,Russia,Tomsk,1489425
Toguchin,Russia,Novosibirsk,1489508
Tobolâ€™sk,Russia,Tjumen,1489530
Tayshet,Russia,Irkutsk,1489870
Tayga,Russia,Kemerovo,1489907
Tavda,Russia,Sverdlovsk,1489962
Tatarsk,Russia,Novosibirsk,1490003
Tashtagol,Russia,Kemerovo,1490042
Tarko-Sale,Russia,Yamalo-Nenetskiy Avtonomnyy Okrug,1490085
Tara,Russia,Omsk,1490140
Talnakh,Russia,Krasnoyarskiy,1490256
Talâ€™menka,Russia,Altai Krai,1490266
Talitsa,Russia,Sverdlovsk,1490277
Talitsa,Russia,Sverdlovsk,1490281
Sysertâ€™,Russia,Sverdlovsk,1490402
Suzun,Russia,Novosibirsk,1490551
Surgut,Russia,Khanty-Mansiyskiy Avtonomnyy Okrug,1490624
Sukhoy Log,Russia,Sverdlovsk,1490686
Strezhevoy,Russia,Tomsk,1490796
Sredneuralsk,Russia,Sverdlovsk,1491159
Sovetskiy,Russia,Khanty-Mansiyskiy Avtonomnyy Okrug,1491230
Sosnovoborsk,Russia,Krasnoyarskiy,1491291
Slavgorod,Russia,Altai Krai,1491706
Shushenskoye,Russia,Krasnoyarskiy,1491953
Shumikha,Russia,Kurgan,1491999
Sharypovo,Russia,Krasnoyarskiy,1492401
Shadrinsk,Russia,Kurgan,1492517
Serov,Russia,Sverdlovsk,1492663
Sayanogorsk,Russia,Khakasiya,1492893
Salekhard,Russia,Yamalo-Nenetskiy Avtonomnyy Okrug,1493197
Rubtsovsk,Russia,Altai Krai,1493467
Rezh,Russia,Sverdlovsk,1493648
Reftinskiy,Russia,Sverdlovsk,1493687
Promyshlennaya,Russia,Kemerovo,1494091
Prokopâ€™yevsk,Russia,Kemerovo,1494114
Poykovskiy,Russia,Khanty-Mansiyskiy Avtonomnyy Okrug,1494276
Polysayevo,Russia,Kemerovo,1494456
Polevskoy,Russia,Sverdlovsk,1494573
Plast,Russia,Chelyabinsk,1494907
Osinniki,Russia,Kemerovo,1495974
Omsk,Russia,Omsk,1496153
Obâ€™,Russia,Novosibirsk,1496421
Nyagan,Russia,Khanty-Mansiyskiy Avtonomnyy Okrug,1496476
Noyabrsk,Russia,Yamalo-Nenetskiy Avtonomnyy Okrug,1496503
Novyy Urengoy,Russia,Yamalo-Nenetskiy Avtonomnyy Okrug,1496511
Novosilikatnyy,Russia,Altai Krai,1496739
Novosibirsk,Russia,Novosibirsk,1496747
Novokuznetsk,Russia,Kemerovo,1496990
Novoaltaysk,Russia,Altai Krai,1497173
Norilsk,Russia,Krasnoyarskiy,1497337
Nizhnyaya Salda,Russia,Sverdlovsk,1497393
Nizhnevartovsk,Russia,Khanty-Mansiyskiy Avtonomnyy Okrug,1497543
Nizhneudinsk,Russia,Irkutsk,1497549
Nevâ€™yansk,Russia,Sverdlovsk,1497795
Nefteyugansk,Russia,Khanty-Mansiyskiy Avtonomnyy Okrug,1497917
Nazarovo,Russia,Krasnoyarskiy,1497951
Nadym,Russia,Yamalo-Nenetskiy Avtonomnyy Okrug,1498087
Myski,Russia,Kemerovo,1498129
Minusinsk,Russia,Krasnoyarskiy,1498693
Miass,Russia,Chelyabinsk,1498894
Mezhdurechensk,Russia,Kemerovo,1498920
Megion,Russia,Khanty-Mansiyskiy Avtonomnyy Okrug,1499053
Mayma,Russia,Altai Republic,1499163
Mariinsk,Russia,Kemerovo,1499350
LinÃ«vo,Russia,Novosibirsk,1500532
Lesosibirsk,Russia,Krasnoyarskiy,1500607
Leninsk-Kuznetsky,Russia,Kemerovo,1500665
Labytnangi,Russia,Yamalo-Nenetskiy Avtonomnyy Okrug,1500933
Kyzyl,Russia,Tyva,1500973
Kyshtym,Russia,Chelyabinsk,1500997
Kuybyshev,Russia,Novosibirsk,1501141
Kurtamysh,Russia,Kurgan,1501255
Kurgan,Russia,Kurgan,1501321
Kupino,Russia,Novosibirsk,1501365
Kulunda,Russia,Altai Krai,1501460
Krasnoyarsk,Russia,Krasnoyarskiy,1502026
Krasnouralâ€™sk,Russia,Sverdlovsk,1502060
Krasnoturâ€™insk,Russia,Sverdlovsk,1502061
Krasnoobsk,Russia,Novosibirsk,1502091
Korkino,Russia,Chelyabinsk,1502536
Kopeysk,Russia,Chelyabinsk,1502603
Yugorsk,Russia,Khanty-Mansiyskiy Avtonomnyy Okrug,1502725
Kolpashevo,Russia,Tomsk,1502862
Kodinsk,Russia,Krasnoyarskiy,1503037
KochenÃ«vo,Russia,Novosibirsk,1503082
KiselÃ«vsk,Russia,Kemerovo,1503277
Kirovgrad,Russia,Sverdlovsk,1503335
Khanty-Mansiysk,Russia,Khanty-Mansiyskiy Avtonomnyy Okrug,1503772
Kemerovo,Russia,Kemerovo,1503901
Kedrovka,Russia,Kemerovo,1503940
Kayyerkan,Russia,Krasnoyarskiy,1504139
Kataysk,Russia,Kurgan,1504212
Kasli,Russia,Chelyabinsk,1504251
Kartaly,Russia,Chelyabinsk,1504317
Karpinsk,Russia,Sverdlovsk,1504343
Karasuk,Russia,Novosibirsk,1504489
Karabash,Russia,Chelyabinsk,1504636
Kansk,Russia,Krasnoyarskiy,1504682
Kamyshlov,Russia,Sverdlovsk,1504769
Kamensk-Uralâ€™skiy,Russia,Sverdlovsk,1504826
Kamenâ€™-na-Obi,Russia,Altai Krai,1504871
Kaltan,Russia,Kemerovo,1504972
Kalachinsk,Russia,Omsk,1505074
Ivdelâ€™,Russia,Sverdlovsk,1505260
Iskitim,Russia,Novosibirsk,1505429
Ishim,Russia,Tjumen,1505453
Irbit,Russia,Sverdlovsk,1505526
Ilanskiy,Russia,Krasnoyarskiy,1505933
Gurâ€™yevsk,Russia,Kemerovo,1506073
Gornyak,Russia,Altai Krai,1506260
Gorno-Altaysk,Russia,Altai Republic,1506271
Dudinka,Russia,Krasnoyarskiy,1507116
Divnogorsk,Russia,Krasnoyarskiy,1507379
Degtyarsk,Russia,Sverdlovsk,1507488
Chunskiy,Russia,Irkutsk,1507636
Chernogorsk,Russia,Khakasiya,1508054
Cherepanovo,Russia,Novosibirsk,1508161
Chelyabinsk,Russia,Chelyabinsk,1508291
Chebarkulâ€™,Russia,Chelyabinsk,1508350
Borovskiy,Russia,Tjumen,1508879
Borodino,Russia,Krasnoyarskiy,1508943
Bolotnoye,Russia,Novosibirsk,1509819
Bogotol,Russia,Krasnoyarskiy,1509852
Bogdanovich,Russia,Sverdlovsk,1509888
Biysk,Russia,Altai Krai,1510018
Beryozovsky,Russia,Sverdlovsk,1510203
BerÃ«zovskiy,Russia,Kemerovo,1510205
BerÃ«zovka,Russia,Krasnoyarskiy,1510255
Berdsk,Russia,Novosibirsk,1510350
Beloyarskiy,Russia,Khanty-Mansiyskiy Avtonomnyy Okrug,1510450
Belovo,Russia,Kemerovo,1510469
Barnaul,Russia,Altai Krai,1510853
Barabinsk,Russia,Novosibirsk,1510916
Asino,Russia,Tomsk,1511309
Asbest,Russia,Sverdlovsk,1511330
ArtÃ«movskiy,Russia,Sverdlovsk,1511368
Aramil,Russia,Sverdlovsk,1511466
Anzhero-Sudzhensk,Russia,Kemerovo,1511494
Aleysk,Russia,Altai Krai,1511783
Alapayevsk,Russia,Sverdlovsk,1511954
Akademgorodok,Russia,Novosibirsk,1512086
Achinsk,Russia,Krasnoyarskiy,1512165
Abaza,Russia,Khakasiya,1512205
Abakan,Russia,Khakasiya,1512236
Snezhinsk,Russia,Chelyabinsk,1536289
Ozersk,Russia,Chelyabinsk,1538634
Zheleznogorsk,Russia,Krasnoyarskiy,1538635
Novouralâ€™sk,Russia,Sverdlovsk,1538636
Seversk,Russia,Tomsk,1538637
Gubkinskiy,Russia,Yamalo-Nenetskiy Avtonomnyy Okrug,1539209
Raduzhny,Russia,Khanty-Mansiyskiy Avtonomnyy Okrug,1540356
Muravlenko,Russia,Yamalo-Nenetskiy Avtonomnyy Okrug,1540711
Lyantor,Russia,Khanty-Mansiyskiy Avtonomnyy Okrug,1541359
Zima,Russia,Irkutsk,2012484
Zheleznogorsk-Ilimskiy,Russia,Irkutsk,2012557
Zeya,Russia,Amur,2012593
Yakutsk,Russia,Sakha,2013159
Vyazemskiy,Russia,Khabarovsk Krai,2013229
Vrangelâ€™,Russia,Primorskiy,2013258
Vladivostok,Russia,Primorskiy,2013348
Vikhorevka,Russia,Irkutsk,2013399
Ustâ€™-Kut,Russia,Irkutsk,2013923
Ustâ€™-Ilimsk,Russia,Irkutsk,2013952
Ussuriysk,Russia,Primorskiy,2014006
Usolâ€™ye-Sibirskoye,Russia,Irkutsk,2014022
Ulan-Ude,Russia,Respublika Buryatiya,2014407
Udachny,Russia,Sakha,2014624
Tynda,Russia,Amur,2014718
Tulun,Russia,Irkutsk,2014927
Trudovoye,Russia,Primorskiy,2015051
Fokino,Russia,Primorskiy,2015310
Svobodnyy,Russia,Amur,2015833
Spassk-Dalâ€™niy,Russia,Primorskiy,2016187
Slyudyanka,Russia,Irkutsk,2016422
Shimanovsk,Russia,Amur,2016701
Shelekhov,Russia,Irkutsk,2016764
Severobaykalâ€™sk,Russia,Respublika Buryatiya,2016910
Raychikhinsk,Russia,Amur,2017487
Petrovsk-Zabaykalâ€™skiy,Russia,Transbaikal Territory,2017945
Partizansk,Russia,Primorskiy,2018116
Neryungri,Russia,Sakha,2019309
Nerchinsk,Russia,Transbaikal Territory,2019326
Nakhodka,Russia,Primorskiy,2019528
Mirny,Russia,Sakha,2019951
Luchegorsk,Russia,Primorskiy,2020689
Lesozavodsk,Russia,Primorskiy,2020812
Lensk,Russia,Sakha,2020838
Kyakhta,Russia,Respublika Buryatiya,2021066
Krasnokamensk,Russia,Transbaikal Territory,2021618
Komsomolsk-on-Amur,Russia,Khabarovsk Krai,2021851
Khabarovsk,Russia,Khabarovsk Krai,2022890
Kavalerovo,Russia,Primorskiy,2023058
Irkutsk,Russia,Irkutsk,2023469
Gusinoozyorsk,Russia,Respublika Buryatiya,2023782
Dalâ€™nerechensk,Russia,Primorskiy,2025159
Chita,Russia,Transbaikal Territory,2025339
Cheremkhovo,Russia,Irkutsk,2025527
Borzya,Russia,Transbaikal Territory,2026126
Bolâ€™shoy Kamenâ€™,Russia,Primorskiy,2026303
Bodaybo,Russia,Irkutsk,2026583
Blagoveshchensk,Russia,Amur,2026609
Birobidzhan,Russia,Jewish Autonomous Oblast,2026643
Bikin,Russia,Khabarovsk Krai,2026696
Belogorsk,Russia,Amur,2026895
Baykalâ€™sk,Russia,Irkutsk,2026979
Aykhal,Russia,Sakha,2027296
ArtÃ«m,Russia,Primorskiy,2027456
Arsenâ€™yev,Russia,Primorskiy,2027468
Angarsk,Russia,Irkutsk,2027667
Amursk,Russia,Khabarovsk Krai,2027749
Aldan,Russia,Sakha,2027968
Dal'negorsk,Russia,Primorskiy,2051471
Bratsk,Russia,Irkutsk,2051523
Sayansk,Russia,Irkutsk,2055166
Khabarovsk Vtoroy,Russia,Khabarovsk Krai,2056752
Markova,Russia,Irkutsk,2056881
Vilyuchinsk,Russia,Kamtsjatka,2118647
Yuzhno-Sakhalinsk,Russia,Sakhalin,2119441
Yelizovo,Russia,Kamtsjatka,2119538
Vanino,Russia,Khabarovsk Krai,2119932
Sovetskaya Gavanâ€™,Russia,Khabarovsk Krai,2121052
Poronaysk,Russia,Sakhalin,2121909
Petropavlovsk-Kamchatsky,Russia,Kamtsjatka,2122104
Okha,Russia,Sakhalin,2122614
Nikolayevsk-on-Amure,Russia,Khabarovsk Krai,2122850
Nevelâ€™sk,Russia,Sakhalin,2122894
Magadan,Russia,Magadan,2123628
Korsakov,Russia,Sakhalin,2124286
Kholmsk,Russia,Sakhalin,2124615
Baltiysk,Russia,Kaliningrad,2609906
Isakogorka,Russia,Arkhangelskaya,6315399
Krasnoznamensk,Russia,MO,6417459
Chertanovo Yuzhnoye,Russia,Moscow,6418146
Zagorâ€™ye,Russia,Moscow,6418201
Orekhovo-Borisovo,Russia,Moscow,6418220
Metrogorodok,Russia,Moscow,6418787
Kogalym,Russia,Khanty-Mansiyskiy Avtonomnyy Okrug,6695754
Pyt-Yakh,Russia,Khanty-Mansiyskiy Avtonomnyy Okrug,6696686
Langepas,Russia,Khanty-Mansiyskiy Avtonomnyy Okrug,6696767
Lesnoy,Russia,Sverdlovsk,6853140
Zarya,Russia,MO,7117880
Raduzhnyy,Russia,Vladimir,7117885
Nizhnesortymskiy,Russia,Khanty-Mansiyskiy Avtonomnyy Okrug,7287775
Pokachi,Russia,Khanty-Mansiyskiy Avtonomnyy Okrug,7289676
Izluchinsk,Russia,Khanty-Mansiyskiy Avtonomnyy Okrug,7290697
Kurortnyy,Russia,Leningrad,8436165
Chernaya Rechka,Russia,Leningrad,8504946
Untolovo,Russia,Leningrad,8504947
Petrogradka,Russia,St.-Petersburg,8504948
Vasyl'evsky Ostrov,Russia,St.-Petersburg,8504949
Parnas,Russia,Leningrad,8504950
Kalininskiy,Russia,Leningrad,8504951
Krasnogvargeisky,Russia,St.-Petersburg,8504952
Admiralteisky,Russia,St.-Petersburg,8504953
Krestovskiy ostrov,Russia,Leningrad,8504955
Akademicheskoe,Russia,Leningrad,8504958
Finlyandskiy,Russia,Leningrad,8504959
Centralniy,Russia,St.-Petersburg,8504960
Svetlanovskiy,Russia,Leningrad,8504964
Sampsonievskiy,Russia,Leningrad,8504965
Vostochnoe Degunino,Russia,MO,8505053
Rwamagana,Rwanda,Eastern Province,201463
Musanze,Rwanda,Northern Province,201521
Nzega,Rwanda,Southern Province,201865
Kigali,Rwanda,Kigali,202061
Kibuye,Rwanda,Western Province,202065
Kibungo,Rwanda,Eastern Province,202068
Gitarama,Rwanda,Southern Province,202217
Cyangugu,Rwanda,Western Province,202326
Gisenyi,Rwanda,Western Province,202905
Byumba,Rwanda,Northern Province,203104
Butare,Rwanda,Southern Province,203112
Yanbu,Saudi Arabia,Al MadÄ«nah al Munawwarah,100425
Umm Lajj,Saudi Arabia,MinÅ£aqat TabÅ«k,100926
Å¢urayf,Saudi Arabia,Northern Borders,101312
Turabah,Saudi Arabia,Makkah,101322
TÄrÅ«t,Saudi Arabia,Eastern Province,101554
Tabuk,Saudi Arabia,MinÅ£aqat TabÅ«k,101628
Å¢ubarjal,Saudi Arabia,Al Jawf,101631
SulÅ£Änah,Saudi Arabia,Al MadÄ«nah al Munawwarah,101760
SayhÄt,Saudi Arabia,Eastern Province,102318
ÅžÄmitah,Saudi Arabia,Jizan,102451
Sakakah,Saudi Arabia,Al Jawf,102527
ÅžafwÃ¡,Saudi Arabia,Eastern Province,102585
ÅžabyÄ,Saudi Arabia,Jizan,102651
Raá¸©Ä«mah,Saudi Arabia,Eastern Province,102985
RÄbigh,Saudi Arabia,Makkah,103035
Qalâ€˜at BÄ«shah,Saudi Arabia,MinÅ£aqat â€˜AsÄ«r,103369
NajrÄn,Saudi Arabia,NajrÄn,103630
Mecca,Saudi Arabia,Makkah,104515
Khamis Mushait,Saudi Arabia,MinÅ£aqat â€˜AsÄ«r,105072
Jizan,Saudi Arabia,Jizan,105299
Jeddah,Saudi Arabia,Makkah,105343
Ha'il,Saudi Arabia,á¸¨ÄÊ¼il,106281
Duba,Saudi Arabia,MinÅ£aqat TabÅ«k,106909
Buraydah,Saudi Arabia,Al-Qassim,107304
Abqaiq,Saudi Arabia,Eastern Province,107312
Badr á¸¨unayn,Saudi Arabia,Al MadÄ«nah al Munawwarah,107744
Az Zulfi,Saudi Arabia,Ar RiyÄá¸‘,107781
Dhahran,Saudi Arabia,Eastern Province,107797
AÅ£ Å¢araf,Saudi Arabia,Eastern Province,107959
Taâ€™if,Saudi Arabia,Makkah,107968
As Sulayyil,Saudi Arabia,Ar RiyÄá¸‘,108048
Riyadh,Saudi Arabia,Ar RiyÄá¸‘,108410
Ar Rass,Saudi Arabia,Al-Qassim,108435
â€˜Arâ€˜ar,Saudi Arabia,Northern Borders,108512
An NimÄÅŸ,Saudi Arabia,MinÅ£aqat â€˜AsÄ«r,108617
Qurayyat,Saudi Arabia,Al Jawf,108648
Al Wajh,Saudi Arabia,MinÅ£aqat TabÅ«k,108773
Al â€˜UlÃ¡,Saudi Arabia,Al MadÄ«nah al Munawwarah,108841
Al QayÅŸÅ«mah,Saudi Arabia,Eastern Province,108918
Al QaÅ£Ä«f,Saudi Arabia,Eastern Province,108927
Al Munayzilah,Saudi Arabia,Eastern Province,109059
Al Mubarraz,Saudi Arabia,Eastern Province,109101
Al Mithnab,Saudi Arabia,Al-Qassim,109131
Medina,Saudi Arabia,Al MadÄ«nah al Munawwarah,109223
Khobar,Saudi Arabia,Eastern Province,109323
Al KhafjÄ«,Saudi Arabia,Eastern Province,109380
Al JumÅ«m,Saudi Arabia,Makkah,109417
Al Jubayl,Saudi Arabia,Eastern Province,109435
Al HufÅ«f,Saudi Arabia,Eastern Province,109571
Al BukayrÄ«yah,Saudi Arabia,Al-Qassim,109878
Al BaÅ£Å£ÄlÄ«yah,Saudi Arabia,Eastern Province,109915
Al BÄá¸©ah,Saudi Arabia,MinÅ£aqat al BÄá¸©ah,109953
â€˜AfÄ«f,Saudi Arabia,Ar RiyÄá¸‘,110250
Ad Dilam,Saudi Arabia,Ar RiyÄá¸‘,110314
Ad DawÄdimÄ«,Saudi Arabia,Ar RiyÄá¸‘,110325
Dammam,Saudi Arabia,Eastern Province,110336
AbÅ« â€˜ArÄ«sh,Saudi Arabia,Jizan,110619
Abha,Saudi Arabia,MinÅ£aqat â€˜AsÄ«r,110690
Ash ShafÄ,Saudi Arabia,Makkah,410096
Unaizah,Saudi Arabia,Al-Qassim,8394316
Honiara,Solomon Islands,Guadalcanal,2108502
Victoria,Seychelles,English River,241131
Zalingei,Sudan,Central Darfur,363533
Wad Medani,Sudan,Al JazÄ«rah,364103
Umm Ruwaba,Sudan,ShamÄl KurdufÄn,364706
Omdurman,Sudan,Khartoum,365137
TokÄr,Sudan,Red Sea,366323
TandaltÄ«,Sudan,White Nile,366426
Singa,Sudan,SinnÄr,366847
Shendi,Sudan,River Nile,367308
SawÄkin,Sudan,Red Sea,367544
Sinnar,Sudan,SinnÄr,367644
Rabak,Sudan,White Nile,368277
Maiurno,Sudan,SinnÄr,370838
Kosti,Sudan,White Nile,371760
Kuraymah,Sudan,Northern State,371870
KinÄna,Sudan,SinnÄr,372386
Kassala,Sudan,Kassala,372753
Kadugli,Sudan,Southern Kordofan,373141
Doka,Sudan,Al Qaá¸‘Ärif,376332
Dilling,Sudan,Southern Kordofan,376450
Port Sudan,Sudan,Red Sea,377039
Berber,Sudan,River Nile,377690
BÄrah,Sudan,ShamÄl KurdufÄn,377724
Atbara,Sudan,River Nile,378231
As SÅ«kÄ«,Sudan,SinnÄr,378271
Ar Ruseris,Sudan,Blue Nile,378459
Ar Rahad,Sudan,ShamÄl KurdufÄn,378493
An NuhÅ«d,Sudan,West Kordofan State,378699
El Obeid,Sudan,ShamÄl KurdufÄn,379003
Al QiÅ£ena,Sudan,White Nile,379014
Al Qadarif,Sudan,Al Qaá¸‘Ärif,379062
Al Mijlad,Sudan,West Kordofan State,379102
Al ManÄqil,Sudan,Al JazÄ«rah,379149
Khartoum,Sudan,Khartoum,379252
Geneina,Sudan,Western Darfur,379303
Al HilÄliyya,Sudan,Al JazÄ«rah,379406
Al á¸¨awÄtah,Sudan,Al Qaá¸‘Ärif,379416
Al Hasaheisa,Sudan,Al JazÄ«rah,379427
El Fasher,Sudan,Northern Darfur,379555
El Bauga,Sudan,River Nile,379630
Ad Douiem,Sudan,White Nile,380129
El Daein,Sudan,Eastern Darfur,380148
Ad Dindar,Sudan,SinnÄr,380151
Ed Damer,Sudan,River Nile,380173
Ad-Damazin,Sudan,Blue Nile,380174
AbÅ« Zabad,Sudan,West Kordofan State,380348
Abu Jibeha,Sudan,Southern Kordofan,380757
UmeÃ¥,Sweden,VÃ¤sterbotten,602150
SkellefteÃ¥,Sweden,VÃ¤sterbotten,602913
PiteÃ¥,Sweden,Norrbotten,603570
LuleÃ¥,Sweden,Norrbotten,604490
Kiruna,Sweden,Norrbotten,605155
Boden,Sweden,Norrbotten,606531
Ystad,Sweden,SkÃ¥ne,2662149
Visby,Sweden,Gotland,2662689
VÃ¤xjÃ¶,Sweden,Kronoberg,2663536
VÃ¤stervik,Sweden,Kalmar,2664203
VÃ¤sterÃ¥s,Sweden,VÃ¤stmanland,2664454
VÃ¤rnamo,Sweden,JÃ¶nkÃ¶ping,2664855
Varberg,Sweden,Halland,2664996
VÃ¤nersborg,Sweden,VÃ¤stra GÃ¶taland,2665171
Vallentuna,Sweden,Stockholm,2665452
Uppsala,Sweden,Uppsala,2666199
Upplands VÃ¤sby,Sweden,Stockholm,2666238
Uddevalla,Sweden,VÃ¤stra GÃ¶taland,2666670
Tumba,Sweden,Stockholm,2667094
Tullinge,Sweden,Stockholm,2667109
TrollhÃ¤ttan,Sweden,VÃ¤stra GÃ¶taland,2667303
Trelleborg,Sweden,SkÃ¥ne,2667402
TÃ¤by,Sweden,Stockholm,2669772
Sundsvall,Sweden,VÃ¤sternorrland,2670781
Sundbyberg,Sweden,Stockholm,2670879
Stockholm,Sweden,Stockholm,2673730
Solna,Sweden,Stockholm,2675397
Sollentuna,Sweden,Stockholm,2675408
SÃ¶dertÃ¤lje,Sweden,Stockholm,2676176
SkÃ¶vde,Sweden,VÃ¤stra GÃ¶taland,2677234
Skara,Sweden,VÃ¤stra GÃ¶taland,2678210
Sandviken,Sweden,GÃ¤vleborg,2680075
RÃ¥sunda,Sweden,Stockholm,2683034
Partille,Sweden,VÃ¤stra GÃ¶taland,2684395
Ã–stersund,Sweden,JÃ¤mtland,2685750
Ã–stermalm,Sweden,Stockholm,2685828
Oskarshamn,Sweden,Kalmar,2686162
Ã–rnskÃ¶ldsvik,Sweden,VÃ¤sternorrland,2686469
Ã–rebro,Sweden,Ã–rebro,2686657
NykÃ¶ping,Sweden,SÃ¶dermanland,2687700
NorrtÃ¤lje,Sweden,Stockholm,2688250
NorrkÃ¶ping,Sweden,Ã–stergÃ¶tland,2688368
NÃ¤ssjÃ¶,Sweden,JÃ¶nkÃ¶ping,2690170
Nacka,Sweden,Stockholm,2690580
Motala,Sweden,Ã–stergÃ¶tland,2690960
MÃ¶lndal,Sweden,VÃ¤stra GÃ¶taland,2691459
MÃ¤rsta,Sweden,Stockholm,2692475
MalmÃ¶,Sweden,SkÃ¥ne,2692969
Lund,Sweden,SkÃ¥ne,2693678
LinkÃ¶ping,Sweden,Ã–stergÃ¶tland,2694762
LidkÃ¶ping,Sweden,VÃ¤stra GÃ¶taland,2696329
LidingÃ¶,Sweden,Stockholm,2696334
Lerum,Sweden,VÃ¤stra GÃ¶taland,2696503
Landskrona,Sweden,SkÃ¥ne,2697720
Kungsbacka,Sweden,Halland,2698729
KungÃ¤lv,Sweden,VÃ¤stra GÃ¶taland,2698739
Kristinehamn,Sweden,VÃ¤rmland,2699282
Kristianstad,Sweden,SkÃ¥ne,2699310
KÃ¶ping,Sweden,VÃ¤stmanland,2699791
Katrineholm,Sweden,SÃ¶dermanland,2701223
Karlstad,Sweden,VÃ¤rmland,2701680
Karlskrona,Sweden,Blekinge,2701713
Karlskoga,Sweden,Ã–rebro,2701715
Karlshamn,Sweden,Blekinge,2701727
Kalmar,Sweden,Kalmar,2702261
JÃ¶nkÃ¶ping,Sweden,JÃ¶nkÃ¶ping,2702979
Jakobsberg,Sweden,Stockholm,2703396
Huskvarna,Sweden,JÃ¶nkÃ¶ping,2704136
Huddinge,Sweden,Stockholm,2704620
Helsingborg,Sweden,SkÃ¥ne,2706767
HÃ¤ssleholm,Sweden,SkÃ¥ne,2707399
HÃ¤rnÃ¶sand,Sweden,VÃ¤sternorrland,2707684
Haninge,Sweden,Stockholm,2707953
Halmstad,Sweden,Halland,2708365
GÃ¶teborg,Sweden,VÃ¤stra GÃ¶taland,2711537
GÃ¤vle,Sweden,GÃ¤vleborg,2712414
Gamla Uppsala,Sweden,Uppsala,2712993
Falun,Sweden,Dalarna,2715459
FalkÃ¶ping,Sweden,VÃ¤stra GÃ¶taland,2715568
Falkenberg,Sweden,Halland,2715573
EslÃ¶v,Sweden,SkÃ¥ne,2715946
Eskilstuna,Sweden,SÃ¶dermanland,2715953
EnkÃ¶ping,Sweden,Uppsala,2716166
Bromma,Sweden,Stockholm,2719111
BorlÃ¤nge,Sweden,Dalarna,2720383
BorÃ¥s,Sweden,VÃ¤stra GÃ¶taland,2720501
Boo,Sweden,Stockholm,2721259
Ã…rsta,Sweden,Stockholm,2725201
Ã„ngelholm,Sweden,SkÃ¥ne,2725901
AlingsÃ¥s,Sweden,VÃ¤stra GÃ¶taland,2726756
Ã…kersberga,Sweden,Stockholm,2727234
Majorna,Sweden,VÃ¤stra GÃ¶taland,6619708
Singapore,Singapore,Central Singapore,1880252
Jamestown,Saint Helena,Saint Helena,3370903
Trbovlje,Slovenia,Trbovlje,3188915
Velenje,Slovenia,Velenje,3189075
Ptuj,Slovenia,Ptuj,3192241
Novo Mesto,Slovenia,Novo Mesto,3194351
Maribor,Slovenia,Maribor,3195506
Ljubljana,Slovenia,Ljubljana,3196359
Kranj,Slovenia,Kranj,3197378
Koper,Slovenia,Koper-Capodistria,3197753
Celje,Slovenia,Celje,3202781
Longyearbyen,Svalbard and Jan Mayen,Svalbard,2729907
Vranov nad TopÄ¾ou,Slovakia,PreÅ¡ovskÃ½,723195
TrebiÅ¡ov,Slovakia,KoÅ¡ickÃ½,723358
StarÃ¡ Ä½ubovÅˆa,Slovakia,PreÅ¡ovskÃ½,723505
SpiÅ¡skÃ¡ NovÃ¡ Ves,Slovakia,KoÅ¡ickÃ½,723526
Snina,Slovakia,PreÅ¡ovskÃ½,723559
RoÅ¾Åˆava,Slovakia,KoÅ¡ickÃ½,723713
RimavskÃ¡ Sobota,Slovakia,BanskobystrickÃ½,723736
PreÅ¡ov,Slovakia,PreÅ¡ovskÃ½,723819
Poprad,Slovakia,PreÅ¡ovskÃ½,723846
Michalovce,Slovakia,KoÅ¡ickÃ½,724144
KoÅ¡ice,Slovakia,KoÅ¡ickÃ½,724443
KeÅ¾marok,Slovakia,PreÅ¡ovskÃ½,724503
HumennÃ©,Slovakia,PreÅ¡ovskÃ½,724627
Bardejov,Slovakia,PreÅ¡ovskÃ½,725168
Zvolen,Slovakia,BanskobystrickÃ½,3056459
ZlatÃ© Moravce,Slovakia,Nitriansky,3056495
Å½ilina,Slovakia,Å½ilinskÃ½,3056508
Å½iar nad Hronom,Slovakia,BanskobystrickÃ½,3056523
Trnava,Slovakia,TrnavskÃ½,3057124
TrenÄÃ­n,Slovakia,TrenÄiansky,3057140
Skalica,Slovakia,TrnavskÃ½,3057630
Senica,Slovakia,TrnavskÃ½,3057691
Sellye,Slovakia,Nitriansky,3057769
RuÅ¾omberok,Slovakia,Å½ilinskÃ½,3057789
PÃºchov,Slovakia,Nitriansky,3057963
Prievidza,Slovakia,Nitriansky,3058000
PovaÅ¾skÃ¡ Bystrica,Slovakia,TrenÄiansky,3058060
PieÅ¡Å¥any,Slovakia,TrnavskÃ½,3058202
Pezinok,Slovakia,BratislavskÃ½,3058210
PartizÃ¡nske,Slovakia,Nitriansky,3058268
NovÃ© ZÃ¡mky,Slovakia,Nitriansky,3058472
NovÃ© Mesto nad VÃ¡hom,Slovakia,TrenÄiansky,3058477
Nitra,Slovakia,Nitriansky,3058531
Martin,Slovakia,Å½ilinskÃ½,3058780
Malacky,Slovakia,BratislavskÃ½,3058897
LuÄenec,Slovakia,BanskobystrickÃ½,3058986
LiptovskÃ½ MikulÃ¡Å¡,Slovakia,Å½ilinskÃ½,3059050
Levice,Slovakia,Nitriansky,3059101
KysuckÃ© NovÃ© Mesto,Slovakia,Å½ilinskÃ½,3059179
KomÃ¡rno,Slovakia,Nitriansky,3059436
Hlohovec,Slovakia,TrnavskÃ½,3060095
HandlovÃ¡,Slovakia,Nitriansky,3060139
Galanta,Slovakia,TrnavskÃ½,3060219
DunajskÃ¡ Streda,Slovakia,TrnavskÃ½,3060308
Dubnica nad VÃ¡hom,Slovakia,Nitriansky,3060346
DolnÃ½ KubÃ­n,Slovakia,Å½ilinskÃ½,3060405
Detva,Slovakia,BanskobystrickÃ½,3060589
ÄŒadca,Slovakia,Å½ilinskÃ½,3060835
Brezno,Slovakia,BanskobystrickÃ½,3060950
Bratislava,Slovakia,BratislavskÃ½,3060972
BanskÃ¡ Bystrica,Slovakia,BanskobystrickÃ½,3061186
BÃ¡novce nad Bebravou,Slovakia,TrenÄiansky,3061188
Waterloo,Sierra Leone,Western Area,2403094
Segbwema,Sierra Leone,Eastern Province,2404041
Port Loko,Sierra Leone,Northern Province,2404433
Makeni,Sierra Leone,Northern Province,2406407
Lunsar,Sierra Leone,Northern Province,2406916
Koidu,Sierra Leone,Eastern Province,2407656
Kenema,Sierra Leone,Eastern Province,2407790
Kabala,Sierra Leone,Northern Province,2408329
Freetown,Sierra Leone,Western Area,2409306
Bo,Sierra Leone,Southern Province,2410048
San Marino,San Marino,San Marino,3168070
Ziguinchor,Senegal,Ziguinchor,2243940
VÃ©lingara,Senegal,Kolda,2244177
Touba,Senegal,Diourbel,2244322
TiÃ©bo,Senegal,Diourbel,2244616
ThiÃ¨s Nones,Senegal,ThiÃ¨s,2244799
Tambacounda,Senegal,Tambacounda,2244991
SÃ©dhiou,Senegal,SÃ©dhiou,2245704
Saint-Louis,Senegal,Saint-Louis,2246452
Richard-Toll,Senegal,Saint-Louis,2246544
Pout,Senegal,ThiÃ¨s,2246606
Pourham,Senegal,Fatick,2246608
Pikine,Senegal,Dakar,2246678
Nioro du Rip,Senegal,Kaolack,2247157
NguÃ©khokh,Senegal,ThiÃ¨s,2247381
NdibÃ¨ne Dahra,Senegal,Louga,2247813
MÃ©khÃ©,Senegal,ThiÃ¨s,2248409
MbakÃ©,Senegal,Diourbel,2248698
Matam,Senegal,Matam,2248752
Louga,Senegal,Louga,2249222
Kolda,Senegal,Kolda,2249782
KÃ©dougou,Senegal,KÃ©dougou,2250645
Kayar,Senegal,ThiÃ¨s,2250677
Kaolack,Senegal,Kaolack,2250805
Kaffrine,Senegal,Kaffrine,2251007
Joal-Fadiout,Senegal,ThiÃ¨s,2251084
GuinguinÃ©o,Senegal,Fatick,2251230
Dara,Senegal,Louga,2253277
Dakar,Senegal,Dakar,2253354
Bignona,Senegal,Ziguinchor,2253901
Wanlaweyn,Somalia,Lower Shabeelle,50672
Qoryooley,Somalia,Lower Shabeelle,52867
Qandala,Somalia,Bari,53157
Mogadishu,Somalia,Banaadir,53654
Marka,Somalia,Lower Shabeelle,54225
Luuq,Somalia,Gedo,54715
Kismayo,Somalia,Lower Juba,55671
Jilib,Somalia,Middle Juba,56166
Jawhar,Somalia,Middle Shabele,56335
Jamaame,Somalia,Lower Juba,56399
Hargeysa,Somalia,Woqooyi Galbeed,57289
Garoowe,Somalia,Nugaal,58933
Gaalkacyo,Somalia,Mudug,59611
Eyl,Somalia,Nugaal,60019
Ceerigaabo,Somalia,Sanaag,62691
Ceeldheer,Somalia,Galguduud,62788
Buurhakaba,Somalia,Bay,63571
Buulobarde,Somalia,Hiiraan,63689
Burao,Somalia,Togdheer,63795
Bosaso,Somalia,Bari,64013
Berbera,Somalia,Woqooyi Galbeed,64435
Beledweyne,Somalia,Hiiraan,64460
Baidoa,Somalia,Bay,64536
Baardheere,Somalia,Gedo,65170
Afgooye,Somalia,Lower Shabeelle,65785
Laascaanood,Somalia,Sool,400769
Baki,Somalia,Awdal,8045596
Paramaribo,Suriname,Paramaribo,3383330
Lelydorp,Suriname,Wanica,3383714
Yei,South Sudan,Central Equatoria,363619
Yambio,South Sudan,Western Equatoria,363656
Wau,South Sudan,Western Bahr al Ghazal,363885
Aweil,South Sudan,Northern Bahr al Ghazal,364367
Torit,South Sudan,Eastern Equatoria,365742
Tonj,South Sudan,Warrap,365763
Rumbek,South Sudan,Lakes,367927
Malakal,South Sudan,Upper Nile,370737
Juba,South Sudan,Central Equatoria,373303
Gogrial,South Sudan,Warrap,374739
Pajok,South Sudan,Eastern Equatoria,375495
Bor,South Sudan,Jonglei,377241
SÃ£o TomÃ©,Sao Tome and Principe,SÃ£o TomÃ© Island,2410763
Zacatecoluca,El Salvador,La Paz,3582805
UsulutÃ¡n,El Salvador,UsulutÃ¡n,3582883
Soyapango,El Salvador,San Salvador,3583096
Sonzacate,El Salvador,Sonsonate,3583098
Sonsonate,El Salvador,Sonsonate,3583102
Sensuntepeque,El Salvador,CabaÃ±as,3583158
San Vicente,El Salvador,San Vicente,3583178
Santiago de MarÃ­a,El Salvador,UsulutÃ¡n,3583199
Santa Ana,El Salvador,Santa Ana,3583334
San Salvador,El Salvador,San Salvador,3583361
San Rafael Oriente,El Salvador,San Miguel,3583379
San Miguel,El Salvador,San Miguel,3583446
San MartÃ­n,El Salvador,CuscatlÃ¡n,3583471
San Marcos,El Salvador,San Salvador,3583480
San Francisco,El Salvador,MorazÃ¡n,3583747
Quezaltepeque,El Salvador,La Libertad,3583981
Puerto El Triunfo,El Salvador,UsulutÃ¡n,3584003
Santa Tecla,El Salvador,La Libertad,3584257
MetapÃ¡n,El Salvador,Santa Ana,3584384
Mejicanos,El Salvador,San Salvador,3584399
La UniÃ³n,El Salvador,La UniÃ³n,3584772
La Libertad,El Salvador,La Libertad,3585157
Izalco,El Salvador,Sonsonate,3585473
Ilopango,El Salvador,San Salvador,3585484
Delgado,El Salvador,San Salvador,3586814
Cuscatancingo,El Salvador,San Salvador,3586833
Cojutepeque,El Salvador,CuscatlÃ¡n,3586977
Chalchuapa,El Salvador,Santa Ana,3587086
Chalatenango,El Salvador,Chalatenango,3587091
Ayutuxtepeque,El Salvador,San Salvador,3587308
Apopa,El Salvador,San Salvador,3587345
Antiguo CuscatlÃ¡n,El Salvador,La Libertad,3587362
AhuachapÃ¡n,El Salvador,AhuachapÃ¡n,3587426
Aguilares,El Salvador,San Salvador,3587428
Acajutla,El Salvador,Sonsonate,3587498
Philipsburg,Sint Maarten,N/A,3513392
YabrÅ«d,Syria,Rif-dimashq,162627
Å¢ayyibat al ImÄm,Syria,Hama,163270
Tartouss,Syria,Tartus,163345
Tall Rifâ€˜at,Syria,Aleppo,163476
Tallkalakh,Syria,Homs,163533
TallbÄ«sah,Syria,Homs,163779
Å¢afas,Syria,Daraa,163806
Tadmur,Syria,Homs,163808
TÄdif,Syria,Aleppo,163811
Souran,Syria,Hama,163915
SubaykhÄn,Syria,Deir ez-Zor,164025
Ash Shaykh MiskÄ«n,Syria,Daraa,164328
SarÄqib,Syria,Idlib,164816
SalqÄ«n,Syria,Idlib,164898
As SalamÄ«yah,Syria,Hama,164947
Satita,Syria,Tartus,165060
QaÅ£anÄ,Syria,Rif-dimashq,165929
JÄsim,Syria,Daraa,165997
QÄrah,Syria,Rif-dimashq,166111
Nubl,Syria,Aleppo,166331
MaÅŸyÄf,Syria,Hama,167046
Manbij,Syria,Aleppo,167357
Maâ€˜arratmiÅŸrÄ«n,Syria,Idlib,167605
KhÄn ShaykhÅ«n,Syria,Idlib,168325
Kafr ZaytÄ,Syria,Hama,168620
Kafr TakhÄrÄ«m,Syria,Idlib,168629
Kafr Nubl,Syria,Idlib,168661
Kafr LÄhÄ,Syria,Homs,168668
Jisr ash ShughÅ«r,Syria,Idlib,169023
JayrÅ«d,Syria,Rif-dimashq,169113
JarÄbulus,Syria,Aleppo,169179
Jablah,Syria,Latakia,169304
â€˜IrbÄ«n,Syria,Rif-dimashq,169372
Inkhil,Syria,Daraa,169375
Idlib,Syria,Idlib,169389
Homs,Syria,Homs,169577
á¸¨arastÄ,Syria,Rif-dimashq,169897
á¸¨amÄh,Syria,Hama,170017
á¸¨alfÄyÄ,Syria,Hama,170044
Aleppo,Syria,Aleppo,170063
Douma,Syria,Rif-dimashq,170592
Damascus,Syria,Dimashq,170654
Dayr á¸¨Äfir,Syria,Aleppo,170785
Deir ez-Zor,Syria,Deir ez-Zor,170794
Ad DarbÄsÄ«yah,Syria,Al-Hasakah,170887
DÄrayyÄ,Syria,Rif-dimashq,170892
Darâ€˜Ä,Syria,Daraa,170905
Binnish,Syria,Idlib,171451
BÄniyÄs,Syria,Tartus,171830
Az ZabadÄnÄ«,Syria,Rif-dimashq,172059
Iâ€˜zÄz,Syria,Aleppo,172082
â€˜Ayn al â€˜Arab,Syria,Aleppo,172256
At Tall,Syria,Rif-dimashq,172349
Ath Thawrah,Syria,Ar-Raqqah,172374
As SuwaydÄâ€™,Syria,As-Suwayda,172408
AÅŸ Åžanamayn,Syria,Daraa,172469
As SafÄ«rah,Syria,Aleppo,172503
Ar Rastan,Syria,Homs,172946
Ar Raqqah,Syria,Ar-Raqqah,172955
An Nabk,Syria,Rif-dimashq,173193
Al QuÅ£ayfah,Syria,Rif-dimashq,173312
Al QuÅŸayr,Syria,Homs,173322
Al QunayÅ£irah,Syria,Quneitra,173334
Al Qaryatayn,Syria,Homs,173361
Al MayÄdÄ«n,Syria,Deir ez-Zor,173480
Latakia,Syria,Latakia,173576
Al Kiswah,Syria,Rif-dimashq,173598
Al á¸¨asakah,Syria,Al-Hasakah,173811
Al á¸¨arÄk,Syria,Daraa,173819
Al BÄb,Syria,Aleppo,174018
â€˜AfrÄ«n,Syria,Aleppo,174186
Ad DÄnÄ,Syria,Idlib,174259
Ä€lbÅ« KamÄl,Syria,Deir ez-Zor,174448
HajÄ«n,Syria,Deir ez-Zor,174506
Mbabane,Swaziland,Hhohho,934985
Manzini,Swaziland,Manzini,934995
Lobamba,Swaziland,Hhohho,935048
Cockburn Town,Turks and Caicos Islands,N/A,3576994
Fada,Chad,Ennedi-Ouest,244128
Am Timan,Chad,Salamat,245338
AbÃ©chÃ©,Chad,OuaddaÃ¯,245785
Sagh,Chad,Moyen-Chari,2425791
Pala,Chad,Mayo-Kebbi Ouest,2426240
Oum Hadjer,Chad,Batha,2426370
N'Djamena,Chad,Chari-Baguirmi,2427123
Moussoro,Chad,Barh el Gazel,2427336
Moundou,Chad,Logone Occidental,2427455
Mongo,Chad,GuÃ©ra,2427637
Mboursou LÃ©rÃ©,Chad,Mayo-Kebbi Ouest,2428042
Massakory,Chad,Hadjer-Lamis,2428228
Massaguet,Chad,Hadjer-Lamis,2428231
Mao,Chad,Kanem,2428394
LaÃ¯,Chad,TandjilÃ©,2429296
KyabÃ©,Chad,Moyen-Chari,2429344
Koumra,Chad,Mandoul,2429605
Kelo,Chad,TandjilÃ©,2430506
Dourbali,Chad,Chari-Baguirmi,2433055
Doba,Chad,Logone Oriental,2433437
Bongor,Chad,Mayo-Kebbi Est,2434910
Bitkine,Chad,GuÃ©ra,2435124
Benoy,Chad,Logone Occidental,2435508
Ati,Chad,Batha,2436400
Port-aux-FranÃ§ais,French Southern Territories,Kerguelen,1546102
Vogan,Togo,Maritime,2363490
TsÃ©viÃ©,Togo,Maritime,2363534
Tchamba,Togo,Centrale,2363908
Sotouboua,Togo,Centrale,2364079
SokodÃ©,Togo,Centrale,2364104
NotsÃ©,Togo,Plateaux,2364752
Niamtougou,Togo,Kara,2364812
SansannÃ©-Mango,Togo,Savanes,2365190
LomÃ©,Togo,Maritime,2365267
KpalimÃ©,Togo,Plateaux,2365560
Kara,Togo,Kara,2366152
Dapaong,Togo,Savanes,2367164
Bassar,Togo,Kara,2367568
Bafilo,Togo,Kara,2367656
Badou,Togo,Plateaux,2367660
AtakpamÃ©,Togo,Plateaux,2367886
AnÃ©ho,Togo,Maritime,2367990
Ban Talat Yai,Thailand,Phuket,1117652
Ban Talat Nua,Thailand,Phuket,1117656
Sam Roi Yot,Thailand,Prachuap Khiri Khan,1117823
Phetchaburi,Thailand,Phetchaburi,1149698
Trang,Thailand,Trang,1150007
Thung Song,Thailand,Nakhon Si Thammarat,1150085
Thoen,Thailand,Lampang,1150154
Thap Than,Thailand,Uthai Thani,1150210
Tha Muang,Thailand,Kanchanaburi,1150246
Tha Maka,Thailand,Kanchanaburi,1150275
Tak,Thailand,Tak,1150490
Surat Thani,Thailand,Surat Thani,1150515
Sukhothai,Thailand,Sukhothai,1150533
Si Satchanalai,Thailand,Sukhothai,1150624
Sawankhalok,Thailand,Sukhothai,1150681
San Pa Tong,Thailand,Chiang Mai,1150728
San Kamphaeng,Thailand,Chiang Mai,1150732
Ron Phibun,Thailand,Nakhon Si Thammarat,1150921
Ratchaburi,Thailand,Ratchaburi,1150954
Ranong,Thailand,Ranong,1150965
Pran Buri,Thailand,Prachuap Khiri Khan,1151063
Prachuap Khiri Khan,Thailand,Prachuap Khiri Khan,1151074
Phunphin,Thailand,Surat Thani,1151211
Phuket,Thailand,Phuket,1151254
Photharam,Thailand,Ratchaburi,1151340
Phayao,Thailand,Phayao,1151426
Pa Sang,Thailand,Lamphun,1151528
Nakhon Si Thammarat,Thailand,Nakhon Si Thammarat,1151933
Mae Sot,Thailand,Tak,1152188
Mae Sai,Thailand,Chiang Rai,1152194
Mae Ramat,Thailand,Tak,1152202
Mae Chan,Thailand,Chiang Rai,1152227
Lat Yao,Thailand,Nakhon Sawan,1152377
Lang Suan,Thailand,Chumphon,1152432
Lamphun,Thailand,Lamphun,1152468
Lampang,Thailand,Lampang,1152473
Kui Buri,Thailand,Prachuap Khiri Khan,1152562
Krabi,Thailand,Krabi,1152633
Khao Yoi,Thailand,Phetchaburi,1152919
Khanu Woralaksaburi,Thailand,Kamphaeng Phet,1152953
Kathu,Thailand,Phuket,1153035
Kanchanaburi,Thailand,Kanchanaburi,1153081
Kamphaeng Phet,Thailand,Kamphaeng Phet,1153090
Huai Yot,Thailand,Trang,1153241
Hua Hin,Thailand,Prachuap Khiri Khan,1153269
Hang Dong,Thailand,Chiang Mai,1153386
Dok Kham Tai,Thailand,Phayao,1153464
Damnoen Saduak,Thailand,Ratchaburi,1153513
Chumphon,Thailand,Chumphon,1153557
Chom Bueng,Thailand,Ratchaburi,1153646
Chiang Rai,Thailand,Chiang Rai,1153669
Chiang Mai,Thailand,Chiang Mai,1153671
Cha-am,Thailand,Phetchaburi,1153807
Bo Phloi,Thailand,Kanchanaburi,1153850
Ban Tak,Thailand,Tak,1154677
Ko Samui,Thailand,Surat Thani,1154689
Ban Pong,Thailand,Ratchaburi,1155139
Ban Na San,Thailand,Surat Thani,1156046
Ban Na,Thailand,Sukhothai,1156257
Bang Saphan,Thailand,Prachuap Khiri Khan,1157662
Bang Phae,Thailand,Ratchaburi,1157683
Nong Kung Si,Thailand,Kalasin,1595679
Ban Nong Wua So,Thailand,Changwat Udon Thani,1599640
Ban Mai,Thailand,Songkhla,1601579
Ban Huai Thalaeng,Thailand,Nakhon Ratchasima,1603235
Ban Khlong Bang Sao Thong,Thailand,Samut Prakan,1604452
Na Klang,Thailand,Changwat Nong Bua Lamphu,1604654
Yasothon,Thailand,Yasothon,1604769
Yaring,Thailand,Pattani,1604771
Yala,Thailand,Yala,1604870
Wiset Chaichan,Thailand,Ang Thong,1605018
Wichian Buri,Thailand,Phetchabun,1605024
Warin Chamrap,Thailand,Changwat Ubon Ratchathani,1605069
Wang Saphung,Thailand,Loei,1605102
Wang Noi,Thailand,Phra Nakhon Si Ayutthaya,1605118
Wang Nam Yen,Thailand,Sa Kaeo,1605119
Uttaradit,Thailand,Uttaradit,1605215
Uthai Thani,Thailand,Uthai Thani,1605221
Udon Thani,Thailand,Changwat Udon Thani,1605239
Ubon Ratchathani,Thailand,Changwat Ubon Ratchathani,1605245
Trat,Thailand,Trat,1605279
Tha Yang,Thailand,Phetchaburi,1605467
Tha Ruea,Thailand,Phra Nakhon Si Ayutthaya,1605509
Thap Khlo,Thailand,Phichit,1605538
Tha Mai,Thailand,Chanthaburi,1605601
Tha Bo,Thailand,Nong Khai,1605677
Taphan Hin,Thailand,Phichit,1605754
Tak Bai,Thailand,Narathiwat,1605957
Surin,Thailand,Surin,1606030
Suphan Buri,Thailand,Suphan Buri,1606033
Su-ngai Kolok,Thailand,Narathiwat,1606050
Songkhla,Thailand,Songkhla,1606147
Si Sa Ket,Thailand,Sisaket,1606239
Si Racha,Thailand,Chon Buri,1606250
Sing Buri,Thailand,Sing Buri,1606270
Seka,Thailand,Changwat Bueng Kan,1606343
Sawang Daen Din,Thailand,Sakon Nakhon,1606350
Satun,Thailand,Satun,1606376
Sattahip,Thailand,Chon Buri,1606386
Saraburi,Thailand,Sara Buri,1606418
Samut Songkhram,Thailand,Samut Songkhram,1606586
Samut Sakhon,Thailand,Samut Sakhon,1606588
Samut Prakan,Thailand,Samut Prakan,1606590
Sam Phran,Thailand,Nakhon Pathom,1606638
Sakon Nakhon,Thailand,Sakon Nakhon,1606790
Sa Kaeo,Thailand,Sa Kaeo,1606807
Sadao,Thailand,Songkhla,1606939
Roi Et,Thailand,Roi Et,1607001
Rayong,Thailand,Rayong,1607017
Ranot,Thailand,Songkhla,1607068
Ra-ngae,Thailand,Narathiwat,1607083
Prakhon Chai,Thailand,Buriram,1607257
Prachin Buri,Thailand,Prachin Buri,1607280
Phu Kradueng,Thailand,Loei,1607435
Phu Khiao,Thailand,Chaiyaphum,1607439
Phra Pradaeng,Thailand,Samut Prakan,1607508
Phra Phutthabat,Thailand,Sara Buri,1607512
Phra Nakhon Si Ayutthaya,Thailand,Phra Nakhon Si Ayutthaya,1607532
Phrae,Thailand,Phrae,1607552
Phon Charoen,Thailand,Nong Khai,1607615
Phitsanulok,Thailand,Phitsanulok,1607708
Phichit,Thailand,Phichit,1607725
Phibun Mangsahan,Thailand,Changwat Ubon Ratchathani,1607730
Phetchabun,Thailand,Phetchabun,1607737
Phatthalung,Thailand,Phatthalung,1607779
Phan Thong,Thailand,Chon Buri,1607793
Phanom Sarakham,Thailand,Chachoengsao,1607801
Phanat Nikhom,Thailand,Chon Buri,1607838
Phak Hai,Thailand,Phra Nakhon Si Ayutthaya,1607865
Pattani,Thailand,Pattani,1607978
Pathum Thani,Thailand,Pathum Thani,1607983
Pak Phanang,Thailand,Nakhon Si Thammarat,1608033
Pak Kret,Thailand,Nonthaburi,1608048
Pak Chong,Thailand,Nakhon Ratchasima,1608057
Mueang Nonthaburi,Thailand,Nonthaburi,1608133
Non Sung,Thailand,Nakhon Ratchasima,1608136
Nong Phai,Thailand,Phetchabun,1608191
Nong Khai,Thailand,Nong Khai,1608232
Nong Khae,Thailand,Sara Buri,1608239
Nong Bua Lamphu,Thailand,Changwat Nong Bua Lamphu,1608269
Narathiwat,Thailand,Narathiwat,1608409
Nang Rong,Thailand,Buriram,1608424
Nan,Thailand,Nan,1608452
Nam Som,Thailand,Changwat Udon Thani,1608462
Nakhon Sawan,Thailand,Nakhon Sawan,1608527
Nakhon Ratchasima,Thailand,Nakhon Ratchasima,1608529
Nakhon Phanom,Thailand,Nakhon Phanom,1608531
Nakhon Pathom,Thailand,Nakhon Pathom,1608534
Nakhon Nayok,Thailand,Nakhon Nayok,1608539
Nakhon Luang,Thailand,Phra Nakhon Si Ayutthaya,1608541
Mukdahan,Thailand,Mukdahan,1608597
Maha Sarakham,Thailand,Maha Sarakham,1608900
Lop Buri,Thailand,Lop Buri,1609032
Lom Sak,Thailand,Phetchabun,1609043
Loei,Thailand,Loei,1609071
Laem Sing,Thailand,Chanthaburi,1609278
Kut Chap,Thailand,Changwat Udon Thani,1609324
Kuchinarai,Thailand,Kalasin,1609345
Bangkok,Thailand,Bangkok,1609350
Krathum Baen,Thailand,Samut Sakhon,1609395
Klaeng,Thailand,Rayong,1609610
Khon Kaen,Thailand,Khon Kaen,1609776
Khon Buri,Thailand,Nakhon Ratchasima,1609795
Khlong Luang,Thailand,Pathum Thani,1609899
Khao Wong,Thailand,Kalasin,1609990
Kaset Wisai,Thailand,Roi Et,1610185
Kaset Sombun,Thailand,Chaiyaphum,1610187
Kantharalak,Thailand,Sisaket,1610227
Kamalasai,Thailand,Kalasin,1610459
Kalasin,Thailand,Kalasin,1610469
Kaeng Khoi,Thailand,Sara Buri,1610503
Kaeng Khro,Thailand,Chaiyaphum,1610505
Kabin Buri,Thailand,Prachin Buri,1610538
Hat Yai,Thailand,Songkhla,1610780
Det Udom,Thailand,Changwat Ubon Ratchathani,1610940
Den Chai,Thailand,Phrae,1610943
Dan Khun Thot,Thailand,Nakhon Ratchasima,1610963
Chum Phae,Thailand,Khon Kaen,1611026
Chon Daen,Thailand,Phetchabun,1611106
Chon Buri,Thailand,Chon Buri,1611110
Chok Chai,Thailand,Nakhon Ratchasima,1611135
Chanthaburi,Thailand,Chanthaburi,1611269
Chaiyaphum,Thailand,Chaiyaphum,1611407
Chai Nat,Thailand,Chai Nat,1611416
Chai Badan,Thailand,Lop Buri,1611424
Chachoengsao,Thailand,Chachoengsao,1611439
Buriram,Thailand,Buriram,1611453
Bua Yai,Thailand,Nakhon Ratchasima,1611492
Betong,Thailand,Yala,1611635
Ban Selaphum,Thailand,Roi Et,1613284
Ban Rangsit,Thailand,Pathum Thani,1613769
Phatthaya,Thailand,Chon Buri,1614295
Ban Phan Don,Thailand,Changwat Udon Thani,1614336
Ban Phai,Thailand,Khon Kaen,1614455
Ban Phaeo,Thailand,Samut Sakhon,1614465
Ban Mo,Thailand,Sara Buri,1616658
Ban Lam Luk Ka,Thailand,Pathum Thani,1617111
Bang Rakam,Thailand,Phitsanulok,1619276
Bang Racham,Thailand,Sing Buri,1619281
Bang Pakong,Thailand,Chachoengsao,1619363
Bang Pa-in,Thailand,Phra Nakhon Si Ayutthaya,1619369
Bang Mun Nak,Thailand,Phichit,1619400
Bang Len,Thailand,Nakhon Pathom,1619415
Bang Lamung,Thailand,Chon Buri,1619423
Bang Kruai,Thailand,Nonthaburi,1619434
Bang Krathum,Thailand,Phitsanulok,1619437
Bang Bua Thong,Thailand,Nonthaburi,1619602
Bang Ban,Thailand,Phra Nakhon Si Ayutthaya,1619616
Ban Dung,Thailand,Changwat Udon Thani,1619650
Ban Chang,Thailand,Rayong,1620254
Ban Bueng,Thailand,Chon Buri,1620371
Ban Talat Bueng,Thailand,Chon Buri,1620442
Ban Bang Kadi Pathum Thani,Thailand,Phra Nakhon Si Ayutthaya,1620875
Bang Bo District,Thailand,Samut Prakan,1620919
Aranyaprathet,Thailand,Sa Kaeo,1621020
Amnat Charoen,Thailand,Amnat Charoen,1621060
Amphoe Sikhiu,Thailand,Nakhon Ratchasima,1948015
Wichit,Thailand,Phuket,6696291
Ban Chalong,Thailand,Phuket,7091861
Ban Ratsada,Thailand,Phuket,7091912
Yovon,Tajikistan,Khatlon,1220112
Voseâ€™,Tajikistan,Khatlon,1220163
Vakhsh,Tajikistan,Khatlon,1220219
Istaravshan,Tajikistan,Viloyati Sughd,1220253
Tursunzoda,Tajikistan,Republican Subordination,1220301
QÅ­rghonteppa,Tajikistan,Khatlon,1220747
Panjakent,Tajikistan,Viloyati Sughd,1220798
Farkhor,Tajikistan,Khatlon,1220826
Vahdat,Tajikistan,Republican Subordination,1220855
Norak,Tajikistan,Khatlon,1220905
KÅ­lob,Tajikistan,Khatlon,1221194
Kolkhozobod,Tajikistan,Khatlon,1221259
Khorugh,Tajikistan,Gorno-Badakhshan,1221328
Ishqoshim,Tajikistan,Gorno-Badakhshan,1221614
Hisor,Tajikistan,Republican Subordination,1221714
Dushanbe,Tajikistan,Dushanbe,1221874
Danghara,Tajikistan,Khatlon,1221965
Chubek,Tajikistan,Khatlon,1221997
Boshkengash,Tajikistan,Dushanbe,1222107
Proletar,Tajikistan,Viloyati Sughd,1514839
KhÅ­jand,Tajikistan,Viloyati Sughd,1514879
Konibodom,Tajikistan,Viloyati Sughd,1514891
Isfara,Tajikistan,Viloyati Sughd,1514896
Chkalov,Tajikistan,Viloyati Sughd,1538311
Moskovskiy,Tajikistan,Khatlon,8416817
Suai,East Timor,Cova Lima,1626459
Maubara,East Timor,LiquiÃ§Ã¡,1635826
Maliana,East Timor,Bobonaro,1636670
Liquica,East Timor,LiquiÃ§Ã¡,1637730
Dili,East Timor,DÃ­li,1645457
Baucau,East Timor,Baucau,1649539
Aileu,East Timor,Aileu,1651816
Same,East Timor,Manufahi,1937031
Lospalos,East Timor,LautÃ©m,1937274
Venilale,East Timor,Baucau,1943235
Balkanabat,Turkmenistan,Balkan,161616
Kaka,Turkmenistan,Ahal,161901
Gumdag,Turkmenistan,Balkan,161943
Gazanjyk,Turkmenistan,Balkan,161974
Abadan,Turkmenistan,Ahal,162099
Baharly,Turkmenistan,Ahal,162158
Ashgabat,Turkmenistan,Ahal,162183
Annau,Turkmenistan,Ahal,162199
Yylanly,Turkmenistan,DaÅŸoguz,601432
Tagta,Turkmenistan,DaÅŸoguz,601475
TÃ¼rkmenbaÅŸy,Turkmenistan,Balkan,601594
KÃ¶neÃ¼rgench,Turkmenistan,DaÅŸoguz,601608
Boldumsaz,Turkmenistan,DaÅŸoguz,601661
DaÅŸoguz,Turkmenistan,DaÅŸoguz,601734
YolÃ¶ten,Turkmenistan,Mary,1218021
Tejen,Turkmenistan,Ahal,1218239
Seydi,Turkmenistan,Mary,1218420
SaÃ½at,Turkmenistan,Lebap,1218436
Mary,Turkmenistan,Mary,1218667
Atamyrat,Turkmenistan,Lebap,1219002
Gowurdak,Turkmenistan,Lebap,1219392
TÃ¼rkmenabat,Turkmenistan,Lebap,1219649
Bayramaly,Turkmenistan,Mary,1219762
Gazojak,Turkmenistan,Lebap,1514792
Zaghouan,Tunisia,ZaghwÄn,2464041
Oued Lill,Tunisia,TÅ«nis,2464168
Tunis,Tunisia,TÅ«nis,2464470
Tozeur,Tunisia,Tawzar,2464648
Tataouine,Tunisia,Tataouine,2464701
Thala,Tunisia,Al QaÅŸrayn,2464795
Takelsa,Tunisia,NÄbul,2464804
Tajerouine,Tunisia,Kef,2464809
Sousse,Tunisia,SÅ«sah,2464915
Siliana,Tunisia,SilyÄnah,2465030
Sidi Bouzid,Tunisia,SÄ«dÄ« BÅ« Zayd,2465840
Skanes,Tunisia,Al MunastÄ«r,2467246
Sfax,Tunisia,ÅžafÄqis,2467454
La Sebala du Mornag,Tunisia,TÅ«nis,2467521
RadÃ¨s,Tunisia,TÅ«nis,2467815
Ksour Essaf,Tunisia,Al MahdÄ«yah,2467856
Korba,Tunisia,NÄbul,2467920
KÃ©libia,Tunisia,NÄbul,2467959
Kebili,Tunisia,QibilÄ«,2468018
Ksar Hellal,Tunisia,Al MunastÄ«r,2468106
Carthage,Tunisia,TÅ«nis,2468245
El Fahs,Tunisia,ZaghwÄn,2468285
Galaat el Andeless,Tunisia,Ariana,2468329
Gafsa,Tunisia,Gafsa,2468353
GabÃ¨s,Tunisia,QÄbis,2468369
Nefta,Tunisia,Tawzar,2468561
Nabeul,Tunisia,NÄbul,2468579
Midoun,Tunisia,MadanÄ«n,2468925
Mateur,Tunisia,Banzart,2469088
Msaken,Tunisia,SÅ«sah,2469140
Menzel Jemil,Tunisia,Banzart,2469256
Mennzel Bou Zelfa,Tunisia,NÄbul,2469262
Menzel Bourguiba,Tunisia,Banzart,2469264
Menzel Abderhaman,Tunisia,Banzart,2469268
Manouba,Tunisia,Manouba,2469274
Medjez el Bab,Tunisia,BÄjah,2469386
Medenine,Tunisia,MadanÄ«n,2469473
Jendouba,Tunisia,JundÅ«bah,2470088
Zarzis,Tunisia,MadanÄ«n,2470173
Djemmal,Tunisia,Al MunastÄ«r,2470191
Houmt Souk,Tunisia,MadanÄ«n,2470384
Hammam Sousse,Tunisia,SÅ«sah,2470579
Hammam-Lif,Tunisia,TÅ«nis,2470588
La Goulette,Tunisia,TÅ«nis,2470656
Douz,Tunisia,QibilÄ«,2471287
Douar Tindja,Tunisia,Banzart,2471475
Dar Chabanne,Tunisia,NÄbul,2471637
Ben Arous,Tunisia,Bin â€˜ArÅ«s,2472479
Bizerte,Tunisia,Banzart,2472706
Beni Khiar,Tunisia,NÄbul,2472722
BÃ©ja,Tunisia,BÄjah,2472774
Zouila,Tunisia,Al MahdÄ«yah,2472833
Chebba,Tunisia,Al MahdÄ«yah,2473229
Ariana,Tunisia,Ariana,2473247
Ar Rudayyif,Tunisia,Gafsa,2473257
Ouardenine,Tunisia,Al MunastÄ«r,2473420
Kairouan,Tunisia,Al QayrawÄn,2473449
Kasserine,Tunisia,Al QaÅŸrayn,2473457
Gremda,Tunisia,ÅžafÄqis,2473470
Monastir,Tunisia,Al MunastÄ«r,2473493
La Mohammedia,Tunisia,TÅ«nis,2473499
Metlaoui,Tunisia,Gafsa,2473517
Al MarsÃ¡,Tunisia,TÅ«nis,2473540
Mahdia,Tunisia,Al MahdÄ«yah,2473572
El Kef,Tunisia,Kef,2473634
El Jem,Tunisia,Al MahdÄ«yah,2473654
Hammamet,Tunisia,NÄbul,2473744
El Hamma,Tunisia,QÄbis,2473747
Bekalta,Tunisia,Al MunastÄ«r,2473826
El Alia,Tunisia,Banzart,2473876
Akouda,Tunisia,SÅ«sah,2473913
Douane,Tunisia,NÄbul,2581754
Nukuâ€˜alofa,Tonga,Tongatapu,4032402
YÃ¼ksekova,Turkey,HakkÃ¢ri,296173
Yozgat,Turkey,Yozgat,296562
YeÅŸilli,Turkey,Mardin,296832
Erzin,Turkey,Hatay,296852
YerkÃ¶y,Turkey,Yozgat,296895
Didim,Turkey,AydÄ±n,297090
YataÄŸan,Turkey,MuÄŸla,297564
YalvaÃ§,Turkey,Isparta,297789
YahyalÄ±,Turkey,Kayseri,297917
ViranÅŸehir,Turkey,ÅžanlÄ±urfa,298033
Varto,Turkey,MuÅŸ,298088
Van,Turkey,Van,298117
Cimin,Turkey,Erzincan,298230
UÅŸak,Turkey,UÅŸak,298299
Urla,Turkey,Ä°zmir,298316
ÃœrgÃ¼p,Turkey,NevÅŸehir,298326
ÅžanlÄ±urfa,Turkey,ÅžanlÄ±urfa,298333
Turgutlu,Turkey,Manisa,298806
Tunceli,Turkey,Tunceli,298846
TorbalÄ±,Turkey,Ä°zmir,298935
Tire,Turkey,Ä°zmir,299137
Tekirova,Turkey,Antalya,299445
TavÅŸanlÄ±,Turkey,KÃ¼tahya,299545
Tatvan,Turkey,Bitlis,299582
Tarsus,Turkey,Mersin,299817
Talas,Turkey,Kayseri,299900
Susurluk,Turkey,BalÄ±kesir,300058
SuruÃ§,Turkey,ÅžanlÄ±urfa,300075
Sorgun,Turkey,Yozgat,300352
Soma,Turkey,Manisa,300371
Solhan,Turkey,BingÃ¶l,300377
SÃ¶ke,Turkey,AydÄ±n,300399
Siverek,Turkey,ÅžanlÄ±urfa,300614
Sivas,Turkey,Sivas,300619
ÅžÄ±rnak,Turkey,ÅžÄ±rnak,300640
Simav,Turkey,KÃ¼tahya,300791
Silvan,Turkey,DiyarbakÄ±r,300796
Silopi,Turkey,ÅžÄ±rnak,300797
Silifke,Turkey,Mersin,300808
Siirt,Turkey,Siirt,300822
SeydiÅŸehir,Turkey,Konya,301010
Serinyol,Turkey,Hatay,301089
Serik,Turkey,Antalya,301101
ÅžereflikoÃ§hisar,Turkey,Ankara,301116
Senirkent,Turkey,Isparta,301172
Åžemdinli,Turkey,HakkÃ¢ri,301209
SelÃ§uk,Turkey,Ä°zmir,301256
Seferhisar,Turkey,Ä°zmir,301350
ÅžarkÄ±ÅŸla,Turkey,Sivas,301537
ÅžarkÃ®karaaÄŸaÃ§,Turkey,Isparta,301539
SaraykÃ¶y,Turkey,Denizli,301827
SandÄ±klÄ±,Turkey,Afyonkarahisar,301911
Salihli,Turkey,Manisa,302043
ReyhanlÄ±,Turkey,Hatay,302355
PolatlÄ±,Turkey,Ankara,302525
PazarcÄ±k,Turkey,KahramanmaraÅŸ,302800
Patnos,Turkey,AÄŸrÄ±,302819
Pasinler,Turkey,Erzurum,302824
Osmaniye,Turkey,Osmaniye,303195
OrtakÃ¶y,Turkey,Aksaray,303290
Ortaca,Turkey,MuÄŸla,303354
Ã–demiÅŸ,Turkey,Ä°zmir,303700
Nusaybin,Turkey,Mardin,303750
Nizip,Turkey,Gaziantep,303798
NiÄŸde,Turkey,NiÄŸde,303827
NevÅŸehir,Turkey,NevÅŸehir,303831
Nazilli,Turkey,AydÄ±n,303873
Mut,Turkey,Mersin,304013
MuÅŸ,Turkey,MuÅŸ,304081
MuÄŸla,Turkey,MuÄŸla,304184
Mucur,Turkey,KÄ±rÅŸehir,304196
Milas,Turkey,MuÄŸla,304355
Midyat,Turkey,Mardin,304382
Mercin,Turkey,Mersin,304531
Menemen,Turkey,Ä°zmir,304612
Marmaris,Turkey,MuÄŸla,304782
Mardin,Turkey,Mardin,304797
Manisa,Turkey,Manisa,304827
Manavgat,Turkey,Antalya,304854
Malazgirt,Turkey,MuÅŸ,304916
Malatya,Turkey,Malatya,304922
Mahmutlar,Turkey,Antalya,304964
Lice,Turkey,DiyarbakÄ±r,305089
KÃ¼tahya,Turkey,KÃ¼tahya,305268
KuÅŸadasÄ±,Turkey,AydÄ±n,305359
Kurtalan,Turkey,Siirt,305532
Beykonak,Turkey,Antalya,305680
Kulu,Turkey,Konya,305742
Kulp,Turkey,DiyarbakÄ±r,305750
Kula,Turkey,Manisa,305810
Kozluk,Turkey,Batman,306041
Kozan,Turkey,Adana,306112
KovancÄ±lar,Turkey,ElazÄ±ÄŸ,306207
Korkuteli,Turkey,Antalya,306474
Konya,Turkey,Konya,306571
KÄ±zÄ±ltepe,Turkey,Mardin,307084
Serinhisar,Turkey,Denizli,307211
KÄ±rÅŸehir,Turkey,KÄ±rÅŸehir,307515
KÄ±rkaÄŸaÃ§,Turkey,Manisa,307623
KÄ±rÄ±kkale,Turkey,KÄ±rÄ±kkale,307654
KÄ±rÄ±khan,Turkey,Hatay,307657
Kilis,Turkey,Kilis,307864
Keskin,Turkey,KÄ±rÄ±kkale,308024
Kemer,Turkey,Antalya,308220
KemalpaÅŸa,Turkey,Ä°zmir,308224
Kayseri,Turkey,Kayseri,308464
KarapÄ±nar,Turkey,Konya,309415
Karaman,Turkey,Karaman,309527
AÄŸrÄ±,Turkey,AÄŸrÄ±,309647
KarakoÃ§an,Turkey,ElazÄ±ÄŸ,309663
KaraÃ§oban,Turkey,Erzurum,310004
Kaman,Turkey,KÄ±rÅŸehir,310641
KÃ¢hta,Turkey,AdÄ±yaman,310855
KahramanmaraÅŸ,Turkey,KahramanmaraÅŸ,310859
Kadirli,Turkey,Adana,310892
KadÄ±nhanÄ±,Turkey,Konya,310907
Ä°zmir,Turkey,Ä°zmir,311046
Isparta,Turkey,IÄŸdÄ±r,311073
Ä°dil,Turkey,ÅžÄ±rnak,311704
Hizan,Turkey,Bitlis,312024
HÄ±nÄ±s,Turkey,Erzurum,312114
Hilvan,Turkey,ÅžanlÄ±urfa,312134
Hadim,Turkey,Konya,312899
HacÄ±lar,Turkey,Kayseri,313013
GÃ¼roymak,Turkey,Bitlis,313331
GÃ¶lbaÅŸÄ±,Turkey,AdÄ±yaman,314136
GÃ¶ksun,Turkey,KahramanmaraÅŸ,314188
GenÃ§,Turkey,BingÃ¶l,314648
Gemerek,Turkey,Sivas,314665
Gediz,Turkey,KÃ¼tahya,314716
GazipaÅŸa,Turkey,Antalya,314812
Gaziantep,Turkey,Gaziantep,314830
FoÃ§a,Turkey,Ä°zmir,314903
Fethiye,Turkey,MuÄŸla,314967
Ezine,Turkey,Ã‡anakkale Province,315061
EskiÅŸehir,Turkey,EskiÅŸehir,315202
Erzurum,Turkey,Erzurum,315368
Erzincan,Turkey,Erzincan,315373
Ermenek,Turkey,Karaman,315401
Ergani,Turkey,DiyarbakÄ±r,315468
EreÄŸli,Turkey,Konya,315498
Erdemli,Turkey,Mersin,315515
ErciÅŸ,Turkey,Van,315530
EmirdaÄŸ,Turkey,Afyonkarahisar,315621
Emet,Turkey,KÃ¼tahya,315639
ElmalÄ±,Turkey,Antalya,315697
ElmadaÄŸ,Turkey,Ankara,315720
EleÅŸkirt,Turkey,AÄŸrÄ±,315758
Elbistan,Turkey,KahramanmaraÅŸ,315795
ElazÄ±ÄŸ,Turkey,ElazÄ±ÄŸ,315808
EÄŸirdir,Turkey,Isparta,315905
Edremit,Turkey,BalÄ±kesir,315985
Dursunbey,Turkey,BalÄ±kesir,316102
DÃ¶rtyol,Turkey,Hatay,316284
DoÄŸubayazÄ±t,Turkey,AÄŸrÄ±,316411
DiyarbakÄ±r,Turkey,DiyarbakÄ±r,316541
Diyadin,Turkey,AÄŸrÄ±,316542
Dinar,Turkey,Afyonkarahisar,316634
Develi,Turkey,Kayseri,316795
Denizli,Turkey,Denizli,317109
Demirci,Turkey,Manisa,317241
DargeÃ§it,Turkey,Mardin,317587
Darende,Turkey,Malatya,317588
Ã‡umra,Turkey,Konya,317844
Menderes,Turkey,Ä°zmir,317851
Hakkari,Turkey,HakkÃ¢ri,318137
Cizre,Turkey,ÅžÄ±rnak,318253
Ã‡ine,Turkey,AydÄ±n,318372
CeylanpÄ±nar,Turkey,ÅžanlÄ±urfa,318668
Ceyhan,Turkey,Adana,318675
Ã‡eÅŸme,Turkey,Ä°zmir,318755
Ã‡ermik,Turkey,DiyarbakÄ±r,318766
Ã‡ay,Turkey,Afyonkarahisar,319104
Ã‡aÄŸlayancerit,Turkey,KahramanmaraÅŸ,320004
Burhaniye,Turkey,BalÄ±kesir,320369
Burdur,Turkey,Burdur,320392
BulanÄ±k,Turkey,MuÅŸ,320448
Bucak,Turkey,Burdur,320533
BozyazÄ±,Turkey,Mersin,320552
BozÃ¼yÃ¼k,Turkey,Bilecik,320557
Bozova,Turkey,ÅžanlÄ±urfa,320581
Bor,Turkey,NiÄŸde,320871
Bolvadin,Turkey,Afyonkarahisar,320879
Bodrum,Turkey,MuÄŸla,320995
Bitlis,Turkey,Bitlis,321025
Bismil,Turkey,DiyarbakÄ±r,321031
Birecik,Turkey,ÅžanlÄ±urfa,321062
BingÃ¶l,Turkey,BingÃ¶l,321082
BigadiÃ§,Turkey,BalÄ±kesir,321136
BeyÅŸehir,Turkey,Konya,321191
Besni,Turkey,AdÄ±yaman,321337
Bergama,Turkey,Ä°zmir,321426
Belen,Turkey,Hatay,321572
Belek,Turkey,Antalya,321580
BayÄ±ndÄ±r,Turkey,Ä°zmir,321786
Batman,Turkey,Batman,321836
Baskil,Turkey,ElazÄ±ÄŸ,321929
Banaz,Turkey,UÅŸak,322051
BalÄ±kesir,Turkey,BalÄ±kesir,322165
BahÃ§e,Turkey,Adana,322391
AyvalÄ±k,Turkey,BalÄ±kesir,322673
AydÄ±n,Turkey,AydÄ±n,322830
AÅŸkale,Turkey,Erzurum,323094
Antalya,Turkey,Antalya,323777
Antakya,Turkey,Hatay,323779
Ankara,Turkey,Ankara,323786
Anamur,Turkey,Mersin,323828
AliaÄŸa,Turkey,Ä°zmir,324106
AlaÅŸehir,Turkey,Manisa,324172
Alanya,Turkey,Antalya,324190
AkÅŸehir,Turkey,Konya,324490
Aksaray,Turkey,Aksaray,324496
Akhisar,Turkey,Manisa,324698
AkdaÄŸmadeni,Turkey,Yozgat,324768
AkÃ§akale,Turkey,ÅžanlÄ±urfa,324944
Ahlat,Turkey,Bitlis,325103
Afyonkarahisar,Turkey,Afyonkarahisar,325303
AfÅŸin,Turkey,KahramanmaraÅŸ,325304
AdÄ±yaman,Turkey,AdÄ±yaman,325330
Adilcevaz,Turkey,Bitlis,325336
Adana,Turkey,Adana,325363
Denizciler,Turkey,Hatay,438400
Batikent,Turkey,Ankara,442301
Dalaman,Turkey,MuÄŸla,447273
Zonguldak,Turkey,Zonguldak,737022
Zile,Turkey,Tokat,737054
Zeytinburnu,Turkey,Istanbul,737071
Yomra,Turkey,Trabzon,737421
YeniÅŸehir,Turkey,Bursa,737611
KÃ¶rfez,Turkey,Kocaeli,737961
Yalova,Turkey,Yalova,738025
Yakuplu,Turkey,Istanbul,738064
VezirkÃ¶prÃ¼,Turkey,Samsun,738167
VakfÄ±kebir,Turkey,Trabzon,738228
UzunkÃ¶prÃ¼,Turkey,Edirne,738251
ÃœskÃ¼dar,Turkey,Istanbul,738329
Ãœnye,Turkey,Ordu,738349
Umraniye,Turkey,Istanbul,738377
Turhal,Turkey,Tokat,738618
Trabzon,Turkey,Trabzon,738648
Tosya,Turkey,Kastamonu,738662
Tokat,Turkey,Tokat,738743
Tirebolu,Turkey,Giresun,738753
Terme,Turkey,Samsun,738803
Tepecik,Turkey,Istanbul,738858
TekkekÃ¶y,Turkey,Samsun,738907
TekirdaÄŸ,Turkey,TekirdaÄŸ,738927
TaÅŸova,Turkey,Amasya,739015
TaÅŸkÃ¶prÃ¼,Turkey,Kastamonu,739061
SuÅŸehri,Turkey,Sivas,739209
SÃ¼rmene,Turkey,Trabzon,739215
Sungurlu,Turkey,Ã‡orum,739236
Suluova,Turkey,Amasya,739251
ÅžiÅŸli,Turkey,Istanbul,739549
Sinop,Turkey,Sinop,739600
Silivri,Turkey,Istanbul,739634
Åžebin Karahisar,Turkey,Giresun,739914
SarÄ±kamÄ±ÅŸ,Turkey,Kars,740088
Sapanca,Turkey,Sakarya,740230
Samsun,Turkey,Samsun,740264
Safranbolu,Turkey,KarabÃ¼k,740430
Rize,Turkey,Rize,740483
Osmaneli,Turkey,Bilecik,740881
OsmancÄ±k,Turkey,Ã‡orum,740883
Orhangazi,Turkey,Bursa,741045
Ordu,Turkey,Ordu,741100
Oltu,Turkey,Erzurum,741160
Of,Turkey,Trabzon,741240
Niksar,Turkey,Tokat,741304
NallÄ±han,Turkey,Ankara,741347
MustafakemalpaÅŸa,Turkey,Bursa,741385
Mudanya,Turkey,Bursa,741487
Mimarsinan,Turkey,Istanbul,741529
Merzifon,Turkey,Amasya,741609
Maltepe,Turkey,Istanbul,741763
Malkara,Turkey,TekirdaÄŸ,741771
LÃ¼leburgaz,Turkey,KÄ±rklareli,741855
Kumru,Turkey,Ordu,742238
Korgan,Turkey,Ordu,742658
Kocaali,Turkey,Sakarya,742902
KÄ±zÄ±lcahamam,Turkey,Ankara,743051
KÄ±rklareli,Turkey,KÄ±rklareli,743166
Kestel,Turkey,Bursa,743404
KeÅŸan,Turkey,Edirne,743439
Kelkit,Turkey,GÃ¼mÃ¼ÅŸhane,743537
Kazan,Turkey,Ankara,743615
KavaklÄ±,Turkey,Istanbul,743818
Kastamonu,Turkey,Kastamonu,743882
Kars,Turkey,Kars,743952
Karasu,Turkey,Sakarya,744093
KaramÃ¼rsel,Turkey,Kocaeli,744168
Karacabey,Turkey,Bursa,744537
KarabÃ¼k,Turkey,KarabÃ¼k,744562
KaÄŸÄ±zman,Turkey,Kars,744873
Ä°znik,Turkey,Bursa,745026
Ä°zmit,Turkey,Kocaeli,745028
Ä°stanbul,Turkey,Istanbul,745044
Ä°skilip,Turkey,Ã‡orum,745076
Ä°negol,Turkey,Bursa,745169
Horasan,Turkey,Erzurum,745527
Hopa,Turkey,Artvin,745530
Hendek,Turkey,Sakarya,745664
Hayrabolu,Turkey,TekirdaÄŸ,745697
Havza,Turkey,Samsun,745714
GÃ¼rsu,Turkey,Bursa,746232
GÃ¼rpÄ±nar,Turkey,Istanbul,746234
GÃ¼rgentepe,Turkey,Ordu,746252
Gumushkhane,Turkey,GÃ¼mÃ¼ÅŸhane,746425
GÃ¶rele,Turkey,Giresun,746565
GÃ¶nen,Turkey,BalÄ±kesir,746574
GÃ¶lcÃ¼k,Turkey,Kocaeli,746666
Giresun,Turkey,Giresun,746881
Geyve,Turkey,Sakarya,746898
Gerede,Turkey,Bolu,746940
Gemlik,Turkey,Bursa,746958
Gelibolu,Turkey,Ã‡anakkale Province,746983
Gebze,Turkey,Kocaeli,747014
Ferizli,Turkey,Sakarya,747135
Fatsa,Turkey,Ordu,747155
Esenyurt,Turkey,Istanbul,747323
Esenler,Turkey,Istanbul,747340
EreÄŸli,Turkey,Zonguldak,747471
Erdek,Turkey,BalÄ±kesir,747482
Erbaa,Turkey,Tokat,747489
EminÃ¶nÃ¼,Turkey,Istanbul,747538
Edirne,Turkey,Edirne,747712
DÃ¼zce,Turkey,DÃ¼zce,747764
Devrek,Turkey,Zonguldak,748167
Ã‡ubuk,Turkey,Ankara,748870
Ã‡orum,Turkey,Ã‡orum,748879
Ã‡orlu,Turkey,TekirdaÄŸ,748893
Ã‡erkezkÃ¶y,Turkey,TekirdaÄŸ,749274
Ã‡erkeÅŸ,Turkey,Ã‡ankÄ±rÄ±,749279
Ã‡ayeli,Turkey,Rize,749502
Ã‡aycuma,Turkey,Zonguldak,749508
Ã‡atalca,Turkey,Istanbul,749644
Ã‡arÅŸamba,Turkey,Samsun,749704
Khanjarah,Turkey,Ã‡ankÄ±rÄ±,749748
Ã‡anakkale,Turkey,Ã‡anakkale Province,749780
Ã‡an,Turkey,Ã‡anakkale Province,749795
Bursa,Turkey,Bursa,750269
Bulancak,Turkey,Giresun,750317
Boyabat,Turkey,Sinop,750468
Bolu,Turkey,Bolu,750516
Bilecik,Turkey,Bilecik,750598
Biga,Turkey,Ã‡anakkale Province,750605
BeypazarÄ±,Turkey,Ankara,750637
BeÅŸikdÃ¼zÃ¼,Turkey,Trabzon,750735
Bayburt,Turkey,Bayburt,750938
BartÄ±n,Turkey,BartÄ±n,751057
BandÄ±rma,Turkey,BalÄ±kesir,751077
BaÄŸcÄ±lar,Turkey,Istanbul,751324
Bafra,Turkey,Samsun,751335
Babaeski,Turkey,KÄ±rklareli,751371
Artvin,Turkey,Artvin,751817
Arsin,Turkey,Trabzon,751838
Arhavi,Turkey,Artvin,751931
ArdeÅŸen,Turkey,Rize,751949
Ardahan,Turkey,Ardahan,751952
AraklÄ±,Turkey,Trabzon,751971
Amasya,Turkey,Amasya,752015
AlaplÄ±,Turkey,Zonguldak,752184
Alaca,Turkey,Ã‡orum,752278
AkyazÄ±,Turkey,Sakarya,752288
AkÃ§akoca,Turkey,DÃ¼zce,752584
AkÃ§aabat,Turkey,Trabzon,752627
AdapazarÄ±,Turkey,Sakarya,752850
Espiye,Turkey,Giresun,831432
merter keresteciler,Turkey,Istanbul,6354984
gÃ¼ngÃ¶ren merter,Turkey,Istanbul,6354985
Turgutreis,Turkey,MuÄŸla,6620290
Sarigerme,Turkey,MuÄŸla,6692524
AtaÅŸehir,Turkey,Istanbul,6947637
BaÅŸakÅŸehir,Turkey,Istanbul,6947639
BeylikdÃ¼zÃ¼,Turkey,Istanbul,6947640
BÃ¼yÃ¼kÃ§ekmece,Turkey,Istanbul,6947641
Ã‡ankaya,Turkey,Ankara,6955677
BahÃ§elievler,Turkey,Istanbul,7627067
Sultangazi,Turkey,Istanbul,7628416
Sultanbeyli,Turkey,Istanbul,7628419
Sancaktepe,Turkey,Istanbul,7628420
KarabaÄŸlar,Turkey,Ä°zmir,7701384
MuratpaÅŸa,Turkey,Antalya,8074174
Tunapuna,Trinidad and Tobago,Tunapuna/Piarco,3573576
Scarborough,Trinidad and Tobago,Tobago,3573703
Sangre Grande,Trinidad and Tobago,Sangre Grande,3573732
San Fernando,Trinidad and Tobago,City of San Fernando,3573738
Rio Claro,Trinidad and Tobago,Mayaro,3573840
Port of Spain,Trinidad and Tobago,City of Port of Spain,3573890
Point Fortin,Trinidad and Tobago,Point Fortin,3573899
Paradise,Trinidad and Tobago,Tunapuna/Piarco,3573989
Mon Repos,Trinidad and Tobago,City of San Fernando,3574116
Marabella,Trinidad and Tobago,City of San Fernando,3574194
Laventille,Trinidad and Tobago,San Juan/Laventille,3574309
Chaguanas,Trinidad and Tobago,Chaguanas,3574810
Arima,Trinidad and Tobago,Borough of Arima,3575051
Funafuti,Tuvalu,Funafuti,2110394
Douliu,Taiwan,Taiwan,1665196
Yujing,Taiwan,Taiwan,1665357
Taipei,Taiwan,Taipei,1668341
Tainan,Taiwan,Taiwan,1668355
Taichung,Taiwan,Taiwan,1668399
Daxi,Taiwan,Taiwan,1668467
Banqiao,Taiwan,Taipei,1670029
Puli,Taiwan,Taiwan,1670310
Nantou,Taiwan,Taiwan,1671566
Magong,Taiwan,Taiwan,1672228
Lugu,Taiwan,Taiwan,1672551
Kaohsiung,Taiwan,Kaohsiung,1673820
Yilan,Taiwan,Taiwan,1674199
Hualien City,Taiwan,Taiwan,1674504
Hsinchu,Taiwan,Taiwan,1675151
Hengchun,Taiwan,Taiwan,1676242
Jincheng,Taiwan,Fukien,1678008
Keelung,Taiwan,Taiwan,1678228
Taoyuan City,Taiwan,Taiwan,6696918
Taitung City,Taiwan,Taiwan,6949678
Zhongxing New Village,Taiwan,Taiwan,7601921
Zanzibar,Tanzania,Zanzibar Urban/West,148730
Wete,Tanzania,Pemba North,148842
Vwawa,Tanzania,Mbeya,148942
Vikindu,Tanzania,Pwani,148987
Uyovu,Tanzania,Geita,149027
Uvinza,Tanzania,Kigoma,149050
Ushirombo,Tanzania,Geita,149129
Usevia,Tanzania,Katavi,149132
Usagara,Tanzania,Mwanza,149151
Usa River,Tanzania,Arusha,149155
Urambo,Tanzania,Tabora,149172
Tunduma,Tanzania,Mbeya,149402
Tumbi,Tanzania,Tabora,149418
Tukuyu,Tanzania,Mbeya,149437
Tinde,Tanzania,Shinyanga,149512
Tarime,Tanzania,Mara,149581
Tanga,Tanzania,Tanga,149606
Tabora,Tanzania,Tabora,149658
Sumbawanga,Tanzania,Rukwa,149703
Songwa,Tanzania,Shinyanga,149775
Somanda,Tanzania,Simiyu,149792
Sokoni,Tanzania,Zanzibar Central/South,149812
Sirari,Tanzania,Mara,149854
Singida,Tanzania,Singida,149879
Sikonge,Tanzania,Tabora,149929
Shinyanga,Tanzania,Shinyanga,150006
Shelui,Tanzania,Singida,150037
Sepuka,Tanzania,Singida,150099
Same,Tanzania,Kilimanjaro,150276
Rulenge,Tanzania,Kagera,150436
Rujewa,Tanzania,Mbeya,150453
Puma,Tanzania,Singida,150634
Old Shinyanga,Tanzania,Shinyanga,150885
Nzega,Tanzania,Tabora,150930
Nyamuswa,Tanzania,Mara,151108
Nyalikungu,Tanzania,Simiyu,151211
Nyakabindi,Tanzania,Simiyu,151266
Nsunga,Tanzania,Kagera,151363
Nshamba,Tanzania,Kagera,151373
Njombe,Tanzania,Njombe,151479
Nguruka,Tanzania,Kigoma,151567
Ngudu,Tanzania,Mwanza,151599
Ngerengere,Tanzania,Morogoro,151678
Ngara,Tanzania,Kagera,151711
Nangwa,Tanzania,Manyara,151929
Namanyere,Tanzania,Rukwa,151986
Mwanza,Tanzania,Mwanza,152224
Mwadui,Tanzania,Shinyanga,152376
Mvomero,Tanzania,Pwani,152403
Musoma,Tanzania,Mara,152451
Muriti,Tanzania,Mara,152497
Mungaa,Tanzania,Singida,152546
Muheza,Tanzania,Tanga,152632
Mugumu,Tanzania,Mara,152663
Mtwango,Tanzania,Njombe,152718
Mto wa Mbu,Tanzania,Arusha,152743
Mtinko,Tanzania,Singida,152781
Msowero,Tanzania,Morogoro,152933
Mpwapwa,Tanzania,Dodoma,153094
Mpanda,Tanzania,Katavi,153176
Moshi,Tanzania,Kilimanjaro,153209
Morogoro,Tanzania,Morogoro,153220
Mlowo,Tanzania,Mbeya,153352
Mlimba,Tanzania,Morogoro,153384
Mlangali,Tanzania,Njombe,153408
Mlandizi,Tanzania,Pwani,153412
Mlalo,Tanzania,Tanga,153423
Mkuranga,Tanzania,Pwani,153482
Mwandiga,Tanzania,Kigoma,153709
Misungwi,Tanzania,Mwanza,153759
Mikumi,Tanzania,Morogoro,153871
Mhango,Tanzania,Shinyanga,154002
Mgandu,Tanzania,Singida,154097
Mbuguni,Tanzania,Arusha,154321
Mbeya,Tanzania,Mbeya,154380
Mazinde,Tanzania,Tanga,154470
Matui,Tanzania,Tanga,154566
Matai,Tanzania,Rukwa,154638
Maswa,Tanzania,Simiyu,154648
Masumbwe,Tanzania,Geita,154654
Maramba,Tanzania,Tanga,154780
Malinyi,Tanzania,Morogoro,155016
Malampaka,Tanzania,Simiyu,155056
Makuyuni,Tanzania,Tanga,155076
Makumbako,Tanzania,Njombe,155101
Mahanje,Tanzania,Ruvuma,155285
Kihangara,Tanzania,Mwanza,155307
Magugu,Tanzania,Manyara,155310
Magomeni,Tanzania,Dar es Salaam,155321
Magole,Tanzania,Morogoro,155334
Mafinga,Tanzania,Iringa,155405
Mabama,Tanzania,Tabora,155515
Lushoto,Tanzania,Tanga,155569
Lugoba,Tanzania,Pwani,155743
Liwale,Tanzania,Lindi,155921
Lembeni,Tanzania,Kilimanjaro,156025
Lalago,Tanzania,Simiyu,156080
Laela,Tanzania,Rukwa,156098
Kyela,Tanzania,Mbeya,156111
Kondoa,Tanzania,Dodoma,156510
Kiwira,Tanzania,Mbeya,156627
Kishapu,Tanzania,Shinyanga,156963
Kisesa,Tanzania,Simiyu,156974
Kirando,Tanzania,Rukwa,157107
Kiomboi,Tanzania,Singida,157198
Kingori,Tanzania,Arusha,157268
Kilosa,Tanzania,Morogoro,157403
Kigoma,Tanzania,Kigoma,157738
Kidodi,Tanzania,Morogoro,157826
Kidatu,Tanzania,Morogoro,157863
Kibondo,Tanzania,Kigoma,157960
Kibiti,Tanzania,Pwani,157977
Kibara,Tanzania,Mara,158016
Kibakwe,Tanzania,Dodoma,158024
Kibaha,Tanzania,Pwani,158027
Katumba,Tanzania,Mbeya,158151
Katoro,Tanzania,Geita,158160
Katerero,Tanzania,Kagera,158179
Kasulu,Tanzania,Kigoma,158214
Kasamwa,Tanzania,Geita,158289
Kiratu,Tanzania,Arusha,158324
Kamachumu,Tanzania,Kagera,158492
Kakonko,Tanzania,Kigoma,158563
Kahama,Tanzania,Shinyanga,158597
Kabanga,Tanzania,Kagera,158684
Izazi,Tanzania,Iringa,158825
Itigi,Tanzania,Singida,158904
Isaka,Tanzania,Shinyanga,159045
Iringa,Tanzania,Iringa,159071
Ipinda,Tanzania,Mbeya,159107
Ilula,Tanzania,Iringa,159179
Ilongero,Tanzania,Singida,159186
Ilembula,Tanzania,Njombe,159218
Ikungi,Tanzania,Singida,159267
Igurusi,Tanzania,Mbeya,159380
Igunga,Tanzania,Tabora,159386
Igugunu,Tanzania,Singida,159398
Ifakara,Tanzania,Morogoro,159492
Hedaru,Tanzania,Kilimanjaro,159647
Geita,Tanzania,Geita,159908
Geiro,Tanzania,Morogoro,159909
Galappo,Tanzania,Manyara,159951
Dongobesh,Tanzania,Manyara,160172
Dodoma,Tanzania,Dodoma,160196
Dar es Salaam,Tanzania,Dar es Salaam,160263
Dareda,Tanzania,Manyara,160266
Chimala,Tanzania,Mbeya,160464
Chato,Tanzania,Geita,160552
Chanika,Tanzania,Tanga,160592
Chalinze,Tanzania,Pwani,160660
Chala,Tanzania,Rukwa,160670
Chake Chake,Tanzania,Pemba South,160677
Butiama,Tanzania,Mara,160798
Buseresere,Tanzania,Geita,160833
Bungu,Tanzania,Pwani,160877
Bunda,Tanzania,Mara,160892
Bukoba,Tanzania,Kagera,160961
Bugarama,Tanzania,Kagera,161023
Biharamulo,Tanzania,Kagera,161154
Basotu,Tanzania,Manyara,161197
Bashanet,Tanzania,Manyara,161204
Bariadi,Tanzania,Simiyu,161218
Bagamoyo,Tanzania,Pwani,161290
Babati,Tanzania,Manyara,161312
Arusha,Tanzania,Arusha,161325
Tingi,Tanzania,Ruvuma,877384
Tandahimba,Tanzania,Mtwara,877391
Songea,Tanzania,Ruvuma,877401
Nyangao,Tanzania,Lindi,877471
Newala Kisimani,Tanzania,Mtwara,877532
Nanyamba,Tanzania,Mtwara,877581
Nangomba,Tanzania,Mtwara,877597
Nanganga,Tanzania,Mtwara,877605
Nachingwea,Tanzania,Lindi,877702
Mtwara,Tanzania,Mtwara,877747
Mbinga,Tanzania,Ruvuma,877998
Matiri,Tanzania,Ruvuma,878041
Masasi,Tanzania,Mtwara,878058
Maposeni,Tanzania,Ruvuma,878073
Lukuledi,Tanzania,Mtwara,878195
Luchingu,Tanzania,Mtwara,878223
Lindi,Tanzania,Lindi,878281
Kitama,Tanzania,Mtwara,878367
Kigonsera,Tanzania,Ruvuma,878400
Merelani,Tanzania,Arusha,6640202
Lebedyn,Ukraine,Sumy,613273
Druzhkivka,Ukraine,Donetsk,616743
Vasylivka,Ukraine,Zaporizhia,686729
Zvenyhorodka,Ukraine,Cherkasy,686803
Zuhres,Ukraine,Donetsk,686818
Zolotonosha,Ukraine,Cherkasy,686875
Zolochiv,Ukraine,Lviv,686896
Znomenka,Ukraine,Kirovohrad,686919
Zmiyiv,Ukraine,Kharkiv,686928
Zhytomyr,Ukraine,Zhytomyr,686967
Zhmerynka,Ukraine,Vinnyts'ka,687116
Zhovti Vody,Ukraine,Dnipropetrovsk,687196
Zhashkiv,Ukraine,Cherkasy,687245
Zdolbuniv,Ukraine,Rivne,687432
Zaporizhzhya,Ukraine,Zaporizhia,687700
Yuzhne,Ukraine,Odessa,687997
Yevpatoriya,Ukraine,Crimea,688105
Yenakiyeve,Ukraine,Donetsk,688148
Yasynuvata,Ukraine,Donetsk,688373
Yalta,Ukraine,Crimea,688533
Yahotyn,Ukraine,Kiev,688587
Vyshhorod,Ukraine,Kiev,688723
Vynohradiv,Ukraine,Zakarpattia,688746
Voznesensk,Ukraine,Mykolaiv,688860
Volnovakha,Ukraine,Donetsk,689198
Vovchansâ€™k,Ukraine,Kharkiv,689304
Volodymyr-Volynsâ€™kyy,Ukraine,Volyn,689378
Vyshneve,Ukraine,Kiev,689487
Vinnytsya,Ukraine,Vinnyts'ka,689558
Vatutine,Ukraine,Cherkasy,690312
Vasylkiv,Ukraine,Kiev,690412
Uzhhorod,Ukraine,Zakarpattia,690548
Umanâ€™,Ukraine,Cherkasy,690688
Tulâ€™chyn,Ukraine,Vinnyts'ka,691016
Tsyurupynsâ€™k,Ukraine,Kherson,691037
Truskavets,Ukraine,Lviv,691179
Torez,Ukraine,Donetsk,691374
Tokmak,Ukraine,Zaporizhia,691469
Ternopilâ€™,Ukraine,Ternopil,691650
Talâ€™ne,Ukraine,Cherkasy,691936
Syevyerodonetsâ€™k,Ukraine,Luhansk,691999
Svitlovodsâ€™k,Ukraine,Kirovohrad,692087
Sverdlovsâ€™k,Ukraine,Luhansk,692105
Svatove,Ukraine,Luhansk,692118
Svalyava,Ukraine,Zakarpattia,692129
Sumy,Ukraine,Sumy,692194
Stryi,Ukraine,Lviv,692372
Stebnyk,Ukraine,Lviv,692632
Starokostyantyniv,Ukraine,Khmelnytskyi,692818
Starobilâ€™sâ€™k,Ukraine,Luhansk,692832
Stakhanov,Ukraine,Luhansk,692975
Sokalâ€™,Ukraine,Lviv,693301
Snizhne,Ukraine,Donetsk,693381
Smila,Ukraine,Cherkasy,693457
Sloviansk,Ukraine,Donetsk,693468
Slavuta,Ukraine,Khmelnytskyi,693581
Skvyra,Ukraine,Kiev,693615
Skadovsâ€™k,Ukraine,Kherson,693709
Synelâ€™nykove,Ukraine,Dnipropetrovsk,693796
Simferopol,Ukraine,Crimea,693805
Shpola,Ukraine,Cherkasy,693920
Shostka,Ukraine,Sumy,693942
Shepetivka,Ukraine,Khmelnytskyi,694216
Shakhtarsâ€™k,Ukraine,Donetsk,694382
Sevastopol,Ukraine,Misto Sevastopolâ€™,694423
Selydove,Ukraine,Donetsk,694677
Sarny,Ukraine,Rivne,694792
Sambir,Ukraine,Lviv,694864
Saky,Ukraine,Crimea,694910
Rubizhne,Ukraine,Luhansk,695274
Rozdilâ€™na,Ukraine,Odessa,695344
Rovenâ€™ky,Ukraine,Luhansk,695379
Romny,Ukraine,Sumy,695464
Rivne,Ukraine,Rivne,695594
Reni,Ukraine,Odessa,695670
Radomyshlâ€™,Ukraine,Zhytomyr,695912
Piatykhatky,Ukraine,Dnipropetrovsk,695965
Putyvlâ€™,Ukraine,Sumy,696008
Pryluky,Ukraine,Chernihiv,696108
Popasna,Ukraine,Luhansk,696566
Poltava,Ukraine,Poltava,696643
Polonne,Ukraine,Khmelnytskyi,696660
Polohy,Ukraine,Zaporizhia,696677
Pidhorodne,Ukraine,Dnipropetrovsk,696943
Pyryatyn,Ukraine,Poltava,697183
Pervomaysâ€™k,Ukraine,Luhansk,697592
Pervomaysâ€™k,Ukraine,Mykolaiv,697593
Pereyaslav-Khmelâ€™nytsâ€™kyy,Ukraine,Kiev,697637
Perevalâ€™sâ€™k,Ukraine,Luhansk,697650
Pavlohrad,Ukraine,Dnipropetrovsk,697889
Ovruch,Ukraine,Zhytomyr,698131
Orikhiv,Ukraine,Zaporizhia,698428
Oleksandriya,Ukraine,Kirovohrad,698625
Odessa,Ukraine,Odessa,698740
Ochakiv,Ukraine,Mykolaiv,698770
Obukhiv,Ukraine,Kiev,698782
Novyy Buh,Ukraine,Mykolaiv,698953
Novovolynsâ€™k,Ukraine,Volyn,699035
Novoukrayinka,Ukraine,Kirovohrad,699078
Novomoskovsâ€™k,Ukraine,Dnipropetrovsk,699445
Novohrad-Volynsâ€™kyy,Ukraine,Zhytomyr,699553
Nova Kakhovka,Ukraine,Kherson,699839
Nosivka,Ukraine,Chernihiv,699917
Nizhyn,Ukraine,Chernihiv,699942
Nyzhnâ€™ohirsâ€™kyy,Ukraine,Crimea,700019
Nikopolâ€™,Ukraine,Dnipropetrovsk,700051
Netishyn,Ukraine,Khmelnytskyi,700261
Nadvirna,Ukraine,Ivano-Frankivsk,700507
Mykolayiv,Ukraine,Mykolaiv,700569
Mukacheve,Ukraine,Zakarpattia,700646
Molodohvardiysâ€™k,Ukraine,Luhansk,700829
Mohyliv-Podilâ€™sâ€™kyy,Ukraine,Vinnyts'ka,700918
Miskhor,Ukraine,Crimea,700997
Myrhorod,Ukraine,Poltava,701075
Merefa,Ukraine,Kharkiv,701347
Melitopolâ€™,Ukraine,Zaporizhia,701404
Mariupol,Ukraine,Donetsk,701822
Marhanetsâ€™,Ukraine,Dnipropetrovsk,701855
Malyn,Ukraine,Zhytomyr,702116
Makiyivka,Ukraine,Donetsk,702320
Lyubotyn,Ukraine,Kharkiv,702417
Lviv,Ukraine,Lviv,702550
Lutuhyne,Ukraine,Luhansk,702563
Lutsâ€™k,Ukraine,Volyn,702569
Luhansk,Ukraine,Luhansk,702658
Lubny,Ukraine,Poltava,702723
Lozova,Ukraine,Kharkiv,702760
Lysychansâ€™k,Ukraine,Luhansk,702972
Ladyzhyn,Ukraine,Vinnyts'ka,703428
Kiev,Ukraine,Kyiv City,703448
Kuznetsovsâ€™k,Ukraine,Rivne,703464
Kurakhovo,Ukraine,Donetsk,703646
Kupjansk,Ukraine,Kharkiv,703656
Kryvyi Rih,Ukraine,Dnipropetrovsk,703845
Krolevetsâ€™,Ukraine,Sumy,704000
Kreminna,Ukraine,Luhansk,704138
Kremenetsâ€™,Ukraine,Ternopil,704143
Kremenchuk,Ukraine,Poltava,704147
Krasnyy Luch,Ukraine,Luhansk,704202
Krasnyy Lyman,Ukraine,Donetsk,704204
Krasnoperekopsâ€™k,Ukraine,Crimea,704362
Krasnohrad,Ukraine,Kharkiv,704388
Krasnodon,Ukraine,Luhansk,704403
Krasnoarmiysâ€™k,Ukraine,Donetsk,704422
Krasyliv,Ukraine,Khmelnytskyi,704492
Kramatorsâ€™k,Ukraine,Donetsk,704508
Kivsharivka,Ukraine,Kharkiv,704608
Kovelâ€™,Ukraine,Volyn,704617
Kotovsâ€™k,Ukraine,Odessa,704679
Kostopilâ€™,Ukraine,Rivne,704737
Korsunâ€™-Shevchenkivsâ€™kyy,Ukraine,Cherkasy,704858
Korostyshiv,Ukraine,Zhytomyr,704885
Korostenâ€™,Ukraine,Zhytomyr,704901
Kostyantynivka,Ukraine,Donetsk,705104
Konotop,Ukraine,Sumy,705135
Komsomolâ€™sâ€™ke,Ukraine,Kharkiv,705183
Kolomyya,Ukraine,Ivano-Frankivsk,705392
Kivertsi,Ukraine,Volyn,705730
Kirovsâ€™k,Ukraine,Luhansk,705809
Kirovohrad,Ukraine,Kirovohrad,705812
Kiliya,Ukraine,Odessa,705883
Khust,Ukraine,Zakarpattia,706165
Khmelâ€™nytsâ€™kyy,Ukraine,Khmelnytskyi,706369
Khmilâ€™nyk,Ukraine,Vinnyts'ka,706380
Kherson,Ukraine,Kherson,706448
Khartsyzâ€™k,Ukraine,Donetsk,706466
Kharkiv,Ukraine,Kharkiv,706483
Kerch,Ukraine,Crimea,706524
Kozyatyn,Ukraine,Vinnyts'ka,706571
Karlivka,Ukraine,Poltava,706749
Kaniv,Ukraine,Cherkasy,706900
Kamieniec Podolski,Ukraine,Khmelnytskyi,706950
Kalush,Ukraine,Ivano-Frankivsk,707099
Kalynivka,Ukraine,Vinnyts'ka,707155
Kakhovka,Ukraine,Kherson,707244
Izyum,Ukraine,Kharkiv,707292
Izyaslav,Ukraine,Khmelnytskyi,707296
Izmayil,Ukraine,Odessa,707308
Ivano-Frankivsâ€™k,Ukraine,Ivano-Frankivsk,707471
Irpin,Ukraine,Kiev,707565
Ilovaysâ€™k,Ukraine,Donetsk,707679
Illichivsâ€™k,Ukraine,Odessa,707688
Horodok,Ukraine,Khmelnytskyi,707752
Horlivka,Ukraine,Donetsk,707753
Hlukhiv,Ukraine,Sumy,707758
Hulyaypole,Ukraine,Zaporizhia,707898
Horodok,Ukraine,Lviv,708313
Horodyshche,Ukraine,Cherkasy,708366
Hola Prystanâ€™,Ukraine,Kherson,708632
Henichesâ€™k,Ukraine,Kherson,708878
Hayvoron,Ukraine,Kirovohrad,708898
Haysyn,Ukraine,Vinnyts'ka,708901
Hadyach,Ukraine,Poltava,709054
Feodosiya,Ukraine,Crimea,709161
Fastiv,Ukraine,Kiev,709248
Energodar,Ukraine,Zaporizhia,709276
Dzhankoy,Ukraine,Crimea,709334
Dzerzhynsâ€™k,Ukraine,Donetsk,709354
Dunaivtsi,Ukraine,Khmelnytskyi,709429
Dubno,Ukraine,Rivne,709540
Drohobych,Ukraine,Lviv,709611
Donetsk,Ukraine,Donetsk,709717
Dolyna,Ukraine,Ivano-Frankivsk,709755
Dolyns'ka,Ukraine,Kirovohrad,709782
Dokuchayevsâ€™k,Ukraine,Donetsk,709835
Dobropillya,Ukraine,Donetsk,709900
Dnipropetrovsk,Ukraine,Dnipropetrovsk,709930
Dniprodzerzhynsâ€™k,Ukraine,Dnipropetrovsk,709932
Dniprorudne,Ukraine,Zaporizhia,709960
Dymytrov,Ukraine,Donetsk,710035
Derhachi,Ukraine,Kharkiv,710098
Debalâ€™tseve,Ukraine,Donetsk,710229
Chuhuyiv,Ukraine,Kharkiv,710374
Chortkiv,Ukraine,Ternopil,710400
Chervonopartyzansâ€™k,Ukraine,Luhansk,710548
Chervonohrad,Ukraine,Lviv,710554
Chernivtsi,Ukraine,Chernivtsi,710719
Chernihiv,Ukraine,Chernihiv,710735
Cherkasy,Ukraine,Cherkasy,710791
Bucha,Ukraine,Kiev,711350
Bryanka,Ukraine,Luhansk,711369
Brovary,Ukraine,Kiev,711390
Brody,Ukraine,Lviv,711416
Boyarka,Ukraine,Kiev,711515
Boryspilâ€™,Ukraine,Kiev,711660
Boryslav,Ukraine,Lviv,711669
Bolhrad,Ukraine,Odessa,711841
Bohuslav,Ukraine,Kiev,711867
Bohodukhiv,Ukraine,Kharkiv,711894
Bilhorod-Dnistrovsâ€™kyy,Ukraine,Odessa,712160
Bila Tserkva,Ukraine,Kiev,712165
Ð‘ÐµÑ€ÐµÐ¶Ð°Ð½Ð¸,Ukraine,Ternopil,712374
Berehove,Ukraine,Zakarpattia,712423
Berdychiv,Ukraine,Zhytomyr,712441
Berdyansâ€™k,Ukraine,Zaporizhia,712451
Bilopillya,Ukraine,Sumy,712559
Bilohirsâ€™k,Ukraine,Crimea,712587
Bar,Ukraine,Vinnyts'ka,712861
Balta,Ukraine,Odessa,712886
Balakliya,Ukraine,Kharkiv,712926
Balaklava,Ukraine,Misto Sevastopolâ€™,712930
Bakhmach,Ukraine,Chernihiv,712967
Bakhchysaray,Ukraine,Crimea,712969
Avdiyivka,Ukraine,Donetsk,713122
Artsyz,Ukraine,Odessa,713163
Artemivsâ€™k,Ukraine,Donetsk,713174
Armyansâ€™k,Ukraine,Crimea,713203
Apostolove,Ukraine,Dnipropetrovsk,713245
Antratsyt,Ukraine,Luhansk,713259
Amvrosiyivka,Ukraine,Donetsk,713504
Alushta,Ukraine,Crimea,713513
Alchevsâ€™k,Ukraine,Luhansk,713716
Okhtyrka,Ukraine,Sumy,713749
Komsomolsk,Ukraine,Poltava,6559559
Ð¡Ð»Ð°Ð²ÑƒÑ‚Ð¸Ñ‡,Ukraine,Kiev,6930327
Yuzhnoukrains'k,Ukraine,Mykolaiv,7525990
Novoyavorivs'k,Ukraine,Lviv,8468760
Yumbe,Uganda,Northern Region,225835
Wobulenzi,Uganda,Central Region,225858
Wakiso,Uganda,Central Region,225964
Tororo,Uganda,Eastern Region,226110
Soroti,Uganda,Eastern Region,226234
Pallisa,Uganda,Eastern Region,226823
Paidha,Uganda,Northern Region,226853
Nyachera,Uganda,Western Region,227528
Ntungamo,Uganda,Western Region,227592
Ntungamo,Uganda,Western Region,227593
Njeru,Uganda,Central Region,227812
Nebbi,Uganda,Northern Region,227904
Namasuba,Uganda,Central Region,228227
Mukono,Uganda,Central Region,228853
Mubende,Uganda,Central Region,228971
Moyo,Uganda,Northern Region,229059
Mityana,Uganda,Central Region,229139
Mbarara,Uganda,Western Region,229268
Mbale,Uganda,Eastern Region,229278
Masindi,Uganda,Western Region,229362
Masaka,Uganda,Central Region,229380
Luwero,Uganda,Central Region,229746
Lugazi,Uganda,Central Region,229911
Lira,Uganda,Northern Region,230166
Kyenjojo,Uganda,Western Region,230299
Kotido,Uganda,Northern Region,230617
Kitgum,Uganda,Northern Region,230893
Kireka,Uganda,Central Region,231139
Kayunga,Uganda,Central Region,231696
Kasese,Uganda,Western Region,232066
Kamwenge,Uganda,Western Region,232371
Kampala,Uganda,Central Region,232422
Kabale,Uganda,Western Region,233070
Jinja,Uganda,Eastern Region,233114
Iganga,Uganda,Eastern Region,233275
Hoima,Uganda,Western Region,233312
Gulu,Uganda,Northern Region,233346
Fort Portal,Uganda,Western Region,233476
Entebbe,Uganda,Central Region,233508
Bwizibwera,Uganda,Western Region,233730
Buwenge,Uganda,Eastern Region,233886
Busia,Uganda,Eastern Region,234077
Busembatia,Uganda,Eastern Region,234092
Bundibugyo,Uganda,Western Region,234178
Bugiri,Uganda,Eastern Region,234565
Arua,Uganda,Northern Region,235039
Adjumani,Uganda,Northern Region,235489
Fort Hunt,United States,Virginia,4046704
Bessemer,United States,Alabama,4048023
Paducah,United States,Kentucky,4048662
Birmingham,United States,Alabama,4049979
Center Point,United States,Alabama,4054378
Daphne,United States,Alabama,4058219
Decatur,United States,Alabama,4058553
Dothan,United States,Alabama,4059102
East Florence,United States,Alabama,4059870
Enterprise,United States,Alabama,4060791
Fairhope,United States,Alabama,4061234
Florence,United States,Alabama,4062577
Gadsden,United States,Alabama,4063619
Helena,United States,Alabama,4066811
Homewood,United States,Alabama,4067927
Hoover,United States,Alabama,4067994
Hueytown,United States,Alabama,4068446
Huntsville,United States,Alabama,4068590
Madison,United States,Alabama,4074267
Mobile,United States,Alabama,4076598
Montgomery,United States,Alabama,4076784
Mountain Brook,United States,Alabama,4078646
Northport,United States,Alabama,4080555
Opelika,United States,Alabama,4081644
Oxford,United States,Alabama,4081914
Pelham,United States,Alabama,4082569
Phenix City,United States,Alabama,4082866
Prattville,United States,Alabama,4084796
Prichard,United States,Alabama,4084888
Selma,United States,Alabama,4089114
Talladega,United States,Alabama,4092788
Tillmans Corner,United States,Alabama,4093753
Troy,United States,Alabama,4094163
Trussville,United States,Alabama,4094212
Tuscaloosa,United States,Alabama,4094455
Vestavia Hills,United States,Alabama,4095415
Bella Vista,United States,Arkansas,4101114
Benton,United States,Arkansas,4101241
Bentonville,United States,Arkansas,4101260
Blytheville,United States,Arkansas,4102412
Bryant,United States,Arkansas,4103448
Cabot,United States,Arkansas,4103957
Conway,United States,Arkansas,4106458
El Dorado,United States,Arkansas,4109785
Fayetteville,United States,Arkansas,4110486
Forrest City,United States,Arkansas,4111382
Fort Smith,United States,Arkansas,4111410
Hot Springs,United States,Arkansas,4115412
Jacksonville,United States,Arkansas,4116315
Jonesboro,United States,Arkansas,4116834
Little Rock,United States,Arkansas,4119403
Maumelle,United States,Arkansas,4120792
North Little Rock,United States,Arkansas,4124112
Paragould,United States,Arkansas,4125388
Pine Bluff,United States,Arkansas,4126226
Rogers,United States,Arkansas,4128894
Russellville,United States,Arkansas,4129397
Searcy,United States,Arkansas,4130430
Siloam Springs,United States,Arkansas,4131116
Springdale,United States,Arkansas,4132093
Texarkana,United States,Arkansas,4133367
Van Buren,United States,Arkansas,4134716
West Memphis,United States,Arkansas,4135865
"Washington, D.C.",United States,"Washington, D.C.",4140963
Bear,United States,Delaware,4141363
Dover,United States,Delaware,4142290
Middletown,United States,Delaware,4143637
Newark,United States,Delaware,4143861
Wilmington,United States,Delaware,4145381
Allapattah,United States,Florida,4145805
Altamonte Springs,United States,Florida,4145941
Apopka,United States,Florida,4146166
Aventura,United States,Florida,4146429
Bartow,United States,Florida,4146723
Bayonet Point,United States,Florida,4146901
Bayshore Gardens,United States,Florida,4146934
Belle Glade,United States,Florida,4147241
Bellview,United States,Florida,4147290
Bloomingdale,United States,Florida,4148207
Boca Del Mar,United States,Florida,4148399
Boca Raton,United States,Florida,4148411
Bonita Springs,United States,Florida,4148533
Boynton Beach,United States,Florida,4148677
Bradenton,United States,Florida,4148708
Brandon,United States,Florida,4148757
Brent,United States,Florida,4148803
Brownsville,United States,Florida,4149077
Buenaventura Lakes,United States,Florida,4149269
Cantonment,United States,Florida,4149956
Cape Coral,United States,Florida,4149962
Carol City,United States,Florida,4150066
Carrollwood,United States,Florida,4150115
Carrollwood Village,United States,Florida,4150118
Casselberry,United States,Florida,4150190
Citrus Park,United States,Florida,4151157
Clearwater,United States,Florida,4151316
Clermont,United States,Florida,4151352
Cocoa,United States,Florida,4151440
Coconut Creek,United States,Florida,4151455
Coconut Grove,United States,Florida,4151460
Cooper City,United States,Florida,4151824
Coral Gables,United States,Florida,4151871
Coral Springs,United States,Florida,4151909
Coral Terrace,United States,Florida,4151921
Country Walk,United States,Florida,4152064
Country Club,United States,Florida,4152093
Crestview,United States,Florida,4152311
Cutler,United States,Florida,4152564
Cutler Ridge,United States,Florida,4152574
Dania Beach,United States,Florida,4152772
Davie,United States,Florida,4152820
Daytona Beach,United States,Florida,4152872
DeLand,United States,Florida,4152890
DeBary,United States,Florida,4152926
Deerfield Beach,United States,Florida,4153071
Delray Beach,United States,Florida,4153132
Deltona,United States,Florida,4153146
Doral,United States,Florida,4153471
Dunedin,United States,Florida,4153759
East Lake,United States,Florida,4154008
East Pensacola Heights,United States,Florida,4154047
Edgewater,United States,Florida,4154205
Egypt Lake-Leto,United States,Florida,4154280
Ensley,United States,Florida,4154489
Estero,United States,Florida,4154568
Eustis,United States,Florida,4154606
Ferry Pass,United States,Florida,4155017
Flagami,United States,Florida,4155529
Florida Ridge,United States,Florida,4155726
Fort Lauderdale,United States,Florida,4155966
Fort Myers,United States,Florida,4155995
Fort Pierce,United States,Florida,4156018
Fort Walton Beach,United States,Florida,4156042
Fountainebleau,United States,Florida,4156091
Fruit Cove,United States,Florida,4156331
Gainesville,United States,Florida,4156404
Glenvar Heights,United States,Florida,4156857
Golden Gate,United States,Florida,4156920
Golden Glades,United States,Florida,4156931
Greenacres City,United States,Florida,4157467
Haines City,United States,Florida,4157827
Hallandale Beach,United States,Florida,4157898
Hialeah,United States,Florida,4158476
Hialeah Gardens,United States,Florida,4158482
Holiday,United States,Florida,4158865
Hollywood,United States,Florida,4158928
Homestead,United States,Florida,4159050
Immokalee,United States,Florida,4159553
Iona,United States,Florida,4159805
Ives Estates,United States,Florida,4159896
Jacksonville,United States,Florida,4160021
Jacksonville Beach,United States,Florida,4160023
Jasmine Estates,United States,Florida,4160100
Jupiter,United States,Florida,4160610
Kendale Lakes,United States,Florida,4160705
Kendall,United States,Florida,4160711
Key West,United States,Florida,4160812
Keystone,United States,Florida,4160822
Kissimmee,United States,Florida,4160983
Lake Butler,United States,Florida,4161178
Lake Magdalene,United States,Florida,4161313
Lake Worth,United States,Florida,4161422
Lake Worth Corridor,United States,Florida,4161424
Lakeland,United States,Florida,4161438
Lakeside,United States,Florida,4161461
Land O' Lakes,United States,Florida,4161534
Largo,United States,Florida,4161580
Lauderdale Lakes,United States,Florida,4161616
Lauderhill,United States,Florida,4161625
Lealman,United States,Florida,4161705
Leesburg,United States,Florida,4161771
Lehigh Acres,United States,Florida,4161785
Leisure City,United States,Florida,4161797
Lutz,United States,Florida,4163033
Lynn Haven,United States,Florida,4163049
Maitland,United States,Florida,4163220
Margate,United States,Florida,4163407
Meadow Woods,United States,Florida,4163918
Melbourne,United States,Florida,4163971
Merritt Island,United States,Florida,4164092
Miami,United States,Florida,4164138
Miami Beach,United States,Florida,4164143
Miami Gardens,United States,Florida,4164167
Miami Lakes,United States,Florida,4164186
Miramar,United States,Florida,4164601
Myrtle Grove,United States,Florida,4165519
Naples,United States,Florida,4165565
Navarre,United States,Florida,4165637
New Smyrna Beach,United States,Florida,4165913
Norland,United States,Florida,4166066
North Fort Myers,United States,Florida,4166195
North Lauderdale,United States,Florida,4166222
North Miami,United States,Florida,4166232
North Miami Beach,United States,Florida,4166233
North Port,United States,Florida,4166274
Oak Ridge,United States,Florida,4166583
Oakland Park,United States,Florida,4166638
Ocala,United States,Florida,4166673
Ocoee,United States,Florida,4166776
Ojus,United States,Florida,4166805
Opa-locka,United States,Florida,4167003
Orlando,United States,Florida,4167147
Ormond Beach,United States,Florida,4167178
Oviedo,United States,Florida,4167348
Pace,United States,Florida,4167424
Palm Bay,United States,Florida,4167499
Palm Beach Gardens,United States,Florida,4167519
Palm City,United States,Florida,4167536
Palm Coast,United States,Florida,4167538
Palm Harbor,United States,Florida,4167545
Palm Springs,United States,Florida,4167583
Palm Valley,United States,Florida,4167601
Palmetto Bay,United States,Florida,4167634
Panama City,United States,Florida,4167694
Parkland,United States,Florida,4167829
Pembroke Pines,United States,Florida,4168139
Pensacola,United States,Florida,4168228
Pine Hills,United States,Florida,4168459
Pinecrest,United States,Florida,4168590
Pinellas Park,United States,Florida,4168630
Pinewood,United States,Florida,4168659
Plant City,United States,Florida,4168773
Plantation,United States,Florida,4168782
Poinciana,United States,Florida,4168930
Pompano Beach,United States,Florida,4169014
Ponte Vedra Beach,United States,Florida,4169060
Port Charlotte,United States,Florida,4169130
Port Orange,United States,Florida,4169156
Port Saint Lucie,United States,Florida,4169171
Princeton,United States,Florida,4169345
Punta Gorda,United States,Florida,4169452
Punta Gorda Isles,United States,Florida,4169455
Richmond West,United States,Florida,4170005
Riverview,United States,Florida,4170156
Riviera Beach,United States,Florida,4170174
Rockledge,United States,Florida,4170358
Royal Palm Beach,United States,Florida,4170617
Ruskin,United States,Florida,4170688
Safety Harbor,United States,Florida,4170797
Saint Cloud,United States,Florida,4170965
Saint Petersburg,United States,Florida,4171563
San Carlos Park,United States,Florida,4171782
Sanford,United States,Florida,4172086
Sarasota,United States,Florida,4172131
Sebastian,United States,Florida,4172372
Seminole,United States,Florida,4172434
South Bradenton,United States,Florida,4173392
South Miami Heights,United States,Florida,4173497
Southchase,United States,Florida,4173600
Spring Hill,United States,Florida,4173838
Stuart,United States,Florida,4174201
Sun City Center,United States,Florida,4174317
Sunny Isles Beach,United States,Florida,4174383
Sunrise,United States,Florida,4174402
Sunset,United States,Florida,4174425
Tallahassee,United States,Florida,4174715
Tamarac,United States,Florida,4174738
Tamiami,United States,Florida,4174744
Tampa,United States,Florida,4174757
Tarpon Springs,United States,Florida,4174855
Temple Terrace,United States,Florida,4174969
The Crossings,United States,Florida,4175091
The Hammocks,United States,Florida,4175117
The Villages,United States,Florida,4175179
Three Lakes,United States,Florida,4175296
Titusville,United States,Florida,4175437
Town 'n' Country,United States,Florida,4175538
University Park,United States,Florida,4176217
Valrico,United States,Florida,4176318
Venice,United States,Florida,4176380
Vero Beach,United States,Florida,4176409
Wekiwa Springs,United States,Florida,4177671
Wellington,United States,Florida,4177703
Wesley Chapel,United States,Florida,4177727
Westchase,United States,Florida,4177779
West Little River,United States,Florida,4177865
West Melbourne,United States,Florida,4177872
West Palm Beach,United States,Florida,4177887
West Pensacola,United States,Florida,4177908
West and East Lealman,United States,Florida,4177960
Westchester,United States,Florida,4177965
Weston,United States,Florida,4178003
Winter Garden,United States,Florida,4178550
Winter Haven,United States,Florida,4178552
Winter Park,United States,Florida,4178560
Winter Springs,United States,Florida,4178573
Wright,United States,Florida,4178775
Acworth,United States,Georgia,4179074
Albany,United States,Georgia,4179320
Alpharetta,United States,Georgia,4179574
Americus,United States,Georgia,4179667
Athens,United States,Georgia,4180386
Atlanta,United States,Georgia,4180439
Augusta,United States,Georgia,4180531
Belvedere Park,United States,Georgia,4181936
Brookhaven,United States,Georgia,4184530
Brunswick,United States,Georgia,4184845
Calhoun,United States,Georgia,4185657
Canton,United States,Georgia,4186213
Carrollton,United States,Georgia,4186416
Cartersville,United States,Georgia,4186531
Columbus,United States,Georgia,4188985
Conyers,United States,Georgia,4189213
Dalton,United States,Georgia,4190581
Decatur,United States,Georgia,4191124
Douglasville,United States,Georgia,4191955
Dublin,United States,Georgia,4192205
Duluth,United States,Georgia,4192289
Dunwoody,United States,Georgia,4192375
East Point,United States,Georgia,4192674
Evans,United States,Georgia,4193699
Fayetteville,United States,Georgia,4194474
Forest Park,United States,Georgia,4195701
Gainesville,United States,Georgia,4196586
Griffin,United States,Georgia,4198322
Hinesville,United States,Georgia,4200671
Kennesaw,United States,Georgia,4203696
Kingsland,United States,Georgia,4204007
La Grange,United States,Georgia,4204230
Lawrenceville,United States,Georgia,4205196
Lithia Springs,United States,Georgia,4205885
Mableton,United States,Georgia,4207226
Macon,United States,Georgia,4207400
Marietta,United States,Georgia,4207783
Martinez,United States,Georgia,4207981
McDonough,United States,Georgia,4208442
Milledgeville,United States,Georgia,4209448
Newnan,United States,Georgia,4212684
North Decatur,United States,Georgia,4212992
North Druid Hills,United States,Georgia,4212995
Peachtree City,United States,Georgia,4215110
Pooler,United States,Georgia,4216948
Redan,United States,Georgia,4218165
Riverdale,United States,Georgia,4219001
Rome,United States,Georgia,4219762
Roswell,United States,Georgia,4219934
St. Marys,United States,Georgia,4220629
Sandy Springs,United States,Georgia,4221333
Savannah,United States,Georgia,4221552
Smyrna,United States,Georgia,4223379
Snellville,United States,Georgia,4223413
Statesboro,United States,Georgia,4224413
Stockbridge,United States,Georgia,4224681
Sugar Hill,United States,Georgia,4225039
Suwanee,United States,Georgia,4225309
Thomasville,United States,Georgia,4226348
Tifton,United States,Georgia,4226552
Tucker,United States,Georgia,4227213
Union City,United States,Georgia,4227777
Valdosta,United States,Georgia,4228147
Warner Robins,United States,Georgia,4229476
Wilmington Island,United States,Georgia,4231354
Woodstock,United States,Georgia,4231874
Alton,United States,Illinois,4232679
Belleville,United States,Illinois,4233813
Cahokia,United States,Illinois,4234969
Carbondale,United States,Illinois,4235193
Charleston,United States,Illinois,4235668
Collinsville,United States,Illinois,4236191
Decatur,United States,Illinois,4236895
East Saint Louis,United States,Illinois,4237579
Edwardsville,United States,Illinois,4237717
Fairview Heights,United States,Illinois,4238132
Godfrey,United States,Illinois,4239509
Granite City,United States,Illinois,4239714
Jacksonville,United States,Illinois,4241704
Marion,United States,Illinois,4243899
Mattoon,United States,Illinois,4244099
Mount Vernon,United States,Illinois,4245152
O'Fallon,United States,Illinois,4245926
Quincy,United States,Illinois,4247703
Springfield,United States,Illinois,4250542
Upper Alton,United States,Illinois,4251841
Bloomington,United States,Indiana,4254679
Broad Ripple,United States,Indiana,4254957
Brownsburg,United States,Indiana,4255056
Carmel,United States,Indiana,4255466
Clarksville,United States,Indiana,4255836
Columbus,United States,Indiana,4256038
Evansville,United States,Indiana,4257227
Fishers,United States,Indiana,4257494
Greenfield,United States,Indiana,4258285
Greenwood,United States,Indiana,4258313
Indianapolis,United States,Indiana,4259418
Jasper,United States,Indiana,4259640
Jeffersonville,United States,Indiana,4259671
Lawrence,United States,Indiana,4260210
New Albany,United States,Indiana,4262045
New Castle,United States,Indiana,4262072
Plainfield,United States,Indiana,4263108
Richmond,United States,Indiana,4263681
Seymour,United States,Indiana,4264617
Shelbyville,United States,Indiana,4264688
Terre Haute,United States,Indiana,4265737
Vincennes,United States,Indiana,4266307
Derby,United States,Kansas,4270356
Emporia,United States,Kansas,4271086
Gardner,United States,Kansas,4271935
Great Bend,United States,Kansas,4272340
Hays,United States,Kansas,4272782
Hutchinson,United States,Kansas,4273299
Junction City,United States,Kansas,4273680
Kansas City,United States,Kansas,4273837
Lawrence,United States,Kansas,4274277
Leavenworth,United States,Kansas,4274305
Leawood,United States,Kansas,4274317
Lenexa,United States,Kansas,4274356
Manhattan,United States,Kansas,4274994
Newton,United States,Kansas,4276248
Olathe,United States,Kansas,4276614
Overland Park,United States,Kansas,4276873
Pittsburg,United States,Kansas,4277241
Prairie Village,United States,Kansas,4277718
Salina,United States,Kansas,4278890
Shawnee,United States,Kansas,4279247
Topeka,United States,Kansas,4280539
Wichita,United States,Kansas,4281730
Ashland,United States,Kentucky,4282757
Bowling Green,United States,Kentucky,4285268
Burlington,United States,Kentucky,4286281
Covington,United States,Kentucky,4288809
Danville,United States,Kentucky,4289445
Elizabethtown,United States,Kentucky,4290988
Erlanger,United States,Kentucky,4291255
Fern Creek,United States,Kentucky,4291620
Florence,United States,Kentucky,4291945
Fort Thomas,United States,Kentucky,4292071
Frankfort,United States,Kentucky,4292188
Georgetown,United States,Kentucky,4292686
Henderson,United States,Kentucky,4294494
Highview,United States,Kentucky,4294799
Hopkinsville,United States,Kentucky,4295251
Independence,United States,Kentucky,4295776
Ironville,United States,Kentucky,4295940
Jeffersontown,United States,Kentucky,4296218
Lexington,United States,Kentucky,4297983
Lexington-Fayette,United States,Kentucky,4297999
Louisville,United States,Kentucky,4299276
Madisonville,United States,Kentucky,4299670
Meads,United States,Kentucky,4300488
Murray,United States,Kentucky,4302035
Newburg,United States,Kentucky,4302504
Newport,United States,Kentucky,4302529
Nicholasville,United States,Kentucky,4302561
Okolona,United States,Kentucky,4303012
Owensboro,United States,Kentucky,4303436
Pleasure Ridge Park,United States,Kentucky,4304713
Radcliff,United States,Kentucky,4305504
Richmond,United States,Kentucky,4305974
Saint Matthews,United States,Kentucky,4307238
Shively,United States,Kentucky,4308225
Valley Station,United States,Kentucky,4311963
Winchester,United States,Kentucky,4313697
Alexandria,United States,Louisiana,4314550
Baton Rouge,United States,Louisiana,4315588
Bayou Cane,United States,Louisiana,4315768
Bossier City,United States,Louisiana,4317639
Central,United States,Louisiana,4319435
Chalmette,United States,Louisiana,4319518
Estelle,United States,Louisiana,4323873
Gretna,United States,Louisiana,4326575
Hammond,United States,Louisiana,4326868
Harvey,United States,Louisiana,4327047
Houma,United States,Louisiana,4328010
Kenner,United States,Louisiana,4329753
Lafayette,United States,Louisiana,4330145
Lake Charles,United States,Louisiana,4330236
Laplace,United States,Louisiana,4330525
Marrero,United States,Louisiana,4332628
Metairie,United States,Louisiana,4333177
Metairie Terrace,United States,Louisiana,4333190
Monroe,United States,Louisiana,4333669
Natchitoches,United States,Louisiana,4334720
New Iberia,United States,Louisiana,4334971
New Orleans,United States,Louisiana,4335045
Opelousas,United States,Louisiana,4336153
Prairieville,United States,Louisiana,4338012
Ruston,United States,Louisiana,4339348
Shenandoah,United States,Louisiana,4341378
Shreveport,United States,Louisiana,4341513
Slidell,United States,Louisiana,4341727
Sulphur,United States,Louisiana,4342816
Terrytown,United States,Louisiana,4343327
Adelphi,United States,Maryland,4346991
Annapolis,United States,Maryland,4347242
Arbutus,United States,Maryland,4347371
Arnold,United States,Maryland,4347426
Aspen Hill,United States,Maryland,4347553
Baltimore,United States,Maryland,4347778
Ballenger Creek,United States,Maryland,4347839
Beltsville,United States,Maryland,4348353
Bethesda,United States,Maryland,4348599
Bowie,United States,Maryland,4349159
Calverton,United States,Maryland,4350160
Camp Springs,United States,Maryland,4350288
Carney,United States,Maryland,4350413
Catonsville,United States,Maryland,4350635
Chillum,United States,Maryland,4351383
Cloverly,United States,Maryland,4351851
Clinton,United States,Maryland,4351871
Cockeysville,United States,Maryland,4351887
College Park,United States,Maryland,4351977
Columbia,United States,Maryland,4352053
Crofton,United States,Maryland,4352539
Cumberland,United States,Maryland,4352681
Damascus,United States,Maryland,4352728
Dundalk,United States,Maryland,4353765
East Riverdale,United States,Maryland,4353925
Easton,United States,Maryland,4353962
Edgewood,United States,Maryland,4354087
Eldersburg,United States,Maryland,4354163
Elkton,United States,Maryland,4354234
Elkridge,United States,Maryland,4354256
Ellicott City,United States,Maryland,4354265
Essex,United States,Maryland,4354428
Fairland,United States,Maryland,4354573
Ferndale,United States,Maryland,4354821
Fort Washington,United States,Maryland,4355355
Frederick,United States,Maryland,4355585
Gaithersburg,United States,Maryland,4355843
Germantown,United States,Maryland,4356050
Glassmanor,United States,Maryland,4356165
Glen Burnie,United States,Maryland,4356188
Green Haven,United States,Maryland,4356783
Greenbelt,United States,Maryland,4356847
Hagerstown,United States,Maryland,4357141
Hanover,United States,Maryland,4357340
Hillcrest Heights,United States,Maryland,4358082
Hunt Valley,United States,Maryland,4358701
Hyattsville,United States,Maryland,4358821
Ilchester,United States,Maryland,4358864
Lake Shore,United States,Maryland,4360201
Landover,United States,Maryland,4360287
Langley Park,United States,Maryland,4360314
Laurel,United States,Maryland,4360369
Lochearn,United States,Maryland,4360954
Maryland City,United States,Maryland,4361831
Middle River,United States,Maryland,4362344
Milford Mill,United States,Maryland,4362438
Montgomery Village,United States,Maryland,4362743
North Bel Air,United States,Maryland,4363836
North Bethesda,United States,Maryland,4363843
North Potomac,United States,Maryland,4363990
Odenton,United States,Maryland,4364362
Olney,United States,Maryland,4364537
Owings Mills,United States,Maryland,4364727
Oxon Hill,United States,Maryland,4364759
Parkville,United States,Maryland,4364946
Parole,United States,Maryland,4364964
Pasadena,United States,Maryland,4364990
Perry Hall,United States,Maryland,4365227
Pikesville,United States,Maryland,4365387
Potomac,United States,Maryland,4366001
Randallstown,United States,Maryland,4366476
Redland,United States,Maryland,4366593
Reisterstown,United States,Maryland,4366647
Rockville,United States,Maryland,4367175
Rosedale,United States,Maryland,4367372
Rossville,United States,Maryland,4367419
Saint Charles,United States,Maryland,4367734
Salisbury,United States,Maryland,4368711
Seabrook,United States,Maryland,4369076
Severn,United States,Maryland,4369190
Severna Park,United States,Maryland,4369224
Silver Spring,United States,Maryland,4369596
South Bel Air,United States,Maryland,4369928
South Gate,United States,Maryland,4369964
South Laurel,United States,Maryland,4369978
Suitland,United States,Maryland,4370616
Takoma Park,United States,Maryland,4370890
Towson,United States,Maryland,4371582
Waldorf,United States,Maryland,4372599
West Elkridge,United States,Maryland,4373104
Westminster,United States,Maryland,4373238
Wheaton,United States,Maryland,4373349
White Oak,United States,Maryland,4373449
Woodlawn,United States,Maryland,4374054
Affton,United States,Missouri,4374513
Arnold,United States,Missouri,4375087
Ballwin,United States,Missouri,4375663
Belton,United States,Missouri,4376482
Blue Springs,United States,Missouri,4377664
Cape Girardeau,United States,Missouri,4379966
Chesterfield,United States,Missouri,4381072
Clayton,United States,Missouri,4381478
Columbia,United States,Missouri,4381982
Concord,United States,Missouri,4382072
Creve Coeur,United States,Missouri,4382837
East Independence,United States,Missouri,4385018
Farmington,United States,Missouri,4386289
Ferguson,United States,Missouri,4386387
Florissant,United States,Missouri,4386802
Gladstone,United States,Missouri,4387990
Grandview,United States,Missouri,4388460
Hannibal,United States,Missouri,4389418
Hazelwood,United States,Missouri,4389967
Independence,United States,Missouri,4391812
Jefferson City,United States,Missouri,4392388
Joplin,United States,Missouri,4392768
Kansas City,United States,Missouri,4393217
Kirkwood,United States,Missouri,4393739
Lee's Summit,United States,Missouri,4394870
Lemay,United States,Missouri,4394905
Liberty,United States,Missouri,4395052
Manchester,United States,Missouri,4396915
Maryland Heights,United States,Missouri,4397340
Mehlville,United States,Missouri,4397962
Nixa,United States,Missouri,4400648
O'Fallon,United States,Missouri,4401242
Oakville,United States,Missouri,4401618
Overland,United States,Missouri,4402178
Ozark,United States,Missouri,4402245
Poplar Bluff,United States,Missouri,4404233
Raymore,United States,Missouri,4405180
Raytown,United States,Missouri,4405188
Rolla,United States,Missouri,4406282
Saint Charles,United States,Missouri,4406831
Saint Joseph,United States,Missouri,4407010
St. Louis,United States,Missouri,4407066
Saint Peters,United States,Missouri,4407237
Sedalia,United States,Missouri,4408000
Sikeston,United States,Missouri,4408672
Spanish Lake,United States,Missouri,4409591
Springfield,United States,Missouri,4409896
University City,United States,Missouri,4412697
Warrensburg,United States,Missouri,4413595
Webster Groves,United States,Missouri,4413872
Wentzville,United States,Missouri,4414001
Wildwood,United States,Missouri,4414749
Biloxi,United States,Mississippi,4418478
Brandon,United States,Mississippi,4419290
Clarksdale,United States,Mississippi,4421935
Clinton,United States,Mississippi,4422133
Columbus,United States,Mississippi,4422442
Gautier,United States,Mississippi,4427569
Greenville,United States,Mississippi,4428475
Greenwood,United States,Mississippi,4428495
Gulfport,United States,Mississippi,4428667
Hattiesburg,United States,Mississippi,4429295
Horn Lake,United States,Mississippi,4430400
Jackson,United States,Mississippi,4431410
Laurel,United States,Mississippi,4433039
Madison,United States,Mississippi,4434663
Meridian,United States,Mississippi,4435764
Natchez,United States,Mississippi,4437982
Ocean Springs,United States,Mississippi,4439506
Olive Branch,United States,Mississippi,4439869
Oxford,United States,Mississippi,4440076
Pascagoula,United States,Mississippi,4440397
Pearl,United States,Mississippi,4440559
Ridgeland,United States,Mississippi,4443296
Southaven,United States,Mississippi,4446675
Starkville,United States,Mississippi,4447161
Tupelo,United States,Mississippi,4448903
Vicksburg,United States,Mississippi,4449620
West Gulfport,United States,Mississippi,4450687
Albemarle,United States,North Carolina,4452303
Apex,United States,North Carolina,4452808
Asheboro,United States,North Carolina,4453035
Asheville,United States,North Carolina,4453066
Boone,United States,North Carolina,4456703
Burlington,United States,North Carolina,4458228
Carrboro,United States,North Carolina,4459343
Cary,United States,North Carolina,4459467
Chapel Hill,United States,North Carolina,4460162
Charlotte,United States,North Carolina,4460243
Clayton,United States,North Carolina,4460943
Clemmons,United States,North Carolina,4461015
Concord,United States,North Carolina,4461574
Cornelius,United States,North Carolina,4461941
Durham,United States,North Carolina,4464368
Eden,United States,North Carolina,4464873
Elizabeth City,United States,North Carolina,4465088
Fayetteville,United States,North Carolina,4466033
Fuquay-Varina,United States,North Carolina,4467485
Garner,United States,North Carolina,4467657
Gastonia,United States,North Carolina,4467732
Goldsboro,United States,North Carolina,4468261
Greensboro,United States,North Carolina,4469146
Greenville,United States,North Carolina,4469160
Havelock,United States,North Carolina,4470244
Henderson,United States,North Carolina,4470566
Hickory,United States,North Carolina,4470778
High Point,United States,North Carolina,4471025
Holly Springs,United States,North Carolina,4471641
Hope Mills,United States,North Carolina,4471851
Huntersville,United States,North Carolina,4472370
Indian Trail,United States,North Carolina,4472687
Jacksonville,United States,North Carolina,4473083
Kannapolis,United States,North Carolina,4474040
Kernersville,United States,North Carolina,4474221
Kinston,United States,North Carolina,4474436
Laurinburg,United States,North Carolina,4475347
Lenoir,United States,North Carolina,4475640
Lexington,United States,North Carolina,4475773
Lumberton,United States,North Carolina,4477525
Matthews,United States,North Carolina,4478334
Mint Hill,United States,North Carolina,4479759
Monroe,United States,North Carolina,4479946
Mooresville,United States,North Carolina,4480125
Morganton,United States,North Carolina,4480219
Morrisville,United States,North Carolina,4480285
New Bern,United States,North Carolina,4481682
Raleigh,United States,North Carolina,4487042
Roanoke Rapids,United States,North Carolina,4488232
Rocky Mount,United States,North Carolina,4488762
Salisbury,United States,North Carolina,4489985
Sanford,United States,North Carolina,4490329
Shelby,United States,North Carolina,4491180
Statesville,United States,North Carolina,4493316
Thomasville,United States,North Carolina,4494942
Wake Forest,United States,North Carolina,4497290
West Raleigh,United States,North Carolina,4498303
Wilmington,United States,North Carolina,4499379
Wilson,United States,North Carolina,4499389
Winston-Salem,United States,North Carolina,4499612
Atlantic City,United States,New Jersey,4500546
Bridgeton,United States,New Jersey,4500942
Camden,United States,New Jersey,4501018
Cherry Hill,United States,New Jersey,4501198
Glassboro,United States,New Jersey,4501931
Jackson,United States,New Jersey,4502434
Lindenwold,United States,New Jersey,4502687
Maple Shade,United States,New Jersey,4502901
Millville,United States,New Jersey,4503078
Mount Laurel,United States,New Jersey,4503136
Ocean Acres,United States,New Jersey,4503346
Pennsauken,United States,New Jersey,4503548
Pleasantville,United States,New Jersey,4503646
Sicklerville,United States,New Jersey,4504118
South Vineland,United States,New Jersey,4504225
Toms River,United States,New Jersey,4504476
Vineland,United States,New Jersey,4504621
Williamstown,United States,New Jersey,4504871
Athens,United States,Ohio,4505542
Beavercreek,United States,Ohio,4506008
Centerville,United States,Ohio,4508204
Cincinnati,United States,Ohio,4508722
Columbus,United States,Ohio,4509177
Dayton,United States,Ohio,4509884
Fairborn,United States,Ohio,4511263
Fairfield,United States,Ohio,4511283
Forest Park,United States,Ohio,4512060
Grove City,United States,Ohio,4513409
Hamilton,United States,Ohio,4513575
Huber Heights,United States,Ohio,4514746
Kettering,United States,Ohio,4515843
Lancaster,United States,Ohio,4516233
Lebanon,United States,Ohio,4516412
Mason,United States,Ohio,4517698
Miamisburg,United States,Ohio,4518188
Middletown,United States,Ohio,4518264
Norwood,United States,Ohio,4519995
Oxford,United States,Ohio,4520760
Pickerington,United States,Ohio,4521209
Portsmouth,United States,Ohio,4521816
Reynoldsburg,United States,Ohio,4522411
Riverside,United States,Ohio,4522586
Springboro,United States,Ohio,4525304
Springfield,United States,Ohio,4525353
Trotwood,United States,Ohio,4526576
Upper Arlington,United States,Ohio,4526993
Vandalia,United States,Ohio,4527124
White Oak,United States,Ohio,4528259
Whitehall,United States,Ohio,4528291
Xenia,United States,Ohio,4528810
Zanesville,United States,Ohio,4528923
Ada,United States,Oklahoma,4529096
Altus,United States,Oklahoma,4529292
Ardmore,United States,Oklahoma,4529469
Bartlesville,United States,Oklahoma,4529987
Bethany,United States,Oklahoma,4530372
Bixby,United States,Oklahoma,4530801
Broken Arrow,United States,Oklahoma,4531405
Chickasha,United States,Oklahoma,4533029
Claremore,United States,Oklahoma,4533580
Del City,United States,Oklahoma,4534934
Duncan,United States,Oklahoma,4535389
Durant,United States,Oklahoma,4535414
Edmond,United States,Oklahoma,4535740
El Reno,United States,Oklahoma,4535783
Enid,United States,Oklahoma,4535961
Jenks,United States,Oklahoma,4539615
Lawton,United States,Oklahoma,4540737
McAlester,United States,Oklahoma,4542367
Midwest City,United States,Oklahoma,4542765
Moore,United States,Oklahoma,4542975
Muskogee,United States,Oklahoma,4543338
Mustang,United States,Oklahoma,4543352
Norman,United States,Oklahoma,4543762
Oklahoma City,United States,Oklahoma,4544349
Owasso,United States,Oklahoma,4547407
Ponca City,United States,Oklahoma,4548267
Sand Springs,United States,Oklahoma,4550659
Sapulpa,United States,Oklahoma,4550881
Shawnee,United States,Oklahoma,4551177
Stillwater,United States,Oklahoma,4552215
Tahlequah,United States,Oklahoma,4552707
Tulsa,United States,Oklahoma,4553433
Yukon,United States,Oklahoma,4556165
Chambersburg,United States,Pennsylvania,4557109
Chester,United States,Pennsylvania,4557137
Drexel Hill,United States,Pennsylvania,4557606
Hanover,United States,Pennsylvania,4558475
Philadelphia,United States,Pennsylvania,4560349
Springfield,United States,Pennsylvania,4561407
West Chester,United States,Pennsylvania,4562144
York,United States,Pennsylvania,4562407
Aiken,United States,South Carolina,4569067
Anderson,United States,South Carolina,4569298
Charleston,United States,South Carolina,4574324
Columbia,United States,South Carolina,4575352
Conway,United States,South Carolina,4575461
Easley,United States,South Carolina,4577263
Florence,United States,South Carolina,4578737
Goose Creek,United States,South Carolina,4580098
Greenville,United States,South Carolina,4580543
Greenwood,United States,South Carolina,4580569
Greer,United States,South Carolina,4580599
Hanahan,United States,South Carolina,4581023
Hilton Head Island,United States,South Carolina,4581833
Lexington,United States,South Carolina,4585000
Mauldin,United States,South Carolina,4586523
Mount Pleasant,United States,South Carolina,4588165
Myrtle Beach,United States,South Carolina,4588718
North Augusta,United States,South Carolina,4589368
North Charleston,United States,South Carolina,4589387
Rock Hill,United States,South Carolina,4593142
Saint Andrews,United States,South Carolina,4593724
Seven Oaks,United States,South Carolina,4595374
Simpsonville,United States,South Carolina,4595864
Socastee,United States,South Carolina,4596208
Spartanburg,United States,South Carolina,4597200
Summerville,United States,South Carolina,4597919
Sumter,United States,South Carolina,4597948
Taylors,United States,South Carolina,4598353
Wade Hampton,United States,South Carolina,4599937
Bartlett,United States,Tennessee,4604183
Brentwood,United States,Tennessee,4608408
Brentwood Estates,United States,Tennessee,4608418
Bristol,United States,Tennessee,4608657
Chattanooga,United States,Tennessee,4612862
Clarksville,United States,Tennessee,4613868
Cleveland,United States,Tennessee,4614088
Collierville,United States,Tennessee,4614748
Columbia,United States,Tennessee,4614867
Cookeville,United States,Tennessee,4615145
Dyersburg,United States,Tennessee,4619800
East Brainerd,United States,Tennessee,4619943
East Chattanooga,United States,Tennessee,4619947
East Ridge,United States,Tennessee,4620131
Farragut,United States,Tennessee,4621846
Franklin,United States,Tennessee,4623560
Gallatin,United States,Tennessee,4624180
Germantown,United States,Tennessee,4624601
Goodlettsville,United States,Tennessee,4625282
Greeneville,United States,Tennessee,4626334
Hendersonville,United States,Tennessee,4628735
Jackson,United States,Tennessee,4632595
Johnson City,United States,Tennessee,4633419
Kingsport,United States,Tennessee,4634662
Knoxville,United States,Tennessee,4634946
La Vergne,United States,Tennessee,4635031
Lebanon,United States,Tennessee,4636045
Maryville,United States,Tennessee,4639848
Memphis,United States,Tennessee,4641239
Morristown,United States,Tennessee,4642938
Mount Juliet,United States,Tennessee,4643336
Murfreesboro,United States,Tennessee,4644312
Nashville,United States,Tennessee,4644585
New South Memphis,United States,Tennessee,4645421
Oak Ridge,United States,Tennessee,4646571
Shelbyville,United States,Tennessee,4657077
Smyrna,United States,Tennessee,4658590
Spring Hill,United States,Tennessee,4659446
Springfield,United States,Tennessee,4659557
Tullahoma,United States,Tennessee,4663494
Abilene,United States,Texas,4669635
Alamo,United States,Texas,4670074
Aldine,United States,Texas,4670146
Alice,United States,Texas,4670234
Allen,United States,Texas,4670300
Alvin,United States,Texas,4670592
Angleton,United States,Texas,4670866
Arlington,United States,Texas,4671240
Atascocita,United States,Texas,4671524
Austin,United States,Texas,4671654
Balch Springs,United States,Texas,4672059
Baytown,United States,Texas,4672731
Beaumont,United States,Texas,4672989
Bedford,United States,Texas,4673094
Bellaire,United States,Texas,4673353
Belton,United States,Texas,4673425
Benbrook,United States,Texas,4673482
Brenham,United States,Texas,4676206
Brownsville,United States,Texas,4676740
Brownwood,United States,Texas,4676798
Brushy Creek,United States,Texas,4676920
Bryan,United States,Texas,4677008
Burleson,United States,Texas,4677551
Canyon Lake,United States,Texas,4678901
Carrollton,United States,Texas,4679195
Cedar Hill,United States,Texas,4679803
Cedar Park,United States,Texas,4679867
Channelview,United States,Texas,4680388
Cibolo,United States,Texas,4681462
Cinco Ranch,United States,Texas,4681485
Cleburne,United States,Texas,4681976
Cloverleaf,United States,Texas,4682127
College Station,United States,Texas,4682464
Colleyville,United States,Texas,4682478
Conroe,United States,Texas,4682991
Converse,United States,Texas,4683021
Coppell,United States,Texas,4683217
Copperas Cove,United States,Texas,4683244
Corinth,United States,Texas,4683317
Corpus Christi,United States,Texas,4683416
Corsicana,United States,Texas,4683462
Cypress,United States,Texas,4684724
Dallas,United States,Texas,4684888
DeSoto,United States,Texas,4685524
Deer Park,United States,Texas,4685737
Denison,United States,Texas,4685892
Denton,United States,Texas,4685907
Dickinson,United States,Texas,4686163
Donna,United States,Texas,4686593
Duncanville,United States,Texas,4687331
Edinburg,United States,Texas,4688275
Ennis,United States,Texas,4689311
Euless,United States,Texas,4689550
Farmers Branch,United States,Texas,4690198
Flower Mound,United States,Texas,4691585
Fort Worth,United States,Texas,4691930
Fresno,United States,Texas,4692400
Friendswood,United States,Texas,4692521
Frisco,United States,Texas,4692559
Gainesville,United States,Texas,4692746
Galveston,United States,Texas,4692883
Garland,United States,Texas,4693003
Gatesville,United States,Texas,4693150
Georgetown,United States,Texas,4693342
Grand Prairie,United States,Texas,4694482
Grapevine,United States,Texas,4694568
Greenville,United States,Texas,4695066
Groves,United States,Texas,4695317
Haltom City,United States,Texas,4695912
Harker Heights,United States,Texas,4696202
Harlingen,United States,Texas,4696233
Highland Village,United States,Texas,4697645
Houston,United States,Texas,4699066
Humble,United States,Texas,4699442
Huntsville,United States,Texas,4699540
Hurst,United States,Texas,4699575
Irving,United States,Connecticut,4700168
West Hartford,United States,Connecticut,4845411
West Haven,United States,Connecticut,4845419
West Torrington,United States,Connecticut,4845519
Westport,United States,Connecticut,4845585
Wethersfield,United States,Connecticut,4845612
Willimantic,United States,Connecticut,4845823
Wilton,United States,Connecticut,4845871
Windham,United States,Connecticut,4845898
Windsor,United States,Connecticut,4845920
Wolcott,United States,Connecticut,4845984
Ames,United States,Iowa,4846834
Ankeny,United States,Iowa,4846960
Bettendorf,United States,Iowa,4848489
Burlington,United States,Iowa,4849826
Cedar Falls,United States,Iowa,4850699
Cedar Rapids,United States,Iowa,4850751
Clinton,United States,Iowa,4852022
Clive,United States,Iowa,4852065
Coralville,United States,Iowa,4852640
Council Bluffs,United States,Iowa,4852832
Davenport,United States,Iowa,4853423
Des Moines,United States,Iowa,4853828
Dubuque,United States,Iowa,4854529
Fort Dodge,United States,Iowa,4857486
Iowa City,United States,Iowa,4862034
Johnston,United States,Iowa,4862760
Marion,United States,Iowa,4866263
Marshalltown,United States,Iowa,4866371
Mason City,United States,Iowa,4866445
Muscatine,United States,Iowa,4868404
Newton,United States,Iowa,4868907
Ottumwa,United States,Iowa,4870380
Sioux City,United States,Iowa,4876523
Urbandale,United States,Iowa,4879890
Waterloo,United States,Iowa,4880889
West Des Moines,United States,Iowa,4881346
Addison,United States,Illinois,4882920
Algonquin,United States,Illinois,4883078
Alsip,United States,Illinois,4883207
Arlington Heights,United States,Illinois,4883555
Aurora,United States,Illinois,4883817
Bartlett,United States,Illinois,4884141
Batavia,United States,Illinois,4884192
Bellwood,United States,Illinois,4884434
Belvidere,United States,Illinois,4884453
Bensenville,United States,Illinois,4884509
Berwyn,United States,Illinois,4884597
Bloomingdale,United States,Illinois,4885156
Bloomington,United States,Illinois,4885164
Blue Island,United States,Illinois,4885186
Bolingbrook,United States,Illinois,4885265
Bourbonnais,United States,Illinois,4885342
Bradley,United States,Illinois,4885418
Bridgeview,United States,Illinois,4885573
Brookfield,United States,Illinois,4885689
Buffalo Grove,United States,Illinois,4885955
Burbank,United States,Illinois,4885983
Calumet City,United States,Illinois,4886255
Carol Stream,United States,Illinois,4886662
Carpentersville,United States,Illinois,4886676
Cary,United States,Illinois,4886738
Champaign,United States,Illinois,4887158
Chicago,United States,Illinois,4887398
Chicago Heights,United States,Illinois,4887442
Cicero,United States,Illinois,4888015
Country Club Hills,United States,Illinois,4888892
Crest Hill,United States,Illinois,4889107
Crystal Lake,United States,Illinois,4889229
Danville,United States,Illinois,4889426
Darien,United States,Illinois,4889447
DeKalb,United States,Illinois,4889553
Deerfield,United States,Illinois,4889668
Des Plaines,United States,Illinois,4889772
Dixon,United States,Illinois,4889959
Dolton,United States,Illinois,4890009
Downers Grove,United States,Illinois,4890119
East Moline,United States,Illinois,4890536
East Peoria,United States,Illinois,4890549
Elgin,United States,Illinois,4890864
Elk Grove Village,United States,Illinois,4890925
Elmhurst,United States,Illinois,4891010
Elmwood Park,United States,Illinois,4891051
Evanston,United States,Illinois,4891382
Evergreen Park,United States,Illinois,4891431
Frankfort,United States,Illinois,4893037
Franklin Park,United States,Illinois,4893070
Freeport,United States,Illinois,4893171
Galesburg,United States,Illinois,4893392
Geneva,United States,Illinois,4893591
Glen Ellyn,United States,Illinois,4893811
Glenview,United States,Illinois,4893886
Goodings Grove,United States,Illinois,4894061
Grayslake,United States,Illinois,4894465
Gurnee,United States,Illinois,4894861
Hanover Park,United States,Illinois,4895066
Harvey,United States,Illinois,4895298
Highland Park,United States,Illinois,4895876
Hinsdale,United States,Illinois,4896012
Hoffman Estates,United States,Illinois,4896075
Homer Glen,United States,Illinois,4896336
Homewood,United States,Illinois,4896353
Huntley,United States,Illinois,4896691
Joliet,United States,Illinois,4898015
Kankakee,United States,Illinois,4898182
La Grange,United States,Illinois,4898846
Lake Forest,United States,Illinois,4899012
Lake Zurich,United States,Illinois,4899170
Lake in the Hills,United States,Illinois,4899184
Lansing,United States,Illinois,4899340
Lemont,United States,Illinois,4899581
Libertyville,United States,Illinois,4899739
Lisle,United States,Illinois,4900080
Lockport,United States,Illinois,4900292
Lombard,United States,Illinois,4900373
Loves Park,United States,Illinois,4900579
Machesney Park,United States,Illinois,4900801
Macomb,United States,Illinois,4900817
Matteson,United States,Illinois,4901445
Maywood,United States,Illinois,4901514
McHenry,United States,Illinois,4901663
Melrose Park,United States,Illinois,4901868
Mokena,United States,Illinois,4902475
Moline,United States,Illinois,4902476
Montgomery,United States,Illinois,4902559
Morton,United States,Illinois,4902754
Morton Grove,United States,Illinois,4902763
Mount Prospect,United States,Illinois,4903024
Mundelein,United States,Illinois,4903184
Naperville,United States,Illinois,4903279
New Lenox,United States,Illinois,4903535
Niles,United States,Illinois,4903730
Normal,United States,Illinois,4903780
North Aurora,United States,Illinois,4903818
North Chicago,United States,Illinois,4903862
North Peoria,United States,Illinois,4903976
Northbrook,United States,Illinois,4904056
Oak Forest,United States,Illinois,4904286
Oak Lawn,United States,Illinois,4904365
Oak Park,United States,Illinois,4904381
Orland Park,United States,Illinois,4904937
Oswego,United States,Illinois,4904996
Ottawa,United States,Illinois,4905006
Palatine,United States,Illinois,4905211
Palos Hills,United States,Illinois,4905263
Park Forest,United States,Illinois,4905337
Park Ridge,United States,Illinois,4905367
Pekin,United States,Illinois,4905599
Peoria,United States,Illinois,4905687
Plainfield,United States,Illinois,4906125
Prospect Heights,United States,Illinois,4906882
Rock Island,United States,Illinois,4907907
Rockford,United States,Illinois,4907959
Rolling Meadows,United States,Illinois,4908052
Romeoville,United States,Illinois,4908068
Roselle,United States,Illinois,4908173
Round Lake,United States,Illinois,4908236
Round Lake Beach,United States,Illinois,4908237
Saint Charles,United States,Illinois,4908737
Schaumburg,United States,Illinois,4910713
Shorewood,United States,Illinois,4911418
Skokie,United States,Illinois,4911600
South Elgin,United States,Illinois,4911893
South Holland,United States,Illinois,4911934
Sterling,United States,Illinois,4912499
Streamwood,United States,Illinois,4912691
Sycamore,United States,Illinois,4913110
Tinley Park,United States,Illinois,4913723
Urbana,United States,Illinois,4914570
Vernon Hills,United States,Illinois,4914738
Villa Park,United States,Illinois,4914830
Wasco,United States,Illinois,4915539
Washington,United States,Illinois,4915545
Waukegan,United States,Illinois,4915734
West Chicago,United States,Illinois,4915963
Westchester,United States,Illinois,4916140
Westmont,United States,Illinois,4916207
Wheaton,United States,Illinois,4916288
Wheeling,United States,Illinois,4916311
Wilmette,United States,Illinois,4916732
Woodridge,United States,Illinois,4917089
Woodstock,United States,Illinois,4917123
Yorkville,United States,Illinois,4917298
Zion,United States,Illinois,4917358
Anderson,United States,Indiana,4917592
Crawfordsville,United States,Indiana,4919381
Crown Point,United States,Indiana,4919451
Dyer,United States,Indiana,4919820
East Chicago,United States,Indiana,4919857
Elkhart,United States,Indiana,4919987
Fort Wayne,United States,Indiana,4920423
Frankfort,United States,Indiana,4920473
Gary,United States,Indiana,4920607
Goshen,United States,Indiana,4920808
Granger,United States,Indiana,4920869
Griffith,United States,Indiana,4920986
Hammond,United States,Indiana,4921100
Highland,United States,Indiana,4921402
Hobart,United States,Indiana,4921476
Huntington,United States,Indiana,4921725
Kokomo,United States,Indiana,4922388
LaPorte,United States,Indiana,4922459
Lafayette,United States,Indiana,4922462
Lebanon,United States,Indiana,4922673
Logansport,United States,Indiana,4922968
Marion,United States,Indiana,4923210
Merrillville,United States,Indiana,4923482
Michigan City,United States,Indiana,4923531
Mishawaka,United States,Indiana,4923670
Muncie,United States,Indiana,4924006
Munster,United States,Indiana,4924014
Noblesville,United States,Indiana,4924198
Portage,United States,Indiana,4925006
Schererville,United States,Indiana,4926170
South Bend,United States,Indiana,4926563
Valparaiso,United States,Indiana,4927537
West Lafayette,United States,Indiana,4928096
Westfield,United States,Indiana,4928118
Abington,United States,Massachusetts,4928662
Acton,United States,Massachusetts,4928703
Agawam,United States,Massachusetts,4928788
Amesbury,United States,Massachusetts,4929004
Amherst Center,United States,Massachusetts,4929023
Arlington,United States,Massachusetts,4929180
Ashland,United States,Massachusetts,4929283
Attleboro,United States,Massachusetts,4929399
Auburn,United States,Massachusetts,4929417
Barnstable,United States,Massachusetts,4929771
Belmont,United States,Massachusetts,4930282
Beverly,United States,Massachusetts,4930505
Beverly Cove,United States,Massachusetts,4930511
Billerica,United States,Massachusetts,4930577
Boston,United States,Massachusetts,4930956
Braintree,United States,Massachusetts,4931181
Brockton,United States,Massachusetts,4931429
Brookline,United States,Massachusetts,4931482
Burlington,United States,Massachusetts,4931737
Cambridge,United States,Massachusetts,4931972
Canton,United States,Massachusetts,4932214
Chelmsford,United States,Massachusetts,4932869
Chelsea,United States,Massachusetts,4932879
Chicopee,United States,Massachusetts,4933002
Concord,United States,Massachusetts,4933743
Danvers,United States,Massachusetts,4934500
Dedham,United States,Massachusetts,4934664
Dracut,United States,Massachusetts,4935038
East Longmeadow,United States,Massachusetts,4935434
Easthampton,United States,Massachusetts,4935582
Easton,United States,Massachusetts,4935623
Everett,United States,Massachusetts,4936008
Fairhaven,United States,Massachusetts,4936087
Fall River,United States,Massachusetts,4936159
Fitchburg,United States,Massachusetts,4936812
Framingham,United States,Massachusetts,4937230
Framingham Center,United States,Massachusetts,4937232
Franklin,United States,Massachusetts,4937276
Gardner,United States,Massachusetts,4937557
Gloucester,United States,Massachusetts,4937829
Grafton,United States,Massachusetts,4938048
Greenfield,United States,Massachusetts,4938378
Hanover,United States,Massachusetts,4938836
Haverhill,United States,Massachusetts,4939085
Holden,United States,Massachusetts,4939647
Holyoke,United States,Massachusetts,4939783
Jamaica Plain,United States,Massachusetts,4940764
Lawrence,United States,Massachusetts,4941720
Leominster,United States,Massachusetts,4941873
Lexington,United States,Massachusetts,4941935
Longmeadow,United States,Massachusetts,4942508
Lowell,United States,Massachusetts,4942618
Ludlow,United States,Massachusetts,4942744
Lynn,United States,Massachusetts,4942807
Malden,United States,Massachusetts,4942939
Mansfield,United States,Massachusetts,4943021
Marblehead,United States,Massachusetts,4943097
Marlborough,United States,Massachusetts,4943170
Medford,United States,Massachusetts,4943629
Melrose,United States,Massachusetts,4943677
Methuen,United States,Massachusetts,4943828
Milford,United States,Massachusetts,4943958
Milton,United States,Massachusetts,4944193
Natick,United States,Massachusetts,4944994
Needham,United States,Massachusetts,4945055
New Bedford,United States,Massachusetts,4945121
Newburyport,United States,Massachusetts,4945256
Newton,United States,Massachusetts,4945283
North Chicopee,United States,Massachusetts,4945588
Northampton,United States,Massachusetts,4945819
Norton,United States,Massachusetts,4945911
Norwood,United States,Massachusetts,4945952
Palmer,United States,Massachusetts,4946620
Peabody,United States,Massachusetts,4946863
Pittsfield,United States,Massachusetts,4947459
Quincy,United States,Massachusetts,4948247
Randolph,United States,Massachusetts,4948403
Reading,United States,Massachusetts,4948462
Rockland,United States,Massachusetts,4948924
Salem,United States,Massachusetts,4950065
Saugus,United States,Massachusetts,4950267
Shrewsbury,United States,Massachusetts,4950898
Somerset,United States,Massachusetts,4951248
Somerville,United States,Massachusetts,4951257
South Boston,United States,Massachusetts,4951305
South Hadley,United States,Massachusetts,4951397
South Peabody,United States,Massachusetts,4951473
Southbridge,United States,Massachusetts,4951594
Springfield,United States,Massachusetts,4951788
Stoneham,United States,Massachusetts,4952121
Stoughton,United States,Massachusetts,4952206
Sudbury,United States,Massachusetts,4952320
Swansea,United States,Massachusetts,4952487
Taunton,United States,Massachusetts,4952629
Tewksbury,United States,Massachusetts,4952762
Wakefield,United States,Massachusetts,4954265
Waltham,United States,Massachusetts,4954380
Watertown,United States,Massachusetts,4954611
Wellesley,United States,Massachusetts,4954738
West Springfield,United States,Massachusetts,4955089
Westfield,United States,Massachusetts,4955190
Westford,United States,Massachusetts,4955219
Weymouth,United States,Massachusetts,4955336
Wilmington,United States,Massachusetts,4955840
Winchester,United States,Massachusetts,4955884
Winthrop,United States,Massachusetts,4955993
Woburn,United States,Massachusetts,4956032
Worcester,United States,Massachusetts,4956184
Yarmouth,United States,Massachusetts,4956335
Auburn,United States,Maine,4956976
Augusta,United States,Maine,4957003
Bangor,United States,Maine,4957280
Biddeford,United States,Maine,4958141
Brunswick,United States,Maine,4959473
Lewiston,United States,Maine,4969398
Portland,United States,Maine,4975802
Saco,United States,Maine,4977222
South Portland,United States,Maine,4979244
South Portland Gardens,United States,Maine,4979245
Waterville,United States,Maine,4982236
West Scarborough,United States,Maine,4982720
Westbrook,United States,Maine,4982753
Adrian,United States,Michigan,4983811
Allen Park,United States,Michigan,4984016
Allendale,United States,Michigan,4984029
Ann Arbor,United States,Michigan,4984247
Auburn Hills,United States,Michigan,4984565
Battle Creek,United States,Michigan,4985153
Bay City,United States,Michigan,4985180
Birmingham,United States,Michigan,4986172
Burton,United States,Michigan,4987482
Canton,United States,Michigan,4987990
Clinton,United States,Michigan,4989133
Dearborn,United States,Michigan,4990510
Dearborn Heights,United States,Michigan,4990512
Detroit,United States,Michigan,4990729
East Lansing,United States,Michigan,4991640
Eastpointe,United States,Michigan,4991735
Farmington Hills,United States,Michigan,4992523
Ferndale,United States,Michigan,4992635
Flint,United States,Michigan,4992982
Forest Hills,United States,Michigan,4993125
Garden City,United States,Michigan,4993659
Grand Rapids,United States,Michigan,4994358
Grandville,United States,Michigan,4994391
Grosse Pointe Woods,United States,Michigan,4994871
Hamtramck,United States,Michigan,4995197
Haslett,United States,Michigan,4995514
Hazel Park,United States,Michigan,4995664
Holland,United States,Michigan,4996248
Holt,United States,Michigan,4996306
Iron River,United States,Michigan,4997238
Jackson,United States,Michigan,4997384
Jenison,United States,Michigan,4997500
Kalamazoo,United States,Michigan,4997787
Kentwood,United States,Michigan,4998018
Lansing,United States,Michigan,4998830
Lincoln Park,United States,Michigan,4999311
Livonia,United States,Michigan,4999837
Madison Heights,United States,Michigan,5000500
Marquette,United States,Michigan,5000947
Midland,United States,Michigan,5001929
Monroe,United States,Michigan,5002344
Mount Clemens,United States,Michigan,5002656
Mount Pleasant,United States,Michigan,5002714
Muskegon,United States,Michigan,5003132
Norton Shores,United States,Michigan,5004005
Novi,United States,Michigan,5004062
Oak Park,United States,Michigan,5004188
Okemos,United States,Michigan,5004359
Owosso,United States,Michigan,5004792
Pontiac,United States,Michigan,5006166
Port Huron,United States,Michigan,5006233
Portage,United States,Michigan,5006250
Redford,United States,Michigan,5006917
Rochester Hills,United States,Michigan,5007402
Romulus,United States,Michigan,5007531
Roseville,United States,Michigan,5007655
Royal Oak,United States,Michigan,5007804
Saginaw,United States,Michigan,5007989
Shelby,United States,Michigan,5009586
Southfield,United States,Michigan,5010636
Southgate,United States,Michigan,5010646
Saint Clair Shores,United States,Michigan,5010978
Sterling Heights,United States,Michigan,5011148
Taylor,United States,Michigan,5011908
Trenton,United States,Michigan,5012521
Troy,United States,Michigan,5012639
Walker,United States,Michigan,5013924
Warren,United States,Michigan,5014051
Waterford,United States,Michigan,5014130
Waverly,United States,Michigan,5014208
Wayne,United States,Michigan,5014224
Westland,United States,Michigan,5014681
Wyandotte,United States,Michigan,5015599
Wyoming,United States,Michigan,5015618
Ypsilanti,United States,Michigan,5015688
Albert Lea,United States,Minnesota,5016024
Andover,United States,Minnesota,5016374
Anoka,United States,Minnesota,5016450
Apple Valley,United States,Minnesota,5016494
Austin,United States,Minnesota,5016884
Blaine,United States,Minnesota,5018651
Bloomington,United States,Minnesota,5018739
Brooklyn Center,United States,Minnesota,5019330
Brooklyn Park,United States,Minnesota,5019335
Buffalo,United States,Minnesota,5019588
Burnsville,United States,Minnesota,5019767
Champlin,United States,Minnesota,5020859
Chanhassen,United States,Minnesota,5020881
Chaska,United States,Minnesota,5020938
Columbia Heights,United States,Minnesota,5021828
Coon Rapids,United States,Minnesota,5022025
Cottage Grove,United States,Minnesota,5022134
Crystal,United States,Minnesota,5023571
Duluth,United States,Minnesota,5024719
Eagan,United States,Minnesota,5024825
Eden Prairie,United States,Minnesota,5025219
Edina,United States,Minnesota,5025264
Elk River,United States,Minnesota,5025471
Faribault,United States,Minnesota,5026291
Farmington,United States,Minnesota,5026321
Forest Lake,United States,Minnesota,5027117
Fridley,United States,Minnesota,5027482
Golden Valley,United States,Minnesota,5028163
Ham Lake,United States,Minnesota,5029181
Hastings,United States,Minnesota,5029500
Hibbing,United States,Minnesota,5030005
Hopkins,United States,Minnesota,5030670
Inver Grove Heights,United States,Minnesota,5031412
Lakeville,United States,Minnesota,5034059
Lino Lakes,United States,Minnesota,5034767
Mankato,United States,Minnesota,5036420
Maple Grove,United States,Minnesota,5036493
Maplewood,United States,Minnesota,5036588
Minneapolis,United States,Minnesota,5037649
Minnetonka,United States,Minnesota,5037784
Minnetonka Mills,United States,Minnesota,5037790
Moorhead,United States,Minnesota,5038108
New Brighton,United States,Minnesota,5039080
New Hope,United States,Minnesota,5039094
Northfield,United States,Minnesota,5039675
Oakdale,United States,Minnesota,5039978
Owatonna,United States,Minnesota,5040647
Plymouth,United States,Minnesota,5041926
Prior Lake,United States,Minnesota,5042373
Ramsey,United States,Minnesota,5042561
Red Wing,United States,Minnesota,5042773
Richfield,United States,Minnesota,5043193
Rochester,United States,Minnesota,5043473
Rosemount,United States,Minnesota,5043779
Roseville,United States,Minnesota,5043799
Saint Cloud,United States,Minnesota,5044407
Saint Louis Park,United States,Minnesota,5045021
Saint Michael,United States,Minnesota,5045258
Saint Paul,United States,Minnesota,5045360
Sartell,United States,Minnesota,5046001
Savage,United States,Minnesota,5046063
Shakopee,United States,Minnesota,5046997
Shoreview,United States,Minnesota,5047234
South Saint Paul,United States,Minnesota,5048033
Stillwater,United States,Minnesota,5048814
West Coon Rapids,United States,Minnesota,5052361
West Saint Paul,United States,Minnesota,5052467
White Bear Lake,United States,Minnesota,5052658
Willmar,United States,Minnesota,5052916
Winona,United States,Minnesota,5053156
Woodbury,United States,Minnesota,5053358
Kirksville,United States,Missouri,5055787
Fargo,United States,North Dakota,5059163
Grand Forks,United States,North Dakota,5059429
Jamestown,United States,North Dakota,5059836
West Fargo,United States,North Dakota,5062458
Bellevue,United States,Nebraska,5063805
Columbus,United States,Nebraska,5066001
Fremont,United States,Nebraska,5068725
Grand Island,United States,Nebraska,5069297
Hastings,United States,Nebraska,5069802
Kearney,United States,Nebraska,5071348
La Vista,United States,Nebraska,5071665
Lincoln,United States,Nebraska,5072006
Norfolk,United States,Nebraska,5073965
Omaha,United States,Nebraska,5074472
Papillion,United States,Nebraska,5074792
Bedford,United States,New Hampshire,5083221
Concord,United States,New Hampshire,5084868
Derry,United States,New Hampshire,5085374
Derry Village,United States,New Hampshire,5085382
Dover,United States,New Hampshire,5085520
East Concord,United States,New Hampshire,5085688
Keene,United States,New Hampshire,5088262
Laconia,United States,New Hampshire,5088438
Manchester,United States,New Hampshire,5089178
Merrimack,United States,New Hampshire,5089478
Nashua,United States,New Hampshire,5090046
Portsmouth,United States,New Hampshire,5091383
Rochester,United States,New Hampshire,5091872
Salem,United States,New Hampshire,5092268
Asbury Park,United States,New Jersey,5095281
Avenel,United States,New Jersey,5095325
Bayonne,United States,New Jersey,5095445
Belleville,United States,New Jersey,5095549
Bergenfield,United States,New Jersey,5095611
Bloomfield,United States,New Jersey,5095779
Carteret,United States,New Jersey,5096316
Cliffside Park,United States,New Jersey,5096686
Clifton,United States,New Jersey,5096699
Colonia,United States,New Jersey,5096798
Cranford,United States,New Jersey,5097017
Dover,United States,New Jersey,5097315
Dumont,United States,New Jersey,5097357
East Brunswick,United States,New Jersey,5097402
East Orange,United States,New Jersey,5097441
Edison,United States,New Jersey,5097529
Elizabeth,United States,New Jersey,5097598
Elmwood Park,United States,New Jersey,5097627
Englewood,United States,New Jersey,5097672
Ewing,United States,New Jersey,5097751
Fair Lawn,United States,New Jersey,5097773
Fords,United States,New Jersey,5098109
Fort Lee,United States,New Jersey,5098135
Garfield,United States,New Jersey,5098343
Hackensack,United States,New Jersey,5098706
Hawthorne,United States,New Jersey,5098909
Hillside,United States,New Jersey,5099093
Hoboken,United States,New Jersey,5099133
Hopatcong,United States,New Jersey,5099289
Hopatcong Hills,United States,New Jersey,5099292
Irvington,United States,New Jersey,5099724
Iselin,United States,New Jersey,5099738
Jersey City,United States,New Jersey,5099836
Kearny,United States,New Jersey,5099967
Lakewood,United States,New Jersey,5100280
Linden,United States,New Jersey,5100506
Livingston,United States,New Jersey,5100572
Lodi,United States,New Jersey,5100604
Long Branch,United States,New Jersey,5100619
Lyndhurst,United States,New Jersey,5100706
Madison,United States,New Jersey,5100748
Mahwah,United States,New Jersey,5100776
Maplewood,United States,New Jersey,5100854
Marlboro,United States,New Jersey,5100886
Montclair,United States,New Jersey,5101334
Morristown,United States,New Jersey,5101427
New Brunswick,United States,New Jersey,5101717
New Milford,United States,New Jersey,5101766
Newark,United States,New Jersey,5101798
North Arlington,United States,New Jersey,5101873
North Bergen,United States,New Jersey,5101879
North Plainfield,United States,New Jersey,5101938
Nutley,United States,New Jersey,5102076
Old Bridge,United States,New Jersey,5102162
Orange,United States,New Jersey,5102213
Palisades Park,United States,New Jersey,5102369
Paramus,United States,New Jersey,5102387
Parsippany,United States,New Jersey,5102427
Passaic,United States,New Jersey,5102443
Paterson,United States,New Jersey,5102466
Perth Amboy,United States,New Jersey,5102578
Piscataway,United States,New Jersey,5102713
Plainfield,United States,New Jersey,5102720
Point Pleasant,United States,New Jersey,5102796
Rahway,United States,New Jersey,5103055
Ridgewood,United States,New Jersey,5103269
Roselle,United States,New Jersey,5103500
Rutherford,United States,New Jersey,5103580
Sayreville,United States,New Jersey,5104404
Sayreville Junction,United States,New Jersey,5104405
Scotch Plains,United States,New Jersey,5104473
Secaucus,United States,New Jersey,5104504
Somerset,United States,New Jersey,5104755
South Old Bridge,United States,New Jersey,5104835
South Orange,United States,New Jersey,5104836
South Plainfield,United States,New Jersey,5104844
South River,United States,New Jersey,5104853
Summit,United States,New Jersey,5105127
Teaneck,United States,New Jersey,5105262
Tinton Falls,United States,New Jersey,5105433
Trenton,United States,New Jersey,5105496
Union,United States,New Jersey,5105608
Union City,United States,New Jersey,5105634
Wayne,United States,New Jersey,5106160
West Milford,United States,New Jersey,5106279
West New York,United States,New Jersey,5106292
West Orange,United States,New Jersey,5106298
Westfield,United States,New Jersey,5106331
Willingboro,United States,New Jersey,5106453
Woodbridge,United States,New Jersey,5106529
Wyckoff,United States,New Jersey,5106615
Albany,United States,New York,5106834
Amherst,United States,New York,5107129
Amsterdam,United States,New York,5107152
Auburn,United States,New York,5107505
Baldwin,United States,New York,5107760
Batavia,United States,New York,5108093
Bay Shore,United States,New York,5108169
Beacon,United States,New York,5108219
Bellmore,United States,New York,5108707
Bensonhurst,United States,New York,5108815
Bethpage,United States,New York,5108955
Binghamton,United States,New York,5109177
Brentwood,United States,New York,5110077
Brighton,United States,New York,5110159
The Bronx,United States,New York,5110266
Brooklyn,United States,New York,5110302
Buffalo,United States,New York,5110629
Centereach,United States,New York,5112035
Central Islip,United States,New York,5112078
Cheektowaga,United States,New York,5112375
Cohoes,United States,New York,5113142
Commack,United States,New York,5113412
Coney Island,United States,New York,5113481
Copiague,United States,New York,5113683
Coram,United States,New York,5113694
Cortland,United States,New York,5113790
Deer Park,United States,New York,5114731
Depew,United States,New York,5114900
Dix Hills,United States,New York,5115107
East Meadow,United States,New York,5115960
East Massapequa,United States,New York,5115962
East New York,United States,New York,5115985
East Northport,United States,New York,5115989
East Patchogue,United States,New York,5116004
East Setauket,United States,New York,5116060
Eastchester,United States,New York,5116119
Eggertsville,United States,New York,5116303
Elmira,United States,New York,5116497
Elmont,United States,New York,5116508
Farmingville,United States,New York,5116937
Floral Park,United States,New York,5117438
Franklin Square,United States,New York,5117891
Freeport,United States,New York,5117949
Garden City,United States,New York,5118226
Glen Cove,United States,New York,5118626
Gloversville,United States,New York,5118743
Greenburgh,United States,New York,5119347
Harrison,United States,New York,5120095
Hauppauge,United States,New York,5120228
Hempstead,United States,New York,5120478
Hicksville,United States,New York,5120656
Holbrook,United States,New York,5120987
Holtsville,United States,New York,5121163
Huntington,United States,New York,5121636
Huntington Station,United States,New York,5121650
Irondequoit,United States,New York,5122331
Islip,United States,New York,5122413
Ithaca,United States,New York,5122432
Jamaica,United States,New York,5122520
Jamestown,United States,New York,5122534
Johnson City,United States,New York,5122794
Kenmore,United States,New York,5123247
Kings Park,United States,New York,5123456
Kingston,United States,New York,5123477
Kiryas Joel,United States,New York,5123533
Lackawanna,United States,New York,5123718
Lake Ronkonkoma,United States,New York,5123840
Levittown,United States,New York,5124276
Lindenhurst,United States,New York,5124497
Lockport,United States,New York,5125011
Long Beach,United States,New York,5125086
Long Island City,United States,New York,5125125
Lynbrook,United States,New York,5125523
Mamaroneck,United States,New York,5125738
Manhattan,United States,New York,5125771
Massapequa,United States,New York,5126183
Massapequa Park,United States,New York,5126187
Mastic,United States,New York,5126208
Medford,United States,New York,5126518
Melville,United States,New York,5126555
Merrick,United States,New York,5126630
Middletown,United States,New York,5126842
Mineola,United States,New York,5127134
Monsey,United States,New York,5127315
Mount Vernon,United States,New York,5127835
Nanuet,United States,New York,5128266
New City,United States,New York,5128481
New Rochelle,United States,New York,5128549
New York City,United States,New York,5128581
Newburgh,United States,New York,5128654
Niagara Falls,United States,New York,5128723
North Amityville,United States,New York,5128884
North Babylon,United States,New York,5128886
North Bay Shore,United States,New York,5128898
North Bellmore,United States,New York,5128904
North Massapequa,United States,New York,5129134
North Tonawanda,United States,New York,5129245
North Valley Stream,United States,New York,5129248
Oceanside,United States,New York,5129603
Ossining,United States,New York,5130045
Oswego,United States,New York,5130081
Pearl River,United States,New York,5130780
Peekskill,United States,New York,5130831
Plainview,United States,New York,5131638
Plattsburgh,United States,New York,5131692
Port Chester,United States,New York,5132002
Port Washington,United States,New York,5132029
Poughkeepsie,United States,New York,5132143
Borough of Queens,United States,New York,5133273
Rochester,United States,New York,5134086
Rockville Centre,United States,New York,5134203
Rome,United States,New York,5134295
Ronkonkoma,United States,New York,5134316
Roosevelt,United States,New York,5134323
Rotterdam,United States,New York,5134453
Rye,United States,New York,5134693
Saratoga Springs,United States,New York,5136334
Sayville,United States,New York,5136421
Scarsdale,United States,New York,5136433
Schenectady,United States,New York,5136454
Seaford,United States,New York,5137507
Selden,United States,New York,5137600
Shirley,United States,New York,5138022
Smithtown,United States,New York,5138539
Spring Valley,United States,New York,5139301
Staten Island,United States,New York,5139568
Syosset,United States,New York,5140402
Syracuse,United States,New York,5140405
Tonawanda,United States,New York,5141175
Troy,United States,New York,5141502
Uniondale,United States,New York,5141927
Utica,United States,New York,5142056
Valley Stream,United States,New York,5142109
Wantagh,United States,New York,5143198
Watertown,United States,New York,5143396
West Albany,United States,New York,5143620
West Babylon,United States,New York,5143630
West Hempstead,United States,New York,5143832
West Islip,United States,New York,5143866
West Seneca,United States,New York,5143992
Westbury,United States,New York,5144040
White Plains,United States,New York,5144336
Woodmere,United States,New York,5145028
Yonkers,United States,New York,5145215
Akron,United States,Ohio,5145476
Alliance,United States,Ohio,5145607
Ashland,United States,Ohio,5146055
Ashtabula,United States,Ohio,5146089
Aurora,United States,Ohio,5146233
Austintown,United States,Ohio,5146256
Avon,United States,Ohio,5146277
Avon Center,United States,Ohio,5146282
Avon Lake,United States,Ohio,5146286
Barberton,United States,Ohio,5146491
Bay Village,United States,Ohio,5146675
Berea,United States,Ohio,5147097
Boardman,United States,Ohio,5147784
Bowling Green,United States,Ohio,5147968
Broadview Heights,United States,Ohio,5148273
Brook Park,United States,Ohio,5148326
Brunswick,United States,Ohio,5148480
Canton,United States,Ohio,5149222
Cleveland,United States,Ohio,5150529
Cuyahoga Falls,United States,Ohio,5151613
Defiance,United States,Ohio,5151861
Delaware,United States,Ohio,5151891
Dublin,United States,Ohio,5152333
East Cleveland,United States,Ohio,5152599
Eastlake,United States,Ohio,5152833
Elyria,United States,Ohio,5153207
Euclid,United States,Ohio,5153420
Fairview Park,United States,Ohio,5153680
Findlay,United States,Ohio,5153924
Fremont,United States,Ohio,5155207
Gahanna,United States,Ohio,5155393
Garfield Heights,United States,Ohio,5155499
Green,United States,Ohio,5156371
Hilliard,United States,Ohio,5157588
Hudson,United States,Ohio,5158164
Kent,United States,Ohio,5159537
Lakewood,United States,Ohio,5160315
Lima,United States,Ohio,5160783
Lorain,United States,Ohio,5161262
Mansfield,United States,Ohio,5161723
Maple Heights,United States,Ohio,5161803
Marion,United States,Ohio,5161902
Marysville,United States,Ohio,5162077
Massillon,United States,Ohio,5162097
Mayfield Heights,United States,Ohio,5162188
Medina,United States,Ohio,5162512
Mentor,United States,Ohio,5162645
Middleburg Heights,United States,Ohio,5162851
Mount Vernon,United States,Ohio,5163799
New Philadelphia,United States,Ohio,5164390
Newark,United States,Ohio,5164466
Niles,United States,Ohio,5164582
North Canton,United States,Ohio,5164706
North Olmsted,United States,Ohio,5164862
North Ridgeville,United States,Ohio,5164903
North Royalton,United States,Ohio,5164916
Norwalk,United States,Ohio,5165101
Oregon,United States,Ohio,5165734
Painesville,United States,Ohio,5166009
Parma,United States,Ohio,5166177
Parma Heights,United States,Ohio,5166184
Perrysburg,United States,Ohio,5166516
Piqua,United States,Ohio,5166819
Rocky River,United States,Ohio,5168491
Sandusky,United States,Ohio,5170691
Shaker Heights,United States,Ohio,5171728
Sidney,United States,Ohio,5172078
Solon,United States,Ohio,5172387
South Euclid,United States,Ohio,5172485
Steubenville,United States,Ohio,5173048
Stow,United States,Ohio,5173171
Streetsboro,United States,Ohio,5173210
Strongsville,United States,Ohio,5173237
Sylvania,United States,Ohio,5173572
Tallmadge,United States,Ohio,5173623
Tiffin,United States,Ohio,5173930
Toledo,United States,Ohio,5174035
Troy,United States,Ohio,5174358
Twinsburg,United States,Ohio,5174550
Wadsworth,United States,Ohio,5175496
Warren,United States,Ohio,5175865
Westerville,United States,Ohio,5176472
Westlake,United States,Ohio,5176517
Willoughby,United States,Ohio,5176937
Wooster,United States,Ohio,5177358
Youngstown,United States,Ohio,5177568
Allentown,United States,Pennsylvania,5178127
Allison Park,United States,Pennsylvania,5178165
Altoona,United States,Pennsylvania,5178195
Back Mountain,United States,Pennsylvania,5178800
Baldwin,United States,Pennsylvania,5178940
Bethel Park,United States,Pennsylvania,5180199
Bethlehem,United States,Pennsylvania,5180225
Carlisle,United States,Pennsylvania,5183234
Easton,United States,Pennsylvania,5188140
Erie,United States,Pennsylvania,5188843
Harrisburg,United States,Pennsylvania,5192726
Hazleton,United States,Pennsylvania,5193011
Hermitage,United States,Pennsylvania,5193309
Johnstown,United States,Pennsylvania,5195561
King of Prussia,United States,Pennsylvania,5196220
Lancaster,United States,Pennsylvania,5197079
Lansdale,United States,Pennsylvania,5197159
Lebanon,United States,Pennsylvania,5197517
Levittown,United States,Pennsylvania,5197796
Limerick,United States,Pennsylvania,5198034
McKeesport,United States,Pennsylvania,5200499
Monroeville,United States,Pennsylvania,5201734
Mount Lebanon,United States,Pennsylvania,5202215
Mountain Top,United States,Pennsylvania,5202534
Murrysville,United States,Pennsylvania,5202765
New Castle,United States,Pennsylvania,5203127
Norristown,United States,Pennsylvania,5203506
Penn Hills,United States,Pennsylvania,5205377
Phoenixville,United States,Pennsylvania,5205849
Pittsburgh,United States,Pennsylvania,5206379
Plum,United States,Pennsylvania,5206606
Pottstown,United States,Pennsylvania,5207069
Radnor,United States,Pennsylvania,5207490
Reading,United States,Pennsylvania,5207728
Scranton,United States,Pennsylvania,5211303
State College,United States,Pennsylvania,5213681
Upper Saint Clair,United States,Pennsylvania,5216895
Wayne,United States,Pennsylvania,5218270
West Mifflin,United States,Pennsylvania,5218802
Whitehall Township,United States,Pennsylvania,5219287
Wilkes-Barre,United States,Pennsylvania,5219488
Wilkinsburg,United States,Pennsylvania,5219501
Williamsport,United States,Pennsylvania,5219585
Willow Grove,United States,Pennsylvania,5219619
Barrington,United States,Rhode Island,5220798
Bristol,United States,Rhode Island,5221077
Central Falls,United States,Rhode Island,5221341
Coventry,United States,Rhode Island,5221637
Cranston,United States,Rhode Island,5221659
Cumberland,United States,Rhode Island,5221703
East Providence,United States,Rhode Island,5221931
Middletown,United States,Rhode Island,5223358
Newport,United States,Rhode Island,5223593
North Kingstown,United States,Rhode Island,5223672
North Providence,United States,Rhode Island,5223681
Pawtucket,United States,Rhode Island,5223869
Portsmouth,United States,Rhode Island,5224082
Providence,United States,Rhode Island,5224151
Smithfield,United States,Rhode Island,5224949
Warwick,United States,Rhode Island,5225507
West Warwick,United States,Rhode Island,5225627
Westerly,United States,Rhode Island,5225631
Woonsocket,United States,Rhode Island,5225809
Aberdeen,United States,South Dakota,5225857
Brookings,United States,South Dakota,5226534
Mitchell,United States,South Dakota,5229794
Sioux Falls,United States,South Dakota,5231851
Watertown,United States,South Dakota,5232741
Burlington,United States,Vermont,5234372
Colchester,United States,Vermont,5235024
Rutland,United States,Vermont,5240509
South Burlington,United States,Vermont,5241248
Appleton,United States,Wisconsin,5244080
Ashwaubenon,United States,Wisconsin,5244267
Beaver Dam,United States,Wisconsin,5245193
Beloit,United States,Wisconsin,5245387
Brookfield,United States,Wisconsin,5246835
Caledonia,United States,Wisconsin,5247415
Cudahy,United States,Wisconsin,5249871
De Pere,United States,Wisconsin,5250201
Eau Claire,United States,Wisconsin,5251436
Fitchburg,United States,Wisconsin,5253219
Fond du Lac,United States,Wisconsin,5253352
Franklin,United States,Wisconsin,5253710
Germantown,United States,Wisconsin,5254218
Green Bay,United States,Wisconsin,5254962
Greenfield,United States,Wisconsin,5255068
Howard,United States,Wisconsin,5257029
Janesville,United States,Wisconsin,5257754
Kaukauna,United States,Wisconsin,5258296
Kenosha,United States,Wisconsin,5258393
La Crosse,United States,Wisconsin,5258957
Madison,United States,Wisconsin,5261457
Manitowoc,United States,Wisconsin,5261585
Marshfield,United States,Wisconsin,5261969
Menasha,United States,Wisconsin,5262596
Menomonee Falls,United States,Wisconsin,5262630
Menomonie,United States,Wisconsin,5262634
Mequon,United States,Wisconsin,5262649
Middleton,United States,Wisconsin,5262838
Milwaukee,United States,Wisconsin,5263045
Muskego,United States,Wisconsin,5264049
Neenah,United States,Wisconsin,5264223
New Berlin,United States,Wisconsin,5264381
North La Crosse,United States,Wisconsin,5264870
Oak Creek,United States,Wisconsin,5265228
Oconomowoc,United States,Wisconsin,5265499
Onalaska,United States,Wisconsin,5265702
Oshkosh,United States,Wisconsin,5265838
Pleasant Prairie,United States,Wisconsin,5267403
Racine,United States,Wisconsin,5268249
Sheboygan,United States,Wisconsin,5272893
South Milwaukee,United States,Wisconsin,5273812
Stevens Point,United States,Wisconsin,5274644
Sun Prairie,United States,Wisconsin,5275020
Superior,United States,Wisconsin,5275191
Watertown,United States,Wisconsin,5278005
Waukesha,United States,Wisconsin,5278052
Wausau,United States,Wisconsin,5278120
Wauwatosa,United States,Wisconsin,5278159
West Allis,United States,Wisconsin,5278420
West Bend,United States,Wisconsin,5278422
Wisconsin Rapids,United States,Wisconsin,5279436
Weirton,United States,West Virginia,5280814
Weirton Heights,United States,West Virginia,5280822
Wheeling,United States,West Virginia,5280854
Ansonia,United States,Connecticut,5281551
Bridgeport,United States,Connecticut,5282804
Bristol,United States,Connecticut,5282835
Branford,United States,Connecticut,5283054
Cheshire,United States,Connecticut,5283837
Fillmore,United States,California,5284756
Buckeye,United States,Arizona,5287262
Bullhead City,United States,Arizona,5287565
Casa Grande,United States,Arizona,5288636
Casas Adobes,United States,Arizona,5288661
Catalina Foothills,United States,Arizona,5288786
Chandler,United States,Arizona,5289282
Douglas,United States,Arizona,5293083
Drexel Heights,United States,Arizona,5293183
El Mirage,United States,Arizona,5293996
Eloy,United States,Arizona,5294167
Flagstaff,United States,Arizona,5294810
Florence,United States,Arizona,5294902
Flowing Wells,United States,Arizona,5294937
Fortuna Foothills,United States,Arizona,5295143
Fountain Hills,United States,Arizona,5295177
Gilbert,United States,Arizona,5295903
Glendale,United States,Arizona,5295985
Goodyear,United States,Arizona,5296266
Green Valley,United States,Arizona,5296802
Kingman,United States,Arizona,5301067
Lake Havasu City,United States,Arizona,5301388
Marana,United States,Arizona,5303705
Maricopa,United States,Arizona,5303752
Mesa,United States,Arizona,5304391
Nogales,United States,Arizona,5306611
Oro Valley,United States,Arizona,5307540
Payson,United States,Arizona,5308305
Peoria,United States,Arizona,5308480
Phoenix,United States,Arizona,5308655
Prescott,United States,Arizona,5309842
Prescott Valley,United States,Arizona,5309858
Queen Creek,United States,Arizona,5310193
Rio Rico,United States,Arizona,5311433
Sahuarita,United States,Arizona,5312544
San Luis,United States,Arizona,5312913
Scottsdale,United States,Arizona,5313457
Sierra Vista,United States,Arizona,5314328
Sun City,United States,Arizona,5316201
Sun City West,United States,Arizona,5316205
Surprise,United States,Arizona,5316428
Tanque Verde,United States,Arizona,5316890
Tempe,United States,Arizona,5317058
Tempe Junction,United States,Arizona,5317071
Tucson,United States,Arizona,5318313
Yuma,United States,Arizona,5322053
Adelanto,United States,California,5322400
Agoura,United States,California,5322551
Agoura Hills,United States,California,5322553
Alameda,United States,California,5322737
Albany,United States,California,5322850
Alhambra,United States,California,5323060
Aliso Viejo,United States,California,5323163
Altadena,United States,California,5323525
Alum Rock,United States,California,5323566
American Canyon,United States,California,5323694
Anaheim,United States,California,5323810
Antelope,United States,California,5324105
Antioch,United States,California,5324200
Apple Valley,United States,California,5324363
Arcadia,United States,California,5324477
Arroyo Grande,United States,California,5324802
Artesia,United States,California,5324862
Arvin,United States,California,5324903
Ashland,United States,California,5325011
Atascadero,United States,California,5325111
Atwater,United States,California,5325187
Avenal,United States,California,5325327
Avocado Heights,United States,California,5325372
Azusa,United States,California,5325423
Bakersfield,United States,California,5325738
Baldwin Park,United States,California,5325866
Banning,United States,California,5326032
Barstow,United States,California,5326297
Barstow Heights,United States,California,5326305
Bay Point,United States,California,5326561
Beaumont,United States,California,5327098
Bell,United States,California,5327298
Bell Gardens,United States,California,5327319
Bellflower,United States,California,5327422
Belmont,United States,California,5327455
Benicia,United States,California,5327550
Berkeley,United States,California,5327684
Beverly Hills,United States,California,5328041
Bloomington,United States,California,5329408
Blythe,United States,California,5329649
Bostonia,United States,California,5330167
Boyle Heights,United States,California,5330413
Brawley,United States,California,5330567
Brea,United States,California,5330582
Brentwood,United States,California,5330642
Buena Park,United States,California,5331575
Burbank,United States,California,5331835
Burlingame,United States,California,5331920
Calabasas,United States,California,5332593
Calexico,United States,California,5332698
Camarillo,United States,California,5333180
Cameron Park,United States,California,5333282
Campbell,United States,California,5333689
Canoga Park,United States,California,5333913
Carlsbad,United States,California,5334223
Carmichael,United States,California,5334336
Carson,United States,California,5334519
Castaic,United States,California,5334799
Castro Valley,United States,California,5334928
Cathedral City,United States,California,5335006
Ceres,United States,California,5335650
Cerritos,United States,California,5335663
Chatsworth,United States,California,5336054
Chico,United States,California,5336269
Chino,United States,California,5336537
Chino Hills,United States,California,5336545
Chowchilla,United States,California,5336667
Chula Vista,United States,California,5336899
Citrus Heights,United States,California,5337561
Claremont,United States,California,5337696
Clearlake,United States,California,5337908
Clovis,United States,California,5338122
Coachella,United States,California,5338166
Colton,United States,California,5338783
Compton,United States,California,5339066
Concord,United States,California,5339111
Corcoran,United States,California,5339539
Corona,United States,California,5339631
Coronado,United States,California,5339663
Costa Mesa,United States,California,5339840
Covina,United States,California,5340175
Cudahy,United States,California,5341051
Culver City,United States,California,5341114
Cupertino,United States,California,5341145
Cypress,United States,California,5341256
Daly City,United States,California,5341430
Dana Point,United States,California,5341483
Danville,United States,California,5341531
Davis,United States,California,5341704
Delano,United States,California,5342485
Desert Hot Springs,United States,California,5342710
Diamond Bar,United States,California,5342992
Dinuba,United States,California,5343171
Dixon,United States,California,5343303
Downey,United States,California,5343858
Duarte,United States,California,5344147
Dublin,United States,California,5344157
East Rancho Dominguez,United States,California,5344817
East Hemet,United States,California,5344942
East Los Angeles,United States,California,5344994
East Palo Alto,United States,California,5345032
El Cajon,United States,California,5345529
El Centro,United States,California,5345609
El Cerrito,United States,California,5345623
El Dorado Hills,United States,California,5345679
El Monte,United States,California,5345743
El Segundo,United States,California,5345860
Elk Grove,United States,California,5346111
Encinitas,United States,California,5346646
Escondido,United States,California,5346827
Fair Oaks,United States,California,5347287
Fairfield,United States,California,5347335
Fallbrook,United States,California,5347578
Florin,United States,California,5349613
Folsom,United States,California,5349705
Fontana,United States,California,5349755
Foothill Farms,United States,California,5349803
Foster City,United States,California,5350159
Fountain Valley,United States,California,5350207
Fremont,United States,California,5350734
Fresno,United States,California,5350937
Fullerton,United States,California,5351247
Galt,United States,California,5351428
Garden Grove,United States,California,5351515
Gardena,United States,California,5351549
Gilroy,United States,California,5352214
Glen Avon,United States,California,5352350
Glendale,United States,California,5352423
Glendora,United States,California,5352439
Goleta,United States,California,5352963
Granite Bay,United States,California,5353530
Greenfield,United States,California,5354172
Hacienda Heights,United States,California,5354819
Hanford,United States,California,5355180
Hawthorne,United States,California,5355828
Hayward,United States,California,5355933
Hemet,United States,California,5356277
Hercules,United States,California,5356451
Hermosa Beach,United States,California,5356521
Hesperia,United States,California,5356576
Highland,United States,California,5356868
Hollister,United States,California,5357499
Hollywood,United States,California,5357527
Huntington Beach,United States,California,5358705
Huntington Park,United States,California,5358736
Imperial Beach,United States,California,5359054
Indio,United States,California,5359446
Inglewood,United States,California,5359488
Irvine,United States,California,5359777
Lodi,United States,California,5367565
Loma Linda,United States,California,5367696
Lomita,United States,California,5367767
Lompoc,United States,California,5367788
Long Beach,United States,California,5367929
Los Altos,United States,California,5368335
Los Angeles,United States,California,5368361
Los Banos,United States,California,5368453
Los Gatos,United States,California,5368518
Lynwood,United States,California,5369367
Madera,United States,California,5369568
Manhattan Beach,United States,California,5370082
Manteca,United States,California,5370164
Marina,United States,California,5370493
Martinez,United States,California,5370868
Maywood,United States,California,5371261
Mead Valley,United States,California,5371858
Menifee,United States,California,5372205
Menlo Park,United States,California,5372223
Merced,United States,California,5372253
Millbrae,United States,California,5373129
Milpitas,United States,California,5373327
Mira Loma,United States,California,5373492
Mission Viejo,United States,California,5373763
Modesto,United States,California,5373900
Monrovia,United States,California,5374175
Montclair,United States,California,5374232
Montebello,United States,California,5374322
Monterey,United States,California,5374361
Monterey Park,United States,California,5374406
Moorpark,United States,California,5374648
Moraga,United States,California,5374671
Moreno Valley,United States,California,5374732
Morgan Hill,United States,California,5374764
Mountain View,United States,California,5375480
Murrieta,United States,California,5375911
Napa,United States,California,5376095
National City,United States,California,5376200
Newark,United States,California,5376803
Newport Beach,United States,California,5376890
Nipomo,United States,California,5377100
Norco,United States,California,5377199
North Glendale,United States,California,5377613
North Highlands,United States,California,5377640
North Hollywood,United States,California,5377654
Northridge,United States,California,5377985
Norwalk,United States,California,5377995
Novato,United States,California,5378044
Oakdale,United States,California,5378500
Oakland,United States,California,5378538
Oakley,United States,California,5378566
Oceanside,United States,California,5378771
Oildale,United States,California,5378870
Ontario,United States,California,5379439
Orange,United States,California,5379513
Orangevale,United States,California,5379566
Orcutt,United States,California,5379609
Orinda,United States,California,5379678
Oroville,United States,California,5379759
Oxnard,United States,California,5380184
Oxnard Shores,United States,California,5380202
Pacifica,United States,California,5380420
Pacific Grove,United States,California,5380437
Palm Desert,United States,California,5380626
Palm Springs,United States,California,5380668
Palmdale,United States,California,5380698
Palo Alto,United States,California,5380748
Paradise,United States,California,5381002
Paramount,United States,California,5381110
Pasadena,United States,California,5381396
Paso Robles,United States,California,5381438
Patterson,United States,California,5381515
Perris,United States,California,5382146
Petaluma,United States,California,5382232
Pico Rivera,United States,California,5382496
Pinole,United States,California,5383187
Pittsburg,United States,California,5383465
Placentia,United States,California,5383527
Pleasant Hill,United States,California,5383720
Pleasanton,United States,California,5383777
Pomona,United States,California,5384170
Port Hueneme,United States,California,5384339
Porterville,United States,California,5384471
Poway,United States,California,5384690
Prunedale,United States,California,5385082
Ramona,United States,California,5385793
Rancho Cordova,United States,California,5385941
Rancho Cucamonga,United States,California,5385955
Rancho Mirage,United States,California,5386015
Rancho Palos Verdes,United States,California,5386035
Rancho San Diego,United States,California,5386053
Rancho Santa Margarita,United States,California,5386082
Redlands,United States,California,5386754
Redondo Beach,United States,California,5386785
Redwood City,United States,California,5386834
Reedley,United States,California,5386984
Rialto,United States,California,5387288
Richmond,United States,California,5387428
Ridgecrest,United States,California,5387494
Rio Linda,United States,California,5387687
Riverbank,United States,California,5387844
Riverside,United States,California,5387877
Rocklin,United States,California,5388319
Rohnert Park,United States,California,5388564
Rosamond,United States,California,5388735
Rosemead,United States,California,5388867
Rosemont,United States,California,5388873
Roseville,United States,California,5388881
Rowland Heights,United States,California,5389126
Rubidoux,United States,California,5389213
Sacramento,United States,California,5389489
Salinas,United States,California,5391295
San Bernardino,United States,California,5391710
San Bruno,United States,California,5391749
San Carlos,United States,California,5391760
San Clemente,United States,California,5391791
San Diego,United States,California,5391811
San Dimas,United States,California,5391891
San Fernando,United States,California,5391945
San Francisco,United States,California,5391959
San Gabriel,United States,California,5392034
San Jacinto,United States,California,5392090
San Jose,United States,California,5392171
San Juan Capistrano,United States,California,5392229
San Leandro,United States,California,5392263
San Lorenzo,United States,California,5392281
San Luis Obispo,United States,California,5392323
San Marcos,United States,California,5392368
San Mateo,United States,California,5392423
San Pablo,United States,California,5392508
San Pedro,United States,California,5392528
San Rafael,United States,California,5392567
San Ramon,United States,California,5392593
Sanger,United States,California,5392868
Santa Ana,United States,California,5392900
Santa Barbara,United States,California,5392952
Santa Clara,United States,California,5393015
Santa Clarita,United States,California,5393049
Santa Cruz,United States,California,5393052
Santa Fe Springs,United States,California,5393128
Santa Maria,United States,California,5393180
Santa Monica,United States,California,5393212
Santa Paula,United States,California,5393245
Santa Rosa,United States,California,5393287
Santee,United States,California,5393429
Saratoga,United States,California,5393485
Seal Beach,United States,California,5394086
Seaside,United States,California,5394136
Selma,United States,California,5394329
Shafter,United States,California,5394842
Sherman Oaks,United States,California,5395244
Simi Valley,United States,California,5396003
Soledad,United States,California,5397018
South El Monte,United States,California,5397376
South Gate,United States,California,5397603
South Lake Tahoe,United States,California,5397664
South Pasadena,United States,California,5397717
South San Francisco,United States,California,5397765
South San Jose Hills,United States,California,5397777
South Whittier,United States,California,5397841
South Yuba City,United States,California,5397851
Spring Valley,United States,California,5398277
Stanton,United States,California,5398630
Stockton,United States,California,5399020
Suisun,United States,California,5399629
Sun City,United States,California,5399901
Sunnyvale,United States,California,5400075
Temecula,United States,California,5401395
Temple City,United States,California,5401469
Thousand Oaks,United States,California,5402405
Torrance,United States,California,5403022
Tracy,United States,California,5403191
Truckee,United States,California,5403676
Tulare,United States,California,5403783
Turlock,United States,California,5404024
Tustin,United States,California,5404119
North Tustin,United States,California,5404122
Twentynine Palms,United States,California,5404198
Ukiah,United States,California,5404476
Union City,United States,California,5404555
Universal City,United States,California,5404794
Upland,United States,California,5404915
Walnut Park,United States,California,5407030
Watsonville,United States,California,5407529
West Carson,United States,California,5407908
West Covina,United States,California,5407933
West Hollywood,United States,California,5408076
West Puente Valley,United States,California,5408191
West Sacramento,United States,California,5408211
Westminster,United States,California,5408406
Westmont,United States,California,5408431
Whittier,United States,California,5409059
Wildomar,United States,California,5409260
Willowbrook,United States,California,5409768
Windsor,United States,California,5410004
Winter Gardens,United States,California,5410129
Woodland,United States,California,5410430
Woodland Hills,United States,California,5410438
Yorba Linda,United States,California,5410902
Yuba City,United States,California,5411015
Yucaipa,United States,California,5411046
Yucca Valley,United States,California,5411079
Arvada,United States,Colorado,5412199
Aurora,United States,Colorado,5412347
Brighton,United States,Colorado,5414941
Broomfield,United States,Colorado,5415035
CaÃ±on City,United States,Colorado,5416005
Castle Rock,United States,Colorado,5416329
Castlewood,United States,Colorado,5416357
Centennial,United States,Colorado,5416541
Cimarron Hills,United States,Colorado,5417041
Clifton,United States,Colorado,5417258
Colorado Springs,United States,Colorado,5417598
Columbine,United States,Colorado,5417657
Commerce City,United States,Colorado,5417737
Denver,United States,Colorado,5419384
Durango,United States,Colorado,5420241
Englewood,United States,Colorado,5421250
Fountain,United States,Colorado,5422191
Golden,United States,Colorado,5423294
Grand Junction,United States,Colorado,5423573
Highlands Ranch,United States,Colorado,5425043
Ken Caryl,United States,Colorado,5427207
Lafayette,United States,Colorado,5427771
Lakewood,United States,Colorado,5427946
Littleton,United States,Colorado,5429032
Louisville,United States,Colorado,5429522
Montrose,United States,Colorado,5431710
Northglenn,United States,Colorado,5433124
Parker,United States,Colorado,5434006
Pueblo,United States,Colorado,5435464
Pueblo West,United States,Colorado,5435477
Sherrelwood,United States,Colorado,5438567
Southglenn,United States,Colorado,5439752
Thornton,United States,Colorado,5441492
Westminster,United States,Colorado,5443910
Wheat Ridge,United States,Colorado,5443948
Dodge City,United States,Kansas,5445298
Garden City,United States,Kansas,5445439
Liberal,United States,Kansas,5445820
Alamogordo,United States,New Mexico,5454627
Albuquerque,United States,New Mexico,5454711
Carlsbad,United States,New Mexico,5460459
Clovis,United States,New Mexico,5462393
Farmington,United States,New Mexico,5467328
Gallup,United States,New Mexico,5468773
Hobbs,United States,New Mexico,5471578
Las Cruces,United States,New Mexico,5475352
Rio Rancho,United States,New Mexico,5487811
Roswell,United States,New Mexico,5488441
Santa Fe,United States,New Mexico,5490263
South Valley,United States,New Mexico,5492450
Boulder City,United States,Nevada,5500539
Carson City,United States,Nevada,5501344
Enterprise,United States,Nevada,5503766
Fernley,United States,Nevada,5504003
Henderson,United States,Nevada,5505411
Las Vegas,United States,Nevada,5506956
Mesquite,United States,Nevada,5508180
North Las Vegas,United States,Nevada,5509403
Pahrump,United States,Nevada,5509851
Paradise,United States,Nevada,5509952
Reno,United States,Nevada,5511077
Spanish Springs,United States,Nevada,5512827
Sparks,United States,Nevada,5512862
Spring Valley,United States,Nevada,5512909
Sun Valley,United States,Nevada,5513307
Sunrise Manor,United States,Nevada,5513343
Whitney,United States,Nevada,5515110
Winchester,United States,Nevada,5515345
Amarillo,United States,Texas,5516233
Big Spring,United States,Texas,5517061
Del Rio,United States,Texas,5520076
Eagle Pass,United States,Texas,5520677
El Paso,United States,Texas,5520993
Hereford,United States,Texas,5523074
Horizon City,United States,Texas,5523369
Lubbock,United States,Texas,5525577
Midland,United States,Texas,5526337
Odessa,United States,Texas,5527554
Pampa,United States,Texas,5527953
Plainview,United States,Texas,5528450
San Angelo,United States,Texas,5530022
Socorro,United States,Texas,5530932
Socorro Mission Number 1 Colonia,United States,Texas,5530937
West Odessa,United States,Texas,5533366
Cedar City,United States,Utah,5536630
Saint George,United States,Utah,5546220
Washington,United States,Utah,5549222
Wasco,United States,California,5550368
Anthem,United States,Arizona,5551498
Apache Junction,United States,Arizona,5551535
Avondale,United States,Arizona,5552301
Juneau,United States,Alaska,5554072
Arcata,United States,California,5558953
Bayside,United States,California,5559320
Eureka,United States,California,5563397
McKinleyville,United States,California,5567770
Redding,United States,California,5570160
Susanville,United States,California,5572400
Boulder,United States,Colorado,5574991
Erie,United States,Colorado,5576859
Evans,United States,Colorado,5576909
Fort Collins,United States,Colorado,5577147
Greeley,United States,Colorado,5577592
Longmont,United States,Colorado,5579276
Loveland,United States,Colorado,5579368
Windsor,United States,Colorado,5583509
Boise,United States,Idaho,5586437
Caldwell,United States,Idaho,5587698
Coeur d'Alene,United States,Idaho,5589173
Eagle,United States,Idaho,5591778
Idaho Falls,United States,Idaho,5596475
Kuna,United States,Idaho,5597955
Lewiston,United States,Idaho,5598538
Lewiston Orchards,United States,Idaho,5598542
Meridian,United States,Idaho,5600685
Moscow,United States,Idaho,5601538
Nampa,United States,Idaho,5601933
Pocatello,United States,Idaho,5604045
Post Falls,United States,Idaho,5604353
Rexburg,United States,Idaho,5605242
Twin Falls,United States,Idaho,5610810
Billings,United States,Montana,5640350
Bozeman,United States,Montana,5641727
Butte,United States,Montana,5642934
Great Falls,United States,Montana,5655240
Helena,United States,Montana,5656882
Kalispell,United States,Montana,5660340
Missoula,United States,Montana,5666639
Bismarck,United States,North Dakota,5688025
Dickinson,United States,North Dakota,5688789
Mandan,United States,North Dakota,5690366
Minot,United States,North Dakota,5690532
North Platte,United States,Nebraska,5697939
Scottsbluff,United States,Nebraska,5699404
Elko,United States,Nevada,5703670
Albany,United States,Oregon,5710756
Aloha,United States,Oregon,5711099
Altamont,United States,Oregon,5711149
Ashland,United States,Oregon,5711789
Beaverton,United States,Oregon,5713376
Bend,United States,Oregon,5713587
Bethany,United States,Oregon,5713759
Canby,United States,Oregon,5717758
Central Point,United States,Oregon,5718601
Coos Bay,United States,Oregon,5720495
Corvallis,United States,Oregon,5720727
Eugene,United States,Oregon,5725846
Forest Grove,United States,Oregon,5727190
Four Corners,United States,Oregon,5727382
Grants Pass,United States,Oregon,5729080
Gresham,United States,Oregon,5729485
Hayesville,United States,Oregon,5730675
Hermiston,United States,Oregon,5731070
Hillsboro,United States,Oregon,5731371
Keizer,United States,Oregon,5734711
Klamath Falls,United States,Oregon,5735238
Lake Oswego,United States,Oregon,5735724
Lebanon,United States,Oregon,5736218
Lents,United States,Oregon,5736378
McMinnville,United States,Oregon,5739936
Medford,United States,Oregon,5740099
Milwaukie,United States,Oregon,5740900
Newberg,United States,Oregon,5742726
Oak Grove,United States,Oregon,5743731
Oregon City,United States,Oregon,5744253
Pendleton,United States,Oregon,5745380
Portland,United States,Oregon,5746545
Redmond,United States,Oregon,5747882
Roseburg,United States,Oregon,5749352
Salem,United States,Oregon,5750162
Sherwood,United States,Oregon,5751632
Springfield,United States,Oregon,5754005
Tigard,United States,Oregon,5756758
Troutdale,United States,Oregon,5757477
Tualatin,United States,Oregon,5757506
West Linn,United States,Oregon,5760009
Wilsonville,United States,Oregon,5761287
Woodburn,United States,Oregon,5761708
Rapid City,United States,South Dakota,5768233
Bountiful,United States,Utah,5771826
Brigham City,United States,Utah,5771960
Centerville,United States,Utah,5772654
Clearfield,United States,Utah,5772959
Clinton,United States,Utah,5773001
Cottonwood Heights,United States,Utah,5773304
Draper,United States,Utah,5774001
Eagle Mountain,United States,Utah,5774215
East Millcreek,United States,Utah,5774301
Farmington,United States,Utah,5774662
Herriman,United States,Utah,5775782
Highland,United States,Utah,5775863
Holladay,United States,Utah,5776008
Kaysville,United States,Utah,5776715
Kearns,United States,Utah,5776727
Layton,United States,Utah,5777107
Lehi,United States,Utah,5777224
Logan,United States,Utah,5777544
Magna,United States,Utah,5777793
Midvale,United States,Utah,5778244
Millcreek,United States,Utah,5778352
Murray,United States,Utah,5778755
North Ogden,United States,Utah,5779036
North Salt Lake,United States,Utah,5779068
Ogden,United States,Utah,5779206
Orem,United States,Utah,5779334
Payson,United States,Utah,5779548
Pleasant Grove,United States,Utah,5779816
Provo,United States,Utah,5780026
Riverton,United States,Utah,5780557
Roy,United States,Utah,5780802
Salt Lake City,United States,Utah,5780993
Sandy City,United States,Utah,5781061
Sandy Hills,United States,Utah,5781070
Saratoga Springs,United States,Utah,5781087
South Jordan Heights,United States,Utah,5781765
South Jordan,United States,Utah,5781770
South Ogden,United States,Utah,5781783
South Salt Lake,United States,Utah,5781794
Spanish Fork,United States,Utah,5781860
Springville,United States,Utah,5781993
Syracuse,United States,Utah,5782391
Taylorsville,United States,Utah,5782476
Tooele,United States,Utah,5783695
West Jordan,United States,Utah,5784549
West Valley City,United States,Utah,5784607
Aberdeen,United States,Washington,5785243
Anacortes,United States,Washington,5785657
Arlington,United States,Washington,5785868
Auburn,United States,Washington,5785965
Battle Ground,United States,Washington,5786485
Bellevue,United States,Washington,5786882
Bellingham,United States,Washington,5786899
Bonney Lake,United States,Washington,5787776
Bothell,United States,Washington,5787829
Bremerton,United States,Washington,5788054
Burien,United States,Washington,5788516
Camas,United States,Washington,5788822
Centralia,United States,Washington,5789683
Cottage Lake,United States,Washington,5790971
Covington,United States,Washington,5791159
Des Moines,United States,Washington,5792244
Edmonds,United States,Washington,5793427
Ellensburg,United States,Washington,5793639
Everett,United States,Washington,5793933
Fairwood,United States,Washington,5794097
Federal Way,United States,Washington,5794245
Five Corners,United States,Washington,5794559
Frederickson,United States,Washington,5795011
Graham,United States,Washington,5795906
Hazel Dell,United States,Washington,5796984
Issaquah,United States,Washington,5798487
Kenmore,United States,Washington,5799587
Kennewick,United States,Washington,5799610
Kent,United States,Washington,5799625
Kirkland,United States,Washington,5799841
Lacey,United States,Washington,5800112
Lake Stevens,United States,Washington,5800317
Lakewood,United States,Washington,5800420
Longview,United States,Washington,5801617
Lynnwood,United States,Washington,5802049
Maple Valley,United States,Washington,5802340
Martha Lake,United States,Washington,5802493
Marysville,United States,Washington,5802570
Mercer Island,United States,Washington,5803139
Mill Creek,United States,Washington,5803457
Monroe,United States,Washington,5803786
Moses Lake,United States,Washington,5803990
Mount Vernon,United States,Washington,5804127
Mountlake Terrace,United States,Washington,5804191
Mukilteo,United States,Washington,5804306
North Creek,United States,Washington,5804953
Oak Harbor,United States,Washington,5805441
Olympia,United States,Washington,5805687
Opportunity,United States,Washington,5805782
Orchards,United States,Washington,5805815
Parkland,United States,Washington,5806253
Pasco,United States,Washington,5806298
Port Angeles,United States,Washington,5807212
Pullman,United States,Washington,5807540
Puyallup,United States,Washington,5807575
Redmond,United States,Washington,5808079
Renton,United States,Washington,5808189
Richland,United States,Washington,5808276
Salmon Creek,United States,Washington,5809333
Sammamish,United States,Washington,5809402
SeaTac,United States,Washington,5809805
Seattle,United States,Washington,5809844
Shoreline,United States,Washington,5810301
Silverdale,United States,Washington,5810490
South Hill,United States,Washington,5811456
Spanaway,United States,Washington,5811581
Spokane,United States,Washington,5811696
Spokane Valley,United States,Washington,5811729
Sunnyside,United States,Washington,5812604
Tacoma,United States,Washington,5812944
Tukwila,United States,Washington,5814043
Tumwater,United States,Washington,5814095
University Place,United States,Washington,5814450
Vancouver,United States,Washington,5814616
Walla Walla,United States,Washington,5814916
Wenatchee,United States,Washington,5815342
West Lake Sammamish,United States,Washington,5815538
West Lake Stevens,United States,Washington,5815539
Bainbridge Island,United States,Washington,5816320
Yakima,United States,Washington,5816605
Casper,United States,Wyoming,5820705
Cheyenne,United States,Wyoming,5821086
Gillette,United States,Wyoming,5826027
Laramie,United States,Wyoming,5830062
Rock Springs,United States,Wyoming,5836898
Sheridan,United States,Wyoming,5838198
American Fork,United States,Utah,5844096
Kahului,United States,Hawaii,5847411
Kailua,United States,Hawaii,5847486
KÄneâ€˜ohe,United States,Hawaii,5848189
KÄ«hei,United States,Hawaii,5849297
Makakilo City,United States,Hawaii,5850554
Mililani Town,United States,Hawaii,5851030
Pearl City,United States,Hawaii,5852275
WahiawÄ,United States,Hawaii,5853992
Wailuku,United States,Hawaii,5854496
Waipahu,United States,Hawaii,5854686
â€˜Ewa Gentry,United States,Hawaii,5855070
Hilo,United States,Hawaii,5855927
Honolulu,United States,Hawaii,5856195
Eagle River,United States,Alaska,5861187
Fairbanks,United States,Alaska,5861897
Anchorage,United States,Alaska,5879400
Badger,United States,Alaska,5879898
Milton,United States,Georgia,6331908
Johns Creek,United States,Georgia,6331909
Cutler Bay,United States,Florida,6332309
Alafaya,United States,Florida,6332439
Fort Bragg,United States,North Carolina,6941080
City of Milford (balance),United States,Connecticut,7160204
Butte-Silver Bow (Balance),United States,Montana,7172886
City of Sammamish,United States,Washington,7174365
Silver Firs,United States,Washington,7176035
Vineyard,United States,California,7176039
Wallingford Center,United States,Connecticut,7257422
Bel Air North,United States,Maryland,7257991
Bel Air South,United States,Maryland,7257992
Setauket-East Setauket,United States,New York,7258965
Tonawanda,United States,New York,7259084
Fort Leonard Wood,United States,Missouri,7259265
West Bloomfield Township,United States,Michigan,7259621
East Lake-Orient Park,United States,Florida,7259705
Four Corners,United States,Florida,7259780
Greater Northdale,United States,Florida,7259823
Candler-McAfee,United States,Georgia,7260019
University,United States,Florida,7260219
Vero Beach South,United States,Florida,7260233
Kendall West,United States,Florida,7260327
Palm River-Clair Mel,United States,Florida,7260548
Arden-Arcade,United States,California,7260806
Bryn Mawr-Skyway,United States,Washington,7260966
Casa de Oro-Mount Helix,United States,California,7261029
Florence-Graham,United States,California,7261268
Fort Hood,United States,Texas,7261291
Inglewood-Finn Hill,United States,Washington,7261476
La Crescenta-Montrose,United States,California,7261553
East Hill-Meridian,United States,Washington,7261759
Security-Widefield,United States,Colorado,7262349
Union Hill-Novelty Hill,United States,Washington,7262428
West Whittier-Los Nietos,United States,California,7262518
Summerlin South,United States,Nevada,7262622
Makakilo,United States,Hawaii,7262761
Schofield Barracks,United States,Hawaii,7262790
San Tan Valley,United States,Arizona,7310164
Enchanted Hills,United States,New Mexico,7839240
West Hills,United States,California,8030162
Oak Hill,United States,Virginia,8097131
Bridgewater,United States,New Jersey,8299576
Warren Township,United States,New Jersey,8299577
Fairfield Heights,United States,Indiana,8347326
Randolph,United States,New Jersey,8469295
Hot Springs National Park,United States,Arkansas,8605040
Dixiana,United States,Alabama,8605041
Cranberry Township,United States,Pennsylvania,8643098
Silver Lake,United States,California,10104153
Echo Park,United States,California,10104154
Young,Uruguay,RÃ­o Negro,3439525
Trinidad,Uruguay,Flores,3439748
Trinidad,Uruguay,Flores,3439749
Treinta y Tres,Uruguay,Treinta y Tres,3439781
TacuarembÃ³,Uruguay,TacuarembÃ³,3440034
Santa LucÃ­a,Uruguay,Canelones,3440571
San JosÃ© de Mayo,Uruguay,San JosÃ©,3440639
San Carlos,Uruguay,Maldonado,3440696
Salto,Uruguay,Salto,3440714
Rocha,Uruguay,Rocha,3440777
Rivera,Uruguay,Rivera,3440781
Progreso,Uruguay,Canelones,3440963
PaysandÃº,Uruguay,PaysandÃº,3441243
Paso de Carrasco,Uruguay,Canelones,3441292
Pando,Uruguay,Canelones,3441354
Montevideo,Uruguay,Montevideo,3441575
Minas,Uruguay,Lavalleja,3441665
Mercedes,Uruguay,Soriano,3441684
Melo,Uruguay,Cerro Largo,3441702
Maldonado,Uruguay,Maldonado,3441894
Las Piedras,Uruguay,Canelones,3442057
La Paz,Uruguay,Canelones,3442098
Fray Bentos,Uruguay,RÃ­o Negro,3442568
Florida,Uruguay,Florida,3442585
Durazno,Uruguay,Durazno,3442727
Dolores,Uruguay,Soriano,3442750
Delta del Tigre,Uruguay,San JosÃ©,3442778
Colonia del Sacramento,Uruguay,Colonia,3443013
Carmelo,Uruguay,Colonia,3443341
Canelones,Uruguay,Canelones,3443413
Artigas,Uruguay,Artigas,3443758
Nukus,Uzbekistan,Karakalpakstan,601294
KhÅ­jayli,Uzbekistan,Karakalpakstan,601339
Oltinkoâ€™l,Uzbekistan,Karakalpakstan,601417
Zomin,Uzbekistan,Jizzax,1215694
Urgut,Uzbekistan,Samarqand,1215839
Tirmiz,Uzbekistan,Surxondaryo,1215957
Shoâ€™rchi,Uzbekistan,Surxondaryo,1216115
Shahrisabz,Uzbekistan,Qashqadaryo,1216187
Samarqand,Uzbekistan,Samarqand,1216265
Qarshi,Uzbekistan,Qashqadaryo,1216311
Muborak,Uzbekistan,Qashqadaryo,1216475
Kitob,Uzbekistan,Qashqadaryo,1216787
Kattaqoâ€™rgâ€™on,Uzbekistan,Samarqand,1216982
Koson,Uzbekistan,Qashqadaryo,1217007
Karakulâ€™,Uzbekistan,Bukhara,1217084
Kogon,Uzbekistan,Bukhara,1217180
Gâ€™uzor,Uzbekistan,Qashqadaryo,1217262
Galaosiyo,Uzbekistan,Bukhara,1217340
Juma,Uzbekistan,Samarqand,1217362
Denov,Uzbekistan,Surxondaryo,1217474
Chiroqchi,Uzbekistan,Qashqadaryo,1217540
Chelak,Uzbekistan,Samarqand,1217569
Bulungâ€™ur,Uzbekistan,Samarqand,1217658
Bukhara,Uzbekistan,Bukhara,1217662
Beshkent,Uzbekistan,Qashqadaryo,1217703
Boysun,Uzbekistan,Surxondaryo,1217734
Oqtosh,Uzbekistan,Samarqand,1217926
Zafar,Uzbekistan,Toshkent,1512287
Yaypan,Uzbekistan,Fergana,1512320
YangiyÅ­l,Uzbekistan,Toshkent,1512339
Yangiyer,Uzbekistan,Sirdaryo,1512342
Yangirabot,Uzbekistan,Navoiy,1512348
Yangiqoâ€˜rgâ€˜on,Uzbekistan,Namangan,1512350
Yangiobod,Uzbekistan,Toshkent,1512372
Wobkent,Uzbekistan,Bukhara,1512423
Uychi,Uzbekistan,Namangan,1512449
Urganch,Uzbekistan,Xorazm,1512473
Dashtobod,Uzbekistan,Jizzax,1512480
UchqÅ­rghon Shahri,Uzbekistan,Namangan,1512501
TÅ­ytepa,Uzbekistan,Toshkent,1512524
TÅ­ragÅ­rghon,Uzbekistan,Namangan,1512549
Toshloq,Uzbekistan,Fergana,1512568
Tashkent,Uzbekistan,Toshkent Shahri,1512569
Toshbuloq,Uzbekistan,Namangan,1512658
Sirdaryo,Uzbekistan,Sirdaryo,1512770
Showot,Uzbekistan,Xorazm,1512790
Shofirkon,Uzbekistan,Bukhara,1512838
Salor,Uzbekistan,Toshkent,1512934
QÅ­shkÅ­pir,Uzbekistan,Xorazm,1512978
Qoâ€˜qon,Uzbekistan,Fergana,1512979
Piskent,Uzbekistan,Toshkent,1512986
Payshanba,Uzbekistan,Samarqand,1513011
Parkent,Uzbekistan,Toshkent,1513017
Pop,Uzbekistan,Namangan,1513023
Paxtakor,Uzbekistan,Jizzax,1513038
Olmaliq,Uzbekistan,Toshkent,1513064
Ohangaron,Uzbekistan,Toshkent,1513072
Nurota,Uzbekistan,Navoiy,1513087
Novyy Turtkulâ€™,Uzbekistan,Karakalpakstan,1513092
Navoiy,Uzbekistan,Navoiy,1513131
Namangan,Uzbekistan,Namangan,1513157
Margâ€˜ilon,Uzbekistan,Fergana,1513243
Manghit,Uzbekistan,Karakalpakstan,1513245
Asaka,Uzbekistan,Andijon,1513271
Quvasoy,Uzbekistan,Fergana,1513331
QÅ­rghontepa,Uzbekistan,Andijon,1513364
Kirguli,Uzbekistan,Fergana,1513555
Qibray,Uzbekistan,Toshkent,1513567
KhÅ­jaobod,Uzbekistan,Andijon,1513600
Khiwa,Uzbekistan,Xorazm,1513604
Haqqulobod,Uzbekistan,Namangan,1513655
Kosonsoy,Uzbekistan,Namangan,1513714
Jizzax,Uzbekistan,Jizzax,1513886
Iskandar,Uzbekistan,Toshkent,1513900
Hazorasp,Uzbekistan,Xorazm,1513957
Gurlan,Uzbekistan,Xorazm,1513962
Guliston,Uzbekistan,Sirdaryo,1513966
Ghijduwon,Uzbekistan,Bukhara,1513983
Gâ€˜azalkent,Uzbekistan,Toshkent,1513996
Gagarin,Uzbekistan,Jizzax,1514011
Fergana,Uzbekistan,Fergana,1514019
DÅ­stlik,Uzbekistan,Jizzax,1514125
Chust Shahri,Uzbekistan,Namangan,1514192
Chirchiq,Uzbekistan,Toshkent,1514210
Chinoz,Uzbekistan,Toshkent,1514215
Chortoq,Uzbekistan,Namangan,1514258
BÅ­ka,Uzbekistan,Toshkent,1514330
Beshariq,Uzbekistan,Fergana,1514382
Beruniy,Uzbekistan,Karakalpakstan,1514387
Bektemir,Uzbekistan,Toshkent Shahri,1514396
Bekobod,Uzbekistan,Toshkent,1514402
Angren,Uzbekistan,Toshkent,1514581
Andijon,Uzbekistan,Andijon,1514588
Oltiariq,Uzbekistan,Fergana,1514615
Quva,Uzbekistan,Fergana,1526979
Navoiy,Uzbekistan,Navoiy,1538229
Vatican City,Vatican,N/A,6691831
Kingstown,Saint Vincent and the Grenadines,Saint George,3577887
Kingstown Park,Saint Vincent and the Grenadines,Saint George,3748726
La AsunciÃ³n,Venezuela,Nueva Esparta,3480908
Anaco,Venezuela,AnzoÃ¡tegui,3486270
Alto Barinas,Venezuela,Barinas,3487903
Zaraza,Venezuela,GuÃ¡rico,3625066
Yaritagua,Venezuela,Yaracuy,3625207
Villa de Cura,Venezuela,Aragua,3625341
Villa Bruzual,Venezuela,Portuguesa,3625346
Valle de La Pascua,Venezuela,GuÃ¡rico,3625515
Valera,Venezuela,Trujillo,3625542
Valencia,Venezuela,Carabobo,3625549
Upata,Venezuela,BolÃ­var,3625710
Turmero,Venezuela,Aragua,3625829
Tucupita,Venezuela,Delta Amacuro,3625929
Trujillo,Venezuela,Trujillo,3625979
Tinaquillo,Venezuela,Cojedes,3626219
TÃ¡riba,Venezuela,TÃ¡chira,3626402
Santa Teresa,Venezuela,Miranda,3627047
Santa Rita,Venezuela,Zulia,3627186
Santa Elena de UairÃ©n,Venezuela,BolÃ­var,3627382
San Mateo,Venezuela,Aragua,3627968
San Juan de los Morros,Venezuela,GuÃ¡rico,3628053
San Juan de ColÃ³n,Venezuela,TÃ¡chira,3628060
San JosÃ© de Guanipa,Venezuela,AnzoÃ¡tegui,3628142
San JoaquÃ­n,Venezuela,Carabobo,3628267
San Felipe,Venezuela,Yaracuy,3628423
San CristÃ³bal,Venezuela,TÃ¡chira,3628473
San Carlos del Zulia,Venezuela,Zulia,3628489
San Carlos,Venezuela,Cojedes,3628503
San Antonio del TÃ¡chira,Venezuela,TÃ¡chira,3628549
San Antonio de Los Altos,Venezuela,Miranda,3628550
Rubio,Venezuela,TÃ¡chira,3628952
La Villa del Rosario,Venezuela,Zulia,3628966
QuÃ­bor,Venezuela,Lara,3629419
Punto Fijo,Venezuela,FalcÃ³n,3629576
Punta CardÃ³n,Venezuela,FalcÃ³n,3629614
Puerto La Cruz,Venezuela,AnzoÃ¡tegui,3629672
Puerto Cabello,Venezuela,Carabobo,3629706
Puerto Ayacucho,Venezuela,Amazonas,3629710
Porlamar,Venezuela,Nueva Esparta,3629965
Petare,Venezuela,Miranda,3630297
Palo Negro,Venezuela,Aragua,3630932
Ocumare del Tuy,Venezuela,Miranda,3631412
Nirgua,Venezuela,Yaracuy,3631507
Mucumpiz,Venezuela,MÃ©rida,3631741
MorÃ³n,Venezuela,Carabobo,3631878
MÃ©rida,Venezuela,MÃ©rida,3632308
Mariara,Venezuela,Carabobo,3632929
Maracay,Venezuela,Aragua,3632998
Maracaibo,Venezuela,Zulia,3633009
MaiquetÃ­a,Venezuela,Vargas,3633341
Machiques,Venezuela,Zulia,3633444
Los Teques,Venezuela,Miranda,3633622
Los Rastrojos,Venezuela,Lara,3633677
Los Dos Caminos,Venezuela,Miranda,3634184
La Victoria,Venezuela,Aragua,3634922
Las TejerÃ­as,Venezuela,Aragua,3635325
Lagunillas,Venezuela,Zulia,3637623
La Guaira,Venezuela,Vargas,3637721
Juan Griego,Venezuela,Nueva Esparta,3639107
GÃ¼iria,Venezuela,Sucre,3639725
GÃ¼igÃ¼e,Venezuela,Carabobo,3639747
Guatire,Venezuela,Miranda,3639898
Guarenas,Venezuela,Miranda,3640049
Guanare,Venezuela,Portuguesa,3640226
Guacara,Venezuela,Carabobo,3640465
El VigÃ­a,Venezuela,MÃ©rida,3641099
El Tocuyo,Venezuela,Lara,3641275
El Tigre,Venezuela,AnzoÃ¡tegui,3641351
El LimÃ³n,Venezuela,Aragua,3642833
El Hatillo,Venezuela,Miranda,3643031
Ejido,Venezuela,MÃ©rida,3644417
CumanÃ¡,Venezuela,Sucre,3644768
CÃºa,Venezuela,Miranda,3644918
Coro,Venezuela,FalcÃ³n,3645213
Ciudad Guayana,Venezuela,BolÃ­var,3645528
Ciudad BolÃ­var,Venezuela,BolÃ­var,3645532
Chivacoa,Venezuela,Yaracuy,3645671
Charallave,Venezuela,Miranda,3645854
Chacao,Venezuela,Miranda,3645981
Tacarigua,Venezuela,Carabobo,3646062
CaucagÃ¼ito,Venezuela,Miranda,3646169
Catia La Mar,Venezuela,Vargas,3646190
CarÃºpano,Venezuela,Sucre,3646382
Carrizal,Venezuela,Miranda,3646451
Carora,Venezuela,Lara,3646487
Caracas,Venezuela,Capital,3646738
Caraballeda,Venezuela,Vargas,3646767
Cantaura,Venezuela,AnzoÃ¡tegui,3646869
Calabozo,Venezuela,GuÃ¡rico,3647444
Cagua,Venezuela,Aragua,3647549
Cabimas,Venezuela,Zulia,3647651
Baruta,Venezuela,Miranda,3648439
Barquisimeto,Venezuela,Lara,3648522
Barinitas,Venezuela,Barinas,3648540
Barinas,Venezuela,Barinas,3648546
Barcelona,Venezuela,AnzoÃ¡tegui,3648559
Araure,Venezuela,Portuguesa,3649017
Altagracia de Orituco,Venezuela,GuÃ¡rico,3649408
Acarigua,Venezuela,Portuguesa,3649833
MaturÃ­n,Venezuela,Monagas,3778045
La FrÃ­a,Venezuela,TÃ¡chira,3795152
El Cafetal,Venezuela,Miranda,3803449
Caucaguita,Venezuela,Miranda,3803515
La Dolorita,Venezuela,Miranda,3803651
Guasdualito,Venezuela,Apure,3804949
San Fernando de Apure,Venezuela,Apure,3805673
Road Town,British Virgin Islands,N/A,3577430
Tortola,British Virgin Islands,N/A,8533874
Charlotte Amalie,U.S. Virgin Islands,Saint Thomas Island,4795467
Saint Croix,U.S. Virgin Islands,Saint Croix Island,4796512
YÃªn Vinh,Vietnam,Nghá»‡ An,1560037
YÃªn BÃ¡i,Vietnam,YÃªn BÃ¡i,1560349
VÅ©ng TÃ u,Vietnam,BÃ  Rá»‹a-VÅ©ng TÃ u,1562414
Vá»‹ Thanh,Vietnam,Hau Giang,1562538
VÄ©nh YÃªn,Vietnam,VÄ©nh PhÃºc,1562548
VÄ©nh Long,Vietnam,VÄ©nh Long,1562693
Vinh,Vietnam,Nghá»‡ An,1562798
Viá»‡t TrÃ¬,Vietnam,PhÃº Thá»,1562820
ThÃ nh Phá»‘ UÃ´ng BÃ­,Vietnam,Quáº£ng Ninh,1563241
Tuy HÃ²a,Vietnam,PhÃº YÃªn,1563281
ThÃ nh Phá»‘ TuyÃªn Quang,Vietnam,TuyÃªn Quang,1563287
TrÃ  Vinh,Vietnam,TrÃ  Vinh,1563926
Thá»§ Dáº§u Má»™t,Vietnam,BÃ¬nh DÆ°Æ¡ng,1565022
Ho Chi Minh City,Vietnam,Ho Chi Minh City,1566083
Thanh HÃ³a,Vietnam,Thanh HÃ³a,1566166
ThÃ nh Phá»‘ ThÃ¡i NguyÃªn,Vietnam,ThÃ¡i NguyÃªn,1566319
ThÃ nh Phá»‘ ThÃ¡i BÃ¬nh,Vietnam,ThÃ¡i BÃ¬nh,1566346
TÃ¢y Ninh,Vietnam,TÃ¢y Ninh,1566559
TÃ¢n An,Vietnam,Long An,1567069
Tam Ká»³,Vietnam,Quáº£ng Nam,1567148
SÆ¡n TÃ¢y,Vietnam,Ha Ná»™i,1567621
SÆ¡n La,Vietnam,SÆ¡n La,1567681
SÃ´ng Cáº§u,Vietnam,PhÃº YÃªn,1567723
SÃ³c TrÄƒng,Vietnam,SÃ³c TrÄƒng,1567788
Sa PÃ¡,Vietnam,LÃ o Cai,1568043
Sadek,Vietnam,Äá»“ng ThÃ¡p,1568212
Ráº¡ch GiÃ¡,Vietnam,Kiáº¿n Giang,1568510
Qui Nhon,Vietnam,BÃ¬nh Äá»‹nh,1568574
Quáº£ng NgÃ£i,Vietnam,Quáº£ng NgÃ£i,1568770
Pleiku,Vietnam,Gia Lai,1569684
ThÃ nh Phá»‘ Phá»§ LÃ½,Vietnam,HÃ  Nam,1570449
PhÃº KhÆ°Æ¡ng,Vietnam,TÃ¢y Ninh,1570549
Phan Thiáº¿t,Vietnam,BÃ¬nh Thuáº­n,1571058
Phan Rang-ThÃ¡p ChÃ m,Vietnam,Ninh Thuáº­n,1571067
ThÃ nh Phá»‘ Ninh BÃ¬nh,Vietnam,Ninh BÃ¬nh,1571968
Nha Trang,Vietnam,KhÃ¡nh HÃ²a,1572151
ThÃ nh Phá»‘ Nam Äá»‹nh,Vietnam,Nam Äá»‹nh,1573517
Má»¹ Tho,Vietnam,Tiá»n Giang,1574023
MÃ³ng CÃ¡i,Vietnam,Quáº£ng Ninh,1574507
Long XuyÃªn,Vietnam,An Giang,1575627
LÃ o Cai,Vietnam,LÃ o Cai,1576303
ThÃ nh Phá»‘ Láº¡ng SÆ¡n,Vietnam,Láº¡ng SÆ¡n,1576633
La Gi,Vietnam,BÃ¬nh Thuáº­n,1577995
Kon Tum,Vietnam,Kon Tum,1578500
HÆ°ng YÃªn,Vietnam,HÆ°ng YÃªn,1580142
Huáº¿,Vietnam,Thá»«a ThiÃªn-Huáº¿,1580240
ThÃ nh Phá»‘ Háº¡ Long,Vietnam,Quáº£ng Ninh,1580410
Há»™i An,Vietnam,Quáº£ng Nam,1580541
ThÃ nh Phá»‘ HÃ²a BÃ¬nh,Vietnam,HÃ²a BÃ¬nh,1580830
HÃ  TÄ©nh,Vietnam,HÃ  TÄ©nh,1581047
HÃ  TiÃªn,Vietnam,Kiáº¿n Giang,1581052
Hanoi,Vietnam,Ha Ná»™i,1581130
Haiphong,Vietnam,Háº£i PhÃ²ng,1581298
ThÃ nh Phá»‘ Háº£i DÆ°Æ¡ng,Vietnam,Háº£i DÆ°Æ¡ng,1581326
ThÃ nh Phá»‘ HÃ  Giang,Vietnam,HÃ  Giang,1581349
HÃ  ÄÃ´ng,Vietnam,Ha Ná»™i,1581364
Don Luan,Vietnam,BÃ¬nh PhÆ°á»›c,1582436
Kwang Binh,Vietnam,Quáº£ng BÃ¬nh,1582886
ÃÃ´ng HÃ ,Vietnam,Quáº£ng Trá»‹,1582926
Dien Bien Phu,Vietnam,Tá»‰nh Ãiá»‡n BiÃªn,1583477
Da Nang,Vietnam,ÄÃ  Náºµng,1583992
ÃÃ  Láº¡t,Vietnam,LÃ¢m Äá»“ng,1584071
Cá»§ Chi,Vietnam,Ho Chi Minh City,1584661
Cho Dok,Vietnam,An Giang,1585660
CÃ¡t BÃ ,Vietnam,Háº£i PhÃ²ng,1586052
Cao LÃ£nh,Vietnam,Äá»“ng ThÃ¡p,1586151
ThÃ nh Phá»‘ Cao Báº±ng,Vietnam,Cao Báº±ng,1586185
Cáº§n ThÆ¡,Vietnam,Cáº§n ThÆ¡,1586203
Cáº§n Giá»,Vietnam,Ho Chi Minh City,1586288
Cáº§n Giuá»™c,Vietnam,Long An,1586296
Cam Ranh,Vietnam,KhÃ¡nh HÃ²a,1586350
Cáº©m Pháº£ Mines,Vietnam,Quáº£ng Ninh,1586357
CÃ  Mau,Vietnam,CÃ  Mau,1586443
BuÃ´n Ma Thuá»™t,Vietnam,Ãáº¯c Láº¯k,1586896
Bá»‰m SÆ¡n,Vietnam,Thanh HÃ³a,1587919
BiÃªn HÃ²a,Vietnam,Äá»“ng Nai,1587923
Báº¿n Tre,Vietnam,Báº¿n Tre,1587976
Báº£o Lá»™c,Vietnam,LÃ¢m Äá»“ng,1588275
Báº¯c Ninh,Vietnam,Báº¯c Ninh,1591449
ThÃ nh phá»‘ Báº¡c LiÃªu,Vietnam,Báº¡c LiÃªu,1591474
Báº¯c Giang,Vietnam,Báº¯c Giang,1591527
Báº¯c Káº¡n,Vietnam,Báº¯c Káº¡n,1591538
Äinh VÄƒn,Vietnam,LÃ¢m Äá»“ng,8991407
Port-Vila,Vanuatu,Shefa,2135171
Mata-Utu,Wallis and Futuna,Circonscription d'UvÃ©a,4034821
Apia,Samoa,Tuamasaga,4035413
ZveÄan,Kosovo,Mitrovica,783770
Vushtrri,Kosovo,Mitrovica,784097
Vitina,Kosovo,Gjilan,784372
Ferizaj,Kosovo,Ferizaj,784759
Suva Reka,Kosovo,Prizren,785238
Shtime,Kosovo,Ferizaj,785485
Prizren,Kosovo,Prizren,786712
Pristina,Kosovo,Pristina,786714
Podujeva,Kosovo,Pristina,786950
PejÃ«,Kosovo,Pec,787157
Orahovac,Kosovo,Gjakova,787456
LlazicÃ«,Kosovo,Prizren,788470
Leposaviq,Kosovo,Mitrovica,788731
MitrovicÃ«,Kosovo,Mitrovica,789225
Kosovo Polje,Kosovo,Pristina,789228
Istok,Kosovo,Pec,789996
Gjilan,Kosovo,Gjilan,790674
Glogovac,Kosovo,Pristina,790701
Dragash,Kosovo,Prizren,791122
DeÃ§an,Kosovo,Gjakova,791580
GjakovÃ«,Kosovo,Gjakova,791646
ZinjibÄr,Yemen,Abyan,69426
ZabÄ«d,Yemen,Muá¸©ÄfazÌ§at al á¸¨udaydah,69500
YarÄ«m,Yemen,Ibb,69559
Taâ€˜izz,Yemen,Taâ€˜izz,70225
SayyÄn,Yemen,Sanaa,70979
Sanaa,Yemen,Sanaa,71137
Saá¸©ar,Yemen,Sanaa,71273
Sa'dah,Yemen,Åžaâ€˜dah,71334
Ma'rib,Yemen,Maâ€™rib,72968
Laá¸©ij,Yemen,Laá¸©ij,73560
Ibb,Yemen,Ibb,74477
á¸¨ajjah,Yemen,á¸¨ajjah,75337
DhÄ« as SufÄl,Yemen,Ibb,76154
DhamÄr,Yemen,DhamÄr,76184
Bayt al FaqÄ«h,Yemen,Muá¸©ÄfazÌ§at al á¸¨udaydah,76991
BÄjil,Yemen,Muá¸©ÄfazÌ§at al á¸¨udaydah,77408
Ataq,Yemen,Shabwah,77726
â€˜AmrÄn,Yemen,Omran,78428
Al MukallÄ,Yemen,Muá¸©ÄfazÌ§at á¸¨aá¸‘ramawt,78754
Al á¸¨udaydah,Yemen,Muá¸©ÄfazÌ§at al á¸¨udaydah,79415
Al á¸¨azm,Yemen,Al Jawf,79455
Al Bayá¸‘Äâ€™,Yemen,Al Bayá¸‘ÄÊ¼,79836
Aden,Yemen,Aden,415189
Mamoudzou,Mayotte,Mamoudzou,921815
Dzaoudzi,Mayotte,Dzaoudzi,921900
Koungou,Mayotte,Koungou,1090225
Roodepoort,South Africa,Gauteng,936374
Zeerust,South Africa,North-West,937136
Wolmaransstad,South Africa,North-West,938457
White River,South Africa,Mpumalanga,938694
Witbank,South Africa,Mpumalanga,939270
Westonaria,South Africa,Gauteng,940316
Wesselsbron,South Africa,Orange Free State,940424
Welkom,South Africa,Orange Free State,940909
Warrenton,South Africa,Northern Cape,941931
Warmbaths,South Africa,Limpopo,941966
Vryheid,South Africa,KwaZulu-Natal,942470
Vryburg,South Africa,North-West,942511
Volksrust,South Africa,Mpumalanga,943032
Virginia,South Africa,Orange Free State,943882
Viljoenskroon,South Africa,Orange Free State,943960
Vereeniging,South Africa,Gauteng,944385
Vanderbijlpark,South Africa,Gauteng,944986
Upington,South Africa,Northern Cape,945945
Mthatha,South Africa,Eastern Cape,946058
Umkomaas,South Africa,KwaZulu-Natal,946128
Ulundi,South Africa,KwaZulu-Natal,946257
Uitenhage,South Africa,Eastern Cape,946877
Tzaneen,South Africa,Limpopo,946973
Thohoyandou,South Africa,Limpopo,949224
Theunissen,South Africa,Orange Free State,949282
Thaba Nchu,South Africa,Orange Free State,949703
Tembisa,South Africa,Gauteng,949880
Stutterheim,South Africa,Eastern Cape,951650
Stilfontein,South Africa,North-West,952192
Stanger,South Africa,KwaZulu-Natal,952734
Standerton,South Africa,Mpumalanga,952747
Springs,South Africa,Gauteng,952865
Soweto,South Africa,Gauteng,953781
Somerset East,South Africa,Eastern Cape,954161
Siyabuswa,South Africa,Mpumalanga,955313
Senekal,South Africa,Orange Free State,956507
Secunda,South Africa,Mpumalanga,956767
Scottburgh,South Africa,KwaZulu-Natal,956878
Schweizer-Reneke,South Africa,North-West,956907
Sasolburg,South Africa,Orange Free State,957487
Rustenburg,South Africa,North-West,958724
Richmond,South Africa,KwaZulu-Natal,962330
Richards Bay,South Africa,KwaZulu-Natal,962367
Reitz,South Africa,Orange Free State,962847
Randfontein,South Africa,Gauteng,963230
Queenstown,South Africa,Eastern Cape,963516
Queensdale,South Africa,Eastern Cape,963525
Pretoria,South Africa,Gauteng,964137
Mokopane,South Africa,Limpopo,964315
Potchefstroom,South Africa,North-West,964349
Port Shepstone,South Africa,KwaZulu-Natal,964406
Port Elizabeth,South Africa,Eastern Cape,964420
Port Alfred,South Africa,Eastern Cape,964432
Plettenberg Bay,South Africa,Western Cape,964712
Piet Retief,South Africa,Mpumalanga,965241
Polokwane,South Africa,Limpopo,965289
Pietermaritzburg,South Africa,KwaZulu-Natal,965301
Phuthaditjhaba,South Africa,Orange Free State,965401
Phalaborwa,South Africa,Limpopo,965528
Parys,South Africa,Orange Free State,966166
Pampierstad,South Africa,North-West,966380
Oudtshoorn,South Africa,Western Cape,967106
Orkney,South Africa,North-West,967476
Modimolle,South Africa,Limpopo,968665
Nkowakowa,South Africa,Limpopo,970341
Nigel,South Africa,Gauteng,970566
Newcastle,South Africa,KwaZulu-Natal,971421
Nelspruit,South Africa,Mpumalanga,971534
Mpumalanga,South Africa,KwaZulu-Natal,973111
Mpophomeni,South Africa,KwaZulu-Natal,973139
Mossel Bay,South Africa,Western Cape,973709
Mondlo,South Africa,KwaZulu-Natal,974670
Mmabatho,South Africa,North-West,975436
Middelburg,South Africa,Eastern Cape,976358
Middelburg,South Africa,Mpumalanga,976361
Messina,South Africa,Limpopo,976885
Margate,South Africa,KwaZulu-Natal,978895
Mabopane,South Africa,Gauteng,980921
Lydenburg,South Africa,Mpumalanga,981158
Louis Trichardt,South Africa,Limpopo,981827
Lichtenburg,South Africa,North-West,982899
Lebowakgomo,South Africa,Limpopo,984087
Lady Frere,South Africa,Eastern Cape,985011
Ladybrand,South Africa,Orange Free State,985015
Kutloanong,South Africa,Orange Free State,986083
Kruisfontein,South Africa,Eastern Cape,986717
Krugersdorp,South Africa,Gauteng,986822
Kroonstad,South Africa,Orange Free State,986846
Kriel,South Africa,Mpumalanga,987202
Komatipoort,South Africa,Mpumalanga,988290
Kokstad,South Africa,KwaZulu-Natal,988356
Knysna,South Africa,Western Cape,988698
Klerksdorp,South Africa,North-West,989921
Kimberley,South Africa,Northern Cape,990930
Johannesburg,South Africa,Gauteng,993800
Howick,South Africa,KwaZulu-Natal,995202
Hennenman,South Africa,Orange Free State,996918
Hendrina,South Africa,Mpumalanga,996930
Heilbron,South Africa,Orange Free State,997140
Heidelberg,South Africa,Gauteng,997151
Harrismith,South Africa,Orange Free State,997751
Grahamstown,South Africa,Eastern Cape,1000501
Graaff-Reinet,South Africa,Eastern Cape,1000543
Giyani,South Africa,Limpopo,1001860
George,South Africa,Western Cape,1002145
Ga-Rankuwa,South Africa,North-West,1002851
Fort Beaufort,South Africa,Eastern Cape,1003953
Fochville,South Africa,North-West,1004109
eSikhawini,South Africa,KwaZulu-Natal,1005029
Ermelo,South Africa,Mpumalanga,1005125
Empangeni,South Africa,KwaZulu-Natal,1005544
eMbalenhle,South Africa,Mpumalanga,1005646
East London,South Africa,Eastern Cape,1006984
Durban,South Africa,KwaZulu-Natal,1007311
Dundee,South Africa,KwaZulu-Natal,1007400
Duiwelskloof,South Africa,Limpopo,1007514
Driefontein,South Africa,Mpumalanga,1008261
Delmas,South Africa,Mpumalanga,1011031
De Aar,South Africa,Northern Cape,1011632
Cullinan,South Africa,Gauteng,1012413
Cradock,South Africa,Eastern Cape,1012600
Christiana,South Africa,North-West,1013550
Carletonville,South Africa,Gauteng,1014073
Butterworth,South Africa,Eastern Cape,1014489
Bronkhorstspruit,South Africa,Gauteng,1015504
Brits,South Africa,North-West,1015621
Brakpan,South Africa,Gauteng,1016181
Botshabelo,South Africa,Orange Free State,1016670
Bothaville,South Africa,Orange Free State,1016698
Boksburg,South Africa,Gauteng,1017780
Bloemhof,South Africa,North-West,1018673
Bloemfontein,South Africa,Orange Free State,1018725
Bhisho,South Africa,Eastern Cape,1019330
Bethlehem,South Africa,Orange Free State,1019704
Bethal,South Africa,Mpumalanga,1019760
Benoni,South Africa,Gauteng,1020098
Beaufort West,South Africa,Western Cape,1020641
Barberton,South Africa,Mpumalanga,1021086
Ballitoville,South Africa,KwaZulu-Natal,1021360
Balfour,South Africa,Mpumalanga,1021396
Allanridge,South Africa,Orange Free State,1023287
Aliwal North,South Africa,Eastern Cape,1023309
Ekangala,South Africa,Gauteng,1105726
Midrand,South Africa,Gauteng,1105776
Centurion,South Africa,Gauteng,1105777
Worcester,South Africa,Western Cape,3359041
Stellenbosch,South Africa,Western Cape,3361025
Saldanha,South Africa,Western Cape,3361934
Paarl,South Africa,Western Cape,3363094
Malmesbury,South Africa,Western Cape,3364346
Lansdowne,South Africa,Western Cape,3364682
Kraaifontein,South Africa,Western Cape,3365083
Hermanus,South Africa,Western Cape,3366880
Grabouw,South Africa,Western Cape,3367513
Ceres,South Africa,Western Cape,3369129
Cape Town,South Africa,Western Cape,3369157
Atlantis,South Africa,Western Cape,3370352
Rondebosch,South Africa,Western Cape,7302802
Retreat,South Africa,Western Cape,8604596
Diepsloot,South Africa,Gauteng,8764562
Nchelenge,Zambia,Luapula,175499
Mbala,Zambia,Northern,176146
Kawambwa,Zambia,Luapula,176555
Siavonga,Zambia,Southern,898188
Sesheke,Zambia,Western,898905
Samfya,Zambia,Luapula,899274
Petauke,Zambia,Eastern,899825
Ndola,Zambia,Copperbelt,901344
Mumbwa,Zambia,Central,904422
Mufulira,Zambia,Copperbelt,905395
Mpika,Zambia,Northern,905846
Monze,Zambia,Southern,906044
Mongu,Zambia,Western,906054
Mazabuka,Zambia,Southern,907111
Mansa,Zambia,Luapula,907770
Lusaka,Zambia,Lusaka,909137
Luanshya,Zambia,Copperbelt,909863
Livingstone,Zambia,Southern,910111
Kitwe,Zambia,Copperbelt,911148
Kasama,Zambia,Northern,912764
Kapiri Mposhi,Zambia,Central,913029
Kansanshi,Zambia,North-Western,913613
Kalulushi,Zambia,Copperbelt,914959
Kafue,Zambia,Lusaka,915883
Kabwe,Zambia,Central,916095
Choma,Zambia,Southern,917748
Chipata,Zambia,Eastern,918702
Chingola,Zambia,Copperbelt,919009
Chililabombwe,Zambia,Copperbelt,919544
Zvishavane,Zimbabwe,Masvingo,878549
Victoria Falls,Zimbabwe,Matabeleland North,879431
Shurugwi,Zimbabwe,Midlands,881164
Rusape,Zimbabwe,Manicaland,882100
Redcliff,Zimbabwe,Midlands,882599
Norton,Zimbabwe,Mashonaland West,884141
Mutare,Zimbabwe,Manicaland,884979
Masvingo,Zimbabwe,Masvingo,886763
Marondera,Zimbabwe,Mashonaland East,886990
Kwekwe,Zimbabwe,Midlands,888710
Karoi,Zimbabwe,Mashonaland West,889191
Kariba,Zimbabwe,Mashonaland West,889215
Kadoma,Zimbabwe,Mashonaland West,889453
Hwange,Zimbabwe,Matabeleland North,889942
Harare,Zimbabwe,Harare,890299
Gweru,Zimbabwe,Midlands,890422
Gokwe,Zimbabwe,Midlands,890983
Chiredzi,Zimbabwe,Masvingo,893485
Chipinge,Zimbabwe,Manicaland,893549
Chinhoyi,Zimbabwe,Mashonaland West,893697
Chegutu,Zimbabwe,Mashonaland West,894239
Bulawayo,Zimbabwe,Bulawayo,894701
Bindura,Zimbabwe,Mashonaland Central,895061
Beitbridge,Zimbabwe,Matabeleland South,895269
Epworth,Zimbabwe,Harare,1085510
Chitungwiza,Zimbabwe,Harare,1106542
'''
# cityList(text)