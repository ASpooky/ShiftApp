document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');

    console.log('ページが読み込まれました！');
    console.log(all_shift);
    console.log(all_shift.length);

    //var calendar = new FullCalendar.Calendar(calendarEl, {　一週間の場合
    //     locale: 'ja',
    // headerToolbar: {
    //    left: 'prev,next today',
    //    center: 'title',
    //    right: '',
    //  },
    //  initialView: 'timeGridWeek',
    //  firstDay: (new Date()).getDay(),
    //  businessHours: true,
    //  editable: true,
    //  selectable: true,
    //  slotMinTime: '06:00:00',
    //  slotMaxTime: '27:00:00',
    //  slotDuration: '00:30:00',
    //  slotLabelInterval: '01:00',
    //  slotLabelFormat: {
    //    hour: 'numeric',
    //    minute: '2-digit',
    //    omitZeroMinute: false,
    //    meridiem: 'short'
    //  },
    //  events: []
    //  
    //});

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

    for (  var i = 0;  i < all_shift.length;  i++  ) {
 
      calendar.addEvent({
        title: all_shift[i]["title"],
        start: '2023-06-18',
        end: '2023-06-19',
        allDay: false,
      });
      
     };

    calendar.render();
  });