import pytest 
import config 
from DataStructures import arraylist as slt
import csv



def cmpfunction (element1, element2):
    if element1["id"] == element2["id"]:
        return 0
    elif element1["id"] < element2["id"]:
        return -1
    else:
        return 1

def cargarArchivo(file):
    lista = []
    print("Cargando archivo ....")
    dialect = csv.excel()
    sep = ";"
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, dialect=dialect)
            for row in reader: 
                lista.append(row)
    except:
        print("Se presento un error en la carga del archivo")
    return lista


@pytest.fixture
def lst_1 ():
    lst = slt.newList(cmpfunction)
    return lst

@pytest.fixture
def lst_2 ():
    lst = slt.newList(cmpfunction)
    return lst

@pytest.fixture
def movies_casting():
    casting = cargarArchivo("Data/Movies/MoviesCastingRaw-small.csv")
    return casting

@pytest.fixture
def movies_details():
    details = cargarArchivo("Data/Movies/SmallMoviesDetailsCleaned.csv")
    return details

@pytest.fixture
def lstmovies_casting(movies_casting):
    lst = slt.newList(cmpfunction)
    for i in range(0, len(movies_casting)):
        slt.addLast(lst, movies_casting[i])
    return lst

@pytest.fixture
def lstmovies_details(movies_details):
    lst = slt.newList(cmpfunction)
    for i in range(0, len(movies_details)):
        slt.addLast(lst, movies_details[i])
    return lst
    


def test_empty (lst_1, lst_2):
    assert slt.isEmpty(lst_1) == True
    assert slt.size(lst_1) == 0
    assert slt.isEmpty(lst_2) == True
    assert slt.size(lst_2) == 0



def test_addFirst (lst_1, lst_2, movies_casting, movies_details):
    assert slt.isEmpty(lst_1) == True
    assert slt.size(lst_1) == 0
    slt.addFirst (lst_1, movies_casting[1])
    assert slt.size(lst_1) == 1
    slt.addFirst (lst_1, movies_casting[2])
    assert slt.size(lst_1) == 2
    casting_movie = slt.firstElement(lst_1)
    assert casting_movie == movies_casting[2]

    assert slt.isEmpty(lst_2) == True
    assert slt.size(lst_2) == 0
    slt.addFirst (lst_2, movies_details[1])
    assert slt.size(lst_2) == 1
    slt.addFirst (lst_2, movies_details[2])
    assert slt.size(lst_2) == 2
    details_movie = slt.firstElement(lst_2)
    assert details_movie == movies_details[2]




def test_addLast (lst_1, lst_2, movies_casting, movies_details):
    assert slt.isEmpty(lst_1) == True
    assert slt.size(lst_1) == 0
    slt.addLast (lst_1, movies_casting[1])
    assert slt.size(lst_1) == 1
    slt.addLast (lst_1, movies_casting[2])
    assert slt.size(lst_1) == 2
    casting_movie = slt.firstElement(lst_1)
    assert casting_movie == movies_casting[1]
    casting_movie = slt.lastElement(lst_1)
    assert casting_movie == movies_casting[2]

    assert slt.isEmpty(lst_2) == True
    assert slt.size(lst_2) == 0
    slt.addLast (lst_2, movies_details[1])
    assert slt.size(lst_2) == 1
    slt.addLast (lst_2, movies_details[2])
    assert slt.size(lst_2) == 2
    details_movie = slt.firstElement(lst_2)
    assert details_movie == movies_details[1]
    details_movie = slt.lastElement(lst_2)
    assert details_movie == movies_details[2]




def test_getElement(lstmovies_casting, lstmovies_details, movies_casting, movies_details):
    casting_movie = slt.getElement(lstmovies_casting, 1)
    assert casting_movie == movies_casting[0]
    casting_movie = slt.getElement(lstmovies_casting, 55)
    assert casting_movie == movies_casting[54]

    details_movie = slt.getElement(lstmovies_details, 1)
    assert details_movie == movies_details[0]
    details_movie = slt.getElement(lstmovies_details, 92)
    assert details_movie == movies_details[91]





def test_removeFirst (lstmovies_casting, lstmovies_details, movies_casting, movies_details):
    assert slt.size(lstmovies_casting) == len(movies_casting)
    slt.removeFirst(lstmovies_casting)
    assert slt.size(lstmovies_casting) == (len(movies_casting)-1)
    casting_movie = slt.firstElement(lstmovies_casting)
    assert casting_movie == movies_casting[1]

    assert slt.size(lstmovies_details) == len(movies_details)
    slt.removeFirst(lstmovies_details)
    assert slt.size(lstmovies_details) == (len(movies_details)-1)
    details_movie = slt.firstElement(lstmovies_details)
    assert details_movie == movies_details[1]



def test_removeLast (lstmovies_casting, lstmovies_details, movies_casting, movies_details):
    assert slt.size(lstmovies_casting) == len(movies_casting)
    slt.removeLast(lstmovies_casting)
    assert slt.size(lstmovies_casting) == (len(movies_casting)-1)
    casting_movie = slt.lastElement(lstmovies_casting)
    assert casting_movie == movies_casting[len(movies_casting)-2]

    assert slt.size(lstmovies_details) == len(movies_details)
    slt.removeLast(lstmovies_details)
    assert slt.size(lstmovies_details) == (len(movies_details)-1)
    details_movie = slt.lastElement(lstmovies_details)
    assert details_movie == movies_details[len(movies_details)-2]



