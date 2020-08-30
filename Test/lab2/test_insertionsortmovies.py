import pytest
import config as cf
from Sorting import insertionsort as sort
from DataStructures import listiterator as it
from ADT import list as lt
import csv

#list_type = 'ARRAY_LIST'
list_type = 'SINGLE_LINKED'

lst_movies = lt.newList(list_type)
lst_movies1 = lt.newList(list_type)
moviesfile = cf.data_dir + 'theMoviesdb/AllMoviesCastingRaw.csv'
moviesfile1 = cf.data_dir + 'theMoviesdb/AllMoviesDetailsCleaned.csv'


def setUp():
    print('Loading movies')
    loadCSVFile(moviesfile, lst_movies)
    loadCSVFile1(moviesfile1, lst_movies1)
    print(lst_movies['size'])
    print(lst_movies1['size'])


def tearDown():
       pass


def loadCSVFile(file, lst):
    input_file = csv.DictReader(open(file, encoding = "utf-8"))
    for row in input_file:
        lt.addLast(lst, row)

def loadCSVFile1 (file, lst):
    input_file = csv.DictReader(open(file, encoding = "utf-8-sig"))
    for row in input_file:
        lt.addLast(lst, row)

def printList(lst):
    iterator = it.newIterator(lst)
    while it.hasNext(iterator):
        element = it.next(iterator)
        print(element['id'])

def less(element1, element2):
    if int(element1['id']) < int(element2['id']):
        return True
    return False

def greater(element1,element2)->tuple:
    if int(element1["id"])>int(element2["id"]):
        return True
    return False

def test_sort():
    """
    Lista con elementos en orden aleatorio
    """
    print("sorting ....")
    sort.insertionSort(lst_movies, less)
    sort.insertionSort(lst_movies1, less)

def test_loading_CSV_y_ordenamiento():
    """
    Prueba que se pueda leer el archivo y que despues de relizar el sort, el orden este correcto
    """
    setUp()
    sort.insertionSort(lst_movies,less)
    while not (lt.isEmpty(lst_movies)):
        x = int(lt.removeLast(lst_movies)['id'])
        if not (lt.isEmpty(lst_movies)):
            y = int(lt.lastElement(lst_movies)['id'])
        else:
            break
        assert x > y

def test_loading_CSV_y_ordenamiento():
    """
    Prueba que se pueda leer el archivo y que despues de relizar el sort, el orden este correcto
    """
    setUp()
    sort.insertionSort(lst_movies1,less)
    while not (lt.isEmpty(lst_movies1)):
        x = int(lt.removeLast(lst_movies1)['id'])
        if not (lt.isEmpty(lst_movies1)):
            y = int(lt.lastElement(lst_movies1)['id'])
        else:
            break
        assert x > y