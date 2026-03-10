# LLM Instructions – Local Config Linter & Auto-Fixer (Offline)

Diese Datei definiert alles, was ein LLM benötigt, um dieses Projekt vollständig selbständig umzusetzen:
- Input/Output-Protokoll
- Modul- und Agenten-Logik
- Regelwerk
- Hardware-Constraints
- How-To-Use

---

## 1. Ziel

Erstelle ein System, das Konfigurationsdateien analysiert, Validierungsfehler meldet
und einfache Auto-Fixes vorschlägt oder anwendet — vollständig offline.

---

## 2. Hardware Constraints

Dieses Projekt muss vollständig auf normaler Consumer-Hardware lauffähig sein:

- CPU-only
- keine GPU-Abhängigkeiten
- keine Modelle > 1 GB
- keine externen APIs oder Cloud-Dienste
- alles offline
- Python-Standardbibliothek

---

## 3. Modul-Spezifikationen

### 3.1 Parser (/src/parser.py)

Signatur: parse(lines: list[str]) -> dict

Aufgabe:
- einfache Key-Value-Konfigurationen parsen (z. B. "KEY=VALUE")

Rückgabeformat:
- config: dict (key → value)

---

### 3.2 Validator (/src/validator.py)

Signatur: validate(config: dict) -> dict

Aufgabe:
- Pflichtfelder prüfen
- Wertebereiche validieren

Rückgabeformat:
- valid: bool
- errors: list[dict]
  - key: string
  - message: string
  - type: string (missing, invalid_value, etc.)

---

### 3.3 Fixer (/src/fixer.py)

Signatur: fix(config: dict, errors: list[dict]) -> dict

Aufgabe:
- einfache Auto-Fixes anwenden
- Beispiele:
  - fehlende Pflichtfelder mit Default-Werten ergänzen
  - ungültige Werte auf Default setzen

Rückgabeformat:
- fixed_config: dict

---

### 3.4 Agent (/src/agent.py)

Signatur: run(lines: list[str]) -> dict

Aufgabe:
- orchestriert parser, validator, fixer
- optionalen zweiten Validierungsdurchlauf

Rückgabeformat:
- original_config: dict
- fixed_config: dict
- validation_before: dict
- validation_after: dict
- steps: list[str]

---

## 4. Orchestrator-Logik

1. config = parse(lines)
2. validation_before = validate(config)
3. fixed_config = fix(config, validation_before.errors)
4. validation_after = validate(fixed_config)
5. Ergebnis zurückgeben

---

## 5. Regelwerk / Constraints

### Parser
- unterstützt einfache "KEY=VALUE"-Zeilen
- ignoriert leere Zeilen und Kommentare (#)

### Validator
- Pflichtfelder (Beispiel):
  - "HOST"
  - "PORT"
- PORT muss eine Zahl sein
- PORT muss im Bereich 1–65535 liegen

### Fixer
- fehlender HOST → "localhost"
- fehlender PORT → "8080"
- ungültiger PORT → "8080"

---

## 6. Aufgaben an das LLM

Das LLM soll:

1. parser.py implementieren  
2. validator.py implementieren  
3. fixer.py implementieren  
4. agent.py implementieren  
5. architecture.md ergänzen  
6. Tests in /tests aktualisieren  

---

## 7. How-To-Use (für Code-Assistenten)

1. Öffne das Repository.  
2. Öffne `instructions.md`.  
3. Markiere den gesamten Inhalt.  
4. Sende ihn an deinen Code-Assistenten mit:

„Lies diese instructions.md vollständig. Implementiere dann alle beschriebenen Module und Dateien. Halte dich strikt an das Input/Output-Protokoll, das Regelwerk und die Hardware-Constraints. Beginne mit parser.py.“

Damit kann ein LLM das Projekt vollständig autonom umsetzen.
