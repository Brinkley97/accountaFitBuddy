//change color of thumbs up
(function() {
  const like = document.getElementById('like');
  like.addEventListener('click', function() {
    //toggle('like') go to main.css and see "#like.like"
    //it is the ".like" that triggering this
    like.classList.toggle('like');
  });
})();
