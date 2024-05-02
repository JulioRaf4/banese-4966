document.querySelector("#btn").addEventListener("click", () => {
    document.querySelector(".sidebar").classList.toggle("open");
    document.querySelector(".home-section").classList.toggle("open");
  });
  
  // Dropdown menu
  document.querySelectorAll(".sub-menu").forEach((submenu) => {
    submenu.parentElement.querySelector(".arrow").addEventListener("click", () => {
      submenu.classList.toggle("open");
    });
  });
  