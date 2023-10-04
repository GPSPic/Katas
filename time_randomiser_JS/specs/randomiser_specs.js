const assert = require('assert');
const minuteConverter = require('../models/randomiser.js');

describe('', function() {
    let initialData = {}

    beforeEach(function() {
        initialData = {
            startTime: "08:00",
            endTime: "20:00",
            ringNum: 12,
            minInterval: "30:00",
            daysSelected: {
                monday: true,
                tuesday: false,
                wednesday: false,
                thursday: false,
                friday: false,
                saturday: false,
                sunday: false
            }
        }
    })

    it('should convert the string for times into a number of minutes', function() {
        const actual = minuteConverter(initialData.startTime)
        assert.deepStrictEqual(actual, 480)
    })
})