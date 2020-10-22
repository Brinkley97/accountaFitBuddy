$("button.learnMoreButton").click(function() {
    $('html,body').animate(
      {
        scrollTop: $(".healthValueTitle").offset().top
      },
        'slow');
});
$("button.imInterestedButton").click(function() {
    $('html,body').animate(
      {
        scrollTop: $(".whyUseApp").offset().top
      },
        'slow');
});

AOS.init({
  duration: 1200,
})
