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
from typing import List,Dict, Optional, Reversible,Tuple,Set
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
def checkArithmeticSubarrays( nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    res:List[bool]=[]
    for i in range(len(l)):
        newArray:List[int]=nums[l[i]:r[i]+1]
        newArray.sort(reverse=False)
        diff:int=newArray[1]-newArray[0]
        flag:bool=True
        for j in range(2,len(newArray)):
            if newArray[j]-newArray[j-1]!=diff:
                flag=False
                break
        res.append(flag)
    return res

def maxDistinct(self, s: str) -> int:
        return len(set(s))

class Codec:
    def __init__(self):
        self._encryptTable:Dict[str,str]={}
        self._decryptTable:Dict[str,str]={}
        self.initializeTable()
    def initializeTable(self):
        key = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        self._encryptTable=dict(zip(alphabet,key))
        self._decryptTable=dict(zip(key,alphabet))
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        cipher:str=''
        for character in longUrl:
            if character.isalpha():
                cipher+=self._encryptTable[character]
            else:
                cipher+=character
        return cipher

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        plaintext:str=''
        for character in shortUrl:
            if character.isalpha():
                plaintext+=self._decryptTable[character]
            else:
                plaintext+=character
        return plaintext
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans:List[int]=[0]
        def dfs(node:TreeNode,maximum:int):
            if node is None:
                return 
            if node.val>=maximum:
                ans[0]+=1
            dfs(node.left,max(maximum,node.val))
            dfs(node.right,max(maximum,node.val))

        dfs(root,float('-inf'))
        return ans[0]
    

def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans:List[int]=[0]
        def dfs(node:TreeNode,low:int,high:int)->int:
            if node is None:
                return 0
            if low<=node.val<=high:
                ans[0]+=node.val
            l=dfs(node.left,low,high)
            r=dfs(node.right,low,high)
            
        dfs(root,low,high)
        return ans[0]

def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    l=self.maxDepth(root.left)
    r=self.maxDepth(root.right)
    return 1+max(l,r)

def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l=self.minDepth(root.left)
        r=self.minDepth(root.right)
        if root.left is None:
            return 1+r
        elif root.right is None:
            return 1+l
        return 1+min(l,r)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans:List[int]=[0]
        def dfs(node:TreeNode)->int:
            if node is None:
                return -1
            l=dfs(node.left)
            r=dfs(node.right)

            ans[0]=max(ans[0],l+r+2)
            return 1+max(l,r)
        dfs(root)
        return ans[0]
    
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return targetSum-root.val == 0
        l=self.hasPathSum(root.left,targetSum-root.val)
        r=self.hasPathSum(root.right,targetSum-root.val)
        return l or r

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val==val:
            return root
        elif val<root.val:
            return self.searchBST(root.left,val)
        return self.searchBST(root.right,val)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node:TreeNode,low:int,high:int)->bool:
            if node is None:
                return True

            if low<node.val<high:
                l=dfs(node.left,low,node.val)
                r=dfs(node.right,node.val,high)
            else:
                return False
            return l and r
        return dfs(root,float('-inf'),float('inf'))
    
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val!=q.val:
            return False
        l=self.isSameTree(p.left,q.left)
        r=self.isSameTree(p.right,q.right)
        return l and r
    
class Solution:
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            elif p.val!=q.val:
                return False
            l=isSameTree(p.left,q.left)
            r=isSameTree(p.right,q.right)
            return l and r
        if root is None:
            return False
        if isSameTree(root,subRoot):
            return True
        l=self.isSubtree(root.left,subRoot)
        r=self.isSubtree(root.right,subRoot)
        return l or r
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans:List[int]=[]
        def helper(node):
            if node is None:
                return 
            helper(node.left)
            ans.append(node.val)
            helper(node.right)
        helper(root)
        return ans
    
