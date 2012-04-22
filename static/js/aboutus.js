var d3HookId = '#d3';

$(document).ready(function () {
  buildDiagram(questions)
});


var buildDiagram = function (data) {
  var svg = d3.select(d3HookId).append('svg')
		  .attr('width', 940)
		  .attr('heght', 470)
		  .attr('transform', 'translate(-0.5, -0.5)');

};

