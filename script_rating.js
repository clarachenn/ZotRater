//javascript for ratings.html
-document.addEventListener('DOMContentLoaded', function () {
    var sliders = document.getElementsByClassName('slider');

    Array.prototype.forEach.call(sliders, function (slider) {
        var sliderHandle = slider.querySelector('.sliderHandle');
        var sliderBackground = slider.querySelector('.sliderBackground');
        var emoji = slider.nextElementSibling;

        sliderHandle.addEventListener('mousedown', function (event) {
            event.preventDefault();
            document.addEventListener('mousemove', moveSlider);
            document.addEventListener('mouseup', stopSlider);
        });
        /*
        function moveSlider(event) {
            var position = event.clientX - slider.getBoundingClientRect().left;
            var percentage = (position / slider.offsetWidth) * 100;
            percentage = Math.max(0, Math.min(100, percentage));

            sliderHandle.style.left = percentage + '%';
            sliderBackground.style.width = percentage + '%';

            var rating = Math.round((percentage / 100) * 5);
            updateEmoji(rating);
        }
        */
        function stopSlider() {
            document.removeEventListener('mousemove', moveSlider);
            document.removeEventListener('mouseup', stopSlider);
        }

        function updateEmoji(rating) {
            if (rating < 2.5) {
                emoji.innerHTML = '😢';
            } else if (rating >= 2.5 && rating <= 3.4) {
                emoji.innerHTML = '😐';
            } else {
                emoji.innerHTML = '😄';
            }
        }
    });
});