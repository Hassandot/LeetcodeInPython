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
from typing import List,Dict, Optional, Reversible,Tuple,Set
from unicodedata import digit
from xml.dom import minicompat
from xmlrpc.client import MININT
vector :List[float]=[]
unordered_map :Dict[int,int]={}
ordered_map :Dict[int,int]={}
pair :Tuple[int,int]=None
def buildArray(nums: List[int]) -> List[int]:
    result:List[int]=[0]*len(nums)
    for i in range(len(nums)):
        result[i]=nums[nums[i]]
    return result
def buildArrays(nums:List[int])->List[int]:
    return [nums[nums[i]] for i in range(len(nums))]
def minimumOperations( nums: List[int]) -> int:
    count:int=0
    for num in nums:
        if num%3!=0:
            count=count+1
    return count
def recoverOrder( order: List[int], friends: List[int]) -> List[int]:
    result:List[int]=None
    for o in order:
        if o in friends:
            result.append(o)
    return result
def recoverorder(order:List[int] , friends:List[int])-> List[int]:
    friends_set=Set(friends)
    return[o for o in order if o in friends_set]
def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans:int=0
        mpp:Dict[str,int]={'++X':1,'X++':1,'--X':-1,'X--':-1}
        for operate in operations:
            ans=ans+mpp[operate]
        return ans
def finalValue(operations:List[str])->int:
    mpp:Dict[str,int]={'++X':1,'X++':1,'--X':-1,'X--':-1}
    return sum([mpp[o] for o in operations])
def findWordsContaining(self, words: List[str], x: str) -> List[int]:
    return [i for i in range(len(words)) if x in words[i]]
def makeCombinations(nums:List[int])->List[List[int]]:
    combinations:List[List[int]]=[]
    numberOfCombinations:int=1<<len(nums)
    for mask in range(numberOfCombinations):
        subset:List[int]=[]
        for i in range(len(nums)):
            if (mask & (1<<i))!=0:
                subset.append(nums[i])
        combinations.append(subset)
    return combinations
def subsetXORSum(self, nums: List[int]) -> int:
    totalSum:int=0
    noOfCom:int=1<<len(nums)
    for mask in noOfCom:
        sumXor:int=0
        for i in range(len(nums)):
            if (mask & (1<<i))!=0:
                sumXor^=nums[i]
        totalSum+=sumXor
    return totalSum
def getSneakyNumbers(self, nums: List[int]) -> List[int]:
    mpp:Dict[int,int]={}
    result:List[int]=[]
    for num in nums:
        mpp[num]=mpp.get(num,0)+1
        if mpp[num]>1:
            result.append(num)
    return result
def numIdenticalPairs( nums: List[int]) -> int:
    return sum([1 for i in range(len(nums)-1) for j in range(i+1,len(nums)) if nums[j]==nums[i]])
def transformArray(nums: List[int]) -> List[int]:
    return sorted([1 if num&1 else 0 for num in nums],reverse=False)
def alternatingSum(self, nums: List[int]) -> int:
     return sum([nums[i] if not(i&1) else -1*nums[i] for i in range(len(nums))])
def dominantIndex(nums: List[int]) -> int:
     index=nums.index(max(nums))  
     nums.sort()
     num=max(nums)
     for i in range(len(nums)-1):
         if nums[i]*2 > num:
             return -1
     return index
def findMaxAverage(nums: List[int], k: int) -> float:
    window_sum:int=sum(nums[:k])
    max_avg:int=window_sum/k
    for i in range(k,len(nums)):
        window_sum+=nums[i]
        window_sum-=nums[i-k]
        max_avg=max(max_avg,window_sum/4)
    return max_avg
def maximumProduct( nums: List[int]) -> int:
    nums.sort(reverse=True)
    return nums[0]*nums[1]*nums[2]
