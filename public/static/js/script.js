document.addEventListener("DOMContentLoaded", () => {
    const a=document.body.classList
        console.log(a);
    function togglee() {
        const a=document.body.classList
        console.log(a);
        
        document.body.classList.toggle("dark-theme");
        // document.body.classList.toggle("light-theme");
        console.log("helo")
    }
    document.querySelector('button').onclick=togglee
});
