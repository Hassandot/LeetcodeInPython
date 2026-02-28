from calendar import TUESDAY
from email.errors import FirstHeaderLineIsContinuationDefect
from inspect import stack
from math import floor
from operator import mul
from statistics import mean
from sys import set_coroutine_origin_tracking_depth
from tkinter import CURRENT, FIRST
from token import LESS
from tokenize import Double
from turtle import Turtle
from typing import List,Dict, Reversible,Tuple,Set
from unicodedata import digit
from xml.dom import minicompat
from xmlrpc.client import MININT
vector :List[float]=[]
unordered_map :Dict[int,int]={}
ordered_map :Dict[int,int]={}
pair :Tuple[int,int]=None
def findThePrefixCommonArray( A: List[int], B: List[int]) -> List[int]:
    result:List[int]=[]
    for i in range(len(A)):
        count:int=0
        temp:List[int]=B[:i+1]
        for j in range(i+1):
            count+=1 if A[j] in temp else 0
        result.append(count)
    return result

