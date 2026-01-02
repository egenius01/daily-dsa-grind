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