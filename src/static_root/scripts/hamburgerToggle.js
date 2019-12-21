function hamburgerToggled() {
  const checkbox = document.getElementById("hamburgerToggle");

  if (checkbox.checked) {
    // Checkbox is checked..
    let menu = document.getElementById("header_menu");
    menu.style.top = "55px";
  } else if (!checkbox.checked) {
    // Checkbox is not checked..
    let menu = document.getElementById("header_menu");
    menu.style.top = "-500px";
  }
}
