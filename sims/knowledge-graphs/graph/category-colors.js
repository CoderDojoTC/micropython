// Function to read the CSV file
function loadCSV(callback) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "graph-data-2.csv", true); // Assuming the updated CSV file is called graph-data.csv
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && (xhr.status === 200 || xhr.status == 0)) {
            callback(xhr.responseText);
        }
    };
    xhr.send(null);
}

// Function to parse CSV data
function parseCSV(data) {
    var lines = data.trim().split('\n');
    var nodes = [];
    var edges = [];

    // Map CategoryID to colors
    var categoryColors = {
        1: 'red',
        2: 'orange',
        3: 'gold',
        4: 'green',
        5: 'cyan',
        6: 'blue',
        7: 'purple',
        8: 'pink',
        9: 'brown',
        10: 'gray',
        11: 'olive'
    };

    lines.forEach(function(line, index) {
        // Skip the header row
        if (index === 0) return;
        
        var parts = line.split(',');
        // concept id in first column
        var id = parts[0].trim();

        // the concept label is in the second column
        var label = parts[1].trim();

        // a pipe delimited list of dependant IDs is in the third colum
        var dependencies = parts[2] ? parts[2].trim().split('|') : [];

        // the category ID is in the 4th column
        var categoryID = parseInt(parts[3].trim());

        // Assign color based on CategoryID
        var color = categoryColors[categoryID] || 'black'; // Default to black if category is not found

        // create a new node with the right ID, label and color
        nodes.push({
            id: id,
            label: label,
            color: color // Set node color
        });

        // now for each dependancy, create an edge between ID and its dependant ID
        dependencies.forEach(function(depId) {
            depId = depId.trim();
            if (depId !== '') {
                edges.push({ from: id, to: depId });
            }
        });
    });

    return { nodes: nodes, edges: edges };
}

// Load the CSV and initialize the graph
loadCSV(function(data) {
    var parsedData = parseCSV(data);

    var nodes = new vis.DataSet(parsedData.nodes);
    var edges = new vis.DataSet(parsedData.edges);

    var container = document.getElementById('network');
    var data = {
        nodes: nodes,
        edges: edges,
    };
    // dot or circle?
    var options = {
        nodes: {
            shape: 'dot',
            size: 10,
            font: {
                size: 18,
            },
        },
        edges: {
            arrows: 'to',
            smooth: true,
        },
        physics: {
            stabilization: false,
        },
    };

    var network = new vis.Network(container, data, options);
});
