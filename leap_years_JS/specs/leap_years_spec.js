const assert = require('assert');
const leapYear = require('../models/leap_year.js');

describe('LeapYear', function() {

    it('should return true if it is a typical leap year', function() {
        const actual = leapYear(1996);
        assert.strictEqual(actual, true);
    })

    // it('should return false for a typical common year', function() {
    //     const actual = leapYear(1995);
    //     assert.strictEqual(actual, false);
    // })
})