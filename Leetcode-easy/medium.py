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

def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        mpp={}
        r=len(nums)
        for num in nums:
            mpp[num]=mpp.get(num,0)+1
        def bt(current):
            if r==len(current):
                res.append(current)
                return
            for num in mpp:
                if mpp[num]>0:
                    mpp[num]-=1
                    newCurr=current[:]
                    newCurr.append(num)
                    bt(newCurr)
                    mpp[num]+=1
        bt([])
        return res
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def bt(start,current):
            if sum(current)==target:
                res.append(current)
                return
            
            for i in range(start,len(candidates)):
                if sum(current)<target:
                    newCurr=current[:]
                    newCurr.append(candidates[i])
                    bt(i,newCurr)
                else:
                    return
        bt(0,[])
        return res

def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        def bt(start,current):
            s=sum(current)
            if s==target:
                res.append(current)
                return
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                if s+nums[i]>target:
                    break

                newCurr=current[:]
                newCurr.append(nums[i])
                bt(i+1,newCurr)
                
        bt(0,[])
        return res

def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        nums=[i for i in range(1,10)]
        def bt(start,current):
            s=sum(current)
            if s==n and len(current)==k:
                res.append(current)
                return
            if s>n:
                return
            for i in range(start,len(nums)):
                newCurr=current[:]
                newCurr.append(nums[i])
                bt(i+1,newCurr)
        bt(0,[])
        return res

def numTilePossibilities(self, tiles: str) -> int:
        res=[]
        mpp={}
        for t in tiles:
            mpp[t]=mpp.get(t,0)+1


        def bt(current):
            if current:
                res.append(current)
            for t in mpp:
                if mpp[t]>0:
                    mpp[t]-=1
                    current.append(t)
                    bt(current)
                    current.pop()
                    mpp[t]+=1
        bt([])
        return len(res)

def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def bt(start,current):
            seen=set()
            if len(current)>=2:
                res.append(current)
            for i in range(start,len(nums)):
                if nums[i] in seen:
                    continue
                if not current or nums[i]>=current[-1]:
                    seen.add(nums[i])
                    newCurr=current[:]
                    newCurr.append(nums[i])
                    bt(i+1,newCurr)

        bt(0,[])
        return res

def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr=[]
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)
        prefix=[0]*(len(arr)+1)
        arr.reverse()
        for i in range(1,len(prefix)):
            prefix[i]=prefix[i-1]+arr[i-1]
        gst=prefix[1:]
        gst.reverse()
        idx=[0]
        def insertionInBST(node,i):
            if node is None:
                return
            insertionInBST(node.left,i+1)
            node.val=gst[idx[0]]
            idx[0]+=1
            insertionInBST(node.right,i+1)
        
        insertionInBST(root,0)
        return root

def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def getHeight(node):
            if node is None:
                return 0
            l=getHeight(node.left)
            r=getHeight(node.right)
            return 1+max(l,r)
        maxHeight=getHeight(root)
        total=[0]
        def dfs(node,depth=1):
            if node is None:
                return
            if depth==maxHeight:
                total[0]+=node.val
            depth+=1
            dfs(node.left,depth)
            dfs(node.right,depth)
        dfs(root)
        return total[0]
def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr=[]
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        arr.sort()
        dfs(root)
        def makeTree(nums):
            if len(nums)==0:
                return None
            mid=len(nums)//2
            node:TreeNode=TreeNode(nums[mid])
            node.left=makeTree(nums[:mid])
            node.right=makeTree(nums[mid+1:])
            return node
        return makeTree(arr)

def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(arr):
            if len(arr)==0:
                return None
            m=max(arr)
            idx=arr.index(m)
            node:TreeNode=TreeNode(m)
            node.left=dfs(arr[:idx])
            node.right=dfs(arr[idx+1:])
            return node
        return dfs(nums)
def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mpp={}
        for num in nums:
            mpp[num]=mpp.get(num,0)+1
        sor=[(key,value) for key,value in mpp.items()]
        sor.sort(key=lambda x:x[0])
        idx=0
        for s in sor:
            for i in range(mpp[s[0]]):
                nums[idx]=s[0]
                idx+=1
def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        indexes=[]
        
        def makezero(row,col):
            for i in range(n):
                matrix[row][i]=0
                
            for i in range(m):
                matrix[i][col]=0
                
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    indexes.append((i,j))

        for i,j in indexes:
            makezero(i,j)    
def majorityElement(self, nums: List[int]) -> List[int]:
        k=len(nums)//3
        mpp={}
        for num in nums:
            mpp[num]=mpp.get(num,0)+1
        res=[]
        for key,value in mpp.items():
            if value>k:
                res.append(key)
        return res
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        res=[]
        queue=deque([root])
        while queue:
            level=[]
            level_size=len(queue)
            for i in range(level_size):
                node=queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res

