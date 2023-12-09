/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */


function ListNode(val, next) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
        function toString() {
            return this.next ? [this.val, this.next.toString()].join(',') : this.val
        }
}

const create = (lists) => {
    const nodes =  lists.map(l => {
        return createList(l)
    })

    console.log('nodes', nodes)

    return nodes
}

const createList = ([first, ...body]) => {
    if (first) {
        return new ListNode(first, createList(body))
    } else {
        return undefined
    }
}

/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function (lists) {
    if (lists.length == 0) return null

    var merged = ListNode()
    for (let i = 0; i < lists.length; i+=2) {
        const l1 = lists[i];
        const l2 = lists[i + 1];
        const mergedTwo = mergeTwoLists(l1, l2)
    }

    return mergeAll(lists)
}

var mergeAll = function ([list1, list2, ]) {
    console.log({list1, list2, remaining})
    const mergedTwo = mergeTwoLists(list1, list2)
    if (remaining.length > 0) {
        return mergeAll([mergedTwo, ...remaining])
    } else {
        return mergedTwo
    }
}

var mergeTwoLists = function (list1, list2) {
    var dummy = ListNode()
    var tail = dummy

    while (list1 && list2) {
        if (list1.val < list2.val) {
            tail.next = list1
            list1 = list2.next
        } else {
            tail.next = list2
            list2 = list2.next
        }
        tail = tail.next
    }

    if (list1) {
        tail.next = list1
    } 
    if (list2) {
        tail.next = list2
    }

    return dummy
    
};

// console.log(create([1,2,3,4]).toString())
// console.log('merged', mergeKLists(create([[], [1, 3, 6], [-9]])))
// console.log('merged', mergeKLists([]))
console.log('merged', mergeKLists(create([[]])))
console.log('nodess2', ListNode([1,2,3,4,5]))
