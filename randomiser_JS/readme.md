# Interval randomiser

The purpose of this exercise is to test the ability of a function to return an object of semi-random time values when being provided initial data.
The initial data is:
- a start time
- an end time
- a number of expected random dateTime objects
- a minimum interval of time between 2 dateTime objects
- days of the week

The expected return will be an object containing random Time objects for each day of the week, with the difference between 2 dateTimes on the same day being greater than the minimum interval time.
The total length of time determined by start/end times should also be fractioned in timeframes according to the number of expected Time objects, so as to provide a perception of randomness for human observers while still spreading the times along the whole total length.

Starting object should look like this:
{
    startTime: string "HH:MM",
    endTime: string "HH:MM",
    ringNum: int,
    minInterval: string "HH:MM",
    daysSelected: {
        monday: bool,
        tuesday: bool,
        wednesday: bool,
        thursday: bool,
        friday: bool,
        saturday: bool,
        sunday: bool
    }
}

Expected result should be:
{
    monday: [Time],
    tuesday: [Time],
    wednesday: [Time],
    thursday: [Time],
    friday: [Time],
    saturday: [Time],
    sunday: [Time]
}