def imageSmoother(img: List[List[int]]) -> List[List[int]]:
    res:List[List[int]]=[[0 for _ in range(len(img[0]))] for _ in range(len(img))]
    for i in range(len(img)):
        for j in range(len(img[i])):
            current_sum:int=0
            count:int=1
            current_sum+=img[i][j]
            if j-1>=0:
                current_sum+=img[i][j-1]
                count+=1
            if j+1<len(img[i]):
                current_sum+=img[i][j+1]
                count+=1
            if i-1>=0:
                current_sum+=img[i-1][j]
                count+=1
            if i+1<len(img):
                current_sum+=img[i+1][j]
                count+=1
            if i-1>=0 and j-1>=0:
                current_sum+=img[i-1][j-1]
                count+=1
            if i+1<len(img) and j+1<len(img[i]):
                current_sum+=img[i+1][j+1]
                count+=1
            if j-1>=0 and i+1<len(img):
                current_sum+=img[i+1][j-1]
                count+=1
            if i-1>=0 and j+1<len(img[i]):
                current_sum+=img[i-1][j+1]
                count+=1

            res[i][j]=current_sum//count
    return res
def largestTriangleArea( points: List[List[int]]) -> float:
    max_x:int=float('-inf')
    max_y:int=float('-inf')
    for row in points:
        max_x=max(max_x,row[0])
        max_y=max(max_y,row[1])
    return (max_x*max_y)/2


    def commonChars(words: List[str]) -> List[str]:
        mpp:Dict[str,int]={}
        for ch in words[0]:
            mpp[ch]=mpp.get(ch,0)+1
        for i in range(1,len(words)):
            temp_word=set(words[i])
            for ch in mpp.keys():
                mpp[ch]=min(mpp.get(ch,0),words[i].count(ch))
        return [key for (key,value) in mpp.items() for i in range(value)]    
def countLargestGroup( n: int) -> int:
    mpp:Dict[int,int]={}
    maxLength:int=0
    for i in range(1,n):
        number:str=str(i)
        if len(number)>1:
            digitSum:int=sum(int(digit) for digit in number)
            mpp[digitSum]=mpp.get(digitSum,0)+1
        mpp[int(number)]=mpp.get(int(number),0)+1
    for value in mpp.values():
        maxLength=max(maxLength,value)
    groups:int=0
    for (key,value) in mpp.items():
        if value==maxLength:
            groups+=1
    return groups
def unequalTriplets( nums: List[int]) -> int:
    count:int=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i]!=nums[j] and nums[i]!=nums[k] and nums[i]!=nums[k]:
                    count+=1
    return count
def minOperations(self, nums: List[int], k: int) -> int:
    unique_numbers:Set[int]=set(nums)
    count:int=0
    less_thenK:int=0
    for num in unique_numbers:
        if num>k:
            count+=1
        if num<k:
            less_thenK+=1
    if count>0:
        return count
    if less_thenK>0:
        return -1
    return 0
def absDifference(self, nums: List[int], k: int) -> int:
    sortedList=sorted(nums,reverse=True)
    return abs(sum(sortedList[:k])-sum(sortedList[-k:]))
def minimumAbsDifference( arr: List[int]) -> List[List[int]]:
    sortedList=sorted(arr,reverse=False)
    minDifference:int=float('inf')
    for i in range(len(sortedList)-1):
        minDifference=min(sortedList[i+1]-sortedList[i])
    res:List[List[int]]=[]
    for i in range(len(arr)-1):
        if (sortedList[i+1]-sortedList[i])==minDifference:
            res.append([sortedList[i],sortedList[i+1]])
    return res
def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
    tempList:List[List[int,List[int]]]=[[abs(rCenter-i)+abs(cCenter-j),[i,j]] for i in range(rows) for j in range(cols)]
    sortedList:List[List[int,List[int]]]=sorted(tempList,key=lambda x: x[0])
    return [l[1] for l in sortedList]
def sortedSquares(self, nums: List[int]) -> List[int]:
    return sorted([num**2 for num in nums])
def resultArray(self, nums: List[int]) -> List[int]:
    arr1:List[int]=[]
    arr2:List[int]=[]
    arr1.append(nums[0])
    arr2.append(nums[1])
    for i in range(2,len(nums)):
        if arr1[-1]>arr2[-1]:
            arr1.append(nums[i])
        else:
            arr2.append(nums[i])
    return arr1+arr2
def smallestRangeI(self, nums: List[int], k: int) -> int:
    for i in range(len(nums)):
        if nums[i]>=-k and nums[i]<=k:
            nums[i]=k
        else:
            nums[i]=(nums[i]-k)
    return max(nums)-min(nums)
def splitNum(self, num: int) -> int:
    num1:str=''
    num2:str=''
    number:str=str(num)
    sortedNumber:str=sorted(number,key=lambda x: int(x))
    for i in range(len(sortedNumber)):
        if i%2==0:
            num1+=sortedNumber[i]
        else:
            num2+=sortedNumber[i]
    return int(num1)+int(num2)
