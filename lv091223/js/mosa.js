/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
    const singleMedian = (nums) => {
        if (nums.length % 2 == 0) {
            const mI = Math.floor(nums.length / 2)
            return (nums[mI - 1] + nums[mI]) / 2
        } else {
            return nums[Math.floor(nums.length / 2)]
        }
    }

    const l1 = nums1.length;
    if (l1 === 0) return singleMedian(nums2)

    const l2 = nums2.length;
    if (l2 === 0) return singleMedian(nums1)

    const total = l1 + l2;
    const m1 = Math.floor(total / 2) - (total % 2 == 1 ? 0 : 1)
    var i1 = 0, i2 = 0;
    for (var i = 0; i < total; i++) {
        if (i == m1) {
            if (total % 2 == 0) {
                var first, second;

                if (i1 >= l1) {
                    first = nums2[i2]
                    i2++
                } else if (i2 >= l2) {
                    first = nums1[i1]
                    i1++
                } else if (nums1[i1] < nums2[i2]) {
                    first = nums1[i1]
                    i1++
                } else {
                    first = nums2[i2]
                    i2++
                }

                if (i1 >= l1) second = nums2[i2]
                else if (i2 >= l2) second = nums1[i1]
                else if (nums1[i1] < nums2[i2]) second = nums1[i1]
                else second = nums2[i2]

                return (first + second) / 2
            } else {
                if (i1 >= l1) return nums2[i2]
                else if (i2 >= l2) return nums1[i1]
                else if (nums1[i1] < nums2[i2]) return nums1[i1]
                else return nums2[i2]
            }
        }

        if (i1 >= l1 || nums1[i1] >= nums2[i2]) {
            i2++;
        } else {
            i1++;
        }
    }
};

console.log(findMedianSortedArrays([2, 2, 4, 4], [2, 2, 4, 4]))