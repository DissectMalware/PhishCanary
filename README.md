# PhishCanary
Given a TLD zone file, PhishCanary extracts International Domain Names (IDNs) that are homoglyphs of specified target domain names.

PhishCanary filters out the IDNs created by the target domain names' authoritative nameservers or by trusted domain names.


# Installing PhishCanary

1. Installing from Repository

```
pip install -U https://github.com/DissectMalware/PhishCanary/archive/master.zip
pip install -U https://github.com/DissectMalware/pyxlsb2/archive/master.zip
pip install -U https://github.com/DissectMalware/XLMMacroDeobfuscator/archive/master.zip
```

# Running PhishCanary
To extracts suspicious IDNs from a zone file

```
phishcanary --zonefile com.zone  --targets target-domains.txt

phishcanary -f com.zone  -t target-domains.txt
```

Where target-domains.txt contain a list of domain names that we are interested in:

```
target-domains.txt:
microsoft.com
twitter.com
instagram.com
yahoo.com
youtube.com
facebook.com
```

Sample ouput

```
instagram,heipinstagram,helpınstagram,xn--helpnstagram-44b.com.	172800	in	ns	ns1.jobsive.cf.
instagram,heip-instagram,hélp-instagram,xn--hlp-instagram-bhb.com.	172800	in	ns	ns09.domaincontrol.com.
instagram,instagram,ınstagram,xn--nstagram-skb.com.	172800	in	ns	ns1.bodis.com.
instagram,instagram-espana,instagram-españa,xn--instagram-espaa-crb.com.	172800	in	ns	ns10.servicio-online.net.
instagram,instagram-teiifhakki,instagram-telifhakkı,xn--instagram-telifhakk-y5c.com.	172800	in	ns	ns09.domaincontrol.com.
instagram,iinstagram,iınstagram,xn--instagram-vpb.com.	172800	in	ns	ns1.jobsive.cf.
instagram,instagram-yardimmerkezi,instagram-yardımmerkezi,xn--instagram-yardmmerkezi-zld.com.	172800	in	ns	ns-cloud-e1.googledomains.com.
instagram,instagramcekiiissitesi,instagramcekilissıtesi,xn--instagramcekilisstesi-0gd.com.	172800	in	ns	ns1.wafbone.com.
instagram,instagramcopyrights,instagramcopyrıghts,xn--instagramcopyrghts-r0c.com.	172800	in	ns	ex1.natrohost.com.
instagram,instagramespana,instagramespaña,xn--instagramespaa-2nb.com.	172800	in	ns	ns10.servicio-online.net.
instagram,instagramhesapiari,instagramhesapları,xn--instagramhesaplar-svc.com.	172800	in	ns	ns17.hostlab.net.tr.
instagram,instagramverify,instagramverıfy,xn--instagramverfy-hgc.com.	172800	in	ns	ns09.domaincontrol.com.
instagram,instagramsecurity,lnstagramsecurıty,xn--lnstagramsecurty-nqc.com.	172800	in	ns	ns1.beget.com.
instagram,insagram,ınsagram,xn--nsagram-qfb.com.	172800	in	ns	ns1.muvhost.com.
instagram,lnstagram,ǀnstagram,xn--nstagram-kmc.com.	172800	in	ns	kim.ns.cloudflare.com.
instagram,instagramcekiiisitesi,ınstagramcekilisitesi,xn--nstagramcekilisitesi-hbd.com.	172800	in	ns	ns03.domaincontrol.com.
instagram,instagramdraw,ınstagramdraw,xn--nstagramdraw-04b.com.	172800	in	ns	ns55.domaincontrol.com.
instagram,instagramheipcenter,ınstagramhelpcenter,xn--nstagramhelpcenter-d0c.com.	172800	in	ns	ns96.kebirhost.com.
instagram,instagramheipcopyright,ınstagramhelpcopyright,xn--nstagramhelpcopyright-jgd.com.	172800	in	ns	ns11.jimdo.com.
instagram,instagramheipcopyrightsupport,ınstagramhelpcopyrightsupport,xn--nstagramhelpcopyrightsupport-xge.com.	172800	in	ns	ns11.jimdo.com.
instagram,instagramverifybadge,ınstagramverifybadge,xn--nstagramverifybadge-f5c.com.	172800	in	ns	ns1jlp.name.com.
instagram,instagrarn,ınstagrarn,xn--nstagrarn-upb.com.	172800	in	ns	ns1.lovellsnames.org.
instagram,pinatagram,piñatagram,xn--piatagram-m6a.com.	172800	in	ns	ns1.namedynamics.net.
instagram,smminstagram,smmınstagram,xn--smmnstagram-1zb.com.	172800	in	ns	ns1.siberdizayn.net.tr.
instagram,istagram,ıstagram,xn--stagram-qfb.com.	172800	in	ns	kurt.ns.cloudflare.com.
instagram,turkinstagram,türkinstagram,xn--trkinstagram-dlb.com.	172800	in	ns	ns49.domaincontrol.com.
yahoo,yahoo,yăhoo,xn--yhoo-0sa.com.	172800	in	ns	ns59.domaincontrol.com.
yahoo,apartamentospeniscoiapiaya3ooo,apartamentospeñiscolaplaya3000,xn--apartamentospeiscolaplaya3000-j1c.com.	172800	in	ns	docks20.rzone.de.
yahoo,bidunyahome,bidünyahome,xn--bidnyahome-ceb.com.	172800	in	ns	ns03.domaincontrol.com.
yahoo,despuesdeyahoraque,despuésdeyahoraque,xn--despusdeyahoraque-ftb.com.	172800	in	ns	ns67.domaincontrol.com.
yahoo,medyahocasi,medyahocası,xn--medyahocas-6ub.com.	172800	in	ns	ns5.poyrazhosting.com.
yahoo,nyahovaspaddei,nyahovåspaddel,xn--nyahovspaddel-ufb.com.	172800	in	ns	ns1.loopia.se.
yahoo,paddeinyahovas,paddelnyahovås,xn--paddelnyahovs-0fb.com.	172800	in	ns	ns1.loopia.se.
yahoo,pitadeciujyahoo,pitădeclujyahoo,xn--pitdeclujyahoo-ivb.com.	172800	in	ns	ns09.domaincontrol.com.
yahoo,psychoonkoiogie-munchen,psychoonkologie-münchen,xn--psychoonkologie-mnchen-8lc.com.	172800	in	ns	ns75.domaincontrol.com.
yahoo,saharahookahioungecafe,saharahookahloungecafé,xn--saharahookahloungecaf-v5b.com.	172800	in	ns	ns1.us266.siteground.us.
yahoo,siyahcorapiiiar,siyahçoraplılar,xn--siyahorapllar-mgb92i.com.	172800	in	ns	ns25.domaincontrol.com.
yahoo,yaho,yahơ,xn--yah-e7a.com.	172800	in	ns	ns1.panamans.com.
yahoo,yahooenespanoi,yahooenespañol,xn--yahooenespaol-skb.com.	172800	in	ns	ns1.parkingcrew.net.
yahoo,yahooespanoi,yahooespañol,xn--yahooespaol-9db.com.	172800	in	ns	ns1.parkingcrew.net.
yahoo,yahoomaii,yahoomaıl,xn--yahoomal-zkb.com.	172800	in	ns	ns77.domaincontrol.com.
yahoo,yahoraque,yahoraqué,xn--yahoraqu-i1a.com.	172800	in	ns	ns35.domaincontrol.com.
twitter,twitter,ţwitter,xn--witter-okb.com.	172800	in	ns	ns-cloud-e1.googledomains.com.
twitter,twisterhardesign,twisterhårdesign,xn--twisterhrdesign-olb.com.	172800	in	ns	dns1.comitnet.com.
twitter,twittei,twitteı,xn--twitte-u9a.com.	172800	in	ns	dns1.registrar-servers.com.
twitter,twittertakipci,twittertakipçi,xn--twittertakipi-tgb.com.	172800	in	ns	chan.ns.cloudflare.com.
twitter,twittertakipcihiiesi,twittertakipçihilesi,xn--twittertakipihilesi-hyb.com.	172800	in	ns	chan.ns.cloudflare.com.
microsoft,mlcrosoft,ꓟꓲꓚꓣꓳꓢꓳꓝꓔ,xn--7l8alajgqf7hkb.com.	172800	in	ns	ns.udag.de.
microsoft,nicrosoft,ñicrosoft,xn--icrosoft-c3a.com.	172800	in	ns	ns1021.ui-dns.biz.
microsoft,microsoft,micrøsoft,xn--micrsoft-84a.com.	172800	in	ns	ns-1131.awsdns-13.org.
microsoft,microsoftoniine,microsoftonlıne,xn--microsoftonlne-hgc.com.	172800	in	ns	ns1.guzelhosting.com.
microsoft,micrusoft,micrüsoft,xn--micrsoft-95a.com.	172800	in	ns	ns-cloud-d1.googledomains.com.
microsoft,onmicrosoft,onmicrosøft,xn--onmicrosft-7cb.com.	172800	in	ns	ns-cloud-e1.googledomains.com.
microsoft,rnicrosoft,rnıcrosoft,xn--rncrosoft-wpb.com.	172800	in	ns	dns1.registrar-servers.com.
microsoft,soportemicrosoftaccount,soportémicrosoftaccount,xn--soportmicrosoftaccount-g8b.com.	172800	in	ns	ns1.verification-hold.suspended-domain.com.
facebook,facebook,fåcebook,xn--fcebook-exa.com.	172800	in	ns	dns113.ovh.net.
facebook,tacebook,ƭacebook,xn--acebook-27b.com.	172800	in	ns	ns53.domaincontrol.com.
facebook,lacebook,łacebook,xn--acebook-mjb.com.	172800	in	ns	dns112.ovh.net.
facebook,facobook,facɵbooĸ,xn--facboo-8bb64w.com.	172800	in	ns	ns1.sedoparking.com.
facebook,facebook-fbcdn,facebooĸ-fbcdn,xn--faceboo-fbcdn-2dc.com.	172800	in	ns	ina1.registrar.eu.
facebook,facebook-fur-business,facebook-für-business,xn--facebook-fr-business-yec.com.	172800	in	ns	ns1045.ui-dns.biz.
facebook,facebook-vacances-frejus,facebook-vacances-fréjus,xn--facebook-vacances-frjus-ucc.com.	172800	in	ns	ns09.domaincontrol.com.
facebook,iogin-facebook,login-facebooĸ,xn--login-faceboo-8dc.com.	172800	in	ns	ina1.registrar.eu.
facebook,nouveautefacebook,nouveautéfacebook,xn--nouveautfacebook-iqb.com.	172800	in	ns	ns1.consulnet.com.
facebook,pubiicite-facebook,publicité-facebook,xn--publicit-facebook-itb.com.	172800	in	ns	a.ns36.de.
facebook,turkfacebook,türkfacebook,xn--trkfacebook-thb.com.	172800	in	ns	ns57.domaincontrol.com.
youtube,youtube,yᴑutube,xn--yutube-w15b.com.	172800	in	ns	ns-cloud-d1.googledomains.com.
youtube,sesiiyoutube,seslıyoutube,xn--seslyoutube-2zb.com.	172800	in	ns	ns1.guzelhosting.com.
youtube,sscyoutube,ssçyoutube,xn--ssyoutube-r3a.com.	172800	in	ns	1107.ns1.above.com.
youtube,turkyoutube,türkyoutube,xn--trkyoutube-9db.com.	172800	in	ns	ns59.domaincontrol.com.
youtube,wwweyoutube,wwwéyoutube,xn--wwwyoutube-d7a.com.	172800	in	ns	ns1.parklogic.com.
youtube,youtibe,youtıbe,xn--youtbe-s9a.com.	172800	in	ns	ns1.parkingcrew.net.
youtube,youtubec,youtubeç,xn--youtube-0xa.com.	172800	in	ns	ns1.renewyourexpireddomain.com.
youtube,yioutube,yıoutube,xn--youtube-rfb.com.	172800	in	ns	ns27.domaincontrol.com.
youtube,yoiutube,yoıutube,xn--youtube-sfb.com.	172800	in	ns	ns23.domaincontrol.com.
youtube,youitube,youıtube,xn--youtube-tfb.com.	172800	in	ns	ns27.domaincontrol.com.
youtube,youtiube,youtıube,xn--youtube-ufb.com.	172800	in	ns	ns27.domaincontrol.com.
youtube,youtuibe,youtuıbe,xn--youtube-vfb.com.	172800	in	ns	ns47.domaincontrol.com.
youtube,youtubeespana,youtubeespaña,xn--youtubeespaa-khb.com.	172800	in	ns	a.ns36.de.
youtube,youtubemuzik,youtubemüzik,xn--youtubemzik-0hb.com.	172800	in	ns	ns23.guzelhosting.com.
```

