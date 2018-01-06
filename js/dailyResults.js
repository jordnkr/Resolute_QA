jQuery(document).ready(function($) {
    $('#resultsTable').DataTable( {
        paging: false
    });

    $('#testModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); // Button that triggered the modal
        var testName = button.data('testname'); // Extract info from data-* attributes
        var testClass = button.data('testclass');
        var namespace = button.data('namespace');
        //var bugs = MAKE CALL TO GET BUGS // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).

        // Update the modal's content
        var modal = $(this);
        modal.find('.modal-title').text('Test - ' + testName);
        modal.find('#modalTestClass').text(testClass);
        modal.find('#modalTestNamespace').text(namespace);
    });

    $('#resultModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); // Button that triggered the modal
        var testName = button.data('testname');
        var result = button.data('result');
        var executionTime = button.data('execution');
        // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
        // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
        var modal = $(this);
        modal.find('.modal-title').text('Test - ' + testName);
        modal.find('#modalResult').text(result);
        modal.find('#modalTestExecutionTime').text(executionTime);
    });
});
