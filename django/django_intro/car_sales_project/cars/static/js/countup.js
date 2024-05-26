// JavaScript for slider effect
let currentIndex = 0;
const images = document.querySelectorAll('.slider img');

function showSlide(index) {
    images.forEach((image, i) => {
        if (i === index) {
            image.classList.add('active');
        } else {
            image.classList.remove('active');
        }
    });
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % images.length;
    showSlide(currentIndex);
}

// Auto-advance slides every 3 seconds
setInterval(nextSlide, 3000);

// Show the first slide initially
showSlide(currentIndex);

// const activitiesCount = new CountUp('activities-count', 0, 1000);
// activitiesCount.start();


// const usersCount = new CountUp('users-count', 0, 5000);
// usersCount.start();


// const carsCount = new CountUp('cars-count', 0, 200);
// carsCount.start();


// const favoriteCarsCount = new CountUp('favorite-cars-count', 0, 50);
// favoriteCarsCount.start();
