# daily-dsa-grind

## Day 1

### Problem-217 Contains Duplicate

<img src="BIG(0)_NOTATION_CHART.png" alt="alt text" width="20%" />

1. **What did I learn today?**
   - I learnt about Big (O) Notation and how to calculate it.
   - I also learnt that using set over list to solving this problem was more efficient
   - I also discovered that my one liner solution shich is in my code is the most efficient, because i used an inbuilt function which reduces interpreter overhead since python uses C directly and we all know C is faster than python and python was built on top of C.
2. **Where did I struggle?**
   - I forgot how to add an element to a set, had to look it up.
   - I made typos
   - I used a dictionary for my third solution instead of a set which just took up more memory than it should have and i was busy logging numbers i shouldnt have, that i wasnt going to use
3. **What was the pattern?**
   - Hashing / Sets

## Day 2

### Problem-242 Valid Anagram

1. **What did I learn today?**
   - I leant about hashmaps(dictionaries)a and retrieval
   - I learnt that i can use the Counter class from the collections module to count the frequency of elements in a list
   - I used Counter Class as the final solution since its uses C directly which is significantly faster
2. **Where did I struggle?**
   - I forgot how to add an element to a set, had to look it up.
   - Confused dict.get() syntax (used brackets instead of parentheses). Need to practice dictionary retrieval
   - I used zip not knowing that it only returns e.g dict1 ={a,b,c} dict2 = {c,d}, zip will only return {a,c} and {b,d} and neglect the last c in a,b,c so i ha to check the length of the list and the set to see if they are equal.
3. **What was the pattern?**
   - Hash Maps

4.  **Big (O) Notation**
    - Time Complexity: O(n) (Iterating through the string).
    - Space Complexity: O(1) - Because the dictionary maxes out at 26 keys (a-z), it doesn't grow infinitely with input size.

### System Analysis
#### Tech Debt: DotFit Architecture Refactor

**Current State:** Profile model has a strict 1:1 Foreign Key to Gym.

**Problem:** Prevents multi-gym membership. user_type is global, preventing mixed roles (Staff vs Member) across locations.

**Solution:**

- Remove gym field from Profile.
- Remove user_type from User (move it to the relation).
- Create Membership model: User + Gym + Role + Expiration.


## Day 3

## Problem-xxx Two Sum 

1. 1. **What did I learn today?**
   - Refactored to use enumerate() for cleaner syntax and hit 0ms runtime beating 100% of leetcoders.
   - I leant not to use nested for loops for tasks like this because its complexity is O(n squared) which is very bad and inneficient.
   - I also learnt to use enumerate instead of range(len(nums)) which is fine but slower than inbuilt enumerate.
   -  I learnt to use the dictionary/hashmaps(notebook) method to store data and use as a checker or pointer to confirm instead of using nested for loops which is what ussually comes to mind first an is bad.
2. **Where did I struggle?**
   - I went ahead to use for loops which is inefficient and struggled to understand the dictionary/hashmaps(notebook) method.

3. **What was the pattern?**
   - Hash Maps / Dictionary

4.  **Big (O) Notation**
    - Time Complexity: O(n) (Iterating through the string).
    - Space Complexity: O(n) - Because the dictionary only gets values store to it n times.

# Day 4 - WASTED

# Day 4 (Recovery)

## Problem- 49 Group Anagrams

1. **What did I learn today?**
   - I learnt to use default dict from collections to create a dictionary and add lists as values instead of manually checking if a key exists
   - I learnt that sorting itself is k log k where k is the length of the string, so it would only be slow if the lenght of the strings are really large
   - I also learnt that i shoulnt drink alcohol aa ay before i have something important to do, it slows me down
2. **Where did I struggle?**
   - i struggled in implementing the algorithm i had in mind
   - i couldnt think about default dict even if i knew about it previously, i was coding like a junior dev
   - i also struggled with the logic of the problem
   - I took too mich time solving the problem >20 minutes

3. **What was the pattern?**
   - Hash Maps / Dictionary (DEFAULT DICT)

4.  **Big (O) Notation**
    - Time Complexity: O(n•k log k) (Iterating through the string).
      - n is the number of strings
      - k is the length of the strings(k is sorting each word)
      - this is efficient enough unless the interview has large or massive string lenghts
      - if the strings are really long, we can use a counter to count the frequency of each character in the string and compare them (New Knowledge)
    - Space Complexity: O(n•k) - to store the map.

# Day 5(catch up)
## Problem-347 Top K Frequent Elements

1. **What did I learn today?**
   - `Counter.items()` unpacks keys/values efficiently.
   - `range(len(nums) + 1)` is needed for 0-based indexing.
   - Technique: Used a Frequency Array where Index = Count.
2. **Where did I struggle?**
   - I struggled with the logic and spent 60 minutes on the task.
3. **What was the pattern?**
   - Bucket Sort + Hash Map
4. **Big (O) Notation**
   - Time Complexity: $O(n)$ (Better than Sorting).
   - Space Complexity: $O(n)$

# Day 6
## Problem- 238. Product of Array Except Self

1. **What did I learn today?**
   - I learnt to use prefix and suffix to solve this problem
   - I learnt to write out the algorithm in plain english/Diagram it out before coding
   - Do not divide. Calculate "Left Product" then multiply by "Right Product."
   
2. **Where did I struggle?**
   - **1 hour manual visualization:** I struggled with the logic and spent over 60 minutes on the task, good thing is i know better now and i used neet code to understand visually and learn to draw shit out first...
3. **What was the pattern?**
   - Prefix and Suffix
4. **Big (O) Notation**
   - Time Complexity: O(n)
   - Space Complexity: O(n)
