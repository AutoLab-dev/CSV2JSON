import csv, json, os

print("=== CSV → JSON Converter ===")

ruta = "ejemplos/ejemplo.csv"
print("Ruta actual:", os.getcwd())
print("Buscando archivo en:", ruta)
print("Existe?", os.path.exists(ruta))

try:
    with open(ruta, encoding="utf-8") as f:
        lector = csv.DictReader(f)
        datos = list(lector)
    with open("ejemplos/ejemplo.json", "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)
    print("✅ Conversión completada. Archivos en carpeta 'ejemplos/'.")
except Exception as e:
    print("❌ Error:", e)
