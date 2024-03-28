let reports = JSON.parse(document.getElementById("data").innerHTML);
// console.log(reports[0])

// import Chart from 'chart.js/auto'

(async function() {
    let labels = []; 
    let datasets = [];

    let DP = {
        label: '舒張壓',
        data:[],
        backgroundColor: "rgba(53, 162, 235, 0.5)"
    }
    let SP = {
        label: '收縮壓',
        data:[],
        backgroundColor: "rgba(255, 99, 132, 0.5)"
    }
    let PL = {
        label: '脈搏',
        data:[],
        backgroundColor: "rgb(171,223,224)"
    }
    let GA = {
        label: '飯前葡萄糖',
        data:[],
        backgroundColor: "rgb(204,178,255)"
    }
    let H1 = {
        label: '血色素',
        data:[],
        backgroundColor: "rgb(255,207,163)"
    }
    let TC = {
        label: '總膽固醇',
        data:[],
        backgroundColor: "rgb(228,229,231)"
    }
    let TG = {
        label: '三酸甘油脂',
        data:[],
        backgroundColor: "rgb(255,178,193)"
    }
    let HC = {
        label: '高密度脂蛋白膽固醇',
        data:[],
        backgroundColor: "rgb(160,208,245)"
    }
    let LC = {
        label: '低密度脂蛋白膽固醇',
        data:[],
        backgroundColor: "rgb(255,230,174)"
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
                text: '血脂變化'
                }
            }
            },
        }
    );
})();
 