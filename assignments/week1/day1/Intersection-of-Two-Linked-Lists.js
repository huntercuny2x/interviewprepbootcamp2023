/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function(headA, headB) {
  let hash = new Set()
  let currNodeA = headA
  let currNodeB = headB

  while(currNodeA) {
      hash.add(currNodeA)
      currNodeA = currNodeA.next
  }
  while(currNodeB) {
      if (hash.has(currNodeB)) {
          return currNodeB
      }
      currNodeB = currNodeB.next
  }
  
  return null
};