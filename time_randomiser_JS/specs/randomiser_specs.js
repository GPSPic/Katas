import assert from 'assert';
import { minuteConverter, totalLengthOfTime } from '../models/randomiser.js';

describe('', function() {
    let initialData = {}

    beforeEach(function() {
        initialData = {
            startTime: "08:00",
            endTime: "20:00",
            ringNum: 12,
            minInterval: "00:30",
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
        const actual1 = minuteConverter(initialData.startTime)
        const actual2 = minuteConverter(initialData.endTime)
        const actual3 = minuteConverter(initialData.minInterval)
        assert.deepStrictEqual(actual1, 480)
        assert.deepStrictEqual(actual2, 1200)
        assert.deepStrictEqual(actual3, 30)
    })

    it('should calculate the total length of time', function () {
        const actual = totalLengthOfTime(initialData.startTime, initialData.endTime)
        assert.deepStrictEqual(actual, 720)
    })


})