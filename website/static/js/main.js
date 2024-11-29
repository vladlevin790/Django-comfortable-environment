let slideIndex = 1;

document.addEventListener("DOMContentLoaded", function() {
    showDivs(slideIndex);

    document.querySelector('.next-slide').addEventListener('click', function() {
        plusDivs(1);
    });

    initializeBeforeAfterSlider(slideIndex);
});

function plusDivs(n) {
    showDivs(slideIndex += n);
}

function showDivs(n) {
    let i;
    const x = document.getElementsByClassName("post");
    if (n > x.length) {slideIndex = 1}
    if (n < 1) {slideIndex = x.length}
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    x[slideIndex-1].style.display = "block";
    initializeBeforeAfterSlider(slideIndex); 
}

function initializeBeforeAfterSlider(index) {
    const slider = document.querySelectorAll('.post')[index-1].querySelector('.before-after-slider');
    const before = slider.querySelector('.before-image');
    const beforeImage = before.getElementsByTagName('img')[0];
    const after = slider.querySelector('.after-image');
    const afterImage = after.getElementsByTagName('img')[0];
    const resizer = slider.querySelector('.resizer');

    let active = false;

    function resizeImages() {
        let width = slider.offsetWidth;
        let height = slider.offsetHeight;
        beforeImage.style.width = width + 'px';
        beforeImage.style.height = height + 'px';
        afterImage.style.width = width + 'px';
        afterImage.style.height = height + 'px';
    }

    resizeImages();

    window.addEventListener('resize', function() {
        resizeImages();
    });

    resizer.addEventListener('mousedown', function() {
        active = true;
        resizer.classList.add('resize');
    });

    document.body.addEventListener('mouseup', function() {
        active = false;
        resizer.classList.remove('resize');
    });

    document.body.addEventListener('mouseleave', function() {
        active = false;
        resizer.classList.remove('resize');
    });

    document.body.addEventListener('mousemove', function(e) {
        if (!active) return;
        let x = e.pageX - slider.getBoundingClientRect().left;
        slideIt(x);
        pauseEvent(e);
    });

    resizer.addEventListener('touchstart', function() {
        active = true;
        resizer.classList.add('resize');
    });

    document.body.addEventListener('touchend', function() {
        active = false;
        resizer.classList.remove('resize');
    });

    document.body.addEventListener('touchcancel', function() {
        active = false;
        resizer.classList.remove('resize');
    });

    document.body.addEventListener('touchmove', function(e) {
        if (!active) return;
        let x;
        for (let i = 0; i < e.changedTouches.length; i++) {
            x = e.changedTouches[i].pageX;
        }
        x -= slider.getBoundingClientRect().left;
        slideIt(x);
        pauseEvent(e);
    });

    function slideIt(x) {
        let transform = Math.max(0, (Math.min(x, slider.offsetWidth)));
        before.style.width = transform + "px";
        resizer.style.left = transform + 'px';
    }

    function pauseEvent(e) {
        if (e.stopPropagation) e.stopPropagation();
        if (e.preventDefault) e.preventDefault();
        e.cancelBubble = true;
        e.returnValue = false;
        return false;
    }
}
