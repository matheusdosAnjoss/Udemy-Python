# Importa o módulo calendar para trabalhar com calendários
import calendar
# Importa o módulo locale para configurar a localização/idioma
import locale

# Define a localização do sistema para o padrão do ambiente (idioma, formatação de datas, etc.)
locale.setlocale(locale.LC_ALL, '')

# Exibe o calendário completo do ano de 2026
print(calendar.calendar(2026))