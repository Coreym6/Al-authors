document.getElementById('csvFile').addEventListener('change', handleFileSelect, false);

function handleFileSelect(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function (e) {
        const contents = e.target.result;
        const lines = contents.split('\n');
        const headers = lines[0].split(',');

        const data = [];
        for (let i = 1; i < lines.length; i++) {
            const values = lines[i].split(',');
            if (values.length === headers.length) {
                const entry = {};
                for (let j = 0; j < headers.length; j++) {
                    entry[headers[j]] = values[j];
                }
                data.push(entry);
            }
        }

        const sortedData = data.sort((a, b) => {
            // Sort by the first column (you can modify this based on your requirements)
            return a[headers[0]].localeCompare(b[headers[0]]);
        });

        displayDataInTable(sortedData, headers);
    };
    reader.readAsText(file);
}

function displayDataInTable(data, headers) {
    const table = document.getElementById('csvTable');
    table.innerHTML = '';

    // Create table headers
    const headerRow = table.insertRow();
    headers.forEach(header => {
        const th = document.createElement('th');
        th.textContent = header;
        headerRow.appendChild(th);
    });

    // Populate table with data
    data.forEach(entry => {
        const row = table.insertRow();
        headers.forEach(header => {
            const cell = row.insertCell();
            cell.textContent = entry[header];
        });
    });
}




