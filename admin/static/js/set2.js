                var chartData = [
                {
                    "date": "2023-05-01",
                    "distance": 7,
                    "duration": 14
                },
                {
                    "date": "2023-05-02",
                    "distance": 21,
                    "duration": 12
                },
                {
                    "date": "2023-05-03",
                    "distance": 3,
                    "duration": 12
                },
                {
                    "date": "2023-05-04",
                    "distance": 5,
                    "duration": 19
                },
                {
                    "date": "2023-05-05",
                    "distance": 14,
                    "duration": 15
                },
                {
                    "date": "2023-05-06",
                    "distance": 6,
                    "duration": 14
                },
                {
                    "date": "2023-05-07",
                    "distance": 8,
                    "duration": 14
                },
                {
                    "date": "2023-05-08",
                    "distance": 8,
                    "duration": 13
                },
                {
                    "date": "2023-05-09",
                    "distance": 18,
                    "duration": 12
                },
                {
                    "date": "2023-05-10",
                    "distance": 9,
                    "duration": 14
                },
                {
                    "date": "2023-05-11",
                    "distance": 3,
                    "duration": 18
                },
                {
                    "date": "2023-05-12",
                    "distance": 22,
                    "duration": 18
                },
                {
                    "date": "2023-05-13",
                },
                {
                    "date": "2023-05-14",
                },
                {
                    "date": "2023-05-15"
                },
                {
                    "date": "2023-05-16"
                },
                {
                    "date": "2023-05-17"
                },
                {
                    "date": "2023-05-18"
                },
                {
                    "date": "2023-05-19"
                },
                {
                    "date": "2023-05-20"
                },
                {
                    "date": "2023-05-21"
                },
                {
                    "date": "2023-05-22"
                },
                {
                    "date": "2023-05-23"
                },
                {
                    "date": "2023-05-24"
                },
                {
                    "date": "2023-05-25"
                },
                {
                    "date": "2023-05-26"
                },
                {
                    "date": "2023-05-27"
                },
                {
                    "date": "2023-05-28"
                },
                {
                    "date": "2023-05-29"
                },
                {
                    "date": "2023-05-30"
                },
                {
                    "date": "2023-05-31"
                }
            ];
            var chart = AmCharts.makeChart("chartdiv", {
            type: "serial",
            theme: "dark",
            dataDateFormat: "YYYY-MM-DD",
            dataProvider: chartData,
            addClassNames: true,
            startDuration: 1,
            color: "#000000",
            marginLeft: 0,
            categoryField: "date",
            categoryAxis: {
                parseDates: true,
                minPeriod: "DD",
                autoGridCount: false,
                gridCount: 50,
                gridAlpha: 0.1,
                gridColor: "#000000",
                axisColor: "#555555",

                dateFormats: [{
                    period: 'DD',
                    format: 'DD'
                }, {
                    period: 'WW',
                    format: 'MMM DD'
                }, {
                    period: 'MM',
                    format: 'MMM'
                }, {
                    period: 'YYYY',
                    format: 'YYYY'
                }]
            },
            valueAxes: [{
                id: "a1",
                title: "Время работы",
                gridAlpha: 0,
                axisAlpha: 0
            }],
            graphs: [{
                id: "g1",
                valueField:  "distance",
                title:  "Время работы (сумма)",
                type:  "column",
                fillAlphas:  0.9,
                valueAxis:  "a1",
                balloonText:  "[[value]] ч.",
                legendValueText:  "[[value]] ч.",
                lineColor: "#232227",
                alphaField: "alpha",
            },{
                id: "g3",
                title: "Пик активности (время)",
                valueField: "duration",
                type: "line",
                valueAxis: "a3",
                lineColor: "#f05833",
                balloonText: "[[value]]:00",
                lineThickness: 1,
                legendValueText: "[[value]]:00",
                bullet: "square",
                bulletBorderColor: "#ff5755",
                bulletBorderThickness: 1,
                bulletBorderAlpha: 1,
                dashLengthField: "dashLength",
                animationPlayed: true
            }],

            legend: {
                bulletType: "round",
                equalWidths: false,
                valueWidth: 120,
                useGraphSettings: true,
                color: "#-+"
            }
            });