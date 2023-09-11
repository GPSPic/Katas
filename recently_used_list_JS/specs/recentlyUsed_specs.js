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

    it('should do be able to add a single string', function() {
        // recentlyUsed.addString(a)
        const actual = recentlyUsed.getArr()[0]
        assert.strictEqual(actual, "a")
    })

    // it('should do be able to add 2 unique strings', function() {
    //     recentlyUsed(a)
    //     const actual = recentlyUsed(b)

    //     assert.strictEqual(actual, "a")
    // })
})