def maximizeExpressionOfThree(self, nums: List[int]) -> int:
    nums.sort(nums,reverse=True)
    return nums[0]+nums[1]-nums[-1]
def trimMean(arr: List[int]) -> float:
    fivePrecentage:int=int(len(arr)*0.05)
    arr.sort()
    totalSum:float=sum([arr[i] for i in range(fivePrecentage,len(arr)-fivePrecentage)])
    return float(totalSum/(len(arr)-(2*fivePrecentage)))
def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
    arr1.sort()
    arr2.sort()
    count:int=0
    for num1 in arr1:
        flag:bool =False
        for num2 in arr2:
            if abs(num1-num2)<=d:
                flag=True
                break
        if not flag:
            count+=1
    return count
def sortArrayByParityII(self, nums: List[int]) -> List[int]:
    res:List[int]=[]
    sortedArray:List[int]=sorted(nums,key=lambda x : x%2==True)
    countOfEven:int=sum([1 for num in nums if num%2==0])
    reverseCounter:int=1
    for i in range(0,countOfEven):
        res.append(sortedArray[i])
        res.append(sortedArray[-reverseCounter])
        reverseCounter+=1
    return res
def maxProduct(self, n: int) -> int:
    number:str=str(n)
    sortedNumber:str=sorted(number,key=lambda x : int(x),reverse=True)
    return int(sortedNumber[0])*int(sortedNumber[1])
def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
    arr.sort()
    flag:bool =True
    d:int=arr[1]-arr[0]
    for i in range(1,len(arr)-1):
        if arr[i+1]-arr[i]!=d:
            flag=False
            break
    return flag
def intersection(self, nums: List[List[int]]) -> List[int]:
    res:List[int]=[]
    search:List[int]=nums[0]
    for i in range(len(search)):
        flag:bool =True
        for j in range(1,len(nums)):
            if search[i] not in nums[j]:
                flag=False
                break
        if flag:
            res.append(search[i])
    return res
def residuePrefixes(s: str) -> int:
    count:int=0
    mpp:Dict[str,int]={}
    for i in range(len(s)):
        mpp[s[i]]=mpp.get(s[i],0)+1
        if len(mpp)==(i+1)%3:
            count+=1

    return count
