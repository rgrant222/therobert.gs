var d3HookId = '#d3';
// var questions = [it's cool, it's been put here by the django template system!]

$(document).ready(buildDiagram);


var buildDiagram = function () {
	var svg = d3.select(d3HookId).append('svg')
		  .attr('width', 940)
		  .attr('heght', 320)
		  .attr('transform', 'translate(-0.5, -0.5)');

};

