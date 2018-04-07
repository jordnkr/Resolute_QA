jQuery(document).ready(function($) {
    $('#bugsTable').DataTable( {
        paging: false
    });

    $('#submitEditBtn').on('click', function() {
        //submit bug update request
        location.reload(); //This can be on successful return from update request
    });

    $('#confirmDeleteBtn').on('click', function() {

        $.ajax({
            url: '../../bug/' + $('#modalConfirmNumber').data('id') + '/delete',
            type: 'DELETE', // This is the default though, you don't actually need to always mention it
            dataType:  'json',
            success: function(data) {
                location.reload(); //This can be on successful return from delete request
            },
            error: function(data) {
                alert('Got an error dude');
            }
        });
    });

    $('#editBugModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); // Button that triggered the modal
        var bugId = button.data('id');
        var bugSourceControlId = button.data('bug');
        var bugTitle = button.data('title');
        var bugSource = button.data('source');
        var bugUrl = button.data('url');

        // Update the modal's content
        var modal = $(this);
        modal.find('#modalEditTitle').text(bugSourceControlId);
        modal.find('#modalEditTitle').attr('data-id', bugId);
        modal.find('#editBugSourceControlIdInput').val(bugSourceControlId);
        modal.find('#editBugTitleInput').val(bugTitle);
        modal.find('#editBugSourceControlInput').val(bugSource);
        modal.find('#editBugUrlInput').val(bugUrl);
    });

    $('#confirmDeleteModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); // Button that triggered the modal
        var bugId = button.data('id');
        var bugSourceControlId = button.data('bug'); // Extract info from data-* attributes
        //var bugs = MAKE CALL TO GET BUGS // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).

        // Update the modal's content
        var modal = $(this);
        modal.find('#modalConfirmNumber').text(bugSourceControlId);
        modal.find('#modalConfirmNumber').attr('data-id', bugId);
    });
});
