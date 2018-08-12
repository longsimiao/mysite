jQuery(document).ready(function ( $ ) {
    var navLists = $(".nav-item");
    navLists.click(function activeNav() {
        var navIndex = navLists.index(this);
        for (var i=0; i <= navLists.length; i++) {
            if (navIndex === i){
                $(navLists[i]).attr("class", "active");
            } else {
                $(navLists[i]).removeClass("active");
            }
        }
    })
});

