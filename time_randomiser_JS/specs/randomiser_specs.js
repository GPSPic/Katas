import assert from "assert";
import {
  minuteConverter,
  totalLengthOfTime,
  getIntervalsEdges,
  getRandomArray,
  getIntervalLength,
  getRandomValue,
} from "../models/randomiser.js";

describe("", function () {
  let initialData;
  let slightlyDifficultData;

  beforeEach(function () {
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
        sunday: false,
      },
    };
    slightlyDifficultData = {
      startTime: "00:00",
      endTime: "01:00",
      ringNum: 7,
      minInterval: "00:00",
      daysSelected: {
        monday: true,
        tuesday: false,
        wednesday: false,
        thursday: false,
        friday: false,
        saturday: false,
        sunday: false,
      },
    };
  });

  it("should convert the string for times into a number of minutes", function () {
    const actual1 = minuteConverter(initialData.startTime);
    const actual2 = minuteConverter(initialData.endTime);
    const actual3 = minuteConverter(initialData.minInterval);
    assert.deepStrictEqual(actual1, 480);
    assert.deepStrictEqual(actual2, 1200);
    assert.deepStrictEqual(actual3, 30);
  });

  it("should calculate the total length of time", function () {
    const start = minuteConverter(initialData.startTime);
    const end = minuteConverter(initialData.endTime);
    const actual = totalLengthOfTime(start, end);
    assert.deepStrictEqual(actual, 720);
  });

  it("should calculate the minimum length of the fractions of time", function () {
    const actual = getIntervalLength(
      minuteConverter(initialData.startTime),
      minuteConverter(initialData.endTime),
      initialData.ringNum
    );
    const actual2 = getIntervalLength(
      minuteConverter(slightlyDifficultData.startTime),
      minuteConverter(slightlyDifficultData.endTime),
      slightlyDifficultData.ringNum
    );
    assert.deepStrictEqual(actual, 60);
    assert.deepStrictEqual(actual2, 8);
  });

  it("should create an array with the values of all time intervals starting from startTime", function () {
    const actual1 = getIntervalsEdges(
      minuteConverter(initialData.startTime),
      minuteConverter(initialData.endTime),
      initialData.ringNum
    );
    const actual2 = getIntervalsEdges(
      minuteConverter(slightlyDifficultData.startTime),
      minuteConverter(slightlyDifficultData.endTime),
      slightlyDifficultData.ringNum
    );
    assert.deepStrictEqual(
      actual1,
      [480, 540, 600, 660, 720, 780, 840, 900, 960, 1020, 1080, 1140, 1200]
    );
    assert.deepStrictEqual(actual2, [0, 9, 18, 27, 36, 44, 52, 60]);
  });

  it("should create an array of random values where i < i+1", function () {
    const arr = getRandomArray(initialData);
    const actual = arr.every((el, index) => {
      if (index < arr.length - 1) {
        return el < arr[index + 1];
      }
      return true;
    });
    assert.deepStrictEqual(actual, true);
  });
});
