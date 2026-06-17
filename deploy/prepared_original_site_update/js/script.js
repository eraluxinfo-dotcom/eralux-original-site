$(document).ready(function(){
    $('input[type="tel"]').mask("+38 (099) 999-99-99");

    $(".js-range-slider_square").ionRangeSlider({
        min: 1,
        max: 150,
        from: 1,
        to: 150,
        grid: false,
        hide_min_max: true,
        onChange: function onChange(data) {
            calc();
        }            
    });
	
    $(".js-range-slider_lights").ionRangeSlider({
        min: 0,
        max: 30,
        from: 0,
        to: 30,
        grid: false,
        hide_min_max: true,
        onChange: function onChange(data) {
            calc();
        }  
    });

    $(".js-range-slider_perimeter").ionRangeSlider({
        min: 1,
        max: 100,
        from: 1,
        to: 100,
        grid: false,
        hide_min_max: true,
        onChange: function onChange(data) {
            calc();
        }  
    });

    var slider;
	slider = new Swiper('.new_portfolio .swiper', {
		loop: true,
		slidesPerView: 1,
		centeredSlides: true,
		spaceBetween: 0,
		autoplay: {
			delay: 2000
		},
		navigation: {
			nextEl: '.new_portfolio .portfolio__next',
			prevEl: '.new_portfolio .portfolio__prev'
		},
		breakpoints: {
			550: {
				slidesPerView: 2,
			},
			768: {
				slidesPerView: 3,
			},	
			1000: {
				slidesPerView: 4,
			},				
			1200: {
				slidesPerView: 6,
			},
			1500: {
				slidesPerView: 7,
			},
			1500: {
				slidesPerView: 7,
			}
		}
	});

    var slider1;
	slider1 = new Swiper('.new_catalog .swiper', {
		loop: true,
		slidesPerView: 1,
		centeredSlides: true,
		spaceBetween: 0,
		autoplay: {
			delay: 2000
		},
		navigation: {
			nextEl: '.new_catalog .portfolio__next',
			prevEl: '.new_catalog .portfolio__prev'
		},
		breakpoints: {
			550: {
				slidesPerView: 2,
			},
			768: {
				slidesPerView: 3,
			},	
			1000: {
				slidesPerView: 4,
			},				
			1200: {
				slidesPerView: 6,
			},
			1500: {
				slidesPerView: 7,
			},
			1500: {
				slidesPerView: 7,
			}
		}
	});

    var slider2;
	slider2 = new Swiper('.new_colors .swiper', {
		loop: true,
		slidesPerView: 1,
		centeredSlides: true,
		spaceBetween: 0,
		autoplay: {
			delay: 2000
		},
		navigation: {
			nextEl: '.new_colors .portfolio__next',
			prevEl: '.new_colors .portfolio__prev'
		},
		breakpoints: {
			550: {
				slidesPerView: 2,
			},
			768: {
				slidesPerView: 3,
			},	
			1000: {
				slidesPerView: 4,
			},				
			1200: {
				slidesPerView: 6,
			},
			1500: {
				slidesPerView: 7,
			},
			1500: {
				slidesPerView: 7,
			}
		}
	});

    var slider3;
	slider3 = new Swiper('.new_portfolio1 .swiper', {
		loop: true,
		slidesPerView: 1,
		centeredSlides: true,
		spaceBetween: 0,
		autoplay: {
			delay: 2000
		},
		navigation: {
			nextEl: '.new_portfolio1 .portfolio__next',
			prevEl: '.new_portfolio1 .portfolio__prev'
		},
		breakpoints: {
			550: {
				slidesPerView: 2,
			},
			768: {
				slidesPerView: 3,
			},	
			1000: {
				slidesPerView: 4,
			},				
			1200: {
				slidesPerView: 6,
			},
			1500: {
				slidesPerView: 7,
			},
			1500: {
				slidesPerView: 7,
			}
		}
	});


	$('.to-form').click(function(e){
		e.preventDefault();

		$([document.documentElement, document.body]).animate({
			scrollTop: $(".footer-offer").offset().top
		}, 1000);
	});
	
	$('form').submit(function(e){
		e.preventDefault();

		var form = $(this);
		var data = form.serialize();

		$.ajax({
			url: "/order.php", 
			type: "POST",
			data: {form_data: data},
			success: function(){
				document.location.href = "/thanks.html";
			}
		});
	});
});

function calc(){
	var square = parseInt($(".js-range-slider_square").val());
	var perimeter = parseInt($(".js-range-slider_perimeter").val());
	var lights = parseInt($(".js-range-slider_lights").val());
	
	var sum = square * 165 + lights * 90 + perimeter * 30;
	$('.calc__total').find('span').text(sum);
}

function pageWidth() {
  return window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
}
