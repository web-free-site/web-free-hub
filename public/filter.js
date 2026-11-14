(function () {
  var input = document.getElementById("tool-filter");
  if (!input) return;

  var empty = document.getElementById("no-results");
  var sections = document.querySelectorAll("section.category");
  var tocLinks = document.querySelectorAll(".toc a[data-cat]");
  var form = input.form;

  function norm(s) {
    return String(s || "")
      .toLowerCase()
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "");
  }

  function apply() {
    var q = norm(input.value.trim());
    var shown = 0;
    sections.forEach(function (sec) {
      var n = 0;
      sec.querySelectorAll("li.tool").forEach(function (li) {
        var hay = li.getAttribute("data-search") || li.textContent;
        var match = !q || norm(hay).indexOf(q) !== -1;
        li.hidden = !match;
        if (match) n += 1;
      });
      sec.hidden = n === 0;
      shown += n;
      tocLinks.forEach(function (a) {
        if (a.getAttribute("data-cat") === sec.id) a.hidden = n === 0;
      });
    });
    if (empty) empty.hidden = shown > 0;
  }

  input.addEventListener("input", apply);
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      apply();
    });
  }

  if (input.value) apply();
})();
