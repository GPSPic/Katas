const getRandomTimesForValidDays = function (data) {
  const dailyTimes = {
    monday: [],
    tuesday: [],
    wednesday: [],
    thursday: [],
    friday: [],
    saturday: [],
    sunday: [],
  };

  return dailyTimes;
};

export const minuteConverter = function (str) {
  const timeParts = str.split(":");
  return Number(timeParts[0]) * 60 + Number(timeParts[1]);
};

export const totalLengthOfTime = function (start, end) {
  if (end > start) {
    return end - start;
  }
};


export const getIntervalsEdges = function (startTime, endTime, ringNum) {
  const start = minuteConverter(startTime);
  const end = minuteConverter(endTime);
  const totalTime = totalLengthOfTime(start, end);

  if (ringNum > 0) {
    const intervalLength = Math.floor(totalTime / ringNum);
    const remainingMinutes = totalTime % ringNum;

    const intervals = [start];
    let newValue = start
    for (let i = 0; i < ringNum; i++) {
      newValue = newValue + intervalLength + (i < remainingMinutes ? 1 : 0)
      intervals.push(newValue);
    }

  return intervals;
  }
};

const getRandomValue = function (i, j) {};
