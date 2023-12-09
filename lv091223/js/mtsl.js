/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */


class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }

    toString() {
        return this.next ? [this.val, this.next.toString()].join(',') : this.val
    }
}

const create = ([first, ...body]) => {
    if (first) {
        return new ListNode(first, create(body))
    } else {
        return undefined
    }
}

/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
    var toMerge;
    if (!list1) return list2
    if (!list2) return list1

    if (list1.val < list2.val) {
        merged = list1
        toMerge = list2
    } else {
        merged = list2
        toMerge = list1
    }

    var current = merged
    do {
        if (!current.next || current.next.val > toMerge.val) {
            var extra = current.next
            current.next = toMerge
            toMerge = extra
        }
        current = current.next
    } while (current.next && toMerge)
    if (toMerge) current.next = toMerge
    return merged;
};

// console.log(create([1,2,3,4]).toString())
console.log(mergeTwoLists(create([1,3,6]), create([-9])).toString())
