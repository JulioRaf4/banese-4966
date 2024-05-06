let menuItems = document.querySelectorAll(".nav-list li");

menuItems.forEach(item => {
    item.addEventListener("click", (e) => {
      // Removendo a classe 'active' de todos os itens
      menuItems.forEach(el => el.classList.remove('active'));
  
      // Adicionando a classe 'active' ao item clicado
      item.classList.add('active');
  
      let subMenu = item.querySelector(".sub-menu");
      if (subMenu) {
        subMenu.classList.toggle("open");
      }
    });
  });
  

let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
let searchBtn = document.querySelector(".bx-search");

closeBtn.addEventListener("click", () => {
    sidebar.classList.toggle("open");
    menuBtnChange();
});

searchBtn.addEventListener("click", () => {
    sidebar.classList.toggle("open");
    menuBtnChange();
});

function menuBtnChange() {
    if (sidebar.classList.contains("open")) {
        closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");
    } else {
        closeBtn.classList.replace("bx-menu-alt-right", "bx-menu");
    }
}

