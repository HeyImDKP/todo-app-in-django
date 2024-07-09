class Hamburger {
    hamburger;
    menu
    constructor(
        hamburgerClass,
        menuClass,
        headerClass
    ) {
        this.hamburger = document.querySelector(hamburgerClass);
        this.menu = document.querySelector(menuClass);
        this.header = document.querySelector(headerClass);

        this.hamburger.addEventListener("click", this.toggle_menu);
    }

    toggle_menu = () => {
        this.menu.classList.toggle("active");
        this.hamburger.classList.toggle("active");
        this.header.classList.toggle("active");
    }
}
