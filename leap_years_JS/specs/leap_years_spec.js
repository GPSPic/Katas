const assert = require('assert');
const leapYear = require('../models/leap_years.js');

describe('leapYear', function() {

    it('should return true if it is a typical leap year', function() {
        const actual = leapYear(1996);
        assert.strictEqual(actual, true);
    })

    it('should return false for a typical common year', function() {
        const actual = leapYear(1995);
        assert.strictEqual(actual, false);
    })

    it('should return false if it is an atypical common year', function() {
        const actual = leapYear(1700);
        assert.strictEqual(actual, false);
    })

    it('should return true if it is an atypical leap year', function() {
        const actual = leapYear(2000);
        assert.strictEqual(actual, true);
    })

    it('should return false if it is a negative common year', function() {
        const actual = leapYear(-35);
        assert.strictEqual(actual, false);
    })

    it('should return true if it is an negative leap year', function() {
        const actual = leapYear(-44);
        assert.strictEqual(actual, true);
    })

    it('should return null if num is not a number', function() {
        const actual = leapYear("pancakes");
        assert.strictEqual(actual, null);
    })
})