def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSameTree( p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            elif p.val!=q.val:
                return False
            l=isSameTree(p.left,q.right)
            r=isSameTree(p.right,q.left)
            return l and r
        return isSameTree(root.left,root.right)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans=[0]
        def helper(node):
            if node is None:
                return 0
            lh=helper(node.left)
            rh=helper(node.right)

            ans[0]=max(ans[0],abs(lh-rh))
            return 1+max(lh,rh)
        helper(root)
        if ans[0]>1:
            return False
        return True
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans:List[int]=[]
        def dfs(node):
            if node is None:
                return
            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ans
    
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans:List[int]=[]
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            ans.append(node.val)
        dfs(root)
        return ans    
    
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return root.val
        l=self.checkTree(root.left)
        r=self.checkTree(root.right)
        return root.val==l+r

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans:List[str]=[]
        def dfs(root:TreeNode,path:str):
            if root is None:
                return 
            if path:
                path=path+'->'+str(root.val)
            else:
                path=str(root.val)

            if root.left is None and root.right is None:
                ans.append(path)
                return 
            dfs(root.left,path)
            dfs(root.right,path)
        dfs(root,'')
        return ans


def minimumOperations(grid: List[List[int]]) -> int:
    total:int=0
    col:int=len(grid[0])
    rows:int=len(grid)
    for i in range(col):
        currentSum:int=0
        actualSum:int=0
        starter:int=grid[0][i]
        for j in range(rows):
            currentSum+=grid[j][i]
            actualSum+=starter
            starter+=1
        total+=actualSum-currentSum
    return total
def findKOr(self, nums: List[int], k: int) -> int:
        mpp:Dict[int,int]={}

        for num in nums:
            binary=format(int(num),'0b')
            n=len(binary)
            for i in range(n-1,-1,-1):
                index=(n-1)-i
                mpp[index]=mpp.get(index,0)+int(binary[i])
        mat:List[List[int]]=[[key,value]  for (key,value) in mpp.items()]
        mat.sort(reverse=True,key=lambda x : x[0])
        number:str=''
        for x in mat:
            if x[1]>=k:
                number+='1'
            else:
                number+='0'
        return int(number,2)
def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans=[0]
        def dfs(node,left):
            if node is None:
                return 
            if node.left is None and node.right is None and left==True:
                ans[0]+=node.val
            dfs(node.left,True)
            dfs(node.right,False)
        dfs(root,False)
        return ans[0]
def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans:List[int]=[0]
        mpp:Dict[int,int]={}
        def dfs(node):
            if node is None:
                return 
            mpp[node.val]=mpp.get(node.val,0)+1
            ans[0]=max(mpp.get(node.val),ans[0])
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        res:List[int]=[key for (key,value) in mpp.items() if value==ans[0]]
        return res

def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    ans:List[int]=[]
    def dfs(node):
        if node is None:
            return 
        ans.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    arr=sorted(ans,reverse=False)
    md:int=float('inf')
    for i in range(len(arr)-1):
        md=min(md,abs(arr[i+1]-arr[i]))
    return md

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        mid=len(nums)//2
        node:TreeNode=TreeNode(nums[mid])    
        node.left=self.sortedArrayToBST(nums[:mid])
        node.right=self.sortedArrayToBST(nums[mid+1:])
        return node    

def permute(self, nums: List[int]) -> List[List[int]]:
        res:List[int]=[]
        used:List[bool]=[False]*len(nums)
        def backtrack(current:List[int]):
            if len(current)==len(nums):
                res.append(current)
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i]=True
                    newCurrent:List[int]=copy.copy(current)
                    newCurrent.append(nums[i])
                    backtrack(newCurrent)
                    used[i]=False
            
        backtrack([])
        return res
def letterCasePermutation(self, s: str) -> List[str]:
        res=[]
        k=len(s)
        def bt(start,current):
            if len(current)==k:
                res.append(current)
                return 
            
            if s[start].isdigit():
                bt(start+1,current+s[start])
            else:
                bt(start+1,current+s[start].lower())
                bt(start+1,current+s[start].upper())
        bt(0,'')
        return res



def getHappyString( n: int, k: int) -> str:
        res=[]
        def bt(current):
            if len(current)==n:
                res.append(current)
                return 
            for ch in 'abc':
                if current and current[-1]==ch:
                    continue
                bt(current+ch)
        bt('')
        if len(res)>=k:
            return res[k-1]
        return ''

