document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.querySelector('input[type="file"]');
    const resultCard = document.getElementById('resultCard');
    const predictionText = document.getElementById('predictionText');
    const uploadedImage = document.getElementById('uploadedImage');
    const clearOutputButton = document.getElementById('clearOutput');
    const uploadNewButton = document.getElementById('uploadNew');

    fileInput.addEventListener('change', function() {
        const file = fileInput.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                uploadedImage.src = e.target.result; // Preview the uploaded image
            };
            reader.readAsDataURL(file);
        }
    });

    clearOutputButton.addEventListener('click', function() {
        // Clear the result card and reset the form
        document.getElementById('resultCard').style.display = 'none';
        document.querySelector('form').reset();
    });

    uploadNewButton.addEventListener('click', function() {
        // Reset the form for a new upload
        document.getElementById('resultCard').style.display = 'none';
        document.querySelector('form').reset();
    });
});
