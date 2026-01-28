# Week 2 Kickoff - Days 9 & 10
**Date:** Jan 14, 2026  
**Focus:** Two Pointers Pattern & Data Integrity  
**Status:** Streak Alive (10 Days)

---

## Day 9: The Pivot (Valid Palindrome & Schema Refactor)

### DSA (Two Pointers)
- **Problem:** Valid Palindrome (LeetCode 125)
- **Lesson:** The "Pincer Movement." Comparing `s[l]` and `s[r]` while skipping junk characters (`isalnum()`) inside the loop.
- **Constraint:** Solved in $O(n)$ time and $O(1)$ space (no string reversing).

### System Design
- **Refactor:** Split the `Membership` model into `MembershipPlan` (The Menu) and `Membership` (The Receipt).
- **Feature:** Added `uuid` for secure QR codes and `owner` field for SaaS multi-tenancy.

---

## Day 10: The Expansion (3Sum & API Logic)

### DSA (Two Pointers Advanced)
- **Problem:** 3Sum (LeetCode 15)
- **Strategy:** Sort the array first ($O(n \log n)$). Fix one anchor (`i`), then run Two Pointers on the rest.
- **Key Learning:** "Bounds First, Values Second." Always check `l < r` before accessing `nums[l]` in a while loop to avoid crashes.

### Backend Engineering
- **Validation:** Implemented a custom `validate()` method in the Serializer.
- **UX:** The API now returns a clean 400 error ("User already has an active membership") instead of a generic 500 Server Error.
- **Fix:** Updated `GymViewSet` to allow regular users to see the gym marketplace.


---

## Day 11: The "Privacy Wall" (Multi-Tenancy)

### DSA (Two Pointers - Optimization)
- **Problem:** Container With Most Water (LeetCode 11)
- **Strategy:** Start wide ($L=0, R=end$) to maximize width. Move the shorter pointer inward at every step because height is the bottleneck.
- **Result:** Solved in $O(n)$ time.

### System Design (Data Isolation)
- **Concept:** SaaS Multi-Tenancy at the API layer.
- **Implementation:** Overrode `get_queryset` in `MembershipViewSet`.
- **Logic:**
    - **Superusers:** See all rows ("God Mode").
    - **Gym Owners:** See memberships for their gyms only (using `gym__owner` lookup).
    - **Regular Members:** See only their own receipts.

---

## Day 12: The Window & The Guard (Permissions)

### DSA (Sliding Window Basics)
- **Problem:** Best Time to Buy and Sell Stock (LeetCode 121)
- **Strategy:** Single Pass (Greedy). Maintained a `min_price` (Left Pointer) and calculated potential profit at every step (Right Pointer).
- **Key Insight:** "Buy Low" is just updating the minimum variable; "Sell High" is checking the difference.

### Backend Engineering (Hybrid Permissions)
- **Feature:** Public "Marketplace" API for Membership Plans.
- **Solution:** Implemented Custom Permission `IsGymOwnerOrReadOnly`.
- **Architecture:** Learned the difference between `has_permission` (The Doorman - View Level) vs. `has_object_permission` (The VIP Guard - Row Level).