def test_insertElement (lst_1, lst_2, movies_casting, movies_details):
    assert slt.isEmpty(lst_1) is True
    assert slt.size(lst_1) == 0
    slt.insertElement(lst_1, movies_casting[0], 1)
    assert slt.size(lst_1) == 1
    slt.insertElement(lst_1, movies_casting[1], 2)
    assert slt.size(lst_1) == 2
    slt.insertElement(lst_1, movies_casting[2], 1)
    assert slt.size(lst_1) == 3
    casting_movie = slt.getElement(lst_1, 1)
    assert casting_movie == movies_casting[2]
    casting_movie = slt.getElement(lst_1, 2)
    assert casting_movie == movies_casting[0]

    assert slt.isEmpty(lst_2) is True
    assert slt.size(lst_2) == 0
    slt.insertElement(lst_2, movies_details[0], 1)
    assert slt.size(lst_2) == 1
    slt.insertElement(lst_2, movies_details[1], 2)
    assert slt.size(lst_2) == 2
    slt.insertElement(lst_2, movies_details[2], 1)
    assert slt.size(lst_2) == 3
    details_movie = slt.getElement(lst_2, 1)
    assert details_movie == movies_details[2]
    details_movie = slt.getElement(lst_2, 2)
    assert details_movie == movies_details[0]



def test_isPresent (lstmovies_casting, lstmovies_details, movies_casting, movies_details):
    casting_1 = {'id':'40000','actor1_name':'John Doe','actor1_gender':'1',\
        'actor2_name':'Jane Doe','actor2_gender':'2','actor3_name':'John Doe','actor3_gender':'1','actor4_name':'Jane Doe','actor4_gender':'2'}
    assert slt.isPresent(lstmovies_casting, movies_casting[200])>0
    assert slt.isPresent(lstmovies_casting, casting_1)==0

    details_1 = {'id':'40000','budget':'30000','genres':'Horror',\
        'imdb_id':'4','original_language':'es','original_title':'El paseo','overview':'na','popularity':'1.500.000','production':'Sony'}
    assert slt.isPresent(lstmovies_details, movies_details[100])>0
    assert slt.isPresent(lstmovies_details, details_1)==0
    


def test_deleteElement (lstmovies_casting, lstmovies_details, movies_casting, movies_details):
    pos = slt.isPresent(lstmovies_casting, movies_casting[400])
    assert pos > 0
    casting_movie = slt.getElement(lstmovies_casting, pos)
    assert casting_movie == movies_casting[400]
    slt.deleteElement(lstmovies_casting, pos)
    assert slt.size(lstmovies_casting) == len(movies_casting) - 1
    casting_movie = slt.getElement(lstmovies_casting, pos)
    assert casting_movie == movies_casting[401]

    pos = slt.isPresent(lstmovies_details, movies_details[400])
    assert pos > 0
    details_movie = slt.getElement(lstmovies_details, pos)
    assert details_movie == movies_details[400]
    slt.deleteElement(lstmovies_details, pos)
    assert slt.size(lstmovies_details) == len(movies_details) - 1
    details_movie = slt.getElement(lstmovies_details, pos)
    assert details_movie == movies_details[401]


def test_changeInfo (lstmovies_casting, lstmovies_details):
    new_casting = {'id':'40000','actor1_name':'John Doe','actor1_gender':'1',\
    'actor2_name':'Jane Doe','actor2_gender':'2','actor3_name':'John Doe','actor3_gender':'1','actor4_name':'Jane Doe','actor4_gender':'2',\
    'actor5_name': 'Brad Pitt', 'actor5_gender':'1', 'actor_number':'4', 'director_name':'Wes Anderson', 'director_gender':'0', 'director_number':'5',\
    'producer_name':'Karen', 'producer_number':'7', 'screenplay':'Carlos', 'editpr_name':'Sylvie Landra'}
    new_details = {'id':'40000','budget':'30000','genres':'Horror',\
    'imdb_id':'4','original_language':'es','original_title':'El paseo','overview':'na','popularity':'1.500.000','production_companies':'Sony',\
    'production_countries':'Austria', 'release_date':'30/06/2005', 'revenue':'736900', 'runtime':'131', 'spoken_languages':'Spanish', 'status':'Released',\
    'title':'Star Wars', 'tagline':'', 'vote_average':'8', 'cote_count':'99', 'production_companies_number':'2', 'production_countries_number':'3',\
    'spoken_languages_number':'1'}

    slt.changeInfo(lstmovies_casting, 1, new_casting)
    assert slt.isPresent(lstmovies_casting, new_casting)>0
    casting_movie = slt.getElement(lstmovies_casting, 1)
    assert new_casting == casting_movie

    slt.changeInfo(lstmovies_details, 1, new_details)
    assert slt.isPresent(lstmovies_details, new_details)>0
    details_movie = slt.getElement(lstmovies_details, 1)
    assert new_details == details_movie


def test_exchange (lstmovies_casting, lstmovies_details, movies_casting, movies_details):
    casting1 = slt.getElement(lstmovies_casting, 229)
    casting2 = slt.getElement(lstmovies_casting, 1541)
    slt.exchange(lstmovies_casting, 229, 1541)
    assert slt.getElement(lstmovies_casting, 229) == casting2
    assert slt.getElement(lstmovies_casting, 1541) == casting1

    details1 = slt.getElement(lstmovies_details, 229)
    details2 = slt.getElement(lstmovies_details, 1541)
    slt.exchange(lstmovies_details, 229, 1541)
    assert slt.getElement(lstmovies_details, 229) == details2
    assert slt.getElement(lstmovies_details, 1541) == details1