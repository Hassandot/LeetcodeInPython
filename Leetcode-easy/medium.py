from calendar import TUESDAY
from email.errors import FirstHeaderLineIsContinuationDefect
from inspect import stack
from math import floor, sqrt
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
def countMaxOrSubsets(self, nums: List[int]) -> int:
        noc=1<<len(nums)
        maxXOR:int=0
        xors:List[int]=[]
        for i in range(1,noc):
            xor:int=0
            for j in range(len(nums)):
                if i & 1<<j :
                    xor|=nums[j]
            maxXOR=max(maxXOR,xor)
            xors.append(xor)
        return xors.count(maxXOR)
def findArray(pref: List[int]) -> List[int]:
    result:List[int]=[pref[0]]
    return result+[pref[i]^pref[i-1] for i in range(1,len(pref))]
def countPoints(points: List[List[int]], queries: List[List[int]]) -> List[int]:
    result:List[int]=[]
    for q in queries:
        count:int=0
        for p in points:
            ed=sqrt((q[0]-p[0])**2+(q[1]-p[1])**2)
            if ed<=q[2]:
                count+=1
        result.append(count)
    return result
def findMatrix(nums: List[int]) -> List[List[int]]:
    mpp:Dict[int,int]={}
    size:int=0
    for num in nums:
        mpp[num]=mpp.get(num,0)+1
        size=max(size,mpp.get(num))
    res:List[List[int]]=[[] for i in range(size)]
    for i in range(size):
        for key,value in mpp.items():
            if value!=0:
                res[i].append(key)
                mpp[key]-=1
    return res
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rec:List[List[int]]=[]
        col:int=len(rectangle[0])
        for i in range(len(rectangle)):
            row:List[int]=[]
            for j in range(col):
                row.append(rectangle[i][j])
            self.rec.append(row)

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                self.rec[i][j]=newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rec[row][col]
def sortTheStudents(score: List[List[int]], k: int) -> List[List[int]]:
    return sorted(score,reverse=True,key=lambda x:x[k])
def minOperations( nums: List[int], k: int) -> int:
    xors=0
    for num in nums:
        xors^=num
    xor:str=format(xors,'032b')
    kbits:str=format(k,'032b')
    count:int=0
    for i in range(32):
        if xor[i]!=kbits[i]:
            count+=1
    return count
def processQueries(q: List[int], m: int) -> List[int]:
    p:List[int]=[i for i in range(1,m+1)]
    res:List[int]=[]
    for i in range(len(q)):
        ind:int=p.index(q[i])
        res.append(ind)
        temp:int=p.pop(ind)
        p.insert(0,temp)
    return res
def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        return sum([piles[i] for i in range(len(piles)//3,len(piles),2)])
def sortMatrix( grid: List[List[int]]) -> List[List[int]]:
    n=len(grid)
    mat:List[List[int]]=[[0]*n for i in range(n)]
    for i in range(n):
        dg:List[int]=[]
        row:int=i
        for j in range(n-i):
            dg.append(grid[row][j])
            row+=1
        dg.sort(reverse=True)
        sorRow:int=i
        for k in range(len(dg)):
            mat[sorRow][k]=dg[k]
            sorRow+=1
    for i in range(1,n):
        row:List[int]=[]
        col:int=i
        for j in range(n-i):
            row.append(grid[j][col])
            col+=1
        row.sort()
        sorCol:int=i
        for j in range(len(row)):
            mat[j][sorCol]=row[j]
            sorCol+=1
    return mat
def rearrangeArray(self, nums: List[int]) -> List[int]:
        list1:List[int]=[num for num in nums if num>0]
        list2:List[int]=[num for num in nums if num<0]
        res:List[int]=[]
        for i in range(len(nums)//2):
            res.append(list1[i])
            res.append(list2[i])
        return res
def onesMinusZeros(grid: List[List[int]]) -> List[List[int]]:
        row:int=len(grid)
        col:int=len(grid[0])
        mat:List[List[int]]=[[0]*col for i in range(row)]
        colsOnesAndZero:List[Tuple[int,int]]=[]
        for j in range(col):
            column:List[int]=[grid[k][j] for k in range(row)]
            colsOnesAndZero.append((column.count(1),column.count(0)))
        for i in range(row):
            oneRow=grid[i].count(1)
            zeroRow=grid[i].count(0)
            for j in range(col):                
                mat[i][j]=oneRow+colsOnesAndZero[j][0]-zeroRow-colsOnesAndZero[j][1]
        return mat
def diagonalSort(grid: List[List[int]]) -> List[List[int]]:
    m=len(grid)
    n=len(grid[0])
    def sortDiagonal(row:int,col:int):
        dg:List[int]=[]
        i,j=row,col
        while i<m and j<n:
            dg.append(grid[i][j])
            i+=1
            j+=1
        dg.sort(reverse=False)
        idx:int=0
        while i<m and j<n:
            grid[i][j]=dg[idx]
            i+=1
            j+=1
            idx+=1
    for i in range(n):
        sortDiagonal(0,i)
    for i in range(1,m):
        sortDiagonal(i,0)
    return grid
