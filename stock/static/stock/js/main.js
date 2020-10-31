var ctx = document.getElementById('myChart').getContext('2d');
var labels = document.getElementById('myLabels').innerText
var data = document.getElementById('myData').innerHTML
var labels_update = labels.replace("']", "")
var labels_update2 = labels_update.replace("['", "")
var labels_cleaned = labels_update2.split("', '")
var data_update = data.replace("]", "")
var data_update2 = data_update.replace("[", "")
var data_cleaned = data_update2.split(", ")

console.log(labels_cleaned)
console.log(data_cleaned)
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: labels_cleaned,
        datasets: [{
            label: 'Stock Prices',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: data_cleaned
        }]
    },

    // Configuration options go here
    options: {}
});
