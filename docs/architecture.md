# Architektur – Local Config Linter & Auto-Fixer

## Module

- parser.py – parst Konfigurationszeilen in ein Dict
- validator.py – prüft Pflichtfelder und Wertebereiche
- fixer.py – wendet Auto-Fixes an
- agent.py – orchestriert den Prozess

## Datenfluss

1. Parser erzeugt config-Dict
2. Validator prüft config
3. Fixer korrigiert config
4. Validator prüft erneut
5. Agent orchestriert alles
