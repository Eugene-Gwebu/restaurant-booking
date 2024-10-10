const editButtons = document.getElementsByClassName("btn-edit");
const bookingText = document.getElementById("id_body");
const confrimBookingForm = document.getElementById("confirmBookingForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let bookingId = e.target.getAttribute("booking_id");
    let bookingContent = document.getElementById(`booking${bookingId}`).innerText;
    bookingText.value = bookingContent;
    submitButton.innerText = "Update";
    confirmBookingForm.setAttribute("action", `edit_booking/${bookingId}`);
  });
}



/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let bookingId = e.target.getAttribute("booking_id");
    deleteConfirm.href = `cancel_booking/${bookingId}`;
    deleteModal.show();
  });
}

