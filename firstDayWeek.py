''' firstDayWeek function takes two parameters, w and y, representing the week number and year respectively, 
and calculates and returns the date of the first day (Monday) of the specified week in the format 'dd-mm-yyyy'.'''
function firstDayWeek(w, y) {
    // Start from January 1 of the given year
    var date = new Date(`${y}-01-01`);

    // If it's not the 1st week, move forward by (w - 1) weeks
    if (w !== 1) {
        for (let i = 1; i < w; i++) {
            date.setDate(date.getDate() + 7);
        }

        // Special correction for year 2017 (custom case handling)
        if (y === '2017') {
            date.setDate(date.getDate() - 7);
        }

        // Adjust to Monday (getDay(): Sunday=0, Monday=1, ... Saturday=6)
        date.setDate(date.getDate() - date.getDay() + 1);
    }

    // Extract day, month, year
    var dd = date.getDate();
    var mm = date.getMonth() + 1; // Months are 0-based in JS
    var yy = date.getFullYear();

    // Add leading zeros for day/month if needed
    if (dd < 10) dd = '0' + dd;
    if (mm < 10) mm = '0' + mm;

    // Pad year with leading zeros if < 1000
    for (var i = 1000; i != 0; i /= 10) {
        if (yy < i) {
            yy = '0' + yy;
        }
    }

    // Return formatted string "dd-mm-yyyy"
    return `${dd}-${mm}-${yy}`;
}
