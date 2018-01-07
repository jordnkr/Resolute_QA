jQuery(document).ready(function($) {
    $('#resultsTable').DataTable( {
        paging: false
    });

    $('.green').on('click', function() {
        $('#modalErrorFields').hide();
    });

    $('.red').on('click', function() {
        $('#modalErrorFields').show();
    });

    $('#testModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); // Button that triggered the modal
        var testName = button.data('testname'); // Extract info from data-* attributes
        var testClass = button.data('testclass');
        var namespace = button.data('namespace');
        //var bugs = MAKE CALL TO GET BUGS // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).

        // Update the modal's content
        var modal = $(this);
        modal.find('.modal-title').text(testName);
        modal.find('#modalTestClass').text(testClass);
        modal.find('#modalTestNamespace').text(namespace);
    });

    $('#resultModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); // Button that triggered the modal
        var testName = button.data('testname');
        var result = button.data('result');
        var machine = button.data('machine');
        var executionTime = button.data('execution');

        var badgeColor = "";
        if (result == 'Passed') {
            badgeColor = "green";
        } else if (result == 'Failed') {
            badgeColor = "red";
        } else {
            badgeColor = "yellow";
        }
        // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
        // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
        var modal = $(this);
        modal.find('.modal-title').text(testName);
        modal.find('#modalResult').text(result).removeClass().addClass(badgeColor + " customBadge");
        modal.find('#modalMachine').text(machine);
        modal.find('#modalTestExecutionTime').text(executionTime);
    });
});
