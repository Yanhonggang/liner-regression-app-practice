document.getElementById('prediction-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    let inputValues = document.getElementById('input-values').value.split(',').map(Number);
    
    fetch('http://localhost:5000/api/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ input: inputValues })
    })
    .then(response => response.json())
    .then(data => {
        let resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '<h2>Predictions:</h2>';
        let ul = document.createElement('ul');
        data.predictions.forEach(prediction => {
            let li = document.createElement('li');
            li.textContent = prediction;
            ul.appendChild(li);
        });
        resultsDiv.appendChild(ul);
    })
    .catch(error => console.error('Error:', error));
});
