let problems = JSON.parse(document.getElementById("data").innerHTML);


(async function() {
    let labels = []; 
    let datasets = [];
    let D = {
        label: '數量',
        data:[],
        backgroundColor: "rgba(53, 162, 235, 0.5)",
    }
   
    for (e in problems) {
        labels.push(e);
    }
   

    Object.values(problems).forEach(element => {
        D.data.push(element);
    });
    
    datasets.push(D)
    let data = {
        labels,
        datasets
    }
    new Chart(
        document.getElementById('pic1'),
        {
            type: 'bar',
            data: data,
            options: {
            responsive: true,
            plugins: {
                legend: {
                position: 'top',
                },
                title: {
                display: true,
                text: '問題數值統計數量'
                }
            }
            },
        }
    );
   
})();
 