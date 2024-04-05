let reports = JSON.parse(document.getElementById("data").innerHTML);
reports = reports.sort((a, b) => a.report_year - b.report_year);

// import Chart from 'chart.js/auto'

(async function() {
    let labels = []; 
    let datasets = [];

    let DP = {
        label: '舒張壓',
        data:[],
        type: 'line',
        backgroundColor: "rgba(53, 162, 235, 0.5)",
        borderColor: "rgba(53, 162, 235, 1)",
        pointStyle: 'circle',
        pointRadius: 10,
        pointHoverRadius: 15
    }
    let SP = {
        label: '收縮壓',
        data:[],
        type: 'line',
        backgroundColor: "rgba(255, 99, 132, 0.5)",
        borderColor:  "rgba(255, 99, 132, 1)",
        pointStyle: 'circle',
        pointRadius: 10,
        pointHoverRadius: 15
    }
    let PL = {
        label: '脈搏',
        data:[],
        backgroundColor: "rgb(171,223,224)"
    }
    let GA = {
        label: '飯前葡萄糖',
        data:[],
        type: 'line',
        backgroundColor: "rgb(204,178,255)",
        borderColor: "rgb(204,178,255)",
        pointStyle: 'circle',
        pointRadius: 10,
        pointHoverRadius: 15
    }
    let H1 = {
        label: '糖化血色素',
        data:[],
        type: 'line',
        backgroundColor: "rgb(255,207,163)",
        borderColor: "rgb(255,207,163)",
        pointStyle: 'circle',
        pointRadius: 10,
        pointHoverRadius: 15
    }
    let TC = {
        label: '總膽固醇',
        data:[],
        backgroundColor: "rgb(228,229,231)",
        borderColor: "rgb(228,229,231)",
        pointStyle: 'circle',
        pointRadius: 10,
        pointHoverRadius: 15
    }
    let TG = {
        label: '三酸甘油脂',
        data:[],
        backgroundColor: "rgb(255,178,193)",
        borderColor: "rgb(255,178,193)",
        pointStyle: 'circle',
        pointRadius: 10,
        pointHoverRadius: 15
    }
    let HC = {
        label: '高密度脂蛋白膽固醇',
        data:[],
        backgroundColor: "rgb(160,208,245)",
        borderColor: "rgb(160,208,245)",
        pointStyle: 'circle',
        pointRadius: 10,
        pointHoverRadius: 15
    }
    let LC = {
        label: '低密度脂蛋白膽固醇',
        data:[],
        backgroundColor: "rgb(255,230,174)",
        borderColor: "rgb(255,230,174)",
        pointStyle: 'circle',
        pointRadius: 10,
        pointHoverRadius: 15
    }

    reports.forEach(element => {
        labels.push(element.report_year)
        DP.data.push(element.diastolic_pressure)
        SP.data.push(element.systolic_pressure)
        PL.data.push(element.pulse)
        GA.data.push(element.glucose_ac)
        H1.data.push(element.hba1c)
        TC.data.push(element.t_cho)
        TG.data.push(element.tg)
        HC.data.push(element.hdl_c)
        LC.data.push(element.ldl_c)
        
    });
    datasets.push(DP, SP)
    let data = {
        labels,
        datasets
    }
    new Chart(
        document.getElementById('pic1'),
        {
            type: 'line',
            data: data,
            options: {
            responsive: true,
            plugins: {
                legend: {
                position: 'top',
                },
                title: {
                display: true,
                text: '血壓變化'
                }
            }
            },
        }
    );
    datasets = []
    datasets.push(GA, H1)
    data = {
        labels,
        datasets
    }  
    new Chart(
        document.getElementById('pic2'),
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
                text: '血糖變化'
                }
            }
            },
        }
    );

    datasets = []
    datasets.push(TC, TG, HC, LC)
    data = {
        labels,
        datasets
    }  
    new Chart(
        document.getElementById('pic3'),
        {
            type: 'line',
            data: data,
            options: {
            responsive: true,
            plugins: {
                legend: {
                position: 'top',
                },
                title: {
                display: true,
                text: '血脂變化'
                }
            }
            },
        }
    );
})();
 