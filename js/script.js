// ========================================
// Prestige Marketing - Interactive Scripts
// ========================================

// DOM Content Loaded
document.addEventListener('DOMContentLoaded', function() {
    initMobileMenu();
    initSmoothScroll();
    initScrollEffects();
    initFormValidation();
    initAnimations();
});

// ========================================
// Mobile Menu Toggle
// ========================================
function initMobileMenu() {
    const mobileMenuToggle = document.getElementById('mobileMenuToggle');
    const navLinks = document.getElementById('navLinks');

    if (mobileMenuToggle && navLinks) {
        mobileMenuToggle.addEventListener('click', function() {
            navLinks.classList.toggle('active');
            mobileMenuToggle.classList.toggle('active');
        });

        // Close menu when clicking on a link
        const links = navLinks.querySelectorAll('a');
        links.forEach(link => {
            link.addEventListener('click', function() {
                navLinks.classList.remove('active');
                mobileMenuToggle.classList.remove('active');
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!event.target.closest('nav')) {
                navLinks.classList.remove('active');
                mobileMenuToggle.classList.remove('active');
            }
        });
    }
}

// ========================================
// Smooth Scroll
// ========================================
function initSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            // Skip if it's just #
            if (href === '#') {
                e.preventDefault();
                return;
            }

            const target = document.querySelector(href);

            if (target) {
                e.preventDefault();
                const headerHeight = document.querySelector('header').offsetHeight;
                const targetPosition = target.offsetTop - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// ========================================
// Scroll Effects
// ========================================
function initScrollEffects() {
    const header = document.querySelector('header');

    // Header scroll effect
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // Fade in elements on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe elements
    const animateElements = document.querySelectorAll('.service-card, .feature-item, .industry-tag, .stat-item');
    animateElements.forEach(element => {
        observer.observe(element);
    });
}

// ========================================
// Form Validation & Submission
// ========================================
function initFormValidation() {
    const contactForm = document.getElementById('contactForm');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();

            // Get form values
            const name = document.getElementById('name').value.trim();
            const phone = document.getElementById('phone').value.trim();
            const industry = document.getElementById('industry').value;
            const message = document.getElementById('message').value.trim();

            // Validation
            if (!name) {
                alert('이름을 입력해주세요.');
                document.getElementById('name').focus();
                return false;
            }

            if (!phone) {
                alert('연락처를 입력해주세요.');
                document.getElementById('phone').focus();
                return false;
            }

            // Phone validation (Korean format)
            const phoneRegex = /^01[0-9]-?[0-9]{3,4}-?[0-9]{4}$/;
            if (!phoneRegex.test(phone.replace(/-/g, ''))) {
                alert('올바른 연락처 형식을 입력해주세요. (예: 010-0000-0000)');
                document.getElementById('phone').focus();
                return false;
            }

            if (!industry) {
                alert('업종을 선택해주세요.');
                document.getElementById('industry').focus();
                return false;
            }

            if (!message) {
                alert('문의 내용을 입력해주세요.');
                document.getElementById('message').focus();
                return false;
            }

            // If validation passes, submit form
            const submitButton = contactForm.querySelector('button[type="submit"]');
            const originalText = submitButton.textContent;

            submitButton.textContent = '전송 중...';
            submitButton.disabled = true;

            // Create FormData
            const formData = new FormData(contactForm);

            // Submit via AJAX
            fetch('contact_process.php', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('문의가 성공적으로 접수되었습니다.\n빠른 시일 내에 연락드리겠습니다.');
                    contactForm.reset();
                } else {
                    alert('문의 접수 중 오류가 발생했습니다.\n전화 또는 카카오톡으로 직접 문의해주세요.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('문의 접수 중 오류가 발생했습니다.\n전화 또는 카카오톡으로 직접 문의해주세요.\n\n카카오톡: pres00\n전화: 010-3966-7687');
            })
            .finally(() => {
                submitButton.textContent = originalText;
                submitButton.disabled = false;
            });

            return false;
        });

        // Phone number auto-formatting
        const phoneInput = document.getElementById('phone');
        if (phoneInput) {
            phoneInput.addEventListener('input', function(e) {
                let value = e.target.value.replace(/[^0-9]/g, '');

                if (value.length > 11) {
                    value = value.slice(0, 11);
                }

                if (value.length >= 4) {
                    if (value.length <= 7) {
                        value = value.slice(0, 3) + '-' + value.slice(3);
                    } else {
                        value = value.slice(0, 3) + '-' + value.slice(3, 7) + '-' + value.slice(7);
                    }
                }

                e.target.value = value;
            });
        }
    }
}

// ========================================
// Animations
// ========================================
function initAnimations() {
    // Add stagger animation to service cards
    const serviceCards = document.querySelectorAll('.service-card');
    serviceCards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
    });

    // Add stagger animation to feature items
    const featureItems = document.querySelectorAll('.feature-item');
    featureItems.forEach((item, index) => {
        item.style.animationDelay = `${index * 0.1}s`;
    });

    // Add stagger animation to industry tags
    const industryTags = document.querySelectorAll('.industry-tag');
    industryTags.forEach((tag, index) => {
        tag.style.animationDelay = `${index * 0.05}s`;
    });

    // Counter animation for stats
    const stats = document.querySelectorAll('.stat-item h3');
    const statsObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                statsObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    stats.forEach(stat => {
        statsObserver.observe(stat);
    });
}

// ========================================
// Counter Animation
// ========================================
function animateCounter(element) {
    const text = element.textContent;
    const hasPlus = text.includes('+');
    const hasPercent = text.includes('%');
    const hasSlash = text.includes('/');

    let endValue;
    let suffix = '';

    if (hasSlash) {
        // Handle "24/7" format
        return; // Skip animation for this format
    } else if (hasPercent) {
        endValue = parseInt(text);
        suffix = '%';
    } else if (hasPlus) {
        endValue = parseInt(text);
        suffix = '+';
    } else {
        endValue = parseInt(text);
    }

    if (isNaN(endValue)) return;

    const duration = 2000;
    const startTime = performance.now();

    function updateCounter(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);

        const currentValue = Math.floor(progress * endValue);
        element.textContent = currentValue + suffix;

        if (progress < 1) {
            requestAnimationFrame(updateCounter);
        } else {
            element.textContent = endValue + suffix;
        }
    }

    requestAnimationFrame(updateCounter);
}

// ========================================
// Utility Functions
// ========================================

// Debounce function
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Get viewport height
function getViewportHeight() {
    return Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0);
}

// Check if element is in viewport
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}
