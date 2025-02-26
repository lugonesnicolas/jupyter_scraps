def get_nested_value(data, keys, default=''):
    """
    Obtiene un dato anidado en un diccionario de forma segura.

    Args:
        data (dict): El diccionario donde se buscará el valor.
        keys (list): Una lista de claves anidadas para acceder al valor.
        default (any, optional): El valor por defecto si la clave no se encuentra.
            Defaults to ''.

    Returns:
        any: El valor encontrado o el valor por defecto.
    """

    try:
        for key in keys:
            data = data[key]
        return data
    except (KeyError, TypeError, IndexError) as e:
        print(f"---- No se pudo extraer el dato anidado - {e}")
        return default