def validateCoupons( code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
      def checkCode(code:str)->bool:
            if len(code)==0:
                return False
            for char in code:
                if not (char.isalpha() or char.isdigit() or char=='_'):
                    return False
            return True

      def checkBuisnessLine(buisnessLine:str)->bool:
            category:Set[str]=["electronics", "grocery", "pharmacy", "restaurant"]
            if buisnessLine not in category:
                return False
            return True

      res:List[Tuple[str,str]]=[]
      for i in range(len(code)):
         if checkCode(code[i])==True and checkBuisnessLine(businessLine[i])==True and isActive[i]==True:
             res.append([code[i],businessLine[i]])
    
      sortedList:List[Tuple[str,str]]=sorted(res,key=lambda x:(x[1],x[0]))
      return [t[0] for t in sortedList]
def isTrionic( nums: List[int]) -> bool:
    
    firstIncreasing:bool=False
    secondDecreasing:bool=False
    thirdIncreasing:bool=False
    
    i:int=0
    while i<len(nums)-1:
        if nums[i]<nums[i+1]:
            firstIncreasing=True
        else:
            break
        i+=1
    p:int=i
    q:int=0
    while i<len(nums)-1:
        if nums[i]>nums[i+1]:
            secondDecreasing=True
        else:
            break
        i+=1
    q=i
    while i<len(nums)-1:
        if nums[i]<nums[i+1]:
            thirdIncreasing=True
        else:
            break
        i+=1
    for i in range(p):
        if not nums[i]<nums[i+1]:
            return False
    for i in range(p,q):
        if not nums[i]>nums[i+1]:
            return False
    for i in range(q,len(nums)-1):
        if not nums[i]<nums[i+1]:
            return False

    return firstIncreasing and secondDecreasing and thirdIncreasing
def findErrorNums(nums: List[int]) -> List[int]:
    mpp:Dict[int,int]={}
    for num in nums:
        mpp[num]=mpp.get(num,0)+1
    missingNumber:int=0
    doubleNumber:int=0
    for i in range(1,len(nums)+1):
        num:int=mpp.get(i,0)
        if num==0:
            missingNumber=i
        if num==2:
            doubleNumber=i
    return [doubleNumber,missingNumber]
def smallerNumbersThanCurrent( nums: List[int]) -> List[int]:
    uniqueNumber:Set[int]=set(nums)
    mpp:Dict[int,int]={}
    for num in nums:
        mpp[num]=mpp.get(num,0)+1
    res:List[int]=[]
    for i in range(len(nums)):
        currentCount:int=0
        for num in uniqueNumber:
            if num<nums[i]:
                currentCount+=mpp.get(num,0)
        res.append(currentCount)
    return res
def findDisappearedNumbers(nums: List[int]) -> List[int]:
    stt:Set[int]=set([nums[i] for i in range(len(nums))])
    res:List[int]=[]
    for i in range(1,len(nums)+1):
        if i not in stt:
           res.append(i)
    return res
def minimumCost(self, nums: List[int]) -> int:
    total:int=0
    total+=nums[0]
    nums[1:]=sorted(nums[1:])
    return sum(nums[1:3])+total
def constructTransformedArray( nums: List[int]) -> List[int]:
    res:List[int]=[0]*len(nums)
    n:int=len(nums)
    for i in range(n):
        if nums[i]>0:
            res[i]=nums[(i+nums[i])%n]
        else:
            res[i]=nums[(i-abs(nums[i])+n)%n]
    return res
def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
    list1:List[int]=[]
    list2:List[int]=[]
    list3:List[int]=[]
    for num in nums:
        if num==pivot:
            list2.append(num)
        elif num<pivot:
            list1.append(num)
        else:
            list3.append(num)
    return list1+list2+list3
def findThePrefixCommonArray( A: List[int], B: List[int]) -> List[int]:
    result:List[int]=[]
    for i in range(len(A)):
        count:int=0
        temp:List[int]=B[:i+1]
        for j in range(i+1):
            count+=1 if A[j] in temp else 0
        result.append(count)
    return result
def largestInteger( num: int) -> int:
    numbers:List[int]=list(map(int,str(num)))
    even:List[int]=[]
    odd:List[int]=[]
    for n in numbers:
        if n&1:
            odd.append(n)
        else:
            even.append(n)
    even.sort(reverse=True)
    odd.sort(reverse=True)
    oddIndexes:List[int]=[i for i in range(len(numbers)) if numbers[i]&1]
    evenIndexes:List[int]=[i  for i in range(len(numbers)) if not(numbers[i]&1)]
    res:List[int]=[0]*len(numbers)
    
    for i,o in enumerate(odd):
        res[oddIndexes[i]]=o
    for i,e in enumerate(even):
        res[evenIndexes[i]]=e

    originalNumber:str=''
    for n in res:
        originalNumber+=str(n)
    return int(originalNumber)
def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        res:List[bool]=[False for _ in range(101)]
        for i in range(len(bulbs)):
            res[bulbs[i]]=not res[bulbs[i]]
        Onbulbs:List[int]=[]
        for i,j in enumerate(res):
            if j:
                Onbulbs.append(i)
        return sorted(Onbulbs)    
def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if (prices[0]+prices[1])<=money:
            return money-(prices[0]+prices[1])
        return money
def minimumDifference(nums: List[int], k: int) -> int:
        n=len(nums)
        if n==1:
            return 0
        nums.sort()
        minDiff:int=float('inf')
        for i in range(n-k+1):
            tempArray:List[int]=nums[i:i+k]
            tempMin:int=max(tempArray)-min(tempArray)
            minDiff=min(minDiff,tempMin)
        return minDiff
def reversePrefix(self, s: str, k: int) -> str:
        temp:List[str]=list(s)
        reversedArray:List[str]=list(reversed(temp[0:k]))
        for i in range(k,len(temp)):
            reversedArray.append(temp[i])
        return ''.join(reversedArray)
def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        alphabets:str=list('abcdefghijklmnopqrstuvwxyz')
        digits:List[int]=[i for i in range(0,26)]
        reversedAlphas:List[str]=list(reversed(alphabets))     
        mpp:Dict[int,str]=dict(zip(digits,reversedAlphas))
        res:str=''
        for word in words:
            total:int=0
            for ch in word:
                total+=weights[ord(ch)-97]
            res+=mpp[total%26]
        return res
def reverseByType(self, s: str) -> str:
        specials:List[str]=[]
        letters:List[str]=[]
        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                specials.append(ch)
        revA:List[str]=list(reversed(letters))
        revS:List[str]=list(reversed(specials))
        res:str=''
        i,j=0,0
        for k in range(len(s)):
            if s[k].isalpha():
                res+=revA[i]
                i+=1
            else:
                res+=revS[j]
                j+=1
        return res
def minimumFlips(self, n: int) -> int:
        binary:List[str]=list(bin(n)[2:])
        revBinary:List[str]=list(reversed(binary))
        count:int=0
        for i in range(len(binary)):
            if binary[i]!=revBinary[i]:
                count+=1
        return count
def largestEven(self, s: str) -> str:
        if '2' not in s:
            return ""
        for i in range(len(s)-1,-1,-1):
            if s[i]=='2':
                return s[:(i+1)]
        return ""
def capitalizeTitle(self, title: str) -> str:
        title+=' '
        res:str=''
        word:str=''
        for ch in title:
            if ch.isalpha():
                word+=ch
            else:
                if len(word)>=3:
                    res+=word.capitalize()+' '
                else:
                    res+=''.join([c.lower() for c in word])+' '
                word=''
                
        return res[:len(res)-1]
def digitSum(s: str, k: int) -> str:
    res:str=s
    while len(res)>k:
        temp:str=''
        for i in range(0,len(res),k):
            temp+=str(sum(list(map(int,res[i:i+k]))))
        res=temp
    return res
def convertTime( current: str, correct: str) -> int:
    curr:List[int]=[]
    corr:List[int]=[]
    curr.append(int(current[0:2]))
    curr.append(int(current[3:]))
    corr.append(int(correct[0:2]))
    corr.append(int(correct[3:]))
    minutes:List[int]=[60,15,5,1]
    i=0
    count=0
    while curr[0]!=corr[0] or curr[1]!=corr[1]:
        h,m=curr[0],curr[1]
        m+=minutes[i]
        h+=m//60
        m=m%60
        if h*60+m <= corr[0]*60+corr[1] :
            curr[0],curr[1]=h,m
            count+=1
        else:
            i+=1
    return count
def furthestDistanceFromOrigin(self, moves: str) -> int:
        countOfL:int=moves.count('L')
        countOfR:int=moves.count('R')
        return max(countOfL,countOfR)+(len(moves)-(countOfL+countOfR))-min(countOfL,countOfR)
class MyHashSet:

    def __init__(self):
        self.sss:Set[int]=set()

    def add(self, key: int) -> None:
        self.sss.add(key)

    def remove(self, key: int) -> None:
        if key in self.sss:
            self.sss.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.sss
class MyHashMap:

    def __init__(self):
        self.keys:List[int]=[]
        self.values:List[int]=[]

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            index=self.keys.index(key)
            self.values[index]=value
        else:
            self.keys.append(key)
            self.values.append(value)

    def get(self, key: int) -> int:
        if key in self.keys:
            index=self.keys.index(key)
            return self.values[index]
        else:
            return -1
    def remove(self, key: int) -> None:
        if key in self.keys:
            index=self.keys.index(key)
            del self.keys[index]
            del self.values[index]
def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        mpp1:Dict[str,int]={}
        mpp2:Dict[str,int]={}
        for w in word1:
            mpp1[w]=mpp1.get(w,0)+1
        for w in word2:
            mpp2[w]=mpp2.get(w,0)+1
        for (key,value) in mpp1.items():
            if mpp1[key]-mpp2.get(key,0)>3:
                return False
        
        for (key,value) in mpp2.items():
            if mpp2[key]-mpp1.get(key,0)>3:
                return False
        return True
def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res:List[str]=[]
        temp:List[str]=text.split(' ')
        third=False
        for i in range(len(temp)-1):
            if third:
                res.append(temp[i+1])
                third=False
            if temp[i]==first and temp[i+1]==second:
                third=True
        return res
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None :
            return None
        
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
       ans:List[int]=[]
       def dfs(node):
           if node is None:
               return 
           ans.append(node.val)
           dfs(node.left)
           dfs(node.right)
       dfs(root)
       uniqueSortedArray=sorted(list(set(ans)))
       if len(uniqueSortedArray)>1:
           return uniqueSortedArray[1]
       return -1
def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned is None:
            return None
        if cloned.val == target.val:
            return cloned
        l=self.getTargetCopy(original,cloned.left,target)
        r=self.getTargetCopy(original,cloned.right,target)

        return l or r
def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None :
            return root2
        if root2 is None:
            return root1
        node:TreeNode=TreeNode(root1.val+root2.val)
        node.left=self.mergeTrees(root1.left,root2.left)
        node.right=self.mergeTrees(root1.right,root2.right)
        return node
def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root is None :
            return False
        if root.left is None and root.right is None:
            return root.val==1
        l=self.evaluateTree(root.left)
        r=self.evaluateTree(root.right)

        if root.val==2:
            return l or r
        return l and r
def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans:List[int]=[]
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        dfs(root)
        def makeTree(nums:List[int]):
            if len(nums)==0:
                return 
            node:TreeNode=TreeNode(nums[0])
            node.right=makeTree(nums[1:])
            return node
        return makeTree(ans)
def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans:List[int]=[0]
        def dfs(node:TreeNode,path:str):
            if node is None:
                return 
            path+=str(node.val)
            if node.left is None and node.right is None:
                ans[0]+=int(path,2)
            dfs(node.left,path)
            dfs(node.right,path)
        dfs(root,'')
        return ans[0]
def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        queue:Deque[TreeNode]=deque([root])
        res:List[float]=[]
        while queue:
            level_size:int=len(queue)
            level:int=0
            for i in range(level_size):
                node:TreeNode=queue.popleft()
                level+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level/level_size)
        return res