# Command Line

```

      ___         ___                       ___           ___
     /\  \       /\  \                     /\__\         /\  \
    /::\  \      \:\  \       ___         /:/ _/_        \:\  \
   /:/\:\__\      \:\  \     /\__\       /:/ /\  \        \:\  \
  /:/ /:/  /  ___ /::\  \   /:/__/      /:/ /::\  \   ___ /::\  \
 /:/_/:/  /  /\  /:/\:\__\ /::\  \     /:/_/:/\:\__\ /\  /:/\:\__\
 \:\/:/  /   \:\/:/  \/__/ \/\:\  \__  \:\/:/ /:/  / \:\/:/  \/__/
  \::/__/     \::/__/       ~~\:\/\__\  \::/ /:/  /   \::/__/
   \:\  \      \:\  \          \::/  /   \/_/:/  /     \:\  \
    \:\__\      \:\__\         /:/  /      /:/  /       \:\__\
     \/__/       \/__/         \/__/       \/__/         \/__/
      ___           ___           ___           ___           ___
     /\__\         /\  \         /\  \         /\  \         /\  \
    /:/  /        /::\  \        \:\  \       /::\  \       /::\  \         ___
   /:/  /        /:/\:\  \        \:\  \     /:/\:\  \     /:/\:\__\       /|  |
  /:/  /  ___   /:/ /::\  \   _____\:\  \   /:/ /::\  \   /:/ /:/  /      |:|  |
 /:/__/  /\__\ /:/_/:/\:\__\ /::::::::\__\ /:/_/:/\:\__\ /:/_/:/__/___    |:|  |
 \:\  \ /:/  / \:\/:/  \/__/ \:\~~\~~\/__/ \:\/:/  \/__/ \:\/:::::/  /  __|:|__|
  \:\  /:/  /   \::/__/       \:\  \        \::/__/       \::/~~/~~~~  /::::\  \
   \:\/:/  /     \:\  \        \:\  \        \:\  \        \:\~~\      ~~~~\:\  \
    \::/  /       \:\__\        \:\__\        \:\__\        \:\__\          \:\__\
     \/__/         \/__/         \/__/         \/__/         \/__/           \/__/


PhishCanary(v0.1.0) - https://github.com/DissectMalware/PhishCanary

usage: extractor.py [-h] [-f FILE_PATH] [-t FILE_PATH] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE_PATH, --zonefile FILE_PATH
                        Specify a TLD zone file path
  -t FILE_PATH, --targets FILE_PATH
                        Specify a file containing target domain names
  -s, --sorted          Determine whether the lines in the input are sorted

```

# Requirements

It relies on the following libraries: dnspython and tldextract


# How to Contribute
If you found a bug or would like to suggest an improvement, please create a new issue on the [issues page](https://github.com/DissectMalware/PhishCanary/issues).

Feel free to contribute to the project forking the project and submitting a pull request.

You can reach [me (@DissectMlaware) on Twitter](https://twitter.com/DissectMalware) via a direct message.

