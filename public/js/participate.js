// TODO : Call this file only for particpate.html

$(document).ready(function() {
    $('.datepicker').pickadate({
        selectMonths: true,         // Creates a dropdown to control month
        selectYears: 200,     // Creates a dropdown of 15 years to control year
        clear: '',                  // Label button "clear"
        close: 'Valider',           // Label button "close"
        today: '',                  // Label button "today"
        format: 'dd/mm/yyyy',
        labelMonthNext: 'Mes siguiente',
        labelMonthPrev: 'Mes anterior',
        labelMonthSelect: 'Sélection du mois',
        labelYearSelect: 'Sélection de l\'année',
        monthsFull: [ 'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Jun', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre' ],
        monthsShort: [ 'Jan', 'Fev', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aou', 'Sep', 'Oct', 'Nov', 'Dec' ],
		weekdaysFull: [ 'Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi' ],
		weekdaysShort: [ 'Dim', 'Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam' ],
		weekdaysLetter: [ 'D', 'S', 'T', 'Q', 'Q', 'S', 'S' ]
    });

});
