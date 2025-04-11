document.getElementById('summarize-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    document.getElementById('loading').style.display = 'block';

    fetch('/summarize', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('loading').style.display = 'none';
        if (data.error) {
            document.getElementById('summary-result').innerText = 'Error: ' + data.error;
        } else {
            // Hide the form elements
            document.getElementById('summarize-form').style.display = 'none';
            // Display the summary result
            document.getElementById('summary-result').innerHTML = `
                <div id="summary-text">${data.summary}</div>
                <button onclick="copyToClipboard()">Copy</button>
                <a href="${data.audio_path}" download="summary.mp3">Download Audio</a>
            `;
        }
    })
    .catch(error => {
        document.getElementById('loading').style.display = 'none';
        console.error('Error:', error);
        document.getElementById('summary-result').innerText = 'An error occurred. Please try again.';
    });
});

function copyToClipboard() {
    const summaryText = document.getElementById('summary-text').innerText;
    navigator.clipboard.writeText(summaryText).then(() => {
        alert('Summary copied to clipboard!');
    }).catch(err => {
        console.error('Failed to copy text: ', err);
    });
}
