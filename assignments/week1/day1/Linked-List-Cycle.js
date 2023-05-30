/* 141. Linked List Cycle */

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    let hash = new Set()
    let currNode = head

    while (currNode) {
        if (hash.has(currNode)) {
            return true
        } else {
            hash.add(currNode)
        }
        currNode = currNode.next
    }

    return false
};