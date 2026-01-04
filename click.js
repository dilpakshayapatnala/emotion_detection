document.addEventListener("click", function (e) {
    if (e.target.tagName === "TEXTAREA" || e.target.tagName === "BUTTON") return;

    const colors = ["#ff00ff", "#00c6ff", "#7cff00", "#ff4ecd", "#ffd500"];

    for (let i = 0; i < 25; i++) {  // more particles
        const particle = document.createElement("span");
        particle.classList.add("click-particle");

        const size = Math.random() * 12 + 10; // larger size
        particle.style.width = size + "px";
        particle.style.height = size + "px";
        particle.style.background =
            colors[Math.floor(Math.random() * colors.length)];

        particle.style.left = e.clientX + "px";
        particle.style.top = e.clientY + "px";

        const x = (Math.random() - 0.5) * 250 + "px"; // bigger spread
        const y = (Math.random() - 0.5) * 250 + "px";

        particle.style.setProperty("--x", x);
        particle.style.setProperty("--y", y);

        document.body.appendChild(particle);

        setTimeout(() => { particle.remove(); }, 800);
    }
});
