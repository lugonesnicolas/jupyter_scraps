def get_nested_value(data, keys, default=''):
    try:
        for key in keys:
            data = data[key]
        return data
    except (KeyError, TypeError, IndexError) as e:
        print(f"No se pudo extraer el dato anidado - {e}")
        return default
    
