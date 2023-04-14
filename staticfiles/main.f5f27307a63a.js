var rainInterval,
    isRaining = false,
    timeBetweenNumberGeneration = 170; //ms

function startRain() {
    rainInterval = setInterval(addLetter, timeBetweenNumberGeneration);
    isRaining = true;
}

function stopRain() {
    clearInterval(rainInterval);
    isRaining = false;
}

function addLetter() {
    var letterElem = $('<div class="letter">' + randomLetter() + '</div>');

    addElementDeath(letterElem);
    addCss(letterElem);

    $('body').append(letterElem);
}

function randomLetter() {
    var letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","أ", "ب", "ت", "ث", "ج", "ح", "خ", "د", "ذ", "ر", "ز", "ش", "س", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ك", "ل", "م", "ن", "ه", "و", "ي"];
    var letter = letters[Math.floor(Math.random() * letters.length)];
    return letter
}

function generateAnimations() {
    var clockwise = (Math.random() >= 0.5), // Random boolean
        fallTime = ((Math.random() * 2) + 4), // 0.3s to 2.3s
        turnTime = ((Math.random() * 2) + 8); // 2s to- 6s
    var fallAnimation = 'fall ' + fallTime + 's linear forwards',
        turnAnimation = clockwise ?
        'turn ' + turnTime + 's linear forwards infinite' :
        'turn-alt ' + turnTime + 's linear forwards infinite';
    return fallAnimation + ', ' + turnAnimation;
}

function addElementDeath(letterElem) {
    letterElem.prefixedEvent('AnimationEnd', function() {
        if (!elementInViewport(this)) {
            $(this).remove();
        }
    })
}

function addCss(letterElem, animations) {
    var startPosition = (Math.random() * 100), // A % of the screen width
        font = Math.floor((Math.random() * 50) + 35),
				animations = generateAnimations(); // 20px to 70px
    letterElem.css({
        '-webkit-animation': animations,
        animation: animations,
        position: "absolute",
        'font-size': font,
        left: startPosition + '%'
    });
}

// Space to stop and start rain
$('body').keyup(function(e) {
    if (e.keyCode === 32) {
        // Space bar
        if (isRaining) {
            stopRain();
        } else {
            startRain();
        }
    }
});

// Enables adding of the letter death
var vendors = ['webkit', 'o', 'ms', 'moz', ''];
var vendorCount = vendors.length;
// Prefixed event check
$.fn.prefixedEvent = function(type, callback) {
    for (var x = 0; x < vendorCount; ++x) {
        if (!vendors[x]) {
            type = type.toLowerCase();
        }

        el = (this instanceof jQuery ? this[0] : this);
        el.addEventListener(vendors[x] + type, callback, false);
    }
    return this;
};

// Test if element is in viewport
function elementInViewport(el) {
    if (el instanceof jQuery) {
        el = el[0];
    }
    var rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}




// logout
