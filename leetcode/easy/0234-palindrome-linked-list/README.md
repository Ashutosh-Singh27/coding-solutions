# Palindrome Linked List

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `head` of a singly linked list, return `true` *if it is a  **palindrome**  or* `false` *otherwise*.

 

 **Example 1:** 

```
Input: head = [1,2,2,1]
Output: true

```

 **Example 2:** 

```
Input: head = [1,2]
Output: false

```

 

 **Constraints:** 

- The number of nodes in the list is in the range [1, 105].
- 0 <= Node.val <= 9

 

 **Follow up:**  Could you do it in `O(n)` time and `O(1)` space?

## Solution

**Language:** Python  
**Runtime:** 44 ms (beats 27.27%)  
**Memory:** 42.4 MB (beats 86.39%)  
**Submitted:** 2026-10-16T16:40:00.427Z  

```py
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
```

---

[View on LeetCode](https://leetcode.com/problems/palindrome-linked-list/)