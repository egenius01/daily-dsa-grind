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


