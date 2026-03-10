# Test: Fixer

## Natürliche Sprache
Der Fixer soll fehlenden PORT mit 8080 ergänzen.

## Maschinenlesbare Struktur
input:
  config:
    HOST: "localhost"
  errors:
    - key: "PORT"
      type: "missing"

expected:
  fixed_config:
    PORT: "8080"
