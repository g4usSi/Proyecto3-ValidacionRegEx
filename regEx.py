class RegexRules:

    rules = {
        "numero_entero": r"^[0-9]+$",                  # Solo digitos, sin decimales ni signos
        "palabra_minuscula": r"^[a-z]+$",              # Solo letras minúsculas
        "nombre_mayuscula_inicial": r"^[A-Z][a-z]+$",  # Nombre con inicial mayúscula
        "telefono_con_guiones": r"[0-9]{3}-[0-9]{4}-[0-9]{4}",  # Teléfono con guiones

        # Ejemplos de reglas generales
        "inicio_cadena": r"^",              # Inicio de cadena
        "fin_cadena": r"$",                 # Fin de cadena
        "conjunto_abc": r"[abc]",           # Solo a, b o c
        "digito": r"[0-9]",                 # Cualquier dígito
        "mayuscula": r"[A-Z]",              # Letra mayúscula
        "minuscula": r"[a-z]",              # Letra minúscula
        "no_digito": r"[^0-9]",             # Cualquier carácter que no sea dígito
        "cero_o_mas": r"a*",                # Cero o más veces "a"
        "uno_o_mas": r"a+",                 # Una o más veces "a"
        "cero_o_una": r"a?",                # Cero o una vez "a"
        "exactamente_n": r"[0-9]{4}",       # Exactamente 4 dígitos
        "al_menos_n": r"[a-z]{3,}",         # Al menos 3 letras minúsculas
        "entre_n_m": r"[0-9]{2,4}",         # Entre 2 y 4 dígitos
        "cualquier_caracter": r".",         # Cualquier caracter excepto salto de línea
        "alternativa": r"(perro|gato)",     # perro o gato
        "punto_literal": r"\.",             # Punto literal
        "grupo_ab": r"(ab)+",               # Repite grupo "ab"
        "binario_3": r"(0|1){3}",           # Cadenas binarias de 3 símbolos
    }

    @classmethod
    def list_rules(cls):
        """Lista todas las reglas disponibles"""
        return list(cls.rules.keys())

    @classmethod
    def get_rule(cls, name: str):
        """Obtiene la regex por su nombre"""
        return cls.rules.get(name, None)
