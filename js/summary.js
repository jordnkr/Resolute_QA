jQuery(document).ready(function($) {
    var ctx = document.getElementById("overallSummaryChart");
    var myDoughnutChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [21, 79],
                backgroundColor: ['#e23636', '#25c452']
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
        paging: false
    });
});
