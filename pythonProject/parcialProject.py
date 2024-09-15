# Conversión de tipos de datos
num_int = 10
num_float = 10.5
num_str = "15"

# Convertir entre tipos
num_str_to_int = int(num_str)
num_str_to_float = float(num_str)

print(f"Entero: {num_int}, Decimal: {num_float}, Cadena: {num_str}")
print(f"Convertido a entero: {num_str_to_int}, Convertido a decimal: {num_str_to_float}")

# Multilíneas de cadenas
multiline_str = """Esto es una cadena
que se extiende en varias líneas
y puede ser útil para textos largos."""
print(multiline_str)

# Función len()
length_of_str = len(multiline_str)
print(f"La longitud de la cadena es: {length_of_str}")

# Sub cadenas
original_str = "Hola, ¿cómo estás?"
first_n_chars = original_str[:5]  # Obtener los primeros 5 caracteres
middle_chars = original_str[6:11]  # Obtener caracteres del medio
last_n_chars = original_str[-6:]  # Obtener los últimos 6 caracteres

print(f"Primeros 5 caracteres: {first_n_chars}")
print(f"Caracteres del medio: {middle_chars}")
print(f"Últimos 6 caracteres: {last_n_chars}")

# Función upper() y lower()
upper_str = original_str.upper()
lower_str = original_str.lower()

print(f"Cadena en mayúsculas: {upper_str}")
print(f"Cadena en minúsculas: {lower_str}")

# Función strip(), replace(), split()
strip_str = "   Cadena con espacios   ".strip()
replaced_str = original_str.replace("¿cómo?", "¿qué tal?")
split_str = original_str.split(", ")

print(f"Cadena sin espacios: '{strip_str}'")
print(f"Cadena reemplazada: '{replaced_str}'")
print(f"Cadena dividida: {split_str}")

# Formato de cadenas F-String
name = "Juan"
greeting = f"Hola, {name}! Bienvenido al proyecto."

print(greeting)
