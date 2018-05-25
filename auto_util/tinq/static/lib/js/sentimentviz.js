// Dimension Sentiment Visualization Library version 3.1

var SentimentViz = (function () {
    'use strict';
    var viz={};

	function pie(containerId,radius,pieX,pieY,pieData,showPieValues){
					var dataset=pieData;
					var arc = d3.svg.arc()
									.innerRadius(0)
									.outerRadius(radius);
					
					var pie = d3.layout.pie();
					
					//Easy colors accessible via a 10-step ordinal scale
					//var color = d3.scale.category10();
					//blues ["#f1eef6","#bdc9e1","#74a9cf","#0570b0"]
					//greens ["#B2DFDC","#80CAC4"]
					var color = d3.scale.ordinal().range(["#f1eef6","#bdc9e1"]);

					//Create SVG element
					var svg = d3.select(containerId).append("g").attr("class","pie")
								.attr("transform", "translate(" + pieX + "," + pieY + ")");
								
					
					//Set up groups
					var arcs = svg.selectAll("g.arc")
								  .data(pie(dataset[1]))
								  .enter()
								  .append("g")
								  .attr("class", "arc");
					
					//Display pie values in tooltip if showPieValues is set to true
					if(!showPieValues){
						arcs.on("mouseover",function(d){
											d3.select("#tooltip")
											.style("left", d3.event.pageX + "px")
											.style("top", d3.event.pageY + "px")
											.style("opacity", 1)
											.select("#value")
											.text(d.value);
											
											d3.select(this).attr("class","arc-highlight");
											})
							.on("mouseout", function () {
									// Hide the tooltip
									d3.select("#tooltip")
										.style("opacity", 0);
									
									d3.select(this).attr("class","arc");
								});
					}
								  
					
					//Draw arc paths
					arcs.append("path")
						// .attr("fill", function(d, i) {
							// return color(i);
						// })
						.attr("id", function(d, i) {
							if(i==0){
								return "Pos";
							}
							else{
								return "Neg";
							}
						})
						.attr("d", arc)
						;
					
					//console.log(dataset);
					//Add Category Labels to pie-chart
					svg.append("text")
						.attr("text-anchor", function(d){
												if(showPieValues){
													if(dataset[3]){
														if(dataset[3][0]<0){
															return "end";
														}
														else{
															return "start";
														}
													}else{return "middle";}
												}else{return "middle";}
											})
						.text(dataset[0])
											//.text(Math.round(pieX).toString()+","+Math.round(pieY).toString() + ", " + Math.round(pieX+pieY))
						.attr("transform", function(d){
												if(showPieValues){
													if (dataset[3]){
														return "translate(" + dataset[3][0] + "," + dataset[3][1] + ")";
													}else{
														return "translate(0,0)";
													};
												}else {return "translate(0,0)";}
											});				
					
					//Labels
					if(showPieValues){
						arcs.append("text")
							.attr("transform", function(d) {
								return "translate(" + arc.centroid(d) + ")";
							})
							.attr("text-anchor", "middle")
							.text(function(d) {
								return d.value;
							});				
					}
					
				};
				
	function calcParams(dataset,circleR,circleX,circleY,startAngle,pieScaling,sortOption){
		var data=dataset,
			centerR=circleR,
			centerX=circleX,
			centerY=circleY,
			pieScaling=pieScaling,
			sortFlag = sortOption ;
			
		//Calculate the radius of each pie-chart based on the radius of the main central circle. 
		//The maximum radius of the pie-chart is always 90% of the central circle.
		var maxRadius=0;
		data.forEach(function(d){if (maxRadius<d3.sum(d[1])){maxRadius=d3.sum(d[1]);}});	
		var pieRadiusCalc=d3.scale.linear()
									.domain([0,maxRadius])
									.range([0,pieScaling*centerR]);
		
		var r=0, x, y, tempR=0, textX, textY;
		var angle=startAngle;
		
		data.forEach(
						function(d,i){
							r = pieRadiusCalc(d3.sum(d[1]));
							angle = angle + ((2*(r))/(centerR+r)+(2*(tempR))/(centerR+tempR))/2 + .025;
							if (sortFlag == 'ascending'){
								if(i<=8){
									x =  Math.cos(angle) * (centerR + r) + centerX;
									y =  Math.sin(angle) * (centerR + r) + centerY;
								}
								else{
									x = (Math.sqrt(i/1.4) * 0.4 * Math.cos(angle) * (centerR + r) + centerX);
									y = (Math.sqrt(i/1.4) * 0.4 * Math.sin(angle) * (centerR + r) + centerY);
								}	
							}
							else {
								if(i<=2){
									x =  Math.cos(angle) * (centerR + r) + centerX;
									y =  Math.sin(angle) * (centerR + r) + centerY;
								}
								else{
									x = (Math.sqrt(i/0.4) * 0.4 * Math.cos(angle) * (centerR + r) + centerX);
									y = (Math.sqrt(i/0.4) * 0.4 * Math.sin(angle) * (centerR + r) + centerY);
								}	
							}

							textX = Math.cos(angle) * (r);
							textY = Math.sin(angle) * (r) + 10;
							
							//Padding for textX and textY to avoid overlapping label with pie-charts
							if(textX>0){
								textX=textX+5;
							}
							else{
								textX=textX-5;
							}
							
							if(textY>0){
								textY=textY+5;
							}
							else{
								textY=textY-10;
							}
							
							tempR=r;
									
							data[i].push([r,x,y]);
							data[i].push([textX,textY]);
					});
		return data;
	};
			
    viz.createViz= function(args){
		var svgId = args.svgId,
			data=args.data,
			radius=args.radius,
			pieScaling=args.pieScaling,
			startPos=args.startPos,
			sortOption=args.sortOption,
			showLegend=args.showLegend,
			title=args.title,
			showCentralPie = args.showCentralPie,
			showPieValues = args.showPieValues;
					
				//Set defaults values for the graph option
				if(typeof(radius) == "undefined"){
					radius = 120;
				};
				
				if(typeof(pieScaling) == "undefined"){
					pieScaling = .75;
				};
				
				if(typeof(startPos) == "undefined"){
					startPos = 85;
				};
				
				if(!sortOption){
					sortOption = "descending";
				};
				
				if(!showLegend){
					showLegend = true;
				};
				
				var	centerX=radius+pieScaling*radius*2+150,
					centerY=radius+pieScaling*radius*2+75;
					
				var svgWidth=2*centerX+20+75,
					svgHeight=2*centerY+20+50;
							
				var getstartAngle=d3.scale.linear().domain([0,100]).range([0,2*Math.PI]);
				var svg;
				if(svgId){
					svg = d3.select(svgId)
								.attr("width", svgWidth)
								.attr("height", svgHeight)
								.style("border", "1px solid black");
					svg.selectAll("g").remove();
					//console.log("svgID passed");
				}else{
					svg = d3.select("body").append("svg")
								.attr("id","sentigraph")
								.attr("width", svgWidth)
								.attr("height", svgHeight)
								.style("border", "1px solid black");
					// console.log("svgID  not  passed");
					
					svgId="#sentigraph";
				};
				
				var circleElement=svg.append("g")
								// .attr("transform", "translate(" + centerX + "," + centerY + ")")
								.attr("class","circle-container");
				
				if(showCentralPie){
					//Create a pie-chart for the Central element
					var TotalPos=0, TotalNeg=0;
					data.categories.forEach(function(d){
													TotalPos=TotalPos+d[1][0];
													TotalNeg=TotalNeg+d[1][1];
												});
					//console.log(TotalPos);
					//console.log(TotalNeg);
					
					pie(".circle-container", radius, centerX, centerY, [data.title,[TotalPos,TotalNeg]],false);
				}else{
					//Create a circle for the Central element
					circleElement.append("circle")
								 .attr("r",radius)
								 .attr("transform", "translate(" + centerX + "," + centerY + ")");
								 
					circleElement.append("text")
								 .style("text-anchor", "middle")
								 .attr("transform", "translate(" + centerX + "," + centerY + ")")
								 .text(data.title);
				}
				//Calculate radius and (x,y) coordinates for each pie-chart for category
				var datatemp=calcParams(data.categories.sort(function(a, b){
																if (sortOption=="ascending")
																{
																	return d3.ascending(d3.sum(a[1]),d3.sum(b[1]));
																}else
																{
																	return d3.descending(d3.sum(a[1]),d3.sum(b[1]));
																}
															}),
										radius,
										centerX,
										centerY,
										getstartAngle(startPos),
										pieScaling,sortOption);
				console.log(datatemp);
				
				//Add a g element to add all the outer pie-charts
				d3.select(svgId).append("g").attr("class","pie-container");
				
				//Draw Pie-charts for each Category
				datatemp.forEach(function(d){pie(".pie-container",d[2][0],
												 d[2][1],
												 d[2][2] ,
												 d,showPieValues)});
												 
				//Add Title to the graph if available
				if(title){
					//console.log("test.");
					var titleContainer = svg.append("g").attr("class","graph-title");
					
					titleContainer.append("text").attr("text-anchor", "middle").attr("x",svgWidth/2).attr("y",25).text(title);
				};
				
				//Add Legend to the graph if available
				if(showLegend){
					var rectX = svgWidth - 115,
						rectY = 0;

					//Graph Legends
					var legendContainer= svg.append("g").attr("class","legendContainer");
					legendContainer.append("rect").attr("x",svgWidth-160).attr("y",rectY+10).attr("width",30).attr("height",30).attr("fill","#f1eef6");
					legendContainer.append("text").attr("x",svgWidth-110).attr("y",rectY+10+20).text("Positive");
					legendContainer.append("rect").attr("x",svgWidth-160).attr("y",rectY+30+20).attr("width",30).attr("height",30).attr("fill","#bdc9e1");
					legendContainer.append("text").attr("x",svgWidth-110).attr("y",rectY+30+20+20).text("Negative");
				};
    };

    return  viz;
}());