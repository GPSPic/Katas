const assert = require('assert')
const RecentlyUsed = require('../models/recentlyUsed.js')

describe('RecentlyUsed', function() {
    let a
    let b
    let c
    let d
    let recentlyUsed

    beforeEach(function () {
        a = "a"
        b = "b"
        c = "c"
        d = "d"
        recentlyUsed = new RecentlyUsed(3)
    })

    it('should do add anything to the array if the string is falsy', function() {
        recentlyUsed.addString("")
        const actual = recentlyUsed.getArr().length
        assert.strictEqual(actual, 0)
    })

    it('should do be able to add a single string', function() {
        recentlyUsed.addString(a)
        const actual = recentlyUsed.getArr()[0]
        assert.strictEqual(actual, "a")
    })

    it('should do be able to add 2 unique strings', function() {
        recentlyUsed.addString(a)
        recentlyUsed.addString(b)
        const actual = recentlyUsed.getArr().length 
        assert.strictEqual(actual, 2)
    })

    it('should push the first input when over max length', function () { 
        recentlyUsed.addString(a)
        recentlyUsed.addString(b)
        recentlyUsed.addString(c)
        recentlyUsed.addString(d)
        const actual = recentlyUsed.getArr()[0]
        assert.strictEqual(actual, 'd')
        const actual2 = recentlyUsed.getArr()[2]
        assert.strictEqual(actual2, 'b')
    })

    it("should not allow duplicate in the list and push them back to last used", function () {
        recentlyUsed.addString(a)
        recentlyUsed.addString(b)
        recentlyUsed.addString(c)
        recentlyUsed.addString(b)
        const actual1 = recentlyUsed.getArr()[0]
        const actual2 = recentlyUsed.getArr()[2]
        assert.strictEqual(actual1, "b")
        assert.notStrictEqual(actual2, "b")
    })

    it("should not allow duplicate in the list and push them back to last used", function () {
        recentlyUsed.addString(b)
        recentlyUsed.addString(b)
        recentlyUsed.addString(b)
        recentlyUsed.addString(b)
        const actual1 = recentlyUsed.getArr().length
        const actual2 = recentlyUsed.getArr()[0]
        assert.strictEqual(actual1, 1)
        assert.strictEqual(actual2, "b")
    })

})