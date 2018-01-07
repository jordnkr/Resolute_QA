jQuery(document).ready(function($) {
    $('#bugsTable').DataTable( {
        paging: false
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
