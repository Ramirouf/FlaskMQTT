document.addEventListener("DOMContentLoaded", function () {
  const themeDropdownItems = document.querySelectorAll("[data-theme]");
  const html = document.documentElement;

  themeDropdownItems.forEach((item) => {
    item.addEventListener("click", function (e) {
      e.preventDefault();
      const selected = this.getAttribute("data-theme");
      html.setAttribute("data-bs-theme", selected);
      fetch(`/set_theme/${selected}`, { method: "POST" });
    });
  });
});
