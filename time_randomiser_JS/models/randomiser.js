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

const minuteConverter = function (str) {
  let numberOfMinutes;

  const hours = parseInt(str[0] + str[1]);
  const minutes = parseInt(str[3] + str[4]);

  numberOfMinutes = hours * 60 + minutes;

  return numberOfMinutes;
};

module.exports = minuteConverter;
