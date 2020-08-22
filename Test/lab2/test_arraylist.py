"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import pytest 
import config 
from DataStructures import arraylist as slt
from App import app



def cmpfunction (element1, element2):
    if element1["id"] == element2["id"]:
        return 0
    elif element1["id"] < element2["id"]:
        return -1
    else:
        return 1


@pytest.fixture
def lst_1 ():
    lst = slt.newList(cmpfunction)
    return lst

@pytest.fixture
def lst_2 ():
    lst = slt.newList(cmpfunction)
    return lst


@pytest.fixture
def books ():
    books = []
    books.append({'book_id':'1', 'book_title':'Title 1', 'author':'author 1'})
    books.append({'book_id':'2', 'book_title':'Title 2', 'author':'author 2'})
    books.append({'book_id':'3', 'book_title':'Title 3', 'author':'author 3'})
    books.append({'book_id':'4', 'book_title':'Title 4', 'author':'author 4'})
    books.append({'book_id':'5', 'book_title':'Title 5', 'author':'author 5'})
    print (books[0])
    return books

@pytest.fixture
def movies_casting():
    casting = app.loadCSVFile("Data\Movies\MoviesCastingRaw-small.csv")
    return casting

@pytest.fixture
def movies_details():
    details = app.loadCSVFile("Data\Movies\SmallMoviesDetailsCleaned.csv")
    return details

@pytest.fixture
def lstmovies_casting(movies_casting):
    lst = slt.newList(cmpfunction)
    for i in range(0,len(movies_casting)-1):    
        slt.addLast(lst,casting[i])    
    return lst

@pytest.fixture
def lstmovies_details(movies_details):
    lst = slt.newList(cmpfunction)
    for i in range(0,len(movies_details)-1):    
        slt.addLast(lst,casting[i])    
    return lst


@pytest.fixture
def lstbooks(books):
    lst = slt.newList(cmpfunction)
    for i in range(0,5):    
        slt.addLast(lst,books[i])    
    return lst



def test_empty (lst_1, lst_2):
    assert slt.isEmpty(lst_1) == True
    assert slt.size(lst_1) == 0
    assert slt.isEmpty(lst_2) == True
    assert slt.size(lst_2) == 0



def test_addFirst (lst_1, lst_2, movies_casting, movies_details):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    assert slt.isEmpty(lst_2) == True
    assert slt.size(lst_2) == 0
    slt.addFirst (lst_1, movies_casting[1])
    assert slt.size(lst_1) == 1
    slt.addFirst (lst_1, movies_details[2])
    assert slt.size(lst_1) == 2
    casting = slt.firstElement(lst_1)
    assert casting == movies_casting[2]
    slt.addFirst (lst_2, movies_details[1])
    assert slt.size(lst_1) == 1
    slt.addFirst (lst_2, movies_details[2])
    assert slt.size(lst_2) == 2
    details = slt.firstElement(lst_2)
    assert details == movies_details[2]




def test_addLast (lst, books):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addLast (lst, books[1])
    assert slt.size(lst) == 1
    slt.addLast (lst, books[2])
    assert slt.size(lst) == 2
    book = slt.firstElement(lst)
    assert book == books[1]
    book = slt.lastElement(lst)
    assert book == books[2]




def test_getElement(lstbooks, books):
    book = slt.getElement(lstbooks, 1)
    assert book == books[0]
    book = slt.getElement(lstbooks, 5)
    assert book == books[4]





def test_removeFirst (lstbooks, books):
    assert slt.size(lstbooks) == 5
    slt.removeFirst(lstbooks)
    assert slt.size(lstbooks) == 4
    book = slt.getElement(lstbooks, 1)
    assert book  == books[1]



def test_removeLast (lstbooks, books):
    assert slt.size(lstbooks) == 5
    slt.removeLast(lstbooks)
    assert slt.size(lstbooks) == 4
    book = slt.getElement(lstbooks, 4)
    assert book  == books[3]



def test_insertElement (lst, books):
    assert slt.isEmpty(lst) is True
    assert slt.size(lst) == 0
    slt.insertElement (lst, books[0], 1)
    assert slt.size(lst) == 1
    slt.insertElement (lst, books[1], 2)
    assert slt.size(lst) == 2
    slt.insertElement (lst, books[2], 1)
    assert slt.size(lst) == 3
    book = slt.getElement(lst, 1)
    assert book == books[2]
    book = slt.getElement(lst, 2)
    assert book == books[0]



def test_isPresent (lstbooks, books):
    book = {'book_id':'10', 'book_title':'Title 10', 'author':'author 10'}
    print(slt.isPresent (lstbooks, books[2]))
    assert slt.isPresent (lstbooks, books[2]) > 0
    assert slt.isPresent (lstbooks, book) == 0
    


def test_deleteElement (lstbooks, books):
    pos = slt.isPresent (lstbooks, books[2])
    assert pos > 0
    book = slt.getElement(lstbooks, pos)
    assert book == books[2]
    slt.deleteElement (lstbooks, pos)
    assert slt.size(lstbooks) == 4
    book = slt.getElement(lstbooks, pos)
    assert book == books[3]


def test_changeInfo (lstbooks):
    book10 = {'book_id':'10', 'book_title':'Title 10', 'author':'author 10'}
    slt.changeInfo (lstbooks, 1, book10)
    book = slt.getElement(lstbooks, 1)
    assert book10 == book


def test_exchange (lstbooks, books):
    book1 = slt.getElement(lstbooks, 1)
    book5 = slt.getElement(lstbooks, 5)
    slt.exchange (lstbooks, 1, 5)
    assert slt.getElement(lstbooks, 1) == book5
    assert slt.getElement(lstbooks, 5) == book1