# #Pillow: redimensionando imagens com Python

# from PIL import Image
# from pathlib import Path

# ROOT_FOLDER = Path(__file__).parent
# ORIGINAL = ROOT_FOLDER / 'carro.jpg'
# NEW_IMAGE = ROOT_FOLDER / 'new.jpg'

# pil_image = Image.open(ORIGINAL)
# width , height = pil_image.size
# exif = pil_image.info.get ('exif')

# #NEW WIDTH

# #NEW HEIGHT
# new_width = 640
# new_height = round(height * new_width / width)

# print(width, height)
# print(new_width, new_height)

# new_image = pil_image.resize((new_width, new_height))
# new_image.save(
#     NEW_IMAGE,
#     optimize=True,
#     quality=70,
#     exif=exif,

# )

from PIL import Image
from pathlib import Path

# Configuração dos caminhos das imagens
ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'carro.jpg'
NEW_IMAGE = ROOT_FOLDER / 'new.jpg'

# Abre a imagem original
pil_image = Image.open(ORIGINAL)
width, height = pil_image.size

# Tenta pegar o EXIF (retorna None se não existir)
exif = pil_image.info.get('exif') 

# Define a nova largura e calcula a nova altura proporcional
new_width = 640
new_height = round(height * new_width / width)

print(f"Dimensões Originais: {width}x{height}")
print(f"Novas Dimensões: {new_width}x{new_height}")

# Redimensiona a imagem passando as dimensões como uma TUPLA (parênteses duplos)
new_image = pil_image.resize((new_width, new_height))

# Prepara os argumentos para salvar a imagem
save_args = {
    'optimize': True,
    'quality': 70
}

# Só adiciona o parâmetro exif se ele realmente existir na imagem original
if exif is not None:
    save_args['exif'] = exif

# Salva a nova imagem aplicando os argumentos dinamicamente
new_image.save(NEW_IMAGE, **save_args)

print("Imagem redimensionada e salva com sucesso!")
