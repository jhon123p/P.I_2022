class MobileNavbar{
    constructor(mobileMenu, navList, navLinks){
        this.mobileMenu = document.querySelector(mobileMenu);
        this.navList = document.querySelector(navList);
        this.navLinks = document.querySelectorAll(navLinks);
        this.activeClass = "active";

        this.handleClick = this.handleClick.bind(this);
    }

    handleClick() {  
        this.navList.classList.toggle(this.activeClass);
        this.mobileMenu.classList.toggle(this.activeClass);
        }

    addClickEvent(){
        this.mobileMenu.addEventListener("click", this.handleClick);
     }
    init(){
        if(this.mobileMenu){
            this.addClickEvent();
     }
     return this;
    }

}
const mobileNavbar = new MobileNavbar(
        ".mobile-menu",
        ".sidebar",
        ".sidebar li",
);
mobileNavbar.init();

const inp=document.getElementById("user");

inp.addEventListener("input", () =>{
    inp.value = inp.value.toUpperCase();
});

/*teste de formulario*/
