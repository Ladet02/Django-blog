// When the user scrolls the page, execute myFunction
window.onscroll = function() {
  myFunction();
};

function myFunction() {
  var winScroll = document.body.scrollTop || document.documentElement.scrollTop;

  // Get the total height of our post item and subtract the height of where we're at now. By the end, we should be at 100%.
  var height =
    document.getElementById("post").scrollHeight -
    document.documentElement.clientHeight;

  var scrolled = (winScroll / height) * 100;

  document.getElementById("myBar").style.width = scrolled + "%";
}
