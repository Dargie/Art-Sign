$(document).ready(function() {
    // Init components materializeCSS
    $(".button-collapse-left").sideNav("show");
    $(".button-collapse").sideNav();        // Menu nav for mobile
    $('.modal').modal();                    // Init modals

    // Inject the last third events in the footer

    // the api url used to fetch the events
    let ApiAgendaUrl = "http://127.0.0.1:8000/api/agenda/";
    // the selector of the dom element event container
    let NextEventSeletor = '#footer-next-events';
    // get the last events
    getLastEvents(ApiAgendaUrl).done(response => {
        if(response.count === 0){
            printAnyEvent(NextEventSeletor)
        }
        let events = response.results;
        let futureEvents = [];
        let i =0;
        // get the third first future events
        events.forEach(event=>{
           if(i <3 && eventIsFuture(event)){
               futureEvents.push(event);
               i++;
           }
        });
        // inject the events in the dom
        injectLastEvent(futureEvents,NextEventSeletor)
    }).fail(error => {
        alert('Impossible de récupérer les événements');
        console.log(error)
    });

});
/**
 * Return a boolean, which tell if the event is a future event
 * @param event operating event
 * @returns {boolean}
 */
function eventIsFuture(event){
    let now = new Date();
    let date = new Date(event.date);
    return now.getTime() < date.getTime();
}
/**
 * Used when any event is in a future
 * @param selector the selector used to manipulate the dom
 * @constructor
 */
function printAnyEvent(selector) {
    $(selector).html('<div class="center card-panel text-lighten-3 footer-next-event">    ' +
        '<a class="grey-text text-lighten-3 next-event-link" href="'+ url +'">' +
        'Pas d\'événement à venir pour le moment !&nbsp;<i class="fa fa-frown-o" aria-hidden="true"></i>' +
        '</a> ' +
        '       </div>')
}
/**
 * Return a promise of the http request
 * @returns {*}
 */
function getLastEvents(url) {
    return $.ajax(url)
}

/**
 * Inject in the dom, the events template
 * @param Events an array of the events
 * @param selector the selector of the dom element used
 */
function injectLastEvent(Events,selector) {
    let element = $(selector);
    Events.forEach(event=>{
        let oldContent = element.html();
        let newContent = oldContent + getEventTemplate(event.date,event.place,event.title,'agenda/'+event.id)
        element.html(newContent);
        console.log(newContent)
    })
}

/**
 * return the template of a footer event
 * @param date event date
 * @param place event place
 * @param name event name
 * @param url event url
 * @returns {string}
 */
function getEventTemplate(date,place,name,url) {
    return '<div class="center card-panel text-lighten-3 footer-next-event">    ' +
                '<a class="grey-text text-lighten-3 next-event-link" href="'+ url +'">' +
                ' ' + name + ' à '+ place +'' +
                '</a> ' +
    '       </div>';
}

