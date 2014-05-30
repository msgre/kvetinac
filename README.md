# O co jde

[Dobrodružství v květináči](http://kvetinac.tkalci.cz/) je projekt, s pomocí
kterého děcka základní školy (a nejen ty) sledují růst hrachu. Přes den v rámci
běžné výuky se o rostlinu starají, odpoledne, večer či o víkendu pak přes
internet sledují její aktuální stav.

V principu jde o jednoduchý přístroj, který si můžete sami vyrobit a následně
využít k realizaci obdobného projektu.

![Takhle rostl hrášek v 3.B ZŠ Žerotínovy z ValMezu](https://raw.github.com/msgre/kvetinac/master/docs/img/timelapse.gif)


## Technické řešení

![Heblo par excellence](https://raw.github.com/msgre/kvetinac/master/docs/img/heblo.jpg)

Poblíž rostliny je umístěn malý počítač Raspberry Pi vybavený webovou kamerou,
který každých 10 minut pořídí snímek hrachu. Focení probíhá nepřetržitě celých
24 hodin. V noci, když je nedostatek okolního světla, se rostlina přisvětluje
externí lampičkou (před pořízením snímku se zapne, po vyfocení zase vypne).

## Podpůrný web

Samotné focení by děcka rychle omrzelo. Měly by možná zážitek se zprovozněním
aparátu, pak by ale musely 2-3 týdny čekat než by se s fotkama dál něco
udělalo. Rozhodl jsem se proto doplnit Raspberry jednoduchým webem a udělat z
růstu hrášku malou reality show.

![Webová reality show](https://raw.github.com/msgre/kvetinac/master/docs/img/web.png)

Raspberry je připojeno do sítě a každých 10 minut posílá na web aktuální fotku
společně s informaci o celkovém počtu již nasnímaných obrázků. Kromě toho
každou hodinu seskládá krátkou animaci dokumentující vývoj růstu za posledních
24 hodin (tj. pokud se na web podívám ve 14 hodin, uvidím události od
včerejších 14 hodin do dnešních 14 hodin).

Součástí webu je i jednoduché fórum, ve kterém děti můžou kytku povzbuzovat.

## Video

Z nafocených snímků následně vznikne
[časosběrné](http://cs.wikipedia.org/wiki/%C4%8Casosb%C4%9Br) video, které bude
atraktivním způsobem dokumentovat celý růst rostliny. Každý den Raspberry
nafotí 144 snímků. Úměrně k délce sledování pak vznikne krátký film (při
dvoutýdenním snímání o délce 1:20, při třítýdenním 2:00).

Při domácích pokusech jsme natočili růst [rostlinky
rajčete](http://youtu.be/Uoc0VKTS82I) a [odkvétání
tulipánu](http://youtu.be/WhbXkk_aydg) (oboje ještě bez lampičky, snímané pouze
v denních časech).


# Software

Aby vše fungovalo jak má, je třeba Raspberry naučit fotit a zprovoznit web
(ten přímo nutný není, je to s ním ale větší sranda).

V adresáři `kv_pi` je sada skriptů, která se stará o pořizování fotek,
generováni animovaného GIFu a odesílání dat na podpůrný server.

V adresáři `kv_web` je kód webové aplikace napsané ve frameworku Django,
který se stará o příjem dat z Raspberry a o jejich následnou prezentaci
ve formě jednoduché webové stránky.

*Podrobnější dokumentace jak obě SW řešení zprovoznit bude doplněn později.*


# Dotazy

### Co je to Raspberry Pi?

[Malý a levný počítač o velikosti platební
karty](http://cs.wikipedia.org/wiki/Raspberry_Pi). Pokud k Raspberry připojíte
klasické periferie (monitor, klávesnici, myš, externí disk), můžete jej
využívat jako normální počítač (sice s nijak ohromujícím výkonem, ale plně
funkční).

Z Raspberry ale čouhá několik drátů, ke kterým s trochou šikovnosti můžete
připojit kde co. V případě našeho projektu jsme jej doplnili webovou kamerou
a jednoduchou elektronikou, která ve večerních hodinách spíná externí lampičku.

### Kolik to stálo?

Raspberry Pi (model B) stojí přibližně 850 Kč, kamerový modul kolem 700 Kč.
Pro napájení je použitá nabíječka mobilních telefonů (cca 250 Kč). Raspberry
pro své fungování potřebuje SD kartu o velikosti minimálně 4 GB (cca 100 Kč).
Elektronika pro spínání externího světla vyšla na cca 100 Kč.

Celkem si tedy připravte něco okolo 2000 Kč. Je ale docela možné, že některá z
komponent se vám povaluje doma (nabíječka, stará SD karta z telefonu či
foťáku, LED baterka, apod.) a dostanete se tak na nižší náklady.

*Přibližné ceny v květnu 2014.*

### Dal by se projekt využít i jinak?

Určitě! V principu nejde o nic jiného než o dlouhodobé a pravidelné pořizování
fotek (s luxusní možností ovládat externí zařízení; v našem případě lampy pro
noční přisvětlování).

Pokud byste chtěli sledovat líhnutí motýla, růst krystalu nebo plísně na chlebu,
můžete tento projekt s minimální modifikací využít (obecně uvažujte o
jakémkoliv pomalém ději, který se dá dokumentovat s periodou v řádech minut).
