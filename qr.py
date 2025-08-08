import qrcode
from xml.etree.ElementTree import Element, SubElement, tostring

# Ссылка для QR-кода
url = "https://t.me/georg_xv"

# Создание QR-кода
qr = qrcode.QRCode(
    version=1,  # Размер QR-кода (1 — минимальный, 40 — максимальный)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Коррекция ошибок
    box_size=10,  # Размер квадрата
    border=0,  # Убираем внешние границы
)
qr.add_data(url)
qr.make(fit=True)

# Генерация данных QR-кода
matrix = qr.modules

# Создание SVG вручную
svg = Element("svg", xmlns="http://www.w3.org/2000/svg", version="1.1")
svg.set("width", f"{len(matrix) * 10}")
svg.set("height", f"{len(matrix) * 10}")
svg.set("viewBox", f"0 0 {len(matrix)} {len(matrix)}")

# Цвет блоков QR-кода
fill_color = "rgb(128, 108, 0)"

# Добавление блоков в SVG
for y, row in enumerate(matrix):
    for x, cell in enumerate(row):
        if cell:  # Если блок заполнен
            rect = SubElement(svg, "rect", x=str(x), y=str(y), width="1", height="1")
            rect.set("fill", fill_color)

# Сохранение SVG в файл
output_file = "qr_code_transparent.svg"
with open(output_file, "wb") as f:
    f.write(tostring(svg))

print(f"QR-код с прозрачным фоном сохранён в файл {output_file}")