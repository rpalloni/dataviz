// Inside the ajax call:
// - url: request based on the URL provided
// - dataType: expecting a JSON object in return;
// - success: when the request completes, data are in response

function getData(callback) {
    $.ajax({
        type: "get",
        url: "/core/dataparser.py",
        dataType: "json",
        success: callback,
        error: function(request, status, error) {
            alert(status);
        }
    });
}


$(function() {

  getData(function(response) {
      // console.log(JSON.stringify(response));
      dataset = response;

      // var ow = dataset.map(function(d) {
      //   return {
      //     Ozone: d.ozone,
      //     Wind: d.wind
      //   }
      // });
      // console.log(ow);

      // Variables
      var body = d3.select('body')
      var margin = { top: 50, right: 50, bottom: 50, left: 50 }
      var h = 500 - margin.top - margin.bottom
      var w = 960 - margin.left - margin.right
      // Scales
      var colorScale = d3.scale.category20()
      var xScale = d3.scale.linear()
        .domain([
          d3.min([0,d3.min(dataset,function (d) { return d.wind  })]),
          d3.max([0,25])
          // console.log(d3.max([0,d3.max(dataset,function (d) { return d.wind  })]));  ?!?!?
          ])
        .range([0,w])
      var yScale = d3.scale.linear()
        .domain([
          d3.min([0,d3.min(dataset,function (d) { return d.ozone  })]),
          d3.max([0,d3.max(dataset,function (d) { return d.ozone  })])
          ])
        .range([h,0])
      // SVG
      var svg = body.append('svg')
          .attr('height',h + margin.top + margin.bottom)
          .attr('width',w + margin.left + margin.right)
        .append('g')
          .attr('transform','translate(' + margin.left + ',' + margin.top + ')')
      // X-axis
      var xAxis = d3.svg.axis()
        .scale(xScale)
        .ticks(5)
        .orient('bottom')
      // Y-axis
      var yAxis = d3.svg.axis()
        .scale(yScale)
        .ticks(5)
        .orient('left')
      // Circles
      var circles = svg.selectAll('circle')
          .data(dataset)
          .enter()
          .append('circle')
          .attr('cx',function (d) { return xScale(d.wind ) })
          .attr('cy',function (d) { return yScale(d.ozone ) })
          .attr('r','4')
          .attr('stroke','black')
          .attr('stroke-width',1)
          .attr('fill',function (d,i) { return colorScale(i) })

      // X-axis
      svg.append('g')
          .attr('class','axis')
          .attr('transform', 'translate(0,' + h + ')')
          .call(xAxis)
        .append('text') // X-axis Label
          .attr('class','label')
          .attr('y',-10)
          .attr('x',w)
          .attr('dy','.71em')
          .style('text-anchor','end')
          .text('Wind')
      // Y-axis
      svg.append('g')
          .attr('class', 'axis')
          .call(yAxis)
        .append('text') // y-axis Label
          .attr('class','label')
          .attr('transform','rotate(-90)')
          .attr('x',0)
          .attr('y',5)
          .attr('dy','.71em')
          .style('text-anchor','end')
          .text('Ozone')

    });

});
