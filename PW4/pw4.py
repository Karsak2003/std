
#region IMPORT
from functools import reduce
from typing import Any
import json
#endregion IMPORT



def getDate(nameflie:str) -> list:
    temp:list = []
    with open(nameflie) as file: temp = json.load(file)    
    return temp

def display(fun, arg):
    print(f'{type(fun)} : {fun}')
    print(f'arg={arg} => fun(arg)={fun(arg)}')
    return fun(arg)

'''
Используя сначала каррирование, а затем замыкания, объявите функцию
categorize_countries(), которая возвращает список стран с некоторым
общим шаблоном (например,  'land', 'ia', 'island', 'stan'), который
можно менять.
'''

def categorize_countries(filt:str):
    def f(x):
        return [v for v in x if filt in v]
    return f


def main() -> None:
    countries:list = getDate("PW4\countries.json")
    print(*countries[0:10], "...", sep=", ")
    
    I = lambda x: list(map(str.lower, x))
    print(*I(countries)[0:10], "...", sep=", ")    
    
    
    I1 = lambda x: "land" in x
    I_1 = lambda x: list(filter(I1, x))
    print(*I_1(countries), sep=", ")
      
    I2 = lambda x: len(x) <= 6
    I_2 = lambda x: list(filter(I2, x))
    print(*I_2(countries)[0:10], "...", sep=", ")  
    
    I3 = lambda x: x[0] in "Ee"
    I_3 = lambda x: list(filter(I3, x))
    print(*I_3(countries), sep=", ")  
    
    I4 = lambda aggr , x: aggr+", "+x
    I_4 = lambda x: reduce(I4, x)
    print(I_4(["Finland", "Sweden", "Denmark", "Norway", "Iceland"]) + "are the Nordic countries.")
    print()
    #8. Решите предыдущие задачи, объединив две или более функций высшего порядка методов 
    
    display(I, countries[0:5])
    display(I_1, countries[0:10])
    display(I_2, countries[0:10])
    display(I_3, countries[0:10])
    print(display(I_4, ["Finland", "Sweden", "Denmark", "Norway", "Iceland"]), "are the Nordic countries.")
    
    
    print()
    '''
    Используя сначала каррирование, а затем замыкания, объявите функцию
    categorize_countries(), которая возвращает список стран с некоторым
    общим шаблоном (например,  'land', 'ia', 'island', 'stan'), который
    можно менять.
    '''
    print(categorize_countries("land")(countries))
    del countries, I, I1, I_1, I2, I_2, I3, I_3, I4, I_4,
    print()
    """
    10. Используя файл countries-data.json, выполните приведенные ниже задания в функциональной парадигме:
        1. Отсортировать страны:
            1. по названию,
            2. по столице,
            3. по численности населения 
        2. Выявить произвольное число (начать с 10) наиболее распространенных языков и где их используют.
        3. Выявить произвольное число (начать с 10) наиболее населенных стран.
    """
    
    countries:list[dict] = getDate("PW4\countries-data.json")
    #// keys:list = list(countries[0].keys())
    I_getByKey = lambda x, key: x[key]
    I_getName = lambda x: I_getByKey(x, "name")
    I_getCapital = lambda x: I_getByKey(x, "capital")
    I_getPopulation = lambda x: I_getByKey(x, "population")
    I_getLanguages = lambda x:I_getByKey(x, "languages")
    
    I = lambda x, fun: list(map(fun, x))
    
    # print(countries[0:10])
    print()
    print(*I(sorted(countries, key=I_getName), I_getName)[0:10], sep=", ")
    print()
    print(*I(sorted(countries, key=I_getCapital), I_getName)[0:10], sep=", ")
    print()
    print(*I(sorted(countries, key=I_getPopulation, reverse=True), I_getName)[0:10], sep=", ")
    print()
    
    print()

    # Выявить произвольное число (начать с 10) наиболее населенных стран.
    print(*I(sorted(countries, key=I_getPopulation), I_getName)[0:5], sep=", ")
    #//print(*I(countries,I_getLanguages), sep=", ")
    print()
    # Выявить произвольное число (начать с 10) наиболее распространенных языков и где их используют.
    
    I1c = lambda fun: lambda x: \
        list(set(reduce(lambda aggr, x1: aggr + x1, list(map(fun, x)))))
    
    lang:list = I1c(I_getLanguages)(countries)
    temp = {f"{x}":[y["name"] for y in countries if x in y["languages"]] for x in lang}
    lang.sort(key=lambda x: len(temp[x]), reverse=True)
    
    I2c = lambda y: lambda x: f"{x} ({len(y[x])}):{", ".join(y[x][0:5])}"
    
    print(*list(map(I2c(temp), lang[0:10])), sep="\n")
    
    
if __name__ == "__main__":main()