def trimTrailingVowels(self, s: str) -> str:
        r=-1
        vowels=['a','e','i','o','u']
        for i in range(len(s)-1,-1,-1):
            if s[i] not in vowels:
                r=i
                break
        return s[:r+1]
def minOperations(self, s: str) -> int:
        n=len(s)
        arr1,arr2=[0]*n,[1]*n
        for i in range(1,n,2):
            arr1[i]=1
            arr2[i]=0
        m1,m2=0,0
        for i in range(n):
            if arr1[i]!=int(s[i]):
                m1+=1
        for i in range(n):
            if arr2[i]!=int(s[i]):
                m2+=1
        return min(m1,m2)

def minimumPushes(self, word: str) -> int:
        cost=1
        total=0
        for i in range(len(word)):
            if i%8==0 and i!=0:
                cost+=1
            total+=cost
        return total

def maximumLengthSubstring(self, s: str) -> int:
        maxLength=0
        starter=0
        n=len(s)
        while starter<n:
            mpp:Dict[str,int]={}
            currentLength=0
 
            for i in range(starter,n):
                mpp[s[i]]=mpp.get(s[i],0)+1
                if mpp[s[i]]>2:
                    break
                currentLength+=1
            maxLength=max(maxLength,currentLength)
            starter=starter+1
        return maxLength
