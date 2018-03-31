jQuery(document).ready(function($) {
    $('#resultsTable').DataTable( {
        paging: false
    });

    $('#suiteRunsSelect').change(function() {
        window.location.href = '../' + $(this).val() + '/dailyresults';
    });

    $('.green').on('click', function() {
        $('#modalErrorFields').hide();
        $.ajax({
            url: '../../individualresult/' + $(this).data('id'),
            type: 'get', // This is the default though, you don't actually need to always mention it
            success: function(data) {
                data = $.parseJSON(data.result)
                $('#modalConsoleOutput').text(data[0].fields.console_output);
            },
            failure: function(data) {
                alert('Got an error dude');
            }
        });
    });

    $('.red').on('click', function() {
        $('#modalErrorFields').show();
        $.ajax({
            url: '../../individualresult/' + $(this).data('id'),
            type: 'get', // This is the default though, you don't actually need to always mention it
            success: function(data) {
                var result = $.parseJSON(data.result);
                var errors = $.parseJSON(data.error_list);

                $('#modalConsoleOutput').text(result[0].fields.console_output);

                var errorString = "";
                var stackString = "";
                for (i = 0; i < errors.length; i++) {
                    errorString += errors[i].fields.error_message;
                    stackString += errors[i].fields.stack_trace;
                    if (i < errors.length - 1) {
                        errorString += '<br><br>';
                        stackString += '<br><br>';
                    }
                }
                $('#modalErrorOutput').html(errorString);
                $('#modalStackTrace').html(stackString);
            },
            failure: function(data) {
                alert('There was an error');
            }
        });
    });

    $('#selectTestsBtn').on('click', function() {
        $('#selectTestsBtnContainer').hide();
        $('#addBugsBtnContainer').show();
        $('.testCheckbox').show();
    });

    $('#plusBugBtn').on('click', function() {
        $('#addBugSourceControlIdInput').val('');
        $('#addBugTitleInput').val('');
        $('#addBugDescriptionInput').val('');
        $('#addBugUrlInput').val('');
    });

    $('#addBugsCancelBtn').on('click', function() {
        $('.testCheckbox').hide();
        $('#addBugsBtnContainer').hide();
        $('#selectTestsBtnContainer').show();
    });

    $('#submitAddBugBtn').on('click', function() {
        var selected = [];

        //fix this
        $('input:checked').each(function() {
            selected.push($(this).data('testid'));
        });

        $('#addBugSourceControlIdInput').val();
        $('#addBugTitleInput').val();
        $('#addBugDescriptionInput').val();
        $('#addBugSourceControlInput').val();
        $('#addBugUrlInput').val();

        // submit request with selected checkboxes
    });

    $('#testAddSingleBugBtn').on('click', function() {
        $('#testAddBugBtnContainer').hide();
        $('#testBugsTableContainer').hide();
        $('#testBugDecisionBtnContainer').show();
        $('#addSingleBugFormContainer').show();
    });

    $('#testBugDecisionBtnContainer button').on('click', function() {
        $('#testBugDecisionBtnContainer').hide();
        $('#addSingleBugFormContainer').hide();
        $('#testAddBugBtnContainer').show();
        $('#testBugsTableContainer').show();
    });

    $('#testModal').on('show.bs.modal', function (event) {
        $('#testBugDecisionBtnContainer').hide();
        $('#addSingleBugFormContainer').hide();
        $('#testAddBugBtnContainer').show();
        $('#testBugsTableContainer').show();

        var button = $(event.relatedTarget); // Button that triggered the modal
        var testName = button.data('testname'); // Extract info from data-* attributes
        var testClass = button.data('testclass');
        var namespace = button.data('namespace');
        //var bugs = MAKE CALL TO GET BUGS // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).

        $.ajax({
            url: '../../test/' + button.data('testid') + '/bugs',
            type: 'get', // This is the default though, you don't actually need to always mention it
            success: function(data) {
                var bugs = $.parseJSON(data.bug_list);

                var bugString = "";
                for (i = 0; i < bugs.length; i++) {
                    bugString += '<tr><td><a href="' + bugs[i].fields.url + '">' + bugs[i].fields.source_control_id + '</a></td><td>' + bugs[i].fields.title + '</td><td><button type="button" class="close" data-bugid="' + bugs[i].pk + '"><span aria-hidden="true">&times;</span></button></td></tr>'
                }
                $('#modalBugTableBody').html(bugString);
            },
            failure: function(data) {
                alert('There was an error');
            }
        });

        // Update the modal's content
        var modal = $(this);
        modal.find('.modal-title').text(testName);
        modal.find('#modalTestClass').text(testClass);
        modal.find('#modalTestNamespace').text(namespace);

        // Clear create bug inputs on open
        modal.find('#createSingleBugSourceControlIdInput').val('');
        modal.find('#createSingleBugTitleInput').val('');
        modal.find('#createSingleBugDescriptionInput').val('');
        modal.find('#createSingleBugUrlInput').val('');
    });

    $('#addBugToTestsModal').on('show.bs.modal', function (event) {

        // Clear input fields on open
        var modal = $(this);
        modal.find('#createBugsSourceControlIdInput').val('');
        modal.find('#createBugsTitleInput').val('');
        modal.find('#createBugsDescriptionInput').val('');
        modal.find('#createBugsUrlInput').val('');
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
