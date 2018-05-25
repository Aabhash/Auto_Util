function createVizfunc() {
  //Dataset for visualization
  var data = {
    title: "{{Politician}}",
    categories: [
      {% for result in result_data %}
        [
          "{{result.dsc}}",
          [
            {{result.pos}}, {{result.neg}}
          ]
        ],
      {% endfor %}
    ]
  };
  var radius = parseFloat(document.getElementById("radius").value);
  var pieScaling = parseFloat(document.getElementById("pieScaling").value);
  var startPos = parseFloat(document.getElementById("startPos").value);
  var sort = (document.getElementById("sort").value).trim();
  var showCentralPie = parseInt(document.getElementById("showCentralPie").value);
  var showPieValues = parseInt(document.getElementById("showPieValues").value);
  <!-- console.log("radius: " + (parseFloat(document.getElementById("radius").value)+1)); -->
  <!-- console.log("pieScaling: " + document.getElementById("pieScaling").value); -->
  <!-- console.log(s); -->
  <!-- console.log(sort); -->
  //Call createViz with parameters to create the graph
  SentimentViz.createViz({
    svgId: "#sentiViz",
    data: data,
    radius: radius,
    pieScaling: pieScaling,
    startPos: startPos,
    sortOption: sort,
    showLegend: true,
    title: "Dimensional Sentiment on {{Politician}}",
    showCentralPie: showCentralPie,
    showPieValues: showPieValues
  });
};
