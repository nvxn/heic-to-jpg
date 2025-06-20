# 📸 Heic or Heif to JPEG

Script en Python para convertir (desde la terminal) archivos `.heic` o `.heif` a `.jpg` utilizando la librería `pillow-heif`.

Compatible con `Windows` y `Linux` (`Linux Mint` u otras distribuciones).

---

## 📝 Script: `main.py`

```python
from pillow_heif import register_heif_opener
from PIL import Image
import os

# Registrar el lector HEIF en PIL
register_heif_opener()

# 📁 Ruta del archivo .heic/.heif que se desea convertir
input_path = r"C:\Users\nahuel\Downloads\IMG_4877.HEIC"  # Cambiar según el sistema operativo

# 📁 Ruta de salida con extensión .jpg
output_path = os.path.splitext(input_path)[0] + ".jpg"

# 🖼️ Abrir y convertir
try:
    img = Image.open(input_path)
    img.save(output_path, "JPEG")
    print("✅ Conversión completada:", output_path)
except Exception as e:
    print("❌ Error durante la conversión:", str(e))
```

---

## 📦 Paso 1: Instalar dependencias

Desde la terminal o PowerShell (dentro de un entorno virtual si estás usando uno):

```bash
pip install pillow pillow-heif
```

---

## 🔧 Paso 2: Personalizar rutas

Cambia la ruta del archivo de entrada y salida según tu sistema:

* **Windows:**

```python
input_path = r"C:\Users\TuUsuario\Pictures\foto.heic"
```

* **Linux (Mint u otra):**

```python
input_path = "/home/tu_usuario/Imágenes/foto.heic"
```

---

## ▶️ Paso 3: Ejecutar el script

### 🪟 En Windows

Desde PowerShell o la terminal de VS Code:

```powershell
python main.py
```

Si estás usando un entorno virtual, asegúrate de activarlo:

```powershell
& "ruta\a\tu\entorno_virtual\Scripts\Activate.ps1"
```

### 🐧 En Linux (Linux Mint)

Desde la terminal:

```bash
python3 main.py
```

Si estás en un entorno virtual, actívalo primero:

```bash
source .venv/bin/activate
```

---

## ✅ Resultado

El script generará un archivo `.jpg` en la misma ubicación que el archivo original.