def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        arr1=[]
        arr2=[]
        def dfs(node,arr):
            if node is None:
                return
            arr.append(node.val)
            dfs(node.left,arr)
            dfs(node.right,arr)
        dfs(root1,arr1)
        dfs(root2,arr2)
        arr=arr1+arr2
        return sorted(arr)


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mpp={}
        for num in nums:
            mpp[num]=mpp.get(num,0)+1
        arr=[(key,value) for key,value in mpp.items()]
        arr.sort(reverse=True,key=lambda x:x[1])
        res=[]
        for i,x in enumerate(arr):
            if i==k:
                break
            res.append(x[0])
        return res  
def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*(len(nums)+1)
        suffix=[1]*(len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1]=prefix[i]*nums[i]
        for i in range(len(nums)-1,-1,-1):
            suffix[i]=suffix[i+1]*nums[i]
        res=[]
        for i in range(len(nums)):
            res.append(prefix[i]*suffix[i+1])
        return res
def minOperations(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        for i in range(n):
            if nums[i]==0 and i!=n-2 and i!=n-1:
                count+=1
                nums[i]=1
                if i+1<n:
                    nums[i+1]=nums[i+1]^1
                if i+2<n:
                    nums[i+2]=nums[i+2]^1
        res=all(x==1 for x in nums)
        if res:
            return count
        return -1

class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] in '+-*/':
                secondnumber=stack.pop()
                firstnumber=stack.pop()
                if tokens[i]=='+':
                    stack.append(firstnumber+secondnumber)
                elif tokens[i]=='-':
                    stack.append(firstnumber-secondnumber)
                elif tokens[i]=='*':
                    stack.append(firstnumber*secondnumber)
                else :
                    stack.append(int(float(firstnumber)/secondnumber))
            else:
                stack.append(int(tokens[i]))
        return stack.pop()

def dailyTemperatures(self, t: List[int]) -> List[int]:
        res=[0]*len(t)
        stack=[]
        for i in range(len(t)):
            if not stack:
                stack.append(i)
                continue
            else:
                while stack and t[stack[-1]]<t[i]:
                    res[stack[-1]]=i-stack[-1]
                    stack.pop()
                stack.append(i)
        return res
class StockSpanner:

    def __init__(self):
        self.prices=[]
        self.stack=[]
        self.index=0
    def next(self, price: int) -> int:
        self.prices.append(price)
        while self.stack and self.prices[self.stack[-1]]<=price:
            self.stack.pop()
        res=0
        if not self.stack:
            res=self.index+1
        else:
            res=self.index-self.stack[-1]
        self.stack.append(self.index)
        self.index+=1
        return res
def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD=10**9+7
        for q in queries:
            idx=q[0]
            while idx<=q[1]:
                nums[idx]=(nums[idx]*q[3])%MOD
                idx+=q[2]
        res=0
        for num in nums:
            res^=num
        return res
def gcd(dividend,divisor):
        if divisor==0:
            return dividend
        return gcd(divisor,dividend%divisor)
def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        while head!=None:
            arr.append(head.val)
            head=head.next
        gcds=[]
        for i in range(len(arr)-1):
            gcds.append(gcd(arr[i],arr[i+1]))
        res=[]
        i=0
        n=len(gcds)
        for num in arr:
            res.append(num)
            if i<n: 
                res.append(gcds[i])
            i+=1
        dummy=ListNode(0)
        head=dummy
        for i in range(len(res)):
            new=ListNode(res[i])
            head.next=new
            head=head.next
        return dummy.next


def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mpp={}
        while head:
            if mpp.get(head,False)==False:
                mpp[head]=True
            elif mpp[head]:
                return head
            head=head.next
        return None
def removetheNthNodefromEnd(head,n):
        dummy=ListNode(0)
        dummy.next=head
        slow=dummy
        fast=dummy
        for i in range(n):
            fast=fast.next
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return dummy.next
def lengthOfLongestSubstring(s: str) -> int:
    maxLength=0
    mpp={}
    i,j=0,0
    while j<len(s):
        mpp[s[j]]=mpp.get(s[j],0)+1
        if mpp[s[j]]==2:
            maxLength=max(maxLength,j-i)
            while s[j]!=s[i]:
                mpp[s[i]]-=1
                i+=1
            mpp[s[j]]-=1
            i+=1
            j+=1
        else:
            j+=1
    return max(maxLength,j-i)
def countDistinctIntegers(self, nums: List[int]) -> int:
        mpp={}
        for num in nums:
            mpp[num]=mpp.get(num,0)+1
            temp=int(str(num)[::-1])
            mpp[temp]=mpp.get(temp,0)+1    
        count=0
        for _ in mpp.items():
            count+=1
        return count
def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        mpp1={}
        for log in logs:
            mpp1[log[0]]=mpp1.get(log[0],[])
            mpp1[log[0]].append(log[1])
        res=[0]*k
        mpp2={}
        for log in mpp1.items():
            kk=len(set(log[1]))
            mpp2[kk]=mpp2.get(kk,0)+1
        for log in mpp2.items():
            if log[0]>=1 and log[0]<=k:
                res[log[0]-1]=log[1]
        return res


