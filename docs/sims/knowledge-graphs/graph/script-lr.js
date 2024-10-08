// script.js

// Function to read the CSV file
function loadCSV(callback) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "graph-data.csv", true);
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

    lines.forEach(function(line) {
        var parts = line.split(',');
        var id = parts[0].trim();
        var label = parts[1].trim();
        var dependencies = parts[2] ? parts[2].trim().split('|') : [];

        nodes.push({ id: id, label: label });

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
    var options = {
        layout: {
            hierarchical: {
              direction: 'LR',  // Left to right
              sortMethod: 'directed',  // Sort nodes based on dependencies
              nodeSpacing: 50,  // Adjust spacing if needed
              levelSeparation: 50  // Adjust for horizontal space between levels
            }
          },
        nodes: {
            shape: 'dot',
            size: 10,
            font: {
                size: 14,
            },
        },
        edges: {
            arrows: 'to',
            smooth: true,
        },
        physics: true
    };

    var network = new vis.Network(container, data, options);
});
