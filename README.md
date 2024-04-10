# Taj-Mahal-Spammer

Ein Python-Skript, das bunte Licht-Anfragen an das LEGO Taj Mahal im Wohnzimmer von Dr. Florian Volk sendet.

## Beschreibung

Dieses unterhaltsame Skript ermöglicht das Senden unterschiedlicher Farbmuster, um das LEGO Taj Mahal zu steuern. Mit Befehlszeilenoptionen können Sie verschiedene Modi auswählen und eine Verzögerung festlegen.

## Installation

**Voraussetzungen**
* Python 3
* `requests` Bibliothek (Installation mit `pip install requests`)

**Anleitung**
1. Klonen Sie dieses Repository.
2. Installieren Sie die erforderliche Bibliothek: `pip install -r requirements.txt`

## Verwendung

```bash
python taj-spammer.py -h  # Anzeigen der Hilfe für alle Optionen
```
## Optionen

    -m, --mode:
        random: Sendet zufällige Farben.
        police: Wechselt zwischen Blau und Rot.
        rainbow: Simuliert einen Regenbogen.
        (Default-Wert : rainbow)

    -d, --delay:
        Legt die Verzögerung in Sekunden zwischen den einzelnen Anfragen fest (Default-Wert : 15).

## Beispiele

    Regenbogenfarben mit einer Verzögerung von 10 Sekunden:
    python taj-spammer.py -m rainbow -d 10

    Abwechselnd Rot und Blau mit einer Verzögerung von 5 Sekunden:
    python taj-spammer.py -m police -d 5

