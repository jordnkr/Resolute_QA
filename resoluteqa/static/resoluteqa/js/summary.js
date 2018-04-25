jQuery(document).ready(function($) {
    var ctx = $('#overallSummaryChart');

    var myDoughnutChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [ctx.attr('data-failpercent'), ctx.attr('data-passpercent')],
                backgroundColor: ['#ea8383', '#83ea94']
            }],

            // These labels appear in the legend and in the tooltips when hovering different arcs
            labels: [
                'Failed',
                'Passed'
            ]
        },
        options: {
            maintainAspectRatio: false
        }
    });
    $('#suiteSummaryTable').DataTable( {
        paging: false,
        "order": [[ 7, "desc" ]]
    });

    $('.summaryRow').each(function() {
        var percent = $(this).attr('data-percentage');
        if (percent == 100) {
            $(this).addClass('green');
        } else if (percent >= 80) {
            $(this).addClass('yellow');
        } else if (percent >= 60) {
            $(this).addClass('orange');
        } else {
            $(this).addClass('red');
        }
    });

    $('#suiteSummaryTable').removeClass('hidden');
});
