var models = [
    { name: 'apple', image: 'img/apple.jpg' },
    { name: 'blue eyes', image: 'img/blue eyes.jpg' },
    { name: 'book', image: 'img/book.jpg' },
    { name: 'esra', image: 'img/esra.jpg' },
    { name: 'happy', image: 'img/happy.jpg' },
    { name: 'love', image: 'img/love.jpg' },
    { name: 'peace', image: 'img/peace.jpeg' },
    { name: 'sadness', image: 'img/sadness.jpg' }
];

var index = 0;
var slaytCount = models.length;
var interval;

var settings = {
    duration: 1000,
    random: false
};

init(settings);

document.querySelector('.fa-arrow-circle-left').addEventListener('click', function() {
    index--;
    showSlide(index);
    console.log(index);
});

document.querySelector('.fa-arrow-circle-right').addEventListener('click', function() {
    index++;
    showSlide(index);
    console.log(index);
});

document.querySelectorAll('.arrow').forEach(function(item) {
    item.addEventListener('mouseenter', function() {
        clearInterval(interval);
    });
});

document.querySelectorAll('.arrow').forEach(function(item) {
    item.addEventListener('mouseleave', function() {
        init(settings);
    });
});

function init(settings) {
    var prev;
    interval = setInterval(function() {
        if (settings.random) {
            do {
                index = Math.floor(Math.random() * slaytCount);
            } while (index == prev);
            prev = index;
        } else {
            if (index + 1 == slaytCount) index = -1;
            showSlide(index);
            index++;
        }
        showSlide(index);
    }, settings.duration);
}

function showSlide(i) {
    index = i;
    if (i < 0) index = slaytCount - 1;
    if (i >= slaytCount) index = 0;

    document.querySelector('.card-title').textContent = models[index].name;
    document.querySelector('.card-img-top').setAttribute('src', models[index].image);
}
