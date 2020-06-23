d3.json("/tasks").then((data) => {
  var list = d3.select("#tasks");

  data.forEach((task) => {
    var li = list.append("li");
    li.text(task.description);
  });
});
