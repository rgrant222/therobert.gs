var data = undefined;
var data = undefined;
var d3HookId = '#d3_start';

$(document).ready(function () {
  d3.json('/aboutus/data/', buildPage);
});


var buildPage = function (responseData) {
  console.log("Displaying error, aha!");
  data = responseData;
  
  var sections = d3.select(d3HookId).selectAll('div.section')
      .data(responseData.sections);
  
  sections.enter().append('div')
      .classed('section', true)
      .classed('row', true)
    .append('div')
      .classed('span12', true)
      .classed('question', true)
    .append('div')
      .classed('title', true);

  var titles = sections.selectAll('.title');
  titles.append('h1')
      .text(function (d) { return d.question; });
  titles.append('p')
      .text(function (d) { return d.content; });
};

