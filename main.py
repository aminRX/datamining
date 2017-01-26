import requests

def mode(list):
        return max(set(list), key=list.count)

def mean(data):
    n = len(data)
    if n < 1:
        raise ValueError('mean requires at least one data point')
    return sum(data)/n

def _ss(data):
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss

def pstdev(data):
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/n
    return pvar**0.5

def ages(body):
    return search_by_index(body, 0)

def sex(body):
    return search_by_index(body, 1)

def search_by_index(body, position):
    list = []
    for line in body:
        list.append(int(float(line.split(',')[position])))
    return list

def count_elements(element):
    duplicateFrequencies = {}
    for i in set(element):
        duplicateFrequencies[i] = element.count(i)
    return duplicateFrequencies

def ages_result(element):
    print('Edades:')
    print('El maximo: {}'.format(max(element)))
    print('El minimo: {}'.format(min(element)))
    print('La mediana {}'.format(mean(element)))
    print('La moda: {}'.format(mode(element)))
    print('La des stand: {}'.format(pstdev(element)))

def sex_result(element):
    print('Sexos:')
    print('El promedio de hombres es de: {}%'.format(float(count_elements(element)[1]) / len(element) * 100))
    print('El promedio de mujeres es de: {}%'.format(float(count_elements(element)[0]) / len(element) * 100))

def main():
    r = requests.get('http://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data')
    body = r.text.encode("utf-8").split()
    years = ages(body)
    sexs = sex(body)
    ages_result(years)
    sex_result(sexs)

if __name__ == "__main__":
    main()
