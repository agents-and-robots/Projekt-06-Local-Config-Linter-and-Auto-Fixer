# Test: Parser

## Natürliche Sprache
Der Parser soll "KEY=VALUE"-Zeilen in ein Dict umwandeln.

## Maschinenlesbare Struktur
input:
  lines:
    - "HOST=localhost"
    - "PORT=8080"

expected:
  config:
    HOST: "localhost"
    PORT: "8080"
