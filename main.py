from pillow_heif import register_heif_opener
from PIL import Image
import os

# Registrar el lector HEIF en PIL
register_heif_opener()

# 📁 Ruta del archivo .heic/.heif que querés convertir
input_path = r"C:\Users\nahuel\Downloads\IMG_4877.HEIF"

# 📁 Ruta de salida con extensión .jpg
output_path = os.path.splitext(input_path)[0] + ".jpg"

# 🖼️ Abrir y convertir
try:
    img = Image.open(input_path)
    img.save(output_path, "JPEG")
    print("✅ Conversión completada:", output_path)
except Exception as e:
    print("❌ Error durante la conversión:", str(e))
