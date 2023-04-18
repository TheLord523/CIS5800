function deleteNote(noteId){
    fetch("/delete-note",{
        method: "POST",
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/"; //takes noteId that we passed and send a POST request to the delete note endpoint
    });
}