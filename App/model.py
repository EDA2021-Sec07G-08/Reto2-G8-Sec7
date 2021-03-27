﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog():
    """ Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
                'videos_by_id': None,
                'videos_by_category_ids': None}

    """
    Esta lista contiene todo los libros encontrados
    en los archivos de carga.  Estos libros no estan
    ordenados por ningun criterio.  Son referenciados
    por los indices creados a continuacion.
    """
    catalog['videos'] = lt.newList('ARRAY_LIST', compareVideosIds)

    catalog['videos_by_id'] = mp.newMap(375943, maptype='PROBING', loadfactor=0.5, comparefunction=compareVideosIds)

    catalog['videos_by_category_ids'] = mp.newMap(37, maptype='CHAINING', loadfactor = 4.0, comparefunction = compareVideosByCategory)

    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):

    lt.addLast(catalog['videos'], video)
    mp.put(catalog['videos_by_id'], video['video_id'], video)
    addCategoryVideo(catalog, video)

def addCategoryVideo(catalog, video):

    categories = catalog['videos_by_category_ids']
    category_id = video['category_id']
    entrada = mp.get(categories, category_id)
    videos_cat = me.getValue(entrada)
    lt.addLast(videos_cat['videos'], video)

def addCategory(catalog, category):

    categories = catalog['videos_by_category_ids']
    category_id = video['category_id']
    existCate = mp.contains(categories, category_id)
    videos_cat = newCategory(category)
    mp.put(categories, category_id, videos_cat)

def newCategory(category):
    entrada = {'category_id': '', 'category_name': '', 'videos': None}
    entrada['category_id'] = category['id']
    entrada['category_name'] = category['name']
    entrada['videos'] = lt.newList('LINKED_LIST', compareVideosByCategory)

# Funciones para creacion de datos

# Funciones de consulta

def videosSize(catalog):

    return lt.size(catalog['videos'])

def categoriesSize(catalog):

    return lt.size(catalog['categoryIds'])

# Funciones utilizadas para comparar elementos dentro de una lista

def compareVideosIds(id1, id2):
    if(id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else: 
        return -1

def compareMapVideosIds(id, entrada):
    identidad = me.getKey(entrada)
    if(id1 == entrada):
        return 0
    elif(id1 > entrada):
        return 1
    else:
        return -1

def compareVideosByCategory(keyname, category):
    catentry = me.getKey(category)
    if (keyname == catentry):
        return 0
    elif (keyname > catentry):
        return 1
    else:
        return -1


# Funciones de ordenamiento
