UNIT_OF_MEASURE_SHORT = {
    'штука': 'шт',
    'упаковка': 'уп',
    'литр': 'л',
    'метр': 'м',
    'килограмм': 'кг'
}


def get_short_unit(unit):
    return UNIT_OF_MEASURE_SHORT.get(unit, unit)