# Local Config Linter & Auto-Fixer (Offline, CPU-only)

Dieses Projekt prüft lokale Konfigurationsdateien und kann einfache Probleme automatisch beheben.
Es arbeitet vollständig offline, benötigt keine GPU und verwendet keine KI-Modelle.

Funktionen:
- Konfigurationsdateien parsen (z. B. .ini, .env)
- Pflichtfelder prüfen
- Wertebereiche validieren
- einfache Auto-Fixes vorschlagen oder anwenden

Das Projekt demonstriert:
- deterministische Validierung
- regelbasierte Auto-Fixes
- klare I/O-Spezifikationen
- Prompt-Driven Development (PDD)

## Projektstruktur

/src  
    parser.py  
    validator.py  
    fixer.py  
    agent.py  

/docs  
    architecture.md  

/tests  
    test_parser.md  
    test_validator.md  
    test_fixer.md  
    test_agent.md  

hardware-requirements.md  
instructions.md  
README.md  
credits.md

## Hardware Requirements

Dieses Projekt ist vollständig lokal ausführbar und benötigt keine spezielle Hardware.
Siehe `hardware-requirements.md`.

## Lizenz

MIT License.

## Credits

Siehe `credits.md`.
