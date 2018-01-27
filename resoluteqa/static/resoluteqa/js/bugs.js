jQuery(document).ready(function($) {
    $('#bugsTable').DataTable( {
        paging: false
    });

    $('#submitEditBtn').on('click', function() {
        //submit bug update request
        location.reload(); //This can be on successful return from update request
    });

    $('#confirmDeleteBtn').on('click', function() {
        //submit delete request
        location.reload(); //This can be on successful return from delete request
    });

    $('#editBugModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); // Button that triggered the modal
        var bugId = button.data('bug');
        var bugTitle = button.data('title');
        var bugDescription = button.data('description');
        var bugSource = button.data('source');
        var bugUrl = button.data('url');

        // Update the modal's content
        var modal = $(this);
        modal.find('#modalEditTitle').text(bugId);
        modal.find('#editBugSourceControlIdInput').val(bugId);
        modal.find('#editBugTitleInput').val(bugTitle);
        modal.find('#editBugDescriptionInput').val(bugDescription);
        modal.find('#editBugSourceControlInput').val(bugSource);
        modal.find('#editBugUrlInput').val(bugUrl);
    });

    $('#confirmDeleteModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); // Button that triggered the modal
        var bugId = button.data('bug'); // Extract info from data-* attributes
        //var bugs = MAKE CALL TO GET BUGS // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).

        // Update the modal's content
        var modal = $(this);
        modal.find('#modalConfirmNumber').text(bugId);
    });
});
