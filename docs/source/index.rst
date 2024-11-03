######################
OBP-Plotter V4: Dokumentation
######################

Letzte Aktualisierung |today|

Der OBP-Plotter V4 wird für die Darstellung von marinen Karten und Daten auf Booten verwendet. Zielgruppe sind Sportbootfahrende in aller Welt. Der OBP-Plotter ist ausgestattet mit einem tageslichttauglichen 10-Zoll-Touch-Display. Als Hardwarebasis dienen Compute Module der Versionen 4 und 5 der Raspberry Foundation. Mit der Außenwelt kommuniziert der Plotter vor allem per USB oder WLAN. Das macht ihn maximal flexibel im Einsatz unterschiedlichster Navigationssysteme an Bord. Eine Einbindung in bestehende NMEA-Netzwerke ist selbstverständlich ebenso möglich, egal ob NMEA-0183 oder NMEA2k. Die Betriebssystembasis bildet ein aktuelles Android (14 oder 15), auf dem die Navigations-App "AvNav" vorinstalliert ist. Alternativ lässt sich von Anwendern auch ein Raspbian nutzen, um dort zum Beispiel OpenCPN zu installieren.

.. toctree::
   :maxdepth: 3
   :caption: Übersicht und Einstieg
   :name: sec-intro

   Hardware: Übersicht <intro/hardware>
   Software: Erster Start <intro/software>
   
.. toctree::
   :maxdepth: 3
   :caption: Installation
   :name: sec-install

   Android-Image aufspielen <install/image>
   AvNav: Wesentliche Konfiguration <install/avkonfig>   
   AvNav: Karten aufspielen <install/avcharts>
   AvNav: O-Charts lizensieren <install/avocharts>
   AvNav: NMEA-Netzwerke  <install/nmea>
   AvNav: WLAN-LAN <install/wlan>
   AvNav: Fernbedienung <install/remote>

.. toctree::
   :maxdepth: 3
   :caption: Bedienung
   :name: sec-usermanual

   Funktionsweise <usermanual/functionality>
   Bedienelemente <usermanual/elements>
   Inbetriebnahme <usermanual/start>
   Konfiguration <usermanual/configuration>
   Bussysteme <usermanual/bussystems>
   Datenaustausch <usermanual/dataexchange>
   Erweiterte Sensorik <usermanual/sensors>
   Beispielkonfiguration <usermanual/samples>
   Sicherheitshinweise <usermanual/safety>

.. toctree::
   :maxdepth: 3
   :caption: Zusammenbau
   :name: sec-assembling
   
   Geräteaufbau <assembling/device>
   Vorbereitung <assembling/preparation>
   Bauteilliste <assembling/partlist>
   Durchführung <assembling/actionsteps>
   Funktionstest <assembling/tests>
      
.. toctree::
   :maxdepth: 3
   :caption: Hilfe
   :name: sec-help   

   Fragen und Antworten <help/faq>
   Meinungen und Tipps <help/opinions>
   Bekannte Fehler <help/errors>
   Technische Unterstützung <help/support>
   Service <help/service>
   Mitarbeit <help/cooperation>
   Spenden <help/donation>
   Glossar <help/glossar>