def findSubarrays(self, nums: List[int]) -> bool:
        mpp:Dict[int,int]={}
        for i in range(len(nums)-1):
            s=nums[i]+nums[i+1]
            mpp[s]=mpp.get(s,0)+1
            if mpp[s]==2:
                return True
        return False

def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        nums.sort(reverse=True)
        res=[]
        n=len(nums)
        for i in range(n):
            s1=sum(nums[0:i])
            s2=sum(nums[i:])
            if s1>s2:
                res=nums[0:i]
                break
        if len(res)==0:
            return nums
        return res

def isPossibleToSplit(self, nums: List[int]) -> bool:
        mpp:Dict[int,int]={}
        for num in nums:
            mpp[num]=mpp.get(num,0)+1
            if mpp[num]==3:
                return False
        return True

def rearrangeCharacters(self, s: str, target: str) -> int:
        mpptar:Dict[str,int]={}
        mpp:Dict[str,int]={}
        for ch in s:
            mpp[ch]=mpp.get(ch,0)+1
        for ch in target:
            mpptar[ch]=mpptar.get(ch,0)+1
        count:int=0
        while True:
            flag=False
            for (key,value) in mpptar.items():
                if mpp.get(key,0)<value:
                    flag=True
                    break
                else:
                    mpp[key]-=value
            if not flag :
                count+=1
            if flag:
                break
        return count
