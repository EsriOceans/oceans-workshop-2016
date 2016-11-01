How does it perform? {data-background="images/bg-7.png"}
--------------------

  <h4>Multiplication of `N*K` Matricies</h4>
<div style="float: left; width: 50%">
  <canvas id="canvas" height="450" width="600"></canvas>
</div>
<div style="float: right; width: 50%">
  <div id="js-legend" class="chart-legend"></div>

  <div style="font-size: .6em; padding-top: 100px;">
  Python 2.7.8, ArcGIS 10.3.1, NumPy 1.9.3, 2.6Ghz Core i7</div>

</div>

<script>
    var barChartData = {
        labels : ["64","128","256"],
        datasets : [
            {
                fillColor : "rgba(220,220,220,0.5)",
                strokeColor : "rgba(220,220,220,0.8)",
                highlightFill: "rgba(220,220,220,0.75)",
                highlightStroke: "rgba(220,220,220,1)",
                data : [0.9728, 0.4149, 0.1769],
                label: "No MKL"
            },
            {
                fillColor : "rgba(151,187,205,0.5)",
                strokeColor : "rgba(151,187,205,0.8)",
                highlightFill : "rgba(151,187,205,0.75)",
                highlightStroke : "rgba(151,187,205,1)",
                data : [16.84, 19.01, 16.71],
                label: "MKL (1 core)"
            },
            {
                fillColor : "rgba(151,50,50,0.5)",
                strokeColor : "rgba(251,50,50,0.8)",
                highlightFill : "rgba(251,25,25,0.75)",
                highlightStroke : "rgba(251,25,25,1)",
                data : [47.92, 46.7, 54.59],
                label: "MKL (4 cores)"
            }

        ]
    }
    window.onload = function(){
        var ctx = document.getElementById("canvas").getContext("2d");
        window.myBar = new Chart(ctx).Bar(barChartData, {
            responsive : true
        });
        //then you just need to generate the legend
        //var legend = window.myBar.generateLegend();

        document.getElementById('js-legend').innerHTML = window.myBar.generateLegend();
    }
</script>
 
