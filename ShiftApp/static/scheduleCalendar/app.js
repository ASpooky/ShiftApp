document.addEventListener('DOMContentLoaded', function () {

    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',

        selectable: true,
        select: function (info) {
            
            moment.locale('ja');
            start=moment(info.start).format('YYYY-MM-DD');
            //const eventName = prompt("イベントを入力してください");
            //if (eventName) {
            //    calendar.addEvent({
            //        title: eventName,
            //        start: info.start,
            //        end: info.end,
            //        allDay: true,
            //    });
            //}
            return window.location.replace(start)
            
        },
    });

    calendar.render();
});