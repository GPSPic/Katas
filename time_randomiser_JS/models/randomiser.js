const randomiser = function (data) {
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
  if (minuteConverter(end) > minuteConverter(start)) {
    return minuteConverter(end) - minuteConverter(start);